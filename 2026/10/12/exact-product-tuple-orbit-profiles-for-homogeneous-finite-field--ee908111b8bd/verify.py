from itertools import product
from fractions import Fraction


def gauss(n,r,q):
    if r<0 or r>n: return 0
    if r>n-r: r=n-r
    z=1
    for i in range(1,r+1):
        z=z*(q**(n-r+i)-1)//(q**i-1)
    return z

def rref(mat,q,ncols):
    a=[list(row) for row in mat if any(x%q for x in row)]
    row=0
    for col in range(ncols):
        piv=next((i for i in range(row,len(a)) if a[i][col]%q),None)
        if piv is None: continue
        a[row],a[piv]=a[piv],a[row]
        inv=pow(a[row][col]%q,-1,q)
        a[row]=[(x*inv)%q for x in a[row]]
        for i in range(len(a)):
            if i!=row and a[i][col]%q:
                c=a[i][col]%q
                a[i]=[(x-c*y)%q for x,y in zip(a[i],a[row])]
        row+=1
        if row==len(a): break
    a=[tuple(x%q for x in row) for row in a if any(x%q for x in row)]
    a.sort(key=lambda v: next(i for i,x in enumerate(v) if x))
    return tuple(a)

def enumerate_subspaces(q,n):
    # Generate spans of all ordered lists of at most n vectors; tiny cases only.
    vecs=list(product(range(q), repeat=n))
    spaces={()}
    for basis_len in range(1,n+1):
        # iterative closure: adjoining a vector to every space is enough
        new=set(spaces)
        for S in list(spaces):
            for v in vecs:
                R=rref(list(S)+[v],q,n)
                new.add(R)
        spaces=new
    return spaces

def matrix_counts(q,r):
    gen=sym=alt=0
    for xs in product(range(q), repeat=r*r):
        M=[xs[i*r:(i+1)*r] for i in range(r)]
        gen+=1
        if all(M[i][j]==M[j][i] for i in range(r) for j in range(r)):
            sym+=1
        if all(M[i][i]==0 for i in range(r)) and all((M[i][j]+M[j][i])%q==0 for i in range(r) for j in range(r)):
            alt+=1
    return gen,sym,alt

def profiles(q,n):
    B=sum(gauss(n,r,q)*q**(r*r) for r in range(n+1))
    S=sum(gauss(n,r,q)*q**(r*(r+1)//2) for r in range(n+1))
    A=sum(gauss(n,r,q)*q**(r*(r-1)//2) for r in range(n+1))
    return B,S,A

def main():
    checks=0
    for q,nmax in [(2,4),(3,3)]:
        for n in range(nmax+1):
            spaces=enumerate_subspaces(q,n)
            bydim={d:0 for d in range(n+1)}
            for S in spaces: bydim[len(S)]+=1
            for d in range(n+1):
                assert bydim[d]==gauss(n,d,q)
                checks+=1
    for q,rmax in [(2,3),(3,2)]:
        for r in range(rmax+1):
            g,s,a=matrix_counts(q,r)
            assert g==q**(r*r)
            assert s==q**(r*(r+1)//2)
            assert a==q**(r*(r-1)//2)
            checks+=3
    for q in (2,3,5,7):
        for n in range(0,9):
            B,S,A=profiles(q,n)
            Sprod=1
            for i in range(1,n+1): Sprod*=1+q**i
            Aprod=1
            for i in range(0,n): Aprod*=1+q**i
            assert S==Sprod
            assert A==Aprod
            assert 2*S==(1+q**n)*A if n>0 else S==A==1
            assert B>=q**(n*n)
            checks+=4
    # Numerical approach to the asymptotic constants.
    for q in (2,3,5):
        C=1.0
        for j in range(1,200): C*=1+q**(-j)
        for n in (8,12,20):
            _,S,A=profiles(q,n)
            assert abs(S/q**(n*(n+1)//2)-C) < 6*q**(-n)
            assert abs(A/q**(n*(n-1)//2)-2*C) < 12*q**(-(n-1))
            checks+=2
    print('VERIFY_OK', checks, 'exact/numerical assertions')
    for q in (2,3):
        print('q=',q,'n=0..5', [profiles(q,n) for n in range(6)])

if __name__=='__main__': main()

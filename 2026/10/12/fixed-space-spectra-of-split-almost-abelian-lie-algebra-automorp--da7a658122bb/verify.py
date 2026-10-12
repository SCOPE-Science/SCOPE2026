"""Self-contained finite-field checks of a Lie-automorphism fixed-space census.

No external dependencies. This is a finite test, not a substitute for the proof.
"""
from itertools import product
from math import gcd, prod, isqrt


class Field:
    def __init__(self, q):
        self.q = q
        if q in (4, 9):
            self.p = isqrt(q)
            self.deg = 2
            self.A, self.B = (1, 1) if q == 4 else (0, 1)
        else:
            self.p = q
            self.deg = 1
            self.A = self.B = 0
            assert all(q % d for d in range(2, isqrt(q) + 1))

    def add(self, x, y):
        p = self.p
        if self.deg == 1:
            return (x + y) % p
        return ((x % p + y % p) % p) + p * ((x // p + y // p) % p)

    def neg(self, x):
        return self.sub(0, x)

    def sub(self, x, y):
        p = self.p
        if self.deg == 1:
            return (x - y) % p
        return ((x % p - y % p) % p) + p * ((x // p - y // p) % p)

    def mul(self, x, y):
        p = self.p
        if self.deg == 1:
            return (x * y) % p
        a,b = x % p, x // p
        c,d = y % p, y // p
        return ((a*c - self.B*b*d) % p) + p*((a*d+b*c-self.A*b*d) % p)

    def power(self,x,n):
        z=1
        while n:
            if n%2: z=self.mul(z,x)
            x=self.mul(x,x)
            n//=2
        return z

    def root(self,m):
        assert (self.q-1)%m == 0
        for x in range(2, self.q):
            if self.power(x,m)==1 and all(self.power(x,k)!=1 for k in range(1,m)):
                return x
        if m==1: return 1
        raise AssertionError((self.q,m))


def matmul(F, A, B):
    n=len(A)
    return tuple(tuple(sum_field(F,[F.mul(A[i][k],B[k][j]) for k in range(n)]) for j in range(n)) for i in range(n))


def sum_field(F, xs):
    y=0
    for x in xs: y=F.add(y,x)
    return y


def determinant(F,A):
    n=len(A)
    B=[list(row) for row in A]
    d=1
    for c in range(n):
        piv=next((i for i in range(c,n) if B[i][c]!=0),None)
        if piv is None:return 0
        if piv!=c:
            B[piv],B[c]=B[c],B[piv]
            d=F.neg(d)
        a=B[c][c]
        d=F.mul(d,a)
        inv=F.power(a,F.q-2)
        for i in range(c+1,n):
            f=F.mul(B[i][c],inv)
            for j in range(c,n):
                B[i][j]=F.sub(B[i][j],F.mul(f,B[c][j]))
    return d


def minus_identity(F,A):
    return tuple(tuple(F.sub(A[i][j],1 if i==j else 0) for j in range(len(A))) for i in range(len(A)))


def matrices(F,s):
    for t in product(range(F.q),repeat=s*s):
        yield tuple(tuple(t[s*i+j] for j in range(s)) for i in range(s))


def GL(F,s):
    return [A for A in matrices(F,s) if determinant(F,A)!=0]


def predicted(F,m,s,D,G):
    q=F.q
    def totient(d): return sum(1 for a in range(1,d+1) if gcd(a,d)==1)
    return q**(m*s)*sum(totient(d)*(G**(d-1)*D)**(m//d)
                          for d in range(2,m+1) if m%d==0)


def count_monoblocks(F,m,s):
    """Enumerate intertwining blocks (not the closed-form product count)."""
    assert m*s<=4
    H=GL(F,s)
    z=F.root(m)
    eig=[F.power(z,i) for i in range(m)]
    n_good=0
    n_total=0
    for a in eig:
        targets=[]
        for e in eig:
            t=next((j for j,f in enumerate(eig) if e==F.mul(a,f)),None)
            assert t is not None
            targets.append(t)
        for blocks in product(H, repeat=m):
            n_total+=1
            if a==1: continue
            # Build full S without using the cycle-product lemma.
            n=m*s
            S=[[0]*n for _ in range(n)]
            for j,U in enumerate(blocks):
                for i in range(s):
                    for k in range(s):
                        S[targets[j]*s+i][j*s+k]=U[i][k]
            S=tuple(map(tuple,S))
            # Check ST=aTS entrywise, independent of cycle argument.
            for i in range(n):
                for j in range(n):
                    assert F.mul(S[i][j],eig[j//s])==F.mul(F.mul(a,eig[i//s]),S[i][j])
            if determinant(F,minus_identity(F,S))!=0:
                n_good+=1
    return n_total,n_good


def rank(F,A):
    n=len(A)
    B=[list(row) for row in A]
    r=0
    for c in range(len(B[0]) if B else 0):
        k=next((i for i in range(r,n) if B[i][c]!=0),None)
        if k is None:continue
        B[k],B[r]=B[r],B[k]
        v=F.power(B[r][c],F.q-2)
        for j in range(c,len(B[0])):B[r][j]=F.mul(v,B[r][j])
        for i in range(n):
            if i==r:continue
            h=B[i][c]
            for j in range(c,len(B[0])):
                B[i][j]=F.sub(B[i][j],F.mul(h,B[r][j]))
        r+=1
        if r==n:break
    return r


def gauss(q,n,k):
    if k<0 or k>n:return 0
    a=prod(q**(n-j)-1 for j in range(k))
    b=prod(q**(k-j)-1 for j in range(k))
    return a//b


def order_gl(q,n):
    return prod(q**n-q**i for i in range(n))


def Pcoeff(q,s):
    out=[]
    for k in range(s+1):
        t=sum((-1)**j*q**(j*(j-1)//2)*gauss(q,s-k,j)*q**((k+j)*(s-k-j))*order_gl(q,s-k-j)
              for j in range(s-k+1))
        out.append(gauss(q,s,k)*t)
    return out


def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def poly_pow(a,k):
    r=[1]
    for _ in range(k):r=poly_mul(r,a)
    return r


def totient(d):
    return sum(gcd(a,d)==1 for a in range(1,d+1))


def spectrum_formula(q,m,s):
    G=order_gl(q,s);n=m*s
    P=Pcoeff(q,s)
    a=[0]*(n+2)
    for d in range(2,m+1):
        if m%d:continue
        Q=poly_pow(P,m//d)
        scale=totient(d)*q**n*G**(m-m//d)
        for i,x in enumerate(Q):a[i]+=scale*x
    H=poly_pow(P,m)
    for k,x in enumerate(H):
        a[k]+=x*(q**n-q**(n-k))
        a[k+1]+=x*q**(n-k)
    assert sum(a)==m*q**n*G**m
    return a


def spectrum_independent(F,m,s,do_all_w=True):
    """Directly enumerate block maps, then calculate kernel of the full matrix.
    For large cases compare only vector parts and block prediction."""
    assert s*m<=4
    q=F.q;n=s*m;z=F.root(m);H=GL(F,s)
    eig=[F.power(z,i) for i in range(m)]
    A=[0]*(n+2)
    for a in eig:
        targets=[]
        for e in eig:
            t=next(j for j,f in enumerate(eig) if e==F.mul(a,f))
            targets.append(t)
        for blocks in product(H,repeat=m):
            S=[[0]*n for _ in range(n)]
            for j,U in enumerate(blocks):
                for i in range(s):
                    for k in range(s):S[targets[j]*s+i][j*s+k]=U[i][k]
            # Directly calculate the full (n+1)-dimensional matrix rank.
            if do_all_w:
                ws=product(range(q),repeat=n)
            else:
                ws=((0,)*n,)
            for w in ws:
                E=[[F.sub(a,1)]+[0]*n]
                for i in range(n):
                    E.append([w[i]]+[F.sub(S[i][j],int(i==j)) for j in range(n)])
                fixed=(n+1)-rank(F,E)
                A[fixed]+=1
    return A


def spectral_stabilizer(F,sp):
    return [a for a in range(1,F.q) if all(
        F.mul(lam,F.power(a,F.q-2)) in sp and
        sp[F.mul(lam,F.power(a,F.q-2))]==v
        for lam,v in sp.items())]


def spectrum_general(F,sp):
    q=F.q;n=sum(sp.values())
    H=spectral_stabilizer(F,sp)
    assert H and 1 in H
    first=[1]
    for r in sp.values():first=poly_mul(first,Pcoeff(q,r))
    ans=[0]*(n+2)
    for a in H:
        if a==1:continue
        unseen=set(sp)
        term=[1]
        while unseen:
            lam=next(iter(unseen))
            cyc=[]
            v=lam
            while v not in cyc:
                cyc.append(v)
                v=F.mul(v,F.power(a,q-2))
            assert v==lam
            unseen.difference_update(cyc)
            dim=sp[lam]
            assert all(sp[x]==dim for x in cyc)
            term=poly_mul(term,[order_gl(q,dim)**(len(cyc)-1)*h for h in Pcoeff(q,dim)])
        for k,h in enumerate(term):ans[k]+=q**n*h
    for k,h in enumerate(first):
        ans[k]+=(q**n-q**(n-k))*h
        ans[k+1]+=q**(n-k)*h
    size=q**n*len(H)*prod(order_gl(q,r) for r in sp.values())
    assert sum(ans)==size
    return ans


def spectrum_general_direct(F,sp):
    """Build every Lie algebra automorphism matrix and directly compute rank."""
    q=F.q;n=sum(sp.values())
    elems=sorted(sp)
    off={};v=0
    for lam in elems:off[lam]=v;v+=sp[lam]
    H=spectral_stabilizer(F,sp)
    out=[0]*(n+2)
    opts=[GL(F,sp[lam]) for lam in elems]
    for a in H:
        for blocks in product(*opts):
            S=[[0]*n for _ in range(n)]
            for lam,U in zip(elems,blocks):
                target=F.mul(lam,F.power(a,q-2))
                r=sp[lam]
                for i in range(r):
                    for j in range(r):S[off[target]+i][off[lam]+j]=U[i][j]
            # Determine ST=aTS on every entry (checks automorphism parametrization).
            labels=sum(([lam]*sp[lam] for lam in elems),[])
            for i in range(n):
                for j in range(n):
                    assert F.mul(S[i][j],labels[j])==F.mul(F.mul(a,labels[i]),S[i][j])
            for w in product(range(q),repeat=n):
                E=[[F.sub(a,1)]+[0]*n]
                for i in range(n):
                    E.append([w[i]]+[F.sub(S[i][j],int(i==j)) for j in range(n)])
                fixed=n+1-rank(F,E)
                out[fixed]+=1
    return out


def main():
    checks=0
    from fractions import Fraction
    for q,s in [(3,1),(3,2),(3,3),(4,1),(4,2),(5,1),(5,2),(7,1),(9,1)]:
        F=Field(q)
        L=GL(F,s)
        observed=[0]*(s+1)
        for U in L:observed[s-rank(F,minus_identity(F,U))]+=1
        expected=Pcoeff(q,s)
        assert observed==expected,(q,s,observed,expected)
        G=len(L);D=observed[0]
        rho=sum((Fraction((-1)**j,prod(q**i-1 for i in range(1,j+1))) for j in range(s+1)),Fraction(0))
        assert D==G*rho,(q,s,D,G,rho)
        checks+=1
        print('GL_PROFILE_CHECK',q,s,'profile',observed)
    for q,m,s in [(3,2,1),(3,2,2),(4,3,1),(5,2,1),(7,3,1),(9,4,1)]:
        F=Field(q)
        expected=spectrum_formula(q,m,s)
        if m*s<=3:
            actual=spectrum_independent(F,m,s,True)
            assert actual==expected,(q,m,s,actual,expected)
            print('LIE_PROFILE_CHECK',q,m,s,'profile',actual)
            checks+=1
        elif q==3 and s==2:
            actual=spectrum_independent(F,m,s,True)
            assert actual==expected,(q,m,s,actual,expected)
            print('LIE_PROFILE_CHECK',q,m,s,'profile',actual)
            checks+=1
        else:
            good=predicted(F,m,s,Pcoeff(q,s)[0],order_gl(q,s))
            assert good==expected[0]
            print('FORMULA_CHECK',q,m,s,'full_distribution',expected)
            checks+=1
    for q,sp in [
        (2,{1:1}),(2,{1:2}),
        (3,{1:2}),(3,{1:1,2:1}),
        (4,{1:1,2:1}),(4,{1:1,2:1,3:1}),
        (5,{1:1,2:1}),(5,{1:1,4:1}),(5,{1:1,2:1,3:1}),
        (7,{1:1,2:1,4:1}),
    ]:
        F=Field(q)
        expect=spectrum_general(F,sp)
        actual=spectrum_general_direct(F,sp)
        assert actual==expect,(q,sp,actual,expect)
        checks+=1
        print('GENERAL_PROFILE_CHECK',q,sp,'stabilizer',spectral_stabilizer(F,sp),'profile',actual)
    print('FINITE_CHECKS',checks,'VERIFY_OK')

if __name__=='__main__':main()

"""Reproducible exact-arithmetic checks for sparse-order finite-field adjacency."""
from math import comb, isqrt


def det_bareiss(mat):
    a = [row[:] for row in mat]
    n = len(a)
    if n == 0: return 1
    denominator = 1
    sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((i for i in range(k+1,n) if a[i][k]), None)
            if j is None: return 0
            a[k],a[j] = a[j],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*pivot - a[i][k]*a[k][j]
                assert num % denominator == 0
                a[i][j] = num//denominator
            a[i][k] = 0
        denominator = pivot
    return sign*a[n-1][n-1]


def resultant(a):
    n = 2**(a-1)
    f = [1]+[0]*(n-1)+[1]
    g = [comb(n,j) for j in range(n+1)]
    g[0] += 1
    rf = list(reversed(f)); rg=list(reversed(g))
    mat = []
    for j in range(n):
        mat.append([0]*j+rf+[0]*(n-1-j))
    for j in range(n):
        mat.append([0]*j+rg+[0]*(n-1-j))
    return det_bareiss(mat)


def factor_integer(n):
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1 if d==2 else 2
    if n>1: out[n]=out.get(n,0)+1
    return out


def trim(f):
    while f and f[-1]==0:f.pop()
    return f


def modpoly(f,g,p):
    f=trim([v%p for v in f[:]]);g=trim([v%p for v in g[:]])
    assert g
    inv=pow(g[-1],-1,p)
    while len(f)>=len(g):
        v=f[-1]*inv%p
        shift=len(f)-len(g)
        for j,b in enumerate(g):
            f[j+shift]=(f[j+shift]-v*b)%p
        trim(f)
    return f


def gcdmod(a,b,p):
    a=trim([v%p for v in a[:]]);b=trim([v%p for v in b[:]])
    while b:a,b=b,modpoly(a,b,p)
    if a:
        z=pow(a[-1],-1,p);a=[x*z%p for x in a]
    return a


def polynomial_gcd(a,p):
    n=2**(a-1)
    f=[1]+[0]*(n-1)+[1]
    g=[comb(n,j) for j in range(n+1)];g[0]+=1
    return gcdmod(f,g,p)


def finite_field_count(p,modulus):
    # modulus monic irreducible over F_p in ascending coefficient order
    f=len(modulus)-1;q=p**f
    def enc(d):
        y=0
        for z in reversed(d):y=y*p+z
        return y
    def dec(z):
        d=[]
        for _ in range(f):d.append(z%p);z//=p
        return d
    def mul(a,b):
        aa=dec(a);bb=dec(b)
        v=[0]*(2*f-1)
        for i in range(f):
            for j in range(f): v[i+j]=(v[i+j]+aa[i]*bb[j])%p
        for k in range(2*f-2,f-1,-1):
            v0=v[k]
            for j in range(f):v[k-f+j]=(v[k-f+j]-v0*modulus[j])%p
        return enc(v[:f])
    def power(x,e):
        r=1
        while e:
            if e&1:r=mul(r,x)
            x=mul(x,x);e>>=1
        return r
    primes=list(factor_integer(q-1))
    NSNP=[]
    for x in range(1,q):
        if power(x,(q-1)//2) != p-1: continue
        if any(power(x,(q-1)//r)==1 for r in primes):NSNP.append(x)
    aset=set(NSNP)
    count=0
    for x in NSNP:
        digits=dec(x)
        digits[0]=(digits[0]+1)%p
        if enc(digits) in aset:count+=1
    return q,len(NSNP),count


def main():
    want={1:1,2:5,3:153,4:1051779953}
    wantfact={1:{},2:{5:1},3:{3:2,17:1},4:{7:2,17:4,257:1}}
    for a in range(1,5):
        v=resultant(a)
        if a==1: v=abs(v)
        assert v==want[a],(a,v)
        fac=factor_integer(v)
        assert fac==wantfact[a]
        gcds={p:polynomial_gcd(a,p) for p in fac}
        assert all(len(v)>1 for v in gcds.values())
        print('a=',a,'resultant=',v,'factors=',fac,'gcds=',gcds)
    # x^3+x+constant with no roots; irreducible for degree 3
    irr17=None
    for b in range(1,17):
        if all((x**3+x+b)%17!=0 for x in range(17)):
            irr17=[b,1,0,1];break
    assert irr17
    print('irreducible17=',irr17)
    examples=[(7,[4,0,1],49,2),(5,[1,1,0,1],125,1),(17,irr17,4913,4),
              (41,[0,1],41,0),(89,[0,1],89,0),(113,[0,1],113,0)]
    for p,poly,q,N in examples:
        got=finite_field_count(p,poly)
        assert got[0]==q and got[2]==N,(q,got)
        print('field',q,'NSNP=',got[1],'adjacent_pairs=',got[2])
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()

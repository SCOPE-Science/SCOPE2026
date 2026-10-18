"""Exact finite-state cross-checks for two-proposal cycle hitting laws.

Standard-library-only, does not replace the analytical argument for all sizes.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext


def solve(a, b):
    m = len(b)
    a = [list(row) + [b[i]] for i, row in enumerate(a)]
    for k in range(m):
        pivot = next(j for j in range(k, m) if a[j][k] != 0)
        a[k], a[pivot] = a[pivot], a[k]
        fac = a[k][k]
        a[k] = [v / fac for v in a[k]]
        for i in range(m):
            if i != k:
                fac = a[i][k]
                if fac:
                    a[i] = [v-fac*w for v,w in zip(a[i],a[k])]
    return [row[-1] for row in a]


def distance_chain(n):
    r = n//2
    p = [[Q(0) for _ in range(r)] for _ in range(r)]
    terminal = [Q(0) for _ in range(r)]
    for j in range(1,r+1):
        if n%2 == 0 and j == r:
            p[j-1][j-2] = Q(1)
        else:
            if j == 1:
                terminal[j-1] = Q(3,4)
            else:
                p[j-1][j-2] = Q(3,4)
            p[j-1][j if j<r else j-1] += Q(1,4)
    return p, terminal


def predicted(n,j):
    r=n//2
    if n%2 == 0:
        a=-Q(1, 2*3**(r-1))
        b=(-4*r-4+a)/3**(r-1)
    else:
        a=-Q(1,3**r)
        b=(-8*r-11+2*a)/3**r
    h=Q(2*j)+a*(3**j-1)
    v=Q(6*j)-8*a*j*3**j+b*(3**j-1)-a*a*(3**j-1)**2
    return h,v


def exact_pgf_root(n,j,z):
    with localcontext() as ctx:
        ctx.prec=82
        x=Decimal(z.numerator)/Decimal(z.denominator)
        lam=(2-(4-3*x*x).sqrt())/x
        big=(2+(4-3*x*x).sqrt())/x
        r=n//2
        boundary=x if n%2==0 else 3*x/(4-x)
        eta=(lam/big)**(r-1)*(boundary-lam)/(big-boundary)
        return (lam**j+eta*big**j)/(1+eta)


def main():
    tests=0
    for n in range(3,31):
        p,term=distance_chain(n)
        r=len(term)
        m=[[Q(i==j)-p[i][j] for j in range(r)] for i in range(r)]
        h=solve(m,[Q(1)]*r)
        s2=solve(m,[2*x-1 for x in h])
        for j in range(1,r+1):
            ph,pv=predicted(n,j)
            assert h[j-1]==ph
            assert s2[j-1]-ph*ph==pv
            assert ph> (h[j-2] if j>1 else Q(0))
            tests+=3
        for v in range(1,n):
            neighbors=[(v-1)%n, (v+1)%n]
            vals=[Q(0) if x==0 else h[min(x,n-x)-1] for x in neighbors]
            bellman=Q(1)+sum(min(vals[i],vals[k]) for i in range(2) for k in range(2))/4
            assert bellman==h[min(v,n-v)-1]
            tests+=1
        for z in [Q(1,2),Q(2,3),Q(9,10)]:
            a=[[Q(i==j)-z*p[i][j] for j in range(r)] for i in range(r)]
            f=solve(a,[z*t for t in term])
            for j,number in enumerate(f,1):
                candidate=exact_pgf_root(n,j,z)
                with localcontext() as ctx:
                    ctx.prec=82
                    expected=Decimal(number.numerator)/Decimal(number.denominator)
                assert abs(candidate-expected)<Decimal('1e-60'),(n,j,z)
                tests+=1
    print('PASS:',tests,'independent finite-state moment/Bellman/transform comparisons on N=3..30')
    # At antipodal distance the parity-dependent variance shifts have limits.
    for n in [40,41,60,61]:
        p,t=distance_chain(n);r=len(t)
        mm=[[Q(i==j)-p[i][j] for j in range(r)] for i in range(r)]
        h=solve(mm,[Q(1)]*r); s=solve(mm,[2*x-1 for x in h])
        diff=(s[-1]-h[-1]**2)-6*r
        limit=Q(-57,4) if n%2==0 else Q(-12)
        assert abs(diff-limit)<Q(1,1000000)
        print('antipode',n,'variance remainder',float(diff))

if __name__=='__main__':
    main()

"""Independent finite consistency checks for the biisotropic line-Grassmannian ring formula.

Uses integer arithmetic only. The universal assertion is proved in RESULT.md;
this script is not an exhaustive argument for arbitrary n.
"""
from math import comb, gcd


def poly_add(a, b, fac=1):
    out = dict(a)
    for power, coeff in b.items():
        out[power] = out.get(power, 0) + fac*coeff
    return {k: v for k, v in out.items() if v}


def poly_mul(a, b):
    out = {}
    for (i,j), v in a.items():
        for (k,l), w in b.items():
            key = (i+k, j+l)
            out[key] = out.get(key, 0) + v*w
    return {k:v for k,v in out.items() if v}


def poly_pow(a, n):
    out = {(0,0):1}
    while n:
        if n & 1:
            out = poly_mul(out, a)
        a = poly_mul(a, a)
        n //= 2
    return out

h = {(1,0):1}
c = {(0,1):1}


def complete_homogeneous(max_degree):
    result = [{(0,0):1}, h]
    for j in range(2, max_degree+1):
        result.append(poly_add(poly_mul(h, result[-1]), poly_mul(c, result[-2]), -1))
    return result


def schur_monomials(a, b):
    # Two-variable Schur polynomial s_(a,b)(x,y), indexed by exponent of x.
    return range(b,a+1)


def integral(a,b,p,q,n):
    # The integral on Gr(2,2n+1) of s_(a,b)s_(p,q)h^2,
    # via the Weyl alternant coefficient x^(2n)y^(2n-1).
    m = 2*n-1
    assert a+b+p+q+2 == 2*m
    powers = {}
    for i in schur_monomials(a,b):
        for j in schur_monomials(p,q):
            powers[i+j] = powers.get(i+j,0)+1
    answer = 0
    for power, number in powers.items():
        for t, coef in enumerate((1,2,1)):
            if power+t+1 == m+1:
                answer += number*coef
            if power+t == m+1:
                answer -= number*coef
    return answer


def det(a):
    # Leibniz determinant via recursive elimination, exact integer Bareiss.
    n=len(a)
    if n==1:
        return a[0][0]
    A=[list(map(int,row)) for row in a]
    sign=1
    old=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]),None)
            if j is None: return 0
            A[k],A[j]=A[j],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%old==0
                A[i][j]=num//old
        for i in range(k+1,n):
            A[i][k]=0
        old=pivot
    return sign*A[-1][-1]


def weighted_hilbert(n):
    limit=4*n-2
    base=[sum(1 for b in range(t//2+1)) for t in range(limit+1)]
    out=[]
    for t in range(limit+1):
        def B(q): return base[q] if q>=0 else 0
        out.append(B(t)-B(t-(2*n-1))-B(t-2*n)+B(t-(4*n-1)))
    return out


def gr_rank(n,t):
    # Rank in H^(2t) of Gr(2,2n).
    width=2*n-2
    return sum(1 for b in range(t//2+1) if t-b <= width)


for n in range(2,13):
    q=complete_homogeneous(2*n+1)
    R={}
    for b in range(n):
        term=poly_mul(poly_pow(c,b),q[2*n-1-2*b])
        R=poly_add(R,term,((-1)**b)*(n-b))
    identity=poly_add(poly_mul(poly_pow(h,2),R),poly_mul(h,q[2*n]),-(n+1))
    identity=poly_add(identity,q[2*n+1])
    assert not identity, ('relation identity',n,identity)

    middle=[(2*n-2-b,b) for b in range(n)]
    M=[[integral(*a,*b,n) for b in middle] for a in middle]
    assert all(M[i][j]==(2 if i==j and i<n-1 else 1 if i==j or abs(i-j)==1 else 0)
               for i in range(n) for j in range(n)),('mid matrix',n,M)
    assert det(M)==1,('mid determinant',n)

    high=[(2*n-1-b,b) for b in range(n)]
    low=[(2*n-3-b,b) for b in range(n-1)]
    coefficients=[(-1)**b*(n-b) for b in range(n)]
    for a in low:
        values=[integral(*a,*b,n) for b in high]
        assert sum(x*y for x,y in zip(values,coefficients))==0
        assert values==[comb(2,b-a[1]) if 0<=b-a[1]<=2 else 0 for b in range(n)]

    hilbert=weighted_hilbert(n)
    assert all(hilbert[t]==gr_rank(n,t) for t in range(4*n-3)), ('Hilbert',n)
    assert hilbert[4*n-4]==1
    assert hilbert[4*n-3]==0 and hilbert[4*n-2]==0
    print('n=',n,' middle determinant=1; relation kernel=0; CI Hilbert ranks match')
print('VERIFY_OK')

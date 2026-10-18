"""Exact tests of the radical of a cyclic/bicyclic planar Euler form."""
from math import gcd
from itertools import product
from sympy import Matrix

def elements(moduli):
    return list(product(*(range(n) for n in moduli)))

def add(a,b,ns):
    return tuple((x+y)%n for x,y,n in zip(a,b,ns))

def mul(k,a,ns):
    return tuple((k*x)%n for x,n in zip(a,ns))

def order(a,ns):
    from math import lcm
    out=1
    for x,n in zip(a,ns):
        out=lcm(out,n//gcd(x,n))
    return out

def expected(ns,a,b):
    q=1
    for n in ns:q*=n
    c=add(a,b,ns)
    da=q//order(a,ns);db=q//order(b,ns);dc=q//order(c,ns)
    return da+db-1+(dc if order(c,ns)%2==0 else 0)-(da%2==0)-(db%2==0)

def faithful(ns,a,b):
    q=1
    for n in ns:q*=n
    return len({add(mul(k,a,ns),mul(j,b,ns),ns) for k in range(order(a,ns)) for j in range(order(b,ns))})==q

def exact_fourier_zeros(ns,a,b):
    # A character is indexed by the dual of the coordinate group.
    # The zero factor conditions use only modular integers.
    z=0
    c=add(a,b,ns)
    for t in elements(ns):
        den=1
        from math import lcm
        for n in ns:den=lcm(den,n)
        def phase(x):return sum(tx*den//n*y for tx,n,y in zip(t,ns,x))%den
        aa=phase(a);bb=phase(b);cc=phase(c)
        if aa==0 or bb==0 or (den%2==0 and cc==den//2):z+=1
    return z

def hessian_nullity(ns,a,b):
    E=elements(ns); ix={g:i for i,g in enumerate(E)}
    c=add(a,b,ns)
    n=len(E)
    H=[[0]*n for _ in range(n)]
    for g in E:
        i=ix[g];H[i][i]+=2
        for h,sign in ((a,-1),(b,-1),(c,1)):
            j=ix[add(g,h,ns)]
            r=ix[add(g,mul(-1,h,ns),ns)]
            H[i][j]+=sign; H[i][r]+=sign
    return n-Matrix(H).rank()

count=0; direct=0
for n in range(2,49):
    ns=(n,)
    for a in elements(ns):
        for b in elements(ns):
            if gcd(n,gcd(a[0],b[0])) != 1:continue
            exp=expected(ns,a,b)
            actual=exact_fourier_zeros(ns,a,b)
            assert exp==actual,(ns,a,b,exp,actual)
            count+=1
for m,n in ((2,2),(2,4),(2,6),(3,3),(3,6),(4,4),(2,8)):
    ns=(m,n)
    for a in elements(ns):
        for b in elements(ns):
            if not faithful(ns,a,b):continue
            exp=expected(ns,a,b)
            got=exact_fourier_zeros(ns,a,b)
            assert exp==got,(ns,a,b,exp,got)
            if direct<30:
                rank_null=hessian_nullity(ns,a,b)
                assert rank_null==exp,(ns,a,b,rank_null,exp)
                direct+=1
            count+=1
print(f'VERIFY_OK faithful_action_profiles={count} exact_matrix_rank_checks={direct}')
print('Examples:',[(ns,a,b,expected(ns,a,b)) for ns,a,b in [((4,),(1,),(1,)),((8,),(1,),(3,)),((6,),(1,),(5,)),((2,2),(1,0),(0,1)),((3,3),(1,0),(0,1))]])

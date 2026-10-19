"""Direct finite-field verification for a four-dimensional solvable Lie algebra.

Usage: python verify.py
No third-party dependencies are required.
"""
from itertools import combinations, product
from math import comb


def rref(rows, p):
    if not rows:
        return ()
    n = len(rows[0]); a = [list(x) for x in rows]
    j = 0; i = 0
    while i < len(a) and j < n:
        r = next((u for u in range(i, len(a)) if a[u][j] % p), None)
        if r is None:
            j += 1; continue
        a[i], a[r] = a[r], a[i]
        t = pow(a[i][j], -1, p)
        a[i] = [(z*t) % p for z in a[i]]
        for u in range(len(a)):
            if u != i and a[u][j] % p:
                t = a[u][j]
                a[u] = [(x-t*y) % p for x, y in zip(a[u], a[i])]
        i += 1; j += 1
    return tuple(tuple(row) for row in a[:i])


def all_subspaces(n, p):
    result = []
    for k in range(n+1):
        for pivots in combinations(range(n), k):
            allowed = [(i, j) for i, pivot in enumerate(pivots)
                       for j in range(pivot+1,n) if j not in pivots]
            for vals in product(range(p), repeat=len(allowed)):
                rows = [[int(j == pivot) for j in range(n)] for pivot in pivots]
                for (i,j), val in zip(allowed, vals):rows[i][j]=val
                result.append(tuple(tuple(row) for row in rows))
    assert len(set(result)) == len(result)
    return result


def bracket(x,y,p,lam):
    return (0, (x[0]*y[1]-y[0]*x[1])%p,
            (x[0]*y[2]-y[0]*x[2])%p,
            (lam*(x[0]*y[3]-y[0]*x[3]))%p)


def closed(rows,p,lam):
    for i,x in enumerate(rows):
        for y in rows[i+1:]:
            if len(rref(list(rows)+[bracket(x,y,p,lam)],p)) > len(rows):
                return False
    return True


def permutable(a,b,p,lam):
    s = rref(a+b,p)
    return closed(s,p,lam)


def check(p,lam):
    assert p>2 and lam not in (0,1)
    algebras = [s for s in all_subspaces(4,p) if closed(s,p,lam)]
    N = len(algebras)
    failed = sum(not permutable(a,b,p,lam) for a in algebras for b in algebras)
    expectedN = 2*p**3+5*p**2+4*p+5
    expectedFailed = p**2*(p-1)*(p+1)**2*(3*p+1)
    assert (N,failed)==(expectedN,expectedFailed), (p,lam,N,failed,expectedN,expectedFailed)
    print('DIRECT_SUBALGEBRA_PAIRS',p,lam,'SUBALGEBRAS',N,'NONPERMUTABLE_ORDERED',failed,'PASS')


if __name__=='__main__':
    for p in (3,5):
        for lam in range(2,p):
            check(p,lam)

# A separate, genuine F_4 implementation checks the characteristic-two boundary.
def gf4_mul(a,b):
    poly = 0
    for i in range(2):
        for j in range(2):
            if (a >> i)&1 and (b >> j)&1:
                poly ^= 1<<(i+j)
    if poly & 8:
        poly ^= 0b1110
    if poly & 4:
        poly ^= 0b111
    return poly


def gf4_rref(rows):
    a=[list(row) for row in rows]
    if not a: return ()
    n=len(a[0]); i=0
    for j in range(n):
        pivot=next((k for k in range(i,len(a)) if a[k][j]),None)
        if pivot is None:continue
        a[i],a[pivot]=a[pivot],a[i]
        inv = {1:1,2:3,3:2}[a[i][j]]
        a[i]=[gf4_mul(inv,v) for v in a[i]]
        for k in range(len(a)):
            if k!=i and a[k][j]:
                t=a[k][j]
                a[k]=[v ^ gf4_mul(t,w) for v,w in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return tuple(tuple(row) for row in a[:i])


def gf4_bracket(a,b,lam):
    return (0,)+tuple(gf4_mul(z,lam if i==3 else 1) for i in (1,2,3)
                        for z in [gf4_mul(a[0],b[i]) ^ gf4_mul(b[0],a[i])])


def gf4_closed(rows,lam):
    for i,a in enumerate(rows):
        for b in rows[i+1:]:
            if len(gf4_rref(list(rows)+[gf4_bracket(a,b,lam)]))>len(rows):return False
    return True


def check_gf4(lam=2):
    # Produce canonical subspaces by explicit field-RREF generators.
    spaces=[]
    for k in range(5):
        for piv in combinations(range(4),k):
            free=[(i,j) for i,p in enumerate(piv)
                  for j in range(p+1,4) if j not in piv]
            for vals in product(range(4),repeat=len(free)):
                a=[[int(j==p) for j in range(4)] for p in piv]
                for (i,j),v in zip(free,vals):a[i][j]=v
                spaces.append(tuple(tuple(row) for row in a))
    assert len(spaces)==529
    subs=[a for a in spaces if gf4_closed(a,lam)]
    bad=0
    for a in subs:
        for b in subs:
            if not gf4_closed(gf4_rref(a+b),lam):bad+=1
    q=4
    assert (len(subs),bad)==(2*q**3+5*q**2+4*q+5,q**2*(q-1)*(q+1)**2*(3*q+1))
    print('DIRECT_GF4_SUBALGEBRA_PAIRS','lambda',lam,'SUBALGEBRAS',len(subs),'NONPERMUTABLE_ORDERED',bad,'PASS')


if __name__=='__main__':
    check_gf4(2)
    check_gf4(3)
    print('VERIFY_OK')

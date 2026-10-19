"""Independent small-field enumeration for restricted-range nilpotent map formula.
Run with Python 3 (standard library only)."""
from itertools import product
from collections import Counter
from math import prod


def matmul(a, b, q):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) % q for j in range(len(b[0]))) for i in range(len(a)))


def rank(a, q):
    a = [list(x) for x in a]
    if not a: return 0
    h, w = len(a), len(a[0]); pivot = 0
    for col in range(w):
        ii = next((i for i in range(pivot,h) if a[i][col] % q), None)
        if ii is None: continue
        a[pivot], a[ii] = a[ii], a[pivot]
        inv = pow(a[pivot][col], -1, q)
        a[pivot] = [(v*inv) % q for v in a[pivot]]
        for ii in range(h):
            if ii != pivot:
                s = a[ii][col]
                if s: a[ii] = [(v-s*w) % q for v,w in zip(a[ii],a[pivot])]
        pivot += 1
        if pivot==h: break
    return pivot


def nil_type(b,q):
    r = len(b); power = tuple(tuple(int(i==j) for j in range(r)) for i in range(r))
    old = r; columns = []
    for k in range(1, r+1):
        power = matmul(power,b,q)
        new = rank(power,q)
        columns.append(old-new); old=new
    if old: return None
    return tuple(k for k in range(1,r+1) for _ in range(columns[k-1] - (columns[k] if k<r else 0)))[::-1]


def partitions(n, hi=None):
    if n==0: yield (); return
    if hi is None: hi=n
    for p in range(min(hi,n),0,-1):
        for rest in partitions(n-p,p): yield (p,)+rest


def orbit(q, la):
    r=sum(la); mult=Counter(la)
    conjugate=[sum(v>=j for v in la) for j in range(1,max(la)+1)]
    central=q**(sum(v*v for v in conjugate)-sum(k*(k+1)//2 for k in mult.values()))
    for k in mult.values():
        central*=prod(q**j-1 for j in range(1,k+1))
    gl=prod(q**r-q**i for i in range(r))
    assert gl % central == 0
    return gl//central


def exhaustive_regularity_witness(q, r, c):
    n=r+c
    transforms=[]
    for a in product(range(q), repeat=r*n):
        upper=tuple(tuple(a[i*n:(i+1)*n]) for i in range(r))
        transforms.append(upper+tuple((0,)*n for _ in range(c)))
    for t in transforms:
        predicted=(rank(t,q)==rank(tuple(row[:r] for row in t[:r]),q))
        actual=any(matmul(matmul(t,s,q),t,q)==t for s in transforms)
        assert predicted==actual, (q,r,c,t)
    print(f'PASS q={q} r={r} c={c}: direct TST=T witness criterion on {len(transforms)} maps')


def check(q,r,c):
    n=r+c; by_type=Counter(); all_nil=0; all_reg=0
    # enumerate all r by n matrices, lower c rows forced zero
    for vals in product(range(q), repeat=r*n):
        rows=tuple(tuple(vals[i*n:(i+1)*n]) for i in range(r))
        b=tuple(row[:r] for row in rows)
        la=nil_type(b,q)
        if la is None: continue
        all_nil+=1
        t=rows+tuple((0,)*n for _ in range(c))
        if rank(t,q) == rank(b,q):
            all_reg+=1
            by_type[la]+=1
            # check Jordan type equals lambda plus c singleton blocks
            got = nil_type(t,q)
            assert got==tuple(sorted(la+(1,)*c,reverse=True)), (q,r,c,la,got)
    assert all_nil==q**(r*c+r*r-r),(q,r,c,all_nil)
    expected={p:orbit(q,p)*q**(c*(r-len(p))) for p in partitions(r)}
    assert by_type==Counter(expected),(q,r,c,by_type,expected)
    assert all_reg==sum(expected.values())
    print(f'PASS q={q} r={r} c={c}: nil={all_nil}, regular_nil={all_reg}, types={len(by_type)}')


if __name__=='__main__':
    for p,r,c in [(2,1,0),(2,1,2),(3,1,2),(2,2,0),(2,2,1),(2,2,2),(3,2,1),(2,3,0),(2,3,1)]:
        check(p,r,c)
    exhaustive_regularity_witness(2,2,1)
    print('VERIFY_OK')

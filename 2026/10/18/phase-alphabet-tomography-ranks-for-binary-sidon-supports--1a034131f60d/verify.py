"""Exact support-count checks for finite Boolean Gabor tomography examples."""
from itertools import combinations

IRREDUCIBLES = {4: 0b111, 8: 0b1011, 16: 0b10011}

def mul(a,b,q):
    poly=IRREDUCIBLES[q]; out=0
    while b:
        if b&1: out ^= a
        b >>=1; a <<=1
        if a&q: a ^= poly
    return out

def powf(x,n,q):
    r=1
    while n:
        if n&1:r=mul(r,x,q)
        x=mul(x,x,q);n>>=1
    return r

def tr(a,q):
    r=0; x=a
    for _ in range(q.bit_length()-1):
        r^=x;x=mul(x,x,q)
    assert r in (0,1)
    return r

def ch(xi,x,q):
    z=mul(xi[0],x[0],q)^mul(xi[1],x[1],q)
    return 1 if tr(z,q)==0 else -1

def check(q):
    pts=[(t,powf(t,q-2,q)) for t in range(1,q)]
    k=q-1; N=q*q
    pair={}
    for i,j in combinations(range(k),2):
        h=(pts[i][0]^pts[j][0],pts[i][1]^pts[j][1])
        assert h!=(0,0) and h not in pair
        pair[h]=(i,j)
    assert len(pair)==k*(k-1)//2
    axes=[(a,b) for a in range(q) for b in range(q)]
    diag=[sum(ch(xi,x,q) for x in pts) for xi in axes]
    assert all(v%2 for v in diag)
    flat=0;coded=0
    for h,(i,j) in pair.items():
        zz=[ch(xi,h,q) for xi in axes]
        assert zz.count(1)==zz.count(-1)==N//2
        flat+=zz.count(1)
        coded+=N  # odd-order root phases forbid either cancellation sign
    flat+=sum(v!=0 for v in diag)
    coded+=sum(v!=0 for v in diag)
    want_flat=N + N*k*(k-1)//4
    want_coded=N + N*k*(k-1)//2
    assert flat==want_flat and coded==want_coded
    print(f'q={q}: support={k}, unordered_pairs={len(pair)}, diagonal_nonzero={N}, flat_rank={flat}, phase_coded_rank={coded}, strict_gain={coded-flat}')

for q in (4,8,16): check(q)
print('ALL CHECKS PASSED')

"""Exact checks for the symmetry character of independence complexes on 6-by-n grids.

No external packages required. Run `python3 grid_character_verify.py`.
"""
from functools import lru_cache
from itertools import product

STATES = tuple(s for s in range(1 << 6) if s & (s << 1) == 0)
SIZE = len(STATES)
WEIGHTS = tuple(-1 if s.bit_count() % 2 else 1 for s in STATES)
T = tuple(tuple(WEIGHTS[j] if not (p & q) else 0
                for j, q in enumerate(STATES)) for p in STATES)
ONES = (1,) * SIZE
SEAM = tuple(int((s & 33) != 33 and (s & 18) != 18) for s in STATES)
MIDDLE = tuple(1 - int((s & 33) == 0) - int((s & 18) == 0)
               for s in STATES)
Z56 = (-1, 1, 1, -1, 1, 1, -1, 3, 1, -1, 3, -3, -1, 3,
       -3, 3, 3, -3, 3, -1, -3, 5, -1, 1, 5, -5, 1, 1,
       -5, 5, 1, -1, 5, -3, -1, 3, -3, 3, 3, -3, 3, -1,
       -3, 3, -1, 1, 3, -1, 1, 1, -1, 1, 1, -1, 1, 1)
F28 = (1, -1, -1, 3, 1, -3, 1, 5, -1, -5, 3, 5, -3, -3,
       5, 3, -5, -1, 5, 1, -3, 1, 3, -1, -1, 1, 1, 1)

def mv(v):
    return tuple(sum(row[j] * v[j] for j in range(SIZE)) for row in T)

def left_mv(v):
    return tuple(sum(v[i] * T[i][j] for i in range(SIZE)) for j in range(SIZE))

def power_apply(vec, exponent):
    for _ in range(exponent):
        vec = mv(vec)
    return vec

def dot(u,v):
    return sum(a*b for a,b in zip(u,v))

def strip(k):
    if k == 0: return 1
    return dot(WEIGHTS, power_apply(ONES, k-1))

def halfturn(n):
    if n == 1: return -1
    k=n//2
    return dot(WEIGHTS, power_apply(SEAM if n % 2 == 0 else MIDDLE, k-1))

def ladder(n):
    a,b,c,d=1,0,0,0
    # independently enumerate compatible 2-row column masks by dynamic programming
    dp={0:1}
    for _ in range(n):
        nextdp={}
        for q in (0,1,2):
            nextdp[q]=(-1 if q else 1)*sum(v for p,v in dp.items() if not p&q)
        dp=nextdp
    return sum(dp.values())

def quotient_poly(n, which):
    """Independent cross-check by explicit graph orbits, loop removal, recursion."""
    vertices=tuple(product(range(n),range(6)))
    def f(v):
        x,y=v
        if which=='a':return n-1-x,y
        if which=='b':return x,5-y
        if which=='ab':return n-1-x,5-y
        return x,y
    visited=set(); orbits=[]
    for v in vertices:
        if v not in visited:
            orbit={v,f(v)}
            visited.update(orbit)
            orbits.append(orbit)
    edges=set()
    for x,y in vertices:
        for xx,yy in ((x+1,y),(x,y+1)):
            if 0<=xx<n and 0<=yy<6:
                edges.add((x,y,xx,yy))
    contain={v:i for i,orbit in enumerate(orbits) for v in orbit}
    bad=set(); adj=[0]*len(orbits)
    for x,y,xx,yy in edges:
        i=contain[(x,y)];j=contain[(xx,yy)]
        if i==j:bad.add(i)
        else:adj[i]|=1<<j;adj[j]|=1<<i
    good=[i for i in range(len(orbits)) if i not in bad]
    masks={j:i for i,j in enumerate(good)}
    quotient=[]
    for j in good:
        bit=0
        for h in good:
            if adj[j] & (1<<h):bit|=1<<masks[h]
        quotient.append(bit)
    @lru_cache(None)
    def z(mask):
        if mask==0:return 1
        bit=mask & -mask
        i=bit.bit_length()-1
        return z(mask^bit) - z(mask & ~bit & ~quotient[i])
    return z((1<<len(good))-1)

def verify():
    assert SIZE==21
    assert all(power_apply(e,28)==e for e in (ONES,SEAM,MIDDLE))
    assert (strip(0),strip(28))==(1,1)
    assert tuple(strip(i) for i in range(1,29))==F28
    assert tuple(halfturn(i) for i in range(1,57))==Z56
    assert halfturn(57)==halfturn(1)
    assert all(halfturn(i+56)==halfturn(i) for i in range(1,121))
    assert all(strip(i+28)==strip(i) for i in range(0,57))
    # The three-state ladder transfer certifies period four for every order.
    ladder_states=(0,1,2)
    ladder_weights=(1,-1,-1)
    ladder_matrix=tuple(tuple(ladder_weights[j] if not (p & q) else 0
                                for j,q in enumerate(ladder_states)) for p in ladder_states)
    def ladder_matvec(vec):
        return tuple(sum(ladder_matrix[i][j]*vec[j] for j in range(3)) for i in range(3))
    e=(1,1,1)
    for _ in range(4):e=ladder_matvec(e)
    assert e==(1,1,1)
    assert all(ladder(i)==(1,-1,-1,1)[i%4] for i in range(25))
    for p in (28,8,7):assert any(Z56[i]!=Z56[(i+p)%56] for i in range(56))
    assert set(map(abs,Z56))=={1,3,5}
    assert (strip(8),strip(4-1),ladder(8),halfturn(8))==(5,-1,1,3)  # a quotient n=8 -> 3 columns
    # Entire four-symmetry character independently obtained from orbit quotient graphs.
    direct_cases=0
    for n in range(1,9):
        expected={"id":strip(n),
                  "a":strip((n+1)//2 if n%2 else n//2-1),
                  "b":ladder(n),"ab":halfturn(n)}
        for action,z_expected in expected.items():
            assert quotient_poly(n,action)==z_expected,(n,action)
            direct_cases+=1
    # Character multiplicities for real/rational irreducibles of C2 x C2.
    for n in range(1,121):
        chars=(-strip(n),
               -strip((n+1)//2 if n%2 else n//2-1),
               -ladder(n),-halfturn(n))
        for sign_a,sign_b in product((1,-1),repeat=2):
            assert (chars[0]+sign_a*chars[1]+sign_b*chars[2]+sign_a*sign_b*chars[3])%4==0
    print('VERIFY_OK', 'state_count=',SIZE,'direct_quotient_cases=',direct_cases,'period=',56)

if __name__=='__main__': verify()

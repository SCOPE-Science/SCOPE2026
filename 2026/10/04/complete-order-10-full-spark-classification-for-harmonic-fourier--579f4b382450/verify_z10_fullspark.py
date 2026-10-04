from itertools import combinations, permutations
from math import floor, ceil

N=10
DIVS=(1,2,5,10)
UNITS=(1,3,7,9)
PHI10=(1,-1,1,-1,1) # 1-x+x^2-x^3+x^4

# Exact arithmetic in Z[z]/(Phi_10), basis 1,z,z^2,z^3.
def add(a,b):
    return tuple(a[i]+b[i] for i in range(4))
def neg(a):
    return tuple(-x for x in a)
def mul(a,b):
    t=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            t[i+j]+=x*y
    # x^4 = x^3 - x^2 + x - 1
    for d in range(6,3,-1):
        c=t[d]
        if c:
            t[d]=0
            t[d-1]+=c
            t[d-2]-=c
            t[d-3]+=c
            t[d-4]-=c
    return tuple(t[:4])
ZERO=(0,0,0,0)
ONE=(1,0,0,0)
Z=(0,1,0,0)
POW=[ONE]
for _ in range(1,N):
    POW.append(mul(POW[-1],Z))
assert mul(POW[5],POW[5])==ONE

def perm_sign(p):
    inv=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            inv += p[i]>p[j]
    return -1 if inv%2 else 1

PERMS={m:[(p,perm_sign(p)) for p in permutations(range(m))] for m in range(1,6)}

def det_exact(rows,cols):
    m=len(rows)
    acc=ZERO
    for p,sgn in PERMS[m]:
        term=ONE
        for i in range(m):
            term=mul(term, POW[(rows[i]*cols[p[i]])%N])
        acc=add(acc, term if sgn==1 else neg(term))
    return acc

def uniform(S):
    M=len(S)
    for d in DIVS:
        counts=[0]*d
        for x in S:
            counts[x%d]+=1
        lo=M//d
        hi=(M+d-1)//d
        if any(c not in (lo,hi) for c in counts):
            return False
    return True

def affine_image(S,a,b):
    return tuple(sorted((a*x+b)%N for x in S))
def canon(S):
    return min(affine_image(S,a,b) for a in UNITS for b in range(N))

def fullspark_exact(S):
    m=len(S)
    assert 1 <= m <= 5
    for C in combinations(range(N),m):
        if det_exact(S,C)==ZERO:
            return False,C
    return True,None

# Exact census for dimensions <=5.
small={}
for m in range(1,6):
    U=[S for S in combinations(range(N),m) if uniform(S)]
    full=[]; bad=[]
    for S in U:
        ok,w=fullspark_exact(S)
        (full if ok else bad).append((S,w) if not ok else S)
    small[m]=(U,full,bad)

expected_orbits={
 1:{(0,)},
 2:{(0,1)},
 3:{(0,1,2),(0,1,3)},
 4:{(0,1,2,3),(0,1,3,4)},
 5:{(0,1,2,3,4)},
}
for m,(U,full,bad) in small.items():
    orbs={canon(S) for S in U}
    assert orbs==expected_orbits[m], (m,orbs)

# The unique bad affine orbit in size 4 is the ACM counterexample orbit.
U4,full4,bad4=small[4]
bad_sets4={S for S,_ in bad4}
assert bad_sets4=={S for S in U4 if canon(S)==(0,1,3,4)}
assert len(bad_sets4)==10
# Exact witness stated in Alexeev-Cahill-Mixon.
assert det_exact((0,1,3,4),(0,1,2,6))==ZERO

# All uniformly distributed size-5 sets are exact full spark.
assert len(small[5][0])==20 and len(small[5][2])==0

# Complement symmetry supplies sizes 6..9.
summary=[]
for m in range(1,10):
    U=[S for S in combinations(range(N),m) if uniform(S)]
    if m<=5:
        bad={S for S,_ in small[m][2]}
    else:
        bad=set()
        for S in U:
            C=tuple(sorted(set(range(N))-set(S)))
            if len(C)<=5:
                ok,_=fullspark_exact(C)
                if not ok: bad.add(S)
    full_count=len(U)-len(bad)
    summary.append((m,len(U),full_count,len(bad),len({canon(S) for S in U})))

# The theorem: among uniformly distributed proper nonempty subsets, only the
# affine orbit of {0,1,3,4} and its complements fail full spark.
for m in range(1,10):
    U=[S for S in combinations(range(N),m) if uniform(S)]
    for S in U:
        if m<=5:
            ok,_=fullspark_exact(S)
        else:
            C=tuple(sorted(set(range(N))-set(S)))
            ok,_=fullspark_exact(C)
        exceptional=(canon(S)==(0,1,3,4)) or (canon(tuple(sorted(set(range(N))-set(S))))==(0,1,3,4))
        assert ok == (not exceptional), (S,ok,exceptional)

print('m uniform full nonfull affine_orbits')
for row in summary:
    print(*row)
print('bad4_orbit_size',len(bad_sets4))
print('bad4_rep',(0,1,3,4),'witness_cols',(0,1,2,6),'det',det_exact((0,1,3,4),(0,1,2,6)))
print('VERIFY_OK')

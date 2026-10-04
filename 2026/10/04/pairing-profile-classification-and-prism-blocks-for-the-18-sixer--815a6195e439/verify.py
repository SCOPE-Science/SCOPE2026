from fractions import Fraction
from itertools import combinations, product, permutations
from collections import Counter, defaultdict, deque

# Q(w), w^2+w+1=0, represented by a+b w.
def A(x=0,b=0): return (Fraction(x),Fraction(b))
ZERO=A(0); ONE=A(1); W=A(0,1); W2=A(-1,-1)
ROOTS=(ONE,W,W2)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)
def inv(x):
    a,b=x; n=a*a-a*b+b*b
    if n==0: raise ZeroDivisionError
    return ((a-b)/n, -b/n)
def div(x,y): return mul(x,inv(y))
def eq0(x): return x==ZERO

def rref(rows):
    M=[list(r) for r in rows]; m=len(M); n=len(M[0]); piv=[]; rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if not eq0(M[i][c])),None)
        if p is None: continue
        M[rr],M[p]=M[p],M[rr]
        z=inv(M[rr][c]); M[rr]=[mul(z,v) for v in M[rr]]
        for i in range(m):
            if i!=rr and not eq0(M[i][c]):
                f=M[i][c]; M[i]=[sub(M[i][j],mul(f,M[rr][j])) for j in range(n)]
        piv.append(c); rr+=1
        if rr==m: break
    return tuple(tuple(v for v in row) for row in M), len(piv)

def rank(rows): return rref(rows)[1]

pairings=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
lines=[]; family=[]; params=[]
for pi,pairs in enumerate(pairings):
  for a in ROOTS:
    for b in ROOTS:
      rows=[]
      for (i,j),coef in zip(pairs,(a,b)):
        row=[ZERO]*4; row[i]=ONE; row[j]=coef; rows.append(tuple(row))
      key,_=rref(rows)
      lines.append(key); family.append(pi); params.append((a,b))
assert len(lines)==27 and len(set(lines))==27
lookup={L:i for i,L in enumerate(lines)}

def skew(i,j): return rank(lines[i]+lines[j])==4
sk=[[False]*27 for _ in range(27)]
for i in range(27):
  for j in range(i+1,27): sk[i][j]=sk[j][i]=skew(i,j)

sixers=[]
def extend(chosen,start):
    if len(chosen)==6:
        sixers.append(tuple(chosen)); return
    for i in range(start,27):
        if all(sk[i][j] for j in chosen): extend(chosen+[i],i+1)
extend([],0)
assert len(sixers)==72
Sset=set(sixers)

def matmul_row(row,T):
    return tuple(sum_field(mul(row[k],T[k][j]) for k in range(4)) for j in range(4))
def sum_field(xs):
    z=ZERO
    for x in xs: z=add(z,x)
    return z

def transform_line(L,perm,diag):
    # y=T x with y_i=diag_i*x_perm[i]; equations in y become E*T, enough for set action.
    T=[[ZERO]*4 for _ in range(4)]
    for i in range(4): T[i][perm[i]]=diag[i]
    rows=[matmul_row(row,T) for row in L]
    key,_=rref(rows)
    return lookup[key]

autos=[]; seen=set()
for perm in permutations(range(4)):
  for exps in product(range(3), repeat=3):
    diag=(ONE, ROOTS[exps[0]], ROOTS[exps[1]], ROOTS[exps[2]])
    mp=tuple(transform_line(L,perm,diag) for L in lines)
    if mp not in seen: seen.add(mp); autos.append(mp)
assert len(autos)==648

# orbits on sixers
unseen=set(sixers); orbits=[]
while unseen:
    s=min(unseen); orb={tuple(sorted(mp[i] for i in s)) for mp in autos}
    assert orb <= Sset
    orbits.append(orb); unseen-=orb
orbits.sort(key=len)
assert [len(o) for o in orbits]==[18,54]
O18,O54=orbits

def prof(s): return tuple(sorted(Counter(family[i] for i in s).values() | Counter()))
# direct profile with zeros included
def profile(s):
    c=Counter(family[i] for i in s)
    return tuple(sorted((c[0],c[1],c[2])))
ph=Counter(profile(s) for s in sixers)
assert ph==Counter({(0,3,3):18,(2,2,2):54})
assert all(profile(s)==(0,3,3) for s in O18)
assert all(profile(s)==(2,2,2) for s in O54)

blocks={r:[] for r in range(3)}
for s in O18:
    omitted=[r for r in range(3) if all(family[i]!=r for i in s)]
    assert len(omitted)==1
    blocks[omitted[0]].append(s)
assert [len(blocks[r]) for r in range(3)]==[6,6,6]

def inter(a,b): return len(set(a)&set(b))
# cross-block all exactly one
for r,t in combinations(range(3),2):
    vals=Counter(inter(a,b) for a in blocks[r] for b in blocks[t])
    assert vals==Counter({1:36})

for r in range(3):
    B=blocks[r]
    vals=Counter(inter(a,b) for a,b in combinations(B,2))
    assert vals==Counter({0:9,3:6})
    # disjoint graph is triangular prism: connected, 3-regular, exactly two triangles
    adj0={i:set() for i in range(6)}; adj3={i:set() for i in range(6)}
    for i,j in combinations(range(6),2):
        k=inter(B[i],B[j])
        if k==0: adj0[i].add(j); adj0[j].add(i)
        if k==3: adj3[i].add(j); adj3[j].add(i)
    assert sorted(map(len,adj0.values()))==[3]*6
    q={0}; dq=[0]
    while dq:
        u=dq.pop()
        for v in adj0[u]:
            if v not in q: q.add(v); dq.append(v)
    assert len(q)==6
    tri=sum(1 for c in combinations(range(6),3) if all(v in adj0[u] for u,v in combinations(c,2)))
    assert tri==2
    assert sorted(map(len,adj3.values()))==[2]*6
    q={0}; dq=[0]
    while dq:
        u=dq.pop()
        for v in adj3[u]:
            if v not in q: q.add(v); dq.append(v)
    assert len(q)==6
    tri3=sum(1 for c in combinations(range(6),3) if all(v in adj3[u] for u,v in combinations(c,2)))
    assert tri3==0

pair18=Counter(inter(a,b) for a,b in combinations(O18,2))
assert pair18==Counter({1:108,0:27,3:18})
print('lines=27 sixers=72 aut=648 orbit_sizes=18,54')
print('profile_histogram=(0,3,3):18,(2,2,2):54')
print('orbit18_blocks=6,6,6')
print('cross_block_intersection=1 for all 108 pairs')
print('within_each_block: intersection0=9 intersection3=6; disjoint_graph=triangular_prism; intersection3_graph=C6')
print('orbit18_global_pair_intersections: 0=27 1=108 3=18')
print('VERIFY_OK')

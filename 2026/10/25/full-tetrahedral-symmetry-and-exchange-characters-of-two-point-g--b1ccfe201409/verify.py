"""Self-contained finite checker for the ordered two-particle graph configuration example.
Run with Python 3; uses only the standard library. All arithmetic is exact.
"""
from itertools import combinations, permutations
from collections import Counter

MOD = 1000003
V = [(i,j) for i in range(4) for j in range(4) if i!=j]
VID = {v:k for k,v in enumerate(V)}
E = sorted(tuple(sorted((VID[a],VID[b]))) for a,b in combinations(V,2)
           if a[0]==b[0] or a==b[::-1])
EID = {e:k for k,e in enumerate(E)}
C0 = [(a,b) for a in range(12) for b in range(12) if a!=b]
EV = [(e,v) for e in range(18) for v in range(12) if v not in E[e]]
C1 = [(0,e,v) for e,v in EV] + [(1,v,e) for e,v in EV]
C1ID = {t:k for k,t in enumerate(C1)}
C2 = [(e,f) for e in range(18) for f in range(18) if not set(E[e]) & set(E[f])]
C2ID = {t:k for k,t in enumerate(C2)}
assert (len(V),len(E),len(C0),len(C1),len(C2))==(12,18,132,360,234)

# Signed boundary of an oriented product square (edge e) x (edge f).
B = [[0]*len(C2) for _ in C1]
for k,(e,f) in enumerate(C2):
    a,b=E[e]; c,d=E[f]
    for s,x in ((1,(1,b,f)),(-1,(1,a,f)),(-1,(0,e,d)),(1,(0,e,c))):
        B[C1ID[x]][k]=s

def echelon_columns(matrix, mod=MOD):
    A = [[x%mod for x in row] for row in matrix]
    r=0; piv=[]
    m=len(A); n=len(A[0]);
    for c in range(n):
        k=next((t for t in range(r,m) if A[t][c]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        inv=pow(A[r][c],-1,mod)
        A[r][c:]=[(v*inv)%mod for v in A[r][c:]]
        for t in range(m):
            if t==r or not A[t][c]:continue
            v=A[t][c];tt=A[t];rr=A[r]
            for col in range(c,n):tt[col]=(tt[col]-v*rr[col])%mod
        piv.append(c);r+=1
        if r==m:break
    return A,piv

R,piv=echelon_columns(B)
free=[c for c in range(len(C2)) if c not in set(piv)]
assert (len(piv),len(free))==(214,20)

# Explicit 20 integral 2-cycles, each a product of vertex-disjoint graph cycles.
adj={i:set() for i in range(12)}
for a,b in E:adj[a].add(b);adj[b].add(a)
cycles=[]
for first in range(12):
    def dfs(path):
        for u in sorted(adj[path[-1]]):
            if u==first and len(path)>=3 and path[1]<path[-1]:
                cycles.append(tuple(path))
            elif u>first and u not in path:
                dfs(path+[u])
    dfs([first])
assert len(cycles)==84

def torus_cycle(c,d):
    vec=[0]*len(C2)
    for a,b in zip(c,c[1:]+c[:1]):
        e=EID[tuple(sorted((a,b)))]; es=1 if a<b else -1
        for u,v in zip(d,d[1:]+d[:1]):
            f=EID[tuple(sorted((u,v)))]; fs=1 if u<v else -1
            vec[C2ID[(e,f)]]+=es*fs
    return vec

basis=[];first_nonzero=[];chosen=[]
for a,c in enumerate(cycles):
    for b,d in enumerate(cycles):
        if set(c)&set(d):continue
        vec=torus_cycle(c,d)
        if any(sum(row[j]*vec[j] for j in range(len(C2))) for row in B):
            raise AssertionError('invalid integral product cycle')
        v=[x%MOD for x in vec]
        for pivot,w in zip(first_nonzero,basis):
            if v[pivot]:
                fac=v[pivot]
                v=[(x-fac*y)%MOD for x,y in zip(v,w)]
        nz=next((t for t,x in enumerate(v) if x),None)
        if nz is None:continue
        inv=pow(v[nz],-1,MOD)
        basis.append([(x*inv)%MOD for x in v])
        first_nonzero.append(nz)
        chosen.append((a,b))
        if len(chosen)==20:break
    if len(chosen)==20:break
assert len(chosen)==20
# Thus rank_Q(B) >= 214 by the nonzero modular minor and <=214
# by the independent integral kernel cycles: rank_Q(B)=214.

K=[[0]*20 for _ in C2]
for k,j in enumerate(free):
    K[j][k]=1
    for i,q in enumerate(piv):K[q][k]=(-R[i][j])%MOD
for row in B:
    assert all(sum(a*K[j][k] for j,a in enumerate(row) if a)%MOD==0 for k in range(20))

def perm_type(p):
    seen=set();lengths=[]
    for i in range(4):
        if i in seen:continue
        x=i;s=0
        while x not in seen:
            seen.add(x);s+=1;x=p[x]
        lengths.append(s)
    return tuple(sorted(lengths,reverse=True))

def trace_kernel(p,swap):
    vm=[VID[(p[i],p[j])] for i,j in V]
    em=[];eps=[]
    for a,b in E:
        x,y=vm[a],vm[b]
        em.append(EID[tuple(sorted((x,y)))])
        eps.append(1 if x<y else -1)
    # Coefficient of the free index in the moved kernel basis vector.
    total=0
    for col,(e,f) in enumerate(C2):
        target=C2ID[(em[f],em[e]) if swap else (em[e],em[f])]
        if target not in FREEID:continue
        k=FREEID[target]
        s=(-1 if swap else 1)*eps[e]*eps[f]
        total+=s*K[col][k]
    total%=MOD
    return total if total<MOD//2 else total-MOD

FREEID={j:k for k,j in enumerate(free)}
classes={}
for p in permutations(range(4)):
    t=perm_type(p)
    traces=(trace_kernel(p,False),trace_kernel(p,True))
    if t in classes:
        assert traces==classes[t][0]
        classes[t]=(traces,classes[t][1]+1)
    else:classes[t]=(traces,1)
TYPES=((1,1,1,1),(2,1,1),(2,2),(3,1),(4,))
assert [classes[t][1] for t in TYPES]==[1,6,3,8,6]
assert [classes[t][0] for t in TYPES]==[(20,0),(6,-2),(0,-4),(2,0),(0,0)]
plus=[(classes[t][0][0]+classes[t][0][1])//2 for t in TYPES]
minus=[(classes[t][0][0]-classes[t][0][1])//2 for t in TYPES]
assert plus==[10,2,-2,1,0] and minus==[10,4,2,1,0]
characters={
  'triv':(1,1,1,1,1),
  'sgn':(1,-1,1,1,-1),
  'std':(3,1,-1,0,-1),
  'std_sgn':(3,-1,-1,0,1),
  'two_dim':(2,0,2,-1,0),
}
sizes=[classes[t][1] for t in TYPES]
def decomposition(character):
    v={name:sum(n*a*b for n,a,b in zip(sizes,character,chi))//24
       for name,chi in characters.items()}
    assert all(sum(n*a*b for n,a,b in zip(sizes,character,chi))%24==0
               for chi in characters.values())
    return v
assert decomposition(plus)=={'triv':1,'sgn':0,'std':2,'std_sgn':1,'two_dim':0}
assert decomposition(minus)=={'triv':2,'sgn':0,'std':2,'std_sgn':0,'two_dim':1}
print('graph vertices=12 edges=18; cells=',(132,360,234))
print('boundary rank_Q=214 certified by 214 nonzero modular pivots and 20 independent integral 2-cycles')
print('ordered rational H2 dimension=20')
print('class data (cycle type, multiplicity, traces for g and g*particle_swap):')
for t in TYPES:print(t,classes[t])
print('exchange-even character',tuple(plus),decomposition(plus))
print('exchange-odd character',tuple(minus),decomposition(minus))
print('VERIFY_OK')

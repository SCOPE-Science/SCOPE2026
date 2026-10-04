#!/usr/bin/env python3
from collections import Counter, defaultdict, deque

N=20
EDGES=set()
def add(a,b):
    if a>b: a,b=b,a
    EDGES.add((a,b))
for i in range(10):
    add(i,(i+1)%10)
    add(i,10+i)
    add(10+i,10+((i+3)%10))
assert len(EDGES)==30
ADJ=[0]*N
for a,b in EDGES:
    ADJ[a]|=1<<b; ADJ[b]|=1<<a

faces=[]
for m in range(1<<N):
    ok=True
    x=m
    while x:
        l=x & -x; v=l.bit_length()-1; x-=l
        if ADJ[v]&x:
            ok=False; break
    if ok: faces.append(m)
FSET=set(faces)
fc=Counter(m.bit_count()-1 for m in faces if m)
assert len(faces)==6212
assert max(m.bit_count() for m in faces)==10

ORDER=[9,6,16,1,13,0,8,18,17,12,2,19,15,14,3,10,11,5,4,7]
unmatched=set(faces)
pair={}
for v in ORDER:
    bit=1<<v
    for low in sorted([m for m in unmatched if not (m&bit) and (m|bit) in unmatched]):
        high=low|bit
        if low in unmatched and high in unmatched:
            pair[low]=high; pair[high]=low
            unmatched.remove(low); unmatched.remove(high)
critical=sorted(unmatched)
cc=Counter(m.bit_count()-1 for m in critical if m)
assert 0 not in critical
assert cc==Counter({5:5,4:1}), cc

# All Hasse covers, oriented upward if unmatched and downward if matched.
indeg={m:0 for m in faces}; out=defaultdict(list); covers=0
for high in faces:
    y=high
    while y:
        l=y & -y; y-=l
        low=high^l
        covers+=1
        if pair.get(low)==high:
            a,b=high,low
        else:
            a,b=low,high
        out[a].append(b); indeg[b]+=1
q=deque(sorted(m for m,d in indeg.items() if d==0)); seen=0
while q:
    a=q.popleft(); seen+=1
    for b in out[a]:
        indeg[b]-=1
        if indeg[b]==0:q.append(b)
assert seen==len(faces)

# Sparse rank over F2 for simplicial boundary maps.
def rank_f2(cols):
    piv={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x; break
    return len(piv)
ranks={}
by_size={s:sorted(m for m in faces if m.bit_count()==s) for s in range(1,11)}
for s in range(2,11):
    rows={m:i for i,m in enumerate(by_size[s-1])}
    cols=[]
    for high in by_size[s]:
        col=0; y=high
        while y:
            l=y & -y; y-=l
            col ^= 1<<rows[high^l]
        cols.append(col)
    ranks[s-1]=rank_f2(cols)
betti={}
for dim in range(0,10):
    ns=len(by_size[dim+1])
    rd=ranks.get(dim,0)  # d_dim C_dim -> C_dim-1, d_0=0
    rup=ranks.get(dim+1,0)
    betti[dim]=ns-rd-rup
assert betti=={0:1,1:0,2:0,3:0,4:1,5:5,6:0,7:0,8:0,9:0}, betti

# Exact integral Morse boundary C5^Morse -> C4^Morse via signed gradient paths.
crit4=[m for m in critical if m.bit_count()==5]
crit5=[m for m in critical if m.bit_count()==6]
assert len(crit4)==1 and len(crit5)==5
tau=crit4[0]
def inc(high, low):
    verts=[i for i in range(N) if high>>i&1]
    removed=(high^low).bit_length()-1
    return -1 if verts.index(removed)%2 else 1
memo={}; active=set()
def coeff(alpha):
    if alpha in memo:return memo[alpha]
    assert alpha not in active
    active.add(alpha)
    val=inc(alpha,tau) if (tau & alpha)==tau and alpha.bit_count()==6 else 0
    y=alpha
    while y:
        l=y & -y; y-=l
        beta=alpha^l
        ap=pair.get(beta)
        if ap is not None and ap.bit_count()==6 and ap!=alpha:
            val -= inc(alpha,beta)*inc(ap,beta)*coeff(ap)
    active.remove(alpha); memo[alpha]=val; return val
morse=[coeff(a) for a in crit5]
assert morse==[0]*5, morse

def verts(m): return [i for i in range(N) if m>>i&1]
print('vertices',N,'edges',len(EDGES))
print('independent_faces_including_empty',len(faces))
print('f_vector', [fc[d] for d in range(10)])
print('hasse_covers',covers)
print('critical_4_cell',verts(tau))
print('critical_5_cells',[verts(m) for m in crit5])
print('critical_counts',dict(sorted(cc.items())))
print('boundary_ranks_F2',ranks)
print('betti_F2',betti)
print('morse_d5_to_d4_Z',morse)
print('DESARGUES_IND_VERIFY_OK')

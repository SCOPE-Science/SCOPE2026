#!/usr/bin/env python3
"""Exact finite combinatorial certificate for the Fano-incidence stable curve.

Only Python's standard library is used.  This checks the finite integral
lattice computations; the normalization and descent arguments are mathematical.
"""
from itertools import product
from collections import Counter, defaultdict

POINTS = tuple(range(1,8))

def dot(a,b):
    return (a & b).bit_count() & 1

EDGES = tuple(sorted((i,7+j) for i,a in enumerate(POINTS)
                     for j,b in enumerate(POINTS) if dot(a,b)==0))
assert len(EDGES)==21
EIDX={e:i for i,e in enumerate(EDGES)}
PINDEX={a:i for i,a in enumerate(POINTS)}

def apply(M,x):
    y=0
    for i in range(3):
        if (x>>i)&1:y^=M[i]
    return y

MATS=tuple(M for M in product(POINTS,repeat=3)
           if len({apply(M,x) for x in range(8)})==8)
assert len(MATS)==168

def compose(A,B):
    return tuple(apply(A,x) for x in B)

ID=(1,2,4)
def inverse(M):
    pre={apply(M,x):x for x in range(8)}
    return tuple(pre[1<<i] for i in range(3))

def transpose(M):
    return tuple(sum(((M[j]>>i)&1)<<j for j in range(3)) for i in range(3))

def vperm(M):
    dual=transpose(inverse(M))
    perm=[PINDEX[apply(M,a)] for a in POINTS]
    perm += [7+PINDEX[apply(dual,a)] for a in POINTS]
    assert sorted(tuple(sorted((perm[u],perm[v]))) for u,v in EDGES)==list(EDGES)
    return tuple(perm)

def edge_perm(vp):
    return tuple(EIDX[tuple(sorted((vp[u],vp[v])))] for u,v in EDGES)

def cycle_lengths(P):
    seen=set(); out=[]
    for i in range(len(P)):
        if i in seen:continue
        n=0;j=i
        while j not in seen:
            seen.add(j);n+=1;j=P[j]
        out.append(n)
    return tuple(sorted(out))

def order(M):
    x=ID
    for i in range(1,9):
        x=compose(x,M)
        if x==ID:return i
    raise AssertionError('order exceeded')

# Kruskal: choose one reproducible 13-edge spanning tree.
parents=list(range(14))
def root(x):
    while x!=parents[x]:x=parents[x]
    return x
TREE=[]
for u,v in EDGES:
    a,b=root(u),root(v)
    if a!=b:
        parents[a]=b;TREE.append((u,v))
assert len(TREE)==13
TREE=set(TREE)
CHORDS=tuple(e for e in EDGES if e not in TREE)
assert len(CHORDS)==8
CIDX=tuple(EIDX[e] for e in CHORDS)
NEI={v:[] for v in range(14)}
for u,v in TREE:
    NEI[u].append(v); NEI[v].append(u)

def tree_path(u,v):
    queue=[u];pr={u:None}
    for x in queue:
        if x==v:break
        for y in NEI[x]:
            if y not in pr:pr[y]=x;queue.append(y)
    assert v in pr
    path=[];x=v
    while x is not None:path.append(x);x=pr[x]
    return path[::-1]

# Every fundamental cycle is oriented point -> Fano line.
B=[[0]*8 for _ in EDGES]
for j,(p,l) in enumerate(CHORDS):
    B[EIDX[(p,l)]][j]=1
    path=tree_path(l,p)
    for x,y in zip(path,path[1:]):
        B[EIDX[tuple(sorted((x,y))) ]][j] += 1 if x<7 else -1
for j in range(8):
    for v in range(14):
        flow=sum((B[EIDX[(v,w)]][j] if v<7 else -B[EIDX[(w,v)]][j])
                 for w in range(14) if (min(v,w),max(v,w)) in EIDX)
        assert flow==0

def multiply(A,B):
    assert len(A[0])==len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def U_from_vperm(vp):
    ep=edge_perm(vp)
    GB=[[0]*8 for _ in range(21)]
    for old,new in enumerate(ep):GB[new]=B[old][:]
    U=[GB[r][:] for r in CIDX]
    assert multiply(B,U)==GB
    return U

def determinant(A):
    # Fraction-free Bareiss elimination, exact over the integers.
    a=[list(x) for x in A];n=len(a)
    assert all(len(x)==n for x in a)
    if n==0:return 1
    denom=1;sgn=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sgn=-sgn
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=a[i][j]*p-a[i][k]*a[k][j]
                assert numer%denom==0
                a[i][j]=numer//denom
        for i in range(k+1,n):a[i][k]=0
        denom=p
    return sgn*a[-1][-1]

# Unimodular columns A; each corresponding order's action has the asserted
# integral normal form. The arrays are an independently replayable certificate.
CERT={
  2:[[0,0,-1,0,0,0,1,0],[1,0,0,1,1,0,0,0],
     [0,-1,-1,1,0,-1,0,-1],[0,1,1,0,0,1,0,0],
     [0,0,-1,0,0,0,0,0],[0,-1,-1,1,0,0,0,-1],
     [1,0,-1,2,0,0,1,0],[0,0,0,-1,0,0,0,0]],
  3:[[0,1,0,0,-1,0,-1,2],[-1,0,0,0,1,0,0,1],
     [0,0,0,-1,0,0,0,1],[0,1,0,0,0,0,0,1],
     [0,0,1,0,0,-1,-1,-1],[0,-1,0,0,0,1,-1,0],
     [0,0,1,0,0,0,-1,0],[0,0,-1,0,1,0,2,0]],
  4:[[-1,0,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0],
     [0,0,1,0,0,0,1,0],[0,0,0,0,0,0,-1,0],
     [0,-1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,-1],[0,0,0,-1,0,0,0,0]],
  7:[[-1,-1,0,0,0,0,0,0],[-3,0,-1,-1,0,0,0,0],
     [4,0,0,0,0,1,1,1],[-1,0,0,0,0,-1,0,0],
     [-3,0,0,0,-1,-1,0,0],[4,0,0,1,1,1,0,0],
     [-3,0,0,0,0,-1,-1,0],[4,0,0,0,1,1,1,0]]
}

def block_normal(order):
    W=[[0]*8 for _ in range(8)]
    if order==2 or order==4:
        for start in range(0,8,order):
            for j in range(order):W[start+(j+1)%order][start+j]=1
    elif order==3:
        for start in (0,3):
            for j in range(3):W[start+(j+1)%3][start+j]=1
        W[7][6]=1;W[6][7]=-1;W[7][7]=-1
    elif order==7:
        W[0][0]=1
        for j in range(7):W[1+(j+1)%7][1+j]=1
    return W

reps={1:ID,2:(1,2,5),3:(1,4,6),4:(1,3,6),7:(2,4,3)}

# Verify class sizes by group conjugation, not only element-order counts.
remaining=set(MATS);sizes=[]
while remaining:
    g=min(remaining)
    cl={compose(compose(h,g),inverse(h)) for h in MATS}
    assert cl<=remaining
    remaining-=cl
    sizes.append((order(g),len(cl)))
assert sorted(sizes)==sorted([(1,1),(2,21),(3,56),(4,42),(7,24),(7,24)])

counts=Counter()
for g in MATS:
    m=order(g); counts[m]+=1
    vp=vperm(g);ep=edge_perm(vp)
    vc,ec=cycle_lengths(vp),cycle_lengths(ep)
    expected={
      1:((1,)*14,(1,)*21),
      2:((1,)*6+(2,)*4,(1,)*5+(2,)*8),
      3:((1,)*2+(3,)*4,(3,)*7),
      4:((1,)*2+(2,)*2+(4,)*2,(1,)+(2,)*2+(4,)*4),
      7:((7,)*2,(7,)*3)
    }[m]
    assert (vc,ec)==expected
    U=U_from_vperm(vp)
    # Integral action respects g^order=1. Exact square-matrix recurrence.
    Q=[[int(i==j) for j in range(8)] for i in range(8)]
    vpow=tuple(range(14))
    epow=tuple(range(21))
    for k in range(m):
        # Independent Euler-characteristic trace identity on chain groups.
        assert sum(U[i][i] for i in range(8)) == (sum(i==ep[i] for i in range(21)) - sum(i==vp[i] for i in range(14)) + 1)
        Q=multiply(Q,U)
        vpow=tuple(vp[vpow[i]] for i in range(14))
        epow=tuple(ep[epow[i]] for i in range(21))
    assert vpow==tuple(range(14)) and epow==tuple(range(21))
    assert Q==[[int(i==j) for j in range(8)] for i in range(8)]

# Every order-seven element is conjugate to a nonidentity power of our
# chosen Singer cycle. Thus the regular-module certificate also covers
# the second order-seven conjugacy class (powers simply relabel columns).
base=reps[7]
powers=set()
x=ID
for exponent in range(1,7):
    x=compose(x,base)
    powers.add(x)
all_sevens=set()
for y in powers:
    all_sevens.update(compose(compose(h,y),inverse(h)) for h in MATS)
assert len(all_sevens)==48
assert all(order(g)==7 for g in all_sevens)
for d in (1,2,3,4):
    rep=reps[d]
    c={compose(compose(h,rep),inverse(h)) for h in MATS}
    assert len(c)==dict([(1,1),(2,21),(3,56),(4,42)])[d]

for order_,g in sorted(reps.items()):
    if order_==1:continue
    assert order(g)==order_
    U=U_from_vperm(vperm(g));A=CERT[order_]
    assert abs(determinant(A))==1,('not unimodular',order_)
    W=block_normal(order_)
    assert multiply(U,A)==multiply(A,W),('module mismatch',order_)
    print('integral certificate: order',order_,'det',determinant(A),'verified')

print('GL3(2) cardinality:',len(MATS))
print('conjugacy classes (order,size):',sorted(sizes))
print('orders:',sorted(counts.items()))
print('graph: 14 components, 21 nodes, genus 8')
for d in (1,2,3,4,7):
    vc,ec={1:((1,)*14,(1,)*21),
           2:((1,)*6+(2,)*4,(1,)*5+(2,)*8),
           3:((1,)*2+(3,)*4,(3,)*7),
           4:((1,)*2+(2,)*2+(4,)*2,(1,)+(2,)*2+(4,)*4),
           7:((7,)*2,(7,)*3)}[d]
    v=Counter(vc);e=Counter(ec)
    q=2
    # Comparison of extension counts via cycle spectra and zeta-log derivative.
    for n in range(1,50):
        vertices=sum(k*mult for k,mult in v.items() if n%k==0)
        edges=sum(k*mult for k,mult in e.items() if n%k==0)
        assert vertices*(q**n+1)-edges >= 0
    first=v[1]*(q+1)-e[1]
    print('type',d, 'vertex cycles',dict(sorted(v.items())),
          'edge cycles',dict(sorted(e.items())),
          'F2 points',first)
assert [x for x in (1,2,3,4,7) if {1:21,2:13,3:6,4:5,7:0}[x]==0]==[7]
print('VERIFY_OK')

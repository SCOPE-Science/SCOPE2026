from itertools import product, combinations
from collections import deque, Counter


def rank_f2(cols):
    basis={}
    for x in cols:
        while x:
            i=x.bit_length()-1
            if i in basis:x^=basis[i]
            else:basis[i]=x;break
    return len(basis)

def norm(v):
    for a in v:
        if a&1:return tuple(v)

def symp(a,b):return (a[0]*b[2]+a[1]*b[3]+a[2]*b[0]+a[3]*b[1])&1

def build_W2():
    pts=sorted({norm(v) for v in product(range(2),repeat=4) if any(v)})
    pidx={p:i for i,p in enumerate(pts)}
    lines=set()
    for a,b in combinations(pts,2):
        if symp(a,b):continue
        c=tuple(a[i]^b[i] for i in range(4))
        lines.add(tuple(sorted((a,b,c))))
    lines=sorted(lines);off=len(pts);adj=[set() for _ in range(off+len(lines))]
    for j,L in enumerate(lines):
        for p in L:
            u=pidx[p];v=off+j;adj[u].add(v);adj[v].add(u)
    return [sorted(a) for a in adj],off

def distances(adj):
    D=[]
    for s in range(len(adj)):
        d=[99]*len(adj);d[s]=0;q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==99:d[v]=d[u]+1;q.append(v)
        D.append(d)
    return D

def chains(D,x,y,k,l):
    out=[];n=len(D)
    def rec(a,rem,steps):
        u=a[-1]
        if steps==0:
            if u==y and rem==0:out.append(tuple(a))
            return
        for v in range(n):
            if v==u:continue
            z=D[u][v]
            if 1<=z<=rem:rec(a+[v],rem-z,steps-1)
    rec([x],l,k)
    return out

def boundary_cols(D,dom,cod):
    idx={c:i for i,c in enumerate(cod)};cols=[]
    for c in dom:
        bits=0
        for i in range(1,len(c)-1):
            if D[c[i-1]][c[i+1]]==D[c[i-1]][c[i]]+D[c[i]][c[i+1]]:
                d=c[:i]+c[i+1:]
                if d in idx:bits^=1<<idx[d]
        cols.append(bits)
    return cols

def local(D,x,y):
    C={k:chains(D,x,y,k,5) for k in (2,3,4)}
    b3=boundary_cols(D,C[3],C[2]); b4=boundary_cols(D,C[4],C[3])
    # Check d3 d4=0 by composing bit columns.
    for col in b4:
        z=0;t=col
        while t:
            b=t&-t;i=b.bit_length()-1;z^=b3[i];t-=b
        assert z==0
    r3=rank_f2(b3);r4=rank_f2(b4)
    return (len(C[2]),len(C[3]),len(C[4]),r3,r4,len(C[3])-r3-r4)

def count_8cycles(adj):
    n=len(adj);seen=set()
    def canon(c):
        rots=[]
        for z in (c,tuple(reversed(c))):
            for i in range(8):rots.append(z[i:]+z[:i])
        return min(rots)
    for s in range(n):
        def dfs(path):
            u=path[-1]
            if len(path)==8:
                if s in adj[u]:seen.add(canon(tuple(path)))
                return
            for v in adj[u]:
                if v not in path:dfs(path+[v])
        dfs([s])
    return seen

adj,off=build_W2();D=distances(adj)
assert len(adj)==30 and off==15
assert all(len(a)==3 for a in adj)
assert min(D[u][v] for u in range(30) for v in range(u+1,30) if D[u][v]>0)==1
profiles=Counter();tot=[0]*6
for x in range(30):
    for y in range(30):
        if x==y:continue
        # length 5 is odd, so same-side endpoint chain groups are empty.
        if (x<off)==(y<off):
            assert all(len(chains(D,x,y,k,5))==0 for k in (2,3,4))
            continue
        d=D[x][y]
        assert d in (1,3)
        z=local(D,x,y);profiles[(d,z)]+=1
        for i,a in enumerate(z):tot[i]+=a
assert profiles==Counter({(3,(14,45,40,14,27,4)):360,(1,(8,36,56,8,28,0)):90})
assert tuple(tot)==(5760,19440,19440,5760,12240,1440)
cycles=count_8cycles(adj);assert len(cycles)==90
# Every ordered distance-3 pair is carried by exactly four 8-cycles along its unique geodesic.
inc=Counter()
for c in cycles:
    E={(c[i],c[(i+1)%8]) for i in range(8)}|{(c[(i+1)%8],c[i]) for i in range(8)}
    for x in c:
        for y in c:
            if D[x][y]==3:
                # unique 3-edge geodesic in girth 8; check the cycle contains one such 3-path.
                for direction in (1,-1):
                    i=c.index(x);p=[c[(i+direction*j)%8] for j in range(4)]
                    if p[-1]==y:
                        inc[(x,y)]+=1;break
assert len(inc)==360 and set(inc.values())=={4}
print('vertices=30 edges=45 girth=8')
print('endpoint_profile_d1: blocks=90 C2=8 C3=36 C4=56 rank_d3=8 rank_d4=28 beta=0')
print('endpoint_profile_d3: blocks=360 C2=14 C3=45 C4=40 rank_d3=14 rank_d4=27 beta=4')
print('global_C2=5760 global_C3=19440 global_C4=19440 global_rank_d3=5760 global_rank_d4=12240')
print('MH_3_5_F2_dimension=1440')
print('eight_cycles=90 cycles_per_ordered_distance3_geodesic=4')
print('CHAIN_CONDITION_OK')
print('VERIFY_OK')

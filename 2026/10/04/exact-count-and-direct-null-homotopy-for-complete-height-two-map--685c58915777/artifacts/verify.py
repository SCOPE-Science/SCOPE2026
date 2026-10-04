from itertools import product
from collections import deque


def crown(n):
    # indices 0..n-1 are x_i (minimal), n..2n-1 are y_i (maximal)
    N=2*n
    le=[[False]*N for _ in range(N)]
    for i in range(N): le[i][i]=True
    for i in range(n):
        le[i][n+i]=True
        le[(i+1)%n][n+i]=True
    return le


def ppq(p,q):
    N=p+q
    le=[[False]*N for _ in range(N)]
    for i in range(N): le[i][i]=True
    for a in range(p):
        for b in range(p,p+q): le[a][b]=True
    return le


def maps_ppq_to_crown(p,q,n):
    leY=crown(n)
    N=p+q
    out=[]
    for f in product(range(2*n), repeat=N):
        ok=True
        for a in range(p):
            fa=f[a]
            for b in range(p,p+q):
                if not leY[fa][f[b]]:
                    ok=False;break
            if not ok: break
        if ok: out.append(f)
    return out


def classify_and_witness(f,p,q,n):
    A=f[:p]; B=f[p:]
    # Case I: some source-minimal point maps to a maximal target point.
    maxA=[z for z in A if z>=n]
    if maxA:
        y=maxA[0]
        assert all(z==y for z in B)
        i=y-n
        allowed={i,(i+1)%n,y}
        assert all(z in allowed for z in A)
        # f <= const_y
        return 'I', y, 'up'
    # Case II: A all target-minimal, some source-maximal maps target-minimal.
    minB=[z for z in B if z<n]
    if minB:
        x=minB[0]
        assert all(z==x for z in A)
        allowed={x,n+((x-1)%n),n+x}
        assert all(z in allowed for z in B)
        # const_x <= f
        return 'II', x, 'down'
    # Case III: rank-preserving.
    assert all(z<n for z in A) and all(z>=n for z in B)
    S=set(A)
    if len(S)==1:
        x=next(iter(S))
        assert all(z in {n+((x-1)%n),n+x} for z in B)
        return 'III-single', x, 'down'
    assert len(S)==2
    s=sorted(S)
    # unique y whose two lower neighbors are exactly S
    ys=[]
    for i in range(n):
        if {i,(i+1)%n}==S: ys.append(n+i)
    assert len(ys)==1
    y=ys[0]
    assert all(z==y for z in B)
    return 'III-pair', y, 'up'


def le_map(f,g,leY):
    return all(leY[a][b] for a,b in zip(f,g))

checks=0
for p in range(1,4):
    for q in range(1,4):
        for n in range(3,6):
            maps=maps_ppq_to_crown(p,q,n)
            expected=n*(3**p+3**q-2)
            assert len(maps)==expected,(p,q,n,len(maps),expected)
            leY=crown(n)
            counts={'I':0,'II':0,'III-single':0,'III-pair':0}
            for f in maps:
                case,z,direction=classify_and_witness(f,p,q,n)
                counts[case]+=1
                c=(z,)*(p+q)
                if direction=='up': assert le_map(f,c,leY)
                else: assert le_map(c,f,leY)
            assert counts['I']==n*(3**p-2**p)
            assert counts['II']==n*(3**q-2**q)
            assert counts['III-single']==n*(2**q)
            assert counts['III-pair']==n*(2**p-2)
            checks+=1

# Sharpness at n=2: identity of C_2=P_{2,2} is not in the constant component.
n=2;p=q=2
maps=maps_ppq_to_crown(p,q,n)
leY=crown(n)
adj=[[] for _ in maps]
for i in range(len(maps)):
    for j in range(i+1,len(maps)):
        if le_map(maps[i],maps[j],leY) or le_map(maps[j],maps[i],leY):
            adj[i].append(j);adj[j].append(i)
comp=[-1]*len(maps); sizes=[]
for i in range(len(maps)):
    if comp[i]!=-1: continue
    cid=len(sizes); dq=deque([i]); comp[i]=cid; size=0
    while dq:
        u=dq.popleft(); size+=1
        for v in adj[u]:
            if comp[v]==-1:
                comp[v]=cid; dq.append(v)
    sizes.append(size)
idmap=tuple(range(4)); ii=maps.index(idmap)
constidx=[maps.index((z,)*4) for z in range(4)]
assert len(maps)==36
assert sorted(sizes)==[1,1,1,1,32]
assert comp[ii] not in {comp[j] for j in constidx}
print(f"VERIFY_OK exhaustive_parameter_triples={checks} sharp_n2_maps={len(maps)} sharp_n2_components={sorted(sizes)}")

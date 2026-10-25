"""Exact certificate verifier for a two-stage permutohedral graph Rips filtration.
Run from the directory containing this file; Python 3 and SymPy 1.14 are required.
"""
from pathlib import Path
from itertools import permutations, combinations, product
from collections import Counter, deque
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import json

HERE=Path(__file__).resolve().parent
P=list(permutations(range(4)))
VID={p:i for i,p in enumerate(P)}

def boundary(f):
    return [(f[:i]+f[i+1:],1 if i%2==0 else -1) for i in range(len(f))]

def parity(x):
    return -1 if sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x)))%2 else 1

def graph_distance():
    adj=[set() for _ in P]
    for i,p in enumerate(P):
        for k in range(3):
            q=list(p);q[k],q[k+1]=q[k+1],q[k]
            adj[i].add(VID[tuple(q)])
    assert sum(map(len,adj))==72
    dist=[]
    for src in range(24):
        d={src:0};todo=deque([src])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if v not in d:d[v]=d[u]+1;todo.append(v)
        assert len(d)==24
        dist.append(d)
    return dist

def cliques(dist,r):
    adj=[set(j for j in range(24) if j!=i and dist[i][j]<=r) for i in range(24)]
    out=[]
    def grow(t,can):
        if t:out.append(t)
        for ix,u in enumerate(can):
            grow(t+(u,),[v for v in can[ix+1:] if v in adj[u]])
    grow((),list(range(24)))
    return set(out)

def read_ops(r):
    data=json.loads((HERE/f'morse_scale{r}.json').read_text(encoding='utf-8'))
    return [(x[0],*[tuple(v) for v in x[1:]]) for x in data]

def check_morse(faces,ops,r):
    alive=set(faces);paired={};crit=[]
    cofaces={f:set() for f in faces}
    for f in faces:
        if len(f)>1:
            for smaller,_ in boundary(f):cofaces[smaller].add(f)
    for op in ops:
        if op[0]=='critical':
            (f,)=op[1:]
            assert f in alive and not any(t in alive for t in cofaces[f])
            crit.append(f);alive.remove(f)
        else:
            assert op[0]=='pair' and len(op)==3
            s,t=op[1:]
            assert s in alive and t in alive and len(t)==len(s)+1
            assert s in (u for u,_ in boundary(t))
            assert not any(u in alive and u!=t for u in cofaces[s])
            alive.remove(s);alive.remove(t);paired[s]=t
    assert not alive
    assert Counter(len(f) for f in crit)==({1:1,3:9} if r==2 else {1:1,3:1})
    assert len(paired)==(126 if r==2 else 878)
    # Independent directed Hasse-graph acyclicity check.
    ind={f:0 for f in faces};arcs={f:[] for f in faces}
    for t in faces:
        for s,_ in boundary(t):
            if not s:continue
            a,b=(s,t) if paired.get(s)==t else (t,s)
            arcs[a].append(b);ind[b]+=1
    todo=deque(f for f in faces if ind[f]==0);seen=0
    while todo:
        u=todo.popleft();seen+=1
        for v in arcs[u]:
            ind[v]-=1
            if ind[v]==0:todo.append(v)
    assert seen==len(faces)
    return crit

def cocycle_from_scale3(ops):
    c={}
    for op in reversed(ops):
        if op[0]=='critical':
            f=op[1]
            if len(f)==3:c[f]=1
        else:
            s,t=op[1:]
            if len(s)==3:
                other=sum(sgn*c.get(f,0) for f,sgn in boundary(t) if f!=s)
                eps=next(sgn for f,sgn in boundary(t) if f==s)
                c[s]=-eps*other
            if len(t)==3:c[t]=0
    return c

def hex_cycle(facet,dist):
    remain=set(facet);pairs=[]
    while remain:
        a=min(remain);choices=[b for b in sorted(remain) if b!=a and dist[a][b]==3]
        assert len(choices)==1
        b=choices[0];pairs.append((a,b));remain.remove(a);remain.remove(b)
    assert len(pairs)==3
    z={}
    for opt in product((0,1),repeat=3):
        vals=[pairs[j][opt[j]] for j in range(3)]
        z[tuple(sorted(vals))]=(-1)**sum(opt)*parity(vals)
    return z

def act(a,reverse):
    return [VID[tuple(a[p[3-j if reverse else j]] for j in range(4))] for p in P]

def apply_chain(z,mapping):
    out=Counter()
    for f,coeff in z.items():
        image=[mapping[i] for i in f]
        out[tuple(sorted(image))]+=coeff*parity(image)
    return {f:c for f,c in out.items() if c}

def signed_lefschetz(faces,mapping):
    s=0
    for f in faces:
        v=[mapping[i] for i in f]
        if set(v)==set(f):s+=(-1)**(len(f)-1)*parity(v)
    return s

def cycle_type(p):
    seen=set();lengths=[]
    for i in range(4):
        if i in seen:continue
        j=i;n=0
        while j not in seen:seen.add(j);j=p[j];n+=1
        lengths.append(n)
    return tuple(sorted(lengths,reverse=True))

def main():
    dist=graph_distance()
    k2=cliques(dist,2);k3=cliques(dist,3)
    assert [sum(len(f)==j for f in k2) for j in range(1,5)]==[24,96,112,30]
    assert [sum(len(f)==j for f in k3) for j in range(1,7)]==[24,168,472,618,384,92]
    ops2=read_ops(2);ops3=read_ops(3)
    check_morse(k2,ops2,2);check_morse(k3,ops3,3)
    c=cocycle_from_scale3(ops3)
    assert all(sum(s*c.get(sub,0) for sub,s in boundary(f))==0 for f in k3 if len(f)==4)
    assert len([f for f in c if c[f]])==34
    hexes=[]
    for pos in (0,3):
        for label in range(4):
            facet=tuple(i for i,p in enumerate(P) if p[pos]==label)
            z=hex_cycle(facet,dist)
            if pos==3:z={f:-v for f,v in z.items()}
            assert len(z)==8 and set(z).issubset(k2)
            assert all(sum(coeff*sgn for f,coeff in z.items() for sub,sgn in boundary(f) if sub==e)==0
                       for e in k2 if len(e)==2)
            assert all(dist[u][v]<=3 for u,v in combinations(facet,2))
            hexes.append(z)
    data=json.loads((HERE/'primitive_cycle.json').read_text(encoding='utf-8'))
    z={tuple(f):int(x) for f,x in data['cycle']}
    assert len(z)==20 and all(f in k2 for f in z)
    edgecoeff=Counter()
    for f,v in z.items():
        for e,s in boundary(f):edgecoeff[e]+=v*s
    assert not any(edgecoeff.values())
    pair=sum(z.get(f,0)*c.get(f,0) for f in z)
    assert pair in (-1,1)
    tri=sorted(f for f in k2 if len(f)==3)
    tet=sorted(f for f in k2 if len(f)==4)
    edges=sorted(f for f in k2 if len(f)==2)
    tid={f:i for i,f in enumerate(tri)};eid={e:i for i,e in enumerate(edges)}
    b2=zeros(len(edges),len(tri))
    for j,f in enumerate(tri):
        for e,s in boundary(f):b2[eid[e],j]=s
    assert b2.rank()==73
    cols=[{e:s for e,s in boundary(f)} for f in tet]
    A=zeros(len(tri),len(tet)+len(hexes)+1)
    for j,f in enumerate(tet):
        for e,s in boundary(f):A[tid[e],j]=s
    for j,chain in enumerate(hexes+[z]):
        for f,v in chain.items():A[tid[f],len(tet)+j]=v
    assert b2*A==zeros(len(edges),len(tet)+9)
    D=smith_normal_form(A,domain=ZZ)
    invariants=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    assert len(invariants)==39 and all(d==1 for d in invariants)
    assert sum(c.get(f,0)*chain.get(f,0) for chain in hexes for f in chain)==0
    chars={}
    for a in P:
        for rev in (0,1):
            g=act(a,rev)
            # These are simplicial actions at both scales.
            assert all(tuple(sorted(g[i] for i in f)) in k3 for f in k3)
            # The eight hexagon-sphere classes transform by the literal facet permutation.
            for i,h in enumerate(hexes):
                j=(4 if (i<4 and rev) or (i>=4 and not rev) else 0)+a[i%4]
                assert apply_chain(h,g)==hexes[j]
            t2=signed_lefschetz(k2,g)-1
            t3=signed_lefschetz(k3,g)-1
            expected3=parity(a)*(-1)**rev
            assert t3==expected3
            assert sum(c.get(f,0)*v for f,v in apply_chain(z,g).items())==expected3*pair
            key=(cycle_type(a),rev)
            if key in chars:assert chars[key]==(t2,t3)
            chars[key]=(t2,t3)
    expected={
      ((1,1,1,1),0):(9,1),((1,1,1,1),1):(-1,-1),
      ((2,1,1),0):(3,-1),((2,1,1),1):(1,1),
      ((2,2),0):(1,1),((2,2),1):(-1,-1),
      ((3,1),0):(3,1),((3,1),1):(-1,-1),
      ((4,),0):(-1,-1),((4,),1):(1,1)}
    assert chars==expected
    print('F_VECTORS_2_3', [24,96,112,30], [24,168,472,618,384,92])
    print('MORSE_PAIRS_2_3',126,878,'CRITICAL_2',(1,9),'CRITICAL_3',(1,1))
    print('HEXAGON_PRIMITIVE_BASIS',len(hexes),'BASIS_CYCLE',len(z),'SMITH',len(invariants),'UNIT_FACTORS')
    print('INTEGER_PERSISTENCE_PAIRING',pair)
    print('S4_C2_CHARACTER_CLASSES',len(chars),'ALL_GROUP_ELEMENTS',48)
    print('INTEGRAL_EXACT_SEQUENCE_Z8_TO_Z9_TO_Z_AND_RATIONAL_MODULES')
    print('VERIFY_OK_PERMUTOHEDRON_EQUIVARIANT_PERSISTENCE')

if __name__=='__main__':main()

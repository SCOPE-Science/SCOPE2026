#!/usr/bin/env python3
"""Self-contained, exact verification of a Frucht-graph higher-independence theorem.

Only Python standard library. The face sets and all discrete-Morse
matchings are rebuilt from the graph and deterministic vertex orders.
"""
from collections import Counter, deque

N = 12
EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),
         (3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),
         (7,11),(8,11),(8,9),(10,11))
LCF = (-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)
# The explicit isomorphism maps the displayed graph labels to the
# standard Hamiltonian LCF labels (an alternate canonical presentation).
LCF_ISOMORPHISM = (5,3,2,1,0,7,6,4,10,11,8,9)
DELETION_ORDERS = {
 0:(4,3,2,5,6,10,7,1,9,11,8),
 4:(3,11,9,1,5,0,8,10,7,2,6),
 10:(5,6,2,4,3,7,1,9,8,11,0),
 11:(8,6,3,4,5,7,1,10,0,9,2),
}
EXPECTED = {None:1,0:2,1:2,2:2,3:1,4:2,5:2,6:1,
            7:3,8:1,9:2,10:2,11:4}
ZERO_IMAGE = {0,6,8,9}


def verify_graph_labeling():
    std = {frozenset((i,(i+1)%N)) for i in range(N)}
    std.update(frozenset((i,(i+j)%N)) for i,j in enumerate(LCF))
    actual = {frozenset((LCF_ISOMORPHISM[i],LCF_ISOMORPHISM[j])) for i,j in EDGES}
    assert len(set(LCF_ISOMORPHISM)) == N
    assert std == actual and len(std) == len(EDGES) == 18


def build_faces():
    adj = [0]*N
    for a,b in EDGES:
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    # A graph induced on S has components of order at most two iff
    # each vertex has at most one neighbor in S.
    return [s for s in range(1,1<<N) if all(
        not (s>>v)&1 or (adj[v]&s).bit_count()<=1 for v in range(N))]


def vertex_match(faces, order):
    unpaired=set(faces)
    pairs=[]
    for v in order:
        bit=1<<v
        for f in faces:
            t=f|bit
            if not (f&bit) and f in unpaired and t in unpaired:
                unpaired.remove(f)
                unpaired.remove(t)
                pairs.append((f,t))
    assert len(unpaired)+2*len(pairs)==len(faces)
    return unpaired, pairs


def verify_acyclic(faces,pairs):
    # The acyclic Morse matching reverses precisely its cover arrows
    # in the Hasse diagram. A topological sort tests the full diagram.
    sfaces=set(faces)
    paired={p for p in pairs}
    assert len(paired)==len(pairs)
    indeg={f:0 for f in faces}; outgoing={f:[] for f in faces}
    n_cover=0
    for t in faces:
        for v in range(N):
            if not (t>>v)&1: continue
            s=t^(1<<v)
            if not s or s not in sfaces: continue
            if (s,t) in paired:
                outgoing[s].append(t);indeg[t]+=1
            else:
                outgoing[t].append(s);indeg[s]+=1
            n_cover+=1
    todo=deque(f for f in faces if indeg[f]==0)
    count=0
    while todo:
        x=todo.popleft();count+=1
        for y in outgoing[x]:
            indeg[y]-=1
            if indeg[y]==0:todo.append(y)
    assert count==len(faces), 'A directed alternating cycle exists'
    return n_cover


def signed_boundary(t):
    vertices=[i for i in range(N) if (t>>i)&1]
    return {t^(1<<v):(-1)**i for i,v in enumerate(vertices)}


def morse_boundary(critical,pairs,k):
    # All k-1 lower faces paired with k-faces are eliminated by
    # exact integral unit pivots. This computes the Morse incidence
    # from each critical k-cell to the critical (k-1)-cells.
    upper={s:t for s,t in pairs if s.bit_count()==k}
    roots=sorted(f for f in critical if f.bit_count()==k+1)
    targets=sorted(f for f in critical if f.bit_count()==k)
    result=[]
    for root in roots:
        chain=signed_boundary(root)
        steps=0
        while True:
            eligible=next((x for x in chain if x in upper),None)
            if eligible is None:break
            t=upper[eligible]
            b=signed_boundary(t)
            factor=chain[eligible]*b[eligible] # b[eligible]=+/-1
            for f,c in b.items():
                coefficient=chain.get(f,0)-factor*c
                if coefficient:chain[f]=coefficient
                else:chain.pop(f,None)
            steps+=1
            assert steps<=len(pairs), 'A gradient-path cycle exists'
        result.append([chain.get(x,0) for x in targets])
    return result,targets


def mod2_betti(faces):
    # This calculation does not use the matching or the Morse model.
    degrees=Counter(s.bit_count()-1 for s in faces)
    sets={k:sorted(s for s in faces if s.bit_count()-1==k) for k in degrees}
    ranks={}
    for k in degrees:
        if k==0:ranks[k]=0;continue
        rows={s:i for i,s in enumerate(sets[k-1])}
        pivots={}
        for s in sets[k]:
            col=0
            for v in range(N):
                if (s>>v)&1:
                    col ^= 1 << rows[s^(1<<v)]
            while col:
                p=col.bit_length()-1
                if p in pivots:col ^=pivots[p]
                else:pivots[p]=col;break
        ranks[k]=len(pivots)
    # Unreduced H_0: rank(d0)=0. Subtract 1 in degree zero.
    return {k:degrees[k]-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0)
            for k in degrees}



def lift_degree_three_cycle(root,pairs):
    """Exact integral cycle lifting using the pairs in dimensions (2,3)."""
    up = {s:t for s,t in pairs if s.bit_count()==3}
    chain={root:1}
    d=signed_boundary(root)
    steps=0
    while True:
        s=next((s for s in d if s in up),None)
        if s is None:break
        t=up[s]
        dt=signed_boundary(t)
        factor=d[s]*dt[s]
        a=chain.get(t,0)-factor
        if a:chain[t]=a
        else:chain.pop(t,None)
        for f,c in dt.items():
            a=d.get(f,0)-factor*c
            if a:d[f]=a
            else:d.pop(f,None)
        steps+=1
        assert steps<=len(pairs)
    assert not d,'Lifting failed to produce an integral cycle'
    return chain


def project_on_full_three_cells(chain,fullpairs,fullcrit3):
    """Reduce modulo matched (3,4) boundaries, retaining critical cells."""
    up={s:t for s,t in fullpairs if s.bit_count()==4}
    c=dict(chain)
    steps=0
    while True:
        s=next((s for s in c if s in up),None)
        if s is None:break
        dt=signed_boundary(up[s])
        factor=c[s]*dt[s]
        for f,a in dt.items():
            x=c.get(f,0)-factor*a
            if x:c[f]=x
            else:c.pop(f,None)
        steps+=1
        assert steps<=len(fullpairs)
    return [c.get(x,0) for x in fullcrit3]


def direct_relative_mod2_map(fullfaces):
    """Independent chain-matrix test of all inclusion images over F_2.

    For each deletion, calculate kernel(d3) inside the deleted complex,
    then test its image modulo the full boundary space im(d4).
    """
    C3=sorted(s for s in fullfaces if s.bit_count()==4)
    C4=sorted(s for s in fullfaces if s.bit_count()==5)
    C2=sorted(s for s in fullfaces if s.bit_count()==3)
    i3={s:i for i,s in enumerate(C3)}
    i2={s:i for i,s in enumerate(C2)}
    def b(s,index):
        z=0
        for v in range(N):
            if (s>>v)&1:z ^=1<<index[s^(1<<v)]
        return z
    def insert(vec,piv):
        while vec:
            j=vec.bit_length()-1
            if j in piv:vec^=piv[j]
            else:piv[j]=vec;return 1
        return 0
    B={}
    for t in C4:insert(b(t,i3),B)
    assert len(B)==157
    result={}
    for vertex in range(N):
        kernel_basis={}; cycles=[]
        for t in C3:
            if (t>>vertex)&1:continue
            z=b(t,i2);c=1<<i3[t]
            while z:
                j=z.bit_length()-1
                if j in kernel_basis:
                    oldz,oldc=kernel_basis[j];z^=oldz;c^=oldc
                else:kernel_basis[j]=(z,c);break
            if not z:cycles.append(c)
        work=dict(B);result[vertex]=sum(insert(c,work) for c in cycles)
        assert result[vertex] in (0,1)
    return result

def main():
    verify_graph_labeling()
    fullfaces=build_faces()
    print('edges:',len(EDGES),'Frucht graph verified against its LCF representation')
    print('full face count:',len(fullfaces),'f-vector:',dict(sorted(Counter(s.bit_count()-1 for s in fullfaces).items())))
    fullcrit,fullpairs=vertex_match(fullfaces,tuple(range(N)))
    fullcrit3=sorted(f for f in fullcrit if f.bit_count()==4)
    assert fullcrit3==[834,1100]
    mod2_map=direct_relative_mod2_map(fullfaces)
    for deleted in (None,)+tuple(range(N)):
        faces=fullfaces if deleted is None else [f for f in fullfaces if not (f>>deleted)&1]
        order=tuple(range(N)) if deleted is None else DELETION_ORDERS.get(
            deleted,tuple(v for v in range(N) if v!=deleted))
        assert len(order)==len(set(order))==N-(deleted is not None)
        assert set(order)==set(range(N))-({deleted} if deleted is not None else set())
        critical,pairs=vertex_match(faces,order)
        incidences=verify_acyclic(faces,pairs)
        vector=Counter(f.bit_count()-1 for f in critical)
        assert vector[0]==1 and not any(vector[k] for k in vector if k not in (0,3,4))
        assert vector[4]<=1
        inc,lower=morse_boundary(critical,pairs,4)
        if vector[4]:
            assert len(inc)==1 and len(lower)==vector[3]
            assert sum(abs(x) for x in inc[0])==1, (deleted,inc)
        else:assert not inc
        assert vector[3]-vector[4]==EXPECTED[deleted]
        if deleted is not None:
            # The full Morse differential is [0,1], so its first
            # critical three-cell generates the integral H_3.
            image_coefficients=[project_on_full_three_cells(
                lift_degree_three_cycle(f,pairs),fullpairs,fullcrit3)[0]
                for f in sorted(f for f in critical if f.bit_count()==4)]
            is_zero=all(a==0 for a in image_coefficients)
            is_surj=any(abs(a)==1 for a in image_coefficients)
            assert is_zero==(deleted in ZERO_IMAGE)
            assert is_surj==(deleted not in ZERO_IMAGE)
            assert mod2_map[deleted]==int(is_surj)
        b=mod2_betti(faces)
        assert b.get(3,0)==EXPECTED[deleted] and all(
            x==0 for k,x in b.items() if k!=3),(deleted,b)
        label='full' if deleted is None else f'delete {deleted}'
        map_text='' if deleted is None else (
            ', inclusion_image='+('zero' if deleted in ZERO_IMAGE else 'surjective'))
        print(f'{label:>10} : faces={len(faces):3d}, cover={incidences:4d}, '
              f'pairs={len(pairs):3d}, critical={dict(sorted(vector.items()))}, '
              f'd4={inc}, homotopy=vee^{EXPECTED[deleted]} S^3'+map_text)
    print('PASS: acyclic matchings, integral incidence and inclusion maps, and independent F2 chain matrices for all 13 complexes')

if __name__=='__main__':main()

"""Exact finite verification of the ordered-tier orbit-space model.

No external packages; all simplicial homology computed over F_2 by bitset elimination.
"""
from itertools import product, combinations, permutations
from math import comb
from collections import defaultdict


def graph_components(face, blocks):
    if not face: return []
    B={v:i for i,block in enumerate(blocks) for v in block}
    adj={v:{w for w in face if w!=v and B[v]!=B[w]} for v in face}
    unseen=set(face); components=[]
    while unseen:
        q=[min(unseen)];unseen.remove(q[0]);co=[]
        while q:
            v=q.pop();co.append(v)
            for u in sorted(adj[v] & unseen):
                unseen.remove(u);q.append(u)
        components.append(co)
    return components


def legal_from_graph(face,blocks,r):
    return all(len(c)<=r for c in graph_components(face,blocks))


def legal_support(counts,r):
    return sum(x>0 for x in counts)<=1 or sum(counts)<=r


def tier_faces(sizes,r):
    vertices=[(i,j) for i,mi in enumerate(sizes) for j in range(1,mi+1)]
    faces=set()
    for mask in range(1<<len(vertices)):
        fs=frozenset(vertices[z] for z in range(len(vertices)) if mask>>z&1)
        active={i for i,j in fs}
        if len(active)<=1 or sum(max(j for ii,j in fs if ii==i) for i in active)<=r:
            faces.add(fs)
    return vertices,faces


def gf2_rank(rows):
    piv={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:
                piv[p]=x;break
    return len(piv)


def reduced_betti(faces):
    chain=defaultdict(list)
    for f in faces:
        chain[len(f)-1].append(tuple(sorted(f)))
    for d in chain:chain[d].sort()
    dims=sorted(d for d in chain if d>=0)
    ranks={0:1 if chain.get(0) else 0}
    for d in dims:
        if d<1:continue
        basis={f:i for i,f in enumerate(chain[d-1])}
        columns=[]
        for f in chain[d]:
            v=0
            for j in range(len(f)):
                v ^=1<<basis[f[:j]+f[j+1:]]
            columns.append(v)
        ranks[d]=gf2_rank(columns)
    return {d:len(chain[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in dims}


def binom(n,k):return comb(n,k) if 0<=k<=n else 0


def component_faces(sizes,r):
    N=sum(sizes)
    blocks=[];z=0
    for mi in sizes: blocks.append(tuple(range(z,z+mi)));z+=mi
    F=0
    for mask in range(1<<N):
        face=[k for k in range(N) if (mask>>k)&1]
        counts=[sum(v in face for v in block) for block in blocks]
        assert legal_from_graph(face,blocks,r)==legal_support(counts,r),(sizes,r,face)
        if legal_from_graph(face,blocks,r):F+=1
    return F


def perm_char_average(sizes,r):
    # Fixed-oriented trace on H_{r-1} of original complex, average should equal beta of quotient.
    # Chain-trace Euler formula: rank of alt-reduced homology in degree r-1.
    blocks=[];z=0
    for m in sizes:blocks.append(tuple(range(z,z+m)));z+=m
    groups=[list(permutations(b)) for b in blocks]
    total=0;ns=0
    for ps in product(*groups):
        p=list(range(z))
        for block,perm in zip(blocks,ps):
            for v,pv in zip(block,perm):p[v]=pv
        # orientation-signed permutation of each invariant nonempty allowed simplex.
        # reduced Euler characteristic trace = -1 + sum_k (-1)^k tr C_k.
        alternating=-1
        for mask in range(1,1<<z):
            ids=[v for v in range(z) if mask>>v&1]
            counts=[sum(v in ids for v in block) for block in blocks]
            if not legal_support(counts,r):continue
            if set(p[v] for v in ids)!=set(ids):continue
            pos={v:i for i,v in enumerate(ids)}
            seq=[pos[p[v]] for v in ids]
            parity=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2
            alternating+=(-1)**(len(ids)-1+parity)
        total+=(-1)**(r-1)*alternating
        ns+=1
    assert total==ns*binom(len(sizes)-1,r),(sizes,r,total,ns)
    return ns


def main():
    tests=0;original_faces=0;tier_face_total=0; domination=0; group_count=0
    for s in (2,3,4):
        choices=(1,2,3) if s<=3 else (1,2)
        for sizes in product(choices,repeat=s):
            N=sum(sizes)
            for r in range(1,min(N,4)+1):
                original_faces+=component_faces(sizes,r)
                vertices,faces=tier_faces(sizes,r)
                tier_face_total+=len(faces)-1
                # For each extra tier, strong domination by first tier (with free face vertex).
                current=set(faces)
                for i in range(s):
                    for j in range(sizes[i],1,-1):
                        v=(i,j);u=(i,1)
                        for f in current:
                            if v in f and u not in f:
                                assert f|{u} in current, (sizes,r,v,u,f)
                                domination+=1
                        current={f for f in current if v not in f}
                expected={frozenset((i,1) for i in inds) for k in range(min(r,s)+1)
                          for inds in combinations(range(s),k)}
                assert current==expected,(sizes,r,current^expected)
                b=reduced_betti(faces)
                assert all(b.get(d,0)==(binom(s-1,r) if (r<s and d==r-1) else 0)
                           for d in range(max(sizes)+s+1)),(sizes,r,b)
                group_count+=perm_char_average(sizes,r)
                tests+=1
    print(f'VERIFY_OK parameter_cases={tests} original_accepted_faces_including_empty={original_faces} tier_nonempty_faces={tier_face_total} dominated_coface_checks={domination} group_elements_checked={group_count}')

if __name__=='__main__':main()

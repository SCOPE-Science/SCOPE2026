"""Exact finite verification of the neighborhood complex of K_5 Cartesian C_4.
Python 3 stdlib only. All simplices enumerated independently in two ways;
all matched pairs and all covering incidences are inspected; integral
Morse boundary is computed by acyclic gradient substitution.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

M=5;N=4*M;FULL=(1<<N)-1

def facets():
    out=[]
    for i in range(4):
        for a in range(M):
            z=0
            for b in range(M):
                if b!=a: z|=1<<(i*M+b)
            z|=1<<(((i-1)%4)*M+a)
            z|=1<<(((i+1)%4)*M+a)
            out.append(z)
    return out

def subfaces_from_facets():
    faces=set()
    for facet in facets():
        z=facet
        while z:
            faces.add(z)
            z=(z-1)&facet
    return faces

def neigh_masks():
    arr=[]
    for x in range(N):
        i,a=divmod(x,M)
        z=0
        for b in range(M):
            if b!=a:z|=1<<(i*M+b)
        for j in ((i-1)%4,(i+1)%4): z|=1<<(j*M+a)
        arr.append(z)
    return arr

def subfaces_from_adjacency():
    nbr=neigh_masks();out=set()
    # Iterate over all 2^20 subsets using Gray code, updating intersection
    # from scratch for every subset with up to 6 vertices.
    for s in range(1,1<<N):
        if s.bit_count()>M+1:continue
        common=FULL
        z=s
        while z:
            t=z&-z;z-=t
            common&=nbr[t.bit_length()-1]
            if not common:break
        if common:out.add(s)
    return out

def boundary(s):
    out=[];sgn=1;z=s
    while z:
        bit=z&-z;z-=bit
        out.append((s^bit,sgn))
        sgn=-sgn
    return out

def sequential_matching(faces):
    rem=set(faces);pairs=[]
    for v in range(N):
        bit=1<<v
        for s in sorted(tuple(rem)):
            if not s&bit and (s|bit) in rem:
                rem.remove(s);rem.remove(s|bit)
                pairs.append((s,s|bit))
    return pairs,rem

def acyclic_hasse(faces,pairs):
    paired=set(pairs)
    nodes=sorted(faces);degree={f:0 for f in nodes}
    down=defaultdict(list);num=0
    for hi in nodes:
        for low,_ in boundary(hi):
            if not low:continue
            num+=1
            if (low,hi) in paired:
                u,v=low,hi
            else:u,v=hi,low
            degree[v]+=1;down[u].append(v)
    q=deque(x for x in nodes if not degree[x]);visited=0
    while q:
        u=q.popleft();visited+=1
        for v in down[u]:
            degree[v]-=1
            if degree[v]==0:q.append(v)
    assert visited==len(nodes),(visited,len(nodes))
    return num

def morse_boundary(faces,pairs,critical):
    # Analyze exactly the C_3 -> C_2 boundary. In the acyclic Morse
    # contraction, any 2-cell matched upward to a 3-cell can be
    # substituted by the other faces of that 3-cell. Any 2-cell
    # matched downward to a 1-cell disappears in the reduced complex.
    ups={low:hi for low,hi in pairs}
    downs={hi:low for low,hi in pairs}
    crit2={s for s in critical if s.bit_count()==3}
    crit3=sorted(s for s in critical if s.bit_count()==4)
    @lru_cache(None)
    def project(tri):
        assert tri.bit_count()==3
        if tri in crit2:return {tri:1}
        if tri in downs:return {}
        assert tri in ups,(tri,'unmatched noncritical triangle')
        tet=ups[tri];terms=dict(boundary(tet)); c=terms.pop(tri)
        ans=defaultdict(int)
        for u,a in terms.items():
            p=project(u)
            for t,co in p.items():ans[t]-=(a//c)*co if c in (1,-1) else 0
        return {t:v for t,v in ans.items() if v}
    maximal=0
    for tet in crit3:
        out=defaultdict(int)
        for tri,sign in boundary(tet):
            for t,k in project(tri).items():out[t]+=sign*k
        out={t:v for t,v in out.items() if v}
        maximal=max(maximal,len(out))
        assert not out,('nonzero integral Morse boundary',tet,out)
    return len(crit3),len(crit2),maximal,project.cache_info().currsize

def main():
    A=subfaces_from_facets()
    B=subfaces_from_adjacency()
    assert A==B,(len(A),len(B),len(A^B))
    fvec=tuple(sum(s.bit_count()==k+1 for s in A) for k in range(6))
    assert fvec==(20,130,360,300,120,20),fvec
    pairs,critical=sequential_matching(A)
    assert len(pairs)==446,len(pairs)
    dims=Counter(s.bit_count()-1 for s in critical)
    assert dims=={0:1,2:53,3:4},dims
    incidences=acyclic_hasse(A,pairs)
    _,_,maximal,substitutions=morse_boundary(A,pairs,critical)
    print('GRAPH 5-clique Cartesian 4-cycle; open neighborhood complex')
    print('SUBSETS_EXHAUSTIVE',1<<20)
    print('FACETS',len(facets()))
    print('FACES_NONEMPTY',len(A))
    print('FACE_VECTOR',*fvec)
    print('MATCHED_PAIRS',len(pairs))
    print('DIRECTED_HASSE_INCIDENCES',incidences)
    print('CRITICAL_CELLS',dict(sorted(dims.items())))
    print('INTEGRAL_MORSE_BOUNDARY_3_TO_2',maximal,'nonzero entries')
    print('MORSE_TRIANGLE_PROJECTIONS',substitutions)
    cancels, remaining=algebraic_cancel(A,pairs,critical)
    print('DIRECT_INTEGRAL_CHAIN_CANCELLATION',cancels,'pairs;',remaining,'critical cells; all differentials zero')
    print('HOMOTOPY_WEDGE_S2',dims[2],'S3',dims[3])
    print('ALL_CHECKS_PASS')
# Independent algebraic chain cancellation, a cross-check of the gradient
# recurrence. It works directly on integral oriented boundary matrices.
def algebraic_cancel(faces,pairs,critical):
    bd={s:{t:c for t,c in boundary(s) if t} for s in faces}
    remaining=set(faces)
    for lo,hi in pairs:
        assert lo in remaining and hi in remaining
        p=bd[hi].get(lo,0)
        assert abs(p)==1,(lo,hi,p)
        for c in tuple(remaining):
            if c==hi or c.bit_count()!=hi.bit_count():continue
            a=bd[c].get(lo,0)
            if a:
                q=a//p
                for z,h in bd[hi].items():
                    bd[c][z]=bd[c].get(z,0)-q*h
                    if not bd[c][z]:del bd[c][z]
        remaining.remove(lo);remaining.remove(hi)
        for c in tuple(remaining):
            bd[c].pop(lo,None)
            bd[c].pop(hi,None)
        del bd[lo];del bd[hi]
    assert remaining==critical
    nz=[(s,terms) for s,terms in bd.items() if terms]
    assert not nz,('unexpected integral Morse differential',nz[:3])
    return len(pairs),len(remaining)

if __name__=='__main__':main()

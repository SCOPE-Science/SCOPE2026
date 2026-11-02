#!/usr/bin/env python3
"""Exact finite-group verification of a genus-six Petersen boundary theorem.
Run with Python 3.9+; only the standard library is used.
"""
from itertools import combinations, permutations
from collections import Counter, deque

VERTICES = tuple(combinations(range(5), 2))
EDGES = tuple((i,j) for i in range(10) for j in range(i+1,10)
              if set(VERTICES[i]).isdisjoint(VERTICES[j]))
BRANCHES = tuple((e,v) for e,(u,w) in enumerate(EDGES) for v in (u,w))
assert len(VERTICES)==10 and len(EDGES)==15 and len(BRANCHES)==30
VINDEX = {v:i for i,v in enumerate(VERTICES)}
EINDEX = {e:i for i,e in enumerate(EDGES)}


def cycle_type(p):
    visited=set(); ans=[]
    for i in range(5):
        if i not in visited:
            j=i; z=0
            while j not in visited:
                visited.add(j);z+=1;j=p[j]
            ans.append(z)
    return tuple(sorted(ans, reverse=True))


def orbits(mapping):
    unseen=set(range(len(mapping))); counts=Counter()
    while unseen:
        start=min(unseen);j=start;m=0
        while j in unseen:
            unseen.remove(j);m+=1;j=mapping[j]
        assert j==start
        counts[m]+=1
    return dict(sorted(counts.items()))


def poly_mul(a,b):
    result=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): result[i+j]+=u*v
    return result


def poly_div_monic(a,b):
    a=list(a);res=[0]*(len(a)-len(b)+1)
    assert b[-1]==1 and len(a)>=len(b)
    for i in range(len(res)-1,-1,-1):
        v=a[i+len(b)-1];res[i]=v
        for j,c in enumerate(b):a[i+j]-=v*c
    assert all(v==0 for v in a),a
    return res


def orbit_poly(cycles, signs=None):
    ans=[1]
    for length,sgn in cycles:
        a=[0]*(length+1);a[0]=-sgn;a[-1]=1
        ans=poly_mul(ans,a)
    return ans


def oriented_edge_orbit_poly(mapping,edge_signs):
    remaining=set(range(15)); signed_orbits=[]
    while remaining:
        start=min(remaining);j=start;length=0;sgn=1
        while j in remaining:
            remaining.remove(j)
            length+=1;sgn*=edge_signs[j];j=mapping[j]
        assert j==start
        signed_orbits.append((length,sgn))
    return orbit_poly(signed_orbits)


def matmul(a,b):
    n=len(a);return [[sum(a[i][k]*b[k][j] for k in range(n))
                  for j in range(n)] for i in range(n)]


def charpoly_matrix(a):
    n=len(a)
    powers=[];b=[[int(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        b=matmul(b,a);powers.append(sum(b[i][i] for i in range(n)))
    coeff=[1]
    for k in range(1,n+1):
        y=sum(coeff[k-i]*powers[i-1] for i in range(1,k+1))
        assert y%k==0
        coeff.append(-y//k)
    return list(reversed(coeff))


def spanning_tree():
    adj={i:[] for i in range(10)}
    for e,(a,b) in enumerate(EDGES):
        adj[a].append((b,e));adj[b].append((a,e))
    parent={0:None};tree=[];Q=deque([0])
    while Q:
        u=Q.popleft()
        for v,e in adj[u]:
            if v not in parent:
                parent[v]=(u,e);tree.append(e);Q.append(v)
    assert len(parent)==10 and len(tree)==9
    chords=[i for i in range(15) if i not in tree]
    assert len(chords)==6
    cycles=[]
    tree_adj={i:[] for i in range(10)}
    for e in tree:
        a,b=EDGES[e]
        tree_adj[a].append((b,e));tree_adj[b].append((a,e))
    for e in chords:
        a,b=EDGES[e];vec=[0]*15;vec[e]=1
        queue=deque([b]); paths={b:[]}
        while queue and a not in paths:
            u=queue.popleft()
            for v,f in tree_adj[u]:
                if v not in paths:
                    paths[v]=paths[u]+[(u,v,f)];queue.append(v)
        assert a in paths
        for u,v,f in paths[a]:
            vec[f]=1 if EDGES[f]==(u,v) else -1
        cycles.append(vec)
    return chords,cycles

CHORDS,CYCLES=spanning_tree()

def analyze(p):
    vmap=[VINDEX[tuple(sorted((p[a],p[b])))] for a,b in VERTICES]
    emap=[];signs=[]
    for u,v in EDGES:
        a,b=vmap[u],vmap[v]
        emap.append(EINDEX[tuple(sorted((a,b)))])
        signs.append(1 if a<b else -1)
    bidx={b:i for i,b in enumerate(BRANCHES)}
    bmap=[bidx[(emap[e],vmap[v])] for e,v in BRANCHES]
    vo=orbits(vmap);eo=orbits(emap);bo=orbits(bmap)
    # Determinant identity from the integral graph chain complex.
    char_v=orbit_poly([(d,1) for d,c in vo.items() for _ in range(c)])
    char_e=oriented_edge_orbit_poly(emap,signs)
    chi=poly_div_monic(poly_mul(char_e,[-1,1]),char_v)
    # A separate integer calculation: act on a fundamental cycle basis.
    M=[[0]*6 for i in range(6)]
    for j,vec in enumerate(CYCLES):
        out=[0]*15
        for i,k in enumerate(emap):out[k]+=signs[i]*vec[i]
        for i,k in enumerate(CHORDS):M[i][j]=out[k]
        # All coefficients, including tree edges, must reconstruct exactly.
        reconstruction=[sum(M[i][j]*CYCLES[i][k] for i in range(6)) for k in range(15)]
        assert out==reconstruction
    assert chi==charpoly_matrix(M)
    assert len(chi)==7 and chi[-1]==1
    # Compare the trace against the exterior square of the standard S5 module.
    fixed_one = sum(p[i] == i for i in range(5))
    fixed_two = sum(p[p[i]] == i for i in range(5))
    trace_standard = fixed_one - 1
    trace_standard_squared = fixed_two - 1
    assert -chi[-2] == (trace_standard**2 - trace_standard_squared)//2
    # Check the point-count identity over the first 12 extension degrees.
    for n in range(1,13):
        c=sum(d*k for d,k in vo.items() if n%d==0)
        e=sum(d*k for d,k in eo.items() if n%d==0)
        b=sum(d*k for d,k in bo.items() if n%d==0)
        for q in (2,3,5):
            pt=(q**n+1)*c-b+e
            # Independent fixed-point calculation from powers of the permutations.
            def fixed(f):
                total=0
                for i in range(len(f)):
                    j=i
                    for _ in range(n):j=f[j]
                    if j==i:total+=1
                return total
            assert pt==(q**n+1)*fixed(vmap)-fixed(bmap)+fixed(emap)
            assert pt>=0
    return (cycle_type(p),tuple(chi),tuple(sorted(vo.items())),
            tuple(sorted(eo.items())),tuple(sorted(bo.items())))



def integral_matrix_determinant(a):
    """Fraction-free Bareiss determinant, so unimodularity is checked exactly."""
    a=[list(row) for row in a]
    n=len(a);previous=1;sgn=1
    for k in range(n-1):
        j=next((j for j in range(k,n) if a[j][k]),None)
        if j is None:return 0
        if j!=k:a[k],a[j]=a[j],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for z in range(k+1,n):
                x=a[i][z]*pivot-a[i][k]*a[k][z]
                assert x%previous==0
                a[i][z]=x//previous
            a[i][k]=0
        previous=pivot
    return sgn*a[-1][-1]


def certificate_of_integral_blocks(p):
    """Construct explicit unimodular Z-Frobenius-module block bases."""
    typ=cycle_type(p)
    vm=[VINDEX[tuple(sorted((p[a],p[b])))] for a,b in VERTICES]
    em=[];s=[]
    for a,b in EDGES:
        x,y=vm[a],vm[b]
        em.append(EINDEX[tuple(sorted((x,y)))])
        s.append(1 if x<y else -1)
    M=[[0]*6 for _ in range(6)]
    for j,vec in enumerate(CYCLES):
        out=[0]*15
        for k,z in enumerate(em):out[z]+=s[k]*vec[k]
        for k,z in enumerate(CHORDS):M[k][j]=out[z]
    def act(v):return [sum(M[i][j]*v[j] for j in range(6)) for i in range(6)]
    def unit(i):return [int(j==i) for j in range(6)]
    def orbit(i,n):
        seq=[unit(i)]
        for _ in range(1,n):seq.append(act(seq[-1]))
        assert act(seq[-1])==seq[0]
        return seq
    if typ==(5,):
        columns=orbit(0,5)+[[-1,1,0,-1,0,0]]
        assert act(columns[-1])==columns[-1]
        blocks=['R5','Gm']
    elif typ==(4,1):
        w=unit(2)
        columns=orbit(0,4)+[w,act(w)]
        assert act(columns[-1])==[-x for x in w]
        blocks=['R4','U4']
    elif typ==(3,2):
        columns=orbit(0,6);blocks=['R6']
    elif typ==(3,1,1):
        columns=orbit(0,3)+orbit(1,3);blocks=['R3','R3']
    elif typ==(2,2,1):
        columns=orbit(2,2)+orbit(3,2)+[unit(0),unit(1)]
        assert act(columns[-1])==[-x for x in columns[-1]]
        assert act(columns[-2])==[-x for x in columns[-2]]
        blocks=['R2','R2','N2','N2']
    elif typ==(2,1,1,1):
        columns=orbit(0,2)+orbit(2,2)+orbit(3,2)
        blocks=['R2','R2','R2']
    else:
        assert typ==(1,1,1,1,1)
        columns=[unit(j) for j in range(6)]
        assert all(act(w)==w for w in columns)
        blocks=['Gm']*6
    U=[[columns[j][i] for j in range(6)] for i in range(6)]
    determinant=integral_matrix_determinant(U)
    assert abs(determinant)==1,(typ,determinant)
    # Verify Frobenius on the entire integral lattice, not merely a rational character.
    expected_orders={
      'Gm': lambda q:q-1,
      'R2': lambda q:q*q-1,
      'R3': lambda q:q**3-1,
      'R4': lambda q:q**4-1,
      'R5': lambda q:q**5-1,
      'R6': lambda q:q**6-1,
      'N2': lambda q:q+1,
      'U4': lambda q:q*q+1,
    }
    low=charpoly_matrix(M)
    for q in (2,3,5,7,11):
        actual=sum(low[k]*q**k for k in range(7))
        product=1
        for block in blocks:product*=expected_orders[block](q)
        assert actual==product,(typ,q,actual,product)
    return (blocks,determinant,columns)

EXPECTED={
 (5,):(0,(0,0)),
 (4,1):(1,(0,1)),
 (3,2):('q+1',(1,0)),
 (3,1,1):('q+1',(1,0)),
 (2,2,1):('2q+3',(2,3)),
 (2,1,1,1):('4q+1',(4,3)),
 (1,1,1,1,1):('10q-5',(10,15)),
}

def main():
    cases={};counts=Counter();representatives={}
    for p in permutations(range(5)):
        item=analyze(p);t=item[0];counts[t]+=1
        if t in cases:assert cases[t]==item,(p,item,cases[t])
        else:cases[t]=item;representatives[t]=p
    assert len(cases)==7 and sum(counts.values())==120
    assert sorted(counts.values())==sorted([24,30,20,20,15,10,1]) # group class sizes
    print('ALL_120_PERMUTATIONS_OK')
    print('TEN_COMPONENTS_FIFTEEN_NODES_THIRTY_BRANCHES')
    for t,item in sorted(cases.items(),reverse=True):
        _,chi,vo,eo,bo=item
        def d(a):return dict(a)
        fixed_v=d(vo).get(1,0);fixed_e=d(eo).get(1,0);fixed_b=d(bo).get(1,0)
        assert (fixed_v,fixed_e)==EXPECTED[t][1]
        val=(fixed_v,fixed_e,fixed_b)
        print('TYPE',t,'CLASS',counts[t],'CHI_LOW_TO_HIGH',chi,
              'COMPONENTS',dict(vo),'NODES',dict(eo),'BRANCHES',dict(bo),
              'RATIONAL_FOOTPRINT',val,'POINTS',f'({fixed_v})*(q+1)-{fixed_b}+{fixed_e}')
        assert sum(k*v for k,v in vo)==10
        assert sum(k*v for k,v in eo)==15
        assert sum(k*v for k,v in bo)==30
    for typ in sorted(cases,reverse=True):
        blocks,determinant,columns=certificate_of_integral_blocks(representatives[typ])
        print('TORUS_INTEGRAL_BLOCKS',typ,'BLOCKS',','.join(blocks),
              'UNIMODULAR_DET',determinant,
              'BASIS_COLUMNS',columns)
    print('INTEGRAL_TORUS_BLOCKS_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()

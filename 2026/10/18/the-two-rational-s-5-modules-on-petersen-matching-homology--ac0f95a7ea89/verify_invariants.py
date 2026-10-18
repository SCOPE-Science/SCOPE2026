"""Independent rational calculation via cyclic-group fixed subcomplexes.

Only the Python standard library is needed.
"""
from itertools import combinations, permutations
from fractions import Fraction
from collections import Counter

U = tuple(range(5))
vertices = tuple(combinations(U, 2))
# Graph edges, with a different ordering from vertex-pair lexicographic order.
vertices_index = {x:i for i,x in enumerate(vertices)}
edge_data = {}
for i in U:
    rest = [x for x in U if x != i]
    for a,b,c,d in [(rest[0],rest[1],rest[2],rest[3]),
                    (rest[0],rest[2],rest[1],rest[3]),
                    (rest[0],rest[3],rest[1],rest[2])]:
        v = vertices_index[tuple(sorted((a,b)))]
        w = vertices_index[tuple(sorted((c,d)))]
        edge_data[tuple(sorted((v,w)))] = (i,tuple(sorted((a,b))),tuple(sorted((c,d))))
edges = tuple(sorted(edge_data, key=lambda x:edge_data[x]))
assert len(edges)==15
edge_number = {x:i for i,x in enumerate(edges)}
C={0:[()]}
for size in range(1,6):
    C[size]=[s for s in combinations(range(15),size)
             if len({v for i in s for v in edges[i]}) == 2*size]
assert [len(C[i]) for i in range(6)]==[1,15,75,145,90,6]
lookup={i:{s:j for j,s in enumerate(C[i])} for i in C}

def cyc_type(g):
    seen=set(); out=[]
    for i in U:
        if i not in seen:
            k=i; t=0
            while k not in seen:
                seen.add(k);t+=1;k=g[k]
            out.append(t)
    return tuple(sorted(out, reverse=True))

def edge_perm(g):
    p=[vertices_index[tuple(sorted(g[x] for x in v))] for v in vertices]
    return [edge_number[tuple(sorted(p[x] for x in e))] for e in edges]

def act_face(face,p):
    mapped=[p[i] for i in face]
    sign=(-1)**sum(mapped[i]>mapped[j]
                   for i in range(len(mapped)) for j in range(i+1,len(mapped)))
    return tuple(sorted(mapped)),sign

def fixed_basis(size,p):
    """Invariant orbit-sum basis, listed as integer coordinate dictionaries."""
    seen=set(); result=[]; rep=[]; killed=[]
    for f in C[size]:
        if f in seen: continue
        orbit={}; cur=f; coefficient=1
        while cur not in orbit:
            orbit[cur]=coefficient;seen.add(cur)
            cur,eps=act_face(cur,p)
            coefficient*=eps
        assert cur==f
        if coefficient==1:
            result.append(orbit);rep.append(f)
        else:
            killed.append(f)
    return result,rep,killed

def rational_rank_sparse_columns(columns):
    """Exact Gaussian elimination over Q on sparse integer columns."""
    basis={}
    for col in columns:
        v={i:Fraction(a) for i,a in col.items() if a}
        while v:
            r=min(v); a=v[r]
            if r not in basis:
                basis[r]={j:q/a for j,q in v.items()};break
            for j,q in basis[r].items():
                v[j]=v.get(j,Fraction(0))-a*q
                if not v[j]: del v[j]
    return len(basis)

def invariants_for(g):
    p=edge_perm(g)
    tuples=[fixed_basis(k,p) for k in range(6)]
    # Each invariant chain is uniquely determined by its coefficient at
    # one chosen representative of every coherently oriented orbit.
    ranks={0:0}
    for k in range(1,6):
        target={f:i for i,f in enumerate(tuples[k-1][1])}
        columns=[]
        for orbit in tuples[k][0]:
            bd=Counter()
            for face,coeff in orbit.items():
                for j in range(k):
                    sub=face[:j]+face[j+1:]
                    bd[sub]+=coeff*(-1)**j
            # Test invariance of the boundary on every face, not just reps.
            for face,coeff in bd.items():
                im,eps=act_face(face,p)
                assert bd[im]==coeff*eps
            assert all(not bd[f] for f in tuples[k-1][2])
            columns.append({target[f]:bd[f] for f in target if bd[f]})
        ranks[k]=rational_rank_sparse_columns(columns)
    inv=[len(tuples[k][0])-ranks[k]-ranks[k+1] for k in range(1,5)]
    return inv, [len(x[0]) for x in tuples],ranks

def represent_type(t):
    start=0;g=list(range(5))
    for size in t:
        c=list(range(start,start+size))
        for i,a in enumerate(c):g[a]=c[(i+1)%size]
        start+=size
    return tuple(g)

answers={}
for t in sorted({cyc_type(g) for g in permutations(U)}):
    g=represent_type(t)
    inv,cnt,rank=invariants_for(g)
    assert inv[0]==0 and inv[1]==0
    answers[t]=inv[-2:]
    print('fixed_homology',t,tuple(inv[-2:]),'invariant_chains',cnt,'boundary_ranks',rank)

# Character values from fixed homology: dim V^<g>=|g|^{-1}sum chi(g^j).
# Every nonidentity power of a 3-cycle or 5-cycle is conjugate to its inverse.
chi={};dim=answers[(1,1,1,1,1)]
for t in [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(4,1),(5,),(3,2)]:
    fixed=answers[t]
    if t==(1,1,1,1,1): char=dim
    elif t in [(2,1,1,1),(2,2,1)]:char=[2*x-y for x,y in zip(fixed,dim)]
    elif t==(3,1,1):char=[(3*x-y)//2 for x,y in zip(fixed,dim)]
    elif t==(4,1):char=[(4*x-y-z)//2 for x,y,z in zip(fixed,dim,chi[(2,2,1)])]
    elif t==(5,):char=[(5*x-y)//4 for x,y in zip(fixed,dim)]
    else:char=[(6*x-y-2*z-w)//2 for x,y,z,w in zip(fixed,dim,chi[(3,1,1)],chi[(2,1,1,1)])]
    chi[t]=char
print('characters',chi)
for t,h in chi.items():
    sgn=(-1)**(5-len(t))
    fivepoint=sum(x==1 for x in t)
    f2=sum(x for x in t if x in [1,2])
    expected2=sgn*fivepoint
    expected3=((fivepoint-1)**2+(f2-1))//2-fivepoint
    assert h==[expected2,expected3],(t,h,expected2,expected3)
print('INDEPENDENT_ORBIT_PROOF_OK')

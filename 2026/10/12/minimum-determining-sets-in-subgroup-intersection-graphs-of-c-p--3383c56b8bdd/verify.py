#!/usr/bin/env python3
from itertools import product, combinations
from math import comb

def norm(v,p):
    v=tuple(x%p for x in v)
    if not any(v): return None
    i=next(i for i,x in enumerate(v) if x)
    inv=pow(v[i],-1,p)
    return tuple((x*inv)%p for x in v)

def det3(f,p):
    a,b,c,d,e,f1,g,h,i=f
    return (a*(e*i-f1*h)-b*(d*i-f1*g)+c*(d*h-e*g))%p

def adjugate_inverse(f,p):
    a,b,c,d,e,f1,g,h,i=f
    cof=(e*i-f1*h, c*h-b*i, b*f1-c*e,
          f1*g-d*i, a*i-c*g, c*d-a*f1,
          d*h-e*g, b*g-a*h, a*e-b*d)
    invdet=pow(det3(f,p),-1,p)
    return tuple((x*invdet)%p for x in cof)

def projective_objects(p):
    pts=sorted({norm(v,p) for v in product(range(p),repeat=3) if any(v)})
    lns=pts[:] # normalized nonzero covectors
    return pts,lns

def incident(P,L,p):
    return sum(x*y for x,y in zip(P,L))%p==0

def pgl_reps(p):
    reps=set()
    for f in product(range(p),repeat=9):
        if det3(f,p)==0: continue
        j=next(j for j,x in enumerate(f) if x)
        inv=pow(f[j],-1,p)
        reps.add(tuple((x*inv)%p for x in f))
    return sorted(reps)

def apply_point(f,v,p):
    M=(f[:3],f[3:6],f[6:])
    return norm(tuple(sum(M[i][j]*v[j] for j in range(3))%p for i in range(3)),p)

def apply_line(f,l,p):
    inv=adjugate_inverse(f,p)
    M=(inv[:3],inv[3:6],inv[6:])
    return norm(tuple(sum(l[j]*M[j][k] for j in range(3))%p for k in range(3)),p)

def build_actions(p):
    pts,lns=projective_objects(p); t=len(pts)
    pi={v:i for i,v in enumerate(pts)}
    li={v:i for i,v in enumerate(lns)}
    reps=pgl_reps(p)
    acts=[]
    for f in reps:
        pa=[pi[apply_point(f,v,p)] for v in pts]
        la=[li[apply_line(f,l,p)] for l in lns]
        acts.append(pa+[t+x for x in la])
    return pts,lns,reps,acts

def graph_edges(p,pts,lns):
    t=len(pts); E=set()
    for i,j in combinations(range(t),2):
        pass # distinct point vertices are nonadjacent
    for i,j in combinations(range(t),2):
        E.add((t+i,t+j))
    for i,P in enumerate(pts):
        for j,L in enumerate(lns):
            if incident(P,L,p): E.add((i,t+j))
    return E

def stabilizer_masks(acts,n):
    masks=[]
    for v in range(n):
        m=0
        for k,a in enumerate(acts):
            if a[v]==v: m|=1<<k
        masks.append(m)
    return masks

def base_stats(p,k):
    pts,lns,reps,acts=build_actions(p); t=len(pts); n=2*t
    E=graph_edges(p,pts,lns)
    # Exact graph/degree checks.
    deg=[0]*n
    for u,v in E: deg[u]+=1; deg[v]+=1
    assert set(deg[:t])=={p+1}
    assert set(deg[t:])=={(p+1)**2}
    # Every PGL representative preserves every graph edge/nonedge.
    for a in acts:
        img={tuple(sorted((a[u],a[v]))) for u,v in E}
        assert img==E
    expected=p**3*(p**3-1)*(p**2-1)
    assert len(reps)==expected
    masks=stabilizer_masks(acts,n)
    allmask=(1<<len(acts))-1
    # identity is first? detect instead.
    ids=[idx for idx,a in enumerate(acts) if all(a[v]==v for v in range(n))]
    assert len(ids)==1
    idmask=1<<ids[0]
    counts={}
    total=0
    for S in combinations(range(n),k):
        m=allmask
        for v in S: m &= masks[v]
        if m==idmask:
            typ=sum(v<t for v in S)
            counts[typ]=counts.get(typ,0)+1
            total+=1
    return t,expected,total,counts

t2,g2,total2,c2=base_stats(2,3)
assert t2==7 and g2==168 and total2==56 and c2=={0:28,3:28}
# No two-vertex determining set for p=2.
pts,lns,reps,acts=build_actions(2); masks=stabilizer_masks(acts,14)
ididx=next(i for i,a in enumerate(acts) if all(a[v]==v for v in range(14)))
for S in combinations(range(14),2):
    m=(1<<len(acts))-1
    for v in S:m&=masks[v]
    assert m!=(1<<ididx)

t3,g3,total3,c3=base_stats(3,4)
assert t3==13 and g3==5616
assert total3==5*g3//12==2340
assert c3=={0:g3//24,1:g3//6,3:g3//6,4:g3//24}
# No three-vertex determining set for p=3.
pts,lns,reps,acts=build_actions(3); masks=stabilizer_masks(acts,26)
ididx=next(i for i,a in enumerate(acts) if all(a[v]==v for v in range(26)))
for S in combinations(range(26),3):
    m=(1<<len(acts))-1
    for v in S:m&=masks[v]
    assert m!=(1<<ididx)

# Direct combinatorial count formulas for several odd primes.
for p in (3,5,7,11):
    t=p*p+p+1
    g=p**3*(p**3-1)*(p**2-1)
    ordered_triangles=g//((p-1)**2)
    triangles=ordered_triangles//6
    avoiding=t-3*p
    assert avoiding==(p-1)**2
    frames=g//24
    mixed=triangles*avoiding
    assert mixed==g//6
    assert 2*frames+2*mixed==5*g//12

print(f"p=2: |PGL|={g2}, minimum determining sets={total2}, type counts={c2}")
print(f"p=3: |PGL|={g3}, minimum determining sets={total3}, type counts={c3}")
print("odd-prime counting identities checked for p=3,5,7,11")
print("VERIFY_OK")

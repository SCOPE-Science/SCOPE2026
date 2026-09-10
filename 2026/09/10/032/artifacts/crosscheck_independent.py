"""Independent cross-check via a different code path (stdlib only).

- J^2 generators built from ALL covers (not only minimal), so pair-sums from
  non-minimal covers are included explicitly.
- Minimality of 2-covers tested by descent against the full 2-cover set.
- Recomputes sdefect for l=1..5; must match verify_target.py exactly.
"""
import itertools

def build_D(l):
    verts = ['a1','a2','a3','b1','b2','b3'] + ([f'z{i}' for i in range(1,l)] if l>=2 else [])
    idx={v:i for i,v in enumerate(verts)}
    edges=[('a1','a2'),('a2','a3'),('a1','a3'),('b1','b2'),('b2','b3'),('b1','b3')]
    if l==1: edges.append(('a1','b1'))
    else:
        edges.append(('a1','z1'))
        for i in range(1,l-1): edges.append((f'z{i}',f'z{i+1}'))
        edges.append((f'z{l-1}','b1'))
    return verts,[(idx[u],idx[v]) for u,v in edges]

EXPECTED={1:5,2:7,3:13,4:20,5:29}
ok=True
for l in [1,2,3,4,5]:
    verts,E=build_D(l); n=len(verts)
    allcovers=[[1 if (m>>i)&1 else 0 for i in range(n)] for m in range(1<<n)
               if all(((m>>i)&1 or (m>>j)&1) for i,j in E)]
    gens2=set()
    for c1 in allcovers:
        for c2 in allcovers:
            gens2.add(tuple(c1[i]+c2[i] for i in range(n)))
    S=[a for a in itertools.product(range(3),repeat=n) if all(a[i]+a[j]>=2 for i,j in E)]
    Sset=set(S)
    def minimal(a):
        for k in range(n):
            if a[k]>=1:
                b=tuple(a[i]-1 if i==k else a[i] for i in range(n))
                if b in Sset: return False
        return True
    min2=[a for a in S if minimal(a)]
    out=[a for a in min2 if not any(all(g[i]<=a[i] for i in range(n)) for g in gens2)]
    match = (len(out)==EXPECTED[l])
    ok = ok and match
    print(f"l={l}: allcovers={len(allcovers)} gens2={len(gens2)} min2={len(min2)} sdefect={len(out)} expected={EXPECTED[l]} {'MATCH' if match else 'MISMATCH'}")
print("CROSS_CHECK:", "PASS" if ok else "FAIL")

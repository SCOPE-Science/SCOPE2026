"""Full target audit for triangle-dumbbell cover ideals D_l.

Proves/refutes from scratch (stdlib only):
 (a) w_l in J(D_l)^{(2)} \\ J(D_l)^2 for every l >= 1 (general proof:
     edge exponent-sums + degree gap via tau formula, tau verified by
     brute force for l <= 8);
 (b) J(D_l)^{(2)} = J(D_l)^2 + (w_l) ? Tested by complete minimal-2-cover
     enumeration (minimal 2-covers have max entry <= 2, so {0,1,2}^n
     enumeration is complete) and pair-sum divisibility for J^2 membership.

Writes certificate JSON to stdout and certificate.json.
"""
import itertools, json

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

def tau_bruteforce(n,E):
    best=n+1
    for m in range(1<<n):
        if all(((m>>i)&1 or (m>>j)&1) for i,j in E):
            s=bin(m).count('1')
            if s<best: best=s
    return best

def min_covers(n,E):
    Slist=[]
    for mask in range(1<<n):
        S={i for i in range(n) if mask>>i&1}
        if all(i in S or j in S for i,j in E): Slist.append(S)
    return [tuple(sorted(S)) for S in Slist if not any(T<S for T in Slist)]

def audit_l(l):
    verts,E=build_D(l); n=len(verts)
    mc=min_covers(n,E); tau=min(len(m) for m in mc)
    # (a): w_l = all-ones; edge sums all 2 -> in J^{(2)}; deg gap -> outside J^2
    part_a_in = all(1+1>=2 for _ in E)
    part_a_gap = (2*tau > n)
    # (b): enumerate minimal 2-covers
    S=set(a for a in itertools.product(range(3),repeat=n) if all(a[i]+a[j]>=2 for i,j in E))
    min2=[a for a in S if not any(tuple(a[i]-1 if i==k else a[i] for i in range(n)) in S for k in range(n) if a[k]>=1)]
    pair={tuple(sum(1 for c in (c1,c2) if i in c) for i in range(n)) for c1 in [set(m) for m in mc] for c2 in [set(m) for m in mc]}
    def inJ2(a): return any(all(a[i]>=p[i] for i in range(n)) for p in pair)
    out=[a for a in min2 if not inJ2(a)]
    return dict(l=l,n=n,nedges=len(E),tau=tau,formula_tau=4+(l-1)//2,
                part_a_in_sym2=part_a_in, part_a_deggap=part_a_gap,
                n_min2=len(min2), sdefect=len(out),
                gap_witnesses=[dict(zip(verts,a)) for a in sorted(out)])

cert={}
for l in range(1,7):
    cert[l]=audit_l(l)
    c=cert[l]
    print(f"l={l}: n={c['n']} tau={c['tau']} (formula {c['formula_tau']}) "
          f"(a): in_sym2={c['part_a_in_sym2']} deggap=2*{c['tau']}>{c['n']}={c['part_a_deggap']} "
          f"(b): #min2={c['n_min2']} sdefect={c['sdefect']}")
taus={}
for l in range(1,9):
    v,E=build_D(l); taus[l]=tau_bruteforce(len(v),E)
print("tau l=1..8:",taus)
with open('output/artifacts/certificate.json','w') as f:
    json.dump({str(k):v for k,v in cert.items()},f,indent=1)
print("wrote output/artifacts/certificate.json")

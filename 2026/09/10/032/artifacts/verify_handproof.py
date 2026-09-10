"""Verify the general-l hand-proof certificates for the target audit (stdlib only).

Certifies for each l in 1..12:
 (H1) tau construction: C* = {a1,a2,b1,b2} U {z_{2j}} is a vertex cover of
      size 4+floor((l-1)/2)  =>  tau(D_l) <= 4+floor((l-1)/2)
      (combined with brute-force tau >= formula, tau formula is exact;
      the report gives a case-analysis lower-bound proof).
 (H2) The 5 canonical patterns W0,M1..M4 are 2-covers (edge sums >= 2),
      minimal 2-covers (no single decrement is a 2-cover), and outside J^2
      (no minimal-cover pair-sum lies below), with the degree-gap fact
      deg(W0)=l+5 < 2*tau for the all-ones witness.
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

def min_covers(n,E):
    Slist=[]
    for mask in range(1<<n):
        S={i for i in range(n) if mask>>i&1}
        if all(i in S or j in S for i,j in E): Slist.append(S)
    return [tuple(sorted(S)) for S in Slist if not any(T<S for T in Slist)]

def pat(verts,Lp,Rp):
    m={}
    for v,x in zip(['a1','a2','a3'],Lp): m[v]=x
    for v,x in zip(['b1','b2','b3'],Rp): m[v]=x
    for v in verts:
        if v.startswith('z'): m[v]=1
    return tuple(m[v] for v in verts)

PATS={'W0':((1,1,1),(1,1,1)),'M1':((1,1,1),(2,0,2)),'M2':((1,1,1),(2,2,0)),
      'M3':((2,0,2),(1,1,1)),'M4':((2,2,0),(1,1,1))}

print("l | tau<=formula? | H1-constr-cover? size | W0 deggap | patterns: 2cov/min/outJ2")
for l in range(1,13):
    verts,E=build_D(l); n=len(verts); idx={v:i for i,v in enumerate(verts)}
    mc=min_covers(n,E); tau=min(len(m) for m in mc)
    formula=4+(l-1)//2
    # H1 construction
    C={'a1','a2','b1','b2'}|{f'z{2*j}' for j in range(1,n) if 2*j<=l-1}
    Ci={idx[v] for v in C}
    covers=all(i in Ci or j in Ci for i,j in E)
    w=pat(verts,(1,1,1),(1,1,1))
    sets=[set(m) for m in mc]
    flags=[]
    for name,(Lp,Rp) in PATS.items():
        m=pat(verts,Lp,Rp)
        is2=all(m[i]+m[j]>=2 for i,j in E)
        mins=True
        for k in range(n):
            if m[k]>=1:
                b=tuple(m[i]-1 if i==k else m[i] for i in range(n))
                if all(b[i]+b[j]>=2 for i,j in E): mins=False;break
        inJ2=any(all((1 if i in c1 else 0)+(1 if i in c2 else 0)<=m[i] for i in range(n))
                 for c1 in sets for c2 in sets)
        flags.append(f"{name}:{'OK' if (is2 and mins and not inJ2) else 'FAIL'}")
    print(f"{l:2d}| tau={tau}<=formula={formula}?{tau<=formula} | constr size={len(C)} cover={covers} | "
          f"degW0={sum(w)}<2tau={2*tau}?{sum(w)<2*tau} | "+" ".join(flags))
print("ALL CHECKS DONE")

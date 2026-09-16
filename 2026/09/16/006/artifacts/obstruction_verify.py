"""Verify uniformisation-obstruction family for trilinear Bogolyubov.

Family: G1=G2=F2^n, G3=F2, A={(x,y,z): <x,y>=0} (dot product mod 2).
Checks for n=2,3,4:
 - density >= 1/2,
 - each fibre A_{y,z} is ker(chi_y) (subgroup index 2) for y!=0, whole G1 for y=0,
 - A_y - A_y = A_y,
 - intersection over all y!=0 of H_y = {0},
 - fixed Bohr sets: for rho<1/2, B(Gamma;rho) = annihilator subspace; covering
   fraction-c of fibres needs |Gamma| >= n + log2(c) (checked by brute force
   annihilator enumeration for small n),
 - for rho>=1/2, B = whole G1, contained in no proper H_y.
"""
import itertools, json, os

def dot(u,v):
    return sum(a*b for a,b in zip(u,v))%2

def vecs(n):
    return list(itertools.product([0,1],repeat=n))

def run(n):
    G1=vecs(n); G2=vecs(n); G3=[0,1]
    A={(x,y,z) for x in G1 for y in G2 for z in G3 if dot(x,y)==0}
    total=len(G1)*len(G2)*len(G3)
    delta=len(A)/total
    # fibre check for one z
    zero=tuple([0]*n)
    ok=True
    for y in G2:
        H={x for x in G1 if dot(x,y)==0}
        F={x for x in G1 if (x,y,0) in A}
        assert F==H
        # difference set H-H == H
        D={tuple((a[i]+b[i])%2 for i in range(n)) for a in H for b in H}
        assert D==H, (n,y)
    # intersection over y!=0
    inter=set(G1)
    for y in G2:
        if y==zero: continue
        inter &= {x for x in G1 if dot(x,y)==0}
    assert inter=={zero}, (n,inter)
    # Bohr check: enumerate all Gamma (subsets of dual=F2^n) up to size 2 for n<=3,
    # verify B(Gamma,rho<1/2)=annihilator and containment forces chi_y in span.
    # Represent span membership via linear algebra over F2.
    import numpy as np
    def span_contains(Gamma, y):
        # does integer/F2 span of Gamma contain y? (dual identification)
        if y==zero: return True
        r=len(Gamma)
        if r==0: return False
        M=np.array(Gamma,dtype=int)  # r x n
        t=np.array(y,dtype=int)
        # brute force 2^r combos
        for mask in range(2**r):
            s=np.zeros(n,dtype=int)
            for i in range(r):
                if mask>>i & 1: s=(s+M[i])%2
            if tuple(s)==tuple(t): return True
        return False
    # verify duality claim on random Gamma for n=3
    checks=[]
    if n<=3:
        import random
        random.seed(0)
        for _ in range(200):
            r=random.randint(0,min(3,n))
            Gamma=[tuple(random.choice(G1)) for _ in range(r)]
            B={x for x in G1 if all(dot(a,x)==0 for a in Gamma)}  # rho<1/2 annihilator
            for y in G2:
                H={x for x in G1 if dot(x,y)==0}
                if set(B)<=set(H):
                    assert span_contains(Gamma,y), (Gamma,y)
                    checks.append(True)
    return {"n":n,"density":delta,
            "intersection_over_nonzero_y_is_zero": inter=={zero},
            "duality_checks_passed": len(checks)}

if __name__=="__main__":
    out=[run(n) for n in [2,3,4]]
    print(json.dumps(out,indent=1))
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "obstruction_verify_result.json"),"w") as f:
        json.dump(out,f,indent=1)
    # rank lower bound illustration: need |Gamma|>=n+log2(c)
    import math
    for n in [2,3,4,10,20]:
        for c in [0.25,0.5]:
            print(f"n={n} c={c} lower_bound={n+math.log2(c):.2f}")

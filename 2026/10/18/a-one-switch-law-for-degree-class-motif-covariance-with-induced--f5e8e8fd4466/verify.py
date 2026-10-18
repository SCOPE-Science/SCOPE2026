"""Exact finite-graph verification of degree-class/motif covariance identities.

Uses exhaustive edge-mask enumeration and rational expectations independent of the
conditioning derivation. Every counting convention is specified in the program.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import permutations


def h_edges(h, edge_pairs):
    return {tuple(sorted(x)) for x in edge_pairs}


def fall(a, r):
    if r > a: return 0
    t = 1
    for j in range(r): t *= a-j
    return t


def b(n, k, p):
    if k < 0 or k > n: return Fraction(0)
    return comb(n, k) * p**k * (1-p)**(n-k)


def predicted(n, k, h, edges, p, induced):
    deg = [0]*h
    for i,j in edges:
        deg[i]+=1; deg[j]+=1
    e = len(edges)
    q = 1-p
    required = comb(h,2)-e if induced else 0
    event = fall(n,h)*p**e*q**required
    baseline = h*b(n-1,k,p)
    if induced:
        cond = sum(b(n-h,k-d,p) for d in deg)
    else:
        cond = sum(b(n-1-d,k-d,p) for d in deg)
    return event*(cond-baseline)


def exhaustive(n,k,h,edges,p,induced):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    M=len(pairs)
    index = {pair:i for i,pair in enumerate(pairs)}
    embeddings=[]
    for f in permutations(range(n),h):
        on=0; off=0
        for i in range(h):
            for j in range(i+1,h):
                mask = 1<<index[tuple(sorted((f[i],f[j])))]
                if (i,j) in edges: on|=mask
                else: off|=mask
        embeddings.append((on,off))
    A=B=C=Fraction(0)
    q=1-p
    weights=[p**m*q**(M-m) for m in range(M+1)]
    for x in range(1<<M):
        degree=[0]*n
        for a,(i,j) in enumerate(pairs):
            if (x>>a)&1:degree[i]+=1;degree[j]+=1
        dk=sum(d==k for d in degree)
        cnt=sum((x&on)==on and (not induced or (x&off)==0) for on,off in embeddings)
        w=weights[x.bit_count()]
        A+=w*dk*cnt; B+=w*dk; C+=w*cnt
    return A-B*C


def main():
    motifs = [
        ('edge',2,{(0,1)}),
        ('path3',3,{(0,1),(1,2)}),
        ('triangle',3,{(0,1),(1,2),(0,2)}),
        ('edge_isolate',3,{(0,1)}),
        ('empty3',3,set()),
    ]
    checks=0
    for n in (3,4,5):
        for title,h,ed in motifs:
            if n<h:continue
            for p in (Fraction(1,5),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(4,5)):
                for k in range(n):
                    for induced in (False,True):
                        observed=exhaustive(n,k,h,ed,p,induced)
                        theory=predicted(n,k,h,ed,p,induced)
                        assert observed==theory, (n,title,k,p,induced,observed,theory)
                        checks+=1
    # Sharp double re-entrance in the induced 3-path for n=4.
    ed={(0,1),(1,2)}
    for p,sgn in [(Fraction(1,5),1),(Fraction(1,3),0),(Fraction(1,2),-1), (Fraction(2,3),0),(Fraction(4,5),1)]:
        val=predicted(4,1,3,ed,p,True)
        assert (val>0)-(val<0)==sgn
        checks+=1
    # The same non-induced path has exactly one sign switch.
    for p,sgn in [(Fraction(1,10),1),(Fraction(2,9),0),(Fraction(1,2),-1)]:
        val=predicted(4,1,3,ed,p,False)
        assert (val>0)-(val<0)==sgn
        checks+=1
    print(f'PASS: {checks} exact rational independent enumeration/formula comparisons and sign assertions')

if __name__=='__main__':main()

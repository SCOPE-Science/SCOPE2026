"""Exact rational star discrepancy. alpha=(P+Q s5)/R, s5=sqrt(5).
For each x_n={n alpha}: to compare Fractions u/v vs r + t s5 we decide sign of A + B s5
by integer arithmetic (B==0 -> sign A; else square). Implement comparator via key:
internal exact ordering of values a + b s5 (a,b Fractions) with common denom scaling to ints.
Then sort indices by x_n exactly, compute discrepancies as (i/N - x) and (x-(i-1)/N)
maxima as A+B s5 forms; report float + exact pair. Three-distance cross-check: gap multiset
has <=3 distinct values (exact equality classes)."""
import json, math
from fractions import Fraction
S5 = math.sqrt(5)

recs = json.load(open("output/artifacts/alpha_table.json"))
RBYW = {tuple(r["w"]): r for r in recs}

def s5sign(A, B):
    # A,B ints (not both zero); sign of A + B sqrt5
    if B == 0: return (A>0)-(A<0)
    if A == 0: return (B>0)-(B<0)
    if (A>=0)==(B>=0): return (A>=0)*2-1  # same sign, nonzero
    # opposite signs: compare A^2 vs 5B^2
    d = A*A - 5*B*B
    return (d>0)-(d<0) if A>0 else -((d>0)-(d<0))

def cmp_xn(n1, n2, P, Q, R):
    # compare frac(n1 a) vs frac(n2 a): n1 a - floor, exact via floor from float with correction
    # compute exact floor by float guess then adjust with s5sign
    for n in (n1, n2): pass
    return None

# Precompute floors robustly: f_n = floor(n*alpha) via float guess +-2 correction with exact sign tests
def floors(P,Q,R,N):
    # returns list f[1..N]
    f = [0]*(N+1)
    for n in range(1,N+1):
        g = int(math.floor(n*(P+Q*S5)/R))
        # adjust: need exact test nP + nQ s5 - gR ? 0 and vs R
        while True:
            A = n*P - g*R; B = n*Q
            s = s5sign(A,B)  # sign of (n alpha - g)
            if s >= 0:
                A2 = n*P-(g+1)*R; B2=B
                s2 = s5sign(A2,B2)
                if s2 >= 0: g+=1; continue
                else: break
            else: g-=1
        f[n]=g
    return f

def frac_parts(P,Q,R,N,f):
    # represent frac_n = (A_n + B_n s5)/R with A_n=nP-fR, B_n=nQ ; R>0
    return [(n*P-f[n]*R, n*Q) for n in range(N+1)]

def sort_idx(FP, R):
    idx=list(range(1,len(FP)-1+1))
    # sort by value (A+B s5)/R; comparison A1+B1 s5 vs A2+B2 s5
    import functools
    def cmp(i,j):
        A=(FP[i][0]-FP[j][0]); B=(FP[i][1]-FP[j][1])
        return s5sign(A,B)
    idx.sort(key=functools.cmp_to_key(cmp))
    return idx

def Dstar_exact(P,Q,R,N):
    f=floors(P,Q,R,N)
    FP=frac_parts(P,Q,R,N,f)
    idx=sort_idx(FP,R)
    # maxima of i/N - x_i and x_i-(i-1)/N as A+B s5 forms over denom RN
    # i/N - x = i/N - (A+Bs)/R = (iR - N A - N B s)/RN -> pair (iR-NA, -NB)
    best1=None; best2=None
    for k,i in enumerate(idx,1):
        A,B=FP[i]
        c1=(k*R - N*A, -N*B)
        c2=(N*A-(k-1)*R, N*B)
        if best1 is None or s5sign(c1[0]-best1[0], c1[1]-best1[1])>0: best1=c1
        if best2 is None or s5sign(c2[0]-best2[0], c2[1]-best2[1])>0: best2=c2
    # D* = max / RN ; sign vs 0
    c = best1 if s5sign(best1[0]-best2[0], best1[1]-best2[1])>=0 else best2
    val=(c[0]+c[1]*S5)/(R*N)
    return val, c, idx, FP

def gaps3(idx, FP, R):
    # successive gaps incl wrap; classify exact equality
    m=len(idx)
    gaps=[]
    for k in range(m):
        i1=idx[k]; i2=idx[(k+1)%m]
        if k<m-1: G=(FP[i2][0]-FP[i1][0], FP[i2][1]-FP[i1][1])
        else: G=(FP[i2][0]-FP[i1][0]+R, FP[i2][1]-FP[i1][1])
        gaps.append(G)
    classes=[]
    for G in gaps:
        for cl in classes:
            if G[0]==cl[0] and G[1]==cl[1]: cl.append(G); break
        else:
            # exact equality requires identical pair since 1,s5 independent over Q
            classes.append([G])
    # count distinct
    return len(classes), [len(c) for c in classes]

import sys
targets = sys.argv[1:]  # e.g. certify list or "all"
for N in (512,1024,2048):
    print(f"===== N={N} exact sweep over {len(recs)} alphas =====")
    vals=[]
    for r in recs:
        v,c,_,_=Dstar_exact(r["P"],r["Q"],r["R"],N)
        vals.append((v,c,tuple(r["w"])))
    vals.sort(key=lambda t:t[0])
    for v,c,w in vals[:6]:
        print(f"  {v:.10f} C={c} w={list(w)}")
    (v0,c0,w0),(v1,c1,w1)=vals[0],vals[1]
    print(f"  gap={v1-v0:.3e} minfrac check: Dmin*N={(v0*N):.10f}")
    # three-distance check on top + a sample
    for w in [w0, vals[-1][2], tuple(recs[len(recs)//2]["w"])]:
        r=RBYW[w]
        _,_,idx,FP=Dstar_exact(r["P"],r["Q"],r["R"],N)
        nc,cnts=gaps3(idx,FP,r["R"])
        print(f"  3-dist w={list(w)}: distinct={nc} counts={sorted(cnts,reverse=True)[:5]}")
    json.dump([{"w":list(w),"D":v,"C":list(c)} for v,c,w in vals],
              open(f"output/artifacts/Dstar_N{N}.json","w"))
    print(f"  saved Dstar_N{N}.json")

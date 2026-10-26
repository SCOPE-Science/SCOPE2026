"""Reproduction checks for sharp stability of scalar AMLE on metric stars.
Requires scipy for independent finite linear-program benchmarks.
"""
from fractions import Fraction
from itertools import combinations
from math import isclose
from random import Random
from scipy.optimize import linprog

def boundary_lip(vals, lengths):
    return max(abs(vals[i]-vals[j])/(lengths[i]+lengths[j])
               for i,j in combinations(range(len(lengths)),2))

def center(vals, lengths):
    active = max(combinations(range(len(lengths)),2),
                 key=lambda ij: abs(vals[ij[0]]-vals[ij[1]])/
                                (lengths[ij[0]]+lengths[ij[1]]))
    a,b = active
    return (lengths[b]*vals[a]+lengths[a]*vals[b])/(lengths[a]+lengths[b])

def predicted(lengths):
    if len(lengths) == 2:
        return Fraction(1)
    return max(Fraction(1) + (2*lengths[a]*lengths[b]) /
               ((lengths[a]+lengths[b])*lengths[i])
               for i in range(len(lengths))
               for a,b in combinations([k for k in range(len(lengths)) if k != i],2))

def lp_piece_norm(lengths,a,b,i):
    n=len(lengths)
    wa=float(lengths[b]/(lengths[a]+lengths[b])); wb=1-wa
    obj=[0.0]*n; obj[i]+=1.0;obj[a]-=wa;obj[b]-=wb
    # quotient by constants by fixing delta[0]=0
    A=[];B=[]
    for j,k in combinations(range(n),2):
        row=[0.0]*n;row[j]=1.0;row[k]=-1.0
        A.append(row);B.append(float(lengths[j]+lengths[k]));A.append([-q for q in row]);B.append(float(lengths[j]+lengths[k]))
    norm=0.0
    for sign in [1,-1]:
        r=linprog([-sign*v for v in obj],A_ub=A,b_ub=B,bounds=[(0,0)]+[(None,None)]*(n-1),method='highs')
        assert r.success, r.message
        norm=max(norm,-r.fun/float(lengths[i]))
    return norm

def main():
    rng=Random(902131)
    counts={'independent_LP_masks':0,'attaining_pairs':0,'random_pairs':0,'equilateral_cases':0}
    for n in range(2,8):
        for rep in range(10):
            lengths=[Fraction(rng.randrange(1,10),rng.randrange(1,7)) for _ in range(n)]
            formula=predicted(lengths)
            lpmax=1.0
            for a,b in combinations(range(n),2):
                for i in range(n):
                    lpmax=max(lpmax,lp_piece_norm(lengths,a,b,i))
                    counts['independent_LP_masks']+=1
            assert isclose(float(formula),lpmax,rel_tol=1e-9,abs_tol=1e-9),(lengths,formula,lpmax)
            if n>=3:
                best=max(((Fraction(1)+(2*lengths[a]*lengths[b])/((lengths[a]+lengths[b])*lengths[i]),a,b,i)
                            for i in range(n) for a,b in combinations([k for k in range(n) if k != i],2)))
                rat,a,b,i=best
                u=[Fraction(0)]*n;u[a]=-lengths[a];u[b]=lengths[b]
                d=[Fraction(0)]*n;d[a]=-lengths[a];d[b]=-lengths[b];d[i]=lengths[i]
                eps=Fraction(1,100)
                v=[u[k]+eps*d[k] for k in range(n)]
                assert boundary_lip(d,lengths)==1
                assert center(u,lengths)==0
                diff=center(v,lengths)-center(u,lengths)
                ratio=max(abs(eps*d[k]-diff)/lengths[k] for k in range(n))/eps
                assert ratio==rat,(lengths,rat,ratio)
                counts['attaining_pairs']+=1
            for k in range(50):
                u=[Fraction(rng.randrange(-12,13),5) for _ in range(n)]
                v=[Fraction(rng.randrange(-12,13),7) for _ in range(n)]
                delta=[a-b for a,b in zip(u,v)]
                bd=boundary_lip(delta,lengths)
                if bd==0:continue
                cd=center(u,lengths)-center(v,lengths)
                out=max(abs(delta[i]-cd)/lengths[i] for i in range(n))
                assert out <= formula*bd,(n,lengths,out,formula,bd)
                counts['random_pairs']+=1
    for n in range(2,15):
        lengths=[Fraction(1)]*n
        assert predicted(lengths)==(Fraction(1) if n==2 else Fraction(2))
        counts['equilateral_cases']+=1
    print('PASS',counts,'total',sum(counts.values()))

if __name__=='__main__':main()

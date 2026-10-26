#!/usr/bin/env python3
"""Exact arithmetic checks of finite star/path epidemic-tail identities.

All computations are finite consistency checks; the universal inequalities
and uniqueness statements are proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from math import comb
import json


def star_tail(n, t, p):
    q = 1-p
    return sum(F(k+1,n)*comb(n-1,k)*p**k*q**(n-1-k)
               for k in range(t-1,n))


def path_tail(n, t, p):
    return p**(t-1)*(t*(n-t+1)-(t-1)*(n-t)*p)/n


def pair_component_tail(n, t, p, star):
    # Direct finite check: enumerate every edge subset, build components,
    # then size-bias by the uniform epidemic seed.
    edges = [(0,j) for j in range(1,n)] if star else [(j,j+1) for j in range(n-1)]
    out=F(0)
    for mask in range(1<<(n-1)):
        parent=list(range(n))
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        for e,(u,v) in enumerate(edges):
            if mask>>e&1:
                ru,rv=root(u),root(v)
                parent[ru]=rv
        sizes={}
        for v in range(n):
            r=root(v)
            sizes[r]=sizes.get(r,0)+1
        good=sum(s for s in sizes.values() if s>=t)
        k=mask.bit_count()
        out += F(good,n)*p**k*(1-p)**(n-1-k)
    return out


def conditional_path(n,t,j):
    if j<t-1:return F(0)
    return F(comb(j,t-1),comb(n-1,t-1))*F(t*(n-1)+1-(t-1)*j,n)


def conditional_star(n,t,j):
    return F(j+1,n) if j>=t-1 else F(0)


def coeff_signs(n,t):
    return [int(conditional_star(n,t,j)>conditional_path(n,t,j))
            - int(conditional_star(n,t,j)<conditional_path(n,t,j))
            for j in range(n)]


def run():
    cert={"exact_arithmetic":"fractions.Fraction", "cases":{}, "examples":{}}
    counts={"tail_direct":0,"conditional_coefficients":0,"sign_blocks":0,
            "ratio_logconcavity":0,"mean_order":0}
    for n in range(3,10):
        for t in range(2,n+1):
            for p in [F(1,4),F(1,2),F(3,4)]:
                assert star_tail(n,t,p)==pair_component_tail(n,t,p,True)
                assert path_tail(n,t,p)==pair_component_tail(n,t,p,False)
                counts['tail_direct']+=2
    for n in range(4,61):
        for t in range(2,n+1):
            for j in range(n):
                # Use the elementary binomial identity for the Bernstein coefficient.
                if j<t-1:
                    assert conditional_path(n,t,j)==0
                else:
                    a=F(t*(n-t+1),n)*F(comb(j,t-1),comb(n-1,t-1))
                    b=F((t-1)*(n-t),n)*F(comb(j,t),comb(n-1,t)) if j>=t else 0
                    assert conditional_path(n,t,j)==a-b
                counts['conditional_coefficients']+=1
            if t==2:
                signs=coeff_signs(n,t)
                assert all(v<=0 for v in signs)
                assert any(v<0 for v in signs)
            elif t==n:
                assert all(v==0 for v in coeff_signs(n,t))
            else:
                signs=coeff_signs(n,t)
                ss=[x for x in signs if x]
                assert ss[0]==1
                assert ss==sorted(ss,reverse=True)
                neg = any(v<0 for v in signs)
                assert neg==(n>t*(t-1)+1)
                counts['sign_blocks']+=1
                R=[]
                for j in range(t-1,n):
                    R.append(conditional_path(n,t,j)/conditional_star(n,t,j))
                assert R[-1]==1 and R[0]<1
                for j in range(1,len(R)-1):
                    assert R[j]**2>R[j-1]*R[j+1]
                    counts['ratio_logconcavity']+=1
    for n in range(4,31):
        for p in [F(1,4),F(1,2),F(3,4)]:
            # Pair distance formula; no Monte Carlo.
            star_mean=F(1)+F(2*(n-1),n)*p+F((n-1)*(n-2),n)*p*p
            path_mean=F(1)+F(2,n)*sum((n-d)*p**d for d in range(1,n))
            assert star_mean>path_mean
            counts['mean_order']+=1
    p_lo,p_hi=F(1,2),F(19,20)
    assert star_tail(8,3,p_lo)>path_tail(8,3,p_lo)
    assert star_tail(8,3,p_hi)<path_tail(8,3,p_hi)
    cert['examples']={
        'n8_t3_p_half_tail_star':str(star_tail(8,3,p_lo)),
        'n8_t3_p_half_tail_path':str(path_tail(8,3,p_lo)),
        'n8_t3_p_19_over_20_tail_star':str(star_tail(8,3,p_hi)),
        'n8_t3_p_19_over_20_tail_path':str(path_tail(8,3,p_hi)),
        'n7_t3_p_half_star_minus_path':str(star_tail(7,3,p_lo)-path_tail(7,3,p_lo))
    }
    cert['cases']=counts
    cert['status']='all exact finite consistency checks passed'
    print(json.dumps(cert,indent=2,sort_keys=True))

if __name__=='__main__':run()

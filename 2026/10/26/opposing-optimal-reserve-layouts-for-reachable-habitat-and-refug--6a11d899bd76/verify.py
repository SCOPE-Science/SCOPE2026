"""Exact checks for ring-refuge Bernoulli site-retention identities.

All arithmetic uses fractions. The enumeration is finite corroboration;
unrestricted results require the accompanying algebraic proof.
"""
from fractions import Fraction
from itertools import combinations, product
from collections import defaultdict
import hashlib
import json


def gap_law(length, p):
    q = 1-p
    if length == 0:
        return [Fraction(1)]
    return [(j+1)*q*q*p**j for j in range(length-1)] + [length*q*p**(length-1), p**length]


def convolve(a, b):
    ans = [Fraction(0)]*(len(a)+len(b)-1)
    for j, x in enumerate(a):
        for h, y in enumerate(b):
            ans[j+h] += x*y
    return ans


def law_formula(gaps,p):
    ans = [Fraction(1)]
    for length in gaps:
        ans = convolve(ans,gap_law(length,p))
    return ans


def connected_formula(gaps,p):
    s = sum(gaps)
    return p**s * (sum(p**(-length) for length in gaps) -(len(gaps)-1))


def gaps_of(n, protected):
    refs = sorted(protected)
    k = len(refs)
    return tuple((refs[(i+1)%k]-refs[i]-1)%n for i in range(k))


def direct(n, refs, p):
    refs=set(refs)
    others=[j for j in range(n) if j not in refs]
    hist=[Fraction(0)]*(len(others)+1)
    all_connected=Fraction(0)
    for flags in product((0,1),repeat=len(others)):
        alive=refs | {v for v,a in zip(others,flags) if a}
        weight=p**sum(flags)*(1-p)**(len(others)-sum(flags))
        def reachable(starts):
            found=set(starts)
            queue=list(starts)
            while queue:
                u=queue.pop()
                for v in ((u-1)%n,(u+1)%n):
                    if v in alive and v not in found:
                        found.add(v)
                        queue.append(v)
            return found
        covered=reachable(refs)
        hist[len(covered)-len(refs)] += weight
        if refs.issubset(reachable({next(iter(refs))})):
            all_connected += weight
    return hist,all_connected


def dominates(left,right):
    assert len(left)==len(right)
    tail_l=tail_r=Fraction(0)
    strict=False
    for i in range(len(left)-1,-1,-1):
        tail_l+=left[i];tail_r+=right[i]
        if tail_l<tail_r:return False,False
        if tail_l>tail_r:strict=True
    return True,strict


def comps(total, count):
    if count==1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in comps(total-first,count-1):
                yield (first,)+rest


def verify():
    checks={'direct_enumerations':0,'gap_laws':0,'balancing_edges':0,
            'global_extrema':0,'polynomial_tail_certificates':0,'connectivity_extrema':0,
            'coverage_ceiling':0}
    digest=hashlib.sha256()
    for p in (Fraction(1,3),Fraction(2,3)):
        for n in range(3,10):
            for k in range(2,min(n,5)+1):
                for tail in combinations(range(1,n),k-1):
                    refs=(0,)+tail
                    gaps=gaps_of(n,refs)
                    observed,cprob=direct(n,refs,p)
                    pred=law_formula(gaps,p)
                    assert observed==pred, ('gap',n,k,gaps,p)
                    assert cprob==connected_formula(gaps,p), ('connect',n,k,gaps,p)
                    checks['direct_enumerations']+=1
                    digest.update(str((n,k,gaps,str(p),tuple(map(str,observed)),str(cprob))).encode())
    for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
        for length in range(0,16):
            g=gap_law(length,p)
            assert sum(g)==1 and all(x>=0 for x in g)
            checks['gap_laws']+=1
        for n in range(3,15):
            for k in range(2,min(n,5)+1):
                s=n-k
                memo={}
                for g in set(tuple(sorted(c,reverse=True)) for c in comps(s,k)):
                    memo[g]=(law_formula(g,p),connected_formula(g,p))
                B=tuple(sorted((s//k+1,)*(s%k)+(s//k,)*(k-s%k),reverse=True))
                E=tuple(sorted((s,)+(0,)*(k-1),reverse=True))
                for g,(law,cprob) in memo.items():
                    ok1,_=dominates(memo[B][0],law)
                    ok2,_=dominates(law,memo[E][0])
                    assert ok1 and ok2,(n,k,g,p,'global coverage')
                    assert memo[B][1]<=cprob<=memo[E][1],(n,k,g,p,'global connectivity')
                    checks['global_extrema']+=1
                    checks['connectivity_extrema']+=1
                    for i in range(k):
                        for j in range(k):
                            if g[i]>=g[j]+2:
                                h=list(g)
                                h[i]-=1
                                h[j]+=1
                                h=tuple(sorted(h,reverse=True))
                                if h==g:continue
                                good,strict=dominates(memo[h][0],law)
                                assert good,(n,k,g,h,p,'local coverage')
                                assert (strict == (g[i]>2 or g[j]!=0)),(n,k,g,h,p,'strict')
                                assert memo[h][1]<cprob,(n,k,g,h,p,'local connectivity')
                                checks['balancing_edges']+=1
                    if max(g)<=2:
                        expected=[Fraction(1)]
                        for _ in range(s):expected=convolve(expected,[1-p,p])
                        assert expected==law
                        checks['coverage_ceiling']+=1
    # Coefficients of (Q_a Q_b - Q_(a-1) Q_(b+1)) / (1-z)
    # are exactly the balancing improvements in upper-tail probabilities.
    for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
        for b in range(0,9):
            for a in range(b+2,19):
                old=convolve(gap_law(a,p),gap_law(b,p))
                new=convolve(gap_law(a-1,p),gap_law(b+1,p))
                cumulative=Fraction(0)
                coeff=[]
                for x,y in zip(old,new):
                    cumulative+=x-y
                    coeff.append(cumulative)
                assert cumulative==0 and all(t>=0 for t in coeff), (a,b,p,'tails')
                assert (any(t>0 for t in coeff)) == ((a,b)!=(2,0))
                checks['polynomial_tail_certificates']+=1
    return {'schema_version':1,'exact_arithmetic':'fractions.Fraction',
            'checks':checks,'digest_sha256':digest.hexdigest(),
            'status':'all finite checks passed',
            'limitation':'Finite checks are not a substitute for the all-parameter polynomial and gap proofs.'}


if __name__=='__main__':
    result=verify()
    print(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False))

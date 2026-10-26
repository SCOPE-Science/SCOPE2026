"""Exact finite verification for biased random tournament cycle-count moments."""
from fractions import Fraction
from itertools import combinations
from math import comb

def moments(n, p):
    edges = list(combinations(range(n),2))
    edgeindex = {e:i for i,e in enumerate(edges)}
    tris = [(edgeindex[a,b],edgeindex[b,c],edgeindex[a,c])
            for a,b,c in combinations(range(n),3)]
    r=p*(1-p)
    total = Fraction(0)
    sq = Fraction(0)
    vals = {}
    for mask in range(1<<len(edges)):
        k=mask.bit_count()
        weight=p**k*(1-p)**(len(edges)-k)
        z=sum(bool((mask>>ab)&1) and bool((mask>>bc)&1) and not bool((mask>>ac)&1) or
              not bool((mask>>ab)&1) and not bool((mask>>bc)&1) and bool((mask>>ac)&1)
              for ab,bc,ac in tris)
        vals[z]=vals.get(z,Fraction())+weight
        total += weight*z
        sq += weight*z*z
        # exact Hoeffding decomposition of the centered statistic
        ys = [Fraction((mask>>i)&1)-p for i in range(len(edges))]
        l=(1-2*p)*sum((c-a-1)*ys[edgeindex[a,c]] for a,c in edges)
        q=sum(ys[ab]*ys[bc]-ys[ab]*ys[ac]-ys[bc]*ys[ac] for ab,bc,ac in tris)
        assert Fraction(z)-comb(n,3)*r==l+q, (n,mask)
    exact_var=sq-total*total
    pred_mean=comb(n,3)*r
    pred_var=3*comb(n,3)*r*r + r*(1-2*p)**2 * Fraction(n*(n-1)**2*(n-2),12)
    assert total==pred_mean, (n,p,total,pred_mean)
    assert exact_var==pred_var, (n,p,exact_var,pred_var)
    assert sum(vals.values())==1
    return exact_var, pred_var

def main():
    cases = 0
    for n in range(3,7):
        for p in (Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(2,3)):
            a,b=moments(n,p)
            print(n,str(p),str(a))
            cases += 1
    print('PASS',cases,'complete finite weighted state-space cases')
if __name__=='__main__': main()

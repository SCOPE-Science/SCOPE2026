"""Finite sanity checks for total Roman {2} domination on rook graphs.

These checks do not replace the proof for arbitrary sizes.
"""
from itertools import product, combinations
from math import factorial, comb
from fractions import Fraction


def expected(p, q):
    if p > q:
        p, q = q, p
    return min(2*p, p+q-min(p, (p+q)//3))


def valid(labels, p, q):
    for i in range(p):
        for j in range(q):
            k=i*q+j
            neigh = [i*q+l for l in range(q) if l!=j]
            neigh += [r*q+j for r in range(p) if r!=i]
            if labels[k]==0:
                if sum(labels[x] for x in neigh)<2:
                    return False
            elif not any(labels[x]>0 for x in neigh):
                return False
    return True


def brute(p,q):
    best = p*q+1
    cnt=0
    for lab in product((0,1,2), repeat=p*q):
        w=sum(lab)
        if w>best:
            continue
        if valid(lab,p,q):
            if w<best:
                best=w;cnt=0
            cnt+=1
    return best,cnt


def forest_count(n):
    """Count minimum forests by exponential-formula dynamic programming."""
    c=(2*n)//3
    # dp[(rows,cols,comps)] weighted by exp-generating coefficients
    dp={(0,0,0):Fraction(1)}
    for s in range(1,c+1):
        nd={}
        for (r,t,num),v in dp.items():
            for a in range(1,n-r+1):
                for b in range(1,n-t+1):
                    if a+b<3:continue
                    # bipartite labeled Cayley tree formula
                    trees=a**(b-1)*b**(a-1)
                    w=v*Fraction(trees, factorial(a)*factorial(b)*s)
                    key=(r+a,t+b,num+1)
                    nd[key]=nd.get(key,Fraction())+w
        dp=nd
    count=dp.get((n,n,c),Fraction())*factorial(n)**2
    assert count.denominator==1
    return count.numerator




def closed_census(n):
    """Closed census of minimum total Roman {2} functions on K_n square K_n."""
    if n < 2:
        raise ValueError("n must be at least 2")
    k, residue = divmod(n, 3)
    base = Fraction(factorial(n)**2, 4**k * factorial(k)**2)
    if residue == 0:
        value = base
    elif residue == 1:
        value = base * Fraction(k*(64*k*k + 107*k + 49), 18*(k+1))
    else:
        value = base * Fraction(4*k+3, 3*(k+1))
    assert value.denominator == 1
    return value.numerator

def binary_count(n, sz):
    total=0
    for support in combinations(range(n*n),sz):
        labels=[0]*(n*n)
        for k in support:labels[k]=1
        total+=valid(labels,n,n)
    return total

if __name__=='__main__':
    for p,q in ((2,2),(2,3),(2,4),(3,3),(3,4)):
        best,n=brute(p,q)
        print('brute',p,q,'weight',best,'count',n,'formula',expected(p,q))
        assert best==expected(p,q)
    for n in range(2,11):
        v=forest_count(n)
        print('forest',n,expected(n,n),v)
        if n<=4:
            w=binary_count(n,expected(n,n))
            print('binary direct',n,w)
            assert w==v
        assert v == closed_census(n), (n, v, closed_census(n))
    print('ALL_TESTS_PASSED')

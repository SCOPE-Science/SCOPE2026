"""Exact finite checks of a uniform transitive-delegation participation theorem.
Python standard library only; run python3 delegation_verify.py.
"""
from fractions import Fraction
from itertools import product
from math import prod


def formulas(n, q):
    # q=probability of direct vote; all other choices uniform among n-1 peers.
    assert n >= 2 and Fraction(0) <= q <= Fraction(1)
    a = []
    falling = Fraction(1)
    for k in range(n):
        if k:
            falling *= Fraction(n-k, n-1)
        a.append(q * (1-q)**k * falling)
    p = sum(a)
    p11 = Fraction(0)
    for k in range(n):
        s = k+1
        if s == n:
            f = Fraction(0)
        else:
            # h_l: conditional success having exposed l distinct non-gurus
            # outside a previously established successful path of size s.
            h = Fraction(0)
            for ell in range(n-s, 0, -1):
                h = Fraction(s, n-1) + Fraction(n-s-ell, n-1)*(q + (1-q)*h)
            f = q + (1-q)*h
        p11 += a[k] * (Fraction(k, n-1) + Fraction(n-k-1, n-1)*f)
    return p, p11


def enumeration(n, q):
    a, b = q.numerator, q.denominator
    opts = []
    for i in range(n):
        # (target -1 for direct voter, integral probability numerator)
        opts.append([(-1, a*(n-1))] + [(j,b-a) for j in range(n) if j!=i])
    denominator = (b*(n-1))**n
    sum_z = 0; sum_z2 = 0; count = 0; prob_sum = 0
    for choices in product(*opts):
        parent = [x[0] for x in choices]
        weight = prod(x[1] for x in choices)
        status = [-1]*n  # -1 unknown, 0 cyclical, 1 represented
        for i in range(n):
            if status[i]!=-1: continue
            path=[]; visited=set(); j=i
            while True:
                if parent[j]==-1:
                    result=1; break
                if status[j]!=-1:
                    result=status[j]; break
                if j in visited:
                    result=0; break
                visited.add(j);path.append(j);j=parent[j]
            for v in path:status[v]=result
            if parent[i]==-1:status[i]=1
        z=sum(parent[i]==-1 or status[i]==1 for i in range(n))
        sum_z+=weight*z;sum_z2+=weight*z*(z-1)
        prob_sum+=weight;count+=1
    assert prob_sum==denominator
    return Fraction(sum_z, n*denominator), Fraction(sum_z2,n*(n-1)*denominator),count


def main():
    checks=0;total=0
    for n in range(2,7):
        for q in [Fraction(1,3),Fraction(2,5)]:
            p,p11=formulas(n,q)
            got_p,got_p11,count=enumeration(n,q)
            assert p==got_p,(n,q,p,got_p)
            assert p11==got_p11,(n,q,p11,got_p11)
            print('PASS',n,str(q),'assignments',count,'mean',p,'joint',p11)
            checks+=1;total+=count
    print('EXACT_CHECKS_OK',checks,'ASSIGNMENTS',total)
if __name__=='__main__':main()

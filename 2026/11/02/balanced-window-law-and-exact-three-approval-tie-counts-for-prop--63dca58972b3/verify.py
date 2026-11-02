"""Exact exhaustive checks for circular-consecutive-approval Thiele optimal committees.
Standalone, standard-library Python 3.9+.
"""
from math import comb, floor, lcm


def count_closed_form(n, k):
    if not (3 <= n and 0 <= k <= n):
        raise ValueError('requires n>=3 and 0<=k<=n')
    if k in (0, n):
        return 1
    t = min(k, n-k)
    if 3*t <= n:
        numerator = n * comb(n-2*t, t)
        assert numerator % (n-2*t) == 0
        return numerator // (n-2*t)
    total = 0
    for a in range(1, min(k, n-k)+1):
        if a <= k <= 2*a and a <= n-k <= 2*a:
            numerator = n * comb(a, k-a) * comb(a, n-k-a)
            assert numerator % a == 0
            total += numerator // a
    return total


def verify_small():
    tested = 0
    for n in range(3, 13):
        scale = lcm(*range(1, n+1))
        H = [0]
        for j in range(1, n+1):
            H.append(H[-1] + scale//j)
        fullmask=(1 << n)-1
        for d in range(1, n+1):
            masks=[]
            for i in range(n):
                masks.append(sum(1 << ((i+j) % n) for j in range(d)))
            best = [None]*(n+1)
            count=[0]*(n+1)
            for s in range(1<<n):
                k=s.bit_count()
                vals=[(s&mask).bit_count() for mask in masks]
                score=sum(H[v] for v in vals)
                q,r=divmod(d*k,n)
                expected=(n-r)*H[q]+r*H[q+1] if r else n*H[q]
                assert score<=expected,(n,d,k,s,score,expected)
                balanced=all(q<=v<=q+1 for v in vals)
                assert (score==expected)==balanced,(n,d,k,s,score,expected)
                if best[k] is None or score > best[k]:
                    best[k]=score
                    count[k]=1
                elif score == best[k]:
                    count[k]+=1
                tested+=1
            for k in range(n+1):
                q,r=divmod(d*k,n)
                expected=(n-r)*H[q]+r*H[q+1] if r else n*H[q]
                assert best[k]==expected,(n,d,k,best[k],expected)
                if d==3:
                    assert count[k]==count_closed_form(n,k),(n,k,count[k],count_closed_form(n,k))
            print('PASS_n',n,'widths',n,'optimal_counts_for_d3', [count_closed_form(n,k) for k in range(n+1)])
    return tested


def verify_range():
    tested=0
    for n in range(13,19):
        d=3
        masks=[sum(1 << ((i+j)%n) for j in range(3)) for i in range(n)]
        win_counts=[0]*(n+1)
        for s in range(1<<n):
            k=s.bit_count()
            vals=[(s&m).bit_count() for m in masks]
            q,r=divmod(d*k,n)
            score=sum((0,6,9,11)[v] for v in vals)
            bound=(n-r)*(0,6,9,11)[q]+r*(0,6,9,11)[q+1] if r else n*(0,6,9,11)[q]
            assert score<=bound
            if score==bound:
                assert all(q<=x<=q+1 for x in vals)
                win_counts[k]+=1
            tested+=1
        for k in range(n+1):
            assert win_counts[k]==count_closed_form(n,k),(n,k,win_counts[k],count_closed_form(n,k))
        print('PASS_large',n,'mid_count',win_counts[n//2])
    return tested

if __name__=='__main__':
    a=verify_small();b=verify_range()
    print('VERIFY_OK enumerated_binary_committees',a+b,'domain_first',3,'domain_last',18)

"""Exact independent finite checks of one-shot temporal-contact outbreaks.

Uses event-by-event infection simulation, not the temporal-pair proof.
Run with Python 3 (standard library only).
"""
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def exact_mean_by_events(edge_times, p):
    n = len(edge_times) + 1
    order = sorted(range(n - 1), key=lambda j: edge_times[j])
    k = n - 1
    total = Fraction(0)
    for root in range(n):
        for succeeds in product((False, True), repeat=k):
            w = p ** sum(succeeds) * (1-p) ** (k-sum(succeeds))
            infected = [False] * n
            infected[root] = True
            for e in order:
                if succeeds[e] and infected[e] != infected[e+1]:
                    infected[e] = infected[e+1] = True
            total += w * sum(infected)
    return total/n


def predicted_mean(edge_times, p):
    n = len(edge_times)+1
    ans = 1+Fraction(2*(n-1),n)*p
    for d in range(2,n):
        for i in range(n-d):
            segment = edge_times[i:i+d]
            if all(segment[j] < segment[j+1] for j in range(d-1)) or all(segment[j] > segment[j+1] for j in range(d-1)):
                ans += p**d/n
    return ans


def extrema(n,p):
    mn = 1 + Fraction(2*(n-1),n)*p
    if n >= 3:
        mn += Fraction(n-2,n)*p*p
    mx = 1 + Fraction(2*(n-1),n)*p + sum((Fraction(n-d,n)*p**d for d in range(2,n)),Fraction(0))
    av = 1 + Fraction(2,n)*sum((Fraction(n-d,factorial(d))*p**d for d in range(1,n)),Fraction(0))
    return mn,mx,av


def alternating(edge_times):
    return all((edge_times[i] < edge_times[i+1]) != (edge_times[i+1] < edge_times[i+2]) for i in range(len(edge_times)-2))


def monotone(edge_times):
    return all(edge_times[i] < edge_times[i+1] for i in range(len(edge_times)-1)) or all(edge_times[i]>edge_times[i+1] for i in range(len(edge_times)-1))


def main():
    checks=0
    for n in range(2,8):
        for p in (Fraction(1,2),Fraction(2,3),Fraction(1)):
            mn,mx,av = extrema(n,p)
            total=Fraction(0)
            count=0
            for times in permutations(range(n-1)):
                actual=exact_mean_by_events(times,p)
                predicted=predicted_mean(times,p)
                assert actual==predicted,(n,p,times,actual,predicted)
                checks+=1
                assert mn<=actual<=mx,(n,p,times,actual,mn,mx)
                checks+=1
                if n>=4:
                    assert (actual==mn)==alternating(times),(n,p,times,'min')
                    assert (actual==mx)==monotone(times),(n,p,times,'max')
                    checks+=2
                total+=actual
                count+=1
            assert total/count==av,(n,p,total/count,av)
            checks+=1
    # The direct-index-case mean is only degree-weighted, regardless of event order.
    for n in range(2,8):
        for p in (Fraction(1,2),Fraction(2,3),Fraction(1)):
            targets = sum(len([x for x in (v-1,v+1) if 0 <= x < n]) for v in range(n))
            assert Fraction(targets,n)*p == Fraction(2*(n-1),n)*p
            checks+=1
    print(f'ALL_CHECKS_PASSED assertions={checks}; exact event simulation through 7 vertices; probabilities=1/2,2/3,1')

if __name__=='__main__':
    main()

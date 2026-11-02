"""Independent sharpness witness check for Schrijver graph 2-extension."""
from itertools import combinations


def stable(subset, n):
    return all((i+1)%n not in subset for i in subset)


def max_independent_subset(n, allowed):
    best = 0
    for k in range(len(allowed)+1):
        for subset in combinations(allowed, k):
            if stable(subset,n):
                best = max(best,k)
    return best


def run():
    tested=0
    for r in range(2,8):
        for n in range(2*r+1,4*r):
            a=set(range(0,2*r,2))
            b=set(range(1,2*r,2))
            assert len(a)==len(b)==r and a.isdisjoint(b)
            assert stable(a,n) and stable(b,n)
            remaining=sorted(set(range(n)) - a - b)
            alpha=max_independent_subset(n,remaining)
            assert alpha == (n-2*r+1)//2, (r,n,alpha)
            assert alpha < r if n <= 4*r-2 else alpha >= r
            tested+=1
    print(f'PASS: {tested} sharp non-triangle edge witnesses, r=2..7, all 2r+1<=n<4r')

if __name__=='__main__':
    run()

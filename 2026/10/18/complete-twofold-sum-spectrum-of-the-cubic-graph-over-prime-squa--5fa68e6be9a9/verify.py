"""Exact twofold convolution census for prime-square cubic graphs.
Run with Python 3; integer arithmetic only.
"""
from collections import Counter

def predicted(p):
    n=p*p
    nonzero={
        2:(n-p)*(n-p)//2,
        p:n-1,
        2*p:(p-1)*(p-1)//2,
        n:1,
    }
    return {0:n*n-sum(nonzero.values()),**nonzero}

def empirical(p):
    n=p*p
    counts=Counter()
    for a in range(n):
        for b in range(n):
            x=(a+b)%n
            y=(pow(a,3,n)+pow(b,3,n))%n
            counts[(x,y)]+=1
    return Counter({k:v for k,v in Counter(counts.values()).items()}) | Counter({0:n*n-len(counts)})

def run():
    for p in (5,7,11,13,17):
        actual=empirical(p)
        formula=Counter(predicted(p))
        assert actual==formula, (p,actual,formula)
        n=p*p
        assert sum(t*v for t,v in actual.items())==n*n
        energy=sum(t*t*v for t,v in actual.items())
        expected=6*p**4-8*p**3+3*p**2
        assert energy==expected, (p,energy,expected)
        print(f'p={p}: fibers={dict(sorted(actual.items()))}; energy={energy}: OK')
    print('ALL_VERIFY_OK')

if __name__=='__main__':run()

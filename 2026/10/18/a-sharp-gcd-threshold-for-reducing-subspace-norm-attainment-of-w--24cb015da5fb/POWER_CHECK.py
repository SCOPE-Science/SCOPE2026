from math import gcd, lcm

def implication_arithmetic(m,d):
    g=gcd(m,d)
    return m>=2*d-g

def implication_combinatorial(m,d):
    if m<d:
        return False
    L=m-d+1
    for s in range(d):
        forbidden={(s-j)%d for j in range(L)}
        if all(any(a not in forbidden for a in range(d) if a%gcd(m,d)==r%gcd(m,d)) for r in range(m)):
            return False
    return True

def counterexample_blocks(m,d):
    assert not implication_arithmetic(m,d)
    if m<d:
        starts=[r+m*lcm(m,d)*20 for r in range(m)]
    else:
        g=gcd(m,d);L=m-d+1;s=d-1
        F={(s-j)%d for j in range(L)}
        starts=[]
        for r in range(m):
            possibles=[a for a in range(d) if a%g==r%g and a not in F]
            assert possibles
            a=possibles[0]
            z=next(k for k in range(lcm(m,d)) if k%m==r and k%d==a)
            starts.append(z+r*lcm(m,d)*20)
    intervals=sorted((x,x+m-1) for x in starts)
    assert all(intervals[i+1][0]>intervals[i][1]+d for i in range(m-1)) or m<d
    support={k for x in starts for k in range(x,x+m)}
    def covers(n):
        matches=set()
        for k in range(max(support)+1):
            if all(k+j in support for j in range(n)):
                matches.add(k%n)
        return len(matches)==n
    assert covers(m) and not covers(d),(m,d,starts)
    return starts

checks=0
for m in range(1,31):
    for d in range(1,31):
        if m>=d:
            assert implication_arithmetic(m,d)==implication_combinatorial(m,d),(m,d)
        if not implication_arithmetic(m,d):
            # avoid exponential cost in huge support set; test first 12
            if m<=12 and d<=12:counterexample_blocks(m,d)
        checks+=1
print('PASS',checks,'pairs and all finite CRT witnesses with m,d<=12')
print('m=4,d=3 starts',counterexample_blocks(4,3))

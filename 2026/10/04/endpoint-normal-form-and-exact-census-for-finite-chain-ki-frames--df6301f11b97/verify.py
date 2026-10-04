#!/usr/bin/env python3

def downward(R,n):
    for x in range(n):
        for xp in range(x,n):
            for yp in range(n):
                if (xp,yp) in R:
                    if not any((x,y) in R and y <= yp for y in range(n)):
                        return False
    return True

def forward(R,n):
    for x in range(n):
        for xp in range(x,n):
            for y in range(n):
                if (x,y) in R:
                    if not any((xp,yp) in R and y <= yp for yp in range(n)):
                        return False
    return True

def endpoints(R,n):
    mins=[]; maxs=[]
    for i in range(n):
        row=[j for j in range(n) if (i,j) in R]
        mins.append(min(row) if row else n)
        maxs.append(max(row) if row else -1)
    return mins,maxs

def nondecreasing(xs):
    return all(xs[i] <= xs[i+1] for i in range(len(xs)-1))

direct=[]
for n in range(1,5):
    count=0
    for mask in range(1 << (n*n)):
        R={(i,j) for i in range(n) for j in range(n)
           if (mask >> (i*n+j)) & 1}
        d=downward(R,n)
        f=forward(R,n)
        mins,maxs=endpoints(R,n)
        assert d == nondecreasing(mins)
        assert f == nondecreasing(maxs)
        both=d and f
        if both:
            count += 1
            row_nonempty=[any((i,j) in R for j in range(n)) for i in range(n)]
            assert (not any(row_nonempty)) or all(row_nonempty)
            if all(row_nonempty):
                assert all(0 <= mins[i] <= maxs[i] < n for i in range(n))
    direct.append(count)
assert direct == [2,7,80,2855]

def formula_count(n):
    states=[(m,M) for m in range(n) for M in range(m,n)]
    weight={(m,M):1 << max(M-m-1,0) for m,M in states}
    dp={s:weight[s] for s in states}
    for _ in range(1,n):
        nd={}
        for t in states:
            nd[t]=weight[t]*sum(v for s,v in dp.items()
                                if s[0] <= t[0] and s[1] <= t[1])
        dp=nd
    return 1 + sum(dp.values())

formula=[formula_count(n) for n in range(1,11)]
assert formula[:6] == [2,7,80,2855,374660,195589841]
assert formula[:4] == direct
print('DIRECT_COUNTS', direct)
print('FORMULA_COUNTS', formula)
print('VERIFY_OK')

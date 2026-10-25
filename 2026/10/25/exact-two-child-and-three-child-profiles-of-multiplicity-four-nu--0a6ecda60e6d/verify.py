"""Reproducible finite checks for exact offspring-degree enumeration of multiplicity-four numerical semigroups."""
from collections import Counter, defaultdict

LIMIT = 90

def kunz(a, b, c):
    return all((b <= 2*a, c <= a+b, a <= b+c+1, b <= 2*c+1))

def degree_direct(a, b, c):
    W = [0, 4*a+1, 4*b+2, 4*c+3]
    F = max(W)-4
    def isin(n):
        return n >= 0 and n >= W[n % 4]
    # The unique minimal generators are the positive elements which do not split
    # as a sum of two positive elements of the semigroup.
    degree = 0
    for value in [4, W[1], W[2], W[3]]:
        minimal = not any(isin(i) and isin(value-i) for i in range(1, value))
        if minimal and value > F:
            degree += 1
    return degree

def pair_sets(N):
    out = [defaultdict(set) for _ in range(3)]
    for t in range(1, N + 1):
        for c in range((t+1)//2, t+1):
            for abc in [(t,t,c),(t+1,t,c)]:
                if sum(abc) <= N:
                    out[0][sum(abc)].add(abc)
        for b in range(1,t+1):
            abc=(t,b,t)
            if sum(abc)<=N:out[1][sum(abc)].add(abc)
        for b in range(1,t+2):
            abc=(t+1,b,t)
            if sum(abc)<=N:out[1][sum(abc)].add(abc)
        for a in range(t//2+1,t+2):
            abc=(a,t,t)
            if sum(abc)<=N:out[2][sum(abc)].add(abc)
        for a in range((t+3)//2,t+2):
            abc=(a,t+1,t)
            if sum(abc)<=N:out[2][sum(abc)].add(abc)
    return out

def e2_formula(g):
    return sum(max(0,1+(g-j)//5) for j in (5,6,8) if g >= j)

pairs=pair_sets(LIMIT)
counts=defaultdict(Counter)
for g in range(3,LIMIT+1):
    for a in range(1,g-1):
        for b in range(1,g-a):
            c=g-a-b
            if not kunz(a,b,c):
                continue
            triple=(a,b,c)
            d=degree_direct(a,b,c)
            counts[g][d]+=1
            pair_count=sum(triple in p[g] for p in pairs)
            apdeg=d-(1 if g==3 else 0)
            assert pair_count == (0 if apdeg<=1 else 1 if apdeg==2 else 3), (g,triple,d,pair_count)
    assert counts[g][2]==e2_formula(g), (g,counts[g],e2_formula(g))
    assert counts[g][3]==(1 if g>=4 else 0)
    assert counts[g][4]==(1 if g==3 else 0)
    assert sum(counts[g][d] for d in range(5,12))==0
print('VERIFY_OK', 'genus_3_through',LIMIT,'degree2_g26',counts[26][2], 'degree3_g26',counts[26][3])
print('DEGREE2_G3_G25', [(g,counts[g][2]) for g in range(3,26)])

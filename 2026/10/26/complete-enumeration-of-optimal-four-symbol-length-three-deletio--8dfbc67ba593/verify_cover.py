"""Finite exhaustive census of minimal quaternary three-letter single-deletion covers.
Run with Python 3.10+; uses only the standard library.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import comb

Q = 4
FULL = (1 << (Q * Q)) - 1

def digits(w):
    return w // 16, (w // 4) % 4, w % 4

def shadow(w):
    a, b, c = digits(w)
    return (1 << (4*a + b)) | (1 << (4*a + c)) | (1 << (4*b + c))

M = [shadow(w) for w in range(64)]

# Independent exact counting method: subset-sum dynamic programming
# in the Boolean-union semiring, selecting each possible triple at most once.
DP = [defaultdict(int) for _ in range(7)]
DP[0][0] = 1
for i, ball in enumerate(M):
    for k in range(min(6, i+1), 0, -1):
        for covered, multiplicity in tuple(DP[k-1].items()):
            DP[k][covered | ball] += multiplicity
assert sum(DP[6].values()) == comb(64,6)
assert DP[6][FULL] == 644

# Independent direct exhaustive enumeration with certified upper-capacity
# pruning: each future word can add at most three distinct received pairs.
coverings = []
for a in range(59):
    ma=M[a]
    for b in range(a+1,60):
        mb=ma | M[b]
        for c in range(b+1,61):
            mc=mb | M[c]
            if mc.bit_count() < 7: continue
            for d in range(c+1,62):
                md=mc | M[d]
                if md.bit_count() < 10: continue
                for e in range(d+1,63):
                    me=md | M[e]
                    if me.bit_count() < 13: continue
                    for f in range(e+1,64):
                        if me | M[f] == FULL:
                            coverings.append((a,b,c,d,e,f))
assert len(coverings) == 644

# Reversal and global alphabet permutations generate a 48-element group.
perms = tuple(permutations(range(4)))
def action(code, p, rev):
    out=[]
    for w in code:
        letters=digits(w)
        if rev: letters=letters[::-1]
        out.append(16*p[letters[0]]+4*p[letters[1]]+p[letters[2]])
    return tuple(sorted(out))

def whole_orbit(code):
    return {action(code,p,rev) for p in perms for rev in (0,1)}

unseen=set(coverings)
orbit_sizes=Counter()
rep_rows=[]
while unseen:
    rep=min(unseen)
    orbit=whole_orbit(rep)
    assert orbit <= unseen
    orbit_sizes[len(orbit)] += 1
    unseen -= orbit
    rep_rows.append((rep,len(orbit)))
assert len(rep_rows) == 21
assert orbit_sizes == Counter({8:1, 12:3, 24:9, 48:8})
assert sum(k*v for k,v in orbit_sizes.items()) == 644

# The overlap statistic includes every excess incidence beyond the first.
profile=Counter()
perfect=0
for code in coverings:
    incidence=[0]*16
    sizes=[]
    for w in code:
        sh=M[w]; sizes.append(sh.bit_count())
        for v in range(16):
            incidence[v]+=(sh>>v)&1
    assert min(incidence)>=1
    overlap=sum(n-1 for n in incidence)
    if overlap==0: perfect+=1
    profile[(overlap,tuple(sorted(Counter(sizes).items())))] += 1
assert perfect == 120
assert profile == Counter({
    (0, ((1,1),(3,5))):48,
    (0, ((2,2),(3,4))):72,
    (1, ((2,1),(3,5))):336,
    (2, ((3,6),)):188,
})

print('TOTAL_6_WORD_SUBSETS=',sum(DP[6].values()))
print('OPTIMAL_COVERS=',len(coverings))
print('PERFECT_DECODABLE_COVERS=',perfect)
print('OPTIMAL_BUT_NOT_DECODABLE=',len(coverings)-perfect)
print('ORBIT_NUMBER=',len(rep_rows))
print('ORBIT_SIZES=',sorted(orbit_sizes.items()))
print('OVERLAP_AND_BALL_SIZE_PROFILE=',sorted(profile.items()))
print('ORBIT_REPRESENTATIVES=',rep_rows)
print('VERIFY_OK')

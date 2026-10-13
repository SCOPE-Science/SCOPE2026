import math
from collections import Counter

# Structural factorization.
def S(t, lam, theta):
    return math.exp(-(lam/theta)*(math.exp(theta*t)-1.0))

def subdensity(t, j, lam1, lam2, theta):
    lam = lam1 if j == 1 else lam2
    return lam*math.exp(theta*t)*S(t,lam1,theta)*S(t,lam2,theta)

def total_density(t, lam1, lam2, theta):
    return (lam1+lam2)*math.exp(theta*t)*S(t,lam1,theta)*S(t,lam2,theta)

for lam1,lam2,theta in [(0.4,1.2,0.7),(2.1,0.3,1.4),(0.8,1.7,0.2)]:
    for t in (0.01,0.1,0.5,1.5):
        f = total_density(t,lam1,lam2,theta)
        assert abs(subdensity(t,1,lam1,lam2,theta)/f-lam1/(lam1+lam2)) < 2e-15
        assert abs(subdensity(t,2,lam1,lam2,theta)/f-lam2/(lam1+lam2)) < 2e-15

# The 45 failures printed in the 2026 source table.
E = [
    0.002,0.003,0.005,0.008,0.021,0.028,0.031,0.064,0.069,0.076,
    0.104,0.119,0.144,0.160,0.221,0.226,0.236,0.282,0.303
]
D = [
    0.168,0.191,0.203,0.211,0.261,0.264,0.278,0.284,0.286,0.298,
    0.314,0.317,0.318,0.320,0.327,0.328,0.328,0.348,0.350,0.360,
    0.369,0.377,0.387,0.392,0.412,0.446
]
assert len(E)==19 and len(D)==26

vals=E+D
indexed=sorted(enumerate(vals),key=lambda z:z[1])
ranks=[None]*len(vals)
i=0
while i<len(vals):
    j=i+1
    while j<len(vals) and indexed[j][1]==indexed[i][1]:
        j+=1
    # Ordinary ranks i+1,...,j have doubled midrank (i+1)+j.
    doubled=(i+1)+j
    for q in range(i,j):
        ranks[indexed[q][0]]=doubled
    i=j

k=len(E)
n=len(vals)
obs2=sum(ranks[:k])
mean2=k*(n+1)
assert obs2==438
assert mean2==874
assert obs2/2==219
U=obs2/2-k*(k+1)/2
assert U==29

# Exact subset-sum distribution of the doubled rank sum for a uniformly chosen
# k-subset of the observed failure positions.
dp=[Counter() for _ in range(k+1)]
dp[0][0]=1
used=0
for r in ranks:
    for j in range(min(k,used+1),0,-1):
        for s,c in list(dp[j-1].items()):
            dp[j][s+r]+=c
    used+=1

denom=math.comb(n,k)
assert sum(dp[k].values())==denom
dev=abs(obs2-mean2)
extreme=sum(c for s,c in dp[k].items() if abs(s-mean2)>=dev)
p=extreme/denom

assert denom==2438362177020
assert extreme==44812
assert abs(p-1.837790973889128e-8)<1e-22

print("VERIFY_OK")
print("rank_sum_E",obs2/2)
print("mann_whitney_U",U)
print("conditional_assignments",denom)
print("two_sided_extreme_assignments",extreme)
print("exact_two_sided_p",format(p,".16e"))

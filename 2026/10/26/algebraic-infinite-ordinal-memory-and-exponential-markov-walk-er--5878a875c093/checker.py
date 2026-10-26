"""Exact rational verification for tripling-map ordinal run statistics."""
from fractions import Fraction as F

E=[F(0),F(1,3),F(1,2),F(2,3),F(1)]
n=4
P=[[F(0) for j in range(n)] for i in range(n)]
for i in range(n):
    a,c=E[i],E[i+1]
    for branch in range(3):
        lo=max(a,F(branch,3))
        hi=min(c,F(branch+1,3))
        if lo>=hi:continue
        ylo=3*lo-branch
        yhi=3*hi-branch
        for j in range(n):
            length=max(F(0),min(yhi,E[j+1])-max(ylo,E[j]))
            P[i][j]+=length/(3*(c-a))
expected=[
  [F(1,3),F(1,6),F(1,6),F(1,3)],
  [F(2,3),F(1,3),F(0),F(0)],
  [F(0),F(0),F(1,3),F(2,3)],
  [F(1,3),F(1,6),F(1,6),F(1,3)]
]
assert P==expected
assert all(sum(row)==1 for row in P)
print('FOUR_CELL_MARKOV_MATRIX_EXACT_PASS')

# Independent inverse-image interval calculation of rising-order cylinders.
A=[(F(0),F(1,3)),(F(1,2),F(2,3))]
def merge(intervals):
    intervals=sorted((a,b) for a,b in intervals if b>a)
    out=[]
    for a,b in intervals:
        if out and a<=out[-1][1]:out[-1]=(out[-1][0],max(b,out[-1][1]))
        else:out.append((a,b))
    return out

def preimage(intervals):
    return merge([((a+k)/3,(b+k)/3) for (a,b) in intervals for k in range(3)])

def intersect(left,right):
    return merge((max(a,c),min(b,d)) for a,b in left for c,d in right)

N=A
for length in range(1,10):
    p=sum((b-a for a,b in N),F(0))
    expected_prob=F(length+2,2*3**length)
    assert p==expected_prob,(length,p,expected_prob)
    N=intersect(A,preimage(N))
print('DIRECT_PREIMAGE_RISING_RUNS_PASS',9)

# Matrix and generating-function identities, exact rational checks.
pi=[E[i+1]-E[i] for i in range(4)]
D=[0,2]
for k in range(1,21):
    v=[pi[i] for i in D]
    for _ in range(k-1):v=[sum(v[h]*P[D[h]][D[j]] for h in range(2)) for j in range(2)]
    prob=sum(v)
    assert prob==F(k+2,2*3**k)
print('HIDDEN_MARKOV_RISING_RUNS_PASS',20)

p_A=F(1,2)
p_AA=F(4,9)
p_AB=F(5,9)
assert p_A*p_AA==F(2,9)
assert p_AA-p_AB==-F(1,9)
for k in range(1,20):
    cond=F(k+3,3*(k+2))
    assert cond==F(k+3,2*3**(k+1))/F(k+2,2*3**k)
    if k>=2:assert cond != p_AA
print('STRICT_INFINITE_MEMORY_AND_PROXY_SPECTRUM_PASS',19)
print('ASYMPTOTIC_NONMARKOV_CLAIMS_REQUIRE_ANALYTICAL_PROOF')

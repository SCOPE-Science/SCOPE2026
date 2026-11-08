"""Independent finite checks for a classification of common subsequences.
Run: python3 verify.py  (Python standard library only).
Finite tests complement, but do not replace, the proof in RESULT.md.
"""
from collections import Counter
from math import comb

def subsequences(text):
    words={''}
    for c in text:
        words |= {w+c for w in tuple(words)}
    return words

def maximal_common(x,y):
    common=subsequences(x)&subsequences(y)
    return {w for w in common if not any(w[:i]+c+w[i:] in common
          for i in range(len(w)+1) for c in '012')}

def descents(w, order):
    rank={c:i for i,c in enumerate(order)}
    return sum(rank[u]>=rank[v] for u,v in zip(w,w[1:]))

def predicted_maximal(w,r,s):
    if r>2*s:return w=='021'*s
    if s>2*r:return w=='012'*r
    return (len(w)==r+s and w[0]=='0' and w[-1] in '12'
            and all(a!=b for a,b in zip(w,w[1:]))
            and descents(w,'012')==r-1 and descents(w,'021')==s-1)

def expected_count(r,s):
    if max(r,s)>2*min(r,s):return 1
    return comb(r+s,2*min(r,s)-max(r,s))

def lcs_dp(a,b):
    prev=[0]*(len(b)+1)
    for x in a:
        now=[0]*(len(b)+1)
        for j,y in enumerate(b,1):
            now[j]=prev[j-1]+1 if x==y else max(now[j-1],prev[j])
        prev=now
    return prev[-1]

full=0;words_checked=0
for r in range(1,6):
    for s in range(1,6):
        X='012'*r;Y='021'*s
        actual=maximal_common(X,Y)
        common=subsequences(X)&subsequences(Y)
        predicted={w for w in common if predicted_maximal(w,r,s)}
        assert actual==predicted,(r,s,actual-predicted,predicted-actual)
        assert len(actual)==expected_count(r,s),(r,s,len(actual),expected_count(r,s))
        assert set(map(len,actual))=={min(r+s,3*min(r,s))},(r,s)
        full+=1;words_checked+=len(common)

length=0
for r in range(1,31):
    for s in range(1,31):
        assert lcs_dp('012'*r,'021'*s)==min(r+s,3*min(r,s)),(r,s)
        length+=1

# Independent coefficient recurrence from the proposed transfer rational function.
# The 0-th indices here represent r,s starting at 1.
N=[[0]*41 for _ in range(41)]
N[1][1]=2;N[1][2]=1;N[2][1]=1
coef=0
for r in range(1,41):
    for s in range(1,41):
        if (r,s) not in {(1,1),(1,2),(2,1)}:
            N[r][s]=3*N[r-1][s-1]+(N[r-2][s-1] if r>=2 else 0)+(N[r-1][s-2] if s>=2 else 0)
        expected=(comb(r+s,2*r-s) if 0<=2*r-s<=r+s else 0)
        # This GF counts paths with BOTH descent capacities saturated.
        assert N[r][s]==expected,(r,s,N[r][s],expected)
        coef+=1
print(f'PASS: {full} complete maximal-subsequence sets; {words_checked} common words; '
      f'{length} independent LCS DP instances; {coef} transfer coefficients')

#!/usr/bin/env python3
"""Independent finite checks for cyclic tolerance-rough observation fibers."""
from collections import Counter

S=((0,0),(0,1),(1,0),(1,1))

def transition(symbol):
    M=[[0]*4 for _ in range(4)]
    for i,(a,b) in enumerate(S):
        for c in (0,1):
            y=('0' if a+b+c==0 else '1' if a+b+c==3 else '?')
            if y==symbol:
                M[i][S.index((b,c))]+=1
    return M

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def fiber_trace(word):
    M=[[int(i==j) for j in range(4)] for i in range(4)]
    for symbol in word:
        M=mul(M,TRANS[symbol])
    return sum(M[i][i] for i in range(4))

def observe(mask,n):
    digits=[(mask>>i)&1 for i in range(n)]
    lo=up=0
    for i in range(n):
        t=digits[(i-1)%n]+digits[i]+digits[(i+1)%n]
        if t==3:lo|=1<<i
        if t>0:up|=1<<i
    return lo,up

def to_word(pair,n):
    lo,up=pair
    return ''.join('1' if lo>>i&1 else '?' if up>>i&1 else '0' for i in range(n))

TRANS={s:transition(s) for s in ('0','1','?')}
A=TRANS['?']
P=[[int(i==j) for j in range(4)] for i in range(4)]
powers=[P]
for t in range(100):
    powers.append(mul(powers[-1],A))
F=[0,1]
for i in range(2,105):F.append(F[-1]+F[-2])

def correction(t):return (1,0,-1)[t%3]
def second(n):return (F[n-2]+correction(n-1))//2
def central(n):
    L=F[n-1]+F[n+1]
    return L+(2 if n%3==0 else -1)

for t in range(0,80):
    a,b=powers[t][0][0],powers[t][0][3]
    s=1 if t==0 else F[t-1]
    assert a+b==s and a-b==correction(t)
    assert powers[t][3][3]==a and powers[t][3][0]==b
    if t>=7:
        assert max(powers[t-1][0][0],powers[t-1][0][3])<powers[t][0][0]
for p in range(35):
    for q in range(35):
        fp=max(powers[p][0][0],powers[p][0][3])
        fq=max(powers[q][0][0],powers[q][0][3])
        fpq=max(powers[p+q][0][0],powers[p+q][0][3])
        assert fp*fq<=fpq
print('TRANSFER_IDENTITIES_AND_SUPERMULTIPLICATIVITY_OK')

states_total=0; obs_total=0
for n in range(3,17):
    cnt=Counter(observe(mask,n) for mask in range(1<<n))
    counts=sorted(cnt.values(),reverse=True)
    top=cnt[(0,(1<<n)-1)]
    assert top==central(n) and counts[0]==top and counts[1]<top
    if n>=7:
        assert counts[1]==second(n)
        runners={to_word(q,n) for q,v in cnt.items() if v==counts[1]}
        expected={'?'*i+s+'?'*(n-i-1) for s in '01' for i in range(n)}
        assert runners==expected
    if n<=11:
        for q,count in cnt.items():
            assert fiber_trace(to_word(q,n))==count
    states_total+=1<<n
    obs_total+=len(cnt)
    print('CASE',n,'central',top,'runnerup',counts[1],
          'runnerup_count',sum(v==counts[1] for v in cnt.values()),
          'observations',len(cnt),'PASS')
print('VERIFY_OK binary_inputs',states_total,'observations',obs_total,
      'all_fiber_traces_n_le_11=PASS sharp_runnerup_n_7_to_16=PASS')

#!/usr/bin/env python3
from collections import Counter
from decimal import Decimal, getcontext

nu = {
'S':['S','q1'],
'q1':['q2'],'q2':['q3'],'q3':['q4'],'q4':['q5'],'q5':['q7','q8'],
'q7':['q9','q10'],'q8':['q11'],'q9':['q5','q12'],'q10':['q13'],
'q11':['q14'],'q12':['q15'],'q13':['q16'],'q14':['q17'],'q15':['q18'],
'q16':['q19'],'q17':['q20'],'q18':['q22'],'q19':['q23'],'q20':['q24','q1'],
'q22':['q9'],'q23':['q25','q10'],'q24':['q26','q1'],'q25':['q20','q27'],
'q26':['q23','q8'],'q27':['q15']}
eta = {
'S':'10','q1':'1','q2':'0','q3':'1','q4':'10','q5':'01','q7':'11','q8':'0',
'q9':'10','q10':'0','q11':'1','q12':'1','q13':'1','q14':'0','q15':'1',
'q16':'0','q17':'01','q18':'0','q19':'11','q20':'10','q22':'11','q23':'01',
'q24':'00','q25':'01','q26':'11','q27':'1'}
letters = ['S'] + [f'q{i}' for i in range(1,28) if i not in (6,21)]
assert set(letters)==set(nu)==set(eta) and len(letters)==26
J = [a for a in letters if a!='S']

# Closure of adjacent letter pairs in iterates of S.
pairs=set()
for a in letters:
    im=nu[a]
    pairs.update(zip(im,im[1:]))
while True:
    nxt=set(pairs)
    for a,b in pairs:
        nxt.add((nu[a][-1],nu[b][0]))
    if nxt==pairs: break
    pairs=nxt
pairs=sorted(pairs)
assert len(pairs)==68

# Linear state: counts of 26 letters and 68 adjacent letter pairs.
def basis_state(letter=None,pair=None):
    lc=Counter(); pc=Counter()
    if letter is not None: lc[letter]=1
    if pair is not None: pc[pair]=1
    return lc,pc

def step(state):
    lc,pc=state
    nl=Counter(); np=Counter()
    for a,n in lc.items():
        im=nu[a]
        for b in im: nl[b]+=n
        for p in zip(im,im[1:]): np[p]+=n
    for (a,b),n in pc.items():
        p=(nu[a][-1],nu[b][0])
        assert p in pairs
        np[p]+=n
    return nl,np

def out_len(state):
    lc,_=state
    return sum(n*len(eta[a]) for a,n in lc.items())

def out_01(state):
    lc,pc=state
    q=0
    for a,n in lc.items():
        s=eta[a]
        q += n*sum(s[i:i+2]=='01' for i in range(len(s)-1))
    for (a,b),n in pc.items():
        q += n*(eta[a][-1]=='0' and eta[b][0]=='1')
    return int(q)

def out_ones(state):
    lc,_=state
    return sum(n*eta[a].count('1') for a,n in lc.items())

x=(Counter({'S':1}),Counter())
L=[]; Q=[]; O=[]
for m in range(105):
    L.append(out_len(x)); Q.append(out_01(x)); O.append(out_ones(x)); x=step(x)
assert L[:3]==[2,3,4]
assert O[:3]==[1,2,2]
assert Q[:6]==[0,1,1,2,2,3]
# State dimension is 94. By Cayley-Hamilton, 94 consecutive zero residuals
# certify each displayed scalar recurrence for all later iterates.
DIM=len(letters)+len(pairs)
assert DIM==94
assert all(L[m+3]-L[m+1]-L[m]==0 for m in range(DIM))
assert all(O[m+3]-O[m+1]-O[m]==0 for m in range(DIM))
assert all(Q[m+6]-Q[m+4]-Q[m+1]-Q[m]==0 for m in range(DIM))

# The 25-letter growing component is primitive; verify M^20 is strictly positive.
idx={a:i for i,a in enumerate(J)}
M=[[0]*len(J) for _ in J]
for a in J:
    j=idx[a]
    for b in nu[a]: M[idx[b]][j]+=1

def matmul(A,B):
    n=len(A); k=len(B); m=len(B[0]); C=[[0]*m for _ in range(n)]
    for i in range(n):
        for t,v in enumerate(A[i]):
            if v:
                Bt=B[t]
                for j,w in enumerate(Bt):
                    if w: C[i][j]+=v*w
    return C
P=[row[:] for row in M]
primitive_exp=None
for e in range(1,21):
    if all(v>0 for row in P for v in row):
        primitive_exp=e; break
    P=matmul(P,M)
assert primitive_exp==20

# Direct recurrence replay, independent of the morphism count engine.
def nested(N):
    a=[0]*(N+2); a[1]=1
    for n in range(2,N+2):
        a[n]=n-a[n-a[n-a[n-1]]]
    return a
N=200000
a=nested(N+1)
d=[a[n+1]-a[n] for n in range(N)]
assert set(d)<={0,1}
cnt=Counter(zip(d[:-1],d[1:]))

# High-precision root c of c^3-c^2+2c-1=0 by Newton iteration.
getcontext().prec=50
c=Decimal('0.57')
for _ in range(20):
    f=c*c*c-c*c+2*c-1
    fp=3*c*c-2*c+2
    c-=f/fp
q=(Decimal(3)-c-c*c)/Decimal(7)
p00=(Decimal(4)-Decimal(6)*c+c*c)/Decimal(7)
p11=(Decimal(8)*c+c*c-Decimal(3))/Decimal(7)
assert abs(sum(Decimal(cnt[k]) for k in [(0,0),(0,1),(1,0),(1,1)])/Decimal(N-1)-1) < Decimal('1e-40')
# Loose finite sanity check; infinite formulas are proved by recurrence + PF argument, not this bound.
for k,target in [((0,0),p00),((0,1),q),((1,0),q),((1,1),p11)]:
    empirical=Decimal(cnt[k])/Decimal(N-1)
    assert abs(empirical-target) < Decimal('0.00005'), (k,empirical,target)

print('VERIFY_OK state_dim=94 pair_states=68 primitive_exponent=20 '
      'L_init=2,3,4 Q_init=0,1,1,2,2,3 recurrence_windows=94 '
      'direct_N=200000 counts='+','.join(str(cnt[k]) for k in [(0,0),(0,1),(1,0),(1,1)])+
      ' c='+format(c,'.15f')+' q01='+format(q,'.15f'))

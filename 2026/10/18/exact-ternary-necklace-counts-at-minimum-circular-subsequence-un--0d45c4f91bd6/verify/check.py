from itertools import product
from math import gcd, factorial

def circular_good(w):
    n=len(w); k=n//3
    return any(all(len({w[(phase+3*j+a)%n] for a in range(3)})==3 for j in range(k)) for phase in range(3))

def as_subsequence(pat, host):
    i=0
    for a in host:
        if a==pat[i]:
            i+=1
            if i==len(pat):return True
    return False

def brute_good(w):
    k=len(w)//3
    for r in range(len(w)):
        v=w[r:]+w[:r]
        if all(as_subsequence(u,v) for u in product(range(3),repeat=k)):
            return True
    return False

def rotkey(w):
    return min(w[r:]+w[:r] for r in range(len(w)))
for k in range(1,5):
    n=3*k; count=0; phases=[0,0,0,0]; orbs=set(); primitive=0
    for w in product(range(3),repeat=n):
        p=sum(all(len({w[(a+3*j+t)%n] for t in range(3)})==3 for j in range(k)) for a in range(3))
        if p==0:
            if k<=3: assert not brute_good(w)
            continue
        if k<=3: assert brute_good(w)
        count+=1; phases[p]+=1; orbs.add(rotkey(w))
        if all(w!=w[t:]+w[:t] for t in range(1,n)): primitive+=1
    pred_count=3*6**k-9*2**k+6
    pred_phase=[0,3*6**k-18*2**k+18,9*2**k-18,6]
    pred_orbs=sum((6**gcd(k,j)-3*2**gcd(k,j)+2) for j in range(k))//k
    assert (count, phases, len(orbs))==(pred_count, pred_phase, pred_orbs), (k,count,phases,len(orbs),pred_count,pred_phase,pred_orbs)
    assert primitive%(3*k)==0
    print('k',k,'n',n,'labels',count,'phases',phases[1:],'necklaces',len(orbs),'primitive_necklaces',primitive//n,flush=True)
print('TERNARY_CIRCULAR_EXTREMAL_PASS')

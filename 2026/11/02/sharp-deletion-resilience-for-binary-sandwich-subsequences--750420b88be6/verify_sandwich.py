#!/usr/bin/env python3
"""Independent small-case tests for a binary subsequence-avoidance theorem."""
from itertools import product, combinations

def deletion_number_dp(word, b):
    # Longest subsequence that avoids 0 1^b 0 by the greedy match automaton.
    pattern='0'+'1'*b+'0'
    p=len(pattern)
    state=[-10**8]*p
    state[0]=0
    for ch in word:
        new=state.copy()
        for k in range(p):
            if state[k]<0:continue
            j=k+(ch==pattern[k])
            if j<p:
                new[j]=max(new[j],state[k]+1)
        state=new
    return len(word)-max(state)

def deletion_number_gaps(word,b):
    zeros=[i for i,v in enumerate(word) if v=='0']
    z=len(zeros)
    if z<2:
        return 0
    counts=[word[zeros[k]+1:zeros[k+1]].count('1') for k in range(z-1)]
    best=z-1
    for i in range(z):
        s=0
        for j in range(i+1,z):
            s+=counts[j-1]
            best=min(best,i+(z-1-j)+max(0,s-b+1))
    return best

def bound(b,n):
    if n<b+2:return 0
    if n<4*b-1:
        return 1+(n-b-2)//3
    return 1+(n-2*b-1)//2

def witness(b,r):
    s=min(r,b-1)
    return '0'*(s+1)+'1'*b+'01'*r+'0'

def main():
    num=0; lengths=0; witness_checks=0; direct_cases=0
    for b in range(1,6):
        for n in range(0,15):
            maximum=0
            for tup in product('01',repeat=n):
                w=''.join(tup)
                d=deletion_number_dp(w,b)
                assert d==deletion_number_gaps(w,b),(w,b,d,deletion_number_gaps(w,b))
                maximum=max(maximum,d)
                num+=1
            assert maximum==bound(b,n),(b,n,maximum,bound(b,n))
            lengths+=1
    for b in range(1,25):
        for r in range(0,40):
            w=witness(b,r)
            assert len(w)==b+2+2*r+min(r,b-1)
            assert deletion_number_gaps(w,b)==r+1,(b,r)
            witness_checks+=1
    for b in range(1,5):
        for r in range(0,4):
            w=witness(b,r)
            # Directly enumerate all deletion masks, without gap or DP logic.
            for idx in combinations(range(len(w)),r):
                ignored=set(idx)
                sub=''.join(c for i,c in enumerate(w) if i not in ignored)
                ptr=0; p='0'+'1'*b+'0'
                for c in sub:
                    if ptr<len(p) and c==p[ptr]:ptr+=1
                assert ptr==len(p),(b,r,w,idx)
                direct_cases+=1
    print('PASS independent subsequence-automaton/gap comparison:',num,'words')
    print('PASS exact maximum profile:',lengths,'(b,n) cases')
    print('PASS construction lengths and deletion tolerance:',witness_checks,'(b,r) cases')
    print('PASS direct deletion subsets:',direct_cases,'cases')
    print('Extremal examples:')
    for b,r in [(1,3),(2,1),(2,4),(3,2),(4,3),(5,6)]:
        print(' b=',b,' r=',r,' n=',len(witness(b,r)),' word=',witness(b,r))
if __name__=='__main__': main()

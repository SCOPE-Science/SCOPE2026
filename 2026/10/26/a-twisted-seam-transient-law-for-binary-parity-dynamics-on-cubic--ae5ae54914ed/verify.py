#!/usr/bin/env python3
"""Direct finite checks for binary neighbor-parity dynamics on two cyclic ladders."""
from collections import Counter

def rows(n, twisted):
    size=2*n
    out=[]
    for j in range(size):
        if twisted:
            near=[(j-1)%size,(j+1)%size,(j+n)%size]
        else:
            layer,position=divmod(j,n)
            near=[layer*n+(position-1)%n,layer*n+(position+1)%n,(1-layer)*n+position]
        out.append(sum(1<<v for v in near))
    return out

def gf_rank(vectors):
    pivots={}
    for row in vectors:
        v=row
        while v:
            bit=v.bit_length()-1
            if bit not in pivots:
                pivots[bit]=v
                break
            v^=pivots[bit]
    return len(pivots)

def multiply(A,B):
    out=[]
    for row in A:
        value=0
        while row:
            low=row&-row
            value^=B[low.bit_length()-1]
            row-=low
        out.append(value)
    return out

def t_bound(n,twisted):
    if n%3:
        return 0
    k=n&-n
    return (1 if k==1 else 2*k) if twisted else (2 if k==1 else k)

def cumulative(n,t,twisted):
    N=2*n
    if n%3:
        return 1<<N
    k=n&-n
    if twisted:
        e=2 if k==1 else 1
        return 1<<(N-4*k+2*min(e*t,2*k))
    if k==1:
        return 1<<(N-4+2*min(t,2))
    return 1<<(N-4*k+4*min(t,k))

def scalar_update(x,A):
    y=0
    for i,row in enumerate(A):
        y|=((x&row).bit_count()&1)<<i
    return y

rank_tests=0
brute_tests=0
for n in range(3,129):
    for twisted in (False,True):
        A=rows(n,twisted)
        N=2*n
        power=[1<<i for i in range(N)]
        T=t_bound(n,twisted)
        # Independently test every predicted cumulative kernel size through T+1.
        for t in range(T+2):
            actual=1<<(N-gf_rank(power))
            expected=cumulative(n,t,twisted)//cumulative(n,0,twisted)
            assert actual==expected, (n,twisted,t,actual,expected)
            rank_tests+=1
            power=multiply(A,power)
        assert gf_rank(power)==gf_rank(multiply(A,power))
        if n<=9:
            recurrent={scalar_update(x,power) for x in range(1<<N)}
            # power represents A^(T+2), so its image equals the recurrent states.
            assert len(recurrent)==cumulative(n,0,twisted)
            seen=Counter()
            for x in range(1<<N):
                y=x
                for t in range(T+1):
                    if y in recurrent:
                        seen[t]+=1
                        break
                    y=scalar_update(y,A)
                else:
                    raise AssertionError((n,twisted,x))
            for t in range(T+1):
                expected=cumulative(n,t,twisted)-(cumulative(n,t-1,twisted) if t else 0)
                assert seen[t]==expected,(n,twisted,t,seen[t],expected)
            brute_tests+=1
print('VERIFY_OK ranks=',rank_tests,' complete_small_graphs=',brute_tests,' small_state_evaluations=',sum(2**(2*n) for n in range(3,10))*2)
for n in (3,6,9,12,18,24,48):
    k=n&-n
    for twisted in (False,True):
        print('n=',n,'twisted=',twisted,'T=',t_bound(n,twisted),'recurrent=',cumulative(n,0,twisted), 'basin=',(1 if n%3 else 2**(4*k)))

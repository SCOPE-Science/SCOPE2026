#!/usr/bin/env python3
"""Exact finite checks for two-row rook graph majority dynamics.
Run with Python 3 standard library: python3 verify_rook.py
These finite checks supplement, but do not replace, the all-n proof.
"""
from math import comb

def F_vote(n, state):
    u,v=state
    result=[]
    for row,other in ((u,v),(v,u)):
        nr=0
        for j in range(n):
            vote=0
            for i in range(n):
                if i!=j: vote += (row>>i)&1
            vote += (other>>j)&1
            old=(row>>j)&1
            if 2*vote>n or 2*vote==n and old:
                nr |= 1<<j
        result.append(nr)
    return tuple(result)

def F_sets(n,state):
    u,v=state
    full=(1<<n)-1
    k=n//2
    def g(x,y):
        a=x.bit_count()
        if n%2==0:
            if a<k:return 0
            if a==k:return y
            return full
        if a<k:return 0
        if a==k:return y & (~x)&full
        if a==k+1:return full & (~(x&(~y)))
        return full
    return (g(u,v),g(v,u))

def stats_formula(n):
    k=n//2
    B=comb(n,k)
    L=sum(comb(n,a) for a in range(k))
    if n%2==0:
        fixed=4+B
        recurrent=4+B*B
        pre1=4*L*L+4*B-4
        pre2=4*B*(L-1)
        return {(0,1):fixed, (0,2):recurrent-fixed,(1,None):pre1,(2,None):pre2,(3,None):0}
    fixed=4
    recurrent=4+2*(k+2)*B
    upto1=4*L*L+2*B*(2**(k+1)+(k+1)**2)
    pre3=4*sum(a*comb(n,a)*comb(n-a,k) for a in range(1,k))
    pre2=4**n-upto1-pre3
    return {(0,1):fixed,(0,2):recurrent-fixed,(1,None):upto1-recurrent,(2,None):pre2,(3,None):pre3}

def run():
    summary=[]
    for n in range(3,10):
        dim=1<<n
        observed={(0,1):0,(0,2):0,(1,None):0,(2,None):0,(3,None):0}
        fvalues={}
        for u in range(dim):
            for v in range(dim):
                state=(u,v)
                a=F_sets(n,state)
                assert a==F_vote(n,state),(n,state,a,F_vote(n,state))
                x=state
                path=[x]
                for j in range(5):
                    x=F_sets(n,x)
                    path.append(x)
                assert path[5]==path[3],(n,state,path)
                if n%2==0:assert path[4]==path[2]
                t=next(i for i in range(4) if path[i]==path[i+2])
                p=1 if path[t]==path[t+1] else 2
                observed[(t,p if t==0 else None)]+=1
                if n%2: assert t<= (2 if n==3 else 3)
                else:assert t<=2
        predicted=stats_formula(n)
        assert observed==predicted,(n, observed, predicted)
        assert sum(predicted.values())==4**n
        maxpre=max(t for (t,p),count in observed.items() if count>0)
        assert maxpre==(2 if n<=4 else 3 if n%2 else 2)
        summary.append((n,4**n,predicted[(0,1)],predicted[(0,2)],predicted[(1,None)],predicted[(2,None)],predicted[(3,None)]))
    # Analytic formula consistency, not proof of the closed forms.
    for n in range(3,401):
        d=stats_formula(n)
        assert all(v>=0 for v in d.values())
        assert sum(d.values())==4**n
    print('n | total | fixed | period2 states | depth1 | depth2 | depth3')
    for x in summary:print(' '.join(map(str,x)))
    print('EXHAUSTIVE_VOTE_AND_ORBIT_OK: n=3..9; configurations=',sum(4**n for n in range(3,10)))
    print('FORMULA_INTEGRITY_OK: n=3..400')
if __name__=='__main__':run()

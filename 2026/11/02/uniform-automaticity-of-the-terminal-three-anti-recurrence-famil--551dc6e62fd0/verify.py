#!/usr/bin/env python3
"""Independent exact checks of block morphism for anti-recurrence forms (a,3)."""

def predicted(a, n):
    tau = a+3
    kap = 2*tau+1
    state = [None]*n
    state[0] = a+6
    for k in range(1,n):
        m, digit=divmod(k,tau)
        r=state[m]
        # independently generate complement digits rather than algebraic branches
        cs=[x for x in range(1,kap+1) if x!=r]
        j=digit+1
        state[k]=a*cs[2*j-2]+3*cs[2*j-1]-kap*(j-1)
        assert 4<=state[k]<=kap
    return [kap*k+state[k] for k in range(n)]


def actual(a,n):
    # Generate the defining values directly by maintaining excluded values;
    # no block substitution is used in this function.
    chosen=set()
    nonmembers=[]
    next_i=1
    values=[]
    prev=0
    for k in range(n):
        while len(nonmembers)<2*(k+1):
            if next_i not in chosen:
                nonmembers.append(next_i)
            next_i+=1
        x=a*nonmembers[2*k]+3*nonmembers[2*k+1]
        assert x>prev
        assert x not in nonmembers and x not in chosen
        chosen.add(x)
        values.append(x)
        prev=x
    return values


def verify():
    count=0
    for a,n in [(1,10000),(2,10000),(3,10000),(4,10000),(5,10000),(9,10000),(17,10000),(100,5000)]:
        p=predicted(a,n)
        v=actual(a,n)
        assert p==v,(a,[(i,x,y) for i,(x,y) in enumerate(zip(p,v)) if x!=y][:3])
        kap=2*a+7
        assert all(kap*i+4<=x<=kap*(i+1) for i,x in enumerate(v))
        count+=n
    # All finite state transitions for each of 200 a-values, checked with independent enumeration
    trans=0
    for a in range(1,201):
        tau=a+3;kap=2*tau+1
        for r in range(4,kap+1):
            cs=[x for x in range(1,kap+1) if x!=r]
            for j in range(1,tau+1):
                observed=a*cs[2*j-2]+3*cs[2*j-1]-kap*(j-1)
                expected=kap-a-j if r>2*j else (kap+3-a-j if r==2*j else kap+3-j)
                assert observed==expected
                assert 4<=observed<=kap
                trans+=1
    print('VERIFY_OK tested_greedy_terms=%d distinct_a=8 transition_cases=%d a_max=200 all_exact=yes'%(count,trans))

if __name__=='__main__':verify()

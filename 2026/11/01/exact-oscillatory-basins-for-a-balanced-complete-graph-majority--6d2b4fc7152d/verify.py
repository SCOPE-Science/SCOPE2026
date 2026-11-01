"""Standalone exact check for two-type synchronous majority/minority dynamics on K_(2k).
No external packages. For k=1,...,8 independently enumerate labeled states.
"""
from math import comb

def update(state,k):
    """The first k bits are conformists; the remaining k are contrarians."""
    n=2*k
    out=0
    for i in range(n):
        neighbors=state.bit_count()-((state>>i)&1)
        new=(neighbors>=k) if i<k else (neighbors<k)
        out|=int(new)<<i
    return out

def test(k):
    n=2*k; cap=1<<n; mask=(1<<k)-1
    expected_b=comb(k,k//2)**2 if k%2==0 else 0
    expected={0:4+expected_b,1:cap-comb(n,k)-2,2:comb(n,k)-2-expected_b}
    counts={0:0,1:0,2:0}; periodic_2=0; periodic_4=0
    cycles={}
    for state in range(cap):
        path=[]; first={}; x=state
        while x not in first:
            first[x]=len(path);path.append(x);x=update(x,k)
            assert len(path)<8,('unbounded',k,state,path)
        transient=first[x]; period=len(path)-transient
        assert period in (2,4), (k,state,period)
        assert transient<=2, (k,state,transient)
        counts[transient]+=1
        if transient==0:
            if period==2: periodic_2+=1
            else:periodic_4+=1
        cyc=tuple(path[transient:]); canonical=min(cyc[i:]+cyc[:i] for i in range(len(cyc)))
        cycles[canonical]=period
        a=(state&mask).bit_count(); b=(state>>k).bit_count()
        expected_period2=(k%2==0 and a==k//2 and b==k//2)
        if expected_period2:
            assert period==2 and transient==0
        else:
            assert period==4
    assert counts==expected,(k,counts,expected)
    assert periodic_2==expected_b and periodic_4==4
    assert sum(1 for v in cycles.values() if v==4)==1
    assert sum(1 for v in cycles.values() if v==2)==expected_b//2
    print(f'k={k}: {cap} states, T0,T1,T2={counts[0]},{counts[1]},{counts[2]}, period2-orbits={expected_b//2}, four-orbits=1: OK')

if __name__=='__main__':
    for k in range(1,9):test(k)
    print('MAJORITY_MINOR_CONSTELLATION_ALL_CHECKS_PASSED')

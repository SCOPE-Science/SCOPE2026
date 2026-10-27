"""Exact finite tests for the cubic Dickson map's dyadic orbit census."""
from collections import Counter


def v2(x):
    if x == 0:
        return 10**9
    return (abs(x) & -abs(x)).bit_length() - 1


def predicted(k, x):
    r = k-1
    if x % 2 == 0:
        t = x // 2
        a = 2 + v2(t) + v2(t-1) + v2(t+1)
        return (0, 1 << max(0, r-a))
    u = (x-1)//2
    w = v2(u*(u+1))
    return (1, 1 << max(0, r-4-2*w))


def predicted_census(k):
    r=k-1
    cycles={1: (1<<r) if r<=3 else 12 if r==4 else 20}
    for j in range(1, r+1):
        s=r-j
        if s in (3,4): cycles[1<<j]=2
        elif s>=5: cycles[1<<j]=10
    S=max(0,(r-5)//2)
    tails={1:1<<(r-S)}
    for s in range(1,S+1):
        j=r-4-2*s
        assert j>=1
        tails[1<<j]=1<<(r-s)
    return cycles,tails


def direct(k):
    m=1<<k
    f=lambda x: (x*x*x-3*x)%m
    status={}
    for x in range(m):
        if x in status: continue
        path=[]; indices={}; p=x
        while p not in status and p not in indices:
            indices[p]=len(path); path.append(p);p=f(p)
        if p in indices:
            start=indices[p]; period=len(path)-start
            for q in path[start:]: status[q]=(0,period)
            prefix=path[:start]
        else: prefix=path
        for q in reversed(prefix):
            z=status[f(q)];status[q]=(z[0]+1,z[1])
    assert len(status)==m
    cycles=Counter(status[x][1] for x in range(0,m,2) if status[x][0]==0)
    cyclecounts={j:c//j for j,c in cycles.items()}
    tails=Counter(status[x][1] for x in range(1,m,2))
    return status,dict(cyclecounts),dict(tails)


def main():
    count=0
    incident_cases=0
    for k in range(1,16):
        st,cycles,tails=direct(k)
        for x,s in st.items():
            assert s==predicted(k,x),(k,x,s,predicted(k,x))
            count+=1
        pc,pt=predicted_census(k)
        assert cycles==pc,(k,cycles,pc)
        assert tails==pt,(k,tails,pt)
        assert sum((length*number) for length,number in cycles.items())==1<<(k-1)
        assert sum(tails.values())==1<<(k-1)
        r=k-1; m=1<<k; f=lambda x:(x*x*x-3*x)%m
        inbound=Counter(f(x) for x in range(1,m,2))
        visited=set(); found=Counter()
        for root in range(0,m,2):
            if root in visited: continue
            orbit=[]; curr=root
            while curr not in visited:
                visited.add(curr); orbit.append(curr); curr=f(curr)
            length=len(orbit)
            if length==1:continue
            incoming=[inbound.get(q,0) for q in orbit]
            nz=[n for n in incoming if n]
            if not nz:continue
            js=length.bit_length()-1
            sparam=(r-4-js)//2
            assert r-4-js==2*sparam and sparam>=1
            assert len(nz)==len(orbit),(k,root,incoming)
            assert set(nz)=={1<<(sparam+3)},(k,root,incoming)
            found[length]+=1
            incident_cases+=1
        S=max(0,(r-5)//2)
        assert found==Counter({1<<(r-4-2*ss):2 for ss in range(1,S+1)}),(k,found)
    for t in range(-50,51):
        if t in (0,1,-1): continue
        a=v2(4*t*(t*t-1)); mod=1<<120
        for j in range(9):
            z=t%mod
            for _ in range(1<<j):
                z=(4*z*z*z-3*z)%mod
            assert v2((z-t)%mod) == a+j,(t,j)
    print('VERIFY_OK: %d independently traced dyadic starting states; 15 cycle and tail censuses; 99 valuation-lifting samples and %d distinguished leaf-bearing cycles' % (count,incident_cases))

if __name__=='__main__': main()

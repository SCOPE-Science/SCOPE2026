"""Standalone exhaustive and boundary-transfer checks of fan majority periodic states."""
from collections import defaultdict


def update(n,state):
    c=state&1
    x=[(state>>(i+1))&1 for i in range(n)]
    s=sum(x)
    d=1 if 2*s>n else 0 if 2*s<n else c
    out=d
    for i in range(n):
        adj=[c]+([x[i-1]] if i else [])+([x[i+1]] if i<n-1 else [])
        t=sum(adj)
        y=1 if 2*t>len(adj) else 0 if 2*t<len(adj) else x[i]
        out|=y<<(i+1)
    return out


def transfer_counts(n):
    letters=[(x,y) for x in range(2) for y in range(2)]
    dp=defaultdict(int)
    for s in letters:
        for t in letters:
            if s[1]==s[0]*t[0] and s[0]==(s[1]|t[1]):
                dp[(s,t,s[0]+t[0],s[1]+t[1])]+=1
    for i in range(2,n):
        nxt=defaultdict(int)
        for (s,t,nx,ny),w in dp.items():
            for u in letters:
                if t[1]==s[0]*u[0] and t[0]==(s[1]|u[1]):
                    nxt[(t,u,nx+u[0],ny+u[1])]+=w
        dp=nxt
    N=0
    for (s,t,nx,ny),w in dp.items():
        if t[1]==s[0]*t[0] and t[0]==(s[1]|t[1]) and 2*nx>n and 2*ny<n:
            N+=w
    return N


def main():
    checked=0
    for n in range(3,13):
        H=transfer_counts(n)
        fixed=periodic=cycles=0
        for x in range(1<<(n+1)):
            y=update(n,x)
            if y==x:fixed+=1
            if update(n,y)==x:
                periodic+=1
                if not (x&1) and (y&1): cycles+=1
        assert fixed==2,(n,'fixed',fixed)
        assert periodic==2+2*H,(n,'periodic',periodic,H)
        assert cycles==H,(n,'oriented',cycles,H)
        assert (H>0)==(n!=4)
        print('n',n,'fixed',fixed,'two_cycles',H,'periodic_states',periodic)
        checked+=1<<(n+1)
    print('FAN_MORPHOLOGY_VERIFY_OK',checked)

if __name__=='__main__':main()

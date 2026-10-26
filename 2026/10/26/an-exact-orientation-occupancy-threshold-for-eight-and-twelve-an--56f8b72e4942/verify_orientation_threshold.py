#!/usr/bin/env python3
"""Independent exact graph and finite transfer checks for 8/12 orientations."""
from math import sqrt

ALPHABETS={
    8:(0,30,45,60,90,-60,-45,-30),
    12:(0,15,30,45,60,75,90,-75,-60,-45,-30,-15),
}
PRINCIPAL={0,45,-45,90}

def matrix(angles):
    return [[int(0<min((a-b)%180,(b-a)%180)<=45) for b in angles]
            for a in angles]

def power(H):
    n=len(H); v=[1.0]*n
    for _ in range(1000):
        w=[sum(x*y for x,y in zip(row,v)) for row in H]
        norm=sum(x*x for x in w)**0.5
        w=[x/norm for x in w]
        if max(abs(w[i]-v[i]) for i in range(n))<1e-14:break
        v=w
    return sum(v[i]*sum(H[i][j]*v[j] for j in range(n)) for i in range(n)),v

def finite_expectation(S,N):
    # Last run must have length one. Count words and total occurrences of each letter.
    k=len(S)
    trans=matrix(S)
    states={(a,1):(1,tuple(int(i==a) for i in range(k))) for a in range(k)}
    for n in range(2,N+1):
        new={}
        for (a,r),(count,cnts) in states.items():
            for b in range(k):
                if not (trans[a][b] or a==b) or (a==b and r==3):continue
                key=(b,r+1 if a==b else 1)
                prev,prevs=new.get(key,(0,(0,)*k))
                new[key]=(prev+count, tuple(prevs[i]+cnts[i]+(count if i==b else 0) for i in range(k)))
        states=new
    U=sum(c for (a,r),(c,v) in states.items() if r==1)
    freq=[sum(v[i] for (a,r),(c,v) in states.items() if r==1)/(N*U) for i in range(k)]
    return U,dict(zip(S,freq))

def main():
    for k,S in ALPHABETS.items():
        H=matrix(S)
        assert all(H[i][j]==H[j][i] and H[i][i]==0 for i in range(k) for j in range(k))
        assert all(sum(H[i][j] for j in range(k) if S[j] in PRINCIPAL)==2 for i in range(k)) if k==8 else all(sum(row)==6 for row in H)
        rho,v=power(H)
        if k==8:
            target=(3+sqrt(17))/2
            aux=(sqrt(17)-1)/4
            pi=(17+sqrt(17))/136
            assert all(sum(H[i][j] for j in range(k) if S[j] in PRINCIPAL)==2 for i in range(k))
            assert all(sum(H[i][j] for j in range(k) if S[j] not in PRINCIPAL)==(2 if S[i] in PRINCIPAL else 1) for i in range(k))
            assert abs(aux**2/(4+4*aux**2)-(17-sqrt(17))/136)<1e-13
        else:
            target=6
            pi=1/12
        assert abs(rho-target)<1e-11,(k,rho,target)
        ps={a:v[i]*v[i] for i,a in enumerate(S)}
        assert all(abs(ps[a]-pi)<1e-11 for a in PRINCIPAL)
        assert (pi>.1 if k==8 else pi<.1)
        lo,hi=target,target+2
        for _ in range(100):
            x=(lo+hi)/2
            if (x**3 -target*(x*x+x+1))>0:hi=x
            else:lo=x
        lam=(lo+hi)/2
        for n in (12,30,80):
            U,freq=finite_expectation(S,n)
            print('k',k,'n',n,'U',U,'principal_share',round(freq[0],10))
            assert abs(freq[0]-pi)<.02
        print('k',k,'rho',rho,'lambda',lam,'principal_limit',pi)
    print('VERIFY_OK')
if __name__=='__main__':main()

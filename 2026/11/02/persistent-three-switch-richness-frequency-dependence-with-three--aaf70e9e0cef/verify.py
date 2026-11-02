#!/usr/bin/env python3
"""Self-contained exact checks for heterogeneous occupancy covariance signs."""
from math import comb, factorial

W=(9,3,1)
S=sum(W)

def numerator_formula(n,r,w=W):
    s=sum(w)
    a=sum((s-x)**n for x in w)
    z=comb(n,r)*sum(x**r*(s-x)**(n-r) for x in w)
    y=comb(n,r)*sum(w[j]**r*(s-w[i]-w[j])**(n-r) for i in range(len(w)) for j in range(len(w)) if i!=j)
    return a*z-y*s**n # covariance(K,N_r) numer / s**(2n)

def numerator_enumerated(n,r,w=W):
    s=sum(w)
    m=len(w)
    assert m==3
    eK=eR=eKR=0
    for x in range(n+1):
        for y in range(n-x+1):
            z=n-x-y
            counts=(x,y,z)
            wt=comb(n,x)*comb(n-x,y)*w[0]**x*w[1]**y*w[2]**z
            K=sum(v>0 for v in counts)
            R=sum(v==r for v in counts)
            eK+=wt*K;eR+=wt*R;eKR+=wt*K*R
    return eKR*s**n-eK*eR

def max_bases(a,b):
    w=W;s=S
    positives=[(s**b*w[j]**a*w[k]**(b-a),j,k) for j in range(3) for k in range(3) if j!=k]
    negatives=[((s-w[i])**b*w[j]**a*(s-w[j])**(b-a),i,j) for i in range(3) for j in range(3)]
    return max(positives),max(negatives)

def run():
    count=0
    for n in range(2,22):
        for r in range(1,n+1):
            x=numerator_formula(n,r)
            y=numerator_enumerated(n,r)
            assert x==y, (n,r,x,y)
            count+=1
    signs=[]
    for r in range(1,15):
        z=numerator_formula(14,r)
        assert z != 0
        signs.append('+' if z>0 else '-')
    assert ''.join(signs)=='++++-+++++----', ''.join(signs)
    count+=14
    for a,b,sg,lower_num,lower_den in [(1,10,-1,3,2),(2,5,1,13,12),(3,5,-1,7,6),(9,10,1,3,2)]:
        p,n=max_bases(a,b)
        hi,lo=(p[0],n[0]) if sg==1 else (n[0],p[0])
        assert lower_den*hi > lower_num*lo
        count+=1
        for t in [15,16,20,30]:
            N=10*t; r=N*a//b
            assert N*a%b==0
            assert (numerator_formula(N,r)>0)==(sg==-1)
            count+=1
    assert (3/2)**15>9 and (13/12)**30>9 and (7/6)**30>6
    count+=3
    for n in range(2,24):
        for a in range(1,6):
            b=7-a
            w=(a,b);s=a+b
            for r in range(1,n+1):
                f=numerator_formula(n,r,w)
                assert (f>0 if r<n else f<0), (n,w,r,f)
                count+=1
    print('PASS',count,'assertions')
    print('n=14 K-signs:',''.join(signs))
    print('n=14 scaled covariance numerators (r, Q_r):')
    for r in range(1,15): print(r,numerator_formula(14,r)//comb(14,r))
    for a,b,sg,l_num,l_den in [(1,10,-1,3,2),(2,5,1,13,12),(3,5,-1,7,6),(9,10,1,3,2)]:
        p,n=max_bases(a,b)
        print('RATE',a,b,'P',p,'N',n,'sign',sg)

if __name__=='__main__':run()

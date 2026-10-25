#!/usr/bin/env python3
"""Independent checks for the exact finite loose-three-star fixation formula."""
from fractions import Fraction as Q


def closed(m, r):
    r=Q(r); a=r/(r+2*m); b=2*m*r/(2*m*r+1)
    q=(1-b)/a
    H=1/(q**(m-1)+b*sum((q**j for j in range(m-1)),Q(0)))
    c=m*r/(m*(r+1)+1)
    return (a*H,c*H,(a+2*m*c)*H/(2*m+1))


def transitions(m,r,state):
    r=Q(r); n=2*m+1; mutant=state.bit_count(); tot=r*mutant+(n-mutant)
    out={}
    for parent in range(n):
        mutant_parent=(state>>parent)&1
        w=(r if mutant_parent else Q(1))/tot
        edge_ids=range(m) if parent==0 else [(parent-1)//2]
        for j in edge_ids:
            e=(1<<0)|(1<<(2*j+1))|(1<<(2*j+2))
            nxt=(state|e) if mutant_parent else (state&~e)
            inc=w/(m if parent==0 else 1)
            out[nxt]=out.get(nxt,Q(0))+inc
    assert sum(out.values())==1
    return out


def exact_full(m,r):
    n=2*m+1; size=(1<<n); all_mut=size-1
    states=list(range(1,size-1)); indices={state:i for i,state in enumerate(states)}
    A=[]; B=[]
    for state in states:
        trans=transitions(m,r,state);i=indices[state]
        row=[Q(int(j==i)) for j in range(len(states))]
        for nxt,p in trans.items():
            if nxt in indices:row[indices[nxt]]-=p
        A.append(row);B.append(trans.get(all_mut,Q(0)))
    # Exact fraction Gaussian with partial pivoting.
    k=len(states)
    for i in range(k):
        pivot=next((j for j in range(i,k) if A[j][i]),None)
        assert pivot is not None
        A[i],A[pivot]=A[pivot],A[i]
        B[i],B[pivot]=B[pivot],B[i]
        c=A[i][i]
        for j in range(i+1,k):
            if A[j][i]==0:continue
            d=A[j][i]/c;A[j][i]=Q(0)
            for h in range(i+1,k):A[j][h]-=d*A[i][h]
            B[j]-=d*B[i]
    ans=[Q(0)]*k
    for i in reversed(range(k)):
        ans[i]=(B[i]-sum((A[i][j]*ans[j] for j in range(i+1,k)),Q(0)))/A[i][i]
    return [Q(0)]+ans+[Q(1)]


def main():
    for m in range(1,9):
        for r in (Q(1,3),Q(1,2),Q(1),Q(5,4),Q(2),Q(3)):
            h,l,u=closed(m,r)
            assert Q(0)<h<=1 and Q(0)<l<=1 and Q(0)<u<=1
            assert u==(h+2*m*l)/(2*m+1)
            a=r/(r+2*m);b=2*m*r/(2*m*r+1)
            q=(1-b)/a
            if r!=1:
                f=(1-r**-2)/(1-r**-2*q**(m-1))
                assert h/a==f
            else:
                assert h==Q(1,2*m*m+1) and l==Q(m,2*m*m+1)
    print('Exact harmonic identities: 48 parameter cases PASS')
    for m in (1,2):
        for r in (Q(1,2),Q(1),Q(2),Q(3)):
            x=exact_full(m,r)
            h,l,u=closed(m,r)
            assert x[1]==h, (m,r,'hub',x[1],h)
            assert all(x[1<<i]==l for i in range(1,2*m+1)),(m,r,'leaf')
            assert (x[1]+sum(x[1<<i] for i in range(1,2*m+1)))/(2*m+1)==u
    print('Direct labeled absorbing-chain exact rational checks: 8 cases PASS')
    # Sharp all-fitness suppression on the first genuinely nontrivial loose star.
    # Polynomial numerator of Moran - loose fixation, after cancellation of r-1.
    def p(r):return 8*r**4+30*r**3+41*r**2+44*r+7
    for r in (Q(1,9),Q(1,2),Q(1),Q(2),Q(9)):
        _,_,f=closed(2,r)
        moran=Q(1,5) if r==1 else (1-r**-1)/(1-r**-5)
        z=r*r*(r-1)*p(r)/((r+4)*(2*r+3)*(4*r*r+r+4)*(r**4+r**3+r*r+r+1))
        assert moran-f==z
    print('Five exact symbolic-factor identity tests PASS')
    # Exact polynomial identity for every real r: multiply dense integer coefficients.
    def mul(x,y):
        z=[0]*(len(x)+len(y)-1)
        for i,a in enumerate(x):
            for j,b in enumerate(y): z[i+j]+=a*b
        return z
    def sub(x,y):
        n=max(len(x),len(y));return [(x[i] if i<len(x) else 0)-(y[i] if i<len(y) else 0) for i in range(n)]
    # LHS numerator = r^4 * [(r+4)(2r+3)(4r^2+r+4)] - r^2*(2r+7)*(4r+1)*(r^4+...+1).
    den=mul(mul([4,1],[3,2]),[4,1,4]); geo=[1,1,1,1,1]
    first=[0,0,0,0]+den
    second=[0,0]+mul(mul([7,2],[1,4]),geo)
    target=[0,0]+mul([-1,1],[7,44,41,30,8])
    assert list(reversed(list(__import__("itertools").dropwhile(lambda z:z==0,reversed(sub(first,second))))))==target
    print('Universal integer-polynomial suppression factorization PASS')

if __name__=='__main__':main()

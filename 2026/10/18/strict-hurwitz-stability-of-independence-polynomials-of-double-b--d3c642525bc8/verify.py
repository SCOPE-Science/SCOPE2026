"""Exact independent-set coefficient and Hurwitz checks for double-broom trees.

Run: python3 verify.py
No third-party packages are required. The finite checks are independent
of, and do not replace, the infinite half-plane proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def add(a,b):
    return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))) ]


def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]+=u*v
    return out


def tpower(k):
    return [comb(k,i) for i in range(k+1)]


def xmul(p,k=1):return [0]*k+p


def path_poly(n):
    if n==-1:return [1]
    if n==0:return [1]
    a,b=[1],[1,1]
    for j in range(2,n+1):a,b=b,add(b,xmul(a))
    return b


def formula(a,b,d):
    tA,tpB=tpower(a),tpower(b)
    if d==1:return add(multiply(tA,tpB),add(xmul(tA),xmul(tpB)))
    q=multiply(multiply(tA,tpB),path_poly(d-1))
    q=add(q,multiply(xmul(add(tA,tpB)),path_poly(d-2)))
    q=add(q,multiply(xmul([1],2),path_poly(d-3)))
    return q


def graph_edges(a,b,d):
    n=d+1+a+b
    edges=[]
    for j in range(d):edges.append((j,j+1))
    for j in range(d+1,d+1+a):edges.append((0,j))
    for j in range(d+1+a,n):edges.append((d,j))
    return n,edges


def brute(a,b,d):
    n,edges=graph_edges(a,b,d)
    adj=[0]*n
    for x,y in edges:adj[x]|=1<<y;adj[y]|=1<<x
    # Dynamic enumeration of every subset, with independence recorded incrementally.
    valid=bytearray(1<<n)
    valid[0]=1
    arr=[0]*(n+1)
    arr[0]=1
    for mask in range(1,1<<n):
        lb=mask&-mask
        v=lb.bit_length()-1
        prev=mask^lb
        if valid[prev] and not (prev&adj[v]):
            valid[mask]=1
            arr[mask.bit_count()]+=1
    while len(arr)>1 and arr[-1]==0:arr.pop()
    return arr


def routh_strict_stability(poly):
    """Exact Routh table first-column test for strictly Hurwitz real polynomials."""
    p=list(reversed(poly))
    while len(p)>1 and p[0]==0:p.pop(0)
    degree=len(p)-1
    N=(degree+2)//2
    r0=[Fraction(p[2*j]) if 2*j<=degree else Fraction(0) for j in range(N)]
    r1=[Fraction(p[2*j+1]) if 2*j+1<=degree else Fraction(0) for j in range(N)]
    if degree==0:return p[0]>0
    if r0[0]<=0 or r1[0]<=0:return False
    for i in range(2,degree+1):
        if r1[0]==0:return False
        r2=[ (r1[0]*(r0[j+1] if j+1<N else 0)-r0[0]*(r1[j+1] if j+1<N else 0))/r1[0] for j in range(N)]
        if r2[0]<=0:return False
        r0,r1=r1,r2
    return True


def run():
    checked=0
    routh=0
    maxverts=0
    for a in range(2,6):
        for b in range(2,6):
            for d in range(1,7):
                f=formula(a,b,d)
                g=brute(a,b,d) if d+1+a+b<=18 else None
                if g is not None:
                    assert f==g,(a,b,d,f,g)
                    checked+=1
                    maxverts=max(maxverts,d+1+a+b)
                assert routh_strict_stability(f),(a,b,d)
                routh+=1
    print('VERIFIED: exact exhaustive graph polynomial comparisons',checked)
    print('VERIFIED: exact Routh-Hurwitz tables',routh)
    print('MAX_ENUMERATED_VERTICES',maxverts)
    print('VERIFIED: no candidate with a,b in [2,5], d in [1,6] failed')

if __name__=='__main__':run()

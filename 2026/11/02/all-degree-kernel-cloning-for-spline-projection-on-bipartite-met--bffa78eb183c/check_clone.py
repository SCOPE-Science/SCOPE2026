"""Exact rational checks of bipartite metric-graph spline endpoint kernels.

Run: python3 check_clone.py
Only the Python standard library is used.
"""
from fractions import Fraction as Q


def add(a,b,scale=1):
    return [ (a[i] if i<len(a) else Q(0)) + scale*(b[i] if i<len(b) else Q(0)) for i in range(max(len(a),len(b))) ]


def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def inner(a,b):
    c=mul(a,b)
    return sum((v/Q(i+1) for i,v in enumerate(c)),Q(0))


def inv(A):
    n=len(A)
    B=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        z=next(j for j in range(i,n) if B[j][i])
        B[i],B[z]=B[z],B[i]
        pivot=B[i][i]
        B[i]=[x/pivot for x in B[i]]
        for j in range(n):
            if j!=i:
                v=B[j][i]
                if v:B[j]=[x-v*y for x,y in zip(B[j],B[i])]
    return [row[n:] for row in B]


def local(d):
    bubbles=[[Q(0)]*j+[Q(1),Q(-1)] for j in range(1,d)]
    nodals=[[Q(1),Q(-1)],[Q(0),Q(1)]]
    if not bubbles:return nodals,Q(1,3),Q(1,6)
    B=inv([[inner(x,y) for y in bubbles] for x in bubbles])
    h=[]
    for nodal in nodals:
        v=[inner(nodal,b) for b in bubbles]
        coeff=[-sum(B[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]
        w=nodal
        for k,bl in zip(coeff,bubbles):w=add(w,bl,k)
        h.append(w)
    return h,inner(h[0],h[0]),inner(h[0],h[1])


def check():
    count=0
    for d in range(1,9):
        (h0,h1),a,b=local(d)
        assert a==Q(1,d*(d+2)),(d,a)
        assert b==Q((-1)**(d+1),(d+1)*d*(d+2)),(d,b)
        delta=a*a-b*b
        for p in range(1,7):
            for q in range(1,7):
                M=[]
                for i in range(p+q):
                    row=[]
                    for j in range(p+q):
                        if i==j:row.append(a*(q if i<p else p))
                        elif (i<p)!=(j<p):row.append(b)
                        else:row.append(Q(0))
                    M.append(row)
                B=inv(M)
                si=((p-1)/a+a/delta)/(p*q)
                ot=(a/delta-1/a)/(p*q)
                cross=-b/(delta*p*q)
                for j in range(p+q):
                    assert B[0][j]==(si if j==0 else ot if j<p else cross),(d,p,q,j)
                # Cloning K_(p,q) gives q copies of the K_(p,1) kernel, divided by q.
                for t in (Q(0),Q(1,7),Q(1,3),Q(1,2),Q(2,3),Q(6,7),Q(1)):
                    x0=sum(c*t**j for j,c in enumerate(h0))
                    x1=sum(c*t**j for j,c in enumerate(h1))
                    leaf=(si*x0+cross*x1)*q
                    other=(ot*x0+cross*x1)*q
                    expected_leaf=(((p-1)/a+a/delta)*x0-b/delta*x1)/p
                    expected_other=((a/delta-1/a)*x0-b/delta*x1)/p
                    assert leaf==expected_leaf and other==expected_other
                    count+=2
    print('PASS: independent exact Gram inversions and edge-kernel cloning in',count,'rational cases over degrees 1 through 8')


if __name__=='__main__':check()

"""Exact-rational checks for a predictive generalized-tent controller.
Run: python check.py. Finite tests support, but do not prove, the theorem.
"""
from fractions import Fraction as Q

checks = 0

def ck(c, msg=''):
    global checks
    assert c, msg
    checks += 1

def ctrl(H,theta,x):
    f=lambda z: H*min(z,1-z)
    return f(theta*x+(1-theta)*f(x))

def compose_parts(parts,H,s,c):
    out=[]
    for l,u,a,b in parts:
        splits=[l,u]
        if a:
            for v in (Q(1,2),c):
                xx=(v-b)/a
                if l<xx<u: splits.append(xx)
        splits=sorted(set(splits))
        for lo,hi in zip(splits,splits[1:]):
            y=a*(lo+hi)/2+b
            if y<=Q(1,2):
                na,nb=Q(0),Q(0)
            elif y<c:
                na,nb=s*a,s*(b-Q(1,2))
            else:
                na,nb=-s*a,H-s*(b-Q(1,2))
            out.append((lo,hi,na,nb))
    return out

for H in [Q(2),Q(5,2),Q(3),Q(4),Q(7)]:
    lower=1+1/H
    upper=H/(H-1)
    for w in [Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        theta=lower+(upper-lower)*w
        alpha=(H+1)*theta-H
        s=H*alpha
        r=H*(H-(H-1)*theta)
        c=(Q(1,2)+H*(theta-1))/alpha
        R=(1+H*(theta-1))/alpha
        J=(Q(1,2),R)
        L=R-Q(1,2)
        q=2/s
        ck(0<=r<1 and Q(1,2)<c<R<1 and R<H/2)
        ck(ctrl(H,theta,Q(1,2))==r/2)
        ck(ctrl(H,theta,c)==H/2)
        ck(ctrl(H,theta,R)==0)
        ck(ctrl(H,theta,Q(-5))==r*Q(-5))
        ck(ctrl(H,theta,Q(1,4))==r/4)
        ck(ctrl(H,theta,R+1)<=0)
        left=lambda y: (y-H**2*(1-theta))/s
        right=lambda y: (H-H**2*(1-theta)-y)/s
        ck(Q(1,2)<left(Q(1,2))<left(R)<c<right(R)<right(Q(1,2))<R)
        for y in [Q(1,2),Q(3,4)*Q(1,2)+R/4,(Q(1,2)+R)/2, R]:
            ck(ctrl(H,theta,left(y))==y)
            ck(ctrl(H,theta,right(y))==y)
        intervals=[J]
        for n in range(7):
            tot=sum((b-a for a,b in intervals),Q(0))
            ck(len(intervals)==2**n)
            ck(tot==L*q**n)
            ck(all(Q(1,2)<a<b<R for a,b in intervals) if n else True)
            if n<6:
                intervals=sorted([t for a,b in intervals for t in ((left(a),left(b)),(right(b),right(a)))])
                ck(all(intervals[i][1]<intervals[i+1][0] for i in range(len(intervals)-1)))
        # Fixed points on the inverse branches are in the survivor Cantor set.
        for inv in (left,right):
            x=inv(Q(0))/(1-Q(1)/s) if inv is left else None
            # Solve fixed point independently by evaluating inverse endpoints / affine slope.
            y0,y1=inv(Q(0)),inv(Q(1))
            a=y1-y0
            x=y0/(1-a)
            ck(Q(1,2)<x<R and ctrl(H,theta,x)==x)
    # Independently partition the deadbeat map and check the full capture-time tail.
    theta=upper
    s=H*((H+1)*theta-H)
    c=(Q(1,2)+H*(theta-1))/((H+1)*theta-H)
    parts=[(Q(0),Q(1),Q(1),Q(0))]
    for n in range(1,9):
        parts=compose_parts(parts,H,s,c)
        active=sum((hi-lo for lo,hi,a,b in parts if a or b),Q(0))
        expected=Q(1,2) if n==1 else (H-1)**2/(2*H**2)*((H-1)/H**2)**(n-2)
        ck(active==expected,f'capture-tail mismatch H={H} n={n}: {active} != {expected}')
        ck(sum((hi-lo for lo,hi,_,_ in parts),Q(0))==1)
print(f'PASS {checks} exact-rational assertions; parameters, branches, disjoint return cylinders, survivor lengths, deadbeat capture tails.')

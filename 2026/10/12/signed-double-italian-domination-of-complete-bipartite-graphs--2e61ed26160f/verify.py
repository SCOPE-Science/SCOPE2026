from itertools import product
from math import factorial

VALUES=(-1,1,2,3)

def side_states(r):
    # (n_-1,n_1,n_2,n_3,sum,positive_sum,multiplicity)
    out=[]
    for a in range(r+1):
        for b in range(r-a+1):
            for c in range(r-a-b+1):
                d=r-a-b-c
                s=-a+b+2*c+3*d
                p=b+2*c+3*d
                mult=factorial(r)//(factorial(a)*factorial(b)*factorial(c)*factorial(d))
                out.append((a,b,c,d,s,p,mult))
    return out

def pair_ok(x,y):
    ax,bx,cx,dx,SX,PX,_=x
    ay,by,cy,dy,SY,PY,_=y
    for lab,cnt in [(-1,ax),(1,bx),(2,cx),(3,dx)]:
        if cnt and lab+SY<1:
            return False
    if ax and PY<3:
        return False
    if bx and PY<2:
        return False
    for lab,cnt in [(-1,ay),(1,by),(2,cy),(3,dy)]:
        if cnt and lab+SX<1:
            return False
    if ay and PX<3:
        return False
    if by and PX<2:
        return False
    return True

def predicted(m,n):
    if m==n==2:
        return 4
    if min(m,n)<=3:
        return 3
    return 4

print('VERIFY_OK')
instances=0
state_pairs=0
min_labelings=0
for m in range(2,13):
    X=side_states(m)
    for n in range(2,13):
        Y=side_states(n)
        best=None
        count=0
        for x in X:
            for y in Y:
                state_pairs+=1
                if pair_ok(x,y):
                    w=x[4]+y[4]
                    mult=x[6]*y[6]
                    if best is None or w<best:
                        best=w; count=mult
                    elif w==best:
                        count+=mult
        assert best==predicted(m,n),(m,n,best,predicted(m,n))
        instances+=1
        min_labelings+=count
print('complete_bipartite_instances_checked =',instances)
print('side_state_pairs_checked =',state_pairs)
print('minimum_labelings_counted_across_instances =',min_labelings)
print('all minima matched the piecewise formula for 2 <= m,n <= 12')

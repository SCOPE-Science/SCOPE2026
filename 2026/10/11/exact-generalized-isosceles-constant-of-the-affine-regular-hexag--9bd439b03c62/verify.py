from fractions import Fraction as Q

V=[(Q(1),Q(1)),(Q(1),Q(0)),(Q(0),Q(-1)),(Q(-1),Q(-1)),(Q(-1),Q(0)),(Q(0),Q(1))]

def N(z):
    a,b=z
    return max(abs(a),abs(b)) if a*b>=0 else abs(a)+abs(b)

t=Q(1,3)
vals=[]
for x in V:
    for y in V:
        p=(x[0]+t*y[0],x[1]+t*y[1])
        m=(x[0]-t*y[0],x[1]-t*y[1])
        vals.append((N(p)**2+N(m)**2)/2)
assert len(vals)==36
assert set(vals)=={Q(10,9),Q(25,18)}
assert max(vals)==Q(25,18)
assert Q(9,10)*max(vals)==Q(5,4)

u=(Q(1),Q(1,2)); v=(Q(0),Q(1,2))
upv=(u[0]+v[0],u[1]+v[1])
umv=(u[0]-v[0],u[1]-v[1])
up2v=(u[0]+2*v[0],u[1]+2*v[1])
twou_v=(2*u[0]+v[0],2*u[1]+v[1])
assert N(upv)==N(umv)==1
assert N(up2v)==Q(3,2)
assert N(twou_v)==2
R=(N(up2v)**2+N(twou_v)**2)/(5*N(upv)**2)
assert R==Q(5,4)
print('VERIFY_OK')

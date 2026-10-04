from fractions import Fraction as Q

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def inv(x):
    d=x[0]*x[0]-5*x[1]*x[1]
    assert d
    return (x[0]/d,-x[1]/d)
def div(x,y): return mul(x,inv(y))
def powq(x,n):
    r=(Q(1),Q(0))
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r

# Coefficients in order s^2u^2,s^2v^2,t^2u^2,t^2v^2.
F=(Q(1),Q(-3),Q(-3),Q(5))
product=(Q(1),Q(-3),Q(-3),Q(9))
rhs=(Q(0),Q(0),Q(0),Q(4))
assert tuple(product[i]-rhs[i] for i in range(4))==F

def edge(x,y): return x*x*y*y-3*x*x-3*y*y+5
for x,y in [(Q(1),Q(1)),(Q(-1),Q(1)),(Q(1),Q(-1))]:
    assert edge(x,y)==0

def p(x): return [x*x+1,x*x-1,2*x,Q(0)]
def q(y): return [y*y+1,2*y*y+4,Q(0),2*y]

def rank(vs):
    a=[list(map(Q,v)) for v in vs]
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        z=a[r][c]; a[r]=[v/z for v in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                z=a[i][c]; a[i]=[a[i][j]-z*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r
p1,pn,q1,qn=p(Q(1)),p(Q(-1)),q(Q(1)),q(Q(-1))
assert rank([p1,pn,q1])==3
assert rank([p1,q1,qn])==3
assert p1!=q1

# lambda = 1/2 + (7/30)*sqrt(5), obtained from branch-pair ratio r=sqrt(5)/3 by (1+r)^2/(4r).
lam=(Q(1,2),Q(7,30))
one=(Q(1),Q(0))
r=(Q(0),Q(1,3))
assert mul(mul((Q(4),Q(0)),r),lam)==powq(add(one,r),2)
num=mul((Q(256),Q(0)),powq(add(sub(powq(lam,2),lam),one),3))
den=mul(powq(lam,2),powq(sub(lam,one),2))
j=div(num,den)
assert j==(Q(24918016,45),Q(0)),j
print('VERIFY_OK')

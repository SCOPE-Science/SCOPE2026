from fractions import Fraction as F

def first_cycle(lam,b):
    rr=sum(x*x for x in b)
    rAr=sum(l*x*x for l,x in zip(lam,b))
    alpha=rr/rAr
    s=[bi*(1-alpha*l) for bi,l in zip(b,lam)]
    if all(v==0 for v in s):
        return alpha,None,[alpha*bi for bi in b]
    t=[l*si for l,si in zip(lam,s)]
    omega=sum(ti*si for ti,si in zip(t,s))/sum(ti*ti for ti in t)
    x=[alpha*bi+omega*si for bi,si in zip(b,s)]
    return alpha,omega,x

def means(lam,b):
    rr=sum(x*x for x in b)
    m=sum(l*x*x for l,x in zip(lam,b))/rr
    den=sum(x*x*l*(l-m)*(l-m) for l,x in zip(lam,b))
    if den==0:
        return m,None
    n=sum(x*x*l*l*(l-m)*(l-m) for l,x in zip(lam,b))/den
    return m,n

# Exact sign-loss witness.
lam=[F(1),F(2),F(4)]
b=[F(1),F(1,2),F(1,11)]
alpha,omega,x=first_cycle(lam,b)
assert alpha==F(87,106)
assert omega==F(4609,12729)
assert x[2]==F(-7955,14842014)
assert x[2] < 0
m,n=means(lam,b)
assert alpha==1/m and omega==1/n
for li,bi,xi in zip(lam,b,x):
    assert xi == bi*(m+n-li)/(m*n)

# Exact two-mode positivity identity.
for a,c,pnum,pden in [
    (F(1),F(4),1,3),
    (F(2),F(7),2,5),
    (F(3,2),F(11,3),4,7),
]:
    p=F(pnum,pden); q=1-p
    # Choose b so squared weights are p,q only for identity replay through means.
    m=p*a+q*c
    n=(q*a*a+p*c*c)/(q*a+p*c)
    lhs=m+n-c
    rhs=a+p*q*(c-a)*(c-a)/(q*a+p*c)
    assert lhs==rhs and lhs>0

# Deterministic exact-rational envelope checks.
for k in [F(6,5),F(3,2),F(2),F(5,2),F(4),F(7)]:
    lower=k*(2-k)
    upper=(k+1)*(k+1)/(4*k)
    for lam2 in [F(1), (1+k)/2, k]:
        for b2 in [F(1,5),F(1,2),F(2)]:
            for b3 in [F(1,7),F(1,3),F(3,2)]:
                ls=[F(1),lam2,k]
                bs=[F(1),b2,b3]
                a,o,xv=first_cycle(ls,bs)
                if o is None:
                    continue
                for li,bi,xi in zip(ls,bs,xv):
                    eta=li*xi/bi
                    assert lower <= eta <= upper

print('VERIFY_OK')

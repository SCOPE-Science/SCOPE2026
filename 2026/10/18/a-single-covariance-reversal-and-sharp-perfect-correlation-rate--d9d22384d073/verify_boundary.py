"""Exact rational checks for root-cluster / first-generation boundary of a percolated RRT.
Run python3 verify_boundary.py (standard library only). Finite checks are not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial

assertions = 0
configurations = 0

def check(lhs,rhs,label):
    global assertions
    assertions+=1
    if lhs!=rhs:raise AssertionError(f'{label}: {lhs} != {rhs}')

def exact(n,p):
    global configurations
    numer = [F(0) for _ in range(7)]
    # E[C], E[B], E[C²], E[B²], E[CB], E[D], E[D²]
    for parents in product(*(range(1,j) for j in range(2,n+1))):
        par=[0,0]+list(parents)
        for mask in range(1<<(n-1)):
            configurations+=1
            yes=mask.bit_count()
            prob=p**yes*(1-p)**(n-1-yes)
            conn=[False]*(n+1);conn[1]=True
            boundary=0
            for j in range(2,n+1):
                good=bool(mask&(1<<(j-2)))
                if conn[par[j]] and not good:boundary+=1
                conn[j]=conn[par[j]] and good
            size=sum(conn)
            d=boundary-(1-p)/p*(size-1)
            for k,v in enumerate((size,boundary,size*size,boundary*boundary,size*boundary,d,d*d)):
                numer[k]+=prob*v
    count=factorial(n-1)
    return [x/count for x in numer]

def formula(n,p):
    mu=F(1); mm=F(1)
    for j in range(2,n+1):
        k=j-1
        mm=(1+2*p/k)*mm+p*mu/k
        mu=(1+p/k)*mu
    v=mm-mu*mu
    h=sum((F(1)/(k+p) for k in range(1,n)),F(0))
    cov=(1-p)/p*v-(1-p)*mu*h
    return mu,v,cov,h

for p in (F(1,4),F(1,2),F(4,5)):
    for n in range(2,8):
        ec,eb,ec2,eb2,ecb,ed,ed2=exact(n,p)
        mu,v,cov,h=formula(n,p)
        check(ec,mu,'root mean')
        check(ec2-ec*ec,v,'root variance')
        check(eb,(1-p)/p*(mu-1),'boundary mean')
        check(ecb-ec*eb,cov,'cross covariance')
        check(ed,0,'compensated martingale mean')
        check(ed2,(1-p)/(p*p)*(mu-1),'compensated martingale variance')
        check((ecb-ec*eb)-(1-p)/p*v,-(1-p)*mu*h,'negative correction')

# Dense exact finite sign sweep: verify one transition for a range of p.
for p in [F(j,20) for j in range(1,20)]:
    values=[]
    for n in range(2,250):
        mu,v,cov,h=formula(n,p)
        values.append(cov)
    # All grid cases have crossed by the finite sweep endpoint.
    assert values[0]<0 and values[-1]>0
    first=next(i for i,x in enumerate(values) if x>=0)
    check(all(x<0 for x in values[:first]) and all(x>=0 for x in values[first:]),True,'one crossing')
    check(all(x>0 for x in values[first+1:]),True,'strict post-crossing')
print(f'VERIFY_OK configurations={configurations} assertions={assertions}')

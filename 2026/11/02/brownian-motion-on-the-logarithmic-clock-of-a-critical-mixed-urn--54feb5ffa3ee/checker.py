#!/usr/bin/env python3
"""Exact finite-state check of the centered mixed-urn drift and bracket identities."""
from fractions import Fraction as F
from collections import defaultdict

def branches(y1, y2, a, b, c, p):
    total=y1+y2
    for replacement, pr in ((1,p),(0,1-p)):
        for sign, drawprob in ((1,F(y1,total)),(-1,F(y2,total))):
            amount=(a-b if replacement else c)
            totadd=(a+b if replacement else c)
            yy=(y1+(a if sign==1 else b), y2+(b if sign==1 else a)) if replacement else (y1+(c if sign==1 else 0),y2+(c if sign==-1 else 0))
            yield pr*drawprob, yy, amount*sign, totadd

def verify(a,b,c,p,levels=6):
    p=F(p); h=p*(a-b)+(1-p)*c; mu=p*(a+b)+(1-p)*c
    q=p*(a-b)**2+(1-p)*c*c
    assert 2*h==mu, (a,b,c,p,h,mu)
    states={(1,1): F(1)}
    assertions=0
    for n in range(levels+1):
        nextstates=defaultdict(F)
        for (x,y),weight in states.items():
            u=x-y; total=x+y; phi=F(u,total)
            triples=list(branches(x,y,a,b,c,p))
            assert sum(prob for prob,_,_,_ in triples)==1;assertions+=1
            meanstep=sum(prob*step for prob,_,step,_ in triples)
            assert meanstep==h*phi;assertions+=1
            var=sum(prob*(step-h*phi)**2 for prob,_,step,_ in triples)
            assert var==q-h*h*phi*phi;assertions+=1
            second=sum(prob*(u+step)**2 for prob,_,step,_ in triples)
            assert second==(1+F(2*h,total))*u*u+q;assertions+=1
            for prob, yy, step, add in triples:
                assert sum(yy)==total+add;assertions+=1
                assert yy[0]-yy[1]==u+step;assertions+=1
                nextstates[yy]+=weight*prob
        assert sum(states.values())==1;assertions+=1
        states=nextstates
    return assertions, len(states), q, mu

if __name__=='__main__':
    for args in ((1,1,1,F(1,3)),(1,2,3,F(3,8)),(2,1,4,F(4,5)),(1,3,2,F(2,10))):
        a,b,c,p=args
        if p>=1 or 4*b*p != p*(a+b)+(1-p)*c: continue
        n,count,q,mu=verify(*args)
        print('case',args,'assertions',n,'last_states',count,'q',q,'mu',mu)

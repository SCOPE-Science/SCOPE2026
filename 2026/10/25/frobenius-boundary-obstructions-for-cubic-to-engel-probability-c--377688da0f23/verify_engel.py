"""Finite group-level tests for cubic/2-Engel comparison (Python 3 standard library)."""
from itertools import product

def multiplicative_order(a,q):
    x=1
    for k in range(1,q):
        x=x*a%q
        if x==1:return k
    raise AssertionError('not a unit')

def test(q,m):
    primitive=next(a for a in range(2,q) if multiplicative_order(a,q)==q-1)
    lam=pow(primitive,(q-1)//m,q)
    assert multiplicative_order(lam,q)==m
    powers=[pow(lam,k,q) for k in range(m)]
    el=list(product(range(q),range(m)))
    def mul(x,y):return ((x[0]+powers[x[1]]*y[0])%q,(x[1]+y[1])%m)
    def inv(x):return ((-powers[(-x[1])%m]*x[0])%q,(-x[1])%m)
    def com(x,y):return mul(mul(mul(inv(x),inv(y)),x),y)
    e=(0,0)
    cube=sum(mul(mul(x,x),x)==e for x in el)
    engel=sum(com(com(x,y),y)==e for x in el for y in el)
    assert engel == q*m*(q+m-1)
    assert cube == 2*q+1
    print(f'q={q}, m={m}, |G|={len(el)}, Engel-pairs={engel}, cube-elements={cube}, OK')

if __name__=='__main__':
    for q,m in ((7,3),(7,6),(13,3),(13,6),(13,12),(19,3),(19,6),(19,9),(19,18)):
        test(q,m)
    print('VERIFY_OK')

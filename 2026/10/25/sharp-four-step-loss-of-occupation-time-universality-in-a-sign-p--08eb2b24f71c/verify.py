"""Exact rational consistency checks for four-step sign-persistent occupation law.

The symbolic event classifications are justified in RESULT.md. This program
checks their algebraic combination and boundary cases; it does not replace
those probability arguments or independently establish historical priority.
"""
from fractions import Fraction as F
from itertools import product

SIGNS4 = ['++++','+++-','++-+','++--','+-++','+-+-','+--+','+---']

def p2_cond(word, u, v):
    return dict(zip(SIGNS4, [F(0),F(0),u,v,v-u,F(3,8)-v,F(1,4),F(1,2)-v]))[word]

def p4_cond(word, u, v):
    return dict(zip(SIGNS4, [F(1),F(1)-u,F(1)-v,F(1,2),F(1,2),F(3,8),v,u]))[word]

def weight(word,q):
    same=sum(word[i]==word[i-1] for i in range(1,len(word)))
    return q**same*(1-q)**(len(word)-1-same)

def exact4(q,u,v):
    assert 0<=u<=v<F(1,3)
    a=sum((weight(s,q)*p4_cond(s,u,v) for s in SIGNS4),F(0))/2
    b=sum((weight(s,q)*p2_cond(s,u,v) for s in SIGNS4),F(0))
    return a,b

def predicted4(q,v):
    a=(5*q**3-3*q**2+3*q+3)/16
    b=(1-q)*(3-4*q+5*q**2)/8+v*(1-q)**2*(2*q-1)
    return a,b

checks=0
for den in (4,5,7,11,20):
    for k in range(den+1):
        q=F(k,den)
        for u,v in ((F(0),F(0)),(F(1,8),F(1,4)),(F(1,30),F(3,10)),(F(1,20),F(1,6))):
            a,b=exact4(q,u,v)
            assert (a,b)==predicted4(q,v)
            probs=[a,(1-2*a-b)/2,b,(1-2*a-b)/2,a]
            assert sum(probs)==1
            assert all(0<=x<=1 for x in probs)
            checks+=3
        if q in (F(1,2),F(1)):
            assert predicted4(q,F(0))==predicted4(q,F(1,4))
            checks+=1
# Explicit independent exact event calculations: for an Exp(1) magnitude,
# P(X>Y+Z)=E(exp(-(Y+Z)))=1/4; for uniform (1,3/2), X<Y+Z always.
assert predicted4(F(0),F(0))[1]==F(3,8)
assert predicted4(F(0),F(1,4))[1]==F(1,8)
assert predicted4(F(1,2),F(0))[1]==F(9,64)
assert predicted4(F(1,2),F(1,4))[0]==F(35,128)
assert predicted4(F(1),F(0))==(F(1,2),F(0))
checks+=5
# n=2 and n=3 laws, and their symmetries and endpoint consistency.
for den in (4,7,11):
    for k in range(den+1):
        q=F(k,den)
        ps2=[(1+q)/4,(1-q)/2,(1+q)/4]
        ps3=[(1+q*q)/4,(1-q*q)/4,(1-q*q)/4,(1+q*q)/4]
        assert sum(ps2)==1 and sum(ps3)==1
        assert all(x>=0 for x in ps2+ps3)
        checks+=2
print('EXACT_RATIONAL_CHECKS_OK',checks)

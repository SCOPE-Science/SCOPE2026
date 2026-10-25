"""Reproducibility checks for a fixed-composition scattered-subsequence extremum.
Run with Python 3: python check.py .  No third-party packages needed.
"""
from itertools import combinations

def subsequences_dp(word):
    total = 1
    prior = {}
    for symbol in word:
        old = total
        total = 2*total-prior.get(symbol,0)
        prior[symbol] = old
    return total

def subsequences_direct(word):
    result = {''}
    for symbol in word:
        result |= {v+symbol for v in tuple(result)}
    return len(result)

def f(a,b,c,d):
    x,y,z,t = a+2,b+2,c+2,d+2
    return x*y*z*t-x*y-x*t-z*t

def canonical(m):
    t,r=divmod(m,4)
    if r==0:return [(t,t,t,t)]
    if r==1:return [(t,t,t+1,t),(t,t+1,t,t)]
    if r==2:return [(t,t+1,t+1,t)]
    return [(t,t+1,t+1,t+1),(t+1,t+1,t+1,t)]

def predicted(m):
    t,r=divmod(m,4)
    if r==0:return (t+2)**2*(t*t+4*t+1)
    if r==1:return (t+2)*(t**3+7*t*t+13*t+5)
    if r==2:return (t+2)*(t**3+8*t*t+18*t+10)
    return (t+1)*(t+3)*(t*t+7*t+11)

def balanced(p,q):
    return (p//2,(q+1)//2,q//2,(p+1)//2)

def shift_delta(r,s,e,h):
    return f(r+1,s-1+h,s-1,r+1+e)-f(r,s+h,s,r+e)

def main():
    checked=0; direct=0
    for m in range(0,35):
        maximum=-1; argmax=[]
        for a in range(m+1):
            for b in range(m-a+1):
                for c in range(m-a-b+1):
                    d=m-a-b-c
                    word='0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d
                    actual=subsequences_dp(word)
                    assert actual==f(a,b,c,d),(a,b,c,d,actual,f(a,b,c,d))
                    if m<=7:
                        assert subsequences_direct(word)==actual
                        direct+=1
                    if actual>maximum:maximum=actual;argmax=[]
                    if actual==maximum:argmax.append((a,b,c,d))
                    checked+=1
        assert maximum==predicted(m),(m,maximum,predicted(m))
        assert sorted(argmax)==sorted(canonical(m)),(m,argmax,canonical(m))
    # Sign table checks as finite diagnostics, not substitutes for the algebraic proof.
    for r in range(0,50):
        for s in range(1,60):
            for e in (0,1):
                for h in (0,1):
                    delta=shift_delta(r,s,e,h)
                    if (e,h)==(0,1):
                        sign = 1 if s>=r+1 and r>0 or s>=r+2 else (0 if s==r+1 and r==0 else -1)
                    else:sign = 1 if s>=r+2 else -1
                    assert (delta>0)-(delta<0)==sign,(r,s,e,h,delta,sign)
    print('OK; quadruples checked:',checked,'direct set enumerations:',direct,
          'maximum m=34:',predicted(34), 'maximizers:',canonical(34))

if __name__=='__main__':main()

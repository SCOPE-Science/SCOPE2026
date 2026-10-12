"""Finite-field checks for unit-plus-involution additive decomposition counts.
Run with Python 3; no third-party modules.
The mathematical proof, not finite tests, establishes the unrestricted theorem.
"""
from itertools import product
from collections import Counter


def field(p, degree):
    if degree == 1:
        q = p
        return (q, lambda a,b:(a+b)%p,
                lambda a,b:(a*b)%p,
                lambda a:pow(a,-1,p),
                lambda a:(1 if pow(a,(q-1)//2,p)==1 else -1) if a else 0)
    assert p == 3 and degree == 2
    q = 9    # F_3[x]/(x^2+1): x^2=2
    def add(a,b): return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    def mul(a,b):
        x,y=a%3,a//3
        z,w=b%3,b//3
        return (x*z+2*y*w)%3+3*((x*w+y*z)%3)
    def power(a,n):
        r=1
        for _ in range(n):r=mul(r,a)
        return r
    def inv(a):return power(a,7)
    def char(a):
        if a==0:return 0
        return 1 if power(a,4)==1 else -1
    return q,add,mul,inv,char


def check(p,degree):
    q,add,mul,inv,char=field(p,degree)
    neg=lambda a: add(0,mul(p-1,a))
    sub=lambda a,b:add(a,neg(b))
    one=1;zero=0
    def det(A):return sub(mul(A[0],A[3]),mul(A[1],A[2]))
    def mmul(A,B):
        return (add(mul(A[0],B[0]),mul(A[1],B[2])),
                add(mul(A[0],B[1]),mul(A[1],B[3])),
                add(mul(A[2],B[0]),mul(A[3],B[2])),
                add(mul(A[2],B[1]),mul(A[3],B[3])))
    mats=list(product(range(q),repeat=4))
    invol=[V for V in mats if mmul(V,V)==(one,zero,zero,one)]
    assert len(invol)==q*(q+1)+2
    half=inv(2)
    spectrum=Counter()
    min_count=0
    for A in mats:
        t=add(A[0],A[3]);d=det(A)
        a=mul(t,half)
        B=(sub(A[0],a),A[1],A[2],sub(A[3],a))
        E=int(sub(add(d,one),t)!=0)+int(add(add(d,one),t)!=0)
        if B==(0,0,0,0):
            expected=q*(q+1)*int(d!=one)+E
        else:
            delta=sub(mul(a,a),d)
            lam=mul(sub(one,d),half)
            if delta==0:
                H=2*q if lam==0 else q
            else:
                chi=char(delta)
                H=q-chi+(q*chi if mul(lam,lam)==delta else 0)
            expected=q*(q+1)-H+E
            assert expected>=q*q-q+1
            if expected==q*q-q+1:
                min_count+=1
                # An involution or a nontrivial size-two Jordan block at +/-1.
                is_invol=mmul(A,A)==(1,0,0,1)
                jordan=(d==1 and (t==2 or t==neg(2)) and
                        A!=(one,0,0,one) and A!=(neg(one),0,0,neg(one)))
                assert is_invol or jordan,(q,A)
        actual=sum(1 for V in invol if det(tuple(sub(A[i],V[i]) for i in range(4)))!=0)
        assert actual==expected,(q,A,actual,expected)
        spectrum[actual]+=1
    assert spectrum[1]==2
    assert min_count==3*q*q+q-2,(q,min_count)
    print(f'q={q}: all {q**4} matrices, {len(invol)} involutions, minimum count {min_count}, distinct fiber sizes {len(spectrum)}')

if __name__=='__main__':
    for args in [(3,1),(5,1),(7,1),(11,1),(3,2)]:check(*args)
    print('VERIFY_OK')

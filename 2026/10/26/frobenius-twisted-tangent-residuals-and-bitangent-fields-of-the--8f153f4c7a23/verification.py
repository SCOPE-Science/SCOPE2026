"""Pure-Python finite-polynomial verification of bitangent splitting over F3."""
from itertools import product
P=3
def norm(a):
    a=list(a)
    while a and a[-1]%P==0: a.pop()
    return tuple(v%P for v in a)
def add(a,b):
    return norm([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a): return norm([-v for v in a])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return norm(out)
def divmodp(a,b):
    assert b
    a=list(norm(a)); b=norm(b); out=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        shift=len(a)-len(b); lead=a[-1]*pow(b[-1],-1,P)%P; out[shift]=lead
        for j,v in enumerate(b): a[shift+j]=(a[shift+j]-lead*v)%P
        a=list(norm(a))
    return norm(out),norm(a)
def mod(a,b): return divmodp(a,b)[1]
def gcd(a,b):
    while b: a,b=b,mod(a,b)
    return norm([v*pow(a[-1],-1,P) for v in a]) if a else ()
def power(a,n,m):
    z=(1,)
    while n:
        if n&1:z=mod(mul(z,a),m)
        a=mod(mul(a,a),m);n>>=1
    return z
def expr(coeffs):return norm(coeffs)
def xm1(n):return norm([-1]+[0]*(n-1)+[1])
def verify():
    # x^28 + x^21 +1
    target=norm([1]+[0]*20+[1]+[0]*6+[1])
    fs=[(-1,1),(-1,-1,0,1),(1,0,0,1,1,0,1),
        (1,1,1,-1,0,1,1),(1,1,1,1,1,1,1),
        (1,1,-1,0,1,-1,1)]
    # Verify factorization and Rabin irreducibility exactly
    acc=(1,)
    for f in fs:
        f=norm(f)
        acc=mul(acc,f)
        d=len(f)-1
        x=(0,1)
        if d>1:
            for p in [2,3]:
                if d%p==0:
                    assert gcd(f,sub(power(x,3**(d//p),f),x))==(1,), ('proper factor',f)
            assert sub(power(x,3**d,f),x)==() or mod(sub(power(x,3**d,f),x),f)==(), ('non-rabin',f)
    assert acc==target, ('product',acc,target)
    assert mod(xm1(91),target)==(), 'g not divisor of t^91-1'
    deriv=norm([i*v for i,v in enumerate(target)][1:])
    assert gcd(target,deriv)==(1,), 'nonreduced hyperflex scheme'
    assert sorted([len(f)-1 for f in fs])==[1,3,6,6,6,6]
    for n in (1,2,3,4,5,6,9,12):
        # Degree of gcd(g,u^(3^n)-u) counts rational hyperflexes.
        roots=len(gcd(target,sub(power((0,1),3**n,target),(0,1))))-1
        formula=1+(3 if n%3==0 else 0)+(24 if n%6==0 else 0)
        assert roots==formula, (n,roots,formula)
    print('VERIFY_OK', 'factor_degrees=1,3,6,6,6,6', 'cycle_type=1^1 3^1 6^4', 'reduced=28')
if __name__=='__main__':verify()

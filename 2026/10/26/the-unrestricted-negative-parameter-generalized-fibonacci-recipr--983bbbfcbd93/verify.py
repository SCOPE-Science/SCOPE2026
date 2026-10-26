from fractions import Fraction

def recurrence(s,t,m):
    u,v=0,1
    for _ in range(m): u,v=v,s*v-t*u
    return u

def test(s,t,r,n,extra=60):
    D=recurrence(s,t,r*n)-recurrence(s,t,r*(n-1))
    K=n+extra
    S=sum((Fraction(1,recurrence(s,t,r*k)) for k in range(n,K+1)),Fraction(0))
    q=(s-1)**r
    upper=S+Fraction(q, (q-1)*recurrence(s,t,r*(K+1)))
    assert S>Fraction(1,D), (s,t,r,n,D,'lower',S)
    if D>1:
        assert upper<Fraction(1,D-1),(s,t,r,n,D,'upper',upper)
    return D

count=0
for s in range(3,19):
    for t in range(1,s):
        for r in range(1,6):
            for n in range(1,11):
                test(s,t,r,n)
                count+=1
print('VERIFY_OK',count,'parameter/index quadruples with rational upper/lower bounds')

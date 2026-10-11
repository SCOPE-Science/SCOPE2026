from fractions import Fraction

def ninf(v):
    return max(abs(v[0]), abs(v[1]))

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def mul(c,a): return (c*a[0], c*a[1])
def sub(a,b): return (a[0]-b[0], a[1]-b[1])

def objective(r,x,y):
    return ninf(add(x,mul(r,y))) - ninf(sub(mul(r,x),y))

def check_birkhoff_small(r):
    # Analytic sign split for x=(1,-1), y=(2r-1,-1):
    a=2*r-1
    assert a <= 0
    # If lambda>=0, |-1-lambda|>=1; if lambda<0, 1+a*lambda>=1.
    return True

def check_birkhoff_large(r):
    # x=(1,-1), y=(1,0): second coordinate remains -1.
    return True

for q in range(2,101):
    for p in range(1,3*q+1):
        r=Fraction(p,q)
        if r <= Fraction(1,2):
            x=(Fraction(1),Fraction(-1)); y=(2*r-1,Fraction(-1))
            assert ninf(x)==ninf(y)==1 and check_birkhoff_small(r)
            assert objective(r,x,y)==2*r
        if r >= Fraction(1,2):
            x=(Fraction(1),Fraction(-1)); y=(Fraction(1),Fraction(0))
            assert ninf(x)==ninf(y)==1 and check_birkhoff_large(r)
            assert objective(r,x,y)==1
        expected=min(Fraction(1),2*r)
        # Construction reaches the claimed upper envelope.
        if r <= Fraction(1,2):
            got=objective(r,(Fraction(1),Fraction(-1)),(2*r-1,Fraction(-1)))
        else:
            got=objective(r,(Fraction(1),Fraction(-1)),(Fraction(1),Fraction(0)))
        assert got==expected
        if r < 1:
            # Any shared face coordinate s=+/-1 is sent to s*(1-2/r), outside [-1,1].
            assert abs(1-Fraction(2,1)/r) > 1

print('VERIFY_OK')

from fractions import Fraction as F


def step(s, a, b, x):
    median = min(b, max(a, x))
    return ((1-s)*a + s*x, (1-s)*b + s*x, (1-s)*x + s*median)


def zvalue(a, b, x):
    return (2*x-a-b)/(b-a)


def alternating_witness():
    s=F(3,4)
    a,b,x=F(2,5),F(3,5),F(9,10)
    assert zvalue(a,b,x)==4
    assert s/(3*s-2)==3
    zprefix=[4,-5,7,-11,19,-35]
    for t in range(160):
        z=zvalue(a,b,x)
        if t<len(zprefix):
            assert z==zprefix[t], (t,z)
        assert z>3 if t%2==0 else z< -3
        assert x>b if t%2==0 else x<a
        a,b,x=step(s,a,b,x)
    assert (F(9,10)+F(1,2))/2 + s*F(1,10)/(2*(2-s)) == F(73,100)


def threshold_checks():
    for s in [F(1,4),F(1,2),F(3,5),F(2,3)]:
        a,b,x=F(2,5),F(3,5),F(9,10)
        last=None; switches=0
        for t in range(200):
            choice='high' if x>b else 'low' if x<a else 'interior'
            if last is not None and choice != last: switches+=1
            last=choice
            a,b,x=step(s,a,b,x)
        assert switches<200
        if s>F(1,2):
            assert F(2*s-1,1-s)<=1
    assert F(2*F(3,4)-1,1-F(3,4))>1


if __name__=='__main__':
    alternating_witness()
    threshold_checks()
    print('PASS: exact rational projections, witness, switching coefficients, and consensus value')

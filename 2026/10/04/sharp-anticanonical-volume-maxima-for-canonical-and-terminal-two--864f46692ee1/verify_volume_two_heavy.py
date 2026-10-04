from fractions import Fraction


def vol(r,a,b):
    n=r+1
    return Fraction((r+a+b)**n, a*b)

def canonical(r,a,b):
    d=b-a
    return 0 <= d <= r and 1 <= a <= r+d

def terminal(r,a,b):
    d=b-a
    return 0 <= d < r and 1 <= a < r+d

for r in range(2,101):
    can=[]; ter=[]
    # box contains all canonical possibilities, plus margin
    for a in range(1,2*r+3):
        for b in range(a,3*r+4):
            if canonical(r,a,b): can.append((vol(r,a,b),a,b))
            if terminal(r,a,b): ter.append((vol(r,a,b),a,b))
    cm=max(v for v,_,_ in can)
    ctarget=Fraction(6**r * r**(r-1),1)
    assert cm==ctarget, (r,cm,ctarget)
    ceq={(a,b) for v,a,b in can if v==cm}
    expected={(2*r,3*r)} if r>=3 else {(1,3),(4,6)}
    assert ceq==expected,(r,ceq,expected)
    tm=max(v for v,_,_ in ter)
    if r==2:
        ttarget=Fraction(64,1); texpect={(1,1)}
    else:
        ttarget=Fraction((6*r-5)**(r+1),6*(r-1)**2)
        texpect={(2*r-2,3*r-3)}
    assert tm==ttarget,(r,tm,ttarget)
    teq={(a,b) for v,a,b in ter if v==tm}
    assert teq==texpect,(r,teq,texpect)
print('VERIFY_OK r=2..100')

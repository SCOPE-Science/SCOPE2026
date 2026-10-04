from math import isqrt


def fundamental_pell(d):
    a0=isqrt(d)
    if a0*a0==d:
        return None
    m=0; den=1; a=a0
    p0,p1=1,a
    q0,q1=0,1
    while p1*p1-d*q1*q1 != 1:
        m=den*a-m
        den=(d-m*m)//den
        a=(a0+m)//den
        p0,p1=p1,a*p1+p0
        q0,q1=q1,a*q1+q0
    return p1,q1


def seq(a,y,n):
    X0,Y0=1,0
    X1,Y1=a,y
    if n==0: return X0,Y0
    if n==1: return X1,Y1
    for _ in range(1,n):
        X0,X1=X1,2*a*X1-X0
        Y0,Y1=Y1,2*a*Y1-Y0
    return X1,Y1


def fx(a,b,n):
    bn=pow(b,n)
    den=bn*bn-2*a*bn+1
    num=pow(b,n*n+2*n)-a*pow(b,n*n+n)
    return (num//den) % bn


def fy(a,y,b,n):
    bn=pow(b,n)
    den=bn*bn-2*a*bn+1
    num=y*pow(b,n*n+n)
    return (num//den) % bn

cases=0
below_x=below_y=0
threshold_checks=0
for d in range(2,200):
    sol=fundamental_pell(d)
    if sol is None: continue
    a,y=sol
    if a>50: continue
    bx=2*a*(a+1)-1
    by=2*a*(y+1)
    assert by < bx
    # Every smaller base in the positive-denominator domain fails by n<=2.
    for b in range(2*a,bx):
        X1,_=seq(a,y,1); X2,_=seq(a,y,2)
        if fx(a,b,1)==X1 and fx(a,b,2)==X2:
            raise AssertionError(("X smaller base survived",d,a,y,b,bx))
        below_x += 1
    for b in range(2*a,by):
        _,Y1=seq(a,y,1); _,Y2=seq(a,y,2)
        if fy(a,y,b,1)==Y1 and fy(a,y,b,2)==Y2:
            raise AssertionError(("Y smaller base survived",d,a,y,b,by))
        below_y += 1
    # Threshold and the next two bases agree through n=8.
    for b in (bx,bx+1,bx+2):
        for n in range(1,9):
            X,_=seq(a,y,n)
            assert fx(a,b,n)==X, ("X threshold",d,a,y,b,n)
            threshold_checks += 1
    for b in (by,by+1,by+2):
        for n in range(1,9):
            _,Y=seq(a,y,n)
            assert fy(a,y,b,n)==Y, ("Y threshold",d,a,y,b,n)
            threshold_checks += 1
    cases += 1

print(f"VERIFY_OK pell_cases={cases} below_x={below_x} below_y={below_y} threshold_checks={threshold_checks}")

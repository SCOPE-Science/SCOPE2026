from fractions import Fraction as F

def p(h):
    return h**5+30*h**4+180*h**3+360*h**2+180*h-72

def D(h): return h*h+4*h+6

def c0(h): return 2*(3-h)/D(h)
def c1(h): return -2*h*(h*h-6*h-18)/D(h)**2
def c2(h): return -2*h*h*(h+3)*(h*h-12*h-18)/D(h)**3
def c3(h): return -2*h**3*(h**4-12*h**3-108*h*h-216*h-108)/D(h)**4
def c4(h): return -2*h**4*(h**5-15*h**4-180*h**3-540*h*h-540*h-108)/D(h)**5

def tail(h,m):
    cs=[c0(h),c1(h),c2(h),c3(h),c4(h)]
    return F(1)-sum(cs[:m],F(0))

def t1(h): return h*(h+6)/D(h)
def t2(h): return h*h*(h*h+12*h+18)/D(h)**2
def t3(h): return h**3*(h**3+18*h*h+54*h+36)/D(h)**3
def t4(h): return h**4*(h**4+24*h**3+108*h*h+144*h+36)/D(h)**4
def t5(h): return h**5*p(h)/D(h)**5

for h in [F(0),F(1,5),F(1,4),F(1,2),F(1),F(3)]:
    assert tail(h,1)==t1(h)
    assert tail(h,2)==t2(h)
    assert tail(h,3)==t3(h)
    assert tail(h,4)==t4(h)
    assert tail(h,5)==t5(h)

assert p(F(2539,10000)) < 0 < p(F(127,500))
assert t5(F(1,4)) == F(-1607,18424351793)
assert t5(F(1,2)) == F(4237,39135393)
for h in [F(0),F(1,4),F(1,2),F(1),F(2),F(3)]:
    assert c0(h)>=0 and c1(h)>=0 and c2(h)>=0 and c3(h)>=0 and c4(h)>=0
    assert t1(h)>=0 and t2(h)>=0 and t3(h)>=0 and t4(h)>=0
assert c0(F(4))<0
print('VERIFY_OK')

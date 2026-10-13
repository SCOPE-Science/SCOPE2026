import math

p=0.9
m=0.0
z=0.9
R=math.hypot(p,m)
CR=0.5*((1+R)*math.log((1+R)/2)+(1-R)*math.log((1-R)/2))

def D(x):
    q=math.hypot(x,z)
    return CR-0.5*math.log((1-q*q)/4)-(p*x+m*z)*math.atanh(q)/q

def dD(x):
    q=math.hypot(x,z)
    M=p*x+m*z
    return x/(1-q*q)-p*math.atanh(q)/q-x*M*(q/(1-q*q)-math.atanh(q))/(q**3)

lo=0.255924326127
hi=0.255924326128
assert dD(lo) < 0 < dD(hi)
for _ in range(100):
    mid=(lo+hi)/2
    if dD(mid) < 0:
        lo=mid
    else:
        hi=mid
x=(lo+hi)/2
val=D(x)
assert abs(x-0.2559243261276991) < 5e-13
assert abs(val-1.1173300547617506) < 5e-13
K=0.5*math.log(0.5/0.95)+0.5*math.log(0.5/0.05)
saving=1-K/val
assert abs(K-0.8303656034108255) < 5e-15
assert abs(saving-0.2568305131755494) < 5e-13
assert abs(0.45/val-0.40274581184156366) < 5e-13
assert abs(0.45/K-0.5419299621173751) < 5e-13
print('x_star=%.15f' % x)
print('D_inf=%.15f' % val)
print('K_inf=%.15f' % K)
print('saving=%.15f' % saving)
print('VERIFY_OK')

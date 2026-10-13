from fractions import Fraction as F
import math

def add(a,b):
    n=max(len(a),len(b)); c=[F(0) for _ in range(n)]
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return c

def mul(a,b):
    c=[F(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def scale(a,s): return [s*x for x in a]

def shift(a,n): return [F(0)]*n+a

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

# y_minus = z(1-z/6)^2
yminus=mul([F(0),F(1)], mul([F(1),-F(1,6)],[F(1),-F(1,6)]))
three_minus_y=add([F(3)],scale(yminus,-1))
left=mul(yminus,three_minus_y)
right=mul([F(0),F(1)], add([F(3)],scale(yminus,-2)))
diff=trim(add(left,scale(right,-1)))
p=[F(-108),F(144),F(-24),F(1)]
expected=scale(shift(p,3),-F(1,1296))
assert trim(diff)==trim(expected)
assert sum(p[i]*F(5,8)**i for i in range(len(p))) == -F(13891,512)

# y_plus = z(1-z/6+z^2/120)^2
yplus=mul([F(0),F(1)], mul([F(1),-F(1,6),F(1,120)],[F(1),-F(1,6),F(1,120)]))
H=add(mul([F(0),F(0),F(3)], [F(1)]), scale(mul([F(0),F(0),F(1)],yplus),-2))
H=add(H,scale(mul(yplus,yplus),-3))
Q=[F(-4608000),F(-1152000),F(438400),F(-51200),F(2880),F(-80),F(1)]
expectedH=scale(shift(Q,4),-F(1,69120000))
assert trim(H)==trim(expectedH)
assert F(1)+F(450)+F(171250)-F(4608000) < 0

# Regression samples of the theorem; not the infinite proof.
for N in range(2,401):
    for k in range(1,N//2+1):
        th=k*math.pi/N
        exact=(k*math.pi)**2
        L=2*N*N*(1-math.cos(th))
        C=6*N*N*(1-math.cos(th))/(2+math.cos(th))
        G=math.sqrt(L*C)
        A=(L+C)/2
        assert G < exact < A
print('VERIFY_OK')

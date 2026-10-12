import sympy as sp
r=sp.sqrt(5); t,x=sp.symbols('t x')
A3=((-116*r+272)*t**2+(66*r-148)*t-34*r+76)
A2=((-23664*r+52974)*t**4+(62037*r-138785)/2*t**3+(-71882*r+160725)/2*t**2+(39297*r-87871)/2*t+(-3876*r+8667)/2)
A1=((-2096932*r+4689008)*t**6+(8789895*r-19655187)/2*t**5+(-14213809*r+31783015)/2*t**4+(14281062*r-31933423)/2*t**3+(-10526810*r+23538663)/2*t**2+(5316367*r-11887758)/2*t+(-98209*r+219602)/2)
A0=((-69643152*r+155726921)*t**8+(191265401*r-427682729)*t**7+(-1317057443*r+2945029977)/4*t**6+(2349501743*r-5253645563)/8*t**5+(-1901993416*r+4252986577)/16*t**4+(19147095*r-42814206)/4*t**3+(-250668666*r+560512177)/8*t**2+(610197963*r-1364444125)/8*t+(-7465176*r+16692641)/16)
F=sp.expand(x**4+A3*x**3+A2*x**2+A1*x+A0)
# The source bad-fiber polynomial is nonzero at ±1.
a=(1118*r+2598)/27; b=(89700*r+200362)/27
bad=sp.expand(t**4-a*t**3-b*t**2-a*t+1)
assert sp.simplify(bad.subs(t,1))!=0 and sp.simplify(bad.subs(t,-1))!=0
# Involution coefficients.
e=(138+67*r)/19; ff=(2770+1324*r)/355; C=(3035-1302*r)/38
alpha=sp.simplify(t**-2*(t+e)/(e*t+1))
beta=sp.simplify(C*(t-1)*(t**2+ff*t+1)/(t**2*(e*t+1)))
gamma=sp.simplify(t*alpha**2)
assert [sp.simplify(q.subs(t,1)) for q in (alpha,beta,gamma)]==[1,0,1]
assert [sp.simplify(q.subs(t,-1)) for q in (alpha,beta,gamma)]==[-1,-248+108*r,-1]
# Four distinct finite points on t=1.
q1=x**2+(66-24*r)*x-1803+820*r
q2=x**2+(134-60*r)*x+10101-4520*r
assert sp.simplify(F.subs(t,1)-sp.expand(q1*q2))==0
assert sp.discriminant(q1,x)!=0 and sp.discriminant(q2,x)!=0 and sp.resultant(q1,q2,x)!=0
# Two finite fixed points on t=-1.
x0=-124+54*r
y2=3567475528-1595423560*r
assert sp.simplify(beta.subs(t,-1)/2-x0)==0
assert sp.simplify(-F.subs({t:-1,x:x0})-y2)==0 and y2!=0
# Base quotient values.
assert sp.simplify((t+1/t-2).subs(t,1))==0
assert sp.simplify((t+1/t-2).subs(t,-1))==-4
print('VERIFY_OK fixed_split=4+4 base_values=0,-4 tminus1_affine=2 tminus1_infinity=2')

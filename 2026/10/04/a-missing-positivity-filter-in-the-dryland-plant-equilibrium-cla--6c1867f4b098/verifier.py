from fractions import Fraction as Q

# Exact witness for the source theorem's case (ii).
a=b=d=m=Q(1)
c=Q(-3)
assert a>0 and b>0 and d>0 and m>c and b==a

u=(m-c)/(1+d)
p=a+m*u-u*u
q=b+c*u+d*u*u
assert u==2
assert p==q==Q(-1)
v=1/p
assert v==Q(-1) and v<0

# Both equilibrium residuals vanish exactly, but the state is not positive.
du=u*(p*v-1)
dv=1-q*v
assert du==0 and dv==0

# Reduced quadratic and branch feasibility numerator.
F=(1+d)*u*u+(c-m)*u+(b-a)
assert F==0
A=a*(1+d)**2+(m-c)*(m*d+c)
assert A==Q(-4)
assert p*(1+d)**2==A

# For this witness F(u)=2u(u-2): only the positive root u=2 exists,
# and its water coordinate is negative.
roots=[Q(0),Q(2)]
positive_feasible=[]
for r in roots:
    if r>0:
        denom=a+m*r-r*r
        if denom>0:
            positive_feasible.append((r,1/denom))
assert positive_feasible==[]

print('VERIFY_OK')

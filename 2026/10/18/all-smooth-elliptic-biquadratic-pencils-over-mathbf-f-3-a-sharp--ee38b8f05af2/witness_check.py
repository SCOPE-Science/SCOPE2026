"""Exact four-member verification of an extremal biquadratic pencil over F_3."""
import sympy as sp
U,V,S,T = sp.symbols('U V S T')
monomials = [a*b for a in [U**2,U*V,V**2] for b in [S**2,S*T,T**2]]
P1 = [(1,0),(0,1),(1,1),(1,2)]
F = [1,0,0,2,0,1,2,0,0]
G = [0,1,0,1,0,0,2,0,1]
for name,k in [('F',0),('G',-1),('F+G',1),('F+2G',2)]:
    coeff = F if k==0 else G if k==-1 else [(a+k*b)%3 for a,b in zip(F,G)]
    poly = sp.expand(sum(c*m for c,m in zip(coeff,monomials)))
    points=[]
    for i,(u,v) in enumerate(P1):
        for j,(s,t) in enumerate(P1):
            if int(poly.subs({U:u,V:v,S:s,T:t}))%3==0:points.append((i,j))
    for first,second in [(U,V),(V,U)]:
        for third,fourth in [(S,T),(T,S)]:
            sub={first:1,third:1}
            gb=sp.groebner([sp.diff(poly,x).subs(sub) for x in [U,V,S,T]], second,fourth,modulus=3)
            assert list(gb)==[sp.Integer(1)], (name,sub)
    print(name,'coefficients',coeff,'N',len(points),'point_indices',points)
    if name=='F':base=set(points)
    else:base &= set(points)
assert len(base)==3
print('COMMON BASE POINTS:',sorted(base))

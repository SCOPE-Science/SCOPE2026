"""Exact rational checks for the saturation identity and a fixed-norm obstruction.
This program checks finite algebraic examples; its finite tests do not replace the proof.
"""
from fractions import Fraction as F

def interaction(a,k,s,kind):
    if kind=='activation':
        return a*s/(k+s), a*k/(k+s)**2
    if kind=='inhibition':
        return a*k/(k+s), -a*k/(k+s)**2
    raise ValueError(kind)

checks=0
for a in [F(1,3),F(5,2),F(7,4)]:
    for k in [F(1,7),F(2,1),F(9,5)]:
        for s in [F(1,13),F(1,1),F(13,2)]:
            for kind in ['activation','inhibition']:
                h,dh=interaction(a,k,s,kind)
                assert h-s*abs(dh)==h*h/a
                assert 0<h<a
                checks+=1

edges=[(0,1,F(3,2),F(2), 'inhibition'),
       (1,2,F(5,4),F(3), 'activation'),
       (2,0,F(4,3),F(5), 'inhibition'),
       (1,0,F(2,3),F(7), 'activation')]
b=[F(0),F(0),F(1,3)]
for x in [(F(1,5),F(2,3),F(5,6)),(F(1),F(2),F(3)),(F(5,4),F(7,2),F(1,8))]:
    for i in range(3):
        f,q=b[i],b[i]
        derivative_absolute_sum=F(0)
        for ii,j,a,k,kind in edges:
            if ii != i: continue
            h,dh=interaction(a,k,x[j],kind)
            f+=h
            q+=h*h/a
            derivative_absolute_sum+=x[j]*abs(dh)
        assert (-f+derivative_absolute_sum)/x[i]==-q/x[i]
        assert q>0
        checks+=1

# For two mutually inhibitory nodes, original-reaction Jacobian at (1/10,1/10)
# has eigenvalue 19/18 > 0, precluding a uniform negative matrix measure
# in any constant norm on the entire positive orthant.
s=F(1,10)
positive_eigenvalue=-F(1,3)+F(2)/(1+2*s)**2
assert positive_eigenvalue==F(19,18)
checks+=1
# At the two-node equilibrium (1,1), the multiplicative box [1/2,2]^2
# has exact rate min_i q_i,min / U_i = (1/5)^2/2 = 1/50.
box_rate=(F(1)/(1+2*F(2)))**2/F(2)
assert box_rate==F(1,50)
checks+=1
print('PASS',checks,'exact rational identities; fixed-norm spectral obstacle',positive_eigenvalue)

# Exact certificate for the effective fifth-order bound
# Python 3 standard library only. All comparisons use rational arithmetic.
from fractions import Fraction as Q
D=Q(1,288)
rho=Q(3,50)
assert rho**2 >= D+Q(3,4)*D**2
R=Q(1,3)+D
E=18*D
P=3*(rho+Q(3,2)*D)
V=rho+D/2
W=R*(E+2*P)+Q(17,12)*D
X=R*(3*E+3*P)+Q(4,3)*D
terms=[Q(32,9)*D,8*(Q(2,3)*V+D/3),4*(W+Q(5,12)*D),2*V*(R+Q(1,3)),2*X]
S=sum(terms)
assert S == Q(830093,518400)
assert Q(46,27)-S > 0
print('Certified discrepancy bound:',str(S),' < 46/27')
print('Positive margin:',str(Q(46,27)-S))

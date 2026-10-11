from fractions import Fraction as Q

c=Q(331,206)
A=Q(514,345); B=Q(31,69)
C=Q(7,5)*c
q89=Q(89,100)
Qsum=Q(10379,6386)

# Mixed-region boundary S3(u)+S2(v)=C and lower endpoint u+v=c.
u0=Q(131583,144200)
v0=Q(100117,144200)
assert u0+v0==c
S2=lambda q:A-B*q
S3=lambda q:Q(20,11)-Q(9,11)*q
assert S3(u0)+S2(v0)==C
assert q89 < u0 < 1 and Q(1,5)<v0<q89
D32=lambda u,v:(Q(2827)*u+Q(3450)*v-Q(2405)*u*v)/(Q(11)*(Q(95)*v+Q(257)))
D0=D32(u0,v0)
assert D0==Q(18910336411,19465125400)
tau=1-D0
assert tau==Q(554788989,19465125400)

# Feasible geometry excludes the S3/S3 case.
assert 2*S3(q89) < C

# S2/S2 region. D is increasing in u, so only the two upper boundaries matter.
D22=lambda u,v:(Q(257)*(u+v)-Q(155)*u*v)/(Q(257)+Q(95)*v)
vmin=c-q89
vsplit=Qsum-q89
vmax=Qsum/2
assert Q(1,5)<vmin<vsplit<vmax<q89
# On u=89/100 the derivative in v is positive (constant positive numerator).
# On u=Qsum-v, derivative numerator P22 is increasing and still negative at vmax.
def P22(v): return Q(9403385)*v*v+Q(50877262)*v-Q(66685075)
assert P22(vmax)<0
D22max=D22(q89,vsplit)
assert D22max==Q(29270497,30250300)
assert D22max < D0

# Mixed S3/S2 region. D is increasing in u. The S-sum boundary is u=U(v).
U=lambda v:(Q(827521)-Q(351230)*v)/Q(639630)
vend=Q(234773,319300)
assert U(v0)==u0 and U(vend)==q89
# Along u=U(v), derivative sign has numerator P32, increasing for v>0;
# it remains negative through vend, hence D decreases on [v0,vend].
def P32(v): return Q(23532925)*v*v+Q(127325510)*v-Q(123687932)
assert P32(vend)<0
assert D32(U(vend),vend)<D0

# Sharpness: an explicit inward feasible direction gives m>c while D approaches D0.
# u(delta)=u0-delta, v(delta)=v0+6 delta/5.
d=Q(1,10**6)
u=u0-d; v=v0+Q(6,5)*d
assert u+v>c
assert S3(u)+S2(v)>C
assert D32(u,v)<D0
assert D0-D32(u,v) < Q(1,10**4)

print('c=',c, float(c))
print('Dstar=',D0, float(D0))
print('activation=',tau, float(tau))
print('S2S2_max=',D22max, float(D22max))
print('sharpness_sample_D=',D32(u,v), float(D32(u,v)))

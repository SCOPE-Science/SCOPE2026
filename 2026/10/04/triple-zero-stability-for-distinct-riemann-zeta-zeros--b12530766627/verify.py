from fractions import Fraction as F

delta=F(891,200000); m=347
Delta=(m-6)*delta; a=Delta/F(m); beta=F(6*(m-6),2736*m)
tau=F(1233,1000); c=F(3411,1000); H=F(3362285207,5000000000)
rh=8*c-10-c*c; rk=4*c-2-c*c
q3=(1+H-beta)/(2-a); gamma=F(2,1)/(2-a)
qsrc=F(16260119298029,19426831050000)
threshold=(qsrc-q3)/gamma
assert Delta==F(303831,200000)
assert a==F(303831,69400000)
assert beta==F(341,158232)
assert tau*tau-Delta==F(567,500000)>0
assert c==3+tau/3
assert c>=1+tau
assert rh-a==F(980049629,173500000)>0
assert rk-2*a==F(112103,347000000)>0
assert q3==F(165184514109253,197357040825000)
assert gamma==F(138800000,138496169)
# Exact obstruction for every m >= 348 in the same scheme.
m2=348; D2=(m2-6)*delta; a2=D2/F(m2); t0=F(12343,10000)
assert t0*t0 < D2
c0=3+t0/3
rk0=4*c0-2-c0*c0
assert rk0-2*a2==F(-23501321,26100000000)<0
# Since D_m and a_m increase with m, every admissible tau,c for m>=348
# has tau>t0, c>c0, and rk(c)<rk(c0) (c>2), so feasibility fails.
print('VERIFY_OK', 'm=347', f'a={a}', f'beta={beta}', f'tau={tau}', f'c={c}',
      f'rh_minus_a={rh-a}', f'rk_minus_2a={rk-2*a}', f'q3={q3}',
      f'gamma3={gamma}', f'triple_density_threshold={threshold}',
      f'm348_margin={rk0-2*a2}')

from decimal import Decimal, getcontext
getcontext().prec=80
D=Decimal
L=D('2.682918382150264832337066716763')
U=D('2.682918382150264832337066725454')
eps=D('0.02')
# Decimal power via exp/log
ln2=D(2).ln()
delta=D(2)*D(2).sqrt()*(D(1)-((-eps/D(2))*ln2).exp()/(D(1)+eps))
scale=(D(1)+eps).sqrt()/D(2)
lo=scale*(L-delta)
hi=scale*U
assert delta > 0
assert lo > 0 and lo < hi
# Check the analytic derivative signs at rational sample points; proof in RESULT is symbolic.
for k in range(1,100):
    t=D(k)/D(100)
    Hp=t**(D('-0.5'))*(D(1)-(eps/D(2)*t.ln()).exp())
    Hpp=D('0.5')*t**D('-1.5')*((D(1)-eps)*(eps/D(2)*t.ln()).exp()-D(1))
    assert Hp >= 0 and Hpp < 0
print('VERIFY_OK')
print('delta=',delta)
print('R_lower=',lo)
print('R_upper=',hi)

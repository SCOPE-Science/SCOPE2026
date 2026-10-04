from decimal import Decimal, getcontext
getcontext().prec = 60
D=Decimal

def H(b):
    b=D(str(b))
    t=(D(1)+((b-D(2))/(b+D(2))).sqrt())/D(2)
    return ((b+D(1))/b).ln()-(D(1)-t).ln()-(b+D(2))*t*t/D(2),t

lo=D('3.75347721'); hi=D('3.75347722')
hlo,tlo=H(lo); hhi,thi=H(hi)
assert hlo > 0, (hlo,tlo)
assert hhi < 0, (hhi,thi)

for btxt in ['2.1','3','3.75347','3.75348','4','10']:
    b=D(btxt)
    h,t=H(b)
    err=abs(t*(D(1)-t)-D(1)/(b+D(2)))
    assert err < D('1e-50'), (b,err)

# Finite stress tests of the transformed inequality. These are not the proof.
def f(b,t):
    b=D(str(b)); t=D(str(t))
    return ((b+D(1))/b).ln()-(D(1)-t).ln()-(b+D(2))*t*t/D(2)

for b in ['0.5','1','2','3','3.7','3.75347']:
    for j in range(1,1000):
        t=D(j)/D(1000)
        assert f(b,t) > D('-1e-45'), (b,j,f(b,t))
for b in ['3.75348','4','5','10']:
    h,t=H(b)
    assert h < 0, (b,h)
print('VERIFY_OK')

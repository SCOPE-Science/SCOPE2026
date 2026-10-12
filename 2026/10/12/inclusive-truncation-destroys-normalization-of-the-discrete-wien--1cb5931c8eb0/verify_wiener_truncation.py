"""Replay the published discrete Wiener-range truncation at high precision.

Requires Python 3 and mpmath. The proof is analytic; this is a reproducibility aid.
"""
import mpmath as mp

mp.mp.dps=70

def H(T,x,K):
    """Continuous Wiener range CDF at x>0, as printed in the source."""
    T=mp.mpf(T);x=mp.mpf(x)
    assert T>0 and x>0 and K>=1
    return mp.fsum([
        (mp.mpf(8)/(mp.pi**2*(2*k-1)**2)+8*T/(x*x))
        *mp.exp(-mp.pi**2*(2*k-1)**2*T/(2*x*x))
        for k in range(1,K+1)
    ])

def tail_bound(T,x,K):
    """Upper bound for omitted positive CDF series, using (2k-1)^2>=k^2.

    For k>=K+1 the exp(-a*k^2) terms are at most geometrically decreasing
    with ratio exp(-a*(2*K+3)); coefficients are bounded by 8/pi^2+8T/x^2.
    """
    T=mp.mpf(T);x=mp.mpf(x)
    a=mp.pi**2*T/(2*x*x)
    coefficient=mp.mpf(8)/mp.pi**2+8*T/(x*x)
    return coefficient*mp.exp(-a*(K+1)**2)/(1-mp.exp(-a*(2*K+3)))

def F(T,r,K=80):
    assert int(r)==r
    return H(T,int(r)+1,K) if r>=0 else mp.mpf(0)

def pmf(T,r,K=80):
    return F(T,r,K)-F(T,r-1,K)

def interval(T,a,b,K=80):
    assert 0<=a<b and isinstance(a,int) and isinstance(b,int)
    pubden=F(T,b,K)-F(T,a,K)
    true=F(T,b,K)-F(T,a-1,K)
    low=pmf(T,a,K)
    assert pubden>0 and true>pubden and low>0
    assert mp.almosteq(sum(pmf(T,r,K) for r in range(a,b+1)),true,rel_eps=mp.mpf('1e-54'))
    return pubden,true,low

for T,a,b in [('1',2,8),('1',1,7),('0.1',0,1)]:
    d1,p1,low1=interval(T,a,b,80)
    d2,p2,low2=interval(T,a,b,100)
    assert abs(d1-d2)<mp.mpf('1e-55')
    assert abs(p1-p2)<mp.mpf('1e-55')
    assert tail_bound(T,b+1,80)<mp.mpf('1e-55')
    assert mp.almosteq(p1/d1,1+low1/d1,rel_eps=mp.mpf('1e-55'))

D1,C1,p2=interval('1',2,8)
D2,C2,p1=interval('1',1,7)
pubtotal=(C1/D1)*(C2/D2)
pubatom=(p2/D1)*(p1/D2)
trueatom=(p2/C1)*(p1/C2)
assert abs(pubtotal-mp.mpf('86.7321789530702265665086786876')) < mp.mpf('1e-25')
assert abs(pubatom-mp.mpf('65.765166908457719303098517427')) < mp.mpf('1e-25')
assert abs(trueatom-mp.mpf('0.758255675140393813259277121622')) < mp.mpf('1e-25')
assert pubatom>1 and trueatom<1
# A direct integer-grid check, not merely a closed-form ratio.
grid=mp.fsum([pmf('1',r1)*pmf('1',r2)/(D1*D2) for r1 in range(2,9) for r2 in range(1,8)])
assert abs(grid-pubtotal)<mp.mpf('1e-52')

Dh,Ch,p0=interval('0.1',0,1)
p1h=pmf('0.1',1)
assert mp.almosteq(Dh,p1h)
published0=p0/p1h
correct0=p0/Ch
assert abs(published0-mp.mpf('158.70343733965314046239864076968721'))<mp.mpf('1e-26')
assert abs(correct0-mp.mpf('0.99373839400918324719034743977107588'))<mp.mpf('1e-26')
print('VERIFY_OK')
print('T1_marginal_inflation_2_8',mp.nstr(C1/D1,31))
print('T1_marginal_inflation_1_7',mp.nstr(C2/D2,31))
print('T1_published_joint_total',mp.nstr(pubtotal,31))
print('T1_published_cell_2_1',mp.nstr(pubatom,31))
print('T1_correct_cell_2_1',mp.nstr(trueatom,31))
print('T0p1_published_cell_0',mp.nstr(published0,31))
print('T0p1_correct_cell_0',mp.nstr(correct0,31))

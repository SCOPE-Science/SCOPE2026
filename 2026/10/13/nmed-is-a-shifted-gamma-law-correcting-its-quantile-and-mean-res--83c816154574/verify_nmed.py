import mpmath as mp
mp.mp.dps=70

def cdf(x,I,beta):
    if x<=I: return mp.mpf('0')
    y=(x-I)/beta
    return 1-(1+y)*mp.e**(-y)

def surv(x,I,beta):
    if x<=I: return mp.mpf('1')
    y=(x-I)/beta
    return (1+y)*mp.e**(-y)

def q_correct(p,I,beta):
    return I+beta*(-1-mp.lambertw(-(1-p)/mp.e,-1))

def q_printed(p,I,beta):
    return I+beta*(-mp.lambertw((1-p)/mp.e,0)-1)

def m_correct(t,I,beta):
    y=t-I
    return beta*(y+2*beta)/(y+beta)

for I,beta in [(mp.mpf('1.55'),mp.mpf('2')), (mp.mpf('4.91'),mp.mpf('3'))]:
    for p in (mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.9'),mp.mpf('0.99')):
        q=q_correct(p,I,beta)
        assert q>I
        assert abs(cdf(q,I,beta)-p)<mp.mpf('1e-55')
        qp=q_printed(p,I,beta)
        assert qp<I
    for t in (I, I+beta, I+5*beta, I+20*beta):
        mc=m_correct(t,I,beta)
        integ=mp.quad(lambda x: surv(x,I,beta), [t, mp.inf])/surv(t,I,beta)
        assert abs(mc-integ)<mp.mpf('1e-50')
    assert m_correct(I,I,beta)==2*beta
    assert m_correct(I+20*beta,I,beta)>beta
    assert m_correct(I+20*beta,I,beta)<m_correct(I+5*beta,I,beta)<m_correct(I+beta,I,beta)<m_correct(I,I,beta)

print('VERIFY_OK')

import mpmath as mp
mp.mp.dps=70

def B(x,theta):
    x=mp.mpf(x); theta=mp.mpf(theta)
    return 1-(1+2*theta*x)*mp.e**(-2*theta*x)

def pdf(x,alpha,theta):
    x=mp.mpf(x); alpha=mp.mpf(alpha); theta=mp.mpf(theta)
    A=B(1,theta)
    return 4*alpha*theta**2*x*mp.e**(-2*theta*x)*B(x,theta)**(alpha-1)/A**alpha

def survival(x,alpha,theta):
    x=mp.mpf(x); alpha=mp.mpf(alpha); theta=mp.mpf(theta)
    A=B(1,theta)
    return 1-(B(x,theta)/A)**alpha

def hazard(x,alpha,theta):
    return pdf(x,alpha,theta)/survival(x,alpha,theta)

def endpoint_c(alpha,theta):
    alpha=mp.mpf(alpha); theta=mp.mpf(theta)
    return 4*alpha*theta**2*mp.e**(-2*theta)/B(1,theta)

pairs=[
    (mp.mpf('0.2'),mp.mpf('1')),
    (mp.mpf('0.5'),mp.mpf('0.2')),
    (mp.mpf('1'),mp.mpf('3')),
    (mp.mpf('2.5'),mp.mpf('0.7')),
    (mp.mpf('8'),mp.mpf('4')),
]
for alpha,theta in pairs:
    c=endpoint_c(alpha,theta)
    for delta in [mp.mpf('1e-5'),mp.mpf('1e-7'),mp.mpf('1e-9')]:
        x=1-delta
        assert abs(pdf(x,alpha,theta)/c-1) < mp.mpf('1e-4')
        assert abs(survival(x,alpha,theta)/(c*delta)-1) < mp.mpf('1e-4')
        assert abs(delta*hazard(x,alpha,theta)-1) < mp.mpf('1e-4')
    assert hazard(mp.mpf('0.9999'),alpha,theta) > hazard(mp.mpf('0.999'),alpha,theta) > hazard(mp.mpf('0.99'),alpha,theta)

alpha=mp.mpf('0.2'); theta=mp.mpf('1')
h01=hazard(mp.mpf('0.1'),alpha,theta)
h04=hazard(mp.mpf('0.4'),alpha,theta)
h099=hazard(mp.mpf('0.99'),alpha,theta)
assert h01>h04
assert h099>100
assert abs(h01-mp.mpf('3.6531601598260763')) < mp.mpf('1e-12')
assert abs(h04-mp.mpf('2.9552667238347778')) < mp.mpf('1e-12')
assert abs(h099-mp.mpf('100.868370128441385')) < mp.mpf('1e-12')

print('VERIFY_OK')
print('h_0.1',mp.nstr(h01,30))
print('h_0.4',mp.nstr(h04,30))
print('h_0.99',mp.nstr(h099,30))
for alpha,theta in pairs:
    x=mp.mpf('0.999999')
    print('endpoint_ratio',mp.nstr(alpha,8),mp.nstr(theta,8),mp.nstr((1-x)*hazard(x,alpha,theta),25))

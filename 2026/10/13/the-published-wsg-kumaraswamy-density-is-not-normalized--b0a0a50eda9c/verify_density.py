import mpmath as mp
mp.mp.dps=70

c=mp.pi/2

def theta(y,d,a):
    return c*(1-y**d)**a

def cdf(y,d,a):
    t=theta(y,d,a)
    return mp.cos(t)*mp.e**(1-mp.cos(t))

def base_factor(y,d,a):
    return c*d*a*y**(d-1)*(1-y**d)**(a-1)

def f_correct(y,d,a):
    t=theta(y,d,a)
    return base_factor(y,d,a)*mp.sin(t)*mp.e**(1-mp.cos(t))*(1-mp.cos(t))

def f_published(y,d,a):
    t=theta(y,d,a)
    return base_factor(y,d,a)*mp.cos(t)*mp.e**(1-mp.cos(t))*(1-mp.cos(t))

# CDF derivative agrees with corrected density, not the published kernel.
for d,a in [(mp.mpf('0.7'),mp.mpf('0.6')),(mp.mpf('2'),mp.mpf('3')),(mp.mpf('4.5'),mp.mpf('0.4'))]:
    for y in (mp.mpf('0.15'),mp.mpf('0.43'),mp.mpf('0.81')):
        num=mp.diff(lambda z:cdf(z,d,a),y)
        assert abs(num/f_correct(y,d,a)-1) < mp.mpf('1e-50')
        # Away from accidental theta=pi/4 equality, printed and corrected differ.
        assert abs(f_published(y,d,a)-f_correct(y,d,a)) > mp.mpf('1e-20')

# Normalization and universal erroneous mass.
I=mp.quad(lambda t:mp.cos(t)*mp.e**(1-mp.cos(t))*(1-mp.cos(t)),[0,mp.pi/2])
J=mp.quad(lambda t:mp.sin(t)*mp.e**(1-mp.cos(t))*(1-mp.cos(t)),[0,mp.pi/2])
assert abs(J-1) < mp.mpf('1e-60')
assert I < mp.e*(1-mp.pi/4) < 1
assert abs(I-mp.mpf('0.34499279694726429380104422382450697891452293208855535')) < mp.mpf('1e-50')

# Direct y-integrals for representative parameter pairs.
for d,a in [(mp.mpf('0.5'),mp.mpf('0.5')),(mp.mpf('1'),mp.mpf('2')),(mp.mpf('3'),mp.mpf('0.75'))]:
    jc=mp.quad(lambda y:f_correct(y,d,a),[0,mp.mpf('0.5'),1])
    jw=mp.quad(lambda y:f_published(y,d,a),[0,mp.mpf('0.5'),1])
    assert abs(jc-1) < mp.mpf('1e-35')
    assert abs(jw-I) < mp.mpf('1e-35')

print('VERIFY_OK')
print('published_mass',mp.nstr(I,40))
print('analytic_upper_bound',mp.nstr(mp.e*(1-mp.pi/4),40))

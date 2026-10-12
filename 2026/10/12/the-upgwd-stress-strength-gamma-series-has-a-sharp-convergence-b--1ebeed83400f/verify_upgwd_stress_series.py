import mpmath as mp
mp.mp.dps = 70

def direct(b1,b2):
    return b1*mp.e**2*mp.quad(lambda t: t**(b1-1)*mp.e**(-t**b1-t**b2), [1, mp.inf])

def term(n,b1,b2):
    r=mp.mpf(b2)/b1
    return mp.e**2*((-1)**n)/mp.factorial(n)*mp.gammainc(1+n*r,1,mp.inf)

def series(b1,b2,N=160):
    return mp.fsum(term(n,b1,b2) for n in range(N))

def repaired(b1,b2,N=160):
    if b2 < b1:
        return series(b1,b2,N)
    if b2 == b1:
        return mp.mpf('0.5')
    return 1-series(b2,b1,N)

safe=[(mp.mpf('2'),mp.mpf('1.5')),
      (mp.mpf('1.5'),mp.mpf('1')),
      (mp.mpf('1'),mp.mpf('0.5')),
      (mp.mpf('3'),mp.mpf('1'))]
for b1,b2 in safe:
    d=direct(b1,b2)
    s=series(b1,b2)
    assert abs(d-s) < mp.mpf('1e-40')

# Equality: true reliability is one half but terms do not vanish.
deq=direct(mp.mpf('1'),mp.mpf('1'))
assert abs(deq-mp.mpf('0.5')) < mp.mpf('1e-50')
mag20=abs(term(20,mp.mpf('1'),mp.mpf('1')))
mag80=abs(term(80,mp.mpf('1'),mp.mpf('1')))
assert abs(mag80-mp.e**2) < mp.mpf('1e-30')
assert mag20 > 7

# Reversed order: printed terms grow; swapped complementary series is correct.
rb1=mp.mpf('0.5'); rb2=mp.mpf('1.5')
d=direct(rb1,rb2)
assert abs(term(20,rb1,rb2)) > mp.mpf('1e50')
r=repaired(rb1,rb2)
assert abs(d-r) < mp.mpf('1e-40')

print('VERIFY_OK')
for b1,b2 in safe[:3]:
    print('safe', mp.nstr(b1,5), mp.nstr(b2,5), mp.nstr(direct(b1,b2),18), mp.nstr(series(b1,b2),18))
print('equal_direct', mp.nstr(deq,18))
print('equal_term_abs_n80', mp.nstr(mag80,18))
print('reversed_direct', mp.nstr(d,18))
print('reversed_repaired', mp.nstr(r,18))
print('reversed_term_abs_n20', mp.nstr(abs(term(20,rb1,rb2)),8))

"""Reproduce elementary selection and Fourier identities for a double-eclipse model.
Only Python 3 standard library is required. No observational catalogue is used.
"""
from fractions import Fraction
from math import pi, sin, cos


def moments(population):
    m0=sum(prob*eta/(1-e*e) for prob,eta,e in population)
    m1=sum(prob*eta*e/(1-e*e) for prob,eta,e in population)
    return m0,m1,m1/m0


def angle_density(omega, epsilon):
    return (1-epsilon*abs(sin(omega)))/(2*pi-4*epsilon)


def integrate_midpoint(f,N=32768):
    step=2*pi/N
    return step*sum(f((j+.5)*step) for j in range(N))


def validate(population):
    assert sum(p for p,_,_ in population)==1
    assert all(Fraction(0)<e<Fraction(1) and Fraction(0)<eta<1-e for _,eta,e in population)
    m0,m1,eps=moments(population)
    assert 0<eps<1
    assert abs(integrate_midpoint(lambda w: angle_density(w,float(eps)))-1)<3e-9
    for k in range(1,7):
        empirical=integrate_midpoint(lambda w: angle_density(w,float(eps))*cos(2*k*w))
        theoretical=2*float(eps)/((4*k*k-1)*(pi-2*float(eps)))
        assert abs(empirical-theoretical)<3e-9, (k,empirical,theoretical)
        assert abs(integrate_midpoint(lambda w: angle_density(w,float(eps))*sin(k*w)))<3e-9
        assert abs(integrate_midpoint(lambda w: angle_density(w,float(eps))*cos((2*k-1)*w)))<3e-9
    obs=2*float(eps)/(3*(pi-2*float(eps)))
    invert=3*pi*obs/(2*(1+3*obs))
    assert abs(invert-float(eps))<1e-13
    ptot=m0*(1-Fraction(0))
    weighted_both=integrate_midpoint(lambda w: float(sum(p*min(eta*(1+e*sin(w))/(1-e*e),eta*(1-e*sin(w))/(1-e*e)) for p,eta,e in population))/(2*pi))
    assert abs(weighted_both-float(m0)*(1-2*float(eps)/pi))<3e-9
    return float(m0), float(eps)


def main():
    F=Fraction
    single=[(F(1),F(1,10),F(1,2))]
    mixed=[(F(15,22),F(1,10),F(1,4)),(F(7,22),F(1,10),F(3,4))]
    v1=validate(single)
    v2=validate(mixed)
    assert moments(single)[2]==moments(mixed)[2]==F(1,2)
    assert moments(single)[0]!=moments(mixed)[0]
    assert moments(single)[0]==F(2,15)
    assert moments(mixed)[0]==F(8,55)*F(1) # 0.1454545...
    variants=[
      [(F(1,3),F(1,20),F(1,3)),(F(2,3),F(1,7),F(2,5))],
      [(F(1,4),F(1,8),F(1,8)),(F(1,4),F(1,6),F(1,3)),(F(1,2),F(1,12),F(5,6))],
      [(F(1,2),F(2,5),F(1,5)),(F(1,2),F(3,10),F(2,5))],
    ]
    for v in variants:validate(v)
    print('PASS: exact rational indistinguishability, five mixture cases, six Fourier harmonics and direct joint-probability quadratures')
    print('witness transit rates:',v1[0],v2[0],'; shared tilted eccentricity:',v1[1])

if __name__=='__main__':main()

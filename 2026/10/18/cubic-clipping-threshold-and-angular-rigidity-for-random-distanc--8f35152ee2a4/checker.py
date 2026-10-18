#!/usr/bin/env python3
"""Reproducible numerical checks for the short-distance profile of 3D parallelotopes.

No external dependencies. The finite tests supplement the exact proof.
Run: python3 checker.py
"""
import math

PI = math.pi


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def norm(a):
    return math.sqrt(dot(a, a))


def unit(a):
    n = norm(a)
    return tuple(x/n for x in a)


def profile(B):
    s = [norm(row) for row in B]
    c = [[dot(B[i], B[j])/(s[i]*s[j]) for j in range(3)] for i in range(3)]
    fifth = 0.0
    base = 0.0
    angle_deficit = 0.0
    for i in range(3):
        for j in range(i+1, 3):
            x = max(-1.0, min(1.0, c[i][j]))
            f = math.sqrt(max(0., 1.-x*x)) + x*math.asin(x)
            fifth += (8./15.)*s[i]*s[j]*f
            base += (8./15.)*s[i]*s[j]
            angle_deficit += s[i]*s[j]*x*x
    cut = 1./max(s)
    active = [i for i in range(3) if abs(s[i]-max(s)) < 1.e-12]
    onset = (2.*PI/3.)*sum(math.prod(1. - abs(dot(B[j], B[i]))/(s[i]*s[i])
                                   for j in range(3) if j != i) for i in active)
    return s, c, fifth, base, angle_deficit, cut, active, onset


def spherical_cubature(B, count=50000):
    # Unit spherical points from a longitude/latitude-free Fibonacci rule.
    # Spherical moments are then integrated in radius exactly.
    sums = [0.0, 0.0, 0.0]
    golden = (math.sqrt(5.)-1.)/2.
    for k in range(count):
        z = 1. - 2.*(k+.5)/count
        a = 2.*PI*((k*golden) % 1.)
        q = math.sqrt(1.-z*z)
        u = (q*math.cos(a), q*math.sin(a), z)
        l = [abs(dot(row, u)) for row in B]
        sums[0] += sum(l)
        sums[1] += l[0]*l[1] + l[0]*l[2] + l[1]*l[2]
        sums[2] += l[0]*l[1]*l[2]
    return [4.*PI*sums[j]/(count*(j+4.)) for j in range(3)]


def cap_excess(B, r, active, samples_t=45, samples_disk=500):
    # Independent cap integration of the clipped-minus-polynomial covariogram.
    s = [norm(v) for v in B]
    r0 = 1./max(s)
    delta = r-r0
    out = 0.0
    golden = (math.sqrt(5.)-1.)/2.
    for i in active:
        n = unit(B[i])
        v = (1.,0.,0.) if abs(n[0]) < .9 else (0.,1.,0.)
        e = unit(cross(n, v))
        f = cross(n, e)
        others = [j for j in range(3) if j != i]
        for sg in (-1.,1.):
            for t_index in range(samples_t):
                x = delta*(t_index+.5)/samples_t
                tau = r0+x
                radius2 = r*r-tau*tau
                # Area of cap cross-section times the average integrand.
                avg = 0.
                for k in range(samples_disk):
                    rho = math.sqrt((k+.5)/samples_disk)
                    angle = 2*PI*((k*golden) % 1.)
                    v1 = math.sqrt(radius2)*rho*math.cos(angle)
                    v2 = math.sqrt(radius2)*rho*math.sin(angle)
                    z = tuple(sg*tau*n[j]+v1*e[j]+v2*f[j] for j in range(3))
                    avg += (abs(dot(B[i],z))-1.) * math.prod(1.-abs(dot(B[j],z)) for j in others)
                out += (delta/samples_t)*PI*radius2*avg/samples_disk
    return out


def main():
    examples = {
        'unit cube': ((1.,0.,0.), (0.,1.,0.), (0.,0.,1.)),
        'skew one': ((1.,0.,0.), (.35,1.,0.), (.20,-.25,1.)),
        'skew two': ((1.,.20,0.), (.3,1.,0.), (0.,.2,1.)),
        'three angles': ((1.,0.,0.), (.90,1.,0.), (.4,.7,1.)),
    }
    for name,B in examples.items():
        s, c, fifth, base, delta, r0, active, onset = profile(B)
        assert (4./15.)*delta-1.e-11 <= fifth-base
        assert fifth-base <= (8./15.)*(PI/2.-1.)*delta+1.e-11
        q4,q5,h = spherical_cubature(B)
        assert abs(q4 - PI/2.*sum(s)) < 0.002, (name,'fourth',q4)
        assert abs(q5 - fifth) < 0.002, (name,'fifth',q5,fifth)
        assert h > 0 and h < PI/6.*math.prod(s)
        if name == 'unit cube':
            assert abs(q5-1.6) < .002
            assert abs(h-1./6.) < .002
            assert abs(onset-2.*PI) < 1.e-12
        actual = cap_excess(B, r0+0.002*r0, active)
        ratio = actual/(0.002*r0)**3
        assert abs(ratio-onset) <= .075*onset, (name,'onset',ratio,onset)
        print('%-13s r0=%.7f fifth=%.7f sixth=%.7f onset=%.7f observed=%.7f' %
              (name,r0,fifth,h,onset,ratio))
    print('PROFILE_AND_CUBIC_ONSET_CHECK_OK',len(examples),'profiles')


if __name__ == '__main__':
    main()

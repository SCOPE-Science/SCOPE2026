"""Independent discrete-quadrature checks for planar Minkowski mixed-area covariance.

This script tests finite trigonometric support functions. The proof in RESULT.md,
not these finite tests, supplies the extension to arbitrary convex bodies.
"""
import math

PI = math.pi
N_ANGLE = 256
N_NORMAL = 256


def area(coeff, angle=0.0):
    # coeff = (mean radius, {frequency: (cos coefficient, sin coefficient)})
    mean, modes = coeff
    subtotal = 0.0
    for j in range(N_NORMAL):
        phi = 2 * PI * j / N_NORMAL
        h, dh = mean, 0.0
        for n, (a, b) in modes.items():
            x = n * (phi - angle)
            h += a * math.cos(x) + b * math.sin(x)
            dh += n * (-a * math.sin(x) + b * math.cos(x))
        subtotal += h * h - dh * dh
    return PI * subtotal / N_NORMAL


def area_sum(K, L, theta):
    mean = K[0] + L[0]
    total = 0.0
    for j in range(N_NORMAL):
        phi = 2 * PI * j / N_NORMAL
        h, dh = mean, 0.0
        for coeff, shift in ((K, 0.0), (L, theta)):
            for n, (a, b) in coeff[1].items():
                x = n * (phi - shift)
                h += a * math.cos(x) + b * math.sin(x)
                dh += n * (-a * math.sin(x) + b * math.cos(x))
        total += h * h - dh * dh
    return PI * total / N_NORMAL


def weights(obj):
    return {n: PI / 2 * (n*n - 1) * (a*a+b*b)
            for n, (a,b) in obj[1].items() if n >= 2}


def covariance_theory(K,L,tau):
    ak, al = weights(K), weights(L)
    return 2 * sum(ak.get(n,0)*al.get(n,0)*math.cos(n*tau) for n in set(ak)|set(al))


def check(K,L, tolerance=5e-11):
    wk, wl = weights(K), weights(L)
    assert all(K[0] > sum(abs(1-n*n)*math.hypot(a,b) for n,(a,b) in K[1].items()) for _ in [0])
    assert L[0] > sum(abs(1-n*n)*math.hypot(a,b) for n,(a,b) in L[1].items())
    values = [area_sum(K,L,2*PI*j/N_ANGLE) for j in range(N_ANGLE)]
    mean = sum(values)/N_ANGLE
    expected_mean = area(K)+area(L)+2*PI*K[0]*L[0]
    assert abs(mean-expected_mean) < tolerance, ('mean',mean,expected_mean)
    deviations=[v-mean for v in values]
    for shift in (0, 9, 29, 64, 79):
        measured=sum(deviations[j]*deviations[(j+shift)%N_ANGLE] for j in range(N_ANGLE))/N_ANGLE
        predicted=covariance_theory(K,L,2*PI*shift/N_ANGLE)
        assert abs(measured-predicted)<tolerance, (shift,measured,predicted)
    Dk, Dl=sum(wk.values()), sum(wl.values())
    assert covariance_theory(K,L,0)<=2*Dk*Dl+1e-15
    return mean,covariance_theory(K,L,0),Dk,Dl


def main():
    # Disjoint Fourier supports: distinct noncircular convex bodies with constant sum area.
    K=(1.0,{2:(.08,0.0)})
    L=(1.1,{3:(.07,0.0)})
    mean,var,dk,dl=check(K,L)
    assert dk>0 and dl>0 and abs(var)<1e-16
    assert max(area_sum(K,L,2*PI*j/64) for j in range(64)) - min(area_sum(K,L,2*PI*j/64) for j in range(64)) < 1e-12
    # Strict sharpness at common harmonic degree four.
    K=(1.0,{4:(.017, .005)})
    L=(1.3,{4:(-.021, .012)})
    mean,var,dk,dl=check(K,L)
    assert abs(var-2*dk*dl)<1e-15
    # Multiple modes and distinct phases: genuine mixed frequencies.
    K=(1.2,{2:(.08,.03),3:(.025,-.03),5:(.003,.005)})
    L=(1.4,{2:(-.04,.05),3:(.02,.009),4:(.012,0.0),5:(-.002,.003)})
    mean,var,dk,dl=check(K,L)
    assert 0<var<2*dk*dl
    # Disk: all rotational fluctuations vanish even if the other summand is not round.
    K=(1.0,{})
    mean,var,dk,dl=check(K,L)
    assert var == 0 and dk == 0
    print('VERIFY_OK: Fourier covariance/mean identities, 4 geometrically convex cases, 20 shifted autocovariances, zero-variance pairs, and sharp equality.')

if __name__ == '__main__': main()

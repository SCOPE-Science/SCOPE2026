"""Deterministic numerical quadrature for the Gaussian contact-trace formula.

Run with Python 3 and its standard library only. The finite quadratures
illustrate the theorem but are not substitutes for its analytic proof.
"""
import math

PI = math.pi


def simpson(func, start, stop, panels=1200):
    assert panels > 0 and panels % 2 == 0
    step = (stop - start) / panels
    total = 0.0
    for j in range(panels + 1):
        weight = 1 if j == 0 or j == panels else (4 if j % 2 else 2)
        total += weight * func(start + j * step)
    return total * step / 3


def tail_primitive(x):
    """Integral over nonnegative s,t of exp(-(x+s+t)^2), for x >= 0."""
    assert x >= 0
    return 0.5 * math.exp(-x*x) - 0.5 * math.sqrt(PI) * x * math.erfc(x)


def predicted_coefficient(contact_order, combined_contact_coefficient, gap):
    p, a, g = contact_order, combined_contact_coefficient, gap
    assert p > 1 and a > 0 and g >= 0
    integral = simpson(lambda s: s**(1 + 1/p) * math.exp(-(g+s)**2), 0, 8)
    return 2*p/((p+1)*PI**1.5 * a**(1/p)) * integral


def quadrature_scaled_trace_for_two_superellipses(R, order, gap, panels=120, cutoff=5):
    """Quadrature of the finite-R integral, divided by R**(1-1/order).

    The bodies are |x+1|^2+|y|^order<=1 and its reflection.
    Their two contact coefficients are 1/2, so their sum is 1.
    Tangential variables are truncated to the stated cutoff.
    Normal-coordinate integrations are analytically eliminated by
    inclusion-exclusion of the twice-integrated Gaussian tail.
    """
    assert R > 0 and order > 1 and gap >= 0 and panels % 2 == 0
    step = 2*cutoff/panels
    scale = R**(1-1/order)
    answer = 0.0
    for i in range(panels+1):
        u = -cutoff + i*step
        y1 = u*scale
        a1 = abs(y1/R)**order
        if a1 >= 1:
            continue
        t1 = math.sqrt(1-a1)
        d1 = R*a1/(1+t1)
        w1 = 2*R*t1
        wi = 1 if i == 0 or i == panels else (4 if i % 2 else 2)
        for j in range(panels+1):
            h = -cutoff + j*step
            y2 = y1 + h
            a2 = abs(y2/R)**order
            if a2 >= 1:
                continue
            t2 = math.sqrt(1-a2)
            d2 = R*a2/(1+t2)
            w2 = 2*R*t2
            d = gap + d1+d2
            normal_integral = (tail_primitive(d)-tail_primitive(d+w1)
                               -tail_primitive(d+w2)+tail_primitive(d+w1+w2))
            wj = 1 if j == 0 or j == panels else (4 if j % 2 else 2)
            answer += wi*wj*math.exp(-h*h)*normal_integral
    return step*step*answer/(9*PI*PI)


def run_checks():
    checks = 0
    def verify(test, message):
        nonlocal checks
        if not test:
            raise AssertionError(message)
        checks += 1
    for order in (2, 4, 6):
        exact_zero = (order*math.gamma(1+1/(2*order)) /
                      ((order+1)*PI**1.5))
        numeric_zero = predicted_coefficient(order, 1, 0)
        verify(abs(exact_zero-numeric_zero) < 1e-7,
               'contact gamma constant: order %s' % order)
        for gap in (0, 0.6):
            target = predicted_coefficient(order, 1, gap)
            verify(target > 0, 'positive coefficient')
            approximations = []
            for R in (20, 80, 320):
                val = quadrature_scaled_trace_for_two_superellipses(R, order, gap)
                approximations.append(val)
                verify(val > 0, 'positive finite trace')
                verify(abs(val-target) / target < 0.025,
                       'finite-size approximation')
            verify(abs(approximations[2]-target) < abs(approximations[0]-target),
                   'approaches the predicted constant')
        verify(predicted_coefficient(order, 1, 0.6) < numeric_zero,
               'strict gap decay')
    verify(abs(predicted_coefficient(2,1,0) - 0.108518808227677)<1e-7,
           'equal-disc tangency benchmark')
    print('Passed', checks, 'Gaussian contact quadrature checks.')


if __name__ == '__main__':
    run_checks()

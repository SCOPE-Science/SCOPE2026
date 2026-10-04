#!/usr/bin/env python3
import math

def P_interval(k, L, alpha):
    z = 0.5 * alpha * alpha * math.tan(k * L)
    return 1.0 / (1.0 + z*z)

def lambda_interval(E, L, c):
    k = math.sqrt(E/c)
    return k * math.tan(k*L)

def main():
    derivative_checks = 0
    halfmax_checks = 0
    scaling_checks = 0

    for L in (0.7, 1.0, 1.3, 2.0):
        for c in (0.5, 1.0, 2.0):
            for n in (1, 2, 3, 4):
                k0 = n*math.pi/L
                E0 = c*k0*k0
                local_weight = 2.0/L
                predicted_derivative = 1.0/(c*local_weight)

                h = 1e-6 * max(1.0, E0)
                got = (lambda_interval(E0+h, L, c) -
                       lambda_interval(E0-h, L, c))/(2*h)
                assert abs(got-predicted_derivative) <= 2e-5*max(1.0, abs(predicted_derivative))
                derivative_checks += 1

                for alpha in (8.0, 16.0, 32.0, 64.0):
                    delta_k = math.atan(2.0/(alpha*alpha))/L
                    km = k0-delta_k
                    kp = k0+delta_k
                    assert abs(P_interval(km, L, alpha)-0.5) < 2e-12
                    assert abs(P_interval(kp, L, alpha)-0.5) < 2e-12

                    exact_width = c*(kp*kp-km*km)
                    leading = 4.0*c*k0*local_weight/(alpha*alpha)
                    assert abs(exact_width/leading-1.0) < 4e-4
                    halfmax_checks += 1

                alpha = 128.0
                for x in (-3.0, -1.5, -0.5, 0.0, 0.5, 1.5, 3.0):
                    E = E0 + 2.0*c*k0*local_weight*x/(alpha*alpha)
                    k = math.sqrt(E/c)
                    gotP = P_interval(k, L, alpha)
                    wantP = 1.0/(1.0+x*x)
                    assert abs(gotP-wantP) < 8e-4
                    scaling_checks += 1

    print("VERIFY_OK")
    print("derivative_checks =", derivative_checks)
    print("halfmax_checks =", halfmax_checks)
    print("lorentzian_scaling_checks =", scaling_checks)
    print("exact_interval_FWHM = 4*c*k0*atan(2/alpha^2)/L")

if __name__ == "__main__":
    main()

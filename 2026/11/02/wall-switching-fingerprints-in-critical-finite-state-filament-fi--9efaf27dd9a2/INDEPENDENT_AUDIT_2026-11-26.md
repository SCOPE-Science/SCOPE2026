# Independent mathematical audit

## correctness

PASS

First-step elimination gives A_s f_{j+1}-B_s f_j+C_s f_{j-1}=0 with f_0=1 and f_{N-1}=b_gamma f_N. In particular b_gamma=1+(s/k_d)(1+lambda_+/(s+lambda_-+gamma)). Strict ordering also follows directly: the derivative of the killed resolvent equation with respect to gamma has forcing f_N-g_N>0 in row (N,a) only, and every transient state reaches that row, so the inverse resolvent makes every component strictly positive. This does not use criticality. At criticality A_0=C_0=D(lambda_++lambda_-), and B_s-A_s-C_s=s(s+lambda_++lambda_-). With s=sigma/N^2 the roots are 1±h/N+O(N^-2). The two cap coefficients in the frozen solution are asymptotic to he^-h/N and -he^h/N, giving the reflected-Brownian transform. For the difference between walls, the boundary forcing is (b_1-b_2)f_N(b_2) at N-1 minus b_1 times N, with b_1-b_2 asymptotic to sigma(delta_1-delta_2)/N^2 for distinct walls. On the difference basis z_+^j-z_-^j this boundary operator is -2h cosh(h)/N to leading order, while f_N(b_2) tends to sech(h). This gives the sign, the cosh(h)^2 denominator, and the factor sinh(hx)/h. Adjacent differences of this wall contrast are O(N^-2), so the active-state equation has the same scaled limit. At s=0 differentiation yields the slope recurrence d_{j+1}=d_j-1/D with d_N=delta_gamma; summation and the active backward equation give (3) and both mean differences. These arguments include x=1, gamma=0, and the trivial equal-wall contrast; they do not assert stochastic ordering. Supporting verifier was inspected, not executed. A fresh direct-generator check at N=9 and rates (k_d,k_e,lambda_+,lambda_-)=(2,3,1,1.5) corroborated all-state transform ordering at s=0.4 for gamma 0, 1 and 3 and the shortening means.

## originality

PASS

Credit the original hard-cap model, its critical mean, and leading diffusion precedent. The new comparison supported here is the strict absorption-transform sensitivity to independently varied cap switching together with the positive-order N^-1 effect at fixed critical bulk rates. In particular, the original mean is not new and the variable-cap mean is a direct extension of its symbolic boundary coefficient, not itself the originality basis. No statement-level match for the relative full-transform correction was established in the inspected sources.

## value

PASS

This gives a measurable distinction between plausible boundary rules whose leading critical first-passage laws coincide: the nonzero relative transform at order 1/N for any positive scaled discount and macroscopic starting position. The exact correction tests approximations across the whole Laplace scale, rather than merely reproducing the original model's mean or a leading Brownian formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

The Fourier coefficient of the free lattice propagator gives probability J_n(2|h|t)^2. Full re-preparation makes the next trial independent of the first pair (duration, outcome). The renewal mean uses the unconditional first duration 1/r, not independence of duration and outcome within a trial. With a=r/(2|h|), the Laplace transform is Q_(n-1/2)(1+a^2/2)/pi, so the success probability is a times that transform and the stated normalization follows. The cosine and positive toroidal integrals have the same normalization: setting rho=exp(-eta), the cosine coefficient expands using the binomial series for the two factors (1-rho exp(±i theta))^(-1/2), and the positive integral with exp(-t)=rho*s reproduces those coefficients times pi via the beta integral. The success rate rq tends to zero at both ends for n>=1 (the fast-rate behavior is q~binom(2n,n)(|h|/r)^(2n)), ensuring an attained finite optimum. At alpha=na and beta=n eta, translation of the rescaled lower endpoint bounds the positive integrand by exp(-(s+beta))/sqrt(s(s+2 beta)), uniformly dominated on compact interior alpha intervals, and gives the K_0 limit. For a<=1 the global bound alpha^2 K_0(c alpha) tends to zero at both alpha boundaries; for a>=1 the bound C n^2 exp(-(n-1)c) tends to zero uniformly. Hence no sequence of global optimizers can escape. The derivative of R=alpha K_1/K_0 is alpha[(K_1/K_0)^2-1]>0; R ranges from 0 to infinity, giving the unique limiting optimizer and convergence for every minimizing sequence. Independent numerical calculation checked alpha=1.552651255645364 and constant 3.262211749335942; the frozen numerical script was inspected, not executed. Neither numeric check substitutes for compactness and the limiting proof.

## originality

PASS

Poisson probing, renewal, the single-trial lattice Bessel amplitude, and the Laplace/Legendre identity are not new. The checked literature and catalogue do not give the globally optimized large-distance theorem for this precisely renewed exponential one-shot protocol on the infinite line. The surviving claim is the compactness and sharp asymptotic for all global optimizers and their value, not priority for its constituent identities or a general advantage over other restart laws.

## value

PASS

This isolates a meaningful gap between ballistic propagation and physical first-detection time in a specified renewal experiment. The sharp quadratic law and rate give more than a formal stationary point or an upper estimate at one chosen rate: every physical-rate optimum has the same scaling, with no unexamined parameter escape. That distinction is useful for comparisons among explicitly different quantum detection protocols.

The dated certificate retains the supplied scientific assessment, sources and limitations.

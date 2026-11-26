# Independent mathematical audit

## correctness

PASS

For the stopped OU search with generator f''−kx f', reset-position law is r g_r(x)dx, and one Brownian-return cycle succeeds with p=phi_r+rJ>0, including hits during return. Cycles regenerate at 0 and finish almost surely. In the renewal transform the denominator tends to p; the defect in the sum of all one-cycle transform terms is rI sqrt(s)+o(sqrt(s)), since the negative-side exit transform is exp(x sqrt(s)), the positive interval has bounded exit mean, and killed occupations inherit bounded Gaussian moments from the unconditioned search. A monotone Tauberian theorem yields K/sqrt(pi t), including divergence at the endpoint alpha=1/2. I also checked the confined limit independently by the OU time change: for start −a the Brownian clock is (exp(2κt)−1)/(2κ); integrating the reflection-principle survival and setting v=κt bounds the rescaled mean by a sqrt(2/pi) times the integral of (exp(2v)−1)^(-1/2), which is pi/2. Dominated convergence gives the same limiting constant sqrt(pi/2)a. For 0<x<1 a bounded-interval exit calculation (or the barrier x(1−x) for κ<=1) keeps that contribution bounded, and the scale-function success tends to x. Dividing the mean cycle duration by its success probability gives the claimed coefficient. Discounted Dynkin applied to x gives phi_r=(r+k)(I−J), so K=1−k phi_r/((r+k)p) lies strictly between zero and one. The no-reset search mean is the finite OU hitting-time Green integral, unlike the free-return mean for each positive r. The frozen numerical verifier was inspected, not executed; the proof, rather than a grid extrapolation, settles both limits.

## originality

PASS

Credit prior work for the same two-stiffness model, the mean renewal equation, and standard Brownian and OU exit identities. The distinct result assessed is the exact free-return total-completion tail, its half-moment endpoint, and the identification of its explicit model-dependent amplitude with the correctly evaluated weak-confinement singularity. The positive-stiffness MFPT formula is not an independent novelty claim.

## value

PASS

The unconfined phase can destroy all completion moments of order at least one half even though the search alone has finite mean. The exact same nonuniversal amplitude controls how the mean becomes singular when that phase is weakly confined. This quantitative separation is useful for comparing stochastic-reset protocols in a standard model; it is not implied merely by knowing a Brownian hitting-time exponent or by reporting an exact positive-stiffness mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.

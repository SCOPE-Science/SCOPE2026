# Scientific review: priced continuous-time corona mixing

## Correctness — PASS

The proof is analytic, not experimental: spectral gap concavity justifies averaging every feasible nonuniform allocation; block diagonalization yields the exact two-rate spectrum; strict convexity yields the unique orbit-constant optimal rates and value. The cyclic case uses both Fourier Fiedler modes to prove every pendant and rim rate must equal its optimal common value. The limiting formulas follow from \(\lambda_n=4\sin^2(\pi/n)\). The standalone standard-library checker independently passed 1549 finite tests, but finite tests are not an all-parameter proof.

## Originality — PASS on the inspected literature

Sun–Boyd–Xiao–Diaconis's 2006 continuous-time formulation covers the general maximin model and its SDP, not the solved corona-specific rates; Boyd–Diaconis–Parrilo–Xiao (2007) optimize discrete-time stochastic SLEM. Shakeri et al. (2015) optimize only interlayer couplings with fixed layers; Suzuki (2013) and Liu–Shao (2022) provide graph spectral information rather than a full priced optimization. The distinctive claim is the exact two-price transitive corona solution and the uniqueness over all independent cyclic edge rates, not the general spectral-gap program or corona spectral factorization. A relevant specialist prior result may still exist, so global priority is not certified.

## Mathematical value — PASS

The theorem gives a closed optimization benchmark for arbitrary transitive cores and demonstrates a non-obvious global rigidity phenomenon for cycles. At fixed aggregate budget the rim rate, pendant rate and spectral gap decay on distinct orders, and the exact cost balance identifies a size-dependent infrastructure design crossover. This addresses a motivated design gap rather than a parameter renaming.

## Boundaries

No claim is made for all-asymmetric uniqueness on noncyclic transitive graphs, arbitrary stationary distributions, nontransitive bases, discrete-time SLEM, or optimal hitting times. Verification remains internal and independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.

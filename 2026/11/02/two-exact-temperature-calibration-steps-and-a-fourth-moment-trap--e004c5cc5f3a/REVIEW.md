# Scientific review

## Correctness: PASS

The source rRKN formula reduces exactly to an independent random-affine recurrence for the harmonic position under full momentum refresh. Its second coefficient moment factors as \(1-zD(z)\), with \(D\) strictly decreasing, providing a necessary and sufficient finite-variance stability interval by contraction and stationary moment identities. Algebra identifies exactly two target-variance calibrations. Strict convexity of the Gaussian characteristic function shows the stationary law is not Gaussian. The exact fourth-coefficient moment, reduced modulo the calibration polynomial, shows fourth-moment finiteness at the lower root and divergence at the higher root. The supplied checker passed 245 checks, but neither finite testing nor simulated convergence substitutes for the proof.

## Originality: PASS, qualified

Bou-Rabee–Kleppe's 2023 full arXiv article provides the rRKN 2.5 force rule and single-step uHMC structure, and illustrates Gaussian-target bias numerically; its Gaussian invariant calculation in Remark 1 concerns the Verlet comparator. It does not state the exact two-rRKN calibration roots or the finite-variance/infinite-fourth-moment separation. Bou-Rabee–Marsden 2022 uses a different lower-order randomized integrator. Available mathematical-record searches matched other Langevin harmonic covariance studies but none for the same rRKN coefficient recurrence and the two moment-class boundaries. Mathematical publication priority remains uncertain because a specialized exact harmonic computation may exist elsewhere.

## Value: PASS

Exact temperature calibration is a natural diagnostic in unadjusted Gaussian-target Monte Carlo. Showing that a chain can match this target variance at two distinct steps while its invariant distribution is non-Gaussian, and at one step even lacks a fourth moment, demonstrates sharply why a second-moment convergence metric alone can conceal severe sampling bias. The larger step is a diagnostic counterexample, not a practical accuracy recommendation. This is a motivated, explicit stability/moment separation for a published time integrator, not an arbitrary polynomial root computation.

## Limitations

Only one harmonic dimension, fully refreshed momenta, independent triangular stage randomization and a single constant integrator step are covered. The maximum finite-variance step does not imply accurate Hamiltonian integration. No independent external validation or universal priority proof is claimed.

Self-review: passed. Independent audit: not yet performed.

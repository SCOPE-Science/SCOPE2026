# Scientific review

## Correctness — PASS
The scalar update factor was reconstructed directly from the two implicit source schemes. Multiplying complementary factors gives the stated rational pair multiplier. The exact identity \(|D|^2-|N|^2=-4\operatorname{Re}(z)(1+c|z|^2)\) proves strict contraction for the whole open left half-plane and neutrality on its imaginary boundary. Compactness gives a uniform contraction over each random stage for any fixed strictly stable \(z\). The small-imaginary expansion and fixed stage means prove necessity of complementary coupling; the covariance identity proves strictly positive imaginary-axis mean-square growth for every nondegenerate independent centered marginal. A packaged verifier confirmed the crucial symbolic identities and 2,652 supplemental rational-stage/complex-mode tests.

## Originality — PASS (qualified)
The motivating source (Bochacik–Przybyłowicz–Stępień, arXiv:2404.19059; BIT Numerical Mathematics 2025) explicitly uses independent uniform fractions, and proves a negative mean-square A-stability result. Its accessible complete preprint Sections 1, 3 and 5 contain no antithetic pair or coupling uniqueness statement. The present result modifies dependence without modifying marginals and proves a pathwise stability restoration plus a sharp uniqueness theorem. Earlier adjoint-composition research makes the deterministic two-step rational stability structure plausible prior art, and is credited rather than claimed as new. Dedicated searches for paired theta stages, complementary coupling, and randomized implicit Runge–Kutta A-stability found no direct covering claim in accessible primary sources or published mathematical findings. This is not proof of absolute historical priority; the full contents of some general composition references were not inspectable.

## Value — PASS
This addresses a documented and nontrivial limitation of an identifiable numerical method, using the same two numerical solves and one-step distributions. The contrast is exact: independent sampling has strictly increasing expected squared magnitude for every nonzero purely imaginary test parameter, whereas paired sampling has unit modulus at every block and contracts every strictly dissipative scalar mode for every realization. The necessity theorem demonstrates that the simple antithetic construction is not one arbitrary fix among pathwise stable centered couplings. The result is specific and usable as a stability design criterion, not a small numerical improvement or isolated parameter check.

## Closest literature and unresolved issues
- Bochacik et al., arXiv:2404.19059 (v1 publicly posted 2024-04-29), full accessible October 2024 text: schemes (S1)/(S2), independent uniform sampling, Facts 2–5 and conclusion. This source is the principal exact-method comparison.
- Blanes, Casas and Murua, DOI 10.1137/030601223: compositions of a method and its adjoint. Its established generic design principle partly anticipates the deterministic algebra, but the accessible abstract does not supply the fixed-marginal probabilistic uniqueness theorem. A historical equivalence in specialized composition literature remains possible.
- Barclay, Griffiths and Higham, *Theta method dynamics*: the accessible text covers the theta multiplier and period-two dynamics with fixed theta, not random complementary stages across steps.
- Higham (2000) treats mean-square stability for stochastic differential equations with stochastic driving noise; this is not identical to randomly selected stages applied to a deterministic ODE.

The result is restricted to the Dahlquist equation at completed pairs. No assertion is made that the source's global convergence-rate results survive the correlation change. Independent audit and validation have not yet been performed.

Self-review: passed. Independent audit: not yet performed.

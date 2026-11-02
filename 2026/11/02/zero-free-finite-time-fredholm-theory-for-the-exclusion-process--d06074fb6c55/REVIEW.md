# Scientific review: finite-time Bessel auxiliary kernel

## Correctness — PASS

The claimed domain is every finite \(s>0\) and every real physical \(\omega\ge-1\), with the weighted Hilbert space specified in the theorem. The Bessel-series factorization is an explicit positive nuclear sum, and density of polynomials proves injectivity rather than merely semidefiniteness. The gamma–Poisson mixture gives the explicit universal finite-window row mass \(\(q_s\)\); detailed balance and two Cauchy–Schwarz steps prove the weighted \(L^2\) operator norm bound. Positive trace-class spectral theory proves the real-negative Fredholm zeros and inverse estimates. Generalized Vandermonde determinants prove strict total positivity in every minor size, not just sampled sizes. Large-argument Bessel asymptotics prove the trace law. The 186 finite numerical tests in `verification_output.txt` independently check identities and normalizations; universal theorems rest on the proof.

## Originality — PASS (qualified best-knowledge)

The first-public 13 October 2026 work of Bénichou and Grabsch introduces the microscopic SEP one-body closure, the same auxiliary Bessel kernel, the persistence interpretation and a determinant representation. These are *prior* and not claimed here. The new theorem supplies an explicit weighted-positive spectral factorization, all-order strict minor positivity, a finite-time contraction bound, a physical-bias zero-free Fredholm domain and a convergence guarantee. Standard noncentral chi-square and classical Fredholm theory are acknowledged as general ingredients. Claim-level searches of related SEP work and published finding records revealed no encompassing assertion for this kernel. An incomplete comparison with the source supplementary material remains a priority risk; no absence-of-results claim is made for any uninspected page.

## Value — PASS

The motivating source represents its exact microscopic correlation solution through an auxiliary integral equation and an infinite determinant. The new operator theorem converts the physical-domain solvability and numerical conditioning of that representation into a global finite-time inequality with an explicit constant, ensures determinant denominators cannot vanish and supplies a convergent geometric solution method for every physical negative tilt. The strict all-order total positivity additionally constrains discrete approximations and reveals a coherent spectral structure; the \(\sqrt{s}\) trace growth measures how its effective spectral mass expands. These consequences address a substantive issue in applying an exact many-body reduction, rather than an arbitrary small parameter slice.

## Closest literature and limitations

- O. Bénichou and A. Grabsch, arXiv:2610.18626v1, https://arxiv.org/abs/2610.18626, exact source kernel and reduction. Inspected relevant main-text kernel, linear equation and determinant statements; supplementary coverage not fully resolved.
- A. Grabsch, D. Venturelli and O. Bénichou, *Physical Review Letters* 135, 137102 (2025), https://doi.org/10.1103/gwdh-3vqm, large-scale rather than this finite-window operator.
- Classical noncentral chi-square mixture identity, https://mathworld.wolfram.com/NoncentralChi-SquaredDistribution.html, a reused ingredient, not claimed as a discovery.

No optimality of \(\(q_s\)\), closed eigenvalue formula, eigenvalue simplicity, or physical asymptotic beyond the inherited microscopic equation is claimed. Priority remains qualified until comprehensive external literature review and an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.

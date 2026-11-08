# Scientific review

## Correctness — PASS

The weight and normalization have been fixed explicitly. The primitive identity follows from generalized Laguerre differentiation; the ODE and the Sonin envelope derivative follow by differentiation without unproved estimates. Strict envelope monotonicity identifies at most two critical-point candidates at every finite degree and the first critical point for \(\alpha\le-1/2\). For fixed \(\alpha\), standard locally uniform Mehler–Heine and Plancherel–Rotach expansions yield the sharp Bessel and bulk limits. The BV bound is sharp by a one-jump equality case. The sampled executable checker passed 655 tests, but these finite tests are not used as infinite proofs. Limits are not uniform under varying \(\alpha\).

## Originality — PASS with residual literature risk

The relevant 2026 Zhang–Liu–Xiang analysis concerns fixed prescribed singularities of Laguerre coefficients rather than a global sharp variation norm and its maximizing jump location. Its fixed-location conclusions do not logically determine the global maximum for each degree or the hard-edge transition. The generic primitive method and ordinary Laguerre case are acknowledged as existing, but neither implies the full generalized \(\alpha>-1\) classification. The later Sluchak preprint was available only at abstract level, so its possible unpublished overlap is an explicit unresolved risk. Targeted published-finding corpus searches did not identify an equivalent or stronger covering theorem; this is not proof of absolute novelty.

## Value — PASS

A complete, natural parameter classification of the sharp BV coefficient norm reveals a change of both exponent and location at the singular index \(\alpha=-1/2\). The finite-degree one/two-root reduction makes the optimal constant computationally accessible without global optimization. These features extend beyond routine evaluation of a single fixed-position coefficient and give a concrete boundary between Bessel and oscillatory bulk concentration.

## Scope and risks

The leading limits assume \(\alpha\) fixed, use unnormalized generalized Laguerre polynomials, and do not yield coefficient-level guarantees for other bases without the normalization conversion. Classical special-function asymptotics are cited rather than re-proved. Independent full-text priority review of earlier and very recent specialty papers has not been carried out.

Self-review: passed. Independent audit: not yet performed.

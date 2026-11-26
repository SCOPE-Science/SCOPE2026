---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Normalize a positive quadratic form by its smallest ratio to N². The resulting two-sided sandwich survives permutation averaging at no increase in squared distortion. The averaged positive form is a scalar multiple of I+t11ᵀ with t>−1/n. The uniform positive and opposite-coordinate unit vectors rule out t<0 by giving a ratio greater than 2. For t≥0 and max(‖x₊‖₂,‖x₋‖₂)=1, writing v for the smaller sign norm, Q≥1+v²+t(1−√(n−1)v)₊². Its minimum is exact at (1,−s,…,−s), s=t/(1+(n−1)t). For a mixed-sign vector the extremal sign-sum bounds reduce the upper bound to two convex quadratics in v, so an endpoint suffices. The uniform positive vector and the vector with n−1 equal positives and one negative attain the two candidate upper values. The resulting quotient switches at 1/(2√(n−1)); below that point the derivative numerator is H_n=c_n−2+2c_n(n−1)t+nc_n(n−1)t² and above it the slope is n−1. At the switch H_n equals c_n(1+√(n−1)+n/4)−2: negative for n=2,3, zero for n=4, positive thereafter. H_n(0) is negative at 5 and 6 and positive from 7 on. These signs and strict monotonicity where needed verify every minimum, exact values, and uniqueness only of the normalized invariant parameter.

## originality

PASS

The exact all-dimensional calculation, notably the n=5 and n=6 interior optima and the first dimension of Euclidean optimality, is distinct from the strongest inspected statements. Do not credit the known norm, the uniform upper bound, or the planar endpoint as stand-alone novelty: the planar value is implied by the nearby Day–James theorem and continuity.

## value

PASS

This determines a natural linear invariant of a classical signed norm, not merely its equivalence constant for the identity map. The sharp cutover at dimension seven, with two different regimes of tilted optimizers below it, distinguishes where the canonical Euclidean structure loses or attains optimality. The classified dimensions and the normalized optimal forms can serve as exact geometric comparison examples independently of the known planar limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.

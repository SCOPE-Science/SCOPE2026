---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Solving F(x)=y gives branches u(y)=y−y²/2 and 1−u(y), with absolute inverse derivative 1−y. The densities of the two preimages sum to 2, so the invariant density is 2(1−y), normalized on [0,1], and J has mass 1/4. Independently describe the sets directly in starting coordinates: for n≥1 the first n images miss J exactly when F(x)<u^(n−1)(1/2). On the decreasing right-hand branch this means x>1−u^n(1/2). Integrating the conditional density on this interval gives 4a_n², also valid at n=0. For example the first tail is 9/16; at x=1 the return is infinite, but that singleton has zero mass. The recurrence decreases to zero, and tail subtraction gives 4a_(n−1)^3−a_(n−1)^4. The identity a_n²=2(a_n−a_(n+1)) telescopes the mean to four; the reciprocal increments tend to 1/2, giving n a_n→2 and constants 16 and 32. The point-mass comparison with n^−3 gives the strict s<2 moment range, including the endpoint divergence and the trivial s=0 case.

## originality

PASS

Credit the source family, standard inducing estimates and recurrence analysis as prior methods. The verified distinct claim is the full measure-specific positive-integer return law at the neutral endpoint, with its exact normalization and tail factors. The strongest inspected family results exclude this endpoint, and the closest broad inducing theorem has structurally incompatible branch hypotheses. No priority claim is made for the normalized cusp map itself, its elementary invariant-density calculation in isolation, or the general phenomenon of polynomial return tails.

## value

PASS

This is the neutral continuation of a specified expanding cusp family, and the natural complementary half-interval isolates excursions through the neutral branch. The exact first-return distribution gives finite-time probabilities and a concrete normalized renewal-law input; the critical moment and constants show what changes at the boundary. The interest is not merely substitution of θ=0 or a familiar tail exponent: it is the all-index conditional law with exact measures of the return cylinders.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The 15 nonempty strict ranking types group into five by first choice. Independent Gamma(1) variables under flat Dirichlet prior imply first-choice totals Dirichlet(5,5,5) independent of within-C first-choice group. After C first elimination, the fractions transferring to A, B, exhausted have Dirichlet(2,2,1). Writing D=U_B-U_A, a Jacobian with T=U_B+U_A yields density f_D(d)=1-3d^2+2|d|^3, integrating to 1 and symmetric. B beats A iff D>(a-b)/c=delta; direct integration on delta..1 gives 1/2(1-delta)^3(1+delta) for 0<delta<1, zero for delta>=1, strictly less than 1/2. As counts grow with a>b>c, posterior group totals Dirichlet(n_i+5) concentrate while within-C transfer law remains unchanged, proving positive irreducible risk if a<1/2. Under separate six-full-ranking ballot prior, transfer U is uniform, yielding (1-delta)/2. Fresh independent symbolic integration checked normalization and the quartic identity; simulations are merely diagnostics.

## originality

PASS

Rosenman–Liang (2026) introduce the same 15-type flat-Dirichlet model and simulate winner probabilities from richer ranked responses, so model and conjugacy are prior. The inspected primary text does not derive the exact conditional B-upset quartic given only population first-choice shares, its infinite-poll risk floor or the different six-complete-ranking comparator. Indexed IRV paradox tables concern different unconditional culture models. This is a narrow, best-of-knowledge formula, not a distribution-free finding.

## value

PASS

How much uncertainty survives arbitrarily large cheap first-choice-only surveys is a natural operational decision quantity for ranked-choice polling. Exact positive Bayes-error floor, third-order majority frontier, and contrast of truncated/full ballot spaces have direct model-theoretic content. This is not a generic Dirichlet moment without an IRV elimination rule; external calibration remains entirely conditional on the specified prior.

The dated certificate retains the supplied scientific assessment, sources and limitations.

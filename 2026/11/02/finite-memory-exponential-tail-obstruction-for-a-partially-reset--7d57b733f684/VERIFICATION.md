---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The quadratic generator has LV=4-2(x-q)^2-rx^2, coercive for r,g>0, ensuring an invariant law with finite first/second moments and symmetry. Solving the exact reset-free linear SDE after (0,q) yields X_a=b_g(a)q+N(0,v_g(a)), with b_g=g/(g+1)(1-e^{-(1+1/g)a}) and v_g=2a/(g+1)+g²/(g+1)²(1-e^{-2(1+1/g)a}). Independently used symbolic differentiation and the matrix fundamental solution to check its mean and variance formulas, including t=0. Exponential-age conditioning at the last reset with bath preserved, Jensen bound E e^{sbQ}>=1, and v_g>=2a/(g+1) force MGF divergence at and beyond sqrt(r(g+1)). Restricting exponential age to [cz,cz+1] with bounded Q and optimizing rc+(g+1)/(4c) yields the tail lower bound; squeezing establishes zero Gaussian coefficient. The comparator has limiting variance (2r+1)/r and Gaussian quadratic log coefficient r/[2(2r+1)]. No matching finite-g rate or subthreshold MGF finiteness asserted.

## originality

PASS

Qualified best-of-knowledge comparison of actual statements with primary literature and published mathematical results; not a claim of exhaustive historical-priority verification.

## value

PASS

An order-of-limits obstruction for a natural physical stochastic-reset model: arbitrarily long no-reset excursions force heavier-than-Gaussian far tails at every finite memory, even though the motivating strong-memory quasistatic expression is Gaussian. Quantifies the exact moment-divergence barrier and lower-tail exponent without overselling a full tail asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.

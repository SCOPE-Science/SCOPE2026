---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Expanding the scaled T_3 polynomial gives the stated quadratic solution polynomial q_2. Its scalar values are positive on [mu,L], so q_2(A) has positive diagonal. For i!=j the exact A^2 expansion splits the off-diagonal into a nonnegative two-edge sum plus (-a_ij)[24(L+mu)-16(a_ii+a_jj)]; kappa<=3 makes the latter nonnegative. In two dimensions trace(A)=L+mu gives the stronger all-kappa sign formula. The sharp 3D block family has an explicitly negative q_2(A) off-diagonal for every kappa>3. Independent exact rational expansion reproduced the displayed kappa=4 matrix and negative witness.

## originality

PASS

Golub--Varga and later Chebyshev-iteration sources establish minimax polynomial acceleration and recurrence construction, but the inspected primary material does not state entrywise positivity of the degree-three solution polynomial on Stieltjes matrices, a condition-number-3 threshold, or the dimension-two immunity theorem. Broad and exact Resultary searches found no stronger theorem covering these coordinatewise conclusions.

## value

PASS

A sharp positivity boundary for a canonical minimax polynomial method is a natural structural question on Stieltjes systems. The all-kappa two-dimensional immunity and matching three-dimensional obstruction identify the precise first geometry where sign loss appears, giving more than a routine expansion of the Chebyshev polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.

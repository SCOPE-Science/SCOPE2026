---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Theorem 43 of Dilworth–Kutzarova–Ostrovskii explicitly gives uniqueness of the automorphism-invariant cycle projection for any Hamming alphabet; finite signed edge-permutation averaging then minimizes P for every ℓp and similarly its complement Q. The cut projection column Dᵀ L†b factors via the K_q eigenvector h and a radial Green kernel f=(qI+L_H(d-1,q))^-1 δ0 with integral formula. Its strictly decreasing radial coefficients enable the exact ℓ1 absolute sum of 2(q-1)/q for first-coordinate edges and (d-1)(q-1)/q for other directions. Transitivity/rank gives Q_ee=2(1-q^-d)/(d(q-1)), hence ||P||_1=1+||Q||_1-2Q_ee. Symmetry gives equal ℓ∞ norms. Independently built graph Laplacian pseudoinverses for H(2,2), H(2,3), H(2,4), H(3,3), H(3,4); both formulas match. The verification is bounded, but the integral/telescoping proof covers all d,q. Binary q=2 is acknowledged prior art.

## originality

PASS

The accessible primary manuscript Theorem 43 proves all-alphabet invariant-projection uniqueness but its Theorem 45 and Corollary 60 explicitly evaluate endpoint norms for binary cubes. The nonbinary closed endpoint formulas are obtained by a new radial Green-kernel edge variation, not by changing a parameter in the printed q=2 result. No identified stronger published covering formula in targeted result search.

## value

PASS

An exact infinite two-parameter projection constant for natural cut and cycle subspaces fills the evaluation gap immediately adjacent to the primary theorem specifically investigating Hamming graph projection constants. The formulas quantify graph-flow complementability beyond the binary hypercube and supply explicit simultaneously optimal projections.

The dated certificate retains the supplied scientific assessment, sources and limitations.

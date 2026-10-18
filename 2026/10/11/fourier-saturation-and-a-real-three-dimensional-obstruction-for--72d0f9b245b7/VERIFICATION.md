---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

First checked the joint norm and numerical radius definitions in Mal: on ℓ1, each single T has numerical radius ||T||, from a coordinate basis vector and a norming dual functional with prescribed matching phase on that coordinate. This gives universal w_p≥max||T_i|| and ||tuple||_p≤k^(1/p)max||T_i||. For unimodular q×q orthogonal U with first row ones (Fourier complex any q, Walsh real dyadic q), choose rank-one T_i x=x1·(1/q sum_r U_ri e_r); columns have l1=1, joint norm k^(1/p); Bessel ||(f(v_i))||_2≤1 for ||f||∞=1 and p≥2 gives w_p≤1, achieved by a column-matching phase functional with f(e1)=1. For k>m any equality would produce k l1-unit columns at an extremal coordinate with norming functionals f_i yielding Kronecker delta evaluation, hence k independent vectors in dimension m, impossible; finite-dimensional compactness of normalized matrix tuples yields strictness. For (3,3,2) real, sign-cube averaging forces each column entries ±1/3 and every sign quadratic evaluation 1; Fourier coefficients force VV^T=I/3, i.e. an impossible 3×3 real sign Hadamard matrix because odd-length sign rows cannot be orthogonal. Independent exact Walsh q=1,2,4,8 Gram checks, 512 sign-matrix exhaustion, and complex Fourier q=3 Gram check corroborate, but infinite-index clause follows only by embedding a finite rank-one block analytically.

## originality

PASS

Best-of-knowledge statement/implication assessment: The explicit Fourier–Walsh orthogonal-column construction, finite-dimensional biorthogonal rank obstruction, and sign-parity contradiction provide new statements not deductions from the existing general bound or k2 special case. Relevant primary exact-object sources and indexed findings were checked by object, invariant and quantifiers; inaccessible plausible material is retained explicitly as risk, not treated as automatic scientific rejection.

## value

PASS

The joint numerical index is a natural sharp quantitative invariant of operator k-tuples. The theorem bridges the published ℓ1 two-tuple gap to arbitrary finite tuple sizes in complex dimensions and dyadic real dimensions, supplies exact dimension obstruction, and finds the smallest real–complex separation. These results are not mere reuse of a known ℓ∞ table because adjoints fail to preserve the joint norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.

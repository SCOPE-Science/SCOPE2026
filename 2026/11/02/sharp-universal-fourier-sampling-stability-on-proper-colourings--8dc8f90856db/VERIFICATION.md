---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The exact transfer matrix T=J-I has eigenvalues q-1 and -1, giving Z=(q-1)^n+(q-1)(-1)^n and the two-point correlations r_d. Their n-point discrete Fourier transform has the stated lambda_0 and lambda_k, each on q-1 independent nontrivial color-character sectors; the orthogonal constant has eigenvalue 1. The nonconstant modes are positive for q>=3; lambda_0 vanishes only on the ternary triangle. The odd/even frequency bounds and separate q=3,n=5 analysis establish the global exact squared condition number 3(4+sqrt(5))/2 with that unique extremizer, not merely a sampled maximum; Fourier inversion gives nearest-neighbour-plus-rank-one precision. Boundary cases n=3, q=3, even/odd n and q>=4 are treated. The companion finite checker was read, and independently enumerated small proper colorings agreed with moments and eigenvalues; these enumerations do not establish the universal inequality.

## originality

PASS

The zero-temperature Potts/chromatic transfer matrix and Potts covariance color sectors are prior art. The bounded primary reading and published-finding comparisons did not identify the simultaneous finite-n spatial Gram eigenvalues, q,n-uniform sharp condition-number extremizer, and rank-one precision correction. This is a qualified best-of-knowledge PASS, not proof of priority.

## value

PASS

The precise conditioning of the degree-one Fourier restriction on the canonical proper-coloring measure is a natural question in Fourier sampling and Potts correlations. It supplies a full spectrum, a unique worst condition-number pair and exact local inverse structure, not a routine restatement of the known chromatic polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

The claimed family is parametrized by orthonormal frames Q under tr(A²)=1 (Gibson–Saldanha–Tomei, Theorem 2). For B=A²>0, d_k=q_k^TBq_k>0 and Σd_k=1. Hadamard yields (det A)² ≤ ∏d_k, equality exactly when Q diagonalizes B; AM–GM yields ∏d_k≤n^(−n), equality exactly when every d_k=1/n. The constant-diagonal lemma is proved by picking a Rayleigh-quotient-c vector then compressing inductively at preserved mean trace, so the upper cube is attained even for repeated eigenvalues. SO(n) connected for n≥2 and sign-changing a column preserves volume, giving the full interval; polar cross-polytope volume is (2^n)/(n!∏√d_k), yielding the exact reciprocal spectrum and fixed Mahler product 4^n/n!. Correct all n≥2, A positive definite, tr(A²)=1; finite tests do not establish infinite scope.

## originality

PASS

Best-of-knowledge: Gibson–Saldanha–Tomei establishes existence and O(n) parametrization and the exact half-edge formula, not the range or extremal frame characterizations of Euclidean volume. Schur–Horn/constant-diagonal, Hadamard and AM–GM are classical tools but do not by themselves state the constrained geometric classification. Searches of published exact-result corpus and literature showed the same posted claim and other ellipsoid/polytope invariants, not a distinct prior theorem subsuming this spectrum.

## value

PASS

The complete volume image and equality geometry of the canonical tight Fuss family, including a uniformly available regular cube for every admissible anisotropic ellipsoid and its polar spectrum, answer a natural quantitative refinement of the known existence/parameterization theorem. It is a compact structural classification rather than a bare repeated inequality or arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

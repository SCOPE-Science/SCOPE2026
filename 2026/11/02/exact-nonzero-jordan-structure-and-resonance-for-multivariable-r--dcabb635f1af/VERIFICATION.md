---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS: Under Σ(N+1)^d|a_N|<∞ each homogeneous output row has rank D_d(N), nuclear norm ≤D_d(N)|a_N|sqrt(N+1), so trace-norm summation and finite triangular diagonal give Fredholm determinant and trace powers. Reducing transverse monomial spaces X_β give finite lower terraced row coefficients a_{i+|β|}; cumulative sums obey (λ−a_i)S_i=λ S_{i−1}. Every repeated nonzero λ on each line has exactly one eigenvector, hence a single Jordan block with repeat count; compact tail has no λ eigenvalue and is invertible off λ, so finite-head generalized λ-root space lifts uniquely. Counting β gives alg ΣD_d(n_i), geom D_d(max n_i), pole order number of repeats. Strictly decreasing adjacent ratios q(N+2)/(N+1) give at most two collisions and exact q_{n,m}. Independent sympy/rational finite Jordan ranks passed 26 checks (including triple collision); infinite spectral claims follow from compactness proof.

## originality

PASS

Best-knowledge PASS with significant priority risk. Pilla 2026 introduced these same multivariable Rhaly operators and transverse-line decomposition, credited. The accessible abstract and original package review indicate point-spectral inclusions and compactness, whereas the present claim is exact nonzero Jordan diagram and resonant multiplicities. However Pilla full text was inaccessible by lawful OA and the authorized institutional retrieval was blocked by a disconnected VPN, so equivalence/coverage is NOT excluded by snippets. Older triangular factorable-matrix Jordan theorems could also imply the one-dimensional step. Inaccessibility alone is not a scientific FAIL.

## value

PASS

PASS: Jordan multiplicity, resolvent pole order and resonance loci are natural nontrivial spectral invariants for the newly defined operator class. The result yields exact transition among nonzero spectral blocks in all dimensions and is not just a trace formula or numerical eigenvalue check.

The dated certificate retains the supplied scientific assessment, sources and limitations.

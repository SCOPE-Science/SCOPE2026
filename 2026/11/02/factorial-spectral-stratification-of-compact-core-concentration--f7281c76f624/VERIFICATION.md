---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Reconstructed the Fourier decomposition and positive generalized Gram forms H_m(s)_{ij}=s^{m+i+j+1}/(m+i+j+1). H_m(s)=s^{m+1}D_s H_m(1) D_s proves exact determinant ratio s^{q(m+q)}. Normalized t^m weight concentrates at t=1; y=m(1-t) has moments converging to h!, so orthogonal basis tends coefficientwise to normalized Laguerre polynomials. The dilation C_s becomes y->m(1-s)+sy; its upper triangular entries have leading powers a^{j-i} s^i/(j-i)!. Exterior kth minors have unique highest a-degree k(q-k), reciprocal-factorial Vandermonde determinant yields product top k singular values and successive factorial constants. Eigenvalue ratios tend to s, allowing counting by thresholds; the coefficients sum to zero, with finitely many negative angular sectors. Independently checked 24 exact rational generalized-Gram determinants and high-precision asymptotic ratios for q=3,4 and m=250,500; finite checks only corroborate the proof for m->infinity.

## originality

PASS

Best-of-knowledge acceptance for the precise final claim after separating prior-covered statements from new structural/quantitative content. Value and originality rest on asymptotic spectral stratification not initial Toeplitz decomposition or determinant by itself.

## value

PASS

For a natural compact radial projection in a poly-analytic Hilbert space, supplies complete sharp multi-branch spectral asymptotics and exact determinant laws, including surprising cancellation of opposite branch logarithmic corrections in the global counting function. Precise factorial constants and branch separation are nontrivial reusable operator-theoretic invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.

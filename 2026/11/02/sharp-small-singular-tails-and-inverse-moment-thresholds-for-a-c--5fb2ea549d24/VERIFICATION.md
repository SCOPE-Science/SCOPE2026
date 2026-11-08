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

Gram exactly [[L,conj(Z)],[Z,L]], eigenvalues L±|Z|. Near alignment, fix one phase and use m=L-1 independent uniform relative phases. Quadratic defect is 1/2 phi^T(I-11^T/L)phi with determinant 1/L and strictly positive spectrum; compactness excludes other contributing strata, scaling and dominated convergence give sharp ellipsoid volume coefficient. Layer cake gives sharp negative moment threshold and exact condition-number identity. Independently verified Gram spectral formula, small-ball coefficient and matrix determinants for L=2..7, with L=2 CDF check. Fixed L only, complex Gaussian comparator well justified by Schur complement.

## originality

PASS

The exact low-entropy circular sketch is from Lynch-Davies and Webb (2026), whose full Section 4.2 is about isotropy and numerical SVD rather than the two-row small-eigenvalue edge constant. Ryan–Debbah study joint growing-size Vandermonde moments; Kunis–Nagel deterministic clustered Vandermonde lower bounds. Directional-statistics random-resultant edge laws are an unexcluded equivalent antecedent.

## value

PASS

Sharp failure/validity of inverse-Gram moments at the first small sample sizes distinguishes circular phase sampling from familiar complex Gaussian sketches. This has practical import for when pseudoinverse-based expectations exist, while not asserting a full randomized SVD error bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.

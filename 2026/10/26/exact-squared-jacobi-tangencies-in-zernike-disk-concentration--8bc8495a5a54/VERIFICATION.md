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

For β>-1 and integer k>=1 let A=P_k^(0,β)(2u-1), B=P_(k-1)^(0,β+2)(2u-1), Q=P_(k-1)^(1,β+1)(2u-1). Orthogonality and endpoint normalization give A-uB=-(β+1)(1-u)Q/k and integration by parts gives Q-(1-u)Q'=kB. These imply u^β(A²-u²B²)=(β+1)/k² * d/du[u^(β+1)(1-u)²Q²]. Multiply by 2k+β+1, integrate from 0 to t, and use β>-1 for vanishing endpoint to obtain exact nonnegative square difference of the two normalized cumulative Jacobi energies. Q has exactly k-1 simple shifted interior roots, so k>=2 has exactly k-1 quadratic (not crossing) equality radii; k=1 strictly dominates. On the d>=2 unit ball, polar variables u=r² and β=m+d/2-1 show this is precisely fixed-total-degree adjacent angular Zernike eigenvalue comparison. Independently checked both contiguous identities and the differentiated factorization symbolically for β=-1/2,0,1/3 and k=1..4 (12 cases); finite tests corroborate but do not replace the all-real-β orthogonality proof.

## originality

PASS

The available Greengard–Serkh report establishes the Zernike radial Jacobi basis and norms; Janssen studies radial-derivative bounds. The inspected primary material does not state the exact nonnegative difference of two cumulative squared modes or the complete k-1 contact count. These may follow from an older unindexed Jacobi integral identity; this is explicitly preserved as a priority risk, not asserted absent from all literature.

## value

PASS

The cumulative energy fractions of neighboring angular Zernike modes are natural spectral concentration invariants of a centered disk/ball. The perfect-square identity proves uniform angular ordering for every aperture, gives exactly k-1 degenerate equality radii, and excludes mode-order crossings without numerical root tracking. These are interpretable geometric consequences beyond routine computation of Jacobi polynomial norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.

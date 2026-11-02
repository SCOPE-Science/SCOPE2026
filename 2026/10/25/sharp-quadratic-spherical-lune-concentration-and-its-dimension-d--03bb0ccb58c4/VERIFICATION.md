---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For exact complex homogeneous harmonic degree 2, reconstruct the traceless-symmetric quadratic representation with t=x1²+x2² distributed Beta(1,(n−2)/2), φ independent uniform, and z-orthogonal fourth moments. The invariant decomposition has blocks span{t−2/n,x1²−x2²}, 2x1x2, x1 z_j, x2 z_j, and tracefree z-quadratics. The nontrivial normalized 2×2 Gram block is [[L,sqrt((n−2)/n) sin L],[same,L+sin L cos L]]/(2π). The remaining blocks have eigenvalues (L−sin L cos L)/(2π), (L±sin L)/(2π) with multiplicity n−2, and L/(2π) with remaining multiplicity (n−2)(n−1)/2−1. Its top branch crosses (L+sin L)/(2π) exactly at cos L=2/n, and the proposed eigenfunctions S+wC and x1z_j follow by unnormalizing the block eigenvector; the n=3 transverse zero dimension and complex eigenspaces are covered. A separate direct 1.5-million-point n=3,L=1 sphere-Monte-Carlo moment calculation reproduced the two-block entries within 3.01×10^-4, as corroboration only. The exact moments and matrix eigenvalue comparison, not Monte Carlo, prove all n and L.

## originality

PASS

The arbitrary-region spherical Slepian eigenproblem was already formulated by Simons–Dahlen–Wieczorek; the candidate contribution is its symbolic, sharp evaluation for quadratic harmonics on a non-axisymmetric spherical lune in ALL n≥3, with full multiplicities/equality cases and a dimension-dependent switching angle. The inspected general spherical matrix theory, higher-band hemispherical parity law, and polar-cap work do not imply the explicit wedge formula without a new invariant-block moment evaluation. Best-of-knowledge; a prior specialized low-degree wedge computation could have been missed.

## value

PASS

An exact whole-spectrum and optimizer change on a natural intersection of hemispheres is a meaningful spectral concentration invariant even at one fixed harmonic degree: it distinguishes zonal-like and mixed transverse modes and gives a sharp dimension-dependent threshold cos L=2/n. It is not an arbitrary sample value or generic eigenproblem restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.

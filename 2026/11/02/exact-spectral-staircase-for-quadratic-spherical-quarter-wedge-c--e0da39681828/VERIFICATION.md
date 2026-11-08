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

The normalized spherical Dirichlet moment recurrence M_{a+2,b}=(a+1)M_{a,b}/(d+a+b) fixes every Gram entry, including transverse-coordinate squares. The band of dimension d(d+3)/2 splits orthogonally under O(d−2) and x1↔x2 into scalar-symmetric dimension 4, scalar-antisymmetric dimension 2, (d−2) vector pairs plus (d−2) antisymmetric vectors, and traceless transverse quadratics of dimension d(d−3)/2; their dimensions sum correctly for d>=3. Exact determinant/inertia at lambda=1/4 yields two scalar above/two below, one in each vector pair, one antisymmetric-scalar on either side; trace and the explicit p_d=(1+sqrt(d)u)(1+sqrt(d)v) trial Rayleigh quotient >3/4 isolate a single simple top root. Gamma log-convexity yields eta²>1/16, so the upper transverse-vector root >1/2, while other non-top roots <1/2; all spectrum is strictly in (0,1) by polynomial unique continuation. Independently constructed unreduced Gram matrices for dimensions 3..11 (not just supplied reduced blocks) gave the precise four interval counts and simple top root on every tested d. These finite checks support, not replace, the all-dimension moment/inertia proof.

## originality

PASS

Best-knowledge PASS for the exact all-dimension two-perpendicular-cut *quadratic-band* spectral staircase and optimizer, not the general Slepian concentration eigenproblem or the one-hemisphere pairing. Primary Simons–Dahlen–Wieczorek develops general spherical-region Slepian theory; no exact all-dimension quarter-wedge block/inertia classification was identified. General cap algorithms may compute each d, but do not directly imply the listed symbolic multiplicity staircase without the proof. Risk: a specialized reflection-group concentration decomposition may already contain it.

## value

PASS

A natural second-degree spherical Slepian problem yields a nontrivial protected quarter-energy eigenspace, exact half-energy count and unique best mode in arbitrary dimension. The multiplicity staircase reduces a growing matrix to fixed-size blocks, relevant for localization and sampling. It is an exact structural spectral theorem rather than routine numerical matrix diagonalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.

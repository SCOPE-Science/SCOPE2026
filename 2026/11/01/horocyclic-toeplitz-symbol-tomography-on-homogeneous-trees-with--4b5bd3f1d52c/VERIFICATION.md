---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Uses the complete harmonic-wavelet basis of De Mari–Monti–Rizzo Theorem 14 for q>=2 alpha>1. Distinct wavelets cancel separately on each horocycle: disjoint cones trivial, same root orthogonal child zero-sum vectors, nested roots ancestral wavelet constant on descendants of lower root at each height while child-zero-sum wavelet totals zero. Descendants at level h(v)+m have total squared wavelet amplitude q^(m-1)[(1-s^m)/(1-s)]²; with weight q^(-alpha h), the normalized eigenvalue on root height k is lambda(k)=W(1)^(-1)sum_{m>=1} r^m(1-s^m)² phi(k+m), r=q^(1-alpha),s=1/q. Rational W(z)=r(1-s)² z(1+rsz)/[(1-rz)(1-rsz)(1-rs²z)] follows by three geometric series; shift S is invertible on l∞(Z) and all four factor inverses converge for r<1. Q(-z)=(1+rz)(1+rsz)(1+rs²z)/(1-rsz) has strictly positive Taylor coefficients, giving exact inverse l∞ norm kappa=(1+r)(1+rs)²(1+rs²)/[(1-r)(1-rs)²(1-rs²)], attained by alternating sequences; constants attain norm upper bound. Each horocycle has infinitely many roots, so every labeled eigenvalue has infinite multiplicity and sigma=sigma_ess=closure of its range; surjectivity gives block-constant diagonal C* algebra, no nonzero compact. Independently computed exact benchmark q=2,alpha=2: W(1)=10/21, W(-1)=-2/45, kappa=75/7. Infinite-dimensional completeness comes from the cited primary theorem, not finite-depth checks.

## originality

PASS

Comparison across equivalence, broader coverage, exact results and claimed implication finds no decisive existing result that covers the final scoped theorem in accessible inspected material; precise covered ingredients and full-text access risks are explicitly recorded. This is a best-knowledge scientific judgment, not an attestation of independence or a guarantee of historical priority.

## value

PASS

On a geometrically canonical homogeneous tree, this identifies the complete natural algebra of bounded horocycle-symbol Toeplitz compressions and solves the forward labelled spectrum and inverse symbol-tomography problems with an exactly attained, endpoint-degenerating stability constant. Distinguishing labelled eigenvalues from bare spectrum is mathematically necessary, not a cosmetic renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.

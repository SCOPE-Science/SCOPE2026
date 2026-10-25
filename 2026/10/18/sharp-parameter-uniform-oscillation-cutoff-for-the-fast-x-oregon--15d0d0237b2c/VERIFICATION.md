---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The fast-x root X_q(y) is positive with uniform bounds m≤X≤M, giving forward quadrant invariance and global bounded trapping. The equilibrium condition reduces to quadratic qx²+(q+f−1)x−(1+f)=0, with exactly one positive root. On 0<q<1, use y=x(1−qx)/(x−1), X' =−(x−1)^2/D, h'=N/D where D=qx²−2qx+1>0. The sign threshold occurs at q0(x)=(x²−2x−1)/(2x(x²−x−1)) for x>1+√2, maximized at unique c>1+√2 solving c³−3c²−3c−1=0. The resultant gives 10q_*³+6q_*²+12q_*−1=0. Above q* one has h'≥0, strict negative divergence, positive equilibrium determinant and sink, so Poincaré–Bendixson and trapping prove global attraction and no cycles. Below it choose x=c, f=(1+c)(1−qc)/(c−1), s=1 and ω=−h'/2 to construct a hyperbolic source and trapping annulus, yielding a positive periodic orbit. Independent exact symbolic derivative and resultant checks reproduced q*=0.07973231434646405, c=3.847322101863..., and negative h'(c) for three subcritical q. The finite checks do not replace planar theorems.

## originality

PASS

The theorem belongs to the fast-x square-root quasi-steady reduction, not full 3D Field–Noyes or fast-y Tyson/Llibre models. Same mathematical model Arizona teaching material gives the reduction and sample phase portraits, not an all-(f,s,ω) sharp q boundary. Llibre–Oliveira’s full accessible accepted preprint proves a cycle criterion for a different rational fast-y equation. Historical Field–Noyes and Troy full papers remain plausible access-limited overlap risks; none of their available cited statements settles the exact iff q threshold. Best-of-knowledge O PASS with explicit limitations.

## value

PASS

A parameter-uniform global nonoscillation threshold versus explicit existence of sustained oscillations is a natural bifurcation boundary for a classical chemical-kinetics planar reduction. Proving both sides by analytic divergence and a constructive annulus is more informative than parameter-specific Hopf numerics, and distinguishes the fast-x model from nearby but mathematically different reductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

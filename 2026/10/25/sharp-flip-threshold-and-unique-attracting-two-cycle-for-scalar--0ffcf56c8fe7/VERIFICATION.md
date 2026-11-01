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

Dimensionless map F(z,w)=(z-cg(s),s), s=βw+(1-β)z, g(s)=s/sqrt(1+s²), has unique origin fixed point. Direct Jacobian has determinant β and trace 1+β-d(1-β); Jury inequalities give c*=2(1+β)/(1-β). At criticality eigenvalues -1 and -β: transformed center coordinate has u^+=-u+t u³+O(u^4), yielding u_n^{-2}/n→2t for nontrivial center-manifold orbits and local full-state attraction, nonexponential. Momentum balancing an arbitrary two-cycle, not presuming symmetry, plus odd strict monotonicity of g forces opposite states and exactly one positive amplitude Z=t^{-1}sqrt((ct/2)²-1) for c>c*. The cycle Jacobian coefficient d=8/(c²t³)<c* satisfies strict Jury conditions; monodromy square is attracting. Independent Jacobian/eigenvalue and amplitude/stability computations checked 20 parameter choices including β=0 and β=.99. Higher periods and global basins not asserted.

## originality

PASS

The same mathematical model primary de Oliveira et al. arXiv:2609.30546 defines analytical Soft Muon and gives sufficient small-step convergence, but the accessible abstract does not state this exact all-momentum bifurcation and prime-two-cycle uniqueness. SoftSignum/SoftMuon published adaptive-quantile formulations differ from this fixed-ε two-dimensional recurrence. Published sharp transitions for hard Signum, fourth-root Polar Express, clipped heavy ball, or momentum SAM are different maps and cannot mechanically cover this normal form. Full same-model paper was inaccessible despite authorized attempt, so priority risk is material.

## value

PASS

A complete, natural local transition and exact attractive period-two classification at a modern optimizer’s simplest convex test problem; explains regularization-dependent oscillation and gives critical algebraic relaxation, with explicit separation from practical matrix polynomial method. Not a mere numerical period-two demonstration.

The dated certificate retains the supplied scientific assessment, sources and limitations.

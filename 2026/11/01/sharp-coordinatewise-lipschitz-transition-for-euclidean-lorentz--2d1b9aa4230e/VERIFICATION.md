---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Reconstructed the standard three-region Euclidean Lorentz projection and the middle-branch Jacobian 1/2[[1,u^T],[u,(1+λ)I−λuu^T]], ||u||₂=1. Since a Euclidean projection is globally Lipschitz, segmentwise derivative control and reverse local row-sign perturbations equate the supremum to maximal absolute row sum; axial A_d=(1+sqrt(d))/2. For spatial row i, a=|u_i| and Cauchy on other magnitudes bound the λ→1 endpoint by F_d=1+max[a−a²+sqrt(d−1)a sqrt(1−a²)]/2. g_d strictly concave and has a unique zero of g_d prime. Direct exact trial a=2/3 establishes F>A for d=2..4; strong concavity bounds max g5 below sqrt5−1 by positive margin 26sqrt5/45−229/180 and ∂d(sqrt(d)−1−g_d)>0 for d≥5. Thus exact switch, including d1 separate. Independent symbolic inequality and dimensions 2..15 check corroborate the all-dimensional proof.

## originality

PASS

Read Németh projection/duality results for the Euclidean cone; they study order, isotonicity and duality, not exact infinity row norms. Published Resultary planar ℓp-metric Lorentz projection treats a different projector/norm and cannot imply the all-d≥5 cross-norm threshold. An ℓ∞ metric projection onto Lorentz cone is not the Euclidean projector observed in ℓ∞.

## value

PASS

Cross-norm sensitivity of a canonical Euclidean conic projector is a natural quantitative condition-number invariant in conic optimization and stability. The previously non-obvious competition between axial and spatial output coordinates gives an explicit dimension-five threshold and exact low-dimensional formulas, not an arbitrary toy calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The exact support function of \(K_{d,m,a}\) is reduced in the proof to an angular minimum on a regular polygon's edge normals. On the two intervals split by \(t=1/(a\cos(\pi/m))\), when that quantity lies in \([0,1]\), the squared support inequalities are affine in \(t^2\). This proves the full support-function containment without sampling. The log-determinant is strictly concave. For the John contact measure, the planar covariance is \(I_2/d\) and the transverse covariance is \(I_{d-2}/d\); the first moment vanishes. The Löwner contact measure gives the same matrix after its explicit two-orbit weights.

The standalone program `verify.py` checks support inequalities for 96 parameter configurations, each over a 1001-point grid and seven additional angular directions; it checks the exact contact moment identities in both regimes and compares volume-ratio formulas. A separate numerical constrained optimization of the scalar log-volume was performed for these same 96 configurations, with agreement at better than \(10^{-5}\) in squared semiaxis coordinates where the optimizer converged. No external theorem prover or independent audit was used. Finite checks do not replace analytic quantifiers.

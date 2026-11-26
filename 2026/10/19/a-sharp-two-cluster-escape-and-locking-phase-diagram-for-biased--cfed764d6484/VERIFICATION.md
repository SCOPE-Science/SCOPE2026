---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The bounded Lipschitz convolution kernel gives a unique measure flow for the probability datum (the usual characteristic stability estimate controls velocity differences by the spatial distance plus the Wasserstein distance). In its invariant two-atom class the self terms are p·b/e and q·b/e in the two velocities before the common factor c, and their inclusion gives the exact gap and barycenter equations in lines 66–79. Uniqueness rules out finite-time collision. Differentiating R gives R'=2(F−1)/sinh²(2d); F' has the sign of 1−2d², F(0)=1, and F tends to −∞. Thus R starts at 0, has one strictly nondegenerate maximum, and then falls past 0 to −∞. Reading the signed level δbR−(2−b) gives all basins, including the semistable fold, the equal-mass frozen continuum at b=2, and strict shrinking for b=0. For δ<0 on the escape side the derivative tends to cb|δ|/e; the two collapse rates follow from j~2d and h−1~d². The fold uses the bias derivative 2/b_lock and gap curvature δb_lock R'', yielding the stated coefficient. Independently solving R'=0 and R=0 at 48-digit precision confirmed d*=0.907739233841074601..., R*=0.292182549800972871..., and d₀=1.555728630669671926...; with |δ|=1/2 and b=1.95 the signed levels reproduce the example gaps 0.103110814637206529..., 1.506831535033476222..., and 1.598639907304102643.... These numerical checks corroborate the example only, not the phase portrait.

## originality

PASS

The kernel, transport equation, homogeneous instability analysis and qualitative speculation about escape already belong to Koertje–Sayama. The distinct checked claim is the complete two-atom gap phase portrait, in particular the Gaussian level geometry, explicit mass-dependent fold, and orientation-sensitive basins and escape speed. No equivalent theorem was found in the material inspected; same-model thesis access is the main remaining risk.

## value

PASS

This is a natural exact test of the source paper's free-line group-drift question. It supplies the sharp initial-distance boundary and shows that orientation can give bounded translating locks instead of merely merger or drift, a qualitative distinction not observable from the homogeneous instability test. The finite-dimensional specialization is scientifically useful without claiming diffusive stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

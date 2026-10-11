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
# Verification

The finding is proved analytically. The following checks were carried out on the final claim.

1. The bicycle definition and index range were matched to the foundational source. For \(n=2m\) and \(k=m-1\), Lemma 7.1 applies to the two trapezoids indexed by \(i\) and \(i+m\).
2. The orientation calculation was reconstructed with lifted edge directions. The congruence obtained from the two isosceles trapezoids reduces to \(\alpha_{i+m}=\alpha_i\) because both strict-convexity turns belong to \((0,\pi)\).
3. Summing one period of turns gives exactly \(\pi\), so \(e_{i+m}=-e_i\) and the midpoint \((V_i+V_{i+m})/2\) is independent of \(i\).
4. After centering, the common side and diagonal lengths give \(s^2+d^2=2(\lVert X_i\rVert^2+\lVert X_{i-1}\rVert^2)\), hence the squared radii are \(2\)-periodic.
5. For odd \(m\), central symmetry shifts index parity and forces the two radii to coincide. Strict convexity places consecutive central angles in \((0,\pi)\), where chord length is strictly increasing, so equal sides imply equal central angles and regularity.
6. For even \(m\), the existence side was checked against Tabachnikov's Theorem 10: \(2m\) is even and \(m-1\) is odd.

Limits: no claim is made for degenerate convex polygons with collinear consecutive edges. The even-\(m\) construction is cited prior work and is not independently reclassified here. No numerical experiment or timeout is used as evidence for the infinite theorem.

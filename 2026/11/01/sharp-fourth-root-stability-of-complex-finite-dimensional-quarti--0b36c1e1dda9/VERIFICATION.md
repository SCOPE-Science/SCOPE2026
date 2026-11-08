---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Reconstructed equations (1)–(9) from frozen RESULT.md. Complex phase averaging of ∥u_j+e^{it}u_k∥_4^4 yields exactly 4S_jk and, using fourth-power distortion of the two-coordinate input, S_jk≤ε. Keeping each target row’s maximal column entry deletes fourth-power mass R≤∑_{j<k}S_jk≤Mε; Hölder on the source columns gives ∥A−A0∥≤d^(3/4)R^(1/4). Each remaining disjoint column has fourth power ≥1−(M+1)ε>0; normalizing gives a genuine isometry and the additive (M+1)ε bound. For Aδ(x,y)=(x,y,δ(x+y)), duality gives Δ=8δ^4. Any restricted isometry either has a zero column (distance ≥1) or zero third-row coefficient in at least one column (distance ≥δ); a displayed exact-isometric approximation has error δ+O(δ^4). This proves the limiting ratio 8^(−1/4) without relying on finite checks. Edge cases ε=0, d=2, n=d and complex phases are covered.

## originality

PASS

Best-of-knowledge: the closest 2026 primary theorem identifies exact restricted isometries by disjoint supports and unit columns, but supplies no perturbation-to-isometry quantitative bound. The older almost-disjointness-preserver framework has a positive-operator approximation theorem, and its near-isometry remark does not directly imply this arbitrary-complex, explicit fourth-root theorem with fixed-dimensional sharpness witness. Research index queries for quantitative Lamperti aliases returned unrelated quartic norms/distortions. No decisive stronger implication identified; an older general quantitative theorem remains a residual risk.

## value

PASS

The exact restricted-isometry theorem naturally raises robustness under noisy finite-dimensional ℓ4 norm data. This construction supplies an explicit, target-dimension-independent error estimate for arbitrary complex matrices and an unavoidable 1/4 loss demonstrated in the smallest nontrivial rectangular example. That pair of upper/lower results has mathematical use beyond reproducing a known exact classification; it is not a parameter substitution or trivial numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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
# Analytic verification of the exact counterfamily

The proof is analytic and has no essential external computation. The following checks can be repeated directly from the definitions:

1. The two-coordinate normalized circle covering measure \(2\sigma_1+2\sigma_2\) has total mass \(4\). If \(|z_1|+|z_2|=1\), each nonzero coordinate contributes illuminating measure \(2\times(1/2)=1\); a zero coordinate contributes \(0\). Therefore the minimum over all boundary strata is \(1\). If the block is interior, every support direction is locally inward.
2. For \(|z_j|=1\) in an additional disk coordinate, the independent measure \(2\sigma_j\) assigns weight \(1\) to inward phases. For \(|z_j|<1\), it assigns weight \(2\). Thus the product measure covers every point and has exact mass \(4\cdot2^{n-2}=2^n\).
3. At the selected hard point with active first-block coordinate \(J\), the directional right derivative is \(\operatorname{Re}(e^{-i\theta}v_J)+|v_{3-J}|\). Negativity has conditional probability \(\arccos(|v_{3-J}|/|v_J|)/\pi\) if \(|v_J|>|v_{3-J}|\), else zero. At most one of the two coordinate choices can qualify. The uniform choice gives probability at most \(1/4\).
4. Each of the \(n-2\) independent active disk coordinates contributes a conditional illumination probability at most \(1/2\). The exact bound is therefore \(2^{-n}\). Integrating any fractional cover against this test-point distribution yields its mass at least \(2^n\). No asymptotic approximation occurs.
5. If \(|z_1|+|z_2|\) were a maximum of finitely many \(|a_kz_1+b_kz_2|\), the continuum of points \((1,e^{i\theta})\) would require finitely many coefficient pairs to cover a continuum of alignment phases, although each pair realizes norm two at at most one phase. This verifies the non-equivalence condition independently of the covering computation.
6. Dimensional boundary cases: \(n=2\) has upper/lower mass \(4\), with no disk factors; \(n=3\) has upper/lower mass \(8\), with one disk factor. The proof's formulas are exact for every integer \(n\ge2\).

Limits: These checks establish the stated exact values and non-equivalence only for the specified product family. They neither establish the universal conjectured inequality nor rule out an unindexed prior equivalent result. There has been no independent audit.

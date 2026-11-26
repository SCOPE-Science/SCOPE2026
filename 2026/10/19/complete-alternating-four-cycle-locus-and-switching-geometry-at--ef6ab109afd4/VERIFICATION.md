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

The affine LR return has B=A_R A_L, det B=de and det(B+I)=α. Distinct alternating second-iterate partners have difference in ker(B+I), even at the border, where the branches agree. Throughout the two-saddle region the linear system for the alternating period-two x-coordinates has determinant Δ=(1+d)(1+e)−ab>0 and numerators b+e+1<0 and a+d+1>0, so the point is strictly admissible and the multiplier assertion is well-defined. On α=0, a(−b)=(1−d)(1−e)>0. The case d,e>1 contradicts the strict saddle inequalities, and comparison to −(1+d)(1+e) gives 1+de>0. Then Δ=2(1+de), ker(B²−I)=ker(B+I) is one-dimensional (b≠0), and the fixed line of the alternating fourth return is P+tv. The two left and two right sign inequalities give exactly |t|≤min(−p,q(1−e)/a). The right phase is Q+tw; since a/(1−e)>0 and the strict interior phases have disjoint sign, the only period-two orbit is t=0; for t≠0, F² changes its point. The difference between right and left bounds is σ/[a(1+de)], including the equality case with both clipping inequalities saturated. At strict interior points the fourth-return transverse multiplier is (de)². For de<1 it is below 1 because de>−1 and nearby points stay in alternating cells; for de>1 transverse departure occurs locally. At de=1 the return is a nontrivial shear (not Lyapunov neutrality); the reverse phase has identical trace/determinant, and in the Jordan case conjugacy follows from invertible A_L. Independent exact-rational checks of endpoint orbits and quotient multipliers covered all nine combinations of clipping sign and transverse type, including singular branches (python3 /workspace/reviews/evidence/reproduce.py 2).

## originality

PASS

The general LR flip equation and the attracting Lozi slice of the continuum are covered. The supported distinct content is the full two-saddle weak LRLR segment classification with its exact clipping switch and transverse cases including the expanding and Jordan regimes. The comparisons did not establish equivalent coverage of that content.

## value

PASS

This gives the full extent and exact switching mechanism of the weak alternating family at a natural stability boundary, with examples of all three transverse regimes in the actual admissible parameter region. The result tells a researcher which border visit truncates the continuum and how the fourth return acts nearby; it is not merely the known multiplier criterion or a reparametrization of the attracting Lozi slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

The theorem is proved analytically in `RESULT.md`; no finite computation is used to infer an infinite statement.

The exact checks are:

1. Mean plus total mass on the four support points gives \(p_1=1/2-2\alpha+\delta\) and \(p_2=1/2+\alpha-2\delta\).
2. For \(0\le\alpha,\delta\le1/4\), every entry of the displayed transport matrix is nonnegative.
3. Every row and every column sums to \(1/4\), which makes the constructed \(A\) and \(B\) uniform on \([0,4]\).
4. The matrix totals on differences \(-3,-1,1,3\) are exactly \(p_0,p_1,p_2,p_3\).
5. The necessity argument uses regular conditional probabilities on the common fractional part; no independence between the original marginals is assumed.

`verify.py` performs supplemental exact-rational checks of items 1--4 on a grid containing every boundary face. Its output is included in `verification_output.txt`. The finite grid is not evidence for the universal quantifiers; those are discharged by the symbolic proof.

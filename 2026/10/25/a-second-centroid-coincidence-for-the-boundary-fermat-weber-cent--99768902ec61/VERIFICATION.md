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

The theorem concerns the arclength-weighted Euclidean distance integral on the three sides of the triangle \(\operatorname{conv}\{(-1,0),(1,0),(0,h)\}\), \(h>0\). Its proof relies on strict convexity, an elementary antiderivative, certified signs, continuity, and uniform asymptotics.

Run `python3 verify.py` with `mpmath>=1.3`. This checks \(B_h(1/3)\) at the exact rational heights \(1/10\), \(1/8\), \(1\), and \(2\) by outward-rounded interval arithmetic. Expected strict signs: negative, positive, positive, negative. It additionally reports illustrative solutions of \(B_h(q)=0\), a numerical estimate of the non-equilateral centroid-coincidence height, an equilateral symmetry check, and closed-form versus independent numerical-integration comparisons. The four interval signs certify the finite comparisons; numerical approximations are not interval uniqueness proofs, and the asymptotic and existence arguments are supplied in RESULT.md.

No external expert validation or independent audit was performed.

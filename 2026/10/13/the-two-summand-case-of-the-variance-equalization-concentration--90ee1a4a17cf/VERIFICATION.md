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

The proof is analytic and universal. `verify.py` supplies an independent exact-rational replay of all algebraic ingredients: the laws \(\nu^m\) and \(T(\alpha)\), convolution, the length-two concentration function, the variance formula, inversion of the variance parameter, and the final equalization inequality.

The checker verifies the identity \(\mathcal Q_2(\nu^r+\nu^s)=1/\max\{r,s\}\) for \(1\le r,s<25\), then checks the closed two-summand formula and strict equalization inequality on \(8001\) rational pairs spanning canonical cells through index \(18\). It also verifies the low-parameter example \((\alpha_1,\alpha_2)=(1/3,1/5)\), for which \(\alpha_*=11/45\), the unequal concentration is \(1/5\), and the equalized concentration is \(97/405\).

Final replay output:

`VERIFY_OK`

`pairs_checked 8001`

`example_alpha_star 11/45`

`example_lhs 1/5`

`example_rhs 97/405`

These finite checks are not used to infer the theorem on an infinite parameter set. The universal claim follows from the two-case proof in `RESULT.md`. The published premises are the definition of the extremal family and the fact that the central interval attains concentration for its sums.

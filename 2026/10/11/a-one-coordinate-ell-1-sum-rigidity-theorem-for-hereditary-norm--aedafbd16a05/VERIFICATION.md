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
Let \(E\) have a normalized \(1\)-unconditional Schauder basis. If \(E\) is not coordinatewise \(\ell_1\), choose a finitely supported \(a\ge0\) with \(\|a\|_E=1\) and \(\sum_i a_i>1\). Positivity and Hahn--Banach yield \(f\ge0\), \(\|f\|=f(a)=1\). An occupied index \(i\) has \(f(e_i)<1\). Flipping all other signs in both \(a\) and \(f\), and adjoining a scalar dual coordinate of value one, gives a norm-attaining pair with exact defect
\[
\|F^+\|\,\|x^+\|-F^+(x^+)
=a_i(1-f(e_i))>0.
\]
This is the universal analytic proof, not a finite enumeration.

The bundled `verify.py` checks exact-rational witnesses in the \(\ell_\infty^2\) square, a rational unit point of \(\ell_2^2\), the source-style octagonal plane, and a three-coordinate top-two norm. In each it verifies the primal/dual unit conditions and reports the positive-part HNAp defect. It additionally checks the direct coordinatewise \(\ell_1\) converse in finite test dimensions.

No independent audit or independent validation has been performed.

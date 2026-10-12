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

The proof was checked directly against the source formulas for Theorem 3.5, Theorem 3.6, Theorem 6.1, and Lemma 6.12 of arXiv:2609.39113v1.

Exact substitutions give
\\[
\\frac{6}{m(m-1)}<\\frac{2m}{3(m-1)(m-2)}
\\iff (m-3)(m-6)>0
\\]
for integer \\(m>3\\), and
\\[
\\alpha_m=\\frac{2(m-6)}{3(m^2-4)}.
\\]
The exact consecutive difference is
\\[
\\alpha_{m+1}-\\alpha_m
=\\frac{2(-m^2+11m+2)}{3(m^2-4)(m^2+2m-3)}.
\\]
The positive root \\((11+\\sqrt{129})/2\\) lies in \\((11,12)\\), so the coefficient increases through \\(m=12\\) and decreases thereafter. This proves the infinite-domain uniqueness claim analytically.

`artifacts/verify.py` checks the rational identities, the endpoint values \\(\\alpha_7=2/135\\) and \\(\\alpha_{12}=1/35\\), the improvement factor \\(27/14\\), and a wide finite range as a corroborative regression check. The finite range check is not used as proof of the all-integer statement.

The parameter \\(m\\) is an auxiliary symmetrization size used in the soundness analysis. The physical base tester in the source still consumes three copies per round. No exact general-\\(m\\) spectral gap beyond the source's lower bound is claimed.

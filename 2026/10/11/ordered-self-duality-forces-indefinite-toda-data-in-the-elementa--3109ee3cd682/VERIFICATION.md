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

The ordered dual exponent transformation is
\\[
( A,P,B,Q )
\\longmapsto
\\left(
\\frac{A+P+B+Q}{2},
\\frac{A+P-B-Q}{2},
\\frac{A-P+B-Q}{2},
\\frac{A-P-B+Q}{2}
\\right).
\\]
Subtracting the original coordinates shows that all four fixed-point equations are equivalent to
\\[
A=P+B+Q.
\\]

For a source sign sector with parameters \\(n_+=r\\) and \\(n_-=s\\), direct substitution into the two sign formulas shows that the number of negative \\(\\epsilon_j\\) is
\\[
\\left\\lceil\\frac{s}{2}\\right\\rceil.
\\]
This was algebraically proved in the result and separately sanity-checked over a grid of integer pairs.

On the fixed locus,
\\[
n^+_-=A+B,
\\qquad
n^-_-=A-B=P+Q,
\\]
so the total negative index is
\\[
\\left\\lceil\\frac{A+B}{2}\\right\\rceil
+
\\left\\lceil\\frac{A-B}{2}\\right\\rceil
=
A+\\mathbf 1_{\\{P+Q\\text{ is odd}\\}}.
\\]

The primary source's complete tau product contains
\\[
\\prod_{\\ell=1}^{A}
(1-q^{x+\\ell})^{A+1-\\ell}
(1-q^{x+1-\\ell})^{A+1-\\ell}.
\\]
At \\(x=0\\), only the second factor with \\(\\ell=1\\) vanishes, giving exact order \\(A\\). The positive-sign factors cannot vanish for real \\(x\\), and the half-integer negative factors do not vanish at zero.

No numerical experiment, finite enumeration, or external certification is used to prove the all-parameter statement.

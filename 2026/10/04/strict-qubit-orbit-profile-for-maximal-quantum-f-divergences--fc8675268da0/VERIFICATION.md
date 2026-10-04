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

The analytic proof uses only the two-dimensional overlap form of a unitary matrix, Cayley--Hamilton for a \(2\times2\) positive matrix, the standard integral representation of an operator-convex function, and positivity of the representation coefficients. The critical identities are
\[t(q)=t_{\min}+\Delta(1-q),\]
\[(A+aI)^{-1}=\frac{(t+a)I-A}{\delta+at+a^2},\]
and
\[\frac{d}{dt}\frac{(a+1)(t-\delta-1)}{\delta+at+a^2}=\frac{(a+1)^2(\delta+a)}{(\delta+at+a^2)^2}>0.\]

`artifacts/verify.py` replays exact-rational instances of these formulas, checks strict ordering on a rational grid, and checks the predicted small-angle coefficient numerically for a representative non-affine kernel. The script returning `VERIFY_OK` is corroborative; the finite tests do not establish the universal quantifiers.

The proof requires faithful states so that all inverses exist and nondegenerate spectra so that \(\Delta>0\). The affine-generator and degenerate-spectrum cases are explicitly excluded from the strictness claim. No statement is made about dimensions larger than two.

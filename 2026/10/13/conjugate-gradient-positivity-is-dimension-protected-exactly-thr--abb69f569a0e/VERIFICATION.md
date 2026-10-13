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

The universal part is analytic: the first CG iterate is a positive multiple of the nonnegative right-hand side; exact CG terminates in at most two steps in dimension two; and the explicit two-dimensional Stieltjes inverse is entrywise nonnegative.

The accompanying `verify.py` checks only the sharp three-dimensional witness with exact rational arithmetic. It verifies the Sylvester minors, exact inverse, exact solution, both CG step lengths, and the second-iterate vector. Its finite calculations are not used as a substitute for the universal proof.

Reproducible target values are:
\[
\alpha_0=\frac{21}{44},\qquad
\beta_0=\frac{2285}{1936},\qquad
\alpha_1=\frac{20108}{67599},
\]
\[
x^{(2)}=\frac1{3219}\begin{pmatrix}9076\9469\-32\end{pmatrix},
\qquad
A^{-1}b=\frac1{23}\begin{pmatrix}96\73\8\end{pmatrix}.
\]

No claim is made about finite-precision CG or preconditioned variants.

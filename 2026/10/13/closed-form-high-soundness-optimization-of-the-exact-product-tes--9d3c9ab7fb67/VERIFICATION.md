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

The proof is analytic and is given in `RESULT.md`.

The source's first exact rejection branch is
\[
R(\varepsilon)=\varepsilon-\varepsilon^2
\qquad
(0\le\varepsilon\le1/2).
\]
For \(a=1-\sigma\le1/(2\sqrt2)\), the optimizing boundary \(x+y=2a\) lies wholly inside that branch.

Two exact identities carry the optimization:
\[
\frac{d}{dx}\left[x-R(x^2)\right]=1-2x+4x^3>0
\]
on \(0\le x\le1/\sqrt2\), and, for \(x=a+z\), \(y=a-z\),
\[
R(x^2)+R(y^2)-2R(a^2)
=
2z^2(1-6a^2-z^2).
\]
Since \(|z|\le a\) and \(a^2\le1/8\), the second factor is at least \(1/8\). Hence the unique optimizer is \(x=y=a\).

The bundled checker reproduces these identities, checks the comparison with Proposition 7.1, and numerically evaluates the full piecewise Remark 7.3 objective on deterministic grids for representative soundness values. Those finite calculations are corroborative only.

The result does not claim matching lower bounds on actual QMA conversion soundness and does not cover lower soundness where further product-test branches can enter.

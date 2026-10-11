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
The packaged `verify.py` uses exact symbolic algebra to check the two stationary covariance identities and their factorized Cauchy--Schwarz boundaries.

It verifies
\[
\frac{1-\lambda}{1+\lambda}\le
\frac{\sqrt{\operatorname{Var}(X)}}{\sqrt{1-m^2}}
\le1
\]
and
\[
\frac{\gamma-1}{\gamma+1}\le
\frac{\sqrt{\operatorname{Var}(Y)}}{\sqrt{1-m^2}}
\le1.
\]
It also checks that the proposed lower-bound extremal points
\[
(-c,d),\qquad(c,-d)
\]
are exchanged by the two affine branches and that their branch membership is equivalent to \(d+kc>0\).

The stored execution output is `VERIFY_OK`.

The invariant-measure and equality-rigidity arguments are analytic. No finite orbit experiment is used as an infinite proof. The verification does not assert existence of any non-atomic invariant measure.

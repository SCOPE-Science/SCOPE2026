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
The packaged `verify.py` checks exact symbolic identities for the generalized Sprott J vector field.

It verifies
\[
L F=(z-by)^2-a y^2,
\]
\[
L G=y^2(y+1),
\]
\[
L(xz)=az^2-x^2+xy+xy^2,
\]
and
\[
y'''+by''+(a-1)y'+ab\,y-2yy'=0.
\]
Under the Wirtinger equality substitutions \(y''=-ay\) and \(y'''=-ay'\), it verifies reduction to
\[
-(1+2y)y'=0.
\]

The stored checker output is `VERIFY_OK`.

The checker validates the algebra. The measure proof additionally uses support invariance, and the period proof uses the classical equality case of Wirtinger's inequality.

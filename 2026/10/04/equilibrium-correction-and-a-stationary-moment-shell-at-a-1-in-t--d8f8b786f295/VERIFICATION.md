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

The equilibrium calculation was checked directly from the three differential equations before any division by \(1+x\). At \(x=-1\), the simultaneous equations \(z=xy\) and \(y+z=x\) would require \(0=-1\), so that value cannot represent an equilibrium.

Exact polynomial replay verifies
\[
x^3-(b+1)x-b=(x+1)(x^2-x-b)
\]
and, for \(F=x^2-2x-2y+2z\),
\[
\nabla F\cdot(-x+y+z,xy-z,-xz+y+b)=-2(x^2-x-b).
\]
The accompanying `verify_balance.py` performs these identities coefficient by coefficient using only exact integer polynomial arithmetic and prints `VERIFY_OK` on success.

The measure argument itself is mathematical rather than computational: compact support permits integration of the polynomial Lie derivative against an invariant probability measure, yielding the stationary identity. The script does not certify existence of any non-equilibrium compact invariant set, and no such existence claim is made.

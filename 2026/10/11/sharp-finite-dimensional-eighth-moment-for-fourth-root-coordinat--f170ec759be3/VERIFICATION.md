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

The analytic proof rests on the exact identity
\[
\|F\|_8^8=24S^4-72S^2Q+18Q^2+64SR-34U+|T|^2
\]
and the strict smoothing bound
\[
144-76A-192u+60u^2+16t\ge12.
\]
These establish the universal statement.

The bundled `verify.py` performs finite corroboration: it checks the identity on five exact integer-coefficient cases and the equality family for \(2\le n\le6\). Its expected terminal line is:

`VERIFY_OK identity_cases=5 extremizers=5 max_states=4096`

Finite enumeration is not an exhaustive proof for arbitrary \(n\).

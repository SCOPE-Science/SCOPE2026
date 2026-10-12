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

The universal proof is contained in `RESULT.md`.

The attached `verify.py` checks every integer
\[
2\le n\le1{,}000{,}000
\]
with
\[
\Omega(n)\le3.
\]
It factors each integer, computes
\[
\tau(n),\qquad \sigma(n),\qquad \varphi(n)
\]
from the factorization, tests the defining divisibility directly, and independently evaluates the stated residue criterion for the appropriate factorization shape.

The verifier asserts equality of the direct and predicted predicates for every tested integer and reports counts by multiplicity layer.

This finite replay is corroborative only. The theorem is unbounded because the proof handles each possible factorization shape symbolically.

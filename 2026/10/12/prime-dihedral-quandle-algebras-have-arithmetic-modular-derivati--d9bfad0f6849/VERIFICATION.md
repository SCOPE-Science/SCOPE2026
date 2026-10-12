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
The proof is symbolic.

The packaged checker `artifacts/verify.py` verifies every displayed basis derivation for
\[
p\in\{3,5,7,11,13,17,19,23,31\}.
\]
For
\[
p\in\{3,5,7,11\},
\]
it independently constructs the full derivation linear system and checks that its nullity equals
\[
\frac{2(p-1)}{\operatorname{lcm}(\operatorname{ord}_p(2),2)}.
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.

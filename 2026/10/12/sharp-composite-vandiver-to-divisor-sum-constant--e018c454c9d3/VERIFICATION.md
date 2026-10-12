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

The proof is symbolic and unbounded. Its critical ingredients are
\[
V(n)\ge2\bigl(\sigma(n)+T(n)\bigr)
\]
and the sharp auxiliary bound
\[
T(n)\ge\frac87\sigma(n),
\]
with the latter proved by the complete split \(\tau(n)=3\), \(\tau(n)=4\), and \(\tau(n)\ge5\).

`verify.py` uses exact integer arithmetic for every composite \(n\le100000\), reconstructs all divisors, and checks
\[
7T(n)\ge8\sigma(n),\qquad V(n)\ge2\bigl(\sigma(n)+T(n)\bigr),\qquad 7V(n)\ge30\sigma(n).
\]
It also compares ratios exactly by cross multiplication.

Recorded output:

`VERIFY_OK`

`limit=100000`

`composite_cases=90407`

`minimum_ratio=30/7`

`unique_minimizer=4`

`auxiliary_equality=[4]`

`theorem7_equality_cases=65`

The finite computation is regression evidence only and is not the infinite proof.

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

The exact verifier `verify_m3f2_decomposition.py` was executed from its delivered package path.

It checks all 512 matrices in \(M_3(\mathbb F_2)\), independently enumerating the 58 idempotents and 22 square-zero matrices and obtaining exactly 380 sums. It separately enumerates all 168 matrices in \(GL_3(\mathbb F_2)\), constructs the conjugacy orbits of the four proposed exceptional representatives, checks orbit sizes 42, 42, 24, and 24, and verifies that their union is exactly the complement of the decomposable set. It also checks explicit decompositions for the ten nonexceptional rational-canonical types.

The replay output is:

`VERIFY_OK`

`idempotents=58 square_zero=22 decomposable=380 nondecomposable=132`

`bad_class_sizes=42,42,24,24`

The exhaustive computation is finite and exact; it is used as an independent replay of the algebraic classification, not as a substitute for the proof. No claim beyond \(3\times3\) matrices over \(\mathbb F_2\) is verified.

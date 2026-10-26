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

The direct checker enumerates centralizers over \(\mathbb F_2\) and \(\mathbb F_3\), independently detects idempotence, and reconstructs the image Jordan types from linear-algebraic ranks. It does not assume the orbit-stabilizer formula when computing observed counts. Checks include the \((a,b,m)=(1,2,2)\) centralizer over \(\mathbb F_2\), containing \(1048576\) matrices.

Run `python3 check_idempotent_jordan.py` in a directory containing that script. Compare the final line with `check_idempotent_jordan_output.txt`. The output lists all tested parameter configurations and spectrum counts. These finite tests neither prove the general counting theorem nor establish the asymptotic total-variation bound; the proof is provided in `RESULT.md`.

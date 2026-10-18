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

## Reproduction
Run `python3 verify.py` in a directory containing this file and `verify.py`. The script checks, by exact integer arithmetic, every reduced-generator coefficient possibility for odd indices through 2049, even indices through 1024, the finite modular residues used in the proof, and independent Apéry shortest-path computations for index values 3–11. The expected result is `VERIFY_OK`.

## Verification limits
The infinity of cases is resolved analytically by the inequalities and congruences in `RESULT.md`, not by an exhaustive finite program. The classical three-generator symmetry and gluing criterion is taken from the cited literature; the program is not an independent proof of that external theorem. An independent mathematical or priority audit has not been performed.

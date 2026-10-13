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

# Verification details

The mathematical proof is fully symbolic. A separate ordinary checker is included as `checker.py`. It uses exact modular arithmetic in a prime field to test Boolean-kernel ranks and direct Jacobian quotient dimensions for the explicitly enumerated small cases and prints reproducible output recorded in `checker_output.txt`.

To repeat the checks, place the two standalone files in the same directory and run `python3 checker.py`. The output file is an observational log, not a substitute for the all-size Boolean interpolation, reduced-gradient-chart, and representation-theoretic arguments.

Independence has not been evaluated. Neither the public data nor the checks establish historical priority. The claimed equivariant Specht decomposition holds over \(\mathbb C\); characteristic-positive cases and full graded module multiplication are not claimed.

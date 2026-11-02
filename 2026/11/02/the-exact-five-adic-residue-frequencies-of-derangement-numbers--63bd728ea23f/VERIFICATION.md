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
# Verification notes

Run `python3 verify.py` with standard Python 3. The script implements the recurrence modulo each \(5^k\), checks all \(2\cdot5^k\) indices for \(1\le k\le6\), asserts the exact frequency formula for every target residue, independently checks the derivative table by polynomial arithmetic and checks minimality of periods as well as the omitted residues modulo four and nine.

Expected final log line: `VERIFY_OK derivative_table=5 residue_censuses=1..6 period_minimality=1..6 small_prime_obstructions=4,9`.

This is not a proof of the theorem at arbitrarily high powers. The unrestricted proof is supplied in `RESULT.md`, based on convergence of the falling-factorial series, the difference-quotient unit law and Hensel digit lifting. The previously known period formula is attributed to Miska (2015). No independent audit has been performed.

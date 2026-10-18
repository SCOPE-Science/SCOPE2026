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

The included `verify.py` has no nonstandard dependencies. Run `python3 verify.py` from the extracted scientific package to check the exact finite table and independent four-label minimization on the listed small rook graphs.

The script independently enumerates every maximum independent hole placement, checks the color set appearing in every empty vertex's open neighborhood, and compares with the closed formula. For \((2,2),(2,3),(3,3)\), it instead also exhausts all assignments of \(\varnothing,\{1\},\{2\},\{1,2\}\), recording their actual minimum and multiplicity.

The output is saved in `verification_output.txt`. These finite tests are not a proof for arbitrary parameters. The proof is in `RESULT.md`. No independent audit has been performed.

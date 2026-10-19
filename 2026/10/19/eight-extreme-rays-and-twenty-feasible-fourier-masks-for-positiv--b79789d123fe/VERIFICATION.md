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

Run `python artifacts/verify.py` using Python 3's standard library. The script enumerates 2002 eight-by-eight rational systems, proves via the active-set criterion that there are precisely eight feasible vertices, verifies each of the twenty strict frequency-support masks and rejects all the other 235 nonempty masks. It prints `VERIFY_OK`. The exact finite base case and the all-dimensional proof use different reasoning: the character-restriction reduction is analytic. The checker does not supply an independent mathematical audit or prove that no earlier work contains an equivalent theorem.

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

Run `python3 wheel_verify.py` using the Python standard library. The actual check in `checker_output.txt` passed 421 exhaustive all-spin energy and ground-state multiplicity comparisons for rim lengths 4–16 and 448 separately implemented min-plus transfer comparisons for lengths 17–202. All fields are exact rational fractions, and the tested set includes the predicted first crossing, saturation, both neighboring perturbations, and intermediate fields.

The theorem's infinite-family conclusion comes from the cycle lemma and hub-sector comparison in `RESULT.md`; exhaustive finite enumeration and finite dynamic-programming runs are auxiliary consistency checks only. No external certification or independent audit has been performed. The closest specialized 2023 paper on Ising-wheel degeneracy was not readable in full, and historical priority is consequently uncertain.

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
# Reproduction and verification

The calculation is a finite exhaustive theorem certificate for the permutation step, not a Monte Carlo sampling. Run `python3 verify.py` with Python 3.9 or newer. No dependencies, remote services or supplementary inputs are required. The script constructs the ten unordered 3+3 splittings, the fifteen pairings, and all sixty incidences. It verifies that each node is in six pairing planes and each plane contains four nodes, computes actions of all 720 permutations on all three sets, compares orbit distributions with the eleven-row claimed table, and independently compares fixed-point counts of powers with counts inferred from the cycles.

A verified run of the supplied exact code prints the eleven spectra and concludes `VERIFY_OK`, as recorded in `verify_output.txt`. The proof that all finite-field forms in scope have the stated arithmetic behavior is separately given by the trace splitting and Frobenius-descent argument in RESULT.md. Exhaustive finite group calculations do not by themselves certify the prior mathematical literature, the geometric identification, or independent validation.

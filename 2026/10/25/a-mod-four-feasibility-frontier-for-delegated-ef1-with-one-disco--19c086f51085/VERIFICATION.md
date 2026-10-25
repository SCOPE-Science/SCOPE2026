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

# Verification of the inventory frontier

Run `python3 verify.py` using Python 3. The only dependency is the Python standard library.

The script enumerates all nonnegative four-part count vectors summing to each inventory size, with a proven filter discarding vectors whose maximum and minimum counts differ by more than one. It subsequently computes the individual EF1 comparisons directly from each agent's own strictly positive per-good value, computes each center's own realized utility, and compares this with the optimal hypothetical reassignment of the other center's goods after deleting one rival good. This independently checks the finite parameter grid against the closed formula and evaluates equality and nearby discount thresholds.

Observed execution: 1,122 exact-rational parameter checks for all inventory sizes from 4 through 80, plus explicit boundary and nonmonotonicity assertions; all passed. Re-running the script prints the count and witness vectors for the first inventory sizes.

The logical proof uses no computationally unverified infinite step. The enumeration is finite and does not establish the formula outside the tested grid; the universal quantification follows from the exhaustive symbolic four-case proof in `RESULT.md`. Neither the comparisons against external literature nor independent scientific review can be certified by this program.

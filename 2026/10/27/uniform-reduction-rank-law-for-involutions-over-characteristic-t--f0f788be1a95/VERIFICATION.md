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

# Reproduction and scope

Run `python verification/check_involutions.py` from the package root; Python standard library is sufficient. The code constructs field multiplication for GF(2) and GF(4), enumerates every coefficient pair for each dual-number matrix, checks the involution equation and reduction rank, and compares all resulting rank histograms against the formula. The recorded output in `verification/check_output.txt` includes the five histograms, checks integer formulas in dimensions one through eleven for the binary field, and terminates with `ALL_DUAL_NUMBER_INVOLUTION_RANK_CHECKS_PASSED exhaustive_elements=327956`.

The direct finite computation is not a proof for arbitrary dimension or field. General correctness rests on explicit centralizer coordinates, orbit-stabilizer, and an Euler-product tail inequality. No independent audit has been performed.

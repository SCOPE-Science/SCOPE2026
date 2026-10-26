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

# Reproducibility and limits

Run the included `verify.py` with Python 3.9 or newer. It uses only the standard library and constructs two-query outcomes directly from diagonal matrix–vector products; this verifies that the success definition and score are implemented as stated. The checker also evaluates the exact probability and contrast identities and compares them against reproducible simulations.

The real-Gaussian ratio distributions and the strict angular-success comparison follow analytically from the proof in `RESULT.md`. The script's finite trials and floating-point comparison checks do **not** establish the universal theorem, the exact global minimum of the contrast function, or uniqueness of any two-dimensional crossing points. The theorem deliberately does not require uniqueness. The precise contrast boundary is the global minimum of a displayed smooth elementary function; the decimal approximation is supplementary.

No independent scientific audit has been performed.

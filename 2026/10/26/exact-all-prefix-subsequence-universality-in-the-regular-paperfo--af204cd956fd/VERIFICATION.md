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

# Reproducibility checks

Run `python verify.py` with Python 3 and no third-party packages. The code reconstructs the regular paperfolding word by a folding recursion and separately by the odd-part arithmetic predicate, comparing 262143 symbols. It checks all four aligned eight-symbol templates under both reachable scanner states, including all nonempty proper prefixes; checks the proposed all-prefix formula for every length from 1 through 262143; independently enumerates all binary scattered subsequences needed to determine the universality index for each prefix from 0 through 28; checks dyadic prefix values for exponents 3 through 17; and confirms both extremal discrepancies in this range.

Successful execution prints `VERIFY_OK` at its conclusion. The infinite theorem and sharpness are established in `RESULT.md` by the exhaustive aligned-block scanner argument; the finite checks alone cannot establish an assertion for all positive integers. The computations are reproducibility evidence, not independent mathematical validation.

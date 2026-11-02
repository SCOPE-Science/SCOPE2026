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

# Verification record

The universal statement through five pairs is certified by the paper's rank-incidence proof. No finite profile enumeration is being interpreted as a universal proof of that portion.

The specified six-pair preference profile can be reproduced by running the bundled Python 3 scripts in one directory, with no third-party dependencies:

```sh
python verify_witness.py
python verify_independent.py
python verify_small.py
```

The first script checks all 720 six-pair perfect matchings by direct preference-position comparisons, obtains the exact seven stable matchings, computes all twelve partner ranks per stable matching, and asserts the unique disjoint optima. The second independently computes blocking preference masks and the rank scores from inverse-position maps over the same 720 matchings. The third checks the simultaneous-optimum property for all 46,656 complete strict three-pair preference profiles; it is only an additional regression.

These scripts were executed successfully from their current source files before packaging, and each printed `PASS`. The independent scientific audit status is not performed. The exact data are one explicit instance, not a census of all six-pair instances.

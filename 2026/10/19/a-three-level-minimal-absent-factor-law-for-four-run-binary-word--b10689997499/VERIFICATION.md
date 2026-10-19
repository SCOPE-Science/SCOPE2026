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

# Reproducibility and limitations

The accompanying `verify.py` uses Python 3 and no third-party modules. Execute `python3 verify.py` in its containing directory. It constructs all minimal absent contiguous words by independent factor-overlap enumeration for all \(7^4=2401\) positive quadruples in \(\{1,\ldots,7\}^4\), directly tests each binary candidate in 310 cases with total length at most eleven, and checks 200 additional fixed-seed quadruples with run lengths at most fifteen. It checks **set equality** and the closed-form count. A successful run prints `FOUR_RUN_MAW_ALL_CHECKS_PASSED`.

These finite checks do not prove the infinite statement. The parameter-uniform proof is in `RESULT.md`, including the critical four-run factor shape, the classification of missing two-run corners, and the upper bound of four runs for minimal absent factors. The checked domain is the linear binary factor language (no wraparound). Independent audit and independent validation are not performed.

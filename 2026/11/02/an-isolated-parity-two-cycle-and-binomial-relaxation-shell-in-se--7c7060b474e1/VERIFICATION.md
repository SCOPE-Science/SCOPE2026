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

Execute `python3 verify.py` in a directory containing this file, `verify.py`, and `VERIFY_OUTPUT.txt`. The script enumerates 360456 labelled initial states in 78 dimension/threshold pairs with \(3\le n\le14\), checks the closed-neighborhood vertex update independently of the proof, and repeats checks over 196 nonidentity-update-order parameter tests. A successful run prints `SEQ_BITHRESHOLD_ALL_CHECKS_PASSED`. The recorded console output is supplied as `VERIFY_OUTPUT.txt`.

The infinite-family result follows from the explicit escape-band proof and Pascal's identity, not from testing finite examples. This check does not establish historical novelty or constitute independent review. It deliberately does not check other models or other parameter ranges.

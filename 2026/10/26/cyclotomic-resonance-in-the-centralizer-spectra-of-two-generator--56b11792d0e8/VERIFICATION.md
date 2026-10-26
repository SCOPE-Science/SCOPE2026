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

# Reproducibility and checks

Run `python3 qci_verify.py` with standard Python 3; no nonstandard dependencies. The script constructs all algebra basis multiplication products using `yx = zeta^{-1}xy`, creates each full commutator matrix, and computes rank by row elimination. It independently evaluates the valuation formula and histogram. Complete finite sweeps cover 158226 prime-field elements for ten parameter triples and 8704 elements in extension field F4 for four parameter pairs, plus 6000 direct-matrix random samples of larger cases. `qci_verify_output.txt` is the actual successful execution output.

The tests check finite samples and are not a substitute for the proof's all-field leading-degree argument. The source PDF for You–Zhang (2019), a possible overlap risk, was not available for full-text inspection. No independent audit has been performed.

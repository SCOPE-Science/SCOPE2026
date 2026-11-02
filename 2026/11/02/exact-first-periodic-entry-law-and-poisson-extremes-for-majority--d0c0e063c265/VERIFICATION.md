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
# Reproducibility and verification

Run `python3 verify.py` in a directory containing the two provided files `verify.py` and `verification_output.txt`. Python 3.9+ and only the standard library are required.

A completed execution of `verify.py` checks all \(65{,}528\) labelled spin configurations on sizes \(3\) through \(15\) against direct synchronous majority dynamics and the independent alternating-run prediction, including their eventual periods. For each size it then verifies the full cumulative distribution from integer matrix powers. It evaluates the finite-size CDF at selected sizes from \(256\) through \(2048\) and compares it numerically with the stated Poisson approximation.

The successful recorded output ends with `MAJORITY232_TRANSIENT_VERIFY_OK`. The direct simulation is finite and does **not** establish the infinite-window Poisson theorem or expectation estimate; those follow from the edge-erosion and factorial-moment proofs. Independent audit has not been performed.

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
# Reproducibility and bounds of verification
Run `python3 verify.py` in the directory containing this file; Python 3 standard library suffices. The script checks every \(\{-1,1,2\}\) assignment on seven small named-vertex examples, independently evaluates all feasibility constraints for every vertex, and compares those results with a separate blade-profile convolution and with the theorem's closed formula. The convolution also tests 77 parameter pairs through \(m=8\), \(t=12\). It prints the observed minima and exact counts for the direct-enumeration tests. The \(t=2\) tests are auxiliary and are not part of the asserted theorem. No numerical search is extrapolated into an infinite proof; the manuscript contains a complete universal argument.

No independent audit, external formal verification or publication-priority certification has been performed.

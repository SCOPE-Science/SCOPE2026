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

# Verification procedures and limits

The mathematical proof is in `RESULT.md`. The executable `checker.py` requires only Python 3 and can be run as `python checker.py` in the directory containing it. It independently constructs scattered-subsequence sets by a left-to-right finite-state expansion, rather than evaluating the five-coordinate signature to construct those sets.

A successful run reports `PASS: 10374 independently constructed spectra, 126 exact count comparisons, saturation tests, and depth-two boundary cases.` The deterministic checks compare each direct spectrum to its proposed signature for \(3\le k\le9\) and \(0\le m\le3(k-2)+5\), verify exact class counts, test sharp stabilization and selected long zero counts, and check the depth-two edge case. Separately, 500 random pairs were compared directly against the signature at depths up to 20 and at most 99 zeros; this extra stress test is not required to run the standalone checker.

Finite tests do not prove assertions for all lengths. The proof's exhaustion of the zero-, one-, and two-marker cases and its bounded-integer counting provide the all-length argument. There is no independently authored mathematical audit and no formal proof certificate. Historical novelty remains subject to independent literature assessment.

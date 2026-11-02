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

# Exact finite verification

Run `python verify.py` in a directory containing `verify.py` and `certificate.json`. `verify_output.txt` contains the recorded output of the included verifier. The verifier reconstructs every binary one-deletion set with **duplicate deletion positions coalesced**; checks each explicit lower-bound code; computes all rational dual objectives via the standard-library fraction implementation; validates every leaf and both branches of every internal proof node; and verifies the short-length VT-class comparison.

The two-list capacity results at lengths \(1\) through \(6\) each have one rational-dual certificate leaf. At length seven the two-list upper-bound tree has 101 nodes and 51 leaves; the independent one-list upper-bound tree has 25 nodes and 13 leaves. Both are checked from the actual included file bytes. The key mathematical inequality and its derivation are in `RESULT.md`.

This checks the **finite** assertions for these prescribed blocklengths. No external program has performed a mathematical audit of the theorem, and no assertion about larger lengths is verified or claimed. The verifier is an exact checker of the supplied certificates, not evidence of exhaustive literature priority.

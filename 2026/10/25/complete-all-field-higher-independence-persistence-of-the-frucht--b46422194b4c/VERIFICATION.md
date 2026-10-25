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
# Verification

Run `python3 verify_frucht_higher.py` using Python 3's standard library. No network requests, user data, or third-party packages are required. The program specifies every graph edge and recomputes all \(4096\) induced subgraphs at all twelve component-size thresholds.

The program enumerates full matching pairs, topologically sorts the complete oriented Hasse graph separately for each stage, reconstructs every signed integral Morse differential, checks every adjacent boundary product, and performs explicit unimodular pivot reduction to certify that all nonzero Smith factors are \(1\). It then computes persistent homology directly from the entire signed simplex boundary matrix in filtration order and checks all \(2048\) persistence pivots are units. A separate mod-two bitset implementation verifies identical pairings.

The required successful terminal output is `COMPLETE_VERIFY_OK`, preceded by `VERIFY_OK` and `MOD2_PERSISTENCE_OK`. This is an exhaustive finite certificate for the specified Frucht graph only; no asymptotic or all-graph claim is drawn from the program. The verified field-valued barcode uses strict positive interval length; the degree-negative augmented interval is excluded. Exact homotopy at threshold \(5\) is deliberately not asserted.

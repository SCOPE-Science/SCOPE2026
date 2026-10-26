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

The complete mathematical proof is in `RESULT.md`. Execute `python3 verify.py` without third-party dependencies. The recorded output is `verification_output.txt`. The proof, not the finite tests, establishes every integer parameter \(m\ge2\).

Direct enumeration checks all \(256\), \(4096\) and \(65536\) initial binary configurations for \(m=2,3,4\) respectively: \(69888\) cases in total. At each case the checker determines first periodic-entry time from actual graph dynamics, compares it with the cyclic-run formula, and counts recurrent states and primitive two-step return periods. It also computes cyclic-word transfer-matrix traces and checks the full cumulative entry-time distribution.

For \(2\le m\le8\), the checker verifies both graph snapshots are simple connected cubic graphs, verifies the one-step translation isomorphism, constructs all four recurrent mixedness templates for bounded exhaustive/prefix payload tests, and verifies that the \(m\)-fold two-step return map is the identity there. The finite tests do not establish the infinite family; that depends on the two exact lemmas for mixedness and payload updates.

Scientific scope: strict open-neighbor majority; phase-tagged two-snapshot dynamics; exact quantities are configuration counts and phase-augmented primitive periods. This is not an independently certified result.

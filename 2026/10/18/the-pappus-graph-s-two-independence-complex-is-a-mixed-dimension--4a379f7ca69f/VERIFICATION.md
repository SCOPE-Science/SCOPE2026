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

# Verification instructions

Run `python3 verify_pappus.py` with Python 3.10 or newer. No third-party libraries or external files are needed. The script reconstructs the Pappus graph from its standard LCF sequence, enumerates all vertex subsets and keeps those of induced maximum degree at most one, constructs the staged vertex-toggle matching, proves absence of cycles by a full topological sort of the reversed Hasse incidences, and computes the exact integral signed critical-six-to-critical-five Morse differential.

Expected: 20,651 nonempty simplices; 10,321 matched pairs; critical counts nine in dimension five and one in dimension six; 120,240 Hasse covers, with complete acyclicity verification; integral Morse boundary `[0, 0, 0, 0, 0, 0, 0, 0, 0]`. The direct augmented simplicial mod-two ranks are `[1, 17, 136, 626, 1768, 3038, 2980, 1447, 281, 27]`, yielding reduced Betti numbers nine in degree five and one in degree six. The finite-field calculation is a cross-check; the integral attaching map is established through exact signed Morse reduction and Hurewicz, not through mod-two evidence alone.

Independent external validation is not performed. No general assertion about other graphs follows from the exhaustive finite verification.

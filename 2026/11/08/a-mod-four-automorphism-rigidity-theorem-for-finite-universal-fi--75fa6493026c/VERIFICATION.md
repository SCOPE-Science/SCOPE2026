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

Execute `python verify.py` with Python 3.9 or later; no external packages or network are needed. The script enumerates all periodic de Bruijn cycles for alphabet sizes 2, 3, and 4, deriving their multiplication tables from the third-letter rule and testing every symbol permutation for automorphism compatibility. For each such table, it also tests all changes of one entry to a different value. The program independently constructs the quotient Euler-tour lifts with an involutive half-shift at cardinalities 2, 6, and 10; for cardinality 10 it tests the de Bruijn property and half-shift rather than all 10! permutations. Separate Euler tours at cardinalities 3 and 4 give direct trivial-automorphism examples. All assertions must hold.

`VERIFY_OUTPUT.txt` contains the actual standard output from package replay. The check is exhaustive only in the explicitly reported small ranges; the full theorem relies on the proof's centralizer, voltage, and Eulerian-lift steps. No independent audit is claimed.

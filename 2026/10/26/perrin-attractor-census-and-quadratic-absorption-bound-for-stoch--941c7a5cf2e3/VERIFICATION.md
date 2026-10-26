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

# Verification record

`CHECK.py` is standard-library-only. It was executed with Python 3 on the complete \(2^{n+1}\)-state systems for all \(3\le n\le11\). It constructs every legal single-vertex *change* (unchanged selections supply Markov self-loops that do not affect class membership), computes strongly connected components, retains only closed components, and compares all recurrent states against the proven length and density formulas. All instances passed; `CHECK.out` records actual output.

The arbitrary-size proof does not depend on code. In particular: a rim site has odd degree three, so its flips always lower the integer energy; the hub is the sole neutral coordinate and each energy plateau has at most two reachable states; the displayed two-state first-step equations bound plateau exit time; the energy decreases at least two per strict move and starts at most \(4n\). The cyclic gap-counting identity and transfer-matrix characteristic polynomial are derived in `RESULT.md`.

Limits: checks stop at eleven rim sites; a finite enumeration cannot establish the stochastic expectation bound for unbounded \(n\). This document does not report independent examination or external certification.

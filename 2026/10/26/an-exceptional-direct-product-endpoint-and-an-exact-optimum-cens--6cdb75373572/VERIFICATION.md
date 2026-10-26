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

The reproducibility artifact is the standard-library file `verify.py`. Execute `python3 verify.py` without third-party packages. It independently generates the direct-product adjacency relation, tests all three OITRDF axioms on every ternary labeling for the seven listed small graphs, and compares the minimum weights and exact minimum multiplicities with the theorem. On the two-row graphs it compares *all* weight coefficients, not just the minima, against the closed crown polynomial for \(2\le n\le6\). It also checks the formula's lowest-degree terms by exact polynomial arithmetic for \(2\le n\le9\). The expected minimum/count pairs are \((4,1),(6,25),(7,24),(8,40),(9,60),(8,108),(10,96)\).

The mathematical proof independently establishes the classification for every \(2\le r\le s\); finite verification cannot replace it. The earlier published scalar result for \(r\ge3\) is cited as prior work. The pre-existing \(C_6\) scalar is not claimed as new. No independent audit has been performed.

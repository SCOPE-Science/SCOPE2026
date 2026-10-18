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

# Reproducibility and scope

Run `python3 verify.py` in the directory containing that program. It uses only the Python standard library, builds adjacency lists for both cyclic layers, and applies legal forces until closure stabilizes. For every \(5\le n\le15\), it tests all \(\binom{2n}{4}\) candidate four-vertex sets for equivalence with the union of the five predicted symmetry orbits and all \(\binom{2n}{3}\) three-vertex subsets for failure. It separately checks the five orbit sizes for \(5\le n\le19\), and that every constructed four-set forces the entire graph for those values and for \(n\in\{20,30,50,100\}\). Recorded output is in `verification_output.txt`.

The computations are exhaustive only over the stated finite graph orders. The infinite theorem follows from the proved first-force case split and propagation argument. This file records the absence of independent validation and does not purport to supply such validation.

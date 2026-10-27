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

# Reproducibility

From the folder containing this document, execute `python3 verify_rdrd_cycles.py` with Python 3 and no external dependencies. The independent direct enumerator tests every map from each labeled cycle's vertex set to four labels for orders three through nine against the original local constraints. A separate 16-state weighted pair automaton evaluates the exact minimum-weight cyclic closed-walk count for every order three through 120. Both agree with the theorem. Output from the tested file includes: `PASS direct exhaustive enumeration and dihedral orbits: n=3..9` and `PASS independent weighted cyclic automaton: n=3..120`.

The dynamic program's state is an ordered pair of adjacent labels; an edge from `(a,b)` to `(b,c)` exists if the central label `b` satisfies the requisite conditions with neighboring labels `a,c`. Each edge carries weight `c`. Closed walks of length `n` correspond bijectively to labelings of the ordered cycle; the state and weight conventions count each rooted labeling exactly once. The exhaustive original-definition check does not use the structural classification.

These finite computations are confirmation rather than an infinite proof. The all-orders conclusion rests on the zero-pair and nonzero-label lemmas in `RESULT.md`. No independent audit was requested or performed in this package.

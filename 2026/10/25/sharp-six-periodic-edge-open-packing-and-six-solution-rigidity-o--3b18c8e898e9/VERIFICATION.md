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

The source file `verify.py` directly reconstructs all graph edges and all six construction types, uses pairwise conflict checks (not the manuscript proof) for small optima, and checks the six-solution equality census by separate exact cover. Run `python3 verify.py` with Python 3, NumPy, and SciPy installed. The recorded execution is in `verify_output.txt`.

- Constructed \(n=3,\ldots,999\) edge sets and checked their induced endpoint graphs are exactly disjoint stars of the claimed cardinality.
- Exhaustively enumerated labelled edge subsets for \(n=3,4,5,6\); maxima agree with the theorem.
- Solved an independently assembled integer model of pair conflicts to proven optimum for \(n=3,\ldots,36\).
- Enumerated exact three-centre coverings in one parity class for \(n\in\{3,9,15,21,27,33\}\), with six after the parity swap.

**Limits:** Finite computations corroborate but do not establish the unbounded theorem. The independent-audit channel has not been performed. The cardinality and rigid equality classification instead rely on the proof in RESULT.md.

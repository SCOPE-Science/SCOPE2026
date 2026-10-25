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

# Exact-rational verification

Run `python verify.py` after installing `requirements.txt` in an environment with Python 3 and SymPy.

The checker independently builds each incidence graph from its explicitly specified block collection, verifies that every pair of distinct points lies in one block, and verifies each constant replication number. It then inverts a grounded graph Laplacian over the rational numbers, constructs the canonical orthogonal cut projection on every edge, and checks the matrix symmetry and idempotence and the diagonal and exact real \(\ell_1\)- and \(\ell_\infty\)-endpoint formulas using absolute column sums. The six graphs comprise \(357\) checked columns; the graphs include different block sizes and multiple Steiner triple systems. Symbolic arithmetic separately verifies the summation and norm identities used in the proof.

Expected final line:

`STEINER_INCIDENCE_HODGE_EXACT_OK designs=6 full_columns=357`

This calculation establishes finite exact checks only. The unrestricted mathematical statement follows from the matrix identity and incidence-class count proved in `RESULT.md`. No external or independent mathematical audit has been conducted.

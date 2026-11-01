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

# Reproducible finite verification

Run `python3 check.py` with Python 3 and the standard library. The checker creates each full closed-neighborhood complex from the forbidden edges of the bipartite two-factor. It separately creates each side and their intersection, checks the intersection is the retained graph, checks that removing the apex centers exposes the side complexes, verifies the full two-skeleta, and calculates simplicial boundary ranks over \(\mathbf F_2\) using independent bit-vector elimination.

Expected terminal output: `VERIFY_OK 9 two-factors`. The nine tested cycle-length partitions are \((7)\), \((3,4)\), \((8)\), \((3,5)\), \((4,4)\), \((9)\), \((3,6)\), \((4,5)\), and \((3,3,3)\). Results agree with the stated degree-two rank, the high-dimensional rank, and the Alexander-dual side contributions.

The infinite and integral theorem is proved by the structural argument in `RESULT.md`; the binary-field tests alone do not establish integral torsion-freeness or unrestricted homotopy equivalence. No independent validation has been performed.

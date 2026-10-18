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
Run `python verify.py` with Python 3.10 or newer, without third-party packages. The script enumerates all vertex subsets, determines their independence status from lexicographic-product adjacency, checks the exact face count for each size, and computes reduced simplicial boundary ranks over \(\mathbb F_2\).

Cases: \((n,m)=(7,2),(8,2),(9,2),(7,3)\). Expected nonzero reduced Betti numbers are respectively \((\beta_1,\beta_2)=(1,14)\), \((\beta_2,\beta_3)=(33,2)\), \((\beta_2,\beta_3)=(23,18)\), and \((\beta_1,\beta_2)=(1,84)\). All four tests completed successfully when the package was assembled.

The general proof is a mapping-cone splitting, an explicit link decomposition into paths, and an exact cyclic-gap summation. A finite mod-two computation cannot certify an infinite homotopy assertion or exclude torsion by itself; torsion-freeness follows from the displayed integral wedge equivalence in `RESULT.md`. Independent external assessment has not been performed.

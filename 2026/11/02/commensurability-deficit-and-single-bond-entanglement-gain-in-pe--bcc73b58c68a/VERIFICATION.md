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

# Reproduction and limitations

Run `python checker.py` with Python 3 (standard library only). It reconstructs the explicit nearest-neighbor biadjacency matrices and computes exact Gaussian-elimination ranks over \(\mathbb F_2\). The included output reports 64 rectangle sizes and 703 single-edge rank checks with `PASS`. No precomputed output is used as an input to the checker.

Independent of that finite enumeration, the full theorem follows from (i) the exact graph-state Fourier-character Schmidt spectrum, (ii) factorization of the binary square-torus adjacency into commuting diagonal differences, (iii) the even intersection count of opposite diagonal orbits, and (iv) a rank-one perturbation lemma. The finite checker establishes neither historical novelty nor the universal quantifier; both are separately addressed in the proof and literature comparison.

This is a self-review, not independent scientific validation or external certification.

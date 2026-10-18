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

Checks: execute `python checker.py` from this directory with Python 3, NumPy, SciPy, and SymPy. The program forms arc supports directly and checks the number of recombination paths against the number of mismatch runs; it constructs the full one-skeleton of 17 small uniform layered networks and computes all graph distances by breadth-first search. Separate linear programs check adjacency for 661 vertex pairs across six profiles, and independent dense-matrix eigenvalue calculations compare the complete Laplacian multiset against the tensor formula for eleven profiles. Exact cofactor determinants verify the spanning-tree formula in the smaller profiles.

The universal assertions are proven in RESULT.md, not by these finite computations. No independent mathematical audit has been performed. The source comparison is limited by lack of access to the full 1992 Rispoli paper; its adjacency lemma is accurately attributed through the inspected 2020 preprint. Scientific novelty is therefore provisional pending wider expert review.

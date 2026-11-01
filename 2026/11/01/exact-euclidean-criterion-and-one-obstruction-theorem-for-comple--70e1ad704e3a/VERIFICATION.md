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

# Computational checks and limits

Run `python verify_multipartite.py` with Python 3, SymPy and NumPy. The checker was executed on the embedded source: it constructed unit-conductance complete multipartite Laplacians, inverted their shifted Laplacians over the rationals, reconstructed all effective resistances, and tested the exact quadratic-form decomposition. It also computed rational ranks and numerical eigenvalue signs of the complete centered matrix of squared resistances for sixteen named profiles; a census independently checked all 259 nontrivial part partitions with total size from two through twelve.

The checker completed with `ALL_MULTIPARTITE_EUCLIDEAN_CHECKS_OK` and no assertion failure. Exact rational arithmetic underlies its pairwise and selected-profile checks; the broader census uses floating-point eigenvalues with an explicit tolerance. All-order nondegeneracy, uniqueness of the obstruction, and the scalar boundary are established in `RESULT.md` by algebraic identities and an analytic Cauchy--Schwarz inequality, not by sampling. The source-date and originality conclusions remain subject to independent literature verification; no independent audit was performed.

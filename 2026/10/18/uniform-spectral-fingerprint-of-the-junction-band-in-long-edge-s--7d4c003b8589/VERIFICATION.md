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

# Verification of the regular-parent junction-band theorem

The complete proof and quantitative assumptions are in `RESULT.md`. Its critical analytic checks are: unique interior recurrence solutions for \(\lambda>2\), exact Chebyshev-to-parent reduction, a root near \(u=\sqrt{d-1}\) uniformly in \(\mu\in[-d,d]\), the Taylor remainder \(O_d(\ell(d-1)^{-\ell})\), and interlacing to prove exact eigenvalue count. The proof also checks multiplicities, ordering and the bipartiteness equality case.

Install the packages from `requirements.txt` with Python 3 and run `python verify.py`. The checker constructs direct adjacency matrices for six regular parent graphs (tetrahedron, complete graph on five vertices, complete bipartite graph with three vertices on each side, cube, triangular prism and Petersen graph). At edge lengths \(8,12,16\), it confirms the count and every eigenvalue above \(2\) against independently solved Chebyshev secular roots, evaluates representative asymptotic errors and checks the width. Its recorded output is `VERIFY_OK: 294 numerical assertions in six graph families`.

The finite computations cannot establish existence and uniqueness at arbitrary length, graph size, or degree; those conclusions are established in the analytic argument. Exact source-theorem citations and residual originality risks are given in `RESULT.md` and `REVIEW.md`. No independent audit was performed.

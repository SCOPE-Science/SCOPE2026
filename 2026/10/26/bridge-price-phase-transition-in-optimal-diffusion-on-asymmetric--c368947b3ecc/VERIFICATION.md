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

# Reproducibility and limits

Run `python verify.py` with Python 3, NumPy and SymPy. The included `verification_output.txt` contains the observed output from the packaged source; no external files or network access are required. The script checks exact rational identities for both branches, budget feasibility and strict positivity, eigenvector equations at each vertex, explicit positive-semidefinite dual edge distances, and the exact identity relating the two branch denominators for parameters through \(1\le q\le p\le13\). It computes all numerical eigenvalues and multiplicities for these cases, and performs 1,000 independently drawn asymmetric cost-feasible comparisons.

The proof of the universal theorem is in `RESULT.md`. The computational sample is not exhaustive over all integers or real costs. Symbolic algebra is used for the branch identity; exact rational arithmetic is used for the finite dual identities. Floating-point eigenvalues are independent numerical checks only, not certificates for infinitely many graphs.

The general proof depends on the standard Sturm oscillation ordering for four-node irreducible symmetric Jacobi matrices; its hypotheses (positive edge conductances, positive class multiplicities, monotone centered eigenvector) are stated and satisfied. Published general semidefinite duality is not treated as novel. Historical independent verification is not claimed.

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

# Reproduction and limits

Run `python checks/tree_hardy_checker.py` with Python 3, NumPy and SymPy. The checker passed **172** assertions in the reviewed environment. It verifies the exact \(\mathcal S_2\) and \(\mathcal S_4\) moment identities through symbolic algebra, factors the \(\mathcal S_4\) derivative exactly, tests the distinct optimizer inequalities for five branch counts, and compares closed expressions against two independent discretization procedures. Exact rational midpoint quadrature supplies further finite consistency checks.

The **proof**, not the computational checker, establishes all infinite-dimensional statements: integrate the common-root-path kernel, locate the unique quadratic-derivative root, express the operator norm through the first Dirichlet–Neumann–Kirchhoff eigenvalue, and prove the spectral characteristic root is minimal exactly at the half-length stem. Finite Nyström approximations cannot certify an infinite spectrum or global uniqueness; the checker is not an independent audit or a substitute for the analysis.

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

# Verification

The proof derives all formulas for every real symmetric finite base Hamiltonian and every uniform \(g>0\). The accompanying standalone `verify.py` uses NumPy and independently constructs the doubled Hamiltonian, computes its spectral projectors, forms their Schur squares, and checks the predicted block identity. It includes random symmetric simple graphs, paths, complete graphs and cycles with multiple coupling strengths. The result on the checked cases was:

`VERIFY_OK numerical_graph_cases=288 path_cases=48 clique_gap_cases=27 max_abs_error=2.010e-14`

The 48 path cases directly check rank \(m\), for \(1\le m\le16\) and three couplings; 27 complete-graph cases check the exact predicted smallest eigenvalue within a declared floating tolerance, for \(3\le n\le11\). The proof's nonstandard spectral noncollision step is checked analytically via strict derivative positivity; the kernel intersection follows from positive semidefiniteness and nonnegative quadratic forms. No finite test alone proves the theorem. The checker should be run as `python3 verify.py` with NumPy available; it makes no network calls.

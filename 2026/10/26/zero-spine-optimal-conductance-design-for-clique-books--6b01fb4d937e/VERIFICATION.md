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

# Reproducibility checks

Run `python verify.py` with Python, NumPy and SymPy installed. The exact terminal output from the package run appears in `verification_output.txt`.

The script directly constructs every graph edge of \(K_2\vee(mK_s)\), adds symmetric Laplacian contributions, and checks the claimed eigenvalue multiset against numerical symmetric eigensolvers for 30 integer parameter pairs \(2\le m\le7\), \(2\le s\le6\). It recomputes the minimum Kirchhoff index from the resulting spectrum, compares resource use against the exact budget, and verifies the positivity of the transformed KKT multiplier.

SymPy characteristic polynomials are exactly compared to the claimed factorizations for ten rational weighted examples, including both positive and zero hub-spine edge cases. Two additional examples compare the claimed Kirchhoff-index expression with the exact rational inverse trace. In six graph configurations, the exact proposed optimizer is compared against 500 randomly generated asymmetric budget allocations, for 3,000 finite comparisons.

The finite tests do not prove a universal theorem or establish exhaustive search optimality. The complete mathematical certificate is the spectral decomposition, strict convexity and analytic KKT inequalities proved in `RESULT.md`. No external or independent certification has been performed.

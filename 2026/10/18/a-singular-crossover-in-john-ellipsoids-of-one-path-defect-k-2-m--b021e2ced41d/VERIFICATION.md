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

# Verification of the John ellipsoid and the crossover law

The proof is contained in `RESULT.md`; the programs supplement rather than replace it. The exact positive root is substituted into a weighted Laplacian and the derived effective-resistance identities are independently tested.

Run `python checker.py` in an environment containing NumPy. It assembles full matrices for \(m=2,\ldots,15\) and nine different values of \(t\), totaling 126 configurations. For each it checks the pseudoinverse edge effective resistances, the trace normalization, and the entire positive-eigenvalue determinant against the matrix-tree formula. It also enumerates all spanning trees directly for seven ordinary graphs. Actual result: all 126 configurations and seven enumerations passed.

Run `python exact_checker.py` in an environment containing SymPy. It uses rational parameters and exact algebraic-number reduction, computes grounded Laplacian inverses without the analytic resistance formula, and checks every edge contact, a Laplacian cofactor against the tree polynomial, and the positive-multiplier normalization. Actual result: all five rational cases passed: \((m,t)=(2,1/2),(2,2),(3,3/2),(4,1/3),(5,1)\).

Separate direct numerical evaluations of the normalized volume at \(t=c/\sqrt m\) for \(c=0.1,0.5,1,2,5,10\) and \(m=100,1000,10000\) approached the stated scaling function. The universal asymptotic is proved by the positive-root limit and an explicit log-ratio expansion in `RESULT.md`; these finite evaluations are illustrative.

There is no machine proof or independent external certification. The verification state is self-reviewed only.

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
# Verification of crossing–nesting joint fluctuations

The complete standalone file `check.py` can be run using `python check.py` with the standard library and SymPy installed. It was executed against the same bytes included in this package.

The program independently enumerates all \((2n-1)!!\) perfect matchings for each integer \(2\le n\le7\) (respectively 3, 15, 105, 945, 10,395 and 135,135 matchings). For each matching it classifies every unordered pair of edges and checks the deterministic identity \(C_n+N_n+A_n=\binom n2\). It compares all three exact means and all nine covariance-matrix entries with rational arithmetic for every enumerated \(n\). It additionally uses exact symbolic integration on \(0<u<v<1\) to check both first-projection means, the first-projection covariance matrix \(I_2/45\), the zero cross projection, and the two canonical second moments.

Execution result: **PASS: 146,683 independently counted exact assertions**; all seven symbolic integrals and identities passed. No numerical tolerance, Monte Carlo approximation, or trusted external enumeration table is used for these checks.

The analytic proof of the infinite-parameter claims appears in `RESULT.md`. It rests on the exact symmetric iid order-two kernel representation, Hoeffding orthogonality, the fact that the canonical remainder has variance \(O(n^2)\), and the multivariate iid central limit theorem. The checker does not purport to validate asymptotics by enumeration, establish novelty, or serve as an independent mathematical audit.

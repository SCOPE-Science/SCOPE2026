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

## Reproduction
Run `python check.py` with NumPy available. The checker reconstructs the full normalized complex Fourier matrix, evaluates its smallest Gram eigenvalue, and compares it to the claimed two-by-two closed formula. It also tests adjacency optimality over complete finite periods, additional larger-period samples, monotonicity of the adjacent case, and the limiting constant.

## Observed finite results
`PASS finite assertions: 909`.
Limiting singular compression constant: `0.552915153292649`.
Uniform infimum of squared lower bound: `0.166762438881104`.
At period four, exact formula evaluation: `0.206646659708765`.

## Analytical checks and limitations
The main claims are proved for every integer period in `RESULT.md` by Fourier orthogonality, geometric sums, singular-value reduction, a strictly signed derivative inequality, and monotonicity. The numerical tests cover finitely many instances only. No independent audit was performed; no inference about arbitrary minority cardinality or nonperiodic patterns is claimed.

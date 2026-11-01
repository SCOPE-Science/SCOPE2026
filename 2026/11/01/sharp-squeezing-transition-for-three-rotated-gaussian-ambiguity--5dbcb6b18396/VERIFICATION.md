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

The proof uses exact evaluation of normalized Gaussian ambiguity integrals, radial monotonicity, a three-angle trigonometric inequality, and a scalar derivative sign argument. Critical nonstandard algebraic inequalities are displayed in `RESULT.md`; all variables range over \(T>0\), \(a\ge1\), \(y\ge0\) with strict derivative arguments on \(y>0\). Endpoints \(T=2\), \(a=1\), \(R\to0\) (excluded except as a limit) and \(T\to\infty\) are distinguished.

Run `python check.py` with SciPy available. The script tests 8,823 sampled and algebraically predicted comparisons. It cannot verify universal quantifiers, claims of originality or the complete nonlinear phase retrieval map. Independent audit is not performed.

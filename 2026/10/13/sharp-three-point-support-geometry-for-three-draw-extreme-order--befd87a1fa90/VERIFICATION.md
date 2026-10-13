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
The proof was checked symbolically after normalizing the support to \(\{0,t,1\}\), \(0<t<1\). Exact enumeration of all \(27\) ordered samples reproduces the five raw moments in `RESULT.md`. Substitution gives the stated covariance and variances, and exact simplification gives the displayed formula for \(\operatorname{Corr}(L,U)^2\). Differentiation factors exactly as claimed. The sign analysis uses only the facts that \(11t^2-11t-4<0\) on \((0,1)\) and \(791t^2-791t+380>0\) everywhere.

Running `python verify.py` in the package directory prints `VERIFY_OK`. The checker is finite symbolic verification of algebraic identities; the proof of the global maximizer is the interval sign argument in `RESULT.md`. No claim is made for nonuniform masses, supports with more than three atoms, or sample sizes other than three.

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

# Reproducibility and analytical verification

The proof is completely specified in `RESULT.md`. From the rates, it derives the frozen probability current, entropy production, the sharp quotient, and its derivative. The sign changes prove a unique maximizer for asymmetric equilibrium and a limiting maximizer for symmetric equilibrium. The rare-equilibrium expansion is proved using a strictly increasing equation in the reciprocal optimizer distance. The endpoint and normalization cases are explicit. These analytical steps, rather than finite evaluation, are the basis of the universal claim.

Run the included dependency-free `verify.py` using a standard Python 3 interpreter. Its observed output is `PASS: 96157 deterministic checks; largest tested grid has 999 points per case.` It exercises 16 equilibrium values, 3 relaxation scales, sign/endpoint/root properties, equality at each biased optimizer, every non-equilibrium point on a 999-point grid, equilibrium covariance, and asymptotic consistency at four rare-output scales. The observed example at \(q=0.1\) gives \(x_q=0.729394843024\) and \(sC(q,s)=0.197378005994\), versus \(s\tau_{\mathrm m}=0.09\).

Finite grid checks are not exhaustive; floating-point bisection and comparisons are diagnostics rather than interval-certified infinite-domain proofs. The scientific proof relies instead on the derivative sign and root-bracketing arguments. No independent validation has been performed.

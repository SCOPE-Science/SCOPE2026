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

# Verification details

The complete proof and its quantified domain are in `RESULT.md`. To reproduce independent **finite** consistency checks using Python 3.9 or later and no external packages, run `python3 verify.py`. Expected output is supplied in `verify_output.txt`. The checks reconstruct actual stationary solutions of the four-component original vector field at twelve edge strengths and four supercritical couplings each, and test strict positivity of the full gauge-fixed transverse Hessian. Additional tests cover exact rational flux identities, 900 scalar-derivative/Hessian determinant identities, the exact unique-root relation, the right derivative at the unweighted limit, and the strong-edge saturation.

Finite arithmetic or numerical sampling cannot establish uniqueness of all stationary branches, all-strength monotonicity, or the sharp infinite-parameter limit; these rest on the analytic reductions, branch bounds, monotone algebraic root and Hessian factorization in the proof. No independent external audit or independent validation has been performed.

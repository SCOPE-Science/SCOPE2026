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

# Verification record

The exact derivation in `RESULT.md` establishes the all-current statement. Specifically, it derives the conserved current combination, fixes its integration constant using the vanishing currents at infinity, shows that \(R'=-\sqrt{r(r+\alpha)}\rho\), integrates across the gas, and determines the dense profile and interface from flux matching. Branch inverses and their endpoints are ensured by the stated strict concavity conditions; no Monte Carlo data is used as a universal proof.

Run `python3 verify.py` with Python 3 using the standard library. The test evaluates five distinct concave gas flux laws, checks stationary normalization by Simpson quadrature, solves gas profiles by bisection and checks their local derivatives, and confirms different all-gas branch availability at fixed microscopic control values. All tests passed in the reported execution. Exact coefficients for the two benchmark current maxima and the universal \(e\)-ratio appear in the proof. Numerical error tolerances are encoded in the source.

No experimental validation or independent scholarly audit is included. A finite computation cannot prove the theorem for arbitrary nonlinear constitutive laws; that burden is carried by the analytic proof. The branch classification makes no claim about shock solutions or nonlinear dynamical stability.

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
# Reproduction and scope of verification

The companion `checker.py` is a standalone Python 3 standard-library script. Execute `python checker.py` in the directory containing this file and the script. It performs 5,434 exact-rational and numerical assertions, including exact two-route covariance identities on a rational parameter grid, numerical root/sign and asymptotic checks, randomized normalized-exponential-spacing simulations, and independent circle-center simulations. A successful reproduction prints `PASSED: 5434 exact-rational and numerical checks` and a critical intensity of approximately 1.79328213290076.

Scientific verification is analytic: the Dirichlet one- and two-point survival laws yield all required mixed moments; differentiating the factored covariance proves its unique zero; Taylor expansions prove the limiting threshold. The script is supporting evidence, not a formal proof or a substitute for the analytic argument. Floating-point simulations have finite uncertainty; they do not certify statements over infinitely many sample sizes or all arc lengths. The law for unequal arcs and the originality of any implicit consequences of early joint-transform work are not established here.

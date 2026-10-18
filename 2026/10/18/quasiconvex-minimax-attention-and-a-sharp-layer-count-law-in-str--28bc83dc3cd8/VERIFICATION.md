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

# Verification of opinion-blind multiplex attention design

Run `python verify.py` with Python 3.10 or later from the same directory as `RESULT.md` and `verify.py`. No third-party dependencies are required.

The actual package source performs exact rational checks of equilibrium first-order equations and the aggregated Nash identity over binary private-opinion profiles. It checks the equality between the original bounded-opinion risk formula and the squared-attention transformation under nonuniform stationary centralities and heterogeneous reporting costs. It checks equality witnesses in the rotated quadratic-cone constraints. For the distinct-layer, cost-contrast construction it checks \(81\) exact identities across sizes \(n=2,\ldots,7\), contrasts \(\delta\in\{1/3,1,2\}\), and every support budget. It checks \(534\) further rational attention perturbations against the claimed global lower bound, as well as strict proper-subset impossibility and full-layer cancellation.

The standard-library verification code ran successfully. Its assertions validate each test instance exactly, without floating-point tolerances. Arbitrary-dimensional correctness follows from the six-step proof in `RESULT.md`; the code is not a substitute for checking the underlying mathematical argument. No external scientific verification has been performed.

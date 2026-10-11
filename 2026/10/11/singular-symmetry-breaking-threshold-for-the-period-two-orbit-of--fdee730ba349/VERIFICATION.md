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
# Verification and reproducibility

Run `python3 verify.py` from the directory containing `RESULT.md` and `verify.py`. No external packages are required. The observed output ends with `VERIFY_OK; exact-rational and finite numerical checks: 421`.

The verifier uses independent algebraic identities over rational test inputs, obtains primitive two-cycle pairs by bisection in a logarithmic coordinate, numerically confirms the two forward-map equations, checks the exact multiplier product, and brackets the \(-1\) crossing on both sides. The sampled asymmetries are \(\delta\in\{0.1,0.05,0.02,0.01,0.005\}\); results for the first two values are informative experiments, not assertions that the unspecified universal \(\delta_0\) includes them. The test also samples the exactly symmetric case.

The computer tests do not certify uniqueness for a continuum of parameters, do not certify a global attraction basin, and do not establish the asymptotic expansion as \(\delta\downarrow0\). Those conclusions rely on the derivations in the proof. Floating-point arithmetic does not resolve exponentially small differences when they fall below machine precision; numerical equality of such values is not presented as exact equality. No independent scientific audit has been conducted.

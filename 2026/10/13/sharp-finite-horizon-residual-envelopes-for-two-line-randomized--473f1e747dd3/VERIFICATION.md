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

# Reproducibility and limits

Run `python3 verify.py` in the directory containing this document; Python's standard library is the only software dependency.

The check uses rational parametrizations of pairs of unit vectors and exactly enumerates every sequence of independent row choices up to seven updates for selected rational angles and three initial directions. It compares the resulting exact expected residual with the closed form. A separate rational identity test checks the derivative cubic. Numerical root tracking and long-horizon tests are additional diagnostics, not proofs of uniqueness or asymptotics.

On the provided program, the completed checks report:

`VERIFY_OK 1491 exact rational path tests; 783 exact derivative identities; 500 horizon roots; four asymptotic checks`

The analytic proof in `RESULT.md` is required for the continuous coherence interval, unbounded integer horizons, endpoint treatment, unique optimizer, and sharp asymptotic constant. No external independent audit has been performed.

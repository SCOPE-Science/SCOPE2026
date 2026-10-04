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
The package contains `artifacts/certificate.json` and the standard-library checker `artifacts/verify.py`.

The checker reconstructs the five-vertex wheel from its eight edges, verifies the stated lists of \(16\) primal extreme molecules and \(26\) dual extreme functionals, and recomputes all \(128\) norming extreme pairs. For each of the \(416\) extreme evaluations relevant to the operator norm, it checks an exact rational nonnegative dual combination of the numerical-radius inequalities with total coefficient at most \(2\). It then verifies the explicit equality witness \(T_0\) has numerical radius \(1\) and operator norm \(2\).

Run:

`python3 artifacts/verify.py`

Expected output:

`VERIFY_OK`

The finite certificate proves the exact polyhedral optimization once the standard facts used in RESULT.md are accepted: extreme points of a finite Lipschitz-free unit ball are molecules, graph incidence matrices are totally unimodular, and the numerical radius in finite dimension may be evaluated on norming primal-dual extreme pairs. No larger-wheel statement and no infinite-dimensional extrapolation is verified.

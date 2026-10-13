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

The exact proof uses only the published one-branch dispersion and elementary measure/algebra. The checker performs independent symbolic simplifications and numerical spot comparisons.

Run:

`python3 verify_density.py`

Expected final line:

`VERIFY_OK`

The script verifies: (1) the closed in-gap count \(4|m\eta|/(\pi|\eta^2-4|)\); (2) differentiation of the counting function; (3) the \(|\eta-\eta_c|^{-1}\) total-count coefficient at both critical couplings; and (4) the fixed-energy density coefficient. The samples are not used to justify any universal statement.

Limits not verified by computation: the existence and uniqueness of the guided fiber eigenvalue and the infinite multiplicity at criticality are published operator-theoretic inputs cited in `RESULT.md`.

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

# Reproducibility

Run `python check_transport.py` with the Python standard library. On the packaged source this executes 852 exact rational assertions across five ring/capacity choices, four rational deformations, two bias parameters, and all interior particle-number sectors, plus grand-canonical identities. It also verifies the exact finite-state master equation and normalized net current for each canonical sector.

The script prints the finite check count, a pair of complementary-sector currents, and a peak density. Finite exact computations corroborate but cannot exhaust the infinite parameter domain. The analytic proof separately covers all stated rates, capacities and particle counts. No independent audit or formal proof-assistant certification has been performed.

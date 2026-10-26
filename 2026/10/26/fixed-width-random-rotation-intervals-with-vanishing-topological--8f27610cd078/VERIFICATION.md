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

The executable `verify.py` uses the Python standard library and exact rational numbers. Its finite enumerations check: integer-periodic lift identity, displacement bounds and endpoints, equality of random-activation and deterministic sampled orbit point sets, and active-orbit lift equality. Run `python verify.py` and require the output line `FINITE_IDENTITIES_OK`.

The analytic proof uses the Bernoulli strong law and a published random rotation-interval theorem to pass from two explicitly realized endpoints to the full interval. The exact Bowen metric identity establishes the infinite-time entropy rescaling; the Lipschitz estimate supplies its vanishing upper bound. Finite checks neither substitute for those facts nor provide an exact formula for deterministic map entropy. Independent audit remains unperformed.

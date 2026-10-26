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

The pure-standard-library `verify.py` was run successfully and reported `PASS 18835 deterministic exact-rational/numerical assertions`.

Checks include exact rational beta moments and mean-square coefficient recurrences, the coefficient sign pattern over many finite indices/dimensions, 4,950 rational-probe trials using exact diagonal two-level Rayleigh products, the signed location of the dimension-three risk crossing, and the strict explicit dimension-two risk ratio for sampled parameters. All inputs, normalizations and formulas are present in the standalone source.

Limits: Finite sign checks do not prove a universal parameter statement. The analytical coefficient increment inequality, the single-sign-change argument for dimension three, and the exact dimension-two integral are the actual proofs. The displayed decimal crossing is numerical, with existence/uniqueness provided analytically. No independent external scientific verification was performed.

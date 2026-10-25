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

Run `python3 verify.py` using Python 3's standard library. The expected message is `VERIFY_OK finite_extremal_instances=91`. The program computes the exact finite residue-signature invariant for all decorative words over alphabets of sizes two through four at the documented small periods and all corresponding window sizes, compares the extrema against the closed formula, and checks cyclic de Bruijn witnesses. It also checks an individual nonextremal example and a period-twelve witness.

These exhaustions verify only stated finite test ranges and do not prove universal claims; the proof is the analytical phase decomposition plus de Bruijn extremal argument in RESULT.md. No machine formalization or external independent audit has been performed.

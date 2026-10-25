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

# Reproduction of the exact finite claims

Run `python3 verify_q4_integral.py` using Python 3.10 or later and only the standard library. The script builds its entire object from the four-bit graph definition; it uses no tables or files from prior computations.

The expected terminal acceptance marker is `VERIFY_OK_Q4_INTEGRAL_CROSSCYCLE_AUGMENTATION_QUOTIENT`. The checker asserts the 742-face vector, every one of 2,816 oriented Hasse incidences, the exact 367-pair Morse matching and directed acyclicity, all simplicial boundary-squared identities, all eight minimum-carrier octahedral cycles, the exact seven-by-eight integer projection matrix, the eight exact unit maximal minors, the unique primitive integral relation, and all 384 signed automorphism actions on the original simplicial cycles.

The key finite outputs are an integer Morse zero differential, a 7-by-8 coordinate matrix with all maximal determinants equal to ±1, and the integral signed-permutation action specified in `RESULT.md`. The universal flag-complex minimum-support assertion is proved in the text and is **not** claimed to follow from the finite enumeration of this graph alone. The previously known seven-sphere homotopy type is acknowledged; this verification pertains to the new geometric integral module.

No independent audit or external certification is claimed.

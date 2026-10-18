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

Execute `python3 checker.py` with standard Python 3 and no external packages. The script builds complete finite chain-ring arithmetic, group products and inverses, and then computes all ordered commutators using group operations rather than the counting formula. It checks each resulting fiber and support set against the theorem; it also checks the identity fiber through conjugacy-class counting.

The suite includes modular rings of lengths one through four over small primes and length-two dual-number rings over three finite fields, including a nonprime residue field. The length-one cases test the limiting construction even though the stated theorem assumes length at least two. Successful replay prints `VERIFY_OK`.

This is a finite sanity check. The proof of the all-length/all-chain-ring statement uses exact unit-filtration and linear-fiber sizes; the checker does not certify all infinite parameter values. No independent audit has been performed.

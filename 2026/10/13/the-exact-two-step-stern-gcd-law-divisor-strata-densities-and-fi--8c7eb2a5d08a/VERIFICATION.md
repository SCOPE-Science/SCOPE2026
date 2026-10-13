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

# Verification notes

The proof of the exact pointwise formula uses only Stern's recurrence and adjacent coprimality. The density step uses Reznick (2006), Theorem 4.7, for each **fixed** modulus. The prime-power probability computation and the passage to the global limit are proved in RESULT.md.

Run `python verify.py` in a directory containing the embedded verifier (Python 3, no third-party packages). The exact output checked during this review was:

`EXACT_CERTIFICATE_OK pointwise_n=249999 valuation_strata=15 first_occurrences_through=31 finite_residue_moduli=9`

This checks finite identities and modular counting, not infinitely many indices or the external analytic equidistribution theorem. The arXiv document and the available direct restatement of a correlation theorem were inspected to assess overlap. No independent audit has been performed.

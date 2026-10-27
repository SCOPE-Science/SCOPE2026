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

# Verification evidence and limits

The included `verify.py` (Python 3, standard library) was run against the same scientific claims before packaging and printed:

`VERIFY_OK: necklace, singularity, symmetry spectra and unrestricted-matrix automorphisms; 22 necklace configurations`

The code independently enumerates cyclic necklaces over finite multiplicative-group exponents, compares every orbit's singularity and minimal period with both divisor-sum formulas, checks the normalized structural-matrix rank for all nonzero edge/loop assignments in dimension three over the prime fields of orders two, three and five, and enumerates **all** linear matrices in dimension three over the fields of orders two and three when counting automorphisms. Hence the matrix automorphism checks do not presuppose monomiality. The package uses the normalized coefficients predicted by the proof.

All exact finite tests passed. The proof, not the finite checks, establishes statements for every field and every \(n\ge3\). In particular, finite enumeration does not resolve independent originality risk or certify an infinitely quantified theorem by itself. The value of the general all-fields classification relies on the structural proof and referenced previously proven basis-rigidity criterion.

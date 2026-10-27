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

# Reproduction and limits

Run `python3 check_star.py` from the extracted file directory. It brackets and bisects the unique scalar root in high-precision Decimal arithmetic for each integer \(2\le n\le50\), checks the exact-form equality witnesses against direct graph mass and energy, checks the strictly smaller hub bound, and tests 7,350 seeded random mean-zero real vectors against the claimed coefficient. This is a bounded computational consistency test. Independent floating-point optimization for dimensions \(2,3,4,7,15\) also agrees to numerical precision but is not packaged as a proof step.

The all-integer correctness justification consists of the two Jensen-type averaging identities, the signed cubic discriminant polynomial with explicitly positive coefficients after \(n=2+m\), the strict hub-versus-leaf witness, and an analytic implicit-function expansion at inverse degree zero. In particular, no finite search or random data establishes the all-\(n\) theorem. Published source comparison is limited to examined materials and public search results, so global uniqueness of the discovery is not certified. The stated mean-zero and unnormalized energy conventions are necessary.

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

# Verification of square-zero derivation rank spectra

Run `python3 verify_square_zero.py` in the directory containing the accompanying standalone verifier. Its final `VERIFY_OK` indicates all embedded finite tests passed.

The script constructs derivation matrices directly by applying the Leibniz formula to basis monomials in each truncated algebra, tests composition-square zero by matrix multiplication, and computes matrix rank by field elimination independently of the valuation proof. It enumerates every admissible coefficient tuple over the prime field of order two for lengths 2 through 8 and over the four-element field for lengths 2 through 6. The verifier checks the pair equations and tests both parity sides and expected multiplicities.

These are finite experiments, not an exhaustive computational proof of the all-length theorem; the paper proof supplies the unrestricted algebraic argument. The originality assessment is based on stated published assumptions and inspected textual results, not a proof of global priority. Independent assessment has not been performed.

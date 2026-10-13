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

The proof has two logically separate components. First, exact rational inequalities reduce every odd five-prime-support unitary Zumkeller number to the 90 displayed candidates; this part is universal and does not rely on bounded enumeration. Second, `witnesses.json` supplies a proper-unitary-divisor subset for every candidate, and `verify.py` checks all 90 certificates using exact arithmetic.

Run `python verify.py` beside the certificate. It must print `VERIFY_OK candidates=90 witnesses=90 least=15015`. The checker also recreates the candidate set from the symbolic bounds and verifies the exact inequalities used to exclude all other prime/exponent patterns.

The certificate proves only the stated five-distinct-prime stratum. It does not search or certify the six-or-more-prime odd domain.

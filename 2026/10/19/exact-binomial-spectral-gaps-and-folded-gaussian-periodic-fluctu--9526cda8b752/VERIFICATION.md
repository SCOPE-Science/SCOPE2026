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

# Verification of exact multiplier-gap statistics

Analytical proof: the signed monomial Jacobian product, bijective sign coding, exact binomial multiplicity, and central limit theorem are reconstructed in `RESULT.md`. Finite matrix enumeration is a supplemental arithmetic consistency check rather than proof of the asymptotic statement.

Run `python check_spectral_gap.py` from the same directory as this document. It multiplies exact 2-by-2 integer matrices for every word of length one through twelve, excluding the nonisolated all-left word. It checks exact characteristic type, absolute diagonal doubling exponents and all predicted multiplicities; success ends in `CHECK_OK`.

The verification does not exhaust all lengths, certify the full published literature, or supply an independent audit.

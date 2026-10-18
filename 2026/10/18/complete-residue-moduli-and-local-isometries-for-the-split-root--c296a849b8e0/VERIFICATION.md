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

The full proof establishes the universal claim through the closed form, odd-prime lifting the exponent, and the Fermat/parity obstructions. In particular, no finite experiment is presented as proof of arbitrary moduli.

Execute \(`python3 verify_jacobsthal.py`\) in the same folder as this document with Python 3 standard library. It checks all exact eventual modular state cycles for \(a=2,4,\ldots,50\) and \(m=1,\ldots,120\) (3000 profiles), plus both parity permutations and the exact gcd form of the local valuation identity for 82 relevant profiles. This executable was run directly from the package's source, producing \(`VERIFY_OK 3000 full-state modular profiles; 82 complete-modulus double-permutation/isometry tests`\).

Proof scope is even \(a\ge2\), all \(m\ge1\), all nonnegative indices. Unresolved risks: a general prior Lucas theorem might cover the variable-base specialization; the closest original Jacobsthal paper provides issue-month rather than an exact day. Independent audit has not been performed.

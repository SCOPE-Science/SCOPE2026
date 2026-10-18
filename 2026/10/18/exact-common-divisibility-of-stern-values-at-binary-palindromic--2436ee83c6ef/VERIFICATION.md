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

# Verification and proof boundaries

The exact proof uses four palindrome families of bit length \(\ell\ge8\), represented by the fixed prefixes `1000`, `1100`, `1010`, and `1001`, followed by a variable zero block and mirrored suffix. Direct recurrence multiplication gives their Stern values \(\ell\), \(4\ell-12\), \(9\ell-42\), and \(16\ell-104\), whose gcd is \(\gcd(\ell,2)\). The parity converse follows from the modulo-two Stern recurrence and the divisibility by three of each even-length binary palindrome. All lengths below eight are exhausted separately.

Run `python verify.py` from the extracted package. The standard-library program checks all 4,094 palindromic indices of lengths one through twenty-two, the exact gcd classification for each tested length, the parity obstruction at every tested even length, and four affine template formulas, including selected zero-block lengths up to 113. The proof is required for the infinite conclusion; successful finite execution is not an exhaustive computational certificate. No independent audit has been conducted.

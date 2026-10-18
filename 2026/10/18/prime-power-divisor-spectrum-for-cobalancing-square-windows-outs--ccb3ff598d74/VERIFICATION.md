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

Run `python3 verify.py` using Python 3; no external package is necessary. The run executed against the embedded script before packaging and replays after extraction. It checks 300 positive window lengths times 23 primes, a total of 6900 prime-valuation comparisons, and 219 exact characteristic-recurrence identities. Prime orders are computed independently by modular pair multiplication in the quadratic residue ring. Infinite correctness is established by the accompanying symbolic spectral/Vandermonde/lifting proof, not the finite test. Primes 2, 3, and 7 and full gcd values remain unclassified. No independent audit has been performed.

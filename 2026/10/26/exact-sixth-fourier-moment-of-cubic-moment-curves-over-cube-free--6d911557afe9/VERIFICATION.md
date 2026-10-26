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
# Reproducibility and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script exhaustively groups residue triples by their first three modular power sums and totals squared fiber sizes. It independently checks the exact prime factors at 5 and 7, prime-square factors at 25 and 49, and the CRT factorization for modulus 35. All reported integer counts match the formulas in RESULT.md. The finite tests do not certify any universal quantifier; the full proof is the Vandermonde rank argument plus Newton identities and Fourier orthogonality in RESULT.md.

This is a self-review only. No independent audit or external validation was carried out. The calculation does not address prime-cube factors or primes 2 and 3. An undiscovered historical ramified local-density computation could overlap with the result.

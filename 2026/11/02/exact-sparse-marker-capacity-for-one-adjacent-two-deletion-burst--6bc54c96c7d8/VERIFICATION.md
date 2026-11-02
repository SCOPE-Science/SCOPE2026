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

Run `python3 verify_burst2.py` using Python 3.9+ and only the standard library. The checker reconstructs the actual output words by all possible consecutive two-position deletions, rather than relying on formula predictions for collision membership. It verifies 79,002 pairwise collision decisions through source length 20, checks all 249 explicit constructed codebooks for lengths 2 through 250 (23,251 codewords), exhaustively computes exact optimum independent sets at lengths 2 through 10, and checks residue bounds for 10,001 integer parameters.

The all-length proof is given in RESULT.md. Exhaustive computation at finite lengths does not imply the infinite statement. The case of two arbitrary deletion coordinates is deliberately excluded. No independent scientific audit has been performed.

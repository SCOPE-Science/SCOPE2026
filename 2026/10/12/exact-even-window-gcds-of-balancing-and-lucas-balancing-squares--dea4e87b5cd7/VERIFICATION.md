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
# Reproduction and proof checks

Run `python3 verify.py` with Python 3. The script uses only integer arithmetic from the standard library; no external input or packages are required. The accompanying `verification-output.txt` records the successful execution. Exact recurrence construction and sliding-window identities are checked for even \(k\) through \(250\) and \(80\) consecutive starting positions, making \(20{,}000\) individual square-window values. Each accumulated gcd equals the proposed arithmetic formula. Checks also include the square identity, the requisite \(2\)-adic unit congruences, and the \(3\)-adic balancing valuation for these indices.

This is a **finite reproducibility check**, not an infinite proof or independent audit. For unrestricted correctness, inspect the algebraic identities, Pell strong divisibility, odd-prime lifting in the quadratic \(3\)-adic ring, and binomial reductions modulo \(16\) in `RESULT.md`. The first-window and increment-gcd argument ensures that only these symbolic local claims are needed. No independent external review has been performed.

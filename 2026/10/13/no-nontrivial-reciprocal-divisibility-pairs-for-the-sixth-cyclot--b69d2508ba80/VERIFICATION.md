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

The universal proof is the decreasing-maximal-operand descent in `RESULT.md`. It depends only on integer arithmetic and does not assume primality. Critical steps checked by hand: (1) \(F(a)\equiv1\pmod a\), (2) \(1\le c=F(a)/b<a\) when \(2\le a<b\), (3) \(c^2F(b)\equiv F(c)\pmod a\), (4) preservation of both divisibilities, (5) strict decrease, (6) gcd-class partition producing the exact arithmetic-function product.

Run `python3 verify.py`. The standard-library checker exhaustively tests every eligible divisor partner for \(2\le a\le5000\), every pair in the \(200\times200\) grid, and six arithmetic identities. The exact output is embedded in `verification_output.txt`. These computations are supplemental, not evidence that a finite search proves an infinite theorem.

A distinct source-literature risk remains: an equivalent proof may have appeared in unindexed work. Neither the complete classification of all integral inputs nor the absence of all longer divisibility cycles is claimed.

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

# Verification of the mathematical claim

Execute `python3 verify.py` with Python 3, no optional dependencies. `verification_output.txt` records the deterministic result.

The 2-bounded candidate vectors in order \(n\) are exactly the \((3^n-1)/2\) words with odd coordinate sum. The verifier forms the compatibility graph by the exact integer test \(I(x,y)\equiv0\pmod2\), and separately compares each tested predicate with intersection parity of initial-segment set encodings. The recursive calls use increasing vertex indices, so every clique is visited once; the terminal zero count at sizes 2,3,4,7,8 establishes the respective absence of larger admissible families in orders 1,2,3,4,5.

For the six-coordinate construction, the verifier checks each word's odd sum and every one of the \(\binom{10}{2}=45\) pair intersections. It also constructs disjoint-support witnesses for each order 1 through 48. These finite tests are supplementary to the full general upper and lower proofs in `RESULT.md`, not extrapolations to infinite orders.

**Unproved:** exact optima for orders greater than five, a tight asymptotic growth ratio, and bibliographic priority. Independent verification has not been performed.

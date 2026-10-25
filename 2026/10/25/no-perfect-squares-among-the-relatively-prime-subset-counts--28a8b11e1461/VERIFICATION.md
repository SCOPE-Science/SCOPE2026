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

# Finite checks and their limits
The supplied `verify.py` uses only Python's standard library. Running `python verify.py` returned exactly:

`VERIFY_OK: 15 exhaustive and 999 exact Möbius cases`

It compares a direct enumeration of all nonempty subsets against an independently evaluated divisor formula for each \(1\le n\le15\). For each \(2\le n\le1000\), it checks that \(\Phi(n)\) is positive and not a square, its exact \(2\)-adic valuation for odd \(n\), and its position between the two consecutive squares for even \(n\). It also checks the finite odd-prime-union estimate used in the analytic proof.

Finite enumeration cannot establish any universal statement, nor can it prove novelty. The proof in `RESULT.md` supplies the universal quantifiers by a valuation argument and an inclusion-exclusion union bound. The nontrivial inequality \(2^u\ge u+1\) for \(u\ge1\) follows because its left side is convex and its derivative at \(1\) already exceeds the right side's derivative. No independent audit has been performed.

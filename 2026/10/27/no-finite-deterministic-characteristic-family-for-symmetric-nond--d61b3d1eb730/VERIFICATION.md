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

The proof is self-contained. The direct finite checker `verify.py` enumerates every endofunction on carriers of orders \(1\) through \(4\). It verifies that the powers \(2d\) and \(2(d+d!)\) coincide on every point; it then checks the full three-valued nondeterministic-choice truth table and the legal split at the entry \((1,k)\).

The proof's critical non-enumerative step is elementary functional-graph eventual periodicity: a function on at most \(d\) points has a preperiod smaller than \(d\) and every periodic cycle has length dividing \(d!\). This establishes the identity for all \(d\), not just checked small instances. The dynamic countervaluation uses two syntactically distinct compound formulas, so it does not assign contradictory values to one and the same formula. Nonempty output sets allow extension of the indicated finite partial valuation to a total dynamic valuation.

Reproduce with `python3 verify.py`. The supplied script uses Python's standard library only. No exhaustive search over *all* finite matrices is claimed or required, since arbitrary binary operations cancel when the unary subterms are equal. Historical priority and independent validation remain unverified.

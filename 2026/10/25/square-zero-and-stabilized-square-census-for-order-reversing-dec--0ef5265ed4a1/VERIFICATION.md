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
# Verification details

Run `python verify.py` with Python 3 and no external dependencies. The checker enumerates all nonempty domains and decreasing antitone assignments on \([n]\) for each \(1\le n\le9\), directly composes each transformation, checks \(f^3=f^2\), verifies that every nonzero square has image exactly \(\{\min D\}\), and compares the two counts for every permissible width-height pair with the stated binomial formulas.

The observed triples \((\text{total},\text{nonzero square},\text{zero square})\), in ascending \(n\), are \((1,1,0)\), \((4,3,1)\), \((12,8,4)\), \((33,21,12)\), \((88,55,33)\), \((232,144,88)\), \((609,377,232)\), \((1596,987,609)\), and \((4180,2584,1596)\). The executable finishes with `VERIFY_OK`. Its finite enumeration is not a substitute for the bijective and generating-function proofs valid for all \(n\).

No independent mathematical audit has been conducted. The result assumes no additional hypotheses beyond the definitions in the accompanying proof. The withdrawn related preprint and older thesis were not fully available for novelty comparison.

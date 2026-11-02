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

# Verification record

The attached `verify_inverse_sis.py` program was run using the Python 3 standard library from its own saved path. It executed exact `fractions.Fraction` arithmetic for 2,338 target-root families containing 18,718 individual roots, encompassing \(1\le M\le15\) in the checker (the theorem itself concerns \(M\ge2\)). Its domain checks included 1,279 admissible root families, 1,045 inadmissible families, and 14 sharp sum-one boundary cases. For every family it verified the polynomial identity, leading coefficient, root evaluations, and linearization sign; for \(M\ge2\) it verified the equivalence between strictly positive rates and the strict root-sum inequality.

Run: `python3 verify_inverse_sis.py`. Expected terminal line: `PASS`. The explicit four-channel example is also tested with exact rational arithmetic.

The proof covers all integer interaction orders \(M\ge2\) and all distinct target fractions in \((0,1)\); the finite checker does not certify an infinite quantifier by itself. A complete independent external audit has not been performed. Scientific limitations and related literature are given in `RESULT.md`.

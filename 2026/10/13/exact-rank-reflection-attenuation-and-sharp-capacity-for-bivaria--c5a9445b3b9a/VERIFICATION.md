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
# Verification of the rank-reflection identity

The following statements can be checked directly from the definitions, for all bivariate copulas with continuous uniform margins: (i) reflection changes the centered conditional CDF from \(d(u,v)\) to \(-d(u,1-v)\), (ii) the sum and difference are orthogonal in the joint Lebesgue square, (iii) the folded uniform response has centered conditional CDF \(d(u,t/2)-d(u,1-t/2)\), and (iv) squaring and integrating yields the factor \(1/4\). The total-variance characterization gives both equality regimes and the attainable interval.

The enclosed `verify.py` was executed from its actual package source and passed 2,752 exact rational assertions, including 840 biased-reflection and 240 fair-reflection checkerboard configurations. The script uses only the standard Python `fractions.Fraction` class. To reproduce: `python verify.py`.

These finite calculations do not certify the unrestricted theorem; the proof in RESULT.md supplies all infinite-dimensional quantifiers. The numerical-free interval endpoints derive algebraically, and no inaccessible external computational certificate is needed. Independent audit status is not performed.

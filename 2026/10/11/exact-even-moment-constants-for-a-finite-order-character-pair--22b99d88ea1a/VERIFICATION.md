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

The proof is analytic. The reproducibility script checks only consequences of the symbolic proof and is not used to infer an infinite statement from a finite search.

`artifacts/verify.py` performs the following checks.

1. For \(2\le q\le18\) and \(2\le h\le14\), it evaluates the filtered binomial sum in two independent exact integer forms and verifies equality.
2. It verifies that the filtered sum equals the central binomial coefficient exactly when \(q>h\) in the tested finite range, and is strictly larger when \(q\le h\).
3. It checks the combinatorial phase-frequency condition: no nonzero surviving frequency exists when \(q>h\), while the frequency \(q\) appears with positive coefficient when \(q\le h\).
4. It confirms that the aligned normalized moment polynomial has a strictly positive quadratic coefficient for every tested \((q,h)\).
5. It performs deterministic numerical checks of the sharp inequality and equality witnesses for representative finite orders, moments, magnitude ratios, and phases.

The script does not certify non-even exponents or spectra with more than two characters, and no such claim is made.

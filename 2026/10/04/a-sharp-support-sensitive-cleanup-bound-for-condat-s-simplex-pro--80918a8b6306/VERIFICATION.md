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
The proof gives an all-dimensions upper bound from the strictly decreasing candidate-list size on every nonterminal cleanup pass, proves the special singleton-support reset collapse, and supplies a rational equality family for every \(2\le K\le N\).

`verify.py` replays the stated Fig. 2 update rules with exact `fractions.Fraction` arithmetic. It checks every pair \(2\le N\le30\), \(2\le K\le N\), verifying the constructed final support and the exact cleanup-examination formula. It also checks representative singleton-support inputs.

The finite replay is not used as a proof for arbitrary \(N\). Floating-point behavior, wall-clock cost, and operation counts outside step 4 are not certified by this package.

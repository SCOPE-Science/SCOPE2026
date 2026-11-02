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

# Reproducibility

Run `python3 verify.py` with Python 3 and its standard library only. The verifier uses exact integer coefficient arithmetic and `fractions.Fraction`; it makes no floating-point, stochastic, remote-data, or external-library calls. Execution from the newly prepared standalone file returned:

```
PASS 8885 exact assertions
```

The checks independently enumerate every permutation through eight labels, compare its inversion-refined fixed-position histogram against the symbolic Gaussian-binomial formula, verify symmetry and the direction of adjacent differences for seven positive rational values of \(q\) and sizes through eighteen, enumerate value-subset cut-crossings through nine labels, and compare adjacent exact likelihood-ratio minors on an additional grid. They check both \(q<1\), \(q=1\), and \(q>1\), as well as near-boundary and centrally balanced cuts.

This is a finite exact replay, not an exhaustive verification of infinitely many positive real parameters. The analytic argument in `RESULT.md` proves the full theorem. No external or independent audit has been performed.

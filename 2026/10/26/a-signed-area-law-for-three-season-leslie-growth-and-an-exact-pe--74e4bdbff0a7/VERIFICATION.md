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

# Verification of the three-season Leslie orientation theorem

The theorem is analytically proved in `RESULT.md`. An executable reproducible rational arithmetic check is included as `verify.py` and uses Python 3's standard library only. In the directory containing `verify.py`, run:

```sh
python3 verify.py
```

The checker constructs \(A_1,A_2,A_3\), enumerates all six chronological products for 3,000 rational randomly generated parameter triples, and verifies exactly (using `fractions.Fraction`) that their two trace classes are \(F+bL_+\) and \(F+bL_-\) and that every determinant equals \(-b^3Q\). It tests the relative Perron-multiplier sign against the signed area, and separately verifies the exact rational example by characteristic-polynomial signs. Bisection of the two monotone cubic equations gives approximately \(0.9211616241786795\) and \(1.2667517488103832\). The observed three-step multipliers are approximately \(1.083813441447242\) and \(0.7822668877499197\).

**Analytical basis:** The only possible three-factor trace expressions follow by literal matrix multiplication and cyclic trace invariance. A strictly positive monodromy has a simple dominant positive eigenvalue; its characteristic polynomial is \(z^2-(F+bL_\pm)z-b^3Q\). The sign of the trace difference is \(b\Delta\), and at \(z=1\) the sign of the characteristic polynomial identifies whether the Perron eigenvalue is smaller or larger than one. Both scalar persistence polynomials are strictly monotone in \(b>0\), yielding a complete classification including neutral boundaries. These steps, not a finite sample, establish universal correctness.

The randomized arithmetic experiment does **not** prove originality, nor does it prove a result about more than two stages, season-varying adult fertility, nonlinear feedback, demographic noise, or uncertain seasonal duration. Complete relevant-literature coverage and independent scientific validation remain outstanding.

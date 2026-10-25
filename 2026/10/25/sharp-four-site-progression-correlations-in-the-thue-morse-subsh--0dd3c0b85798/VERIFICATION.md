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

# Reproducibility and exact proof checks

Run `python verify.py` using Python 3.9 or later. The script has no third-party dependencies and uses exact `fractions.Fraction` operations for the mathematical certificate.

The verifier generates both eight-by-eight signed-average renormalization maps directly from the three component offsets, compares them with the full expected matrix row lists, verifies the two base vectors and the zero-lag fixed point, derives the reachable extremal-saturation strings without assuming their size, and checks that they agree with the exhaustive six-type transition table in `RESULT.md`.

It then evaluates the exact correlation for every integer lag from 1 through 10,000, checks the sharp bound and power-of-two equality pattern, and independently computes finite-prefix products from the literal binary parity sequence for 35 lags. Those latter prefix comparisons check consistency only and do not prove an infinite-volume theorem or a numerical approximation error rate. The infinite validity comes from the algebraic closure of the eight states, strong induction under halving, and exhaustive closure of the six saturation types.

Observed output: `VERIFY_OK: eight exact renormalization rows, six exhaustive saturation types, 10000 exact lag evaluations, 35 independent block comparisons`.

The result has undergone self-review but has not been independently audited. No proof of historical uniqueness, no result for arbitrary quadruples, and no full-range classification of all lag correlations is supplied.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n steps the fair-word measure is the number of paths of length n in the allowed three-block graph divided by 2^(n+3); this includes n=0. The total entry sum of A^n is comparable in fixed dimension to a matrix norm, so its nth-root limit is the spectral radius without a primitivity assumption. A based closed path is the uniquely coded binary point fixed by the corresponding shift iterate, including when the iterate is shorter than three, and trace/determinant gives the symbolic zeta. In a fresh exact reproduction of all 120 pairs, characteristic polynomials were recomputed with SymPy and the largest real roots isolated over the rationals. Merely placing roots in the same rational interval, as the uploaded classifier does, would not prove equality within a row. The independent check additionally verified that every polynomial in a row is divisible over Q by its listed row factor, that the factor changes sign across the row interval, and that every characteristic polynomial has exactly one distinct root in that interval. Thus each row shares its largest root exactly. Verified 26 polynomials and 16 ordered radii with multiplicities (2,22,10,4,6,8,4,4,28,4,4,2,4,4,6,8), both extremizer lists, and the witness zeta factorizations. Replay: python /tmp/opencode/frozen_review_reproduce.py holes, with SymPy 1.14.0.

## originality

PASS

The supported distinct result is the exhaustive binary length-four classification, including its exact multiplicities and all equality cases, not a new general method for obtaining an escape rate or zeta function. The strongest general formulas give an individual pair's rate, and the applicable comparison conditions do not provide this binary ordering. The indexed complement-avoidance classifications ask a different question even when a cubic factor agrees.

## value

PASS

This is a complete benchmark at a natural fixed cylinder resolution in the fair binary map, with sharp loss rates for equal-measure holes and an exact witness of what the escape rate forgets: one pair's periodic zeta has extra cyclotomic factors although its leading escape rate agrees with another's. The exact multiplicities and equality cases matter to comparison at this resolution, rather than constituting a collection of selected examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.

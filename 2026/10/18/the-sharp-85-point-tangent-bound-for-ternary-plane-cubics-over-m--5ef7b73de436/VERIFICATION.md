---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Any nonzero cubic with a smooth F9 point admits a projectivity mapping the point and tangent incident flag to ([0:1:0],Z=0); smoothness forces nonzero Y²Z coefficient, scaling to one, while Y³ and XY² vanish. The seven remaining cubic coefficients each range independently over F9, giving an EXHAUSTIVE 9^7=4,782,969 coefficient finite proof after this normal form, including all singular/reducible cubics with any rational smooth point; curves with none cover zero. Read and checked supplied C++ field arithmetic and incidence bitsets. In addition, an independently implemented C++ F9 field, all 91 projective points/line incidence, derivative tests, and full seven-loop enumeration reproduced MAX_COVER=85, FULL_COVERAGE=0 and witness (0,1,0,0,0,0,1). The separate source Python program proves the smooth witness has 16 tangent lines, six uncovered points, claimed histogram; the classical Hermitian q9 quartic fills the plane. Lines, smooth conics (55 tangent-union points), and degenerate conics do not fill. The arithmetic evidence is a genuine exhaustive finite F9 certificate, not sampling, contingent on the exact projective normalization and field implementation.

## originality

PASS

Asgarli–Ghioca formulated the minimum-degree question and supplied the Hermitian F9 degree-four upper bound, but their small-degree nonexistence theorems have hypotheses inapplicable to q=9,d=3. The blocking-set paper addresses curve-points hitting every line, a different incidence predicate. Resultary and exact q9 tangent searches found no published all-cubic bound 85, though equivalent unpublished computational enumeration remains possible. The contribution is the *cubic obstruction*, not the known quartic construction.

## value

PASS

The maximal tangent-union cardinality over all plane cubics on P²(F9) is a natural finite-geometric extremum answering the missing lower-degree case of a published tangent-filling question. Its exact 85 ceiling and attaining smooth cubic determine a meaningful sharp invariant and the first odd-square field minimum degree, even though no classification of all maximizers is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

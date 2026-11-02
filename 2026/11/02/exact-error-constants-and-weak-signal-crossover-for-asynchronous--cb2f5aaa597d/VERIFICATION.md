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

The source `verify_star.py` runs on the Python standard library. Its exact-rational checks compare 480 parameter combinations of the beta-binomial mixture and a separate Markov recurrence, plus 160 rational equal-rate/parity reductions (640 comparisons). It separately enumerates all private signals and first-activation permutations for stars with one through six leaves, checking the final hub decision. Floating evaluations of binomial tails compare \(m=200,800,3200\) with the fixed-bias constant and \(m=2000\) with the weak-signal profile at five \(lpha\) values. No randomized seed, external data, publisher access, or nonstandard library is required. Run `python3 verify_star.py` from the directory containing this document.

The exact comparisons test finitely many cases only; they cannot certify a universal theorem. The all-size and limiting statements instead rely on the mathematical proof in RESULT.md. No separate independent audit has been performed.

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

# Reproduction and checks

Run `python3 tyoung_reflection_verify.py` with Python 3.9 or later; no external dependencies are needed.

The verifier independently enumerates all column-choice facets versus all complements of \(t\)-intervals, computes *complete* reduced mod-two Betti numbers via boundary ranks for each small instance, and evaluates signs of invariant oriented simplices including the empty simplex. It also computes weighted palindromic words directly and independently evaluates the coefficient of the proved generating function.

Passing output from the packaged script:

`PASS: facet derivations 60 mod-2 complete homology 60 signed chain Lefschetz 60 independent palindrome enumerations 255 symbolic parameter substitutions 67500`

These checks are finite evidence and do not certify the all-parameter theorem. The proof valid for arbitrary positive \(t,L\) is in RESULT.md. The sphere-rank input is Theorem 3.6 of arXiv:2511.13477v3, whose earliest public manuscript date is 2025-11-17. No external independent audit has been performed.

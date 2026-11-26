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

Independence gives E[X_i X_j]=q^|N_i∪N_j|. The labeled plant degrees are preserved, so expectations and all single-degree terms cancel; half the variance contrast is exactly the pair-union histogram difference. The displayed pair differs only on rows 2,3 and columns a,c in a genuine checkerboard, is connected on both sides, and has minimum degree two in each guild. The respective histograms, indexed from 0 to 5, are (0,0,1,0,8,1) and (0,0,0,4,3,3), yielding the claimed factorization and strict signs around 1/2. Independently replayed the full bounded lower bound in evidence/4-switch-census.js without executing the frozen C++: permute any given switch to the upper-left identity checkerboard, order columns 3 onward by their two active bits, and order unaffected plant rows by their entire masks. This normalization loses no admissible switch or polynomial (uniqueness of its representatives is unnecessary). The independent search tests both connectivity conditions and exhausts all positive guild sizes through order nine with at least two in each guild; with either guild smaller there is no switch. In the 4+5 and 5+4 cells it examined 10,560 and 8,160 normalized candidates, with 6,727 and 5,256 admissible, respectively. In all cells the transformed coefficients of (1+x)^n P(x/(1+x)) had a common weak sign, proving no reversal for the continuum 0<q<1, not just sampled q. These normalized counts are not the frozen enumerator's labeled counts. The proof is for independent static failures and one switch with connected endpoints, not arbitrary degree-matched pairs.

## originality

PASS

The important distinction is the one-switch adjacency requirement, not the sign-change polynomial in isolation. Same-statistic records allow arbitrary degree-matched pairs (where the sharp order can already be nine) or fix three plants, and the same-date ten-species result uses a different statistic. None of the inspected claims supplies an arbitrary-guild sharp lower bound under one connected-output checkerboard switch together with a matching witness. This is a bounded best-of-knowledge decision, not an assertion of universal priority.

## value

PASS

A smallest local rewiring that reverses stochastic variability is a meaningful boundary: it tests whether a single degree-preserving move can do what some more distant degree-matched pairs can already do. The exact threshold rules out all smaller connected networks, and the witness rules out an artifact caused by leaves or changed means. This is a useful finite result about the specified static model, not an empirical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.

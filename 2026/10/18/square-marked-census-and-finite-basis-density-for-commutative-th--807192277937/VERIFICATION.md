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

# Reproducibility and verification

Run `python verify.py` with a standard Python 3 interpreter. The program uses no optional libraries and reads no external files.

The first enumeration routine directly visits each symmetric multiplication assignment to unordered pairs of generators in the fifteen feasible \((m,k)\) strata with \(3\le n\le7\), tests that every nonzero product color is attained, and records the count of nonzero generator squares. It compares this direct distribution to inclusion--exclusion without sharing its enumeration logic. Separately, the program computes Burnside's fixed maps using partitions and cycle orbits, and independently constructs isomorphism orbits from actual permutations for \(3\le n\le6\). It also verifies the previously published complete labelled totals for \(3\le n\le11\) and complete isomorphism-class totals for \(3\le n\le9\).

A successful replay prints two `VERIFY_OK` lines and the computed sample counts. These finite checks do not prove the formulas for arbitrary \(n\); those follow from the canonical decomposition, inclusion--exclusion, and Burnside arguments in `RESULT.md`. No computational test of finite equational basability itself is claimed; that interpretation uses the cited finite-basis theorem. Bibliographic originality remains subject to independent review.

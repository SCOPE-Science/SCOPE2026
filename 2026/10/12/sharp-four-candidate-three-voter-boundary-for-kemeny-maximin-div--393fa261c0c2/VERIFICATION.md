---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Using the exact result definitions, Kemeny score plus sum of Kendall inversions equals 6 times electorate size for any ranking, and maximin support plus worst opposition equals electorate size. Independently implemented subset-DP optimal ranking scores and minimum pairwise supports for every 24^1+24^2+24^3 strict labeled four-candidate profile. Counts: all 24 and 576 small-voter profiles agree; at three voters 12,768 equal and 1,056 strict Kemeny subsets of maximin (cells (1,3)=144,(1,4)=576,(3,4)=336); eight candidate/voter orbits seven of size144 and one size48. This independent DP differs from the package verifier’s direct rank enumeration; the package script and RESULT.md were inspected. Published 3-candidate equality supplies the separate minimal-candidate premise. The finite universe here is exhaustive, not a sample.

## originality

PASS

The new statement is the complete first four-candidate three-voter divergence and orbit census. Classical three-candidate coincidence and the possibility of disagreement at more alternatives are prior. Resultary related results concern different rule pairs; searches did not reveal the same full table, but that alone is not novelty proof.

## value

PASS

A fully enumerated minimal boundary between two natural voting choice correspondences gives exact first divergence frequency, a universal containment direction, and symmetry classification useful for benchmarking tie rules. This is not merely a single counterexample; its exhaustiveness is mathematically motivated by the sharp minimal electorate/candidate boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.

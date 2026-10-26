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

# Verification

Execute `python verify.py` using standard Python 3; no external dependencies.

It exhaustively examines all \(1,4,64,4096\) loop-free directed graphs for \(n=1,2,3,4\) respectively; checks the correspondence to \(\Diamond\Box q\to\Box\Diamond q\) by evaluating all valuations; checks the first two factorial moments against explicit rational formulas with \(p=1/2\); computes the true minimum insertion count over every three-world graph; and independently enumerates optimal insertion sets for all 211 four-world graphs meeting the stated structural good conditions. For larger sizes, reproducible random samples check explicit repair certificates.

Expected final line: `CHURCH_ROSSER_POISSON_INSERTION_CHECK_OK`. All checks passed on the packaged source. Exhaustive finite checks do not prove Poisson convergence, high-probability disjointness, or the infinite-size normalized repair multiplicity; those are established analytically in RESULT.md.

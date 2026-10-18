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

## Reproduction

Execute `python3 check_volumes.py` using Python 3.9 or later; no third-party libraries are required.

The script independently computes exact anchored coordinate volumes using the leading Ehrhart coefficient obtained by counting integer lattice points in dilates of ten rational network-difference polytopes. It verifies the binomial formula for 492 multipartitions and tests 2230 strictly comparable unordered composition pairs at both within-part distances \(3/2\) and \(2\). Expected output:

`EXACT_MULTIPARTITE_VOLUME_PASS ehrhart=10 endpoints=492 majorization_pairs=2230`

The rationale for using Ehrhart theory here is total unimodularity of the directed vertex-incidence difference matrix after multiplying all rational metric bounds by the denominator. The exact-volume calculations are checks, not an exhaustive proof for every dimension. The theorem for all real \(1\le t\le2\) follows from the measurable extrema decomposition, positive discrete second difference and beta-binomial/Stirling arguments in `RESULT.md`.

## Limits of verification

A finite checker cannot establish the infinite-dimensional quantifiers or prior-work novelty. The analytic proof addresses all dimensions; comparisons with accessible mathematical literature are described in `REVIEW.md`. No independent scientific validation or external certification has been performed.

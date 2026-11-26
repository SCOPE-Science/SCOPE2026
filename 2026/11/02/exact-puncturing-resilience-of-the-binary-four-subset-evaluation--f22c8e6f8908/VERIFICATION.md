---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Differences of four-subsets with three shared positions span all even-weight binary columns, so the kernel is just the constants. Two messages independent modulo constants have at least three joint types. A comparable-support pair requires erasing the entire output-01 fiber for one ordering; any rank loss likewise erases such a fiber by taking a vanished nonconstant message as the second and an independent message as the first. The four-subset formula counts exactly the allowed 3+1 and 2+1+1 multiplicity patterns. For the triple induction, deleting one of a repeated type preserves at least three types. In adding back type t, the increment for target w=t counts all equal-type pairs and is positive; for w≠t it counts two complementary unordered type pairs, at least one present in a set of three types. Thus the triple count grows by at least one per added point, and the four-subset obstruction grows by at least k−3, proving the all-k bound from k=9. The explicit (1,1,0,k−2) puncturing erases exactly the output-01 fiber and retains outputs 10 and 11; the columns on the large group span its even subspace, and the two further special-coordinate columns increase the rank to k−1. The small witnesses and all finite base cases were independently verified.

## originality

PASS

The code and its unpunctured minimality are already known. In the closest inspected work the support test is existential and the geometric formulation is a characterization; neither computes the least number of coordinates needed to remove all obstructions or provides rank-preserving attaining erasures. No equivalent exact resilience result was found in the inspected indexed statements or literature. The pass is for that sharp extremal invariant and its attainment, not priority for the code or its unpunctured parameters.

## value

PASS

The result gives a sharp deterministic erasure guarantee for a standard complete layer and distinguishes the failure of minimality from rank loss. It answers how many coordinates can be removed before the cut/blocking or support property breaks, explains the exceptional small lengths, and provides explicit extremizers that keep the original dimension. This information is not supplied by ordinary distance, rank, or unpunctured minimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.

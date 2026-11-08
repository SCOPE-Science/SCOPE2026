---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The primal weights on length-three constant, adjacent-repeat, and other patterns are 1,1/2,1/4; all fifteen equality patterns of length four have coverage at least one. The dual gives mass 1 to aaaa and aabb, 1/[2(q-2)] to abca, and 1/[4(q-2)] to four-distinct words; counting occurrences in each center type gives dual sums exactly one and matching objective q(q+1)^2/4 for all q>=3. Binary explicit primal and dual achieve four. Independent exact Fraction enumeration for q=2,3,4,5,6 checked every distinct deletion set and every dual inequality, with common objectives 4,12,25,45,147/2. For the integer covering I(q,3,1), published s(4,3)>1/3 makes the asymptotic gap liminf at least 4s>4/3; this is a conditional comparison using the published bound, not a calculation of s.

## originality

PASS

The fully specified fractional LP with distinct deletion descendants has an exact all-alphabet optimum that differs from known integer covering numbers and general sphere or LP lower bounds; best-of-knowledge new, with unindexed LP specializations a possible risk.

## value

PASS

An explicit all-alphabet primal-dual certificate exactly solves a natural insertion-cover relaxation and quantitatively separates it from its integer counterpart; the exact fractional bound is a reusable optimization benchmark, not merely a recomputation of known integer tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.

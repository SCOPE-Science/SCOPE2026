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

A rank-four 4×5 integer matrix has a one-dimensional kernel spanned by the signed minors. Nonzero same-sign minors are equivalent to strict positivity; dividing by their gcd gives the primitive integer generator, and every integer dependence is its integer multiple by Bézout. Consequently a positive primitive relation is minimal as a zero-sum multiset. No valid support can contain antipodes: their two-term relation would contradict the one-dimensional kernel having full support. An independent exact enumeration used all 658,008 five-subsets of the 40 antipodal directions, computing ordered 4-minors by a cached 24-term Leibniz sum. Five nonzero cofactors give rank four and exactly two sign assignments making the relation positive: signs of the cofactors or all reversed. The absolute cofactor sum divided by gcd thus tests every positive support exactly once via one of the two assignments. The run finds 253,152 qualifying direction sets, 506,304 positive supports, length 30 at exactly 768 supports, and two distinct canonical representatives matching the frozen representatives. The 384 group images of each are distinct; their disjoint union is precisely the 768, proving trivial stabilizers. The given coefficients independently sum to zero vector with gcd one. Rooted appearance counts 120,560 and rooted maximum counts (0,0,84,72) also match; neither rooted quantity is a full-support census. Replay /workspace/branches/five_ray_circuit_audit.py, with retained output at /workspace/branches/five_ray_circuit_audit_output.txt; frozen verify_fourcube.cpp was inspected, not executed. No upper bound was established for rank-deficient five-support multisets or for the full Davenport constant.

## originality

PASS

The bounded comparison did not establish earlier exact coverage of restricted maximum length 30 or the two-orbit classification on the four-dimensional radius-one box. Known cofactor formulas, general box bounds, and lower-dimensional exact censuses do not give this statement on the inspected evidence.

## value

PASS

The unit ternary box in dimension four is the next natural case beyond the compared two- and three-dimensional box studies. Full-rank supports of size d+1 isolate the positive-circuit obstruction to sharp bounds on minimal zero-sum lengths. An exact sharp upper bound and complete equality-orbit classification add information beyond the witnesses or a numerical search for long relations; the precise equality cases can be used in further box work.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

The repair equations repeat each kernel word, and the projectively distinct columns prevent supports of size 1 or 2. A line has five points, giving rank three for u>=7. A cap has at most six points since each of its other points uses a different line through any chosen cap point, and only five such lines exist. Thus there is a dependent triple, and its one-dimensional relation space has exactly three nonzero words, each with all three coordinates nonzero. This proves A6=3T and distance six. For the occupancy relaxation I independently enumerated the six counts with sum 21 and retained the point and pair moments. The two unique unrealizable minimizers are (2,2,3,14,0,0) and (2,1,1,16,1,0) with T=14,20. At the intersection of their two empty lines, the other three pencil lines partition S into parts of size at most four; sizes 10 and 11 force at least one and two four-secants respectively, a contradiction. I then reproduced the entire fifteen-row table by exhaustive direct summation over the 21 lines of an independent affine-plus-infinity realization. The check visits all 2^21 masks and verifies the binomial number at each size; it does not use the frozen dynamic program. The frozen recurrence itself counts each new triple once, since its pair lies on a unique joining line through the inserted point.

## originality

PASS

Pass for the complete optimized multiplicity and labelled subset census, especially the exact sharp results at the two infeasible occupancy minima. The construction, standard plane facts, and individual geometrical examples are not new. The indexed length-15 example supplies the same extremal profile and its natural family gives the reported count in that row; this material overlap does not subsume the all-length classification. The closest indexed incidence census optimizes a different functional and does not give the small-triple minima or the complete complementary maxima.

## value

PASS

Within a motivated family whose minimum distance is fixed at six, A6 distinguishes the number of smallest undetectable error patterns. The exact number of configurations attaining each minimum is a meaningful complete finite invariant. The geometric obstruction at sizes 10 and 11 explains why integral moment feasibility alone produces wrong answers and is not just recomputation of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.

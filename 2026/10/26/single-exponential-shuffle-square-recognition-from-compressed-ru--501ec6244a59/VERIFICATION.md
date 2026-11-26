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

A split is fully represented by counts x_i in [0,L_i]: positions within a constant run can be allocated in a contiguous prefix and suffix with no effect on the induced words. Guessing zero, full, or interior fixes which fragments appear, including forced exclusion of the interior state when L_i=1. On each track remove absent fragments and merge adjacent surviving identical symbols. If the resulting symbol sequences agree, equality of corresponding run lengths is necessary and sufficient. After the fixed counts are substituted, an interior variable x_i has one positive incidence from each track, because its opposite fragment has length L_i−x_i. Hence each column is one ordinary or one doubled incidence, giving at most r vertices and at most r edges in the stated graph. Shift each lower bound by one and subtract its incidences from the demands; negative demands are rejected. If a matching solver omits loops, a loop of residual capacity U at v is represented by a triangle on v,a,b with new vertices of exact demand U and all three edge capacities U. Then the two edges at v have the same value x and contribute 2x, and the third has value U−x. Parallel ordinary edges can be collapsed by summing capacities and their recovered multiplicities distributed integrally afterward. These transformations are internal to solving the given loop-allowed instance and preserve O(r) size. Letchford–Reinelt–Theis §1–2 supplies binary-capacity polyhedral separation, including the perfect case: alternatively maximize cardinality under bounded degrees and test saturation of all demands. This provides polynomial-bit-time feasibility and integral recovery without expanding capacities into unit edges. The construction and recovery are therefore valid in 3^r poly(r,S). The stated empty-word convention is consistent. The frozen verifier and notes were inspected, not run: the code compares independent descriptions on tested allocations and stops at the first successful allocation on positive instances. It does not exercise the matching algorithm or solve the large-capacity witness from scratch.

## originality

PASS

Best of current knowledge: the supported distinct claim is the specific 3^r bound with at most r matching edges and r indeterminates after aligning output runs, on binary run lengths, including witness recovery. Run-parameter tractability, single-exponential solvability without that bound, and ordered graph representations should not be credited separately.

## value

PASS

The compressed model allows lengths exponential in the input bits, so an algorithm on expanded positions is not an adequate baseline. After accounting for the earlier nest-free graph, the surviving contribution is an exponential reduction from the straightforward grid-path enumeration and a one-variable-per-input-run formulation with no explicit nest constraints inside each instance. This makes matching feasibility and witness recovery directly applicable to the hard recognition problem and is useful without claiming first run-parameter tractability or an optimal exponential base.

The dated certificate retains the supplied scientific assessment, sources and limitations.

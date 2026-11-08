---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

From explicit Hamming-neighbor rule on 16 cube vertices, independently enumerated all C(16,7)=11440 and C(16,8)=12870 candidate blue sets with synchronous closure; none of size 7 succeeds and exactly 2360 size-8 sets succeed. Built every one-element-exchange edge (22848), verified 384 affine cube automorphisms give 11 state orbits, then ran BFS from every orbit representative. Exact degree counts {14:384,18:384,19:384,20:432,22:480,23:192,24:104}, distance P coefficients [2360,45696,355776,1274880,2110368,1361280,371184,45696,2360], all eccentricities 8, Wiener index 11197808, Johnson excess {0:5458192,1:105600,2:5808}. Proved orbit BFS exhaustive because each automorphism preserves forcing and exchanges; this is a complete finite certificate, not a sample.

## originality

PASS

Prior Z(Q4)=8, prior census 2360 minimum sets, and 11 symmetry classes are credited; the new asserted object is the entire minimum-set exchange graph's nonregular degree distribution, self-centeredness, distance polynomial, Wiener index and Johnson-distance defect. Full primary zero-forcing reconfiguration and hypercube-fort sources inspected without finding these same graph metric statements.

## value

PASS

The graph of minimum ordinary forcing configurations is a natural reconfiguration object. Exact connectivity, diameter, eccentricity and all-pairs metric characterize feasible local transformations; they give reusable finite benchmark data and a nontrivial self-centered nonregular example. This exact finite invariant does not need an arbitrary-dimension generalization to have value.

The dated certificate retains the supplied scientific assessment, sources and limitations.

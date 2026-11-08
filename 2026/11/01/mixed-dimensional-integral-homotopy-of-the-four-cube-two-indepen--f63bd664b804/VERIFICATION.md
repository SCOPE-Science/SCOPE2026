---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

A vertex subset of Q4 is an Ind_2 face exactly when every selected vertex has <=1 selected neighbor; this equivalence follows because connected induced components of maximum degree one are isolated vertices/edges. Exhausting all 2^16 subsets yields 3,055 faces including empty, f-vector by cardinality (1,16,120,464,964,960,440,80,10). A full sequential vertex toggle matching using pivot order (15,0,4,3,8,11,10,13,9,14,2,7,6,1,5,12) yields 1,519 matched pairs, 16 critical 3-faces, one critical 4-face, and an acyclic reversed-Hasse orientation across all 13,584 covers. Independently reproduced signed gradient reduction of the unique critical 4-cell into the 16 critical 3-cells and obtained an identically zero integral boundary column. The Morse CW model has no 1/2-cells; pi3 of its 3-skeleton wedge^16 S3 is Z^16, so a zero boundary means the unique S3-valued 4-cell attaching map is nullhomotopic. The added 4-cell splits as S4: the exact homotopy result follows, without a homology-only inference.

## originality

PASS

Ind_2(G) equals the first forest filtration F_1(G) as identified by Carnero Bravo, which is an equivalent name, not a separate result. Deshpande--Singh give general methods and exact results for other graph families; Q4 is not their tree, path, cycle, complete multipartite or whiskered case. The chordal-graph result excludes Q4, which has induced four-cycles. Published ordinary Ind(Q4) and matching(Q4) concern different complexes. No stronger prior theorem found to imply the 16/1 wedge; best-of-knowledge PASS.

## value

PASS

The four-cube is a natural smallest higher-dimensional Cartesian hypercube beyond standard small cases, and Ind_2 / F1 is a canonical graph-topological invariant with established motivation from higher independence and graph forest filtrations. Its strongly nonpure 7-dimensional simplicial model unexpectedly collapses to a mixed wedge of sixteen S3 and one S4; the exactly null integral attaching map is mathematically substantive and useful as a finite benchmark for later family theorems. No general theorem is required for this independently useful exact natural case.

The dated certificate retains the supplied scientific assessment, sources and limitations.

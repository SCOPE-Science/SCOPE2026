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

At a cubic vertex the three face angles exhaust the three unordered incident pairs. Conversely a complete angle cover glues disks with every edge incident twice and with a single circular vertex link at every vertex; the orientability constraints and Euler characteristic 14−21+7=0 identify the torus. The classification and flip counts were independently reproduced using rotations, not the frozen angle-cover programs. In an oriented cellular embedding the local cyclic orders determine face walks up to coherent choice of orientation; there are exactly two orders at each cubic vertex. Tracing every one of the 2^14 systems gave 16 orientations with seven distinct simple length-six faces, yielding eight boundary sets, twice each under reversal. Exhausting the 24 incidence bijections and toggling their alternating faces gave three 7-cycles and three isolated matchings for each set, with exactly one edge of each face label in each cycle. The frozen triples partition all matchings and exhaust all eight edge-disjoint triples. Exactly 28 six-cycles and 84 individual flips were found; each occurs twice across the eight systems. Removing any face label breaks every 7-cycle; retaining s labels gives exactly 3s edges and hence 24−3s components in a forest. The independent replay also checked all 127 proper subsets per system. Replay with python3 /workspace/branches/448c5fd8-2195-4b24-a20c-34156db20879/heawood_rotation_replay.py; the companion .out contains the incidence and label records. Supplied certificate and verifiers were inspected without executing the frozen code. No claim about embeddings with nonsimple faces is needed.

## originality

PASS

The pass is for the complete embedding-indexed classification, particularly the bijection between all hexagonal torus boundary sets and all frozen one-factorizations, with the twofold face and flip incidence counts. The 24 matching states, eight one-factorizations, 84 unrestricted flips and the natural embedding's own 3C7 plus 3K1 decomposition are covered; they are not independently credited. The inspected claims do not supply the exhaustive correspondence across boundary systems. This is not a priority finding.

## value

PASS

The choice of admissible torus faces changes the allowed moves on the same finite matching space. A complete census of that natural variation, including the exact embedding-to-factorization correspondence and how individual hexagon flips distribute among embeddings, separates geometry-dependent freezing from the known unrestricted trade graph. A user of this standard small toroidal example can determine exactly which embeddings freeze a matching or allow a given trade. This is more than a one-map repeat or a matching-count recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

A column with two occupied endpoints must use its rung, since otherwise that rung would be an extra induced edge. Its neighbors are empty. Thus a_i+a_{i+1}≤2, and summing gives |M|≤floor(n/2), attained by rungs. At even n, equality gives alternating 0/2 or constant 1; the latter pairs consecutive columns with alternating rails and closes precisely when 4 divides n. The distinct even edge sets are disjoint (in the rail case they differ in start offset or at every rail row); |M|≥2 makes them isolated. At odd n=2k+1 the total column deficit is two. A double deficit determines a unique all-rung pattern, and two unit deficits separate one run of ones, paired along alternating rails, from a zero-ended alternating 0/2 run. This gives n rung states and 2nk other states. For exchange exhaustiveness, both rail starts and rung columns in each odd family form cyclic intervals in +2 order, with the rail rows fixed by the initial row. If the rail count increases, the old rail interval must be contained, leaving only the two end extensions, each dropping exactly one rung. For the all-rung to one-rail case, containment of the k−1 rung interval gives the two claimed offsets. At fixed positive rail count with rungs present, identical rails fix the state; identical rungs fix the rail positions and permit a row flip only for a single rail. At the all-rail and all-rung boundaries the length-k intervals share k−1 starts only at shifts ±2; on rails the common rows require a starting-row flip. This recovers every displayed adjacency, including k=2. Counting neighbors gives the degree spectrum and handshaking gives 2n(n+1) edges; rung shifts generate the odd cycle and run shrinkage links every mixed state to it. The proof is all-order; the frozen exact enumeration was inspected, not rerun.

## originality

PASS

Best of current knowledge for the complete untwisted prism classification. The distinct Möbius-ladder result has a substantive odd-order overlap (indeed the odd exchange graphs can be identified using rail lifts) and should be credited as a close analogue. Its seam condition is different and its even counts reverse the residue classes, so it is not a theorem treating the untwisted family. No inspected earlier general result supplied this exact exchange classification.

## value

PASS

This is an explicit all-order reconfiguration graph for optimal packings on a canonical cyclic graph family, not just a packing bound. It determines the failure of every local move at even order, gives paths between all optima at odd order, and locates the sources of the nonuniform odd degrees. The seam comparison also separates the even count's sensitivity to the boundary condition from the persistence of the odd exchange structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.

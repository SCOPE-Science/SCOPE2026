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

I enumerated independent subsets by checking pair separation in coordinate differences for all subsets of sizes 1–6; none of size six exist, so no larger subsets exist. I decoded and validated the supplied matching against the 1410 nonempty faces and all 4550 covers, including disjointness, codimension one, and exhaustion of faces by matched and critical cells. Depth-first cycle detection confirms acyclicity with exactly one critical vertex and 141 critical three-simplices. By the acyclic face-poset matching theorem for a finite simplicial complex this gives a CW model with just those cells; each attaching map S²→point is constant, yielding the integral wedge. Independently, a row with two kings forces neighboring rows empty; the two remaining adjacent rows use pairwise separated, distinct columns and hence hold at most two kings together. A five-set must then occupy every row with successive differences ±2 modulo 5; all signs coincide from closure after five steps. The ten resulting lines are the only possible invariant nonempty faces for a nonidentity order-five translation. The five invariant lines in each distinguished direction contribute +5 in degree four (a 5-cycle has sign +1); the reduced augmentation contributes −1 in every case. Alternating trace therefore gives 141, −4 and 1 on the specified classes in H_3, also checked from permutation cycles on all faces. An equivariant barycentric subdivision has no inversions on simplices (a stabilizer preserves each face in the chain by dimension), so quotient chains are coinvariants. Over Q these identify with invariants by averaging, which is exact; the character averages give 25 (two lines), 29 (four lines) and 5 (full group). No integral quotient assertion follows. Independent replay: python3 /workspace/branches/independent_replay.py 5.

## originality

PASS

The exact independence polynomial and its Euler characteristic are established prior data. The inspected primary literature and closest Resultary records do not furnish the integral wedge or the precise translation representation on this graph. The quotient ranks are consequences of the latter, not an independent novelty claim about transfer.

## value

PASS

This small doubly periodic strong product is a natural exact test case distinct from rectangular path products. The integral wedge supplies attaching-map, concentration and torsion information absent from enumeration. The actual translation character resolves which slopes differ and gives rational homology of both nonfree and free subgroup quotients. These are meaningful exact refinements, not a re-tabulation of the known Euler characteristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.

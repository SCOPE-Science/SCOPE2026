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

Reflection is a rooted automorphism, and the weighted quotient neighbor multisets are {1,1,m}, {m−1,m−1,0}, and {j−1,j+1,m−j} for internal j; repeated entries count. The first update detects exactly 1,m; at the second, 1,m still coincide, and 2 and m−1 are distinguished from the remaining block by seeing one and two entries of the 1,m class. At the third, 1 sees both newly distinguished classes and m sees m−1 twice. For m≥6, the old middle's left end 3 sees 2, its right end m−2 sees 2 and m−1, and the strict interior sees neither. For m=4,5 the 1,m split finishes the partition at round three. Inductively if the middle interval [r+1,m−r] has at least two indices, its left end sees the old singleton r, its right end sees r and m−r+1, and the interior sees only the middle; thus no further split can occur in that round. At most one middle index means a discrete quotient and stability. All steps up to that round are strict, giving max(3,floor(m/2)). Since stable colors are preserved by rooted automorphisms and reflection is transitive on each P_j, the final cells are exactly the rooted orbits. The auxiliary automorphism argument also checks: a four-cycle with one chord would require a three-step circumference path between vertices at circumference distance m>3, and three chords are impossible since they are a matching. For m=3 the graph is K3,3 and its one-marked three classes are equitable after one round. Independent direct vertex replay checks all rounds through stability for 3≤m≤40 (python3 /workspace/replay/finite_checks.py); the universal claim rests on the quotient induction. Frozen scripts were inspected, not executed.

## originality

PASS

The exact one-marked Möbius-ladder wavefront and strict depth survive comparison with the indexed rooted-wavefront analogues and the inspected framework and graph-family papers. Neither the graph definition nor general stable/equitable partition results are distinct contributions here.

## value

PASS

This is an exact dynamical invariant of a natural cubic family: one distinguished vertex breaks all symmetries except reflection, but the least stable refinement round still grows linearly with ladder size. The complete sequence explains why the middle can be finished before reaching the last distance shell, and the small exceptional case tests the role of the family assumptions. This is stronger and more informative than just labeling orbits or reporting a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.

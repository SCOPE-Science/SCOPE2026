---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The bilinear anti-RB defect on basis (1,epsilon) yields exactly 3a²+2bc=0,2c(2a+d)=0,b(3a+d)=0,2ad+2bc+d²=0,3b²=0,4bd=0. For char 2 one obtains b=a=d=0, for char other than 2,3 likewise, with c arbitrary. In char3 splitting by b=0 gives the two 2D planes A (c=d=0) and B (b=0,d=a), intersecting at zero. Invertible maps all in B with a nonzero; B alone obeys strong identity. Aut(D) acts by diagonal(1,u) and scales b,c reciprocally; counting its orbits gives 4q-1 in char3, otherwise 2. Counts 2q²−1, q(q−1) invertibles and Hasse–Weil zeta follow. Independently enumerated all q^4 maps for F2,F3,F5,F7 and tested identity and strongness, yielding (2,17,5,7), and rank profile (1,10,6) and 9 strong maps over F3. Finite checks corroborate direct arbitrary-field case split.

## originality

PASS

PASS best-of-knowledge: Gao–Liu–Bai define anti-RB and strongness in characteristic zero and classify a different noncommutative two-dimensional associative algebra. Their theorem on invertible anti-O-operators being strong is consistent but does not enumerate dual-number moduli in characteristic three. Resultary semantic search did not identify a matching full classification; specialized overlooked source remains possible.

## value

PASS

The dual numbers are the smallest nonsemisimple unital commutative associative algebra. The exact characteristic-three jump from a line to two planes, invertibility, strongness and finite-field automorphism quotients provides a substantial sharp boundary case for anti-dendriform operator theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.

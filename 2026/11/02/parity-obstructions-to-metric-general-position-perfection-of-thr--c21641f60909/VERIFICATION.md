---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS: For even k>=4, odd q>=3, d=q(k-1)-1 even and L=d/2. A diameter path of length d holds d+1 vertices, producing a (k,d)-clique. Any larger set meets three arms; an extending k-subset with one vertex from each cannot be on any simple path, proving omega=d+1. A supposed q-coloring must have every palette color exactly k-1 on each of the 3 diameter paths because each has q(k-1) vertices. For any noncentral color, counts a_i of its occurrences on arm i satisfy a1+a2=a1+a3=a2+a3=k-1, forcing 2a_i=k-1, impossible as k even. Thus chi>=q+1. At k=4,q=3 a depth mod4 four-coloring realizes chi=4, omega=9 on S(4,4,4). This uses diameter paths, not unchecked finite enumeration. Independently checked parity and diameter counts for (k,q)=(4,3),(4,5),(6,3),(8,3).

## originality

PASS

PASS best-of-knowledge: Cody–Detore arXiv:2601.04351v2 explicitly asks Question 6.7 whether every finite tree is (k,d)-perfect; Proposition 3.6 proves only (3,2) tree case. An infinite two-parameter family of negative witnesses is neither a corollary of their positive result nor a simple parameter renaming.

## value

PASS

PASS: This supplies a substantive family of obstructions answering a published open structural question; a small exact 13-vertex example makes the sharp failure transparent. It establishes strict chromatic/clique gap, with parity rather than a numerical search as the mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.

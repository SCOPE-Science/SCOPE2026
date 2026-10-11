---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite verification and limits

Running `python3 verify.py` with Python 3 and no nonstandard dependencies reconstructs the open-neighborhood complex of \(H(3,3)\) from scratch. The exact checks reconstruct 1,404 nonempty faces, the face vector \((27,243,540,405,162,27)\), and 672 disjoint Morse pairs. The 4,698 directed codimension-one incidences form an acyclic graph. Critical cells: one in dimension zero, three in dimension one, 56 in dimension two, none higher. These match the independently recomputed mod-two Betti numbers term-by-term and so are optimal under the weak Morse inequalities for any acyclic matching.

The 26 vertex-edge pairs give a connected cycle-free spanning tree. All 214 edge-triangle eliminations are recursively defined without cyclic dependence; every one of the 540 original triangular relators is substituted and reduced. The 55 nonempty relators are exponent-balanced in each of three surviving generators, and three explicit relators force their pairwise commutation. This proves the integral fundamental group, rather than merely a modular rank.

A separate exact boundary-rank check over \(\mathbb F_2\) gives ranks \((26,214,270,135,27)\) in dimensions one through five. It corroborates the stated dimensions but cannot by itself prove integral torsion-freeness; the integral result follows from the Morse two-complex and its fundamental-group presentation. No higher homotopy groups or canonical attaching maps are established.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Use the standard Abrams cubical deformation-retract model for two unlabeled distinct points on the Heawood graph (girth 6, sufficient subdivision), with 91 zero-, 252 one-, and 168 two-cells and no higher cells. Independently enumerated all simple cycles: lengths 6:28,8:21,10:84,12:56,14:24, and all 42 unordered vertex-disjoint pairs, each (6,6). Constructed oriented cellular boundary B (252x168), torus cycles T (168x42) and 28 signed local 3-term relations R (42x28), checking B*T=T*R=0 by integer arrays. The stated 14x14 minor of T has exact determinant +1; rank B mod 3 is 154, so ker_Z(B) has rank14 and primitive T minor forces its 14 torus columns to generate the entire integral kernel. R has exact 28x28 minor det -2 and rank mod2 27: full rank28 over Q and exactly index2 in its saturated lattice. Every coordinate sum of its 28 relation columns is even, and r_*=(sum R columns)/2 has exactly eleven +1, eleven -1, twenty zero entries, lies in ker T but not integer span of independent R columns, completing saturated relation lattice ker_Z T. Geometry of the natural Fano automorphism group of order 336 and a single orbit of all 42 carriers is independently supported by explicit cycle enumeration and inspected exhaustive permutation code. Rank14 homology and existence of a torus basis already known; new fact is complete 42-generator kernel with indispensable index-two half-sum.

## originality

PASS

Best-of-knowledge noncovered part: Integral relations among all paired-hexagon tori in the Heawood two-point configuration space. The 42 disjoint-hexagon tori are a canonical full symmetry orbit; discovering that 28 obvious local syzygies miss a global half-integral relation isolates a genuine index-two integral lattice phenomenon; Exact saturated kernel presentation is genuinely additional to known top Betti number or torus-basis existence.

## value

PASS

The 42 disjoint-hexagon tori are a canonical full symmetry orbit; discovering that 28 obvious local syzygies miss a global half-integral relation isolates a genuine index-two integral lattice phenomenon. Complete presentation and an integral basis in H2 are precise structurally motivated facts not determined by familiar rank-only computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.

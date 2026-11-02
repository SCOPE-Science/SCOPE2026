---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The fixed finite graph is precisely the Petersen KG(5,2) with vertex {0,1} replaced by a triangle attached to its three neighbors. Independent reconstruction gives 12 vertices, 18 edges, exactly one triangle and 177 nonempty independent faces with dimensions (12,48,75,39,3). The claimed mask-toggle matching yields exactly 87 disjoint codimension-one pairs, critical masks 64 (0-cell), 388 and 2096 (2-cells), and all 492 Hasse arrows form a DAG after reversing matched incidences. Forman Morse equivalence thus gives one 0-cell and two free 2-cell attachments, the integral wedge S2∨S2. Independently enumerating GraphMatcher yields exactly 12 automorphisms, agreeing with the Petersen stabilizer S2×S3; direct signed fixed-face Lefschetz counts yield character +2,−2,0 in 3,3,6 instances and agree with sgn(S3)⊗(1⊕sgn(S2)). The asserted lack of a global invariant follows from the odd S3 action. All checks are finite exhaustive for this one graph and do not claim other graphs or integral group-module splitting.

## originality

PASS

Best-of-knowledge finding after actual Resultary and outside literature searches: Barmak Theorems 3.4–3.5 provide only a suspension criterion, not two sphere summands or this character. Graph catalogues document the Tietze/J3 object and its automorphism order but not the induced topological character. Neighboring published SCOPE findings concern different graph or higher-independence constructions. No stronger source read or matched by implication covers the exact package; unindexed equivariant calculations remain a qualified priority risk.

## value

PASS

This computes two mathematically natural invariants of a canonical twelve-vertex cubic graph obtained by Petersen vertex surgery: an integral homotopy class and the full rational homology representation of its entire automorphism group. The symmetry character distinguishes the three-label sign obstruction from the two-label even/odd splitting, strictly finer than the known graph automorphism group and Betti-number data. Its exact two-sphere topology and complete character form a reusable benchmark for equivariant independence-complex calculations; neither a routine theorem restatement nor an arbitrary unmotivated graph slice. It is explicitly one canonical graph, not an unjustified family-wide extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

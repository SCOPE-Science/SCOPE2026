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

Enumerating all disjoint subsets of the 32 undirected cube edges yields exactly 41,025 faces including the empty face, with cardinality vector (1,32,400,2496,8256,14208,11648,3712,272). Two independently recreated sequential edge-toggle Morse matchings in increasing and decreasing pivot order have 20,408 and 20,435 pairs respectively, leave one 0-cell with (39 four-cells,168 five-cells) or (12 four-cells,141 five-cells), and reverse acyclic orientations on all 210,400 ordinary Hasse covers. Independent signed-gradient recursions (from the actual oriented simplex boundary, not logs) give 39x168 and 12x141 integer Morse matrices with 909 and 512 nonzero entries. Exact SymPy Smith normal forms yield 38 and 11 nonzero invariant factors, all equal to 1, giving H4=Z and H5=Z^130 with no torsion. With no cells in dimensions 1--3, homotopy classes of five-cell attachments to a wedge of S4 are classified by the integral degree matrix. Primitive Smith pivots split off contractible 4/5-cell pairs; the residual S4 and 130 S5 prove the full wedge statement.

## originality

PASS

The same 16-vertex graph is the *periodic* 4x4 square grid C4 square C4 and has 32 edges. Published exact planar P4 square P4 grid results concern 24 edges and differ. Engström gives claw-free independence connectivity, Matsushita two-row strip matchings, and Jonsson broad background; none inspected states or implies the integral 1+130 wedge. Full Jonsson matching chapter unavailable, so best-of-knowledge priority risk remains.

## value

PASS

The matching complex of the four-cube is a canonical next case beyond the 3-cube, and the toroidal 4x4 interpretation makes its exact integral homotopy a reusable invariant for periodic-grid and matching-complex studies. Determining the *two different sphere dimensions*, their exact multiplicities and zero integral torsion requires nontrivial finite integral Morse data. It is a natural complete finite classification, not an arbitrary parameter slice or just a mod-two rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.

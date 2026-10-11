---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The package reconstructs the ordinary 3-cut complex of \(Q_3\) exactly: 32 facets, 188 nonempty faces and f-vector \((8,28,56,64,32)\). The complete Hasse-diagram element matching has 91 pairs, is acyclic, and leaves one critical 0-cell, one critical 3-cell and four critical 4-cells. Exact rational chain ranks \((7,21,35,28)\) give Betti vector \((1,0,0,1,4)\). In the resulting Morse CW complex, the cellular boundary from the four 4-cells to the lone 3-cell has rational rank zero, hence is the zero integral homomorphism; each attaching map \(S^3\to S^3\) therefore has degree zero and is null-homotopic. This proves \(S^3\vee\bigvee^4 S^4\). Nonzero third homology rules out shellability of the pure 4-complex. The verifier additionally exhausts all 255 proper vertex subsets and finds and rechecks a shelling for every induced subgraph, while the source's structural criterion independently applies because the cube is 3-connected and 3-regular.

## originality

PASS

The defining cut-complex paper was materially inspected in full PDF, including a rendered theorem page. Its Corollary 5.5 states the structural minimal-forbidden criterion used here, but full-text searches found no cube, \(Q_3\), or hypercube case and no mixed wedge \(S^3\vee4S^4\). A later grid-graph paper treats planar rectangular \(2\times n\) and \(3\times n\) grids rather than the three-dimensional cube product. Resultary search returned the assigned cube result as the direct exact hit and no earlier equivalent theorem. Thus the structural criterion is prior, while the non-shellability, exact homotopy type, and verification that the cube meets the criterion are new best-of-knowledge content.

## value

PASS

The cube is a canonical smallest 3-regular, 3-connected graph to test the defining paper's minimal-forbidden mechanism. The exact mixed-dimensional homotopy type and exhaustive induced-subgraph shellability certificate give a natural finite obstruction useful to the requested classification program, rather than an arbitrary graph census entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.

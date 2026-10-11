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

# Reproducible checks and limits

Execute `python3 verify_klein_grid.py` from the directory containing this file. The program uses the Python 3 standard library only. It constructs the twisted and untwisted graph from its defining edges, runs breadth-first graph-metric computations and a separate Bron–Kerbosch maximal-clique enumeration, expands every simplex, and tests every collapse by enumerating all codimension-one cofaces at that exact stage.

Tested \((m,n)=(7,7),(7,8),(8,9),(9,10)\) in each topology. For twisted grids the expected numbers of collapses are \(441,504,648,810\). All actual candidate maximal simplices equal the proposed stars and squares; every elementary collapse succeeds, the surviving simplices equal the stated target triangulation, and mod-two and mod-three boundary ranks agree with the expected Klein-bottle homology. The four untwisted controls have mod-three homology of the torus. The output concludes with `VERIFY_OK`.

The code verifies a finite sample; the universal theorem depends on the local Manhattan-distance classification, deck-displacement bound, free-face proof, and quotient topology arguments in RESULT.md. Integer torsion in the universal family is determined by the explicit Klein-bottle triangulation and its standard cellular chain complex, not inferred solely from finite-field samples. Independent audit is not performed.

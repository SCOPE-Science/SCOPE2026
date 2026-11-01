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

## Reproduction
Run `python verify.py` from the directory containing the embedded code. Only the Python standard library is required; `verification_output.txt` records its deterministic output. The source graph is generated from the Cayley rule over four-bit vectors. No input dataset is fetched or assumed.

## Exact checks
The program independently verifies the Clebsch strongly regular parameters \((16,5,0,2)\), enumerates sixteen ten-vertex open neighborhoods in its complement, enumerates all 11,804 nonempty simplices, constructs 4,780 elementary collapses and 1,050 additional vertex-toggle matchings, and topologically sorts every one of 65,680 directed Hasse incidences. Its critical vector is exactly one cell in dimension zero, six in dimension three, and 137 in dimension four. It computes signed integral gradient-path degrees and reproduces an explicit six-by-six minor of determinant one, with critical four-cell indices 2, 4, 9, 10, 23, 26 in sorted face-mask order. It directly computes nine simplicial mod-two boundary ranks from the unreduced complex, finding reduced Betti rank 131 only in dimension four. It independently enumerates all 65,536 candidate dominance subsets and finds Euler characteristic \(-130\).

## Mathematical inference and limits
A unimodular full-row-rank integer degree matrix for attachments of four-cells to a wedge of three-spheres permits integral changes of cellular basis; since \(\pi_3\) of the three-sphere wedge is its degree lattice, no extra attaching-map invariants intervene. Six degree-one attachments cancel the three-cells, leaving 131 four-spheres. The dominance homology follows from the published combinatorial Alexander-dual identity over the sixteen-vertex ground set. Mod-two checks and Euler characteristic alone would not establish torsion-freeness or integral homotopy; the integral attaching certificate is essential. Nothing here verifies the homotopy type of the dominance complex or classifies other graphs.

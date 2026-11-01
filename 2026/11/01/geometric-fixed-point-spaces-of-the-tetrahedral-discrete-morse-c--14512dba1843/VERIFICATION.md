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

# Reproducibility and scope

Run `python3 verification.py certificate.json` using Python 3 and the standard library from the same directory. A successful run prints `VERIFY_OK`. The checker uses the twenty-eight cover relations of the fifteen nonempty tetrahedron faces and tests both full reversed-Hasse acyclicity and closed Forman gradient-path acyclicity independently on every candidate orbit union. Every permutation of the four underlying vertices is checked, not merely one representative from each cycle class.

The exact certificate contains the orbit lists, full orbit-complex face vectors and sixty ordered simplex pairs for the transposition collapse. The checker verifies each pair is a genuine elementary simplicial collapse at the moment of deletion, and that the survivor is exactly the six-vertex octahedral boundary; this is an integral homotopy argument, not an inference from mod-two ranks. It separately checks the two connected four-cycles, contractible simplex, and empty fixed space. The computed nonidentity Euler characteristics agree with already published rational Lefschetz values, which are only a cross-check.

This certificate concerns a single finite complex, the ordinary full tetrahedral Morse-matching complex. It makes no claim about generalized/pure variants, all simplex dimensions, subgroup-system structure, or a complete equivariant homotopy equivalence. Independent mathematical audit has not been performed.

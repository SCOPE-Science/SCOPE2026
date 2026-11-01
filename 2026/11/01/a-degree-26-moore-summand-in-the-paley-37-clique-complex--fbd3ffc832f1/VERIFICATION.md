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

# Reproducibility and boundaries

Run `python3 verify.py` with the Python 3 standard library. This reconstructs all 37 vertices, 333 graph edges, 888 triangles and 555 tetrahedra directly from quadratic residues modulo 37. It tests the absence of higher simplices and verifies that the shortest-path graph diameter is two.

After a canonical breadth-first spanning tree, all 297 remaining edge generators are killed by individually verified unit triangular relations, certifying the nonabelian fundamental-group claim rather than only a rank computation. The 666 two-coface triangle rows of the third cellular boundary form three connected, consistently signable incidence components of 185 tetrahedra each; the 222 remaining rows reduce to six explicitly listed integer triples. Gcd calculations on their minors give determinantal divisors (1,1,26), proving the full integral Smith invariants, including 13-primary torsion. Modulo 2, 3 and 13 ranks independently corroborate the computation but are not substituted for integral proof.

`verification_output.txt` is the program's recorded output. Successful replay ends with `ALL_CHECKS_PASS`. Recompute directly from the embedded script; the recorded output alone is not a proof. Homotopy classification uses the standard three-dimensional simply-connected CW argument and the homology Whitehead theorem, not a separate independent topological certification. Independent audit: not performed.

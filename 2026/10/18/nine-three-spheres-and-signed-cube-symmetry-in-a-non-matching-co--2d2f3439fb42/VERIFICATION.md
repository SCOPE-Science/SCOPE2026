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

# Finite reproduction and limits

The standalone `verify.py` uses only Python 3's standard library. Running `python3 verify.py` deterministically prints a single JSON object; its actual output is stored byte-for-byte as `verification_output.json`.

The program constructs \(Q_3\) as the graph on 3-bit words, tests every one of the 4096 edge subsets against all 44 three-matchings, and counts 601 augmented faces, including 12 vertices, 66 edges, 176 triangles, 222 tetrahedra, 108 4-simplices and 16 5-simplices. The explicit pivot order is `(2,10,11,5,0,4,9,6,7,3,8,1)`. After removing the augmented empty-face match, the ordinary matching has 295 pairs, one critical vertex and nine critical three-simplices; a complete directed Hasse sort reaches all 600 nonempty faces. This finite acyclicity certificate, together with the ordinary discrete-Morse theorem, proves the integral homotopy classification.

A distinct exact mod-two boundary rank calculation yields `(11,55,121,92,16)` for the boundary maps in dimensions 1 through 5. Direct signed simplicial Lefschetz calculations for all 48 automorphisms agree with the rational representation character; the observed character histogram is `{-1:6,0:16,1:15,3:10,9:1}`. Rational character uniqueness supplies the representation identification. These are exhaustive checks for one graph, not sample-based extrapolation to a larger family.

The result is not an integral representation-theoretic classification, and it does not cover larger crown graphs. Literature discovery cannot formally guarantee that no equivalent prior account exists. The file supplies neither an independent external audit nor experimental evidence for infinite cases.

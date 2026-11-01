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

The mathematical proof in RESULT.md supplies the unbounded integral classification. The included standalone checker uses only Python 3 and requires no network access or external packages.

Execute `python3 check_windmill.py` alongside the file. It exhaustively enumerates simplices for twelve finite parameter sets, computes every reduced mod-two homology group by boundary-matrix reduction, tests explicitly generated within-block and equal-size-block automorphisms, and compares 92 selected signed Lefschetz numbers plus all 1,416 elements of three small full automorphism groups with the derived integral character formula. All tests passed on the included source.

The computations neither prove an infinite theorem nor check integral torsion directly. Integral freeness and the natural symmetry modules follow from the explicit chain-kernel identification, join Künneth theorem, and natural deletion–link long exact sequence in the written proof. Independent audit has not been performed.

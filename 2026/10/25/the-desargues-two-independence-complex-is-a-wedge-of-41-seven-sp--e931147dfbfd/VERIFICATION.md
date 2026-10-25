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
# Computational verification

Run `python3 verify.py > verification-output.json` from this directory. The archived JSON is the output of an actual successful run with `verification: VERIFY_OK`.

The program independently checks all \(1{,}048{,}576\) possible vertex masks against (i) the induced-degree condition and (ii) sixty forbidden connected triples, yielding \(62{,}049\) faces including the empty simplex. It constructs a complete sequential vertex-toggle matching with \(31{,}001\) augmented pairs, then topologically sorts the entire reversed-cover Hasse directed graph. It finds three critical six-cells and forty-four critical seven-cells, and verifies that the Morse boundary contains a \(3\)-by-\(3\) integral minor of determinant \(-1\) (rows \(0,3,14\), indexed from zero). It also checks the reduced Euler characteristic against \(-41\).

The exact signed integral Morse coefficients are produced by recursively solving paired-boundary relations, not by approximating ranks over a finite field. The verifier uses only the standard Python library and no data files. All required critical faces, matrix rows, and the unit-minor certificate are in `verification-output.json`.

**Limits.** The calculation is exhaustive for the specified twenty-vertex input only. The topological deduction from the computed acyclic matching uses standard discrete Morse theory and the Hurewicz theorem; computational repetition is not an independent scientific audit. No conclusion is drawn for the wider generalized Petersen family.

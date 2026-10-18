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

# Finite certificate and proof replay

Run `python3 verify.py` with standard Python 3. The attached `verify_output.txt` is the actual captured output of a successful execution.

The program enumerates all twenty three-subsets lexicographically, constructs all twenty radius-one closed neighborhoods and their simplicial subfaces, and independently checks the membership of **every** nonempty subset of the twenty vertices using common neighborhood centers. It checks the exact face-vector length \(10\), including twenty maximal nine-dimensional simplices.

It stages the explicit partial matching in vertex order \(0,1,\ldots,19\), then constructs the full reversed-Hasse incidence digraph and proves its acyclicity by exhaustive topological sorting. It counts every one of the \(87{,}800\) directed covering incidences rather than sampling them. Finally it performs exact signed integer reductions for the Morse differential of every critical 4-cell against the eleven critical 3-cells, confirming thirty zero boundary columns.

The verifier is a finite reproducible certificate for the completely specified graph, not a general Johnson-parameter proof or an independent external audit. The paper proof describes the CW decomposition and the algebraic-topological implication from zero attaching degrees to an integral wedge. No black-box CAS, floating-point rank, source-file download, random seed or nonportable dependency is used.

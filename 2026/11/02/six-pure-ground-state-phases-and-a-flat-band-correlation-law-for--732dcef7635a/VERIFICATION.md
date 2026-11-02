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

# Reproducible verification

Run `python3 verification.py` in a directory containing this document, `verification.py`, and the embedded output file. The program uses only the Python standard library. Its deterministic output is in `verification_output.txt`.

The checker constructs every affine configuration for \(d=1,2,3,4\) for each of six local multisets, checks all coordinate triangles and the exact strict-phase state counts. It enumerates all \(3^9=19683\) spin configurations of \(H(2,3)\) at each of the six rational phase witnesses, checking absolute energies and degeneracies. It then computes exactly (not by floating-point approximation) every ordered-pair covariance on dimensions \(1,2,3\) for the uniform minimizing ensemble, totaling 4914 pair comparisons. Six strict-phase witness inequalities are checked.

These finite calculations do not establish the infinite family alone. The proof is a local exact decomposition, elementary affineness induction, and finite-field character orthogonality as laid out in RESULT.md. The theorem does not provide a coexistence-boundary multiplicity formula, a positive-temperature result, or independent scientific certification.

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

# Reproducibility and limits

Execute `python3 verify.py` alongside `certificate.json` using a standard Python 3 interpreter. The complete deterministic finite verification output appears in `verification_output.txt` and ends with `VERIFY_OK`.

The checker reconstructs all \(598\) faces from the six quadratic residues, tests each of the \(227\) free elementary collapse pairs, checks all remaining simplices and the \(12\)-edge spanning tree, and checks the \(47\) unit-generator triangular relations eliminating the fundamental group. It then independently reconstructs the complete original complex and checks signed simplicial Lefschetz traces of all \(78\) affine symmetries against the character and the stated permutation-module decomposition. Integer arithmetic and comparisons are exact.

The homotopy theorem is an exact finite combinatorial argument plus standard topological consequences; the verifier's success is not independent external mathematical validation. The certificate does not establish equivariant collapsibility or an integral affine module decomposition, nor does it cover other Paley graph orders. Independent audit: not yet performed.

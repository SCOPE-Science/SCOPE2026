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

# Reproduction and limits

Use Python 3 standard library, from the directory containing the extracted files:

```
python3 artifacts/verify_primary.py
python3 artifacts/crosscheck_field.py
```

Both scripts reconstruct the graph; neither uses network access nor outside datasets. The scripts perform complete finite enumerations, direct acyclic-matching checks, integral signed gradient-path substitution, exact fraction-free determinant calculation, graph-automorphism orbit verification, and a separate full simplicial rank computation over two prime fields. The captured output in `artifacts/verification_output.txt` reports the actual face vectors, matching pairs, critical counts, boundary-matrix sizes and unimodular minors, all full modular ranks, and the successful verification markers `PRIMARY_VERIFIED` and `FIELD_CROSSCHECK_OK`.

The face count is finite and exhaustiveness follows from the explicit recursion over all 24 graph edges, not from samples. The rational column-pivot calculation is used only to select a square minor; its determinant is recomputed by exact integer elimination. The integral homotopy conclusion also uses the stated standard algebraic Morse and Hurewicz/CW cancellation theorems. Computational agreement over two fields would not, alone, establish integral torsion absence or homotopy equivalence. No independent scientific audit has been performed.

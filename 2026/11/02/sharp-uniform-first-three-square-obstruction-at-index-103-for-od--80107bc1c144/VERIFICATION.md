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

Run `python3 verify.py` in a directory holding `COVER.tsv` and `SHARPNESS.tsv`. The checker is self-contained and uses only Python's standard library. It constructs coefficients independently from the truncated infinite product for every residue leaf, tests the certified congruence and modulus margin, and verifies the binary prefix-class coverage of all odd residues modulo \(2^{15}\). Its separate logarithmic-derivative recurrence for the \(613\)-color witness is cross-checked against factor multiplication and all \(104\) exact valuations recorded in `SHARPNESS.tsv`.

The proof's extension from those finitely checked residue cylinders to all positive odd numbers of colors uses the congruence lemma proved in `RESULT.md`. The executable arithmetic test alone does not establish bibliographic originality or external scientific certification.

Expected final output: `VERIFY_OK leaves=156 covered_odd_classes=16384 maximum_index=103 maximum_depth=15 sharp_color=613 sharp_index=103 crosscheck=product_vs_derivative`.

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

# Reproducible checks

Run `python3 verify.py` from the directory containing this document and the program. It requires no nonstandard packages. Its successful terminal marker is `VERIFY_OK`.

The program checks the explicit unit-group polynomial homomorphism for each allowed parameter over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), including both inputs from the entire radical, and checks scalar-congruence classification by enumeration of invertible two-by-two changes of basis over these fields. It directly counts rank-at-most-one two-by-\(s\) matrices for \(s=2,3\) and checks full-algebra commuting pairs for \(q=2,3\). Its outputs include 769916 multiplicativity cases, 57 congruence cases, and eight determinantal tuple cases.

These checks are finite corroborations, not an infinite proof. The all-field and all-arity claims follow from the symbolic multiplication and scheme-ideal calculations in RESULT.md; no external or independent audit has been performed.

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

# Verification details

Running `python3 verify.py` from the extracted artifact tests every matrix over \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\) for \((n,q)=(2,2),(3,2),(2,3),(2,4)\), recovering the Smith torsion multiplicity through an independent doubled field-linear representation. Every \(2\times2\) matrix over \(\mathbb Z/4\mathbb Z\) and \(\mathbb Z/9\mathbb Z\) is also enumerated directly; the Smith multiplicity is deduced from the image size rather than a coefficient-field representation. Normalization is checked for \(1\le n\le8\) and \(q\in\{2,3,4,5,7,8,9\}\). Expected successful completion markers are `VERIFY_OK` and `VERIFY_OK_CHAIN_RINGS`.

The symbolic argument, not the finite cases, proves the theorem for arbitrary residue-field orders, matrix sizes and commutative length-two chain rings. No computational claim is made beyond the enumerated sizes. Independent audit has not been performed.

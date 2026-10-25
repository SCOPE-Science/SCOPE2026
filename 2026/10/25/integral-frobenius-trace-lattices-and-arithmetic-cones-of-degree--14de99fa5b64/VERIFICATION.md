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

# Verification

The mathematical proof uses a primitive fixed lattice of the geometric Picard pairing; this is important because the rational fixed space alone does not capture trace-lattice indices. Running `python3 verify_degree5.py` from the same directory, with `requirements.txt` installed, gave the seven expected rows and ended in the exact assertion:

`VERIFY_OK: all 120 Weyl group elements; seven Frobenius types, primitive Picard lattices, Gram SNF, full trace indices, exact effective and nef cone rays`

The script enumerates every one of the 120 elements of the \(A_4\) Weyl group, tests invariance of the lattice pairing and the ten geometric exceptional curve classes, computes primitive fixed lattices by exact unimodular elimination, and evaluates Smith normal forms, integer index minors, and rational primal/dual cone extremality. The seven Frobenius conjugacy classes have sizes 1, 10, 15, 20, 20, 30, 24. Every representative within each class reproduces its designated table row. This finite computation is exhaustive over the Weyl group, but it assumes the published geometric classification of all smooth degree-five del Pezzo surfaces, the standard geometric cone theorem, and finite-field descent.

Limits: no independent external validation was performed; the scientific priority comparison remains qualified, especially against equivalent Weyl-group descriptions. No claims are made about singular surfaces or integral effectivity of arbitrary cone lattice points.

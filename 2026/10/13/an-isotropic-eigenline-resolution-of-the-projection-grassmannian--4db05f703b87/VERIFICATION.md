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
# Verification notes

The general proof is mathematical: a repeated root is equivalent to an isotropic eigenline; the line-incidence equations are a globally surjective linear morphism of vector bundles over a split quadric; the generic defective block has one isotropic eigenline; and a first-order perturbation proves the discriminant equation reduced.

Exact checks: `python verification/check_discriminant.py` (Python 3, SymPy 1.14). In an inspected copy of the package the program returned `VERIFY_OK`. The program verifies the square-zero isotropic block, the size-two factorization, quotient evaluation-map ranks for \(3\le n\le8\), and the nonvanishing first-order coefficient in the same finite range. The code is not an infinite proof and does not determine the full exceptional fiber schemes.

Originality limitations: searches may miss earlier equivalent representations of the characteristic discriminant, in particular in invariant theory, eigenvector incidence geometry and representation theory. The earliest public source for the ED-discriminant identification is arXiv:2610.02018v1 (2026-10-01). Independent audit has not been performed.

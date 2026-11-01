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

The proof uses a standard two-particle cubical deleted-product model, an integral injectivity argument for the second boundary, and equality of rational representations in an equivariant Euler identity. The absence of higher-dimensional cubes and the finite group's semisimplicity are used explicitly.

Run `python unicyclic_two_point_verify.py` in this directory. The self-contained Python script verifies automorphism actions on all cellular degrees with orientation signs, and separately checks the fixed-local-data formula. It checks eight unicyclic graphs and sixty-six automorphisms. The exact output is embedded in `unicyclic_two_point_verification_output.txt`.

Finite experiments do not prove the universal statement; that claim is supported by the combinatorial and representation-theoretic arguments in `RESULT.md`. No integral equivariant splitting, independent audit, or external certification is claimed.

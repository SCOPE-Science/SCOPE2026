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

`verify.py` constructs each complete multipartite graph directly from its part sizes, tests total domination from open neighborhoods, computes the number of connected components of the complement from the literal induced graph structure, and compares every subset against the theorem. It then compares every coefficient of the bivariate enumerator and every stated minimum formula.

The replay output is:

`VERIFY_OK profiles=127 subset_checks=64912 criterion_checks=614128 coefficient_checks=1097 gamma_checks=1049 boundary_checks=20 max_order=10`

The checker also verifies the boundary family \(K_{m,n}\) for \(2\le m\le n\le7\): no TO\(n\)CDS exists, including \(K_{2,2}=C_4\). This finite computation supports error detection only; the proof in `RESULT.md` establishes the theorem for all admissible part sizes.

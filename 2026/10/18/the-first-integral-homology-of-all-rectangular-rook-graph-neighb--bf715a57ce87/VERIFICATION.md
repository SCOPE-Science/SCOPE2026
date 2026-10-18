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

# Verification and reproducibility

The symbolic classification is proved for arbitrary abelian coefficient groups, hence determines the integral torsion without relying on a selected set of mod-prime ranks. See the complete normalization, triangle-relation enumeration and explicit cocycle constructions in `RESULT.md`.

Run `python3 verify_rook_h1.py` (Python 3 standard library; no other dependencies). The script reconstructs the open-neighborhood simplices from the rook adjacency rule; asserts the complete 1-skeleton; enumerates triangles; verifies explicit generating cochains and their cocycle identities; computes exact prime-field boundary ranks using finite-field Gaussian elimination; checks seven board sizes; and prints `ROOK_H1_FINITE_CHECKS_OK`. The recorded output is `verification_output.txt`, including dimensions over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\).

Separately, an exact integer Smith-normal-form comparison on the normalized relation matrix for \((3,3),(3,4),(4,4)\) found respectively two free factors, one free factor, and a single invariant factor two. The optional `integer_smith_check.py` (requires SymPy) independently generates the three normalized relation matrices and computes their exact Smith forms; its output is `smith_output.txt`. This finite calculation is corroborative, not a substitute for the symbolic proof.

No independent mathematical audit has been performed. The implementation does not check infinitely many board sizes or resolve the homotopy type. Equivalence to any unindexed earlier formulation remains a residual literature-search risk.

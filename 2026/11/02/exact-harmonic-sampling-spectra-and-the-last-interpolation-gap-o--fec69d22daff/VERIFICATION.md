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

The mathematical checker is `verify_dodecahedron.py`, written entirely with the Python standard library. Its checks reconstruct the twenty normalized dodecahedral vertices over \(\mathbb Q(\sqrt5)\), select ten antipodal representatives, verify the signed-matrix relations \(C^2=2I-C+J\), \(B^2=A+3I\), and \(B^3=5B\), and compute exact rational reduced-Gram eigenvalue numerators in every degree \(0\le k\le185\). It checks the eight exceptional ranks and nonnegativity at every tested degree. Finally it checks the elementary rational inequality needed to apply the analytic tail estimate from degree \(186\) onward.

The global theorem does **not** follow merely from a finite numerical experiment; the integral estimate for Legendre polynomials in RESULT.md supplies the infinite tail. No floating-point eigenvalue estimate, formal prover, independent audit, or outside certification is claimed.

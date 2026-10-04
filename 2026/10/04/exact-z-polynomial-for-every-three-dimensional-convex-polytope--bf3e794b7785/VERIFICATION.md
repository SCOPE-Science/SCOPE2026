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

The universal proof is analytic and combinatorial. The verifier does not substitute finite enumeration for that proof.

`verify.py` checks the coefficient identities
\[
[x^3]Z_P=v+f-4,
\qquad
[x^2]Z_P=6+8e-6(v+f)=2(v+f)-10
\]
under \(v-e+f=2\), verifies the \(\gamma\)-vector \((1,v+f-8,0)\), and verifies the factor discriminant \((v+f-8)(v+f-4)\). It runs exact integer arithmetic on five standard three-polytopes and prints `VERIFY_OK`.

The proof itself additionally checks why the required interval-poset counts are universal: vertex--facet incidences total \(2e\), vertex--edge and edge--facet incidences each total \(2e\), and the rank-three local toric \(g\)-coefficients sum to \(4e-3(v+f)\).

Limit: no claim is made for nonpolytopal Gorenstein* lattices or for dimensions above three.

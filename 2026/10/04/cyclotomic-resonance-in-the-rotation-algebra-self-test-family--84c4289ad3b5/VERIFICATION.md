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

The proof was checked symbolically at the level of the defining relations. On a finite-dimensional \(Z\)-eigenspace, taking determinants in \(UV=\mu VU\) gives \(\mu^r=1\) exactly. When \(t\notin E\), the scalar \(\mu+\mu^{-1}-t\) is therefore nonzero, so \(U+V=2I\); the positive identity in `RESULT.md` then forces both unitaries to equal the identity.

For resonant \(t\), the standard order-\(q\) clock and shift construction was checked by the bundled script through the exact exponent identity \(UV=\zeta VU\); the analytic construction works for every \(q\), not merely the tested sample orders. The special resonance \(t=2\) is handled by a distinct scalar character.

For \(|t|>2\), the spectrum of \(z+z^*\) lies in \([-2,2]\), hence \(z+z^*-t\mathbf1\) is invertible. This proves the exterior scalar collapse without numerical approximation.

The full primary source was inspected at arXiv:2609.25117v1, Proposition 5.2 and Theorem 5.3, including the defining relation, the root-of-unity argument, the irrational-rotation quotient, and the counts \(|S|=13\), \(|W|=14\), \(N=36\), and \(|X|=250\). The source explicitly says those sizes are presentation-specific and makes no minimality claim. The source's fixed relation is the \(t=1/2\) member after multiplication by a nonzero scalar.

The bundled checker verifies the unchanged support count for nonzero \(t\) and representative clock-shift modular identities. It is a consistency check only and is not used as an infinite proof.

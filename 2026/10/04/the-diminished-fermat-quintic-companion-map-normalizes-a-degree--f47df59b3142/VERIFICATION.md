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

The exact checker `verify.py` reconstructs the affine-chart quintics from the six displayed generators, evaluates the map at \([1:2:1]\), forms the five projective cross-multiplication equations against the nonzero third coordinate, and verifies their factorizations over the integers. It also checks the algebraic branch exclusions used to prove the fiber is a singleton and the Jacobian determinant \(-480\), proving that the singleton fiber is reduced.

The checker does not attempt to compute defining equations or the singular locus of the image surface. Finiteness uses the mathematical argument that the pullback of a hyperplane is the ample bundle \(\mathcal O_{\mathbb P^2}(5)\); degree \(25\) then follows from the finite birational degree formula. Independent audit has not been performed.

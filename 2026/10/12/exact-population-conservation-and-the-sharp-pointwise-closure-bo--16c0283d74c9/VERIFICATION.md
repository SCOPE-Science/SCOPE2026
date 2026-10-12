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

The proof is analytic. `verify.py` checks the exact cancellation of reaction terms and the explicit cosine witnesses used for necessity.

For the no-chemotaxis witness, it confirms that a pointwise-constant initial sum has initial derivative \(\varepsilon k^2(D_I-D_S)\cos(kx)\), so unequal diffusivities cannot preserve the manifold for all admissible data.

For the chemotactic witness with equal relevant diffusion contribution at the midpoint, it confirms \(\partial_x^2\log(1+\varepsilon\cos(kx))=-\varepsilon^2k^2\) at \(x=L_x/2\). Therefore a nonzero \(\chi\) changes the compartment sum there.

The checker does not establish PDE existence or numerical convergence. It verifies only the finite algebraic identities used in the proof. Running `python3 verify.py` returns `VERIFY_OK`.

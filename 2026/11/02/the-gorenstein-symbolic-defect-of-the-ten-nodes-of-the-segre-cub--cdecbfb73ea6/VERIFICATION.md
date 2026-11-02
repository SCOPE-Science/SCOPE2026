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

# Reproducibility and mathematical checks

Run `python verify.py` under Python 3 with SymPy 1.14 or a compatible version. The included `verification_output.txt` is an exact successful output of the packaged verifier. Computations use rational arithmetic only, not floating-point tolerances.

The script computes reduced Gröbner bases for the five node quadrics, for their ordinary square and for the ordinary square plus the Segre cubic; it checks all leading monomials and hence the standard-monomial staircases of lengths ten and fifty. The leading monomials are all independent of \(x_0\), verifying the free \(k[x_0]\)-module structure used in the saturation argument. It verifies all ten singular points, checks direct degree-three and degree-four first-jet ranks \(34\) and \(50\), and reduces degree-five and degree-six products to establish the \((1,5,1)\) symbolic defect and the nondegenerate pairing.

The exact proofs in the accompanying result establish equality of ideals over any characteristic-zero field. The finite computations alone would not justify a claim about higher symbolic powers, positive-characteristic reductions, or all projective point configurations. No independent audit is claimed or performed.

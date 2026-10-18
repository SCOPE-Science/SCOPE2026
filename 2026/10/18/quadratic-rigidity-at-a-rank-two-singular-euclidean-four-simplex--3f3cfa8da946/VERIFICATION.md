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

In a directory containing `checker.py` and `requirements.txt`, install `sympy>=1.12` and run `python checker.py`. The script independently constructs ten Heron polynomials from ten squared-edge coordinates, evaluates their original values, checks the ten-by-ten Jacobian and nonzero eight-by-eight minor, reproduces two right-null and two left-null vectors, and symbolically compares the projected area polynomials and the displayed sum-of-squares certificate. It verifies positive-definite Gram matrices at both signs of one rational kernel perturbation and their exact quadratic area scaling.

The checker is an exact algebraic certificate for the finite polynomial identities, not a test of all nearby simplices. The theorem's uniform local lower bound follows from the separate kernel/complement contradiction argument in `RESULT.md`, which uses continuity and finite-dimensional norm estimates. The local Euclidean domain is justified by the openness of positive definiteness at the base Gram matrix \(I_4/2\). No generalization to all simplices, global area-fiber uniqueness, or independent external audit is asserted.

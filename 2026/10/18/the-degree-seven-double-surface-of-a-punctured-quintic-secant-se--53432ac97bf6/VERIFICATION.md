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

# Reproducibility and limits

Run `python verify.py` in an environment with SymPy (version 1.12 or later). The checker reconstructs the four maximal minors of the Hankel matrix, computes a resultant quotient giving the defining sextic, verifies the triangular normal-form polynomial identity, evaluates the two-point secant parametrization, checks the gradient on the hyperplane at infinity and the graph cubics, and computes a generic section of the graph consisting of seven simple points. It also verifies an exact nondegenerate transverse Hessian.

As a separate finite check it evaluates every point of \(\mathbb P^4(\mathbb F_p)\) for \(p=5,7,11\), comparing the gradient-defined singular support to the three-cubic surface: the singular-point counts are respectively \(36,64,144\) in both descriptions. The program terminates with `VERIFY_OK` on success.

The proof of the characteristic-zero infinite-field assertions is in `RESULT.md`: finite-field sampling alone does not certify them. The numerical generic slice corroborates, but does not replace, the degree-seven complete-intersection argument. No independent audit has been performed.

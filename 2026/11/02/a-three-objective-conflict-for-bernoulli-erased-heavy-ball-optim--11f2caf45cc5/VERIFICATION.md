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

# Reproduction and mathematical checks

Run `python verify.py` from the extracted file set, after satisfying `requirements.txt`. The verifier rederives the exact quadratic Lyapunov identity and transfer coefficients symbolically, checks the derivative of the stability frontier, and compares the three-moment recursion against a direct enumeration of all binary histories for a rational parameter grid. It also verifies the strict all-horizon lower bound and uniqueness on this grid, tests exact stability-boundary algebra, and rechecks the rational example at probability \(p=4/5\). The scientific proof establishes the stated universal quantifiers independently of this finite test suite.

The identity \(\mathbb E[A_n^{\mathsf T}PA_n]-P=-D\operatorname{diag}(1,0)\) is verified by algebra, with the boundary \(D=0\) treated using conserved positive quadratic energy. The excluded \(D<0\) region uses the stationary-moment contradiction in RESULT.md, not numerical spectral tests. The stationary mean-square error \(\sigma^2/D\) is obtained from exact stationary moment equations, while the finite-horizon lower bound comes from the all-erasure event and two witness paths establish uniqueness. No convergence claim is inferred from a finite simulation. No external human review or independent verification has been performed.

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

Run `python check.py` in a Python environment with SymPy. The checker uses exact symbolic arithmetic to verify the displayed Lyapunov derivative, three equilibria, planar harmonic family and characteristic polynomials. It asserts each equality and prints PASS only after all assertions succeed.

Analytical steps not replaced by computation: (i) every forward-bounded polynomial ODE solution extends to all nonnegative times; (ii) a compact connected omega-limit set lies in the largest invariant subset of \(\{\dot L=0\}\) when \(L\) is monotone; (iii) integration of \(\dot z=x^2-y\) and the exact logarithmic equation excludes a symmetry-plane limit for nonzero \(x\) at \(a=0\); (iv) rotation invariance uniquely fixes conditional angular measures on harmonic circles. These are explicit mathematical arguments in RESULT.md, not conclusions from solver traces.

Limits: the theorem assumes bounded forward trajectories, gives no estimates for unbounded solutions, and does not classify nonrecurrent heteroclinic subsets of compact invariant sets. Independent validation has not been performed.

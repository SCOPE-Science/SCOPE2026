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

## Reproducible checks

Execute `python3 checks/verify.py` from a directory containing the supplied checker after installing `sympy` (version \(1.12\) or later). The checker was executed successfully with exact symbolic arithmetic and printed `EXACT_SYMBOLIC_CHECK_PASS`.

It checks
\[
p_*'(z)=4(z+8/5)(z^2+1),
\]
all three factorizations of \(p_*(z)-p_*(\zeta)\) for \(\zeta\in\{-8/5,i,-i\}\), and the convex combinations for \(w=2/21\). In the first fiber the average of its noncritical conjugate roots is \(8/15\), and the exact barycentric weight of that midpoint relative to \(-8/5\) is \(89/112\). For the conjugate fibers the exact weights are \(9/14\) and \(5/14\).

## Proof obligations not delegated to computation

The all-quadratic and all-cubic cases are proved symbolically for arbitrary complex coefficients in `RESULT.md`. The finite symbolic check is not offered as exhaustive evidence for infinitely many cubics. Convexity and the real-part separation used to exclude the witness from the derivative hull are elementary exact inequalities. No general full-shifts theorem is assumed, in particular none from the withdrawn primary manuscript.

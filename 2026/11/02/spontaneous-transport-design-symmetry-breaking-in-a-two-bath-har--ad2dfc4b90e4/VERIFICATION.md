---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For both positive dampings the deterministic mechanical energy has negative dissipation except at zero velocity, and positive definite stiffness (determinant ab+kP) makes the origin the largest invariant subset there. The drift is Hurwitz. Reconstructing the stationary moment equations with q=E[x1 v2]=-E[x2 v1] gives Γ E[v1 v2]=(b−a)q. Eliminating the position moments gives k(E[v1²]−E[v2²])=[(a+k)γ2+(b+k)γ1]q+(b−a)E[v1 v2]; the diagonal velocity balances identify J=kq and recover the stated denominator. With the two budgets it is a constant plus δ²+(Γ²/2)δη+4k²/(1−η²). For r=|η| the δ minimizer is the clipped unconstrained minimizer. Before clipping the derivative in r is r[8k²/(1−r²)²−Γ⁴/8]; after clipping it is 8k²r/(1−r²)²−Γ²P/2, strictly increasing and matched at the seam. This covers the symmetric regime even when clipping occurs, proves uniqueness at Γ²=8k, gives the interior or unique clipped optimum with the stated mirror symmetry above threshold, and excludes |η|=1 by divergence. At P=P_c the formulas meet at r_0. In the example the denominators are 40 and 44 with numerator 4, giving 1/10 and 1/11. The real Langevin noise presupposes nonnegative bath temperatures.

## originality

PASS

Pass restricted to the complete optimizer classification under the two simultaneous allocation budgets, not to the known heat-current law. That law supplies the objective; it does not by itself classify the constrained global minimizers. No inspected source states that phase diagram or establishes a stronger optimization result covering it.

## value

PASS

The budgets turn a standard transport model into a natural resource-allocation problem. A complete global symmetric-to-mirror-optimum threshold, followed by a distinct active pinning constraint, answers when equal allocation costs performance and gives the usable allocations, including the boundary and critical regimes. The value is in the design classification, not an extra derivation of the forward formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.

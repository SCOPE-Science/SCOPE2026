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
The verification target is the exact reduction of the published two-phase sign condition to a one-dimensional Cauchy integral.

Run `python3 verify.py`. A successful replay prints `VERIFY_OK`.

The checker performs four independent finite checks: it confirms the exact crossover relation numerically at \(q_0=\sqrt{3/5}\) and the root ordering on representative values; compares the trigonometric criterion with the tangent-polynomial criterion on a deterministic nonsingular phase grid; evaluates the one-dimensional formula by adaptive Simpson quadrature after \(q=\tan u\); and separately estimates the original two-dimensional torus area by a \(900\times900\) midpoint grid.

The numerical area check is not a proof of the infinite limiting statement. The proof is the explicit half-angle algebra, root ordering, Cauchy conditioning, and equidistribution argument in `RESULT.md`. The checker also does not re-derive the source's asymptotic Floquet criterion.

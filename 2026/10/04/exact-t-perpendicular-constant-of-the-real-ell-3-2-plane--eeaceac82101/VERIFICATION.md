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

Run `python3 verify_tperp_l3.py`. The script returns `VERIFY_OK` and prints the isolated algebraic parameter and the reconstructed value of \(T_{\perp}(\ell_3^2)\).

The exact checks are:

1. The transition polynomial \(8u^3+7u-1\) has exactly one zero in \((0,7/50)\).
2. The small positive-orientation derivative resultant factor has no zero in \((0,7/50)\), and the actual implicit derivative is positive at \(t=2/5\).
3. The large positive-orientation resultant factor is the degree-seventeen polynomial \(Q\) in `RESULT.md`; it has exactly one zero in \((0,1)\), isolated in \((0.7578975,0.7578976)\). The actual implicit derivative is positive at \(t=4/5\) and negative at \(t=19/20\).
4. The negative-orientation derivative resultant factor has exactly one zero in \((0,1)\); actual derivative signs at \(t=1/10\) and \(t=1/5\) show that zero is a minimum. Its endpoint maximum is \(56^{1/6}\).
5. The explicit positive-orientation witness at \(u=3/4\) has sixth-power objective strictly larger than \(56\), so the positive interior maximum dominates the entire negative orientation.
6. Bisection inside the exact isolating interval reconstructs \(u_*\) and the stated value to high precision.

The Sturm calculations use exact rational arithmetic. Decimal arithmetic is used only after the algebraic root has been uniquely isolated, and for derivative sign checks with wide margins; it is not a finite-grid substitute for the global proof.

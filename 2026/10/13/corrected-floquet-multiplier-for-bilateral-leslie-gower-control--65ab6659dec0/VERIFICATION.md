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

For a vertical event surface \(x=h\) with affine reset \(R(x,y)=(cx,y+d)\), the saltation determinant is
\[
\det S=\frac{P^+}{P^-}.
\]
Applying this at the two crossings of the order-2 cycle gives
\[
\mu=
\frac{P(C_4)}{P(B_4)}
\frac{P(A_4)}{P(D_4)}
\exp\!\left(\int(P_x+Q_y)\,dt\right).
\]

The lower reset is exactly
\[
D_4=(h_1,y_{D_4})
\mapsto
A_4=((1+p_1)h_1,y_{D_4}-\tau_1),
\]
so the post-jump prey velocity must be evaluated with \(y_{D_4}-\tau_1\). The source's explicit \(\tau_2\) substitution is therefore not the stated vector field at \(A_4\) when \(\tau_1\ne\tau_2\).

The script `verification/reproduce.py` numerically reconstructs the published Example 4.3 order-2 cycle. It checks the multiplier in two independent ways: saltation ratios plus a divergence integral, and a centered derivative of the scalar return map. Both give approximately \(0.192333\). The script also evaluates the printed lower-coordinate substitution, which yields approximately \(0.403518\) after the same remaining factors.

The numerical calculation verifies only the published example. The generic multiplier formula and the \(\tau_1\) correction follow analytically from the reset map and saltation determinant.

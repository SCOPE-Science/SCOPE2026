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

The proof does not depend on numerical search. The essential deterministic formulas are the equal-mean identity
\[
C_\mu(t)-P_\mu(t)=m-t,
\]
the explicit endpoint laws
\[
B_m^{\mathrm{upper}}=\frac{2(1-m)}{2-m}\delta_{m/2}+\frac{m}{2-m}\delta_1,
\]
\[
B_m^{\mathrm{lower}}=\frac{1-m}{1+m}\delta_0+\frac{2m}{1+m}\delta_{(1+m)/2},
\]
and the mean-preserving compression \(T_\delta(x)=m+(1-\delta)(x-m)\).

Run the standalone `verify.py` in Python 3 with no third-party packages. It constructs exact rational measures for several interior means (including near-boundary means), verifies every mean and the opposite signs of the low-/high-strike stop-loss inequalities, and checks perturbations of a strict convex-order pair. For \(m=1/2\), the symmetric exact witness yields
\[
C_F(1/8)-C_G(1/8)=-1/240,
\qquad
C_F(7/8)-C_G(7/8)=1/240.
\]
Successful output is exactly:
`VERIFY_OK mean=1/2 low_gap=-1/240 high_gap=1/240 smooth_margin_positive=true`.

The checks establish these finite algebraic identities only. Weak compactness, empty relative interior for every comparable pair, and exact-mean smoothing are proved analytically in `RESULT.md`; an infinite claim is not inferred from the finite replay.

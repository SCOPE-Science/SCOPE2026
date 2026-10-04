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

The source's Case-3 equilibrium polynomial was reconstructed as
\[
p(u)=u^3+(L-1)u^2+(D-E)u+(N-A).
\]
With \(J=1-L\), setting \(D_1=J^2-3(D-E)=0\) forces \(D-E=J^2/3\). Exact differentiation then gives
\[
p'(u)=3\left(u-\frac J3\right)^2.
\]
Substituting \(D_1=0\) into the source's printed discriminant expression gives
\[
\Delta_2=\left(J^3+27(N-A)\right)^2,
\]
so the published condition \(D_1=0\), \(\Delta_2<0\) is impossible. The equality \(\Delta_2=0\) is equivalent to \(N-A=-J^3/27\), and then direct expansion yields
\[
p(u)=\left(u-\frac J3\right)^3.
\]

`verify.py` checks these identities symbolically and asserts that \(Q\) does not appear in either the equilibrium cubic or its derivative. The verification is algebraic and exact. It does not test stability, bifurcation normal forms, or biological parameter-path transversality.

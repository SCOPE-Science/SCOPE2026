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

The claim was checked directly from the multiplication law
\[
(a,u)^2=(a^2,2au).
\]
In coordinates this gives the quadratic coordinate space
\[
\operatorname{span}\{x_0^2,x_0x_1,\ldots,x_0x_r\}.
\]

The explicit upper-bound decomposition uses \(x_0^2\) and the two squares \((x_0+x_i)^2,(x_0-x_i)^2\) for each \(i\). The lower-bound check projects arbitrary candidate squares \((a_jx_0+\beta_j)^2\) onto \(\operatorname{Sym}^2(V^*)\). The required mixed terms force the \(\beta_j\) to span \(V^*\), so their square span has dimension at least \(r\); together with the \(r+1\)-dimensional coordinate space in the projection kernel, this forces at least \(2r+1\) summands.

The argument is symbolic and uniform in \(r\). It does not infer an infinite statement from finite experiments. It uses division by \(2\), so characteristic \(2\) is outside scope.

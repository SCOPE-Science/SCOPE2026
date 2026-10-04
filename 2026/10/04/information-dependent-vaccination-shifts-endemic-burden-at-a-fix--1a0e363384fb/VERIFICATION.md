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

The analytic proof uses the source endemic-equilibrium equation after writing \(e=a/b\) and \(C=(p_0\sigma+\mu)(R_0-1)\):
\[
F(I)=\beta I+\frac{e\sigma u_0I}{1+eu_2I}-C.
\]
The universal checks are symbolic: \(F_I>0\), \(F_{u_0}>0\), \(F_{u_2}<0\), and \(F_e>0\), so the implicit-function signs follow immediately. The large-\(u_0\) limit follows from the same exact equation and does not depend on numerical extrapolation.

The bundled `verify.py` independently replays the source's printed baseline parameters with decimal arithmetic and a bracketed root solver. It verifies the equilibrium residual, checks that increasing \(u_0\) or \(a\) lowers the root, checks that increasing \(u_2\) or \(b\) raises it, and verifies numerically that \(u_0I^*\) approaches \(Cb/(a\sigma)\) for large \(u_0\). It prints `VERIFY_OK` only if all checks pass.

Limits: the computation is a reproducibility check, not an exhaustive proof over the positive parameter domain. Neither the proof nor the checker establishes monotonicity of transient infection peaks, preservation of equilibrium stability, or finite-parameter eradication for \(R_0>1\).

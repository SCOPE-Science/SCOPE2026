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

The proof is exact algebra. Starting from the published two-block strictly contractive Peaceman–Rachford iteration, solve the scalar quadratic subproblems explicitly and use the state \(v^k=(y^k,\lambda^k)^T\). Direct elimination yields
\[
\det M_\alpha=\frac{\beta^2(1-\alpha)^2}{(a+\beta)(b+\beta)}
\]
and
\[
\operatorname{tr}M_\alpha
=\frac{\beta^2\alpha^2-2\beta(a+b+\beta)\alpha+ab+a\beta+b\beta+2\beta^2}{(a+\beta)(b+\beta)}.
\]
Substitution of \(u=\beta/\sqrt{(a+\beta)(b+\beta)}\) and \(w=\beta(a+b+\beta)/((a+\beta)(b+\beta))\) gives the formulas used in the proof.

The repeated-root equation is
\[
T(\alpha)+2u(1-\alpha)=0.
\]
Under the stated penalty ordering it has exactly one root in \((0,1)\), because its value is positive at zero, negative at one, and its derivative is strictly negative on the interval. At that root the discriminant vanishes and the repeated eigenvalue is negative.

`verify.py` uses only the Python standard library. It reconstructs the recurrence coefficients directly from the four scalar updates using rational arithmetic, compares its trace and determinant against the closed forms on several rational parameter tuples, then checks the repeated-root and spectral-radius inequalities numerically on representative instances.

Limits: the script is not an exhaustive proof over all positive real parameters. The quantified theorem rests on the symbolic derivation and inequalities above; the executable checks are reproducibility support. No independent audit has been performed.

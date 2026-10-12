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

The proof was checked directly against the published fast-variable threshold system, especially Eq. (3.7), and the pure thresholds in Eqs. (3.8) and (3.12).

The critical elimination uses no numerical fit. The key exact identities are:

\[
c_p\frac{n-1}{n}z+c_t\frac{(n-1)(n-2)}{n^2}z^2=R_0-1,
\]

\[
y=\frac{\tau x}{R_0},
\]

and

\[
R_0n(n-1)(R_0+a)z+(n-1)(1-q)c_tz^2
=n[ R_0(nq-1)+(1-q)].
\]

For \(0<q<1\), setting \(w=1/z\) makes \(c_p\) affine and \(c_t\) quadratic in \(w\), so their elimination is exactly quadratic. For \(q=1\), the coefficient of the quadratic term vanishes and the branch is exactly linear.

The bundled `verify.py` uses exact rational arithmetic for the source's mixed-intervention parameters \(n=5\), \(\tau=7/10\), \(a=1\), and \(q=3/5\). It verifies the source endpoint formulas, the identity \(C_t=LC_p+QC_p^2\), and the exact midpoint gap. This finite computation supports the algebraic derivation but is not used as a proof for all parameters.

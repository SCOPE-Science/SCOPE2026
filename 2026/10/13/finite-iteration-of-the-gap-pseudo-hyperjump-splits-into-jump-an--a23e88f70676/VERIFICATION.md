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

Let
\[
H=\operatorname{HJ}_{e_*}.
\]

The primary source proves for every real \(Y\):
\[
Y<_TH(Y),
\]
\[
\omega_1^Y=\omega_1^{\mathrm{CK}}
\Longrightarrow
H(Y)\equiv_TY',
\]
and
\[
\omega_1^Y>\omega_1^{\mathrm{CK}}
\Longrightarrow
H(Y)\equiv_T\mathcal O^Y.
\]

For the low side, the necessary invariant is
\[
\omega_1^{Y'}=\omega_1^Y.
\]
The inequality
\[
\omega_1^Y\leq\omega_1^{Y'}
\]
follows from \(Y\leq_TY'\). Conversely, \(Y'\) is hyperarithmetic in \(Y\), so every \(Y'\)-recursive well-ordering has order type below \(\omega_1^Y\).

For the high side, the source's hyperjump computes its oracle:
\[
Y\leq_T\mathcal O^Y.
\]
Thus
\[
\omega_1^{\mathcal O^Y}\geq\omega_1^Y,
\]
so a high-side input remains on the high side.

The source also records
\[
U\leq_{\mathrm{HYP}}V
\Longrightarrow
\mathcal O^U\leq_T\mathcal O^V.
\]
Therefore Turing-equivalent oracles have Turing-equivalent hyperjumps.

These facts support induction at every finite stage and yield the exact jump and hyperjump towers stated in the finding.

The source theorem itself supplies strict degree growth at every stage after substituting
\[
Y=H^n(X).
\]

## Limits

The verification stops at finite iteration.

No limit-stage operator or transfinite recursion is defined or claimed.

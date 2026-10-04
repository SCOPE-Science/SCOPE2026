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

The proof was replayed from the displayed operators, not from a computation log. For \(N\ge1\), telescoping gives exactly
\[
\sum_{j=1}^{N}\Gamma_j^*\Lambda_j=I_H+S^N.
\]
For each \(f\in\ell^2(\mathbb N_0)\), the estimate
\[
|\langle S^Nf,f\rangle|
\le
\|f\|_2\left(\sum_{m\ge N}|f_m|^2\right)^{1/2}
\]
proves the scalar convergence required by the printed definition and yields the exact Parseval value \(\|f\|_2^2\). For nonzero \(f\), norm convergence of \(f+S^Nf\) would contradict the exact isometry identity \(\|S^Nf\|_2=\|f\|_2\).

For the repaired Bessel regime, both analysis and synthesis operators are bounded. Coordinate truncation in \(\bigoplus_jV_j\) therefore proves unconditional norm convergence of the mixed series. The lower quadratic estimate gives \(S_{\Lambda,\Gamma}\ge C I_H\), which yields invertibility and \(\|S_{\Lambda,\Gamma}^{-1}\|\le C^{-1}\).

The primary source was checked at the definition, operator theorem, convergence proof step, and reconstruction theorem. A later full-text characterization paper and the closest earlier biframe analogue were inspected for stronger coverage or an existing correction. No checked source contained the same counterexample or repaired statement.

Limits: the simultaneous g-Bessel hypothesis is sufficient, not asserted necessary. No independent audit has been performed.

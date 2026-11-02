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

# Verification and limitations

The result is proved analytically from exact beta moments, gamma-ratio inversion, and uniform complex Riemann sums. The explicit normalization, positive-weight parameter domain, boundary evaluation, fixed degree cutoff and three exponent regimes are stated in `RESULT.md`.

The standalone `check.py` uses only Python 3 standard-library functionality. Execute `python3 check.py` in the directory containing the checker. This recomputes the beta moments against independent radial quadrature, the unweighted polynomial kernel, Hermitian symmetry and first-corrected convergence of the three second-order profiles. The accompanying execution passed 210 assertions. The numerical comparisons are finite and cannot establish any limit; the analytical proof provides the infinite-\(N\) argument.

The paper describes no general nonradial weight theorem and makes no claim about varying parameters. On the diagonal, individual subleading coefficients may accidentally vanish in the smooth-dominated regime; this does not invalidate the nonzero two-point coefficient profile. Potential older equivalent literature remains an originality risk. No independent mathematical audit or validation has been performed.

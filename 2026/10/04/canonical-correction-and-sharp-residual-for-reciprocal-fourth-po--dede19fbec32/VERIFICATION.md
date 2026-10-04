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

Run `python verify.py` from the package directory. The script uses only Python's standard library.

It performs exact arithmetic in \(\mathbb Q(\sqrt2)\), reconstructs the first four coefficients
\[
\frac{\binom{m+3}{3}}{1-(17-12\sqrt2)^{m+2}}
\]
of the tail kernel, inverts the formal series, and checks the coefficient identities that force \(c=1/280\). It also checks
\[
\frac{11001\sqrt2}{2665600}
\]
as the limiting residual and
\[
\frac{114672321(4+3\sqrt2)}{6933059000}
\]
as the first correction coefficient.

As an independent finite replay, it evaluates the balancing recurrence and direct reciprocal tails for \(2\le n\le12\), confirming that the observed residual lies above \(1/280\), below the limiting constant, and agrees with the first-order expansion within a conservative \(O((17-12\sqrt2)^{2n})\) bound.

Expected terminal output:

`VERIFY_OK exact_series_coefficients=4 unique_c=1/280 residual_cases=11 n=2..12`

The finite replay is not used as a proof of the infinite asymptotic.

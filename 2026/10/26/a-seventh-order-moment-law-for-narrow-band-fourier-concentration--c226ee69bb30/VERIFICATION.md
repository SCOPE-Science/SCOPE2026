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

# Verification record

The exact operator is the restriction of bandlimited Fourier projection, whose normalized kernel is \(\operatorname{sinc}(\pi W(x-y))\). Its rank-one limit and unit spectral gap imply a holomorphic leading eigenvalue. Expanding the Schur complement through order \((\pi W)^6\) yields the displayed centered-moment polynomial and a remainder of relative order \((WD)^8\). Every algebraic term in the main proof can be recomputed by expanding powers of \(X-Y\) and using \(\mathbb E X=0\).

The standalone script `check_bandwidth_expansion.py` applies positive-weight 64-point Gauss–Legendre quadrature on each interval, computes the Nyström matrix's largest eigenvalue and compares it against the analytic polynomial at three bandwidths. Observed normalized residuals are of order \((\pi W)^8\). This check does not establish any theorem outside the analytically proved statements and does not replace mathematical verification.

Independent audit has not been performed. All error constants depend on the set's fixed diameter through the stated scaling; no finite-bandwidth global-optimality claim is made.

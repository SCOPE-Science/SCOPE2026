---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Complete renewal to a centered position and independent fair sign kills the contribution to E[X_0 X_t] from paths with a reset before t. The two stationary moments and exponential response give the covariance integral stated in the proof; the asymptotic variance is twice that integral, with no change to extrema under positive rescaling. Independently, on an uninterrupted cycle in units k=v=1, the Laplace transforms at x of E[X_t sigma_t] and E[X_t^2] are A=1/[x(x+g+1)] and M=(S+2A)/(x+2), from their zero-cross-moment and variance-S initial data. Integrating the cycle reward's second moment over time pairs with survival factor exp(-x times the later time) gives H=x(M+A/(x+g))/(x+1), precisely the stated H. python3 /workspace/reproductions/audit_reset.py (SymPy) reproduces this identity, both derivative factorizations, endpoint formulas and the exact rational witness. In Q_g the only potentially negative coefficients are constant/linear/quadratic and their thresholds are strictly ordered in reverse power order; Descartes' rule gives one simple positive zero for g<g_c and none for g≥g_c. Divergence of R as x approaches sqrt(2) forces the unique minimum to be inside the interval. Positive crossings of S-R yield the claimed min/max ordering and the excluded-rate-zero case S=S_0; at the trough S=S_* the derivative touches zero quadratically, so there is no extremum (horizontal inflection). At x=sqrt(2) the derivative of the position-reset term is zero, not strictly negative as the prose says; the active term is strictly negative by positivity of P_g, so H'<0 there and the finding is unchanged. The unreset stationary case has limit H(0)=1/g; the stated numerical critical g and baseline crossing agree.

## originality

PASS

The model and static moments are prior work. The distinct finding is the global stationary time-average variance phase diagram: two positive-rate extrema precisely for g below the quartic threshold and S in the stated open window, with a sign-changing reversal relative to the baseline possible. Neither the same-model static moment results nor the compared dynamic resetting results supply that criterion.

## value

PASS

The sharp condition tells when tuning a reset rate can drive stationary estimation noise down, up and down again. This physically meaningful observable differs from the static position variance; the exact two-parameter window, degenerate boundary and baseline-crossing witness give a usable benchmark and not merely an example of nonmonotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.

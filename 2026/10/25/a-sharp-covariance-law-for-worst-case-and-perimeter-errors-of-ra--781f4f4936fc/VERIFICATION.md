---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For iid uniform unit-circle points the ordered Dirichlet gaps equal iid Exp(1) variables divided by their sum. Convex support yields exactly H=1-cos(pi max gap), while perimeter gives D=2 sum(pi gap-sin(pi gap)), even when a gap exceeds pi radians. Taylor/Dirichlet moment control reduces covariance to pi^5/(6 n^4) Cov(M^2 U^-2,F3). The influence polynomial psi(x)=x^3-18x+12 has exponential mean zero, variance 360; the CLT yields normal perimeter variance 40 pi^6. Conditioning on the maximum at L+z gives truncated independent exponentials and an unchanged centered CLT, proving joint Gumbel-normal independence. Exact conditional E[sum psi(Ei)|M=m] = m^3-18m+12 -(n-1) exp(-m)/(1-exp(-m)) (m^3+3m^2-12m); its leading contribution gives Cov(M^2,sum psi)~2(log n)^4 and covariance constant pi^5/3. The ratio limit follows by Slutsky. Bounded independent quadrature and exact factorial-moment checks corroborate but do not prove the asymptotics.

## originality

PASS

The first nonzero mixed Hausdorff/perimeter covariance of order (log n)^4/n^5 and its sharp pi^5/3 coefficient is not an implication of marginal perimeter CLTs, Hausdorff-rate theorems, or area/semiperimeter extrapolation; those lack an exact maximum-conditioned mixed moment. The independent Gumbel/Gaussian joint statement follows from a separate conditional-truncation argument. Best-of-knowledge PASS with inaccessible same mathematical model literature explicitly retained as risk.

## value

PASS

The maximum gap governs worst-case boundary approximation while all gaps govern perimeter. A sharp positive covariance invisible after the separate Gumbel and Gaussian fluctuation normalizations quantifies coupling between a natural local extreme and global geometric estimation error. The exact coefficient is an independently useful benchmark in random convex approximation, not a marginal CLT repeated.

The dated certificate retains the supplied scientific assessment, sources and limitations.

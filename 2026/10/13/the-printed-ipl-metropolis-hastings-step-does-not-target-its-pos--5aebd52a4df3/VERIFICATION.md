---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Eq. (3.5) fixes a nonconstant conditional posterior pi(nu|gamma,eta,xi). Eq. (3.10) instead shows pi*_nu(nu*,var(nuhat))/pi*_nu(nu_old,var(nuhat)). Read literally, its arguments are undefined as a posterior; read as a normal-proposal density, the posterior ratio disappears. For a symmetric normal random walk Hastings terms cancel and valid alpha=min(1,pi(new)/pi(old)). A symmetric displacement-only acceptor and symmetric proposal cannot satisfy detailed balance for this nonconstant target. Independent log-density evaluation on the stated five-point dataset gives ratio 3.844679306266 vs displacement factor .324652467358 at variance .04. Only the printed rule, not unavailable implementation, is assessed.

## originality

PASS

Hastings 1970 already proves the general acceptance formula; novelty is the source-specific contradiction between Eqs. (3.5) and (3.10). The actual 2025 article full text was compared at conditional posteriors, the normal proposal discussion, Algorithm 1 and its Bayesian-estimate dependence. Targeted DOI and name searches and Resultary semantic query did not disclose an IPL-specific published correction. This is a best-of-knowledge finding, not an independent invention of MH.

## value

PASS

The algorithm underlies published Bayesian stress-strength point estimates and credible intervals. A printed transition rule that cannot be unambiguously executed as posterior-preserving changes reproducibility and interpretability; specifying exact MH correction and support handling is materially useful, despite elementary MH algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.

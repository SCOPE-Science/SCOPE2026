---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The strictly stable Lévy density gives first-exit small-time marked hazard kappa_i±; exact self-similarity yields E_i[exp(-u tau_L) 1_{exit±}]=kappa_i±/(u L^alpha)+o(L^-alpha) with fixed u>0. Conditioning on reset versus exit yields F±=a±+diag(b)KF±. For s=theta L^-alpha, a_i±=L^-alpha*kappa_i±/r+o, b_i=1-L^-alpha*(theta+kappa_i)/r+o; any subsequence converges to a constant right eigenvector of irreducible K (periodic allowed), and left multiplication by stationary pi gives (theta+kbar)F±=kbar±. Uniform small exponential moments from the negative s expansion prove all polynomial moment convergence. Independently checked finite killed generator for nonreversible reset chain; it is not a simulation of infinite-activity stable paths.

## originality

PASS

Best-of-knowledge priority for the precise new statement, not for its acknowledged classical proof components; actual prior mathematical implications evaluated and inaccessible plausible antecedents retained as risks.

## value

PASS

A genuine correlated resetting question is solved at the rare large-jump boundary: the full exit-time and marked-side law, all moments and an explicit stationary arithmetic hazard averaging rule hold even for periodic/nonreversible reset chains, extending beyond a single-reset-site mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.

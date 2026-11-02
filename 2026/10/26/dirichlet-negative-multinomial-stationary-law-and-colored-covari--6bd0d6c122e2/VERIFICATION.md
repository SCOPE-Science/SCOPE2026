---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed the common-scalar hidden update theta_i,a <- (1-u)theta_i,a+u theta_j,a and invariant affine family theta_i,a=rho_R,a+Delta_a W_i. The scalar hidden chain preserves Dirichlet(t,...,t) spacings via conditional Beta(t,t) detailed balance. Conditional negative-multinomial factorial moments equal the hidden process dual moments; absorption, exponential-moment determinacy and Foster drift give existence/uniqueness. Total covariance yields Cov(n_i^a,n_j^b)=t² Delta_a Delta_b G_ij for i!=j; at i=j it equals t delta_ab mu_i,a+t mu_i,a mu_i,b+t(t+1)Delta_a Delta_b G_ii, with G_ij=min(i,j)(L-max(i,j))/[L²(Lt+1)]. Strict local cross-color positivity follows from (t+1)G_ii<w(1-w); separated-site sign is sign(Delta_a Delta_b). Independent rational identity tests across 8 chain lengths and exact two-color sample confirm, not replace, the unrestricted duality proof.

## originality

PASS

Casini–Frassek–Giardinà (2026) studies exactly this multi-species process and establishes its dualities/hidden-parameter generator and equilibrium law. Giardinà–Redig–van Tol (2025) and Carinci et al. (2025) provide the scalar ordered-Dirichlet hidden stationary law. Their conjunction substantially suggests the current mixture, but the inspected primary sources do not state the full vector occupation mixture and exact color covariance rank-one reversal. This is a narrow, valuable synthesis, not a new general intertwining method; potential implicit corollary risk is serious.

## value

PASS

The explicit unique all-color nonequilibrium stationary distribution, finite-N covariance tensor, and strict contrast of same-site positive and separated-site negative cross-color correlations resolve a natural observable left open by the published multispecies model, with direct utility for stochastic transport and cross-species fluctuation calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.

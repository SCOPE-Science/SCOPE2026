---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed Gaussian least-squares projection: S=sum X_i²~chi-square(k), Z~N(0,1), V=R/sigma²~chi-square(k−1) independent; F=[S(u−theta_hat)²+R]/(2k), G=S(u−theta_hat)/k. Substitution gives T0=x−gamma(x−theta)/2+gamma*sigma[Z+V/(Z−d sqrt S)]/(2sqrt S). Conditional normal small-window probability about the pole, dominated by E(V S^−1/2), proves t P(|T0|>t)→C with C=gamma*sigma*Gamma((k+1)/2)/(sqrt(pi)*Gamma(k/2))*(1+d²)^(-(k−1)/2) for k≥2. Student residue decays faster (order t^−k); tail integration proves moment iff q<1. For gradient-squared ridge, the local |u|/(u²+a²) integral yields exactly C/2 times log(1/eps), with chi-square integrable dominating function even k=2. Exact-batch-target cancellation makes affine AR1 with scaled t_k innovations: unique stationary q-moment iff q<k, variance gamma*sigma²/((4−gamma)*(k−2)) for k>2; k=1 gives stationary centered Cauchy scale sigma. All denominators are almost surely nonzero for deterministic x. No inference about the unregularized iterated chain's stationarity or capped SPS.

## originality

PASS

Qualified PASS for the quantitative uncapped Gaussian Polyak one-step reciprocal-gradient Cauchy coefficient, exact gradient-ridge logarithmic coefficient, and paired batch-calibrated stationary moment classification. Established SPS and classical Gaussian ratio identities are excluded. The directly relevant NeurIPS 2022 original was read in full; its lower-bound procedure is explicitly capped and addresses convergence rather than this unbounded distribution.

## value

PASS

PASS: an admissible but loose zero lower bound makes an uncapped stochastic step have infinite first absolute moment despite a strongly convex realized quadratic, and the exact positive coefficient identifies batch-size and starting-displacement sensitivity. Quantifying gradient-ridge cost and contrasting true-minimum calibration supplies an actionable mathematical boundary, not merely a textbook Cauchy-ratio restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.

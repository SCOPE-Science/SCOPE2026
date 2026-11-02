---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed RESULT.md from the frozen seven-blob tree. For j≥3, the least likely living label has p≤1/j, so its next-round extinction probability is at least (1-1/j)^n≥(2/3)^n; holding-time summation gives E tau2≤n(3/2)^n, while the direct unanimity skip is ≤n²(3/2)^n(n^(c/sqrt n)/3)^n=o(1). On the two-label face p(a)=logistic((c/sqrt n)log(a/(n-a))), r_n=2^(1-n), and h(a)/r_n=cosh(n theta/2)/cosh(theta/2)^n; hence r_n≤h≤epsilon_n=r_n exp(c sqrt(n)log(n)/2), with epsilon_n²=o(r_n). The resurrected P=Q+h nu is stochastic, strictly positive and invariant under pi; Hoeffding forces every row into G={|a-n/2|≤n^(2/3)}, and Pinsker/KL gives P²(a,.) within O(n^(-1/3)) of fair conditioned binomial nu, uniformly in a. Dobrushin contraction gives stationary good-set mass 1-e^{-Omega(n^(1/3))}. For M=h/r_n, stationarity yields exactly (lambda_n/r_n)(1-r_n beta_n)=sum pi(a)g_n(a), where g=Q M and beta=nu M; central binomial CLT and exponential moments show g→E cosh(2cZ)=e^(c²/2), Z~N(0,1/4), uniformly on G. Polynomial g(a) off G times exponentially small pi(G^c) is negligible, implying lambda_n/r_n→e^(c²/2). Conditioning on survival perturbs P by at most epsilon_n per step; after O(n/log n) burn-in the hazard is lambda_n(1+o(1)), yielding Exp(1) survival and asymptotic mean (dominated by geometric rate r_n). The entrance time is o(1/r_n). Independently implemented 633 bounded floating-point comparisons corroborated the algebraic cosh hazard and stationary identity, stochastic P rows, and neutral c=0 case through n=320; reconstructed Git tree SHA-1 exactly. Finite checks corroborate, not prove, the all-n limit.

## originality

PASS

Qualified best-of-knowledge PASS for the specific sharp alpha_n=c/sqrt(n) limit and explicit e^{-c^2/2} prefactor in the repeated multinomial conclave process. The motivating Benjamini–Cai–Chen–Gong–Li paper defines the exact power-weighted update and its public primary abstract gives a subcritical exponential LOWER bound for fixed alpha<1, not a matching sharp n-dependent rate, limit law or c-dependent coefficient. The primary full text of its August-2026 v2 could not be retrieved in this execution: arXiv PDF/HTML and lawful mirrors failed, and authorized Oxford reported vpn_disconnected. This leaves a serious specific priority risk but no established mathematical implication of coverage from material obtained. Three related published mathematical sources were read in full and concern respectively reducible continuous-time epidemic QSD, sliding-window Rayleigh quotients, and static one-shot occupancy covariance, not the repeated reinforced binary absorption law. Generic rare-killing and Gaussian methods alone do not determine the explicit coefficient; the result does not claim those methods as new.

## value

PASS

The square-root exponent window is a natural, explicitly motivated small-reinforcement regime: central two-label tallies differ by O(sqrt n), so the logistic log-odds are O(1/n) and n-fold unanimous-killing probabilities retain a nontrivial Gaussian cosh factor. The result determines the sharp exponentially large consensus clock, its entire limiting Exp(1) law, the expectation, and the overwhelming two-label bottleneck, refining a fixed-subcritical exponential lower bound. The coefficient e^(-c²/2) varies genuinely with c and is not a change of notation or an arbitrary finite special case. This is an independently useful natural metastable asymptotic, without claiming a novel general probability method.

The dated certificate retains the supplied scientific assessment, sources and limitations.

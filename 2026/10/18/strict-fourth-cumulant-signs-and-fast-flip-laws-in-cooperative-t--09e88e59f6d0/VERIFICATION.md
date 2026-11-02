---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Reconstructed the stated finite n,m, Metzler Hurwitz A, nonnegative b_l,c, positive a_l, independent symmetric rate-gamma two-state forcing, independent Gaussian thermal noise and reachability assumptions. Stable convolution exists; e^{At}>=0 follows by shifting Metzler A and exponentiating; each h_l(t)=c^T e^{At}b_l is exponentially decaying nonnegative and positive on an interval if reached. For sorted input times t1<t2<t3<t4, Markov conditioning yields E sigma1sigma2sigma3sigma4=e^{-2 gamma[(t2-t1)+(t4-t3)]}; subtracting three pairing contractions yields cum4=-2e^{-2 gamma[(t3-t1)+(t4-t2)]}. Fubini and 24 ordered time chambers give the source exact -48 fourfold response integral with exp[-2 gamma(u+2v+w)], independent sources summing in a_l^4 and independent Gaussian contribution vanishing. Positive integrand is strictly positive on a nonzero-volume region. All gamma derivatives follow by positive Laplace transform and dominated differentiation, strict even for j>0. At gamma->0 the four-fold ordered integration equals 1/24 of the fourth power of the response integral, so -48/24=-2. At infinity scaling three gaps U,V,W by 1/gamma gives gap integral 1/16 and coefficient -48/16=-3 times integral h^4; the variance covariance kernel gives gamma Var->sum a_l^2 integral h_l^2 and the normalized -3/gamma law only when Gaussian thermal variance vanishes. Matching stationary OU with decay 2gamma and variance 1 proves equality of all two-time covariance matrices, not of fourth moments. An independently written symbolic 16-mode exponential convolution rederived the exact two-site variance and K4 rational functions, gamma=1 values, -1/320 fast coefficient, -2/81 frozen limit, and positive 10825/918528 signed-probe counterexample. Tests corroborate examples; general theorem is the analytic proof, not numerical extrapolation.

## originality

PASS

Qualified best-of-knowledge PASS on the combined, restricted result, not on the telegraph fourth-cumulant kernel, covariance equivalence or single-pole negative kurtosis in isolation. Materially inspected primary works cover matching RTP/OU two-time covariance (arXiv:2210.09035), first-order filtered telegraph moments (arXiv:1804.03956) and the two-state four-time connected cumulant (arXiv:2505.03877), but no inspected theorem covers strict negative cumulant on every nonnegative readout of every finite stable Metzler network together with strict complete monotonicity of its magnitude in gamma and the -3 integral h^4 fast-switching law. An inaccessible but plausible Pawula 1987 moment formula creates explicit implicit-priority risk, and a general cumulant-filter theorem may subsume the proof. An unsuccessful search alone does not establish novelty.

## value

PASS

The natural physically motivated question is whether stationary displacement statistics of a cooperative overdamped harmonic network can distinguish symmetric bounded active telegraph noise from Gaussian colored forcing despite exactly identical full two-time position covariance. The all-site, all finite stable Metzler network sign obstruction, strict rate ordering, quantitative sharp gamma^-3 coefficient and gamma^-1 standardized decay are structural, testable statements about a natural positivity cone, rather than an isolated parameter substitution. The signed-probe positive counterexample identifies why the cone hypothesis is necessary. The result does not claim original Gaussian covariance matching, original one-pole telegraph kurtosis, or a thermodynamic-limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

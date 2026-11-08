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

For v,alpha,r,gamma,x0>0 and whole-state resets at x0 with fixed orientation sigma, the first-hitting transforms solve the two-velocity backward ODE: h_-(z)=exp[-tau sqrt(z(z+2alpha))], h_+(z)=alpha h_-(z)/(z+alpha+sqrt(z(z+2alpha))). Renewal at exponential rate r gives bulk return Laplace transform Phi_sigma(s)=(s+r)h_sigma(s+r)/(s+r h_sigma(s+r)). The survival-tail transform (1-h(z))/z is strictly decreasing and diverges as z tends to 0, providing unique z in (0,r) with z=r(1-h(z)), q=r-z, and simple positive pole residue R=z h(z)/(1+r h'(z)). The key renewal theorem under exponential tilt gives bulk tail ~R/q e^{-qt}. Alternating independent bulk duration H and Exp(gamma) bound duration B has tilted-cycle kernel Phi(lambda)*gamma/(gamma+lambda-k); the unique real root k=lambda+gamma(1-Phi(lambda)) generates everywhere-finite smooth SCGF psi(k). Gärtner–Ellis and exponential tightness on [0,1] establish good LDP with Legendre rate. Its derivative u=1/(1-gamma Phi'(lambda)) parametrizes all interior, with I(0)=q, I(1)=gamma, left edge q-2 sqrt(gamma R u)+O(u). Large lambda gives Phi~C_sigma lambda^{-m_sigma} exp(-tau lambda), m_-=0 for shortest-path no-tumble atom and m_+=1 for immediate-tumble density; inversion yields I(1-delta)=gamma-(delta/tau)log(1/delta)+(m_sigma delta/tau)log log(1/delta)+O(delta). The orientation-dependent subleading coefficient is specifically proven and does not follow from a numerical rate plot.

## originality

PASS

Best-of-knowledge originality of the precise final claim, not a certification of historical priority: inspected stronger-formulation searches and primary sources do not establish prior coverage of the extra mathematical assertion. Claim-specific comparisons, actual material read and residual risks follow.

## value

PASS

The adsorbed fraction is a physically natural observable distinct from whole-line positive-halfspace occupation. Its exact all-parameter large deviation rate extends the same-model stationary mean into rare-event theory; singular edge expansions quantify the mechanism of almost-zero or almost-full adsorption. The different log-log coefficient distinguishes whether the shortest return carries an atom versus a density, a structural interpretation useful for related renewal and sticky-boundary processes.

The dated certificate retains the supplied scientific assessment, sources and limitations.

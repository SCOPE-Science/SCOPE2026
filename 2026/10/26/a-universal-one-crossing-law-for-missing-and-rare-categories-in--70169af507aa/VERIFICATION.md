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

For m>=3, a=alpha_i>0, b=alpha_j>0, c=T-a-b>0, n>=r>=1, direct Dirichlet-multinomial integration gives P(X_i=0)=(T-a)_n/(T)_n, P(X_j=r)=C(n,r)(b)_r(T-b)_(n-r)/(T)_n, and P(X_i=0,X_j=r)=C(n,r)(b)_r(c)_(n-r)/(T)_n. The claimed Q_n follows and the adjacent denominator minus numerator equals a(b+r)>0. Q_r=(T)_r/(T-a)_r>1, and strict convexity of log Gamma shows its gamma-ratio limit is below one. Digamma differentiation, using strict decrease of trigamma, makes the continuous interpolation strictly decreasing and yields the unique real crossing. For fixed r,alpha, the telescoping first- and second-order expansion at n=rm+u has logarithm -(alpha*u+r(alpha+1)/2)/((alpha+r)m^2)+O(m^-3), yielding rho=rm-r(alpha+1)/(2alpha)+O(m^-1); alpha=1 telescopes exactly to rho=r(m-1). Independently enumerated weak compositions with exact rational Dirichlet-multinomial probabilities over 63 nonidentical (alpha,n,r) combinations, matching the joint/marginal formulas and signs. Experiments corroborate but do not establish infinite quantifiers.

## originality

PASS

The Dirichlet-multinomial marginal and joint mass formulas are elementary prior art, and one-switch results for aggregate occupancy measures are known. The actual claim is the strictly decreasing normalized covariance ratio for a fixed distinct labelled missing/rare category pair across varying n under an arbitrarily asymmetric one-shot Dirichlet mixture, with a unique real crossing and explicit symmetric-reinforcement shift. No inspected published theorem entails all these results; this is a qualified best-of-knowledge PASS, not a statement of absolute novelty.

## value

PASS

The vacancy-versus-exactly-r cell covariance is a natural occupancy statistic for overdispersed finite categorical sampling. Determining its sign over every n, its unique transition and its reinforcement-dependent order-one shift gives an exact dependence invariant useful for sensitivity analyses and statistical sampling design; it is neither merely restating the mass formula nor an arbitrary finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.

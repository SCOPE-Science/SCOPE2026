---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The argument was checked symbolically from the metric-measure definitions and the cited sufficient theorem.

The reverse-doubling step uses the focal uniform-perfectness lemma to place a ball of radius \(\eta r/20\) inside \(B(x,r)\) and at distance at least four of those radii from \(x\). The inner ball is disjoint from \(B(x,3\eta r/20)\). With \(m=\lceil\log_2(40/\eta)\rceil\), doubling compares its mass from below to \(C_\mu^{-m}\mu(B(x,r))\). Iteration gives the power exponent
\[
\kappa=\frac{\log(1/(1-C_\mu^{-m}))}{\log(20/(3\eta))}.
\]

For the cutoff \(u(y)=(r-d(x,y))_+\), every ball of radius \(s\le r\) meeting the support has measure at most a constant times \(M(s/r)^\kappa\), where \(M=\mu(B(x,r))\). Its oscillation is at most \(2s\), so the normalized Campanato contribution is bounded by a constant times
\[
M r^{-\kappa}s^{p+\kappa-\lambda}.
\]
The condition \(\lambda<p+\kappa\) makes this largest at the outer scale \(s=r\). Larger balls are controlled directly by the support mass. Uniform perfectness supplies a zero of the cutoff at distance less than \(r/\eta\), yielding a Hölder quotient at least \(\eta^\alpha r^{1-\alpha}\). After applying the assumed embedding, the power identity
\[
(1-\alpha)-(1-\lambda/p)=Q/p
\]
forces \(\mu(B(x,r))\gtrsim r^Q\).

The proof does not establish the remaining range \(p+\kappa\le\lambda<Q+p\) when \(\kappa<Q\), and it does not assert optimality of \(\kappa\). No independent audit has been performed.

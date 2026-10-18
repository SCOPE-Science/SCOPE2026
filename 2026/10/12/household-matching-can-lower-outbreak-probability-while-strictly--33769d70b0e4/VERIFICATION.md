---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

With type frequencies 1/2, household fractions ((1-b)/2,b,(1-b)/2), and equal susceptibility weights, every contacted descendant household has the same pair-composition law as an ancestor. A type-i infective with partner j contributes Poisson mean beta_i or beta_i+beta_j according to Bernoulli p_ij local infection. This yields F_b=(1-b)F0+bF1 with F0=1/40u+19/40u^2+99/200u^5+1/200u^10 and F1=3/10u+99/200u^5+41/200u^6, u=e^(s-1). Means are 7/2 and 801/200, hence R*(b)=7/2+101b/200. On 0<=s<=1/5, u<=e^(-4/5)<1/2; rational upper bounds put F0,F1 below 1/5 at the endpoint, while F_b(0)>0, hence q_b is in (0,1/5). F1-F0=u(55-95u+41u^5-u^9)/200>0 throughout that strip (bracket >=3839/512), so the unique subunit fixed point q_b strictly increases with b and Pi=1-q_b strictly decreases. Strict compact uniform margins give perturbation stability for biological parameters. Independent rational coefficient/mean check and b=0,1/2,1 numerical roots confirmed without supplying an infinite proof.

## originality

PASS

The highly relevant 2026 OA household epidemic paper already develops the full branching and takeoff model and warns qualitatively against reproduction-number ranking; no assessed source determines this particular all-b fixed-type-marginal strict reversal with the exact positive finite transmission rates. The Resultary R_I-vs-R_* frontier uses a different comparison. Earlier network-clustering Figure 7 remains a genuine unexamined overlap risk, not grounds to falsify this original quantified claim.

## value

PASS

An exact sign reversal along an entire natural fixed-composition household-matching continuum is a substantive and interpretable counterexample to using R* rankings for outbreak probability. The strict parameter robustness makes it more than an accidental numerical pair or arbitrary tiny finite improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.

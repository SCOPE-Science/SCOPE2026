---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For fixed α,ρ∈(0,1), δ>0, conditional on common W=w the e-values are iid lognormal and q_w(t)=P(E≥1/(αt)|W=w). e-BH rejects iff some sorted E_[k]≥K/(αk); for k/K bounded away from zero the empirical tails converge uniformly, and for small k the conditional lognormal tail decays super-polynomially, permitting a binomial/Chernoff geometric control. Thus except at the boundary the rejection event converges to 1{sup_t q_w(t)/t>1}; null FDR equals P(R>0). Equality q_w(t)=t with t=Φbar(x) gives w=g(x)=[log(1/(αΦbar(x)))+δ²/2−s x]/(δ√ρ), s=δ√(1−ρ). The strictly increasing Gaussian hazard h=φ/Φbar has unique h(x*)=s, minimizing g and giving t*=Φbar(x*), w*=g(x*), asymptotic FDR Φbar(w*) by dominated convergence (W continuous). I independently numerically solved h=s: x*=1.71265196548, t*=0.04338829351108, w*=3.29993272728449, FDR=0.000483540037138 at α=.05,δ=3,ρ=.5. The scalar numeric script cannot itself establish the asymptotic small-k step.

## originality

PASS

Existing e-BH work defines the likelihood-ratio e-values and arbitrary-dependence FDR control; existing Gaussian common-factor asymptotic results concern ordinary BH p-values. Their threshold equations differ. The candidate derives a specifically lognormal e-BH closed hazard boundary and α-independent tangency fraction rather than substituting a parameter in the p-value theorem.

## value

PASS

A closed-form exact global-null error limit for a canonical dependence model of e-BH answers a substantive question left by general upper bounds, identifies rare common-factor false-rejection bursts and a nonobvious α-independent critical rejection fraction. The scalar hazard optimization is accessible but the stochastic conditional crossing and precise limiting quantity are motivated and useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.

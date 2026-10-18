---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Relabel p<=q=1-p and set d=log(q/p); the centered law is -pd (probability q) and qd (probability p). All stop-loss a ranges were checked exactly against E(Exp(1)-1-a)_+: a<=-1 gives equality, -1<a<-pd follows log b<=b-1, a>=qd is trivial. In the interior R(a)=p(qd-a)exp(1+a) has its maximum p^p q^q<=1 when d>=1, or pd exp(1-pd)<=1 when d<1. Equal means plus all stop-loss bounds proves convex order. Independent numerical endpoint/critical-threshold checks were consistent; the analytic inequalities, not samples, prove all p and a.

## originality

PASS

The full stop-loss domination for every convex test is stronger than the already-published centered-gamma MGF and tail bounds. Materially examined the primary information-concentration paper including its Section 2.4 and Appendix A; its auxiliary convex-order principles are not a theorem of centered Bernoulli surprisal dominated by a shifted exponential. Resultary searches returned unrelated Bernoulli convex-order and surprisal findings, not a decisive covering source. Best-of-knowledge PASS, not a priority guarantee.

## value

PASS

The full convex-order comparison is a natural strong stochastic-order bound for an information statistic; it controls every convex risk/test simultaneously and is strictly more informative than the already-known one-sided gamma MGF. The exact centered one-sample binary base case is mathematically motivated by alphabet reduction in empirical-divergence concentration, rather than an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

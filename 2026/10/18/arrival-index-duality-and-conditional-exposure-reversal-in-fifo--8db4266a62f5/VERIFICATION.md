---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For FIFO departures D_i nondecreasing and arrivals A_i strictly increasing, B_i(ell)>=k iff D_(i-k)>A_i+ell; F_(i-k)(ell)>=k iff the same strict inequality. Shifting indexes in an arrival-stationary array yields equal entire nonnegative-integer count distributions, equal independent Bernoulli-mark infection risks, and at most k empirical exceedance difference per fixed window. Under iid renewal inputs the tagged sojourn T and older overlaps/labels depend on past plus tagged service whereas later contacts use future increments and labels, giving conditional independence given T for a fixed ell. In unit-service M/D/1, when W=T-1=m+r with 0<r<1 predecessor departure offsets r,r+1,...,r+m give b_ell(t)=m+1_{r>ell}; future marked arrivals to time T-ell are Poisson(lambda*p*(T-ell)). Near t=1 the preceding risk vanishes; for t>(2a-lambda*p*ell)/(a-lambda*p) with a=-log(1-p)>lambda*p, the earlier risk dominates. The workload LST E exp(-sW)=(1-lambda)*s/(s-lambda+lambda*exp(-s)) gives the exact common marginal formula, with the mass at W=0 handled. An independent bounded parameter check verified opposite signs in both regimes for three (lambda,p,ell) sets; no simulation was treated as universal proof.

## originality

PASS

Newman–Pender arXiv:2610.09019 (2026), Conjecture 3.10, explicitly conjectures unconditional equality and conditional iid infection risks in FCFS G/G/1. The rank-shift marginal symmetry has a simple known FIFO overlap underpinning and alone is not claimed novel. The substantive new assertion differentiates true conditional independence from false conditional identical law using exact positive-probability M/D/1 reversal, while deriving the exact marked directional risk. The primary G/G/1 overlap work studies maximum overlap rather than those conditional marked infection laws.

## value

PASS

The question is motivated by explicit Newman–Pender Conjecture 3.10 on infection direction in FIFO queues. Showing unconditional equality holds pathwise/stationarily while conditional independence does not imply identical conditional distribution is a substantive mathematical distinction, with a positive-measure reversal in a standard deterministic-service queue. Exact marked infection formulas and their regimes can be reused in queueing epidemiology; the claim is not merely routine derivation of an old workload LST.

The dated certificate retains the supplied scientific assessment, sources and limitations.

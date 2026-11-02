---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

In a fair independently oriented tournament, condition on the root vertex outneighbors O and inneighbors I with D=d; each of d(N-d) crossing edges independently makes one cyclic triangle, yielding T|D=d ~ Bin(d(N-d),1/2). Since D~Bin(N,1/2), posterior B=min(D,N-D) has weights h_b C(N,b)C(q_b,t)2^(-q_b) with q_b=b(N-b). Adjacent posteriors tilt by (q_b-t)/(t+1), monotone increasing in b, giving likelihood-ratio and stochastic order, with strictness for t<=q_{m-1} and at most one terminal plateau when n even. Reversing every edge gives E[D|T]=N/2; decreasing (N/2-b)^2 gives variance contraction, and centered Bernoulli fourth moments give Cov((D-N/2)^2,T)=-N(N-1)/16. Independent posterior calculations for n=3..10 passed exact strict/constant cutoffs and variance formula; finite computations corroborate all-n conditional proof.

## originality

PASS

Best-of-knowledge PASS, qualified: rooted cycle-count-conditioned degree posterior and sharp parity variance plateau not implied by materially inspected score geometry or deterministic cyclic-triangle connectivity; inaccessible older random-tournament motif papers remain risks.

## value

PASS

Natural local tournament motif statistic sharpens the full posterior of score balance even though signed score retains zero covariance; exact finite-sample likelihood-ratio order and parity-dependent strictness reveal structural dependence beyond elementary mixed moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.

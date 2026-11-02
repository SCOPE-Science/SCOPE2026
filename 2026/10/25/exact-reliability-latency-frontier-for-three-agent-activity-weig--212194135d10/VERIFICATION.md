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

The activity-weighted node-first/neighbor-second scheme exactly selects the two edges with probabilities p=u/(u+z) and q=z/(u+z), independent of center weight v. Initial selected edge is receptive; averaging it produces (a,a,b) or (a,b,b). If the other gap D≥c the configuration freezes forever; if D<c, both gaps remain receptive because convex averaging cannot increase diameter. Each switch in the iid selected-edge sequence, and only a switch, halves diameter; the switch-indicator strong law gives rate 2pq log2. Success probability is p 1_{D12<c}+q 1_{D23<c}. Conditional switches have alternating geometric waiting times, giving 1+ceil(m/2)/q+floor(m/2)/p. The sharp witness (0,2/5,1), c=3/4, δ=1/10 has success q, mean 1+2/p+1/q, optimum p=√2/(1+√2). Independently checked 64 rational positive weight triples; finite checks do not prove all real initial data.

## originality

PASS

Best-of-knowledge qualified PASS: exact conditional success probability together with time-to-tolerance distribution/mean and optimal activity allocation for minimal P3 is not established by the inspected general and numerical bounded-confidence analyses. Edge-weight cancellation and generic geometric waiting identities are standard and are excluded from novelty.

## value

PASS

The three-vertex path is the smallest model admitting stochastic first-update lockout and successful consensus under the same initial receptivity. Its exact and opposing reliability and latency responses offer a meaningful boundary benchmark for activity design, beyond a trivial edge-probability computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

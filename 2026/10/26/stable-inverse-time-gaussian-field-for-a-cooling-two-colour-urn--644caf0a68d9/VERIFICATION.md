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

Computed one-step conditional mean E[V_k|F_{k-1}]=(1-2p_k)Q_{k-1}, so a_k=prod(1-2p_j/(m+j)) and M_k=Q_k/a_k is a martingale with increments D_k=(V_k-(1-2p_k)Q_{k-1})/[(m+k)a_k]. Since p_n->0, a_n and a_n^-1 are positive slowly varying and a_n^-1=n^{o(1)}, making sum Var(D_k) finite and giving L2 terminal convergence. Block increments sqrt(n) a_n sum_{k~nu} D_k have bracket ->(1-Q_infinity^2)(1/r-1/t), and jumps O(n^-1/2), satisfying the martingale stable FCLT with a Brownian independent of terminal history. Truncating future at nR has L2 remainder <=4n a_n^2 sum_{k>nR}1/((m+k)^2 a_k^2)->4/R by Karamata; send R->infinity to obtain the backward Brownian covariance 1/max(s,t), uniformly for r<=t<=T. Uniform slow variation replaces a_n with a_floor(nt). Convergence at t=0 is correctly excluded. The logarithmic product criterion gives a_infinity>0 iff sum p_k/(m+k)<infinity; divergence makes Q_infinity=0. Independently checked exact conditional expectation/second-moment recurrence across 40 finite urn distributions (four seeds, two nonconstant schedules). Finite checks establish no weak convergence.

## originality

PASS

Best-of-knowledge noncoverage after comparing the precise statements and implications, original scope, related general theorems and aliases, with the specific residual priority limitations below; lack of a search hit is not itself evidence of novelty.

## value

PASS

Gives a complete path-level second-order law around the random terminal martingale drift for arbitrary deterministic reversal probabilities tending to zero, with an inverse-time Brownian covariance and a phase distinction between persistent random composition and erased memory. This is a motivated stochastic limit distinct from first-order convergence and fixed-parameter elephant fluctuation laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.

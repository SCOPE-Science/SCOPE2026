---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The singleton partition has finite welfare, so only compositions of contiguous intervals can maximize. Counting ordered adjacent and nonadjacent pairs gives w_l. Its strictly concave quadratic term gives a strict gain 2q(a-b-1) by balancing lengths a,b at fixed k, proving the complete census including ties between k. A negative endpoint could detach without disconnecting the source, doubling its personal gain in welfare; interior members have strictly larger utility than endpoints. An interior member cannot connect to another coalition, and a feasible boundary join leaves old within-block distances unchanged, so its welfare increment is exactly twice the deviator's utility gain. The decreasing sequence of density differences gives precisely the claimed consecutive ties, with L>=2 because d_2>d_1. Off criticality the residual-block construction bounds the total deficit uniformly, and the positive density gap then bounds the number of exceptional vertices, yielding polynomially many placements. At criticality n=Lh+r with h>=L-1>=r is representable by L and L+1; both lengths alone attain the optimal density. The composition generating function has a simple positive dominant pole and no other pole on its modulus because L,L+1 are coprime. The recurrence with a_0=1 is for those coefficient counts; they coincide with N_n on the stated representable range, not necessarily for every small n. An independent cut-mask replay checked 72 parameter profiles and every unilateral destination for 145 exact optimum partitions, without running uploaded code.

## originality

PASS

The credited claim is the all-parameter census and its score-induced critical change in optimizer counts, with every such optimizer stable on a path. Standard pairwise welfare, concavity, and composition generating functions are tools, not claimed original. Strongest path analogues checked use different payoff normalizations and yield different optimal lengths; the open-score framework does not give the census or density phase transition.

## value

PASS

The result gives more than an optimal welfare algorithm: it determines the full optimizer multiplicity, proves that no maximizer needs to be discarded for Nash instability, and shows that an exact tie in per-vertex welfare creates an exponential optimizer family whereas noncritical parameters allow only polynomial degeneracy. This is a structural distinction relevant to counting and selecting optimal coalitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

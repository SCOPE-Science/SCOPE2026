---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Write m=(a+b)/2 and d=(a−b)/2. Exactly four signed coordinate permutations of v=(a,b) become (αm,βd) independently with α,β∈{±1}. Input cube yields |m|+|d|=max{|a|,|b|}≤1; at each step greedy scalar sign against the current scalar prefix keeps |M_k|,|D_k|≤1 by |S−sign(S)x|≤max{|S|,|x|}. The inverse linear map (M,D)↦(M+D,M−D) sends the four invariant-square vertices to (±2,0),(0,±2). Convexity of every ℓ_q norm, including q=1 and q=∞, gives max≤2 on the entire square and ALL prefixes, with no lookahead. For v1=(1,1),v2=(1,−1), every admissible second prefix is a signed coordinate axis vector of magnitude 2; bound sharp for all q. Universal analytic proof, no numerical extrapolation.

## originality

PASS

The target is the finite-q exact cross-norm prefix constant, not the already-covered q=∞ endpoint. The 2026 lead paper states general bounds for permutation balancing; its Theorem 9 specialization as recorded in the inspected package is 2^(1+1/q) for finite q. Classical planar sign-sequence theorem controls the SAME norm, and sign-only balancing does not allow independent diagonal greedy choices. The recent lead paper full text remained inaccessible, hence comparison is bounded and material-read risk is explicitly retained.

## value

PASS

The lead 2026 paper explicitly introduces signed-permutation prefix balancing; determining exact small-dimensional cross-exponent constants is a natural structural boundary case. The constant 2 is uniform across the full q-range and sharp with a two-vector witness. The sign+swap representation decomposes into two scalar online sign games, explaining a nontrivial improvement by the factor 2^(1/q) over the stated general finite-q estimate. Not an unmotivated handpicked norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For r>=2 vertex-glued cliques, translate hub to zero. The centered squared norm is strictly convex on the anchored feasible product of P_a={z in [-1,1]^a: max(z)-min(z)<=1}; its extreme points have all coordinates in {0,1} or {0,-1}, with at least one nonzero. This gives exactly N K - S^2, K=sum_i k_i and S=sum_i eps_i k_i, with 1<=k_i<=a_i. If S>=0, a partly occupied negative blade improves by filling; a partly occupied positive blade forces S>0 and S>=(N-1)/2. A positive blade with k_j<S improves by sign reversal; two positive blades would force K>=3S>N-1, impossible. Thus any partial maximizer has exactly one positive, dominant blade, all others full negative, and largest A>=3Q+2. If A<=3Q+1 full-sign optimizers minimize partition discrepancy delta. In the dominant regime F(k)=2NQ+N^2/4-(k-Q-N/2)^2, so nearest integers yield 2NQ+floor(N^2/4), equality at boundary A=3Q+2, and exact squared gain floor((A-3Q-1)^2/4). Checked all quantifiers including a_i=1, N=T+1, r=2 and the tie. Independent literal labelled assignments for ten nontrivial size tuples, including (5,1),(6,1),(7,1), matched the numerator; these finite checks do not prove the theorem.

## originality

PASS

The optimized invariant and integral-extremizer principle are already established by Alon, Boppana and Spencer (1998), but their Theorem 2.1 does not supply this exact heterogeneous bouquet formula, dominant-blade transition or equality stratification. Random-graph spread, windmill dissociation and clique partitions are different statements; no inspected comparison implies the formula. Priority remains qualified.

## value

PASS

Graph spread is the sharp uniform-vertex variance of all real 1-Lipschitz graph functions, meaningful in product-space concentration. A complete arbitrary-size bouquet formula, full extremizer classification and strict transition between signed-partition and partially occupied clique configurations answer a natural optimization problem. The exact arithmetic squared improvement is not a routine type check or an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

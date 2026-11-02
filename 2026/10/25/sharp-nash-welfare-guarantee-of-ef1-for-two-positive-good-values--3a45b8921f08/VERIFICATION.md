---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For n≥2, m≥n and identical positive additive item values in {a,2a}, EF1 forces every bundle to be nonempty: an empty bundle with m≥n would face another bundle containing at least two positive items. After rescaling by a, the integer loads x_i have max−min≤2 since each item is at most two. Let B(S,n) be the maximum product among nonnegative integer vectors of the same total S; pairwise smoothing shows its maximizers differ by at most one. When the EF1 loads have both L and L+2, replacing one pair (L,L+2) by (L+1,L+1) multiplies the numerical product by (L+1)²/[L(L+2)]≤4/3. This operation consumes one copy of each extreme and terminates in at most floor(n/2) steps, giving B(S,n)≤(4/3)^floor(n/2)∏x_i. Since any actual allocation's product is ≤B, the desired NSW ratio follows. This balancing is a numerical upper bound, not an asserted implementable item transfer. For q=floor(n/2),r=n−2q, the inventory 2q goods of value a plus q+r goods of value 2a realizes EF1 loads (1^q,3^q,2^r) and an equal-2 optimum, attaining (3/4)^(q/n) for every n. An independent exact-rational enumeration rechecked 755 EF1 count vectors for 2≤n≤4 and n≤m≤7, finding no violation. This is corroboration; the proof handles all n and inventories.

## originality

PASS

Yang, Chen, Kuan, Wu, Lin and Chen (2026) study EF1-constrained NSW under identical additive valuations, prove optimality for uniform goods and derive bounds when the maximum item value is small relative to the mean. Their relevant theorem and appendix were materially read from lawful public full text. The parameter-sensitive small-item guarantee and integer-load spread inequality do not already imply the exact inventory-independent bivalued ratio with equality for each n. Earlier Barman–Krishnamurthy–Vaish treats general fair/efficient allocation and NSW context, but the inspected descriptions do not supply this exact same-class factor. The remaining novelty is a sharp universal worst-case price of selecting any EF1 allocation with values 1,2; classical AM–GM and integer smoothing are tools, not newly claimed lemmas. An older discrete bivalued ratio published under a different welfare-price terminology remains a priority risk.

## value

PASS

The theorem gives the precise efficiency loss of any EF1 outcome relative to unrestricted NSW when homogeneous agents value goods at one of two positive levels. The ratio is sharp for each agent count and does not depend on the number or mix of goods, a natural gap between the uniform-goods optimality theorem and arbitrary-value approximations. The extremal pair construction explains the integer-load obstruction; this is a complete structurally motivated fairness-versus-welfare bound rather than an arbitrary finite instance or merely a routine restatement of AM–GM.

The dated certificate retains the supplied scientific assessment, sources and limitations.

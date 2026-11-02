---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For each primitive 2-cycle x->y->x on the finite connected tree, the vector of total firing counts over two steps is harmonic under the graph Laplacian and hence constant; the only nonfixed case has exactly one firing at every vertex. For a phase vector p the number of opposite-phase neighbors k_v must be positive; the first-state chip interval has exactly k_v choices (firing: d_v through d_v+k_v-1; waiting: d_v-k_v through d_v-1). Conversely those choices ensure y has complementary phase and Phi(y)=x. On a tree, selected opposite-phase edges determine the phase up to complement, while the two complements are the same orbit, giving N(T)=sum_{S subset E} product_v deg_S(v). A leaf with a formal parent edge has (F_0(0),F_0(1))=(0,1). A height-h branch satisfies A_h=2B_{h-1}(A_{h-1}+B_{h-1}) and B_h=(A_{h-1}+B_{h-1})(A_{h-1}+3B_{h-1}), leading to the claimed matrix M=[[0,2],[1,3]] and product formula. Both linear coordinates obey z_{j+2}=3z_{j+1}+2z_j. The asymptotic uses positive dominant root (3+sqrt17)/2, negative subdominant root of smaller modulus, and the exact convergent weighted log-series tail; it gives coefficient kappa=4 exp(s)/(19+5 sqrt17), not merely a growth rate. Boundaries h=1 and h=2 yield N=2 and 30; all chip intervals are nonnegative. Independent new tests exhaustively enumerate all edge subsets for h=1,2,3, evaluate a separate branch recursion through h=4, enumerate every chip state with 0<=x_v<2d_v for h=1,2, and numerically check s and kappa. These finite tests only corroborate the general proof.

## originality

PASS

Qualified best-of-knowledge original contribution is the evaluated one-dimensional full-binary-tree recurrence product and sharp pure-exponential per-vertex limit, not the classical period-one-or-two theorem, the common-two-step firing-count lemma or the generic weighted cut representation. Jiang 2010 studies attainable periods; Jiang–Scully–Zhang 2014 studies firing patterns and tree-like subgraphs; Inagaki–Khovanova–Luo studies sequential stabilization on a different infinite tree. Search of the published mathematical finding corpus and targeted literature found no exact duplicate, but non-detection is not a novelty proof. The most relevant Bitar–Goles 1992 article was not fully accessible; this remains a substantive priority risk. The general cut sum does compute each finite case in principle but does not itself supply this exact closed height product or asymptotic prefactor without the additional branch recurrence and singular-limit analysis.

## value

PASS

Finite full binary trees are a canonical sequence of branching networks for the deterministic parallel chip-firing automaton. Beyond the known tree period restriction and generic finite sum, the exact closed product over heights resolves the full count across all chip masses and a natural exponential growth statistic per graph vertex, with a nontrivial nonzero prefactor. The result separates the branching structure from previously evaluated paths, yields the precise entropy s rather than a mere bound, and is a reproducible structural law for an infinite family rather than an arbitrary small-instance gain. Its natural restrictions (indistinguishable chips, open boundary, finite heights, primitive cycles counted once) are explicit, and no unjustified basin-size or fixed-point census is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Review of the sharp graph-gradient projection gap

## Correctness — PASS

The exact electrical row-sum identity \(S_e=(1+T)/(1+c)\) follows from the Dirichlet potential for a deleted nonbridge edge. The independent total-variation bounds \(T\ge1\) and \(T\ge2c\) yield the sharp \(4/3\) inequality. In the equality case, harmonicity and vanishing voltage gradients away from the two endpoints force a single common neighbor and exclude longer cycles. Orthogonal decomposition by disjoint cycle supports gives the converse and the complete cactus formula. Tree, bridge, orientation and scalar-field cases have been treated. Numerical atlas checks supplement the all-size proof.

## Originality — PASS, with residual risk

The closest literature includes Jiang–Lim–Yao–Ye's canonical Hodge gradient projection (arXiv:0811.1067), Kelner–Maymounkov's routing bounds (arXiv:0909.2859), Schild–Rao–Srivastava's absolute transfer-current analysis (arXiv:1708.01632) and Gurel-Gurevich–Nachmias–Sachdeva's sharper average upper bounds (arXiv:2605.24130). The exact **same matrix** occurs in the electrical-flow comparison, so the equivalence is not overlooked. The inspected prior claims give definitions or different-direction averaged upper bounds, not the present uniform lower-bound gap with equality-graph classification. An unindexed earlier equivalent lemma remains possible.

## Mathematical value — PASS

In edgewise maximum norm, a small cyclic perturbation of a tree is impossible within the category of finite simple unweighted graphs: introducing any cycle incurs at least a one-third increase in the worst-case Euclidean Hodge-projection amplification. The equality graph class is completely characterized rather than listed up to a finite order, and the cactus formula gives exact nontrivial examples with longer cycles.

## Limits

No weighted, multigraph, infinite-graph or arbitrary-projection analogue is claimed. Finite numerical checks do not establish the theorem for all graph sizes. Independent scientific validation has not occurred.

Self-review: passed. Independent audit: not yet performed.

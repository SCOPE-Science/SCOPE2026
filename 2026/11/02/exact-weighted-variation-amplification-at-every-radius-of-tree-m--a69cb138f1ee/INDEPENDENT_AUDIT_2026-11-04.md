# Independent mathematical audit

## correctness

PASS

For any finite tree T with at least two vertices, strictly positive variation weights, and unweighted integer hop radius k, layer-cake decomposes weighted TV into threshold-cut perimeters. Superlevel sets of M_k(f) are N_k[S]. For a dilated outer boundary edge xy with distances k and k+1 from S, a tree-unique closest-S path identifies a first original cut edge a→b and shows xy lies in the outward level-(k−1,k) wave of component C_b. Assigning each boundary edge to one first cut edge yields the sharp upper bound J_w(M_k f) ≤ (max_{a→b}F_k(a→b)/w_ab)J_w(f); the indicator of the opposite full component attains every candidate ratio. k=0 is identity; k≥diam(T) gives zero gain. For k=1, degree≥3 violates nonexpansivity by a minimum incident weight and a path contracts exactly with equal edge weights (including a single-edge path). Degree Δ gives ≤(Δ−1)^k, attained for initial radii by the attached-leaf full (Δ−1)-ary tree. Independent exhaustive cut/wave comparison on randomized weighted trees of sizes 2..9 and several radii agreed; inspected source verify.py at Git blob b7bd542bf70a5f82b0825bc8b79a3891e5ca6283. This proves one-input TV growth only, not two-input Lipschitz continuity.

## originality

PASS

The final claim is compared by statement and implication, not by title. Morphological dilation of graph superlevel sets is an exact equivalent of neighborhood max filters; its definition alone does not give the sharp weighted tree frontier ratio or cut extremizers. Static graph-TV optimization and mean-zero cut quotients concern different variational problems. General graph dilation/erosion definitions and graph-TV convex minimization are broader in graphs, but do not directly subsume this one-input nonlinear edge-weighted all-radius operator seminorm theorem; in particular linear signal variation is differently normalized. This is a formula for every weighted tree and radius, not a single tabulated constant. Resultary found nearby but nonmatching static zonotope, path-molecule and TV-optimization records; absence of a matching listing is not proof of novelty. To obtain the exact claim from the inspected prior graph-morphology definitions one must additionally prove a sharp charging inequality along unique tree paths and construct component-side attainment. A plausible 2013 full paper was inaccessible and might contain that argument implicitly. Accessible primary texts were materially compared; inaccessible plausible primary texts are named as residual risks rather than treated as disproving novelty.

## value

PASS

On tree-structured grayscale morphology, the sharp nonlinear weighted-TV gain would naively be a maximization over exponentially many input cuts. This theorem reduces it to 2(|V|−1) oriented frontiers, specifies all-radius extremizing witnesses, characterizes contraction paths, and quantifies exponential transient branching before eventual flattening. These are motivated geometric/operator facts useful for evaluating nonlinear filter-induced variation, not a rebranding of graph dilation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

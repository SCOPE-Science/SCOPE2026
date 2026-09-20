# Review — sharp maximum reformulated Albertson index of trees

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof reduces the adjacent-edge degree-difference sum to a local inequality for nonnegative neighbor weights. For a vertex v, setting x_u=d(u)-1 on its neighbors gives

sum_{u<w in N(v)} |x_u-x_w| <= (d(v)-1) sum_{u in N(v)} x_u.

After summing over vertices, each tree edge uv contributes twice to the resulting bilinear form, giving

RAlb(T) <= 2 sum_{uv in E(T)} x_u x_v.

For a bipartition (A,B), the edge sum is at most the complete cross-product X_A X_B. Since sum_v x_v=n-2, integer AM-GM gives X_A X_B <= floor((n-2)^2/4). This yields the stated bound.

The equality conditions were checked separately. Local equality forces every vertex to have at most one non-leaf neighbor. The induced subgraph on non-leaves is connected in any tree, hence has at most two vertices. A one-center star has RAlb=0 and cannot be extremal for n>=4, leaving exactly a double star. If its two centers have p and q leaves, RAlb=2pq and p+q=n-2, so equality requires and is attained by |p-q|<=1.

Definition-level enumeration of all non-isomorphic trees through n=17 agrees with the formula and gives one maximizing isomorphism class for each n>=4. This computation supports but does not replace the proof.

Correctness assessment: PASS.

## Originality

The foundational Albertson paper was checked as the older source for degree-difference irregularity and extremal questions. Literature on graph operations and irregularity was searched for line-graph formulations. The directly relevant 2025 paper by Cutinha, D'Souza and Nayak defines the reformulated Albertson index, proves RAlb(G)=Alb(L(G)), obtains sharp lower bounds in fixed-order/fixed-maximum-degree tree and unicyclic classes, and gives general upper bounds in Section 5. Its order/size/degree upper bounds do not state the sharp tree maximum floor((n-2)^2/2) or the balanced-double-star equality characterization.

Searches were run under the terms "reformulated Albertson index", "maximum reformulated Albertson index", "Albertson index line graph tree", "irregularity line graph tree", "double star reformulated Albertson", "balanced double star Albertson", and exact-formula variants. No prior statement matching or implying the theorem was located. Recent papers on ordinary Albertson indices with prescribed tree degree sequences were also checked at the title/abstract/full-text-summary level; their invariant is Alb(T), rather than Alb(L(T)).

The internal SCOPE repository was searched by Albertson/reformulated terminology and equivalent line-graph language; no overlapping record was found. Repository code-search responses were marked incomplete, so this is supporting evidence rather than an exhaustive guarantee.

Residual risk: a result may exist under chemical-graph terminology, as an extremal theorem for line graphs/block graphs, or in poorly indexed literature without the phrase "reformulated Albertson". The relevant primary reformulated-Albertson article was accessible in full HTML/search-rendered text; no inaccessible source produced concrete evidence of prior coverage.

Originality assessment: PASS, to the best of our knowledge.

## Value

The result replaces broad parameter-dependent upper bounds by an exact order-only maximum for trees, including a unique extremal structure. Through RAlb(T)=Alb(L(T)), it simultaneously determines the exact maximum Albertson irregularity over line graphs of n-vertex trees. The proof is short and structural, and the balanced-double-star characterization explains why concentrating all non-leaf structure into two nearly equal adjacent hubs is extremal.

Value assessment: PASS.

## Scientific limitations

- The originality search cannot exclude unindexed or differently named equivalent results.
- The theorem concerns trees; no corresponding exact maximum for unicyclic or general connected graphs is claimed.
- The finite enumeration is corroborative and stops at order 17; the general result rests on the symbolic proof.
- Independent audit has not been performed.

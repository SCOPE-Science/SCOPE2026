# Nash equilibria as nullspace polytopes in weighted conformist–rebel networks

## Finding

Let \(G=(C\sqcup R,E)\) be a finite simple bipartite graph with \(c=|C|\ge1\), \(r=|R|\ge1\), and at least one edge. Each edge \(\{i,j\}\) with \(i\in C\), \(j\in R\) has a positive weight \(w_{ij}\); let \(W\in\mathbb R^{c\times r}\) have entries \(w_{ij}\) on edges and zero otherwise. Every player independently chooses one of two actions \(0,1\). A conformist receives the total weight of neighbors choosing the same action; a rebel receives the total weight of neighbors choosing the opposite action.

For a mixed profile, write \(p_i\in[0,1]\) for the probability of action \(1\) and \(z_i=2p_i-1\). **The complete Nash equilibrium set, including every pure, partially mixed, and completely mixed equilibrium**, is exactly

\[
\boxed{\mathcal N(W)=\bigl\{p\in[0,1]^{c+r}: Wz_R=0,\ W^{\mathsf T}z_C=0\bigr\}.}
\]

Every player is indifferent between their two actions at **every** Nash equilibrium. The equilibrium set is a nonempty, centrally symmetric, convex polytope with affine dimension

\[
\boxed{\dim\mathcal N(W)=c+r-2\operatorname{rank}(W).}
\]

In particular, the completely uniform mixed profile is the **unique Nash equilibrium of any kind** precisely when \(c=r\) and \(W\) is nonsingular. A pure Nash equilibrium exists precisely when both signed nullspace conditions admit sign vectors:

\[
\boxed{\ker W^{\mathsf T}\cap\{-1,1\}^{c}\ne\varnothing\quad\text{and}\quad\ker W\cap\{-1,1\}^{r}\ne\varnothing.}
\]

For a fixed bipartite edge support, put \(\nu(G)\) for its maximum matching cardinality. If all present edge weights are sampled independently from atomless probability distributions on the positive reals, then with probability one

\[
\boxed{\dim\mathcal N(W)=c+r-2\nu(G).}
\]

Thus generic weights give a unique Nash equilibrium **if and only if the bipartite graph has a perfect matching**. Simultaneously, with probability one there is **no pure Nash equilibrium**, even when the graph has a perfect matching. The latter statement concerns independent absolutely continuous or, more generally, independent atomless edge weights; it does not assert an absence of pure equilibria for arbitrary chosen weights.

## Assumptions and scope

The network is finite, the two groups are nonempty, there are no within-group edges, each existing edge weight is strictly positive and shared by the two incident utility functions, and neither player has a fixed preference or outside payoff for either action. Player mixed actions are independent conditional on their declared strategies, as in ordinary finite-game Nash equilibrium. Isolated vertices are allowed; their freely chosen mixed probabilities contribute to the stated affine dimension. At least one cross-group edge is assumed for the almost-sure absence of pure equilibria.

No assumption of connectivity, regularity, equal group sizes, or uniform edge weights is needed. The genericity statement holds for independent weights each having no point masses; one may equivalently work off the common zero sets of finitely many nonzero determinant and balancing polynomials in the edge weights. The result does not address correlated, signed, or action-dependent weights.

## Proof

**Step 1: Edgewise conservation.** Write \(d_i=\sum_j w_{ij}\) for a conformist's weighted degree, and \(d_j=\sum_i w_{ij}\) for a rebel's weighted degree. For every pure action profile, each cross-type edge contributes its weight to exactly one endpoint's payoff: to the conformist when the actions match and to the rebel when they differ. Hence, for every mixed profile,

\[
\sum_{i\in C\cup R}\mathbb E[u_i]=T,\qquad T=\sum_{i\in C,j\in R}w_{ij}.
\]

**Step 2: Best-response surplus.** For a conformist \(i\in C\), the expected payoff if choosing action \(1\) minus that from action \(0\) is \((Wz_R)_i\). The two conditional payoffs sum to \(d_i\), so the greatest unilateral payoff against the other players' mixed actions is

\[
B_i=\tfrac12\bigl(d_i+|(Wz_R)_i|\bigr).
\]

Similarly for a rebel \(j\in R\), the conditional payoff difference is \(-(W^{\mathsf T}z_C)_j\) and the best-response payoff is

\[
B_j=\tfrac12\bigl(d_j+|(W^{\mathsf T}z_C)_j|\bigr).
\]

Adding, noting that the sum of all weighted degrees is \(2T\), gives the **exact regret sum identity**

\[
\boxed{\sum_v\bigl(B_v-\mathbb E[u_v]\bigr)
=\tfrac12\bigl(\|Wz_R\|_1+\|W^{\mathsf T}z_C\|_1\bigr).}
\]

Every summand on the left is nonnegative, whether the corresponding player mixes or plays purely. Therefore all players best-respond simultaneously if and only if both displayed norms vanish. In that event their conditional action payoffs coincide. This proves the entire equilibrium characterization, including both boundary and interior mixed profiles; no unsupported extension from the fully mixed case is used.

**Step 3: Geometry, uniqueness, and pure profiles.** The equilibrium conditions are homogeneous. The origin in \(z\)-coordinates lies in the relative interior of the intersection of their joint nullspace with the cube \([-1,1]^{c+r}\). The two kernel dimensions add to \((c-\operatorname{rank} W)+(r-\operatorname{rank} W)\), proving the dimension formula. The set is a singleton exactly when \(\operatorname{rank}W=c=r\). At a pure strategy \(z\) is coordinatewise \(\pm1\), so intersecting the two kernels with the two sign cubes gives the asserted exact necessary-and-sufficient criterion. The exact number of pure equilibria is the product of the two sign-vector intersection cardinalities.

**Step 4: Matching rank under generic positive weights.** A nonzero minor of order \(k\) requires a permutation of \(k\) distinct present edges, that is, a matching of size \(k\). Consequently \(\operatorname{rank} W\le\nu(G)\) for every admissible weighting. Conversely, choose the rows and columns of any maximum matching. Its square determinant polynomial has a monomial equal to the product of the distinct matching-edge variables with coefficient \(\pm1\); another permutation cannot produce that same monomial, so the polynomial is not identically zero. With independent atomless weights, such a nonzero polynomial vanishes with probability zero, by conditioning successively on each edge variable (or by induction on the number of variables). Thus \(\operatorname{rank}W=\nu(G)\) almost surely and the generic dimension and uniqueness classification follow.

**Step 5: Generic extinction of pure equilibria.** If a pure equilibrium existed, every player would be indifferent by Step 2. Choose any vertex incident with an edge. Its indifference condition is a nontrivial signed linear combination of the independently sampled positive incident edge weights. Conditional on all but one incident edge weight, equality forces at most one value of that atomless weight, an event of probability zero. Hence the probability that *any* pure equilibrium exists is zero. This argument works with isolated vertices elsewhere and does not rely on a union bound over infinitely many profiles.

## Verification

The standalone standard-library-only `verify.py` reconstructs direct unilateral best-response inequalities and the separate kernel criterion for rational independent mixing probabilities \(0\), \(1/2\), and \(1\). It verifies their equivalence over \(1,953\) profiles from nine bipartite weighted game instances. It also checks the edgewise constant-payoff identity, exact matrix ranks, matching upper bounds, all \(256\) positive integer weight matrices on \(K_{2,2}\) with entries from \(1\) to \(4\), and explicit pure-equilibrium counts. It executed to completion and printed `VERIFY_OK`.

For \(K_{2,2}\), equal weights \(W=\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\) yield rank \(1\), an equilibrium square of dimension \(2\), and four pure equilibria. Replacing one weight by \(2\) gives \(W=\begin{psmallmatrix}1&1\\1&2\end{psmallmatrix}\), rank \(2\), and a unique equilibrium in which all four players independently choose both actions with probability \(1/2\). For \(W=\begin{psmallmatrix}1&2&3\\4&5&6\end{psmallmatrix}\) on \(K_{2,3}\), rank \(2\) yields a one-dimensional continuum of equilibria.

These finite rational checks test the identities and examples, not the general infinite family or almost-sure statement. Steps 1–5 constitute the general proof.

## Relationship to prior work

The fashion game of Zhang, Cao, Qin and Yang (2018) already observes the uniform binary mixed equilibrium and studies the existence of pure equilibria and homophily. Cao, Qin, Yang and Zhang (2019) analyze best-response cycles rather than classify all Nash mixed profiles. Pei, Cao and Zhang (2026), arXiv:2607.10997, explicitly restrict analysis to pure strategies; they obtain pure-equilibrium restrictions for conformist–rebel networks and multi-strategy results. Cao, Sánchez and Zhang (2026), arXiv:2607.05932, analyze heterogeneous players and pure-equilibrium/dynamic behavior. The present statement concerns a specifically reciprocal **weighted bipartite** specialization and answers a distinct complete-equilibrium-set question: all boundary/interior mixed profiles, exact polytope dimension, and generic uniqueness dictated by maximum matching.

The linear indifference equations and generic structural-rank/matching correspondence are familiar mathematical ideas and are **not** individually claimed new. The contribution is their complete exact identification within this antagonistic network game's Nash set, including the non-obvious fact that even pure equilibrium requires every player to be indifferent. Prior network-game and matrix-game frameworks may contain broader implicit corollaries; no independent priority certification has been undertaken.

## Limitations

The proof does not apply verbatim if conformists interact with one another, rebels interact with one another, agents have intrinsic action biases, or two endpoints assign different weights to the same edge, since the global edgewise payoff conservation used in Step 1 can fail. Pure equilibrium absence is generic rather than universal. No convergence, best-response dynamics, welfare, correlated equilibrium, or multi-strategy generalization is claimed. The generic results concern independently distributed edge weights on fixed support, not randomness of network topology itself.

## References

1. Shan Pei, Wenjie Cao and Boyu Zhang, *Network games with three types of players* / *Equilibria in heterogeneous multi-strategy network games*, arXiv:2607.10997v1 (first public version July 13, 2026), https://arxiv.org/abs/2607.10997 .
2. Wenjie Cao, Ángel Sánchez and Boyu Zhang, *Network games with heterogeneous players*, arXiv:2607.05932 (2026), https://arxiv.org/abs/2607.05932 .
3. Boyu Zhang, Zhigang Cao, Cheng-Zhong Qin and Xiaoguang Yang, *Fashion and Homophily*, Operations Research 66 (2018), 1486–1497, https://doi.org/10.1287/opre.2018.1744 .
4. Zhigang Cao, Cheng-Zhong Qin, Xiaoguang Yang and Boyu Zhang, *Dynamic matching pennies on networks*, International Journal of Game Theory 48 (2019), 887–920, https://doi.org/10.1007/s00182-019-00665-5 .

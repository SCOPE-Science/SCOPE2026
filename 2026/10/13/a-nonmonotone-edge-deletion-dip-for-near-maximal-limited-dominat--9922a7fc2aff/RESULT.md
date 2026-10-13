# A nonmonotone edge-deletion dip for near-maximal limited domination

## Finding

For every integer \(n\ge3\), let \(G_{n,t}=K_{n,n}-M_t\), where \(M_t\) is a matching of \(t\) edges, \(0\le t\le n\). Label the two bipartition classes \(L_1,\ldots,L_n\) and \(R_1,\ldots,R_n\) so that exactly \(L_iR_i\), for \(1\le i\le t\), are deleted. A set \(D\) is \(k\)-limited dominating when every omitted vertex has a neighbor in \(D\), and every selected vertex has at most \(k\) omitted neighbors.

At the uniform capacity \(k=n-2\), the complete matching-deletion profile is

\[
\boxed{\gamma_{n-2}^{\mathrm L}(G_{n,t})=\begin{cases}
3,&2\le t\le n-1,\\
4,&t\in\{0,1,n\}.
\end{cases}}
\]

Moreover, let \(\mu_{n,t}\) be the number of labeled minimum \((n-2)\)-limited dominating sets. Then

\[
\boxed{\mu_{n,t}=\begin{cases}
2(n-t)\binom t2,&2\le t\le n-1,\\
\binom n2^2,&t\in\{0,1,n\}.
\end{cases}}
\]

For \(2\le t<n\), every minimum set consists of one vertex belonging to an unmatched pair on one shore, together with two vertices on the opposite shore whose corresponding deleted matching edges exist. Interchanging shores gives the full list. For \(t=0,1,n\), every minimum set consists of two vertices from each shore, and these can be chosen arbitrarily.

In particular, deleting edges along a matching from \(K_{n,n}\), one by one, makes the minimum go from four down to three at the second deletion and back up to four at the final deletion: neither monotone direction describes this parameter under this nested edge-deletion sequence.

## Assumptions and scope

All graphs are finite, simple, and labeled. The same capacity \(k=n-2\) is applied for every \(t\), so comparisons are on a common scale. For \(t<n\) the maximum degree is \(n\), while for \(t=n\) it is \(n-1\); \(k=n-2\) lies below both, hence is nontrivial throughout. The formula counts labeled vertex subsets, not automorphism orbits, and makes no claim for other capacities or for arbitrary nonmatching edge deletions.

## Proof

**Two selected vertices are impossible.** Suppose a \((n-2)\)-limited dominating set \(D\) had two or fewer vertices. A set confined to a single shore cannot qualify: either an omitted vertex on that shore is undominated (if one is omitted), or a selected vertex has at least \(n-1>n-2\) neighbors across the empty shore (if all of that shore is selected, which also requires \(n\ge3\)). Thus a two-element candidate must be \(D=\{L_i,R_j\}\). If \(i>t\), then \(L_i\) is adjacent to all right vertices and has \(n-1\) neighbors outside \(D\), violating capacity. Similarly, if \(j>t\), selected \(R_j\) violates capacity. Hence \(i,j\le t\). If \(i=j\), the selected vertices are nonadjacent and each has all \(n-1\) neighbors outside \(D\), again violating capacity. If \(i\ne j\), omitted \(R_i\) has no neighbor in \(D\): its only potential selected left neighbor is \(L_i\), to which it is nonadjacent. Thus \(|D|\ge3\) for all \(n,t\).

**Exactly three selected vertices.** Again no qualifying set is confined to a shore. Suppose \(D=\{L_i,R_j,R_h\}\), with \(j\ne h\). If \(i\le t\), then \(R_i\) must be among the selected right vertices, or the omitted vertex \(R_i\) would be undominated. But if \(R_i\in D\), it is nonadjacent to its sole selected left vertex \(L_i\), so all \(n-1\) of its neighbors lie outside \(D\), violating capacity. Therefore \(i>t\), so \(L_i\) is an unmatched left vertex. Each selected right vertex must have a missing edge: if \(j>t\), \(R_j\) would have all \(n-1\) omitted left vertices as neighbors, more than \(n-2\). Thus \(j,h\le t\). Conversely, for every \(i>t\) and distinct \(j,h\le t\), the set \(\{L_i,R_j,R_h\}\) dominates both shores: the unmatched \(L_i\) dominates every omitted right vertex, while the two selected matched right vertices collectively dominate every omitted left vertex. The selected \(L_i\) has exactly \(n-2\) omitted neighbors, and each selected right vertex has exactly \(n-2\) omitted neighbors because its one missing matching edge removes an omitted left neighbor. Hence it satisfies the capacity. The same argument with shores exchanged classifies every \(2+1\) configuration. Therefore size three occurs precisely when \(2\le t\le n-1\), and then the number of three-element solutions is exactly \(2(n-t)\binom t2\).

**Four selected vertices and the endpoints.** For every \(n\ge3\), \(0\le t\le n\), any set selecting exactly two vertices from each shore dominates all omitted vertices, because each vertex has at most one nonneighbor across the bipartition. Every selected vertex has at most \(n-2\) omitted vertices on its opposite shore, so it satisfies the capacity. There are \(\binom n2^2\) such sets. If \(t\in\{0,1,n\}\), the previous argument excludes size three, so four is minimum. Every minimum set with four vertices must select two from each shore: a \(1+3\) configuration could qualify only if the singleton came from an unmatched matching position and the three opposite selected vertices had deleted partners, which requires both \(t<n\) and \(t\ge3\), not true for these endpoint values. A \(4+0\) configuration cannot qualify by the preceding single-shore argument. Hence exactly the \(\binom n2^2\) two-plus-two sets are minimum in those three endpoint cases. This proves both formulas and the nonmonotonic transition. \(\square\)

## Verification

The standalone standard-library program `verify_matching_transition.py` directly constructs each bipartite adjacency matrix and exhaustively tests every vertex subset for the domination and capacity conditions for \(3\le n\le8\) and every \(0\le t\le n\). It independently compares the observed minimum and exact number of minimum labeled sets against the two formulas. The recorded run covers **39 graph profiles and 757248 labeled candidate subsets**, with every comparison passing; see `matching_output.txt`. Execute `python3 verify_matching_transition.py`. This is finite corroboration of the proof, not an inference for all orders.

## Relationship to prior work

Božović, Radić, Kovijanić-Vukićević, and Tepeh introduced \(k\)-limited domination and proved \(\gamma_k^{\mathrm L}(K_{m,n})\) exactly, including the \(t=0\) value four here, in Proposition 1(iv) of arXiv:2606.22422. Their results on regular graphs also explain why the fully deleted crown endpoint \(t=n\) at this capacity coincides with a total-domination calculation. The present contribution is the entire **partial matching-deletion profile**, including the unexpected three-vertex regime, both transition points, and all minimizing configurations with exact multiplicities. General bounds and exact results on other graph classes do not determine this behavior in graphs whose matched and unmatched vertices have differing degrees.

## Limitations

The capacity is fixed at \(n-2\), a natural near-maximal value shared across all intermediate edge deletions; the theorem does not classify all other capacities. Only matching deletions, not arbitrary deleted edge sets, are covered. Exhaustive computations are finite and do not establish universal truth or global novelty. Related work may be unindexed or inaccessible; independent external audit has not been performed.

## References

1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, and A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422 (first public 2026-06-21); DOI 10.1007/s40314-026-03902-2, Proposition 1(iv), Sections 1–6. https://arxiv.org/abs/2606.22422 ; https://doi.org/10.1007/s40314-026-03902-2
2. G. Radić, *An improved lower and upper bound of the \(k\)-limited domination number*, arXiv:2610.01442 (first public 2026-10-01; abstract consulted). https://arxiv.org/abs/2610.01442
3. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (first public 2026-06-21; abstract consulted). https://arxiv.org/abs/2606.22428

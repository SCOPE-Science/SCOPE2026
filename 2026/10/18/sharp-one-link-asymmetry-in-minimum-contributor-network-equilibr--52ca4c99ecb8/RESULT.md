# Sharp one-link asymmetry in minimum-contributor network equilibria

## Finding

In the binary best-shot network public-good game, adding one social link can force an *optimal* pure Nash equilibrium to use almost half of the agents as contributors, even though before the link only two contributors were required. Conversely, one added link can reduce the optimum contributor count by at most one. For every finite connected simple undirected graph \(G\) with \(n\ge4\) vertices, and each nonedge \(uv\), the exact sharp bounds are

\[
-1\le i(G+uv)-i(G)\le\left\lfloor\frac{n-4}{2}\right\rfloor.
\]

Both bounds are achieved at each order \(n\ge4\). The upper bound is achieved with \(G\) a tree at each order \(n\ge6\). Thus the first strictly positive increase is possible with six agents, while no graph with at most five agents shows one.

## Assumptions and scope

All graphs are finite, undirected, loopless and simple. A graph is connected in the usual sense. The added edge \(uv\) joins two distinct previously nonadjacent vertices without changing the vertex set. Every vertex/agent chooses effort \(0\) or \(1\). The best-shot rule is that an agent chooses \(1\) precisely when every neighbor chooses \(0\), and chooses \(0\) otherwise. An equilibrium's contributors therefore form a maximal independent set, equivalently an independent dominating set. Here \(i(G)\) is the **minimum cardinality** of an independent dominating set, so it is the minimum contributor count over all *pure* equilibria; it is not the maximum contributor count, an equilibrium selection probability, or unconstrained social-welfare optimum. Benefits are locally satiated and the common contribution cost is positive and below that benefit, as in the source model. No mixed equilibria, subsidies, formation incentives, weighted contacts, or strategic effects of choosing the new link are claimed.

An independent dominating set \(S\) has no edges inside \(S\) and meets the closed neighborhood of every vertex. For \(t\in S\), define the set of private outside neighbors with respect to \(S\) by \(P_t(S)=\{x\notin S:N_G(x)\cap S=\{t\}\}\).

## Proof

**Equilibrium translation.** Under the specified best-response rule, two adjacent agents cannot both contribute, and each noncontributor must have a contributing neighbor. Conversely, every independent dominating set supplies a profile satisfying both conditions. Thus the optimized contributor number is \(i(G)\).

**Lower perturbation bound.** Put \(H=G+uv\) and take a minimum independent dominating set \(T\) of \(H\). It remains independent in \(G\). If it also dominates \(G\), then \(i(G)\le i(H)\). Otherwise, precisely one of the endpoints, say \(v\), is not dominated by \(T\) in \(G\); the newly added edge \(uv\) must be its only reason for domination in \(H\). Consequently \(u\in T\), \(v\notin T\), and \(v\) is adjacent in \(G\) to no member of \(T\). Then \(T\cup\{v\}\) is an independent dominating set in \(G\): the only formerly undominated vertex is \(v\) itself. Therefore \(i(G)\le i(H)+1\), giving \(i(H)-i(G)\ge-1\).

**Upper perturbation bound.** Let \(S\) be a minimum independent dominating set of \(G\), of cardinality \(k\). If \(\{u,v\}\not\subseteq S\), adding \(uv\) preserves both independence and domination of \(S\), so \(i(H)\le k\). Otherwise \(u,v\in S\) and \(k\ge2\). The sets \(P_u(S)\) and \(P_v(S)\) are disjoint subsets of \(V(G)\setminus S\). Fix \(t\in\{u,v\}\). Choose a maximal independent set \(J_t\) of the induced graph on \(P_t(S)\) (the empty set when \(P_t(S)\) is empty). Because every vertex of \(P_t(S)\) is adjacent among \(S\) only to \(t\), the set

\[
S_t=(S\setminus\{t\})\cup J_t
\]

is independent in \(H\); the other endpoint now dominates \(t\) through the added edge. Every vertex outside \(S\) not privately dominated by \(t\) still has a neighbor in \(S\setminus\{t\}\), and every vertex in \(P_t(S)\) is dominated by \(J_t\) because that set is maximal independent in the induced graph. Hence \(S_t\) dominates \(H\). In particular,

\[
i(H)\le k-1+\min\bigl\{|P_u(S)|,|P_v(S)|\bigr\}
\le k-1+\left\lfloor\frac{n-k}{2}\right\rfloor.
\]

For \(k\ge2\), this yields \(i(H)-i(G)\le\lfloor(n-4)/2\rfloor\). If \(k=1\) or the endpoints are not both in \(S\), the difference is at most zero, also satisfying the asserted bound for \(n\ge4\).

**Sharp deterioration at all large orders.** Choose integers \(b\ge a\ge1\). Form a tree \(T_{a,b}\) by starting with the four-vertex path \(u-p-q-v\), attaching \(a\) leaves only to \(u\), and attaching \(b\) leaves only to \(v\). It has \(n=a+b+4\) vertices, and \(\{u,v\}\) is independent dominating, while no single vertex dominates; therefore \(i(T_{a,b})=2\). Write \(H_{a,b}=T_{a,b}+uv\), with one four-cycle and the pendant leaves unchanged.

Every independent dominating set of \(H_{a,b}\) is in exactly one of three categories. If it contains \(u\), it cannot contain \(v\) or \(p\); it must contain all \(b\) leaves at \(v\) and also \(q\), giving at least \(b+2\) vertices, attained by that choice. If it contains \(v\), the symmetric argument gives at least and exactly \(a+2\) vertices. If it contains neither center, all \(a+b\) leaves are required and at least one of \(p,q\) is needed to dominate both intermediate vertices, giving at least and exactly \(a+b+1\). Consequently

\[
i(H_{a,b})=\min\{a+2,b+2,a+b+1\}=a+2
\quad\text{when }b\ge a\ge1.
\]

Choose \(a=\lfloor(n-4)/2\rfloor\) and \(b=n-4-a\) for every \(n\ge6\). This attains deterioration \(a\), the universal upper bound, by adding one edge to a tree. In particular \(n=6\) and \(a=b=1\) give \(i(T)=2\) and \(i(T+uv)=3\).

**Sharp improvement at all orders.** For every \(n\ge4\), take a tree with edges \(u-w\), \(w-v\) and \(u-z_j\) for its other \(n-3\) vertices \(z_j\). It has \(i(G)=2\), since it has no universal vertex and \(\{u,v\}\) dominates independently. Add \(uv\). Now \(u\) is universal, so \(i(G+uv)=1\), attaining change \(-1\). For the zero upper bound at \(n=4,5\), adding the missing edge between endpoints of the path \(P_n\) produces \(C_n\), and both have independent domination number \(2\). For \(n=3\), the only connected single-edge insertion is from \(P_3\) to \(C_3\), preserving the value \(1\); there is no connected two-vertex graph with a nonedge.

## Verification

Run `python3 verify.py` using Python 3 and its standard library only. This independently enumerates every labelled connected graph on \(3\) through \(6\) vertices and every permissible added edge; it computes minimum independent dominating-set sizes by checking all vertex subsets exactly, and asserts the theorem's bounds. The respective numbers of edge additions are \(3\), \(84\), \(3140\), and \(186360\). On six vertices the observed changes are \(-1\) in \(29895\) comparisons, \(0\) in \(155655\), and \(+1\) in \(810\); no smaller graph has a positive change. The same script checks the improving construction for orders \(4\) through \(14\) and the deteriorating family for orders \(6\) through \(14\). These finite checks corroborate but are not prerequisites for the all-order proof above.

## Relationship to prior work

Dall'Asta, Pin and Ramezanpour identify the binary best-shot equilibria with maximal independent sets and study finding a minimum-contributor equilibrium; they explicitly discuss how changing the network would be a different design problem. Their model supplies the economic interpretation but not a worst-case sharp perturbation theorem. Goddard and Henning survey general independent-domination bounds, standard graph constructions and related criticality concepts. Xu surveys *independence bondage*, which measures how many **deleted** edges can cause **an increase**; that does not imply the size of a change under a **single added** edge. Work on independent-domination stability of trees and unicyclic graphs examines **vertex deletion**, not this edge-insertion extremum. Thakkar and Kakrecha examine **edge domination** (choosing edges rather than vertices), a distinct invariant. The universal two-sided bound extends the known existence of large increases to a sharp worst-case inequality over every connected network of a given order, and it separately bounds possible improvements.

## Limitations

The result is about a minimum among stable pure equilibrium profiles, not predicted actual equilibrium behavior after link formation. Costs are uniform, the graph is unweighted and undirected, and the added edge is costless in the objective. Although the exact bound is sharp, it is a combinatorial limit and says nothing about the prevalence of extremal configurations in realistic networks. Priority beyond the specifically inspected literature is not independently guaranteed.

## References

1. L. Dall'Asta, P. Pin and A. Ramezanpour, *Optimal Equilibria of the Best Shot Game*, Fondazione Eni Enrico Mattei Working Paper 33.2009 (public working-paper catalog dated 23 June 2009). https://services.bepress.com/feem/paper294 ; full paper https://feem-media.s3.eu-central-1.amazonaws.com/wp-content/uploads/NDL2009-033.pdf
2. W. Goddard and M. A. Henning, *Independent domination in graphs: A survey and recent results*, Discrete Mathematics 313 (2013), 839–854, doi:10.1016/j.disc.2012.11.031. https://doi.org/10.1016/j.disc.2012.11.031
3. J.-M. Xu, *On Bondage Numbers of Graphs: A Survey with Some Comments*, International Journal of Combinatorics (2013), Article 595210, doi:10.1155/2013/595210. https://doi.org/10.1155/2013/595210
4. P. Wang et al., *Independent Domination Stable Trees and Unicyclic Graphs*, Mathematics 7 (2019), 820. https://www.mdpi.com/2227-7390/7/9/820
5. D. K. Thakkar and B. M. Kakrecha, *About the Edge Domination Number of the Graphs*, Advances in Theoretical and Applied Mathematics 11 (2016), 93–98. https://www.ripublication.com/atam16/atamv11n2_01.pdf

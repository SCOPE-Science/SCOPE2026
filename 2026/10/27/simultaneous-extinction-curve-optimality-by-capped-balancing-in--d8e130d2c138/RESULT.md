# Simultaneous extinction-curve optimality by capped balancing in mutualistic networks

## Finding

**Theorem.** Let \(r\ge2\), and let \(a_1,\ldots,a_r\) be positive integers. Partition \(N=\sum_j a_j\) active species into disjoint nonempty groups \(G_j\) of sizes \(a_j\). Construct one distinct passive species for each member of the Cartesian product \(G_1\times\cdots\times G_r\); its only active partners are the entries in its tuple. Under sequential permanent removal of active species, with a passive species extinguished exactly when every partner has been removed, repeatedly selecting a not-yet-exhausted group having the **smallest current number of removed members** gives a single order that maximizes the number of extinct passive species at **every** removal budget simultaneously.

If \(1\le a\le b\) and \(r=2\), the maximum sum of the extinct-passive-species counts after each of the \(a+b\) removal stages is

\[
S_{\max}(a,b)=\frac{a(a^2+3b^2+3b-1)}6.
\]

If \(a<b\), static descending-degree ranking removes all \(a\) members of the smaller group first and has area

\[
S_{\deg}(a,b)=\frac{ab(b+1)}2,
\qquad
S_{\max}-S_{\deg}=\frac{a(a-1)(a+1)}6.
\]

Thus for every \(2\le a<b\) **every** degree-descending order is strictly inferior. At \(a=2,b=3\), the scores are 13 versus 12.

**Sharp small-network boundary.** Consider **any** two-partner incidence model with \(n\) active species: each passive species corresponds to an edge of a simple graph \(H\) on the active species, and dies when both endpoints have been removed. For every \(n\le4\), at least one order sorted by descending initial active degree is optimal. At \(n=5\), exactly ten of the \(2^{10}\) labeled graphs admit no optimal descending-degree order; these are precisely the ten labeled copies of \(K_{2,3}\), forming one isomorphism type. The boundary is exact, established by the exhaustive integer dynamic program in `verify.py`.

## Assumptions and scope

Networks are finite and simple, with all active-species group sizes strictly positive; \(r\ge2\). Every possible tuple across the groups creates exactly one passive species. A species has no alternative partners outside its tuple. The removal order is fixed in advance, and removal is permanent. There is no rewiring, compensatory colonization, dynamical cascade, or stochastic loss process. Let \(x_j(t)\) be the count removed from \(G_j\) after exactly \(t\) active removals, where \(t\in\{0,\ldots,N\}\). Define the unnormalized area \(S(\pi)=\sum_{t=1}^N E_\pi(t)\), where \(E_\pi(t)\) is the number of extinct passive species after \(t\) removals; normalization by the number of passive species and by the number of stages leaves every optimizer unchanged. The separate sharp-boundary census concerns all simple graphs, including disconnected graphs and isolates; each graph edge represents exactly one passive species of degree two. The graph census is a finite computational theorem, not an assertion about larger graphs.

## Proof

**Exact extinction identity.** A passive species indexed by a tuple dies precisely when every chosen active partner has been removed. For each group \(G_j\), there are \(x_j(t)\) possible removed partners. Thus

\[
E_\pi(t)=\prod_{j=1}^r x_j(t).
\]

This counts each passive species once, and no other passive species has died.

**Maximizing a fixed prefix.** For \(t<r\), every feasible product vanishes. For \(t\ge r\), there is a feasible positive product. Any maximum must have all coordinates at least one. Suppose a feasible positive profile has \(x_i\ge x_j+2\) and \(x_j<a_j\). Moving one removed member from group \(i\) to group \(j\) preserves the total, respects the group limits, and changes the product by the positive factor associated with

\[
(x_i-1)(x_j+1)-x_ix_j=x_i-x_j-1>0.
\]

Conversely, the integer allocation maximizing the product at total \(t\) is the capped equal-level allocation: start with one per group, then increment currently smallest unsaturated coordinates. This follows by successive exchanges, or equivalently from the strictly decreasing marginal ratios \((k+1)/k\) for \(k\ge1\), which yield the elementary separable concave resource-allocation rule. Starting instead at the all-zero profile and repeatedly incrementing a smallest unsaturated coordinate produces exactly these capped equal-level allocations once \(t\ge r\). Therefore a *single* removal order realizes the maximum \(\max_{\sum_j x_j=t,\,0\le x_j\le a_j}\prod_j x_j\) for every \(t\), simultaneously; summing proves the area optimum. Since each individual prefix reaches its own upper bound, any area optimizer must likewise maximize every prefix product for \(t\ge r\).

**Two-group evaluation.** For \(a\le b\), one such order alternates removals from the two groups for the first \(2a\) stages, then removes the \(b-a\) remaining members of the larger group. At the two stages associated with \(k=1,\ldots,a\), extinct-plant counts are \(k(k-1)\) and \(k^2\). At the \(j\)-th remaining stage they equal \(a(a+j)\). Summing

\[
\sum_{k=1}^a(2k^2-k)+a\sum_{j=1}^{b-a}(a+j)
\]

and simplifying yields \(S_{\max}(a,b)=a(a^2+3b^2+3b-1)/6\). If \(a<b\), active degrees are \(b\) on the \(a\)-member side and \(a\) on the \(b\)-member side. A descending-degree ranking exhausts the first side, then removes the second; the extinct counts in the latter block are \(a,2a,\ldots,ba\), giving \(S_{\deg}=ab(b+1)/2\) and the displayed positive deficit when \(a\ge2\).

**Sharp boundary over all two-partner networks.** For a graph \(H=(V,E)\) of order \(n\), let \(e(S)\) count edges induced by the set \(S\subseteq V\) of removed active species. Define \(F(\varnothing)=G(\varnothing)=0\) and, for nonempty \(S\),

\[
F(S)=e(S)+\max_{v\in S}F(S\setminus\{v\}),
\]

\[
G(S)=e(S)+\max_{\substack{v\in S\\
\deg_H(v)=\min_{u\in S}\deg_H(u)}}G(S\setminus\{v\}).
\]

The first recurrence exhausts **every** order because \(v\) is the last removed vertex; the second exhausts every order sorted by *initial* nonincreasing degree, since its last vertex must have minimum initial degree in the remaining set. These recurrences are inductively exact. `verify.py` enumerates every labeled simple graph by its edge bitmask for each \(1\le n\le5\), computes all induced edge counts and every subset recurrence using integers, and tests \(F(V)>G(V)\). It finds no failures for \(n\le4\), and exactly ten failures for \(n=5\). Each of the ten is checked to be a copy of \(K_{2,3}\) by its exact edge set, with \(F(V)=13\) and \(G(V)=12\). Because all \(2^{\binom n2}\) edge bitmasks and all \(2^n\) subset states are visited, this finite exhaustion proves the sharp boundary and classification.

## Verification

Run `python verify.py` in an ordinary Python 3 installation, with no external dependencies. `certificate.json` stores the exact expected output. The checker independently enumerates all group-label sequences for eight small capacity vectors (not only the proposed balanced schedule), compares their exact maximum with the construction, checks the two-group closed form when applicable, and exhausts \(1+2+8+64+1024=1099\) labeled simple graphs through five vertices. The graph algorithm uses exact integer arithmetic and visits all possible removals of the last vertex, so there is no stochastic simulation, heuristic search, or numerical tolerance. These finite checks do not establish the all-size water-filling theorem; the exchange argument does.

## Relationship to prior work

Domínguez-García and Muñoz (2015) explicitly define attack rankings by sequentially removing active species, declaring passive species extinct when they have lost all partners, and scoring the area of the extinction curve. Their study compares degree centrality and other ranking heuristics on empirical networks and uses a genetic algorithm for approximate best rankings. The present theorem addresses the **same observable** but determines a pointwise optimal ranking for a precisely defined product-incidence network family, and gives a sharp minimum-size classification of degree-ranking failure in the complete two-partner class. It makes no assertion about MusRank convergence or quality.

Memmott, Waser, and Price (2004) motivate sequential pollinator removal and secondary plant extinction but do not establish the present sharp ranking family in the material inspected. General minimum-sum vertex-cover results optimize sums of **first** endpoint positions; here a two-partner plant dies at the **last** endpoint's removal, and the objective minimizes sums of last positions (equivalently maximizes the reverse-order first-position sum). Thus a result minimizing a first-endpoint objective does not imply this theorem by simply relabeling the parameters. Established integer balancing principles underlie the proof; the new application and exact sharp ecological obstruction, not the elementary inequality in isolation, are the scientific contribution.

## Limitations

The product-incidence family is deliberately structured, not a claim about all empirical pollination networks. The sharp five-pollinator census covers simple pair-incidence networks with at most five active nodes, including isolates, and no multiplicities of identical pairwise passive neighborhoods; allowing repeated passive species introduces weights and may change the smallest obstruction. The score counts secondary extinctions after each step, not ecological abundance or dynamic stability. Later work on ranking algorithms and graph ordering may contain an equivalent reformulation; independent bibliographic validation is not asserted. The exhaustive small-network result requires the supplied Python checker and does not alone imply the infinite family theorem.

## References

1. Domínguez-García, V., and Muñoz, M. A. (2015), *Ranking species in mutualistic networks*, Scientific Reports 5, 8182. First public date: 2015-02-02. https://doi.org/10.1038/srep08182
2. Memmott, J., Waser, N. M., and Price, M. V. (2004), *Tolerance of pollination networks to species extinctions*, Proceedings of the Royal Society B 271, 2605–2611. https://doi.org/10.1098/rspb.2004.2909
3. *Minimum-sum vertex cover on complete multipartite graphs*, published-finding corpus published record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-minimum-sum-vertex-cover-on-complete-multipartite-graphs--0406c3406a18

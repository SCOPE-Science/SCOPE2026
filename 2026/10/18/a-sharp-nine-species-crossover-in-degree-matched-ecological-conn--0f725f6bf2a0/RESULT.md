# A sharp nine-species crossover in degree-matched ecological connectivity

## Finding

Consider finite connected, simple bipartite interaction graphs with a nonempty plant guild of size \(a\) and pollinator guild of size \(b\). Plants remain in the network; each pollinator independently disappears with probability \(q\in(0,1)\), together with all its incident edges. Let \(L_G(S)\) denote the order (counting both guilds) of the largest connected component when precisely the pollinators in \(S\) survive, and let \(C_G(q)=\mathbb E[L_G(S)]\). An isolated surviving plant is a component of order one. Two graphs are degree-matched if they have the same guild sizes and identical degree multisets *separately within each guild*.

**Theorem.** For any two degree-matched connected bipartite graphs with at most eight total species, \(C_G(q)-C_H(q)\) has one weak sign throughout \(0<q<1\). More strongly, their expected-largest-component coefficient vectors, defined below, are componentwise comparable. This assertion is sharp: there exist degree-matched connected graphs on four plants and five pollinators, both with nine edges, whose difference is
\[
C_G(q)-C_H(q)=q(1-q)^2(2-3q).
\]
The sign is positive for \(0<q<2/3\), zero at \(q=2/3\), and negative for \(2/3<q<1\). **Moreover**, these witness graphs have the same maximum bipartite matching size for *each individual surviving-pollinator subset*, not merely in expectation.

## Assumptions and scope

All graphs are finite, simple, undirected and bipartite. An incidence row specifies one plant's adjacent pollinators; repeated rows represent different plant species, not repeated edges. Pollinator losses are identically and independently distributed; plants do not disappear or undergo secondary extinction. The largest component counts both surviving plants and surviving pollinators, including isolated plant singletons. Only *connected initial graphs* with nonempty guilds and no initially isolated species are compared. The result concerns finite networks of all guild sizes with at most eight species and an explicit connected nine-species witness; it is not a statement about all larger graphs or dynamical extinction cascades.

## Proof

**Exact reliability expansion.** For a network with \(b\) pollinators let
\[
A_k(G)=\sum_{S\subseteq W,\ |S|=k}L_G(S),\qquad 0\le k\le b.
\]
Independent pollinator survival gives
\[
C_G(q)=\sum_{k=0}^{b} A_k(G)(1-q)^kq^{b-k}.
\]
Each summand's Bernstein-type basis factor is nonnegative on the probability interval. Therefore, coefficientwise comparability of the vectors \((A_0,\ldots,A_b)\) for a degree-matched pair implies that their expectation difference never changes sign. This is a sufficient certificate for the claimed lower bound, without requiring polynomial-root approximations.

**Exhaustion through eight total vertices.** Represent a graph with \(a\) plants and \(b\) pollinators by its \(a\) nonzero binary adjacency rows, each in \(\{1,\ldots,2^b-1\}\). Permuting plant rows preserves its degree signature and all coefficients, so the nondecreasing row tuples enumerate every eligible graph (possibly with redundant pollinator relabelings). Every \((a,b)\) with \(a,b\ge1\), \(2\le a+b\le8\), is enumerated. A disjoint-set connectivity test accepts only connected initial graphs; hence each guild has no isolated vertex. For each accepted graph, every one of its \(2^b\) survivor subsets is enumerated and the largest connected component is computed exactly. The group signature is the pair of sorted within-guild degree lists. All *distinct* coefficient vectors within each degree-signature group are compared coordinatewise, exhaustively.

The complete counts by total vertex number are:

| Total species | Connected row profiles | Degree-signature groups | Distinct coefficient vectors | Compared unequal vector pairs |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 1 | 1 | 1 | 0 |
| 3 | 2 | 2 | 2 | 0 |
| 4 | 5 | 4 | 4 | 0 |
| 5 | 18 | 10 | 10 | 0 |
| 6 | 89 | 27 | 27 | 0 |
| 7 | 590 | 80 | 85 | 5 |
| 8 | 5,160 | 241 | 285 | 50 |

In all 55 comparisons of unequal coefficient vectors, either every coordinate difference is nonnegative or every difference is nonpositive. The enumeration is exhaustive by the binary-row bijection and the plant-permutation quotient; its exact, standalone checker is included as `check_robustness.py`. It independently obtains component orders by disjoint-set union and graph flood fill for **every** survivor subset and asserts agreement, before checking all coefficient-vector pairs. Since coefficientwise dominance implies fixed sign, no degree-matched crossover exists with at most eight vertices.

**Nine-species construction.** Write pollinators as \(a,b,c,d,e\). The four plant neighborhoods are
\[
\begin{aligned}
G &: \{a,b\},\ \{a,c\},\ \{b,d\},\ \{c,d,e\},\\
H &: \{a,b\},\ \{a,c\},\ \{b,c,d\},\ \{d,e\}.
\end{aligned}
\]
Each graph is connected. Both have plant-degree multiset \((2,2,2,3)\) and pollinator-degree multiset \((1,2,2,2,2)\), hence nine edges. Direct enumeration of the \(32\) surviving-pollinator subsets yields
\[
(A_0(G),\ldots,A_5(G))=(1,14,40,59,40,9),
\]
\[
(A_0(H),\ldots,A_5(H))=(1,14,41,58,38,9).
\]
Subtracting the two reliability expansions with survivor probability \(u=1-q\) gives
\[
-u^2(1-u)^3+u^3(1-u)^2+2u^4(1-u)
=u^2(1-u)(3u-1)=q(1-q)^2(2-3q).
\]
The only interior root is \(q=2/3\), and its sign switches. For example, at \(q=1/2\) the expectations are \(163/32\) versus \(161/32\), while at \(q=3/4\) they are \(3117/1024\) versus \(3129/1024\).

**Matching equality.** For a surviving pollinator subset \(S\), let \(M_G(S)\) be the maximum cardinality of a bipartite matching in the surviving graph. An exact plant-by-plant dynamic program stores all sets of pollinators that can be matched to the previously processed plants (including the option to leave a plant unmatched), and then takes the maximum cardinality. Running it on each of the \(32\) subsets for both displayed graphs yields \(M_G(S)=M_H(S)\) in all cases. The sum of either matching maximum over the \(\binom5k\) subsets of size \(k\), for \(k=0,\ldots,5\), is \((0,5,20,30,20,4)\). This is an additional finite, exact property of the exhibited pair; it does not enter the general lower-bound argument.

## Verification

Run `python3 check_robustness.py` with Python 3.9 or later and no third-party dependencies. The script checks all guild sizes and connected incidence graphs through eight total vertices, verifies all 55 required pairwise coefficient comparisons, and reconstructs both witness coefficient vectors by two independently implemented component algorithms. It also expands their difference as an exact integer polynomial in the failure probability and verifies matching equality separately for every one of the \(32\) survivor sets. The script prints `ALL EXACT CHECKS PASSED` on successful completion. The exhaustive finite computation is a proof of this *finite* minimality statement by an explicit complete enumeration, not a proof of any asymptotic graph-property claim.

## Relationship to prior work

Solé and Montoya, *Complexity and Fragility in Ecological Networks* (arXiv:cond-mat/0011196v1, first public version 10 November 2000), study the largest species cluster under random and degree-targeted node removal in three substantial food webs. Their full six-page manuscript, including its largest-cluster measure and experiments, concerns empirical network fragmentation, not a degree-matched complete finite threshold or the one-guild Bernoulli reliability vectors above. Dunne, Williams and Martinez (2002) examine secondary extinctions and connectance-dependent food-web robustness, a different endpoint.

Chabert-Liddell, Barbillon and Donnet (arXiv:2106.06348, 2021; Environmetrics 2022) study robustness of bipartite ecological networks using stochastic block models and sequential removals. Available abstracts discuss expected disconnected-species proportions, not the exact largest-component statistic for a fixed pair of small graphs. Their full text and supplement could not be inspected in this assessment, so no full-document exclusion of overlap is asserted. Kitsak and colleagues (arXiv:1709.10174, 2017) examine component stability under edge percolation; an edge-failure result need not imply the present one-guild vertex-deletion crossover. The exact witness matching equality additionally distinguishes connectivity from allocation capacity, two different network functionals.

## Limitations

This is a complete small-order classification only up to eight vertices, plus a verified nine-vertex example. The nine-vertex witness is not claimed unique or edge-minimal. Exact matching equality is verified only for that pair. The mathematical model does not include secondary plant extinction, correlated pollinator failures, different failure risks, directed interactions, or demographic dynamics. Bibliographic originality is based on identified accessible sources and research searches, not an exhaustive theorem-database guarantee; inaccessible full text of a closely related ecological robustness paper remains a residual risk. No independent scientific audit has been conducted.

## References

1. R. V. Solé and J. M. Montoya, *Complexity and Fragility in Ecological Networks* (2000), arXiv:cond-mat/0011196v1, https://arxiv.org/abs/cond-mat/0011196.
2. J. A. Dunne, R. J. Williams and N. D. Martinez, *Network structure and biodiversity loss in food webs: robustness increases with connectance*, Ecology Letters 5 (2002), 558–567, doi:10.1046/j.1461-0248.2002.00354.x.
3. S.-C. Chabert-Liddell, P. Barbillon and S. Donnet, *Impact of the mesoscale structure of a bipartite ecological interaction network on its robustness through a probabilistic modeling*, Environmetrics 33 (2022), e2709, arXiv:2106.06348, doi:10.1002/env.2709.
4. M. Kitsak et al., *Stability of a giant connected component in a complex network*, Physical Review E 97 (2018), 012309, arXiv:1709.10174, doi:10.1103/PhysRevE.97.012309.

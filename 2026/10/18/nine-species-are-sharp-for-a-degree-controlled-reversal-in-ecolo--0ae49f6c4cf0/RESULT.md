# Nine species are sharp for a degree-controlled reversal in ecological matching capacity

## Finding
Consider a connected simple bipartite interaction network with \(a\ge 1\) plants and \(b\ge 1\) pollinators. Every pollinator fails independently with common probability \(q\in(0,1)\). A remaining pollinator can serve at most one plant, and each served plant requires one distinct surviving pollinator; thus the maximum simultaneously served number of plants is the bipartite maximum matching size \(M_G(S)\), where \(S\) is the set of surviving pollinators. Set \(C_G(q)=\mathbb E[M_G(S)]\).

Two networks are *degree-matched* if they have the same plant and pollinator counts and identical respective multisets of degrees, not necessarily the same labeled adjacency matrix. Among connected degree-matched networks with \(a+b\le8\), the capacity difference \(C_G(q)-C_H(q)\) cannot change sign on \((0,1)\). Indeed, their matching-capacity Bernstein coefficients are componentwise comparable (one sequence dominates the other).

The bound is sharp at nine species. On four plants and five pollinators labeled \(a,b,c,d,e\), define plant neighborhoods
\[
G:\quad \{a,c,d,e\},\ \{a,b,c\},\ \{b\},\ \{a\};
\]
\[
H:\quad \{a,b,c,e\},\ \{b,c,d\},\ \{a\},\ \{a\}.
\]
Both networks are connected, with plant-degree multiset \((1,1,3,4)\) and pollinator-degree multiset \((1,1,2,2,3)\). Nonetheless,
\[
\boxed{C_G(q)-C_H(q)=(1-q)^2(1-2q^2).}
\]
Hence \(G\) has greater expected matching capacity for \(0<q<1/\sqrt2\), the capacities agree at \(q=1/\sqrt2\), and \(H\) has greater expected matching capacity for \(1/\sqrt2<q<1\).

## Assumptions and scope
An interaction represents a feasible plant–pollinator allocation, not a guarantee of biological pollination. Both guilds are finite, their graph is connected and simple, and all species have positive degree before failure. The service rule is a one-to-one capacity model: no surviving pollinator serves more than one plant and no plant receives more than one allocated pollinator. All plants stay potentially available while pollinators fail independently with identical probability \(q\), and allocation is optimized after failures. The quantities concern a single allocation period, not population dynamics or coextinction cascades. The result is for every real \(q\in(0,1)\), not merely sampled rates.

## Proof
Write \(B=\{1,\ldots,b\}\) for the pollinator guild and \(\nu(G[S])\) for the maximum matching size in the subgraph retaining all plants and only pollinators in \(S\subseteq B\). Define exact integers
\[
A_k(G)=\sum_{\substack{S\subseteq B\\|S|=k}}\nu(G[S]),\qquad 0\le k\le b.
\]
Independence yields the Bernstein-basis identity
\[
C_G(q)=\sum_{k=0}^{b}A_k(G)(1-q)^kq^{b-k}.
\]
All basis terms are positive for \(0<q<1\). Therefore a componentwise fixed sign for \(A_k(G)-A_k(H)\) proves a fixed capacity ordering at *every* failure probability.

For \(a+b\le8\), there are finitely many labeled bipartite adjacency matrices, specifically the \(2^{ab}\) binary matrices for each pair of guild sizes \(a,b\ge1\) with \(a+b\le8\). Exhaustively enumerate every such matrix; retain connected graphs and group their \((a,b)\)-specific matrices by the sorted degree multisets of each guild. For each retained graph and every pollinator subset, calculate maximum matching size by the following exact recurrence. Process plants in fixed order; from state \((i,U)\), where \(U\) is the used-pollinator mask, either skip plant \(i\) or assign it to any available adjacent surviving pollinator, adding one and continuing with the enlarged used mask. The base case after the last plant has value zero. This recursion examines *all* partial injective allocations, so its optimum is the maximum matching size, without approximation or a numerical optimizer. Sum these optima for each survivor count to obtain all \(A_k\).

The complete enumeration includes \(70{,}492\) connected labeled matrices, with \(21\) comparisons between distinct coefficient vectors sharing a guild-size and degree-multiset signature. In every such comparison, all nonzero coefficient differences have the same sign. The standalone program reproduces the entire enumeration and each comparison; pairs with identical coefficient vectors are automatically tied. It follows from the positive Bernstein-basis identity that no connected degree-matched pair on at most eight species reverses its capacity ordering.

For the specified four-by-five networks, direct subset enumeration gives
\[
(A_0(G),\ldots,A_5(G))=(0,5,19,27,17,4),
\]
\[
(A_0(H),\ldots,A_5(H))=(0,5,20,26,14,3).
\]
The difference is
\[
-q^3(1-q)^2+q^2(1-q)^3+3q(1-q)^4+(1-q)^5
=(1-q)^2(1-2q^2).
\]
This is positive below \(1/\sqrt2\) and negative above it, establishing sharpness. At \(q=0\), the full-graph maximum matching sizes are four and three; the reversal is genuinely caused by increasing pollinator failure. At \(q=3/4\), capacities are \(19/16\) and \(153/128\), respectively.

## Verification
The standalone C++17 file `verify_matching_capacity.cpp` is self-contained. Compile using `g++ -std=c++17 -O2 -Wall -Wextra verify_matching_capacity.cpp -o verify_matching_capacity` and execute `./verify_matching_capacity`. It enumerates every labeled incidence matrix for all ordered positive guild sizes totaling at most eight, tests connectivity, calculates sorted degree signatures, and compares coefficient vectors. It independently re-evaluates all \(32\) failure subsets of both nine-species witnesses using a second exhaustive assignment routine. It checks the integer coefficients and expands their difference as \(1-2q-q^2+4q^3-2q^4\). All comparisons are integer exact; no floating-point tests are used. The run prints `PASS` after the checks.

## Relationship to prior work
Olesen et al. (2008) demonstrate why temporal plant–pollinator interaction architecture matters; Kaiser-Bunbury et al. (2010) examine resilience under partner losses. Neither establishes a capacity-optimal matching comparison for every node-failure probability. Li and Zhang (2017) prove that identical degree sequences need not determine the *static* maximum matching size in their scale-free constructions. Static inequality at one failure rate does not imply a reversal as that rate varies, nor a sharp minimum nine-vertex theorem. Simmons et al. (2019) show that degrees can hide ecologically important bipartite motif architecture, without computing this matching-capacity survival polynomial. The present result is an exact finite threshold for an allocation-capacity measure, not a claim that degree distribution by itself determines matching behavior.

## Limitations
The lower-bound proof is a complete finite computation, not a pen-and-paper classification of isomorphism classes. Its exact algorithm and full source are part of the result. The service measure assumes one-to-one allocations and perfectly adaptable reassignment after failures, unlike pollinators that visit many plants. No inference is made about actual seed production, persistence, correlated pollinator losses, weighted capacities, or larger networks' complete reversal classifications. Bibliographic overlap remains possible in graph-reliability or stochastic matching literature despite targeted comparisons.

## References
1. Olesen, J. M., Bascompte, J., Elberling, H., and Jordano, P. (2008), “Temporal dynamics in a pollination network,” *Ecology* 89, 1573–1582, https://doi.org/10.1890/07-0451.1. First published 2008-06-01.
2. Kaiser-Bunbury, C. N., et al. (2010), “The robustness of pollination networks to the loss of species and interactions,” *Ecology Letters* 13, 442–452, https://doi.org/10.1111/j.1461-0248.2009.01437.x.
3. Li, H. and Zhang, Z. (2017), “Maximum matchings in scale-free networks with identical degree distribution,” arXiv:1703.09041, https://arxiv.org/abs/1703.09041.
4. Simmons, B. I., et al. (2019), “bmotif: A package for motif analyses of bipartite networks,” *Methods in Ecology and Evolution* 10, 695–701, https://doi.org/10.1111/2041-210X.13149.

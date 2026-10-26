# Exact strong chromatic index of the prism graphs \(C_n\square K_2\)

## Finding
For each integer \(n\ge3\), let \(P_n=C_n\square K_2\), the simple prism graph with two disjoint \(n\)-cycles and a perfect matching of corresponding vertices. Its strong chromatic index (the fewest colors in an edge coloring whose color classes are induced matchings) equals
\[
\chi'_s(P_n)=\begin{cases}
9&n=3,\\
8&n\in\{5,6\},\\
6&4\mid n,\\
7&\text{otherwise}.
\end{cases}
\]
In particular, every odd prism with \(n\ge7\) has strong chromatic index exactly seven, and the five-prism has index eight.

## Assumptions and scope
All graphs are simple and undirected. Let columns be indexed by \(\mathbb Z/n\mathbb Z\), with vertices \(u_i,v_i\) and edges \(r_i=u_iv_i\), \(t_i=u_iu_{i+1}\), \(b_i=v_iv_{i+1}\). The order \(n=3\) denotes the triangular prism (not a multigraph). Strong coloring forbids equal colors on any two edges sharing an endpoint or having an edge between their endpoint sets. The finite certificates specify each column as \((c(r_i),c(t_i),c(b_i))\), with color labels beginning at zero.

## Proof
**Lower bound of six, and a period-four obstruction.** For every edge \(u_iv_i\) in a cubic simple prism, the five edges consisting of that rung and its four incident horizontal edges form a clique of size five in the square of the line graph. Either neighbor rung \(r_{i-1}\) or \(r_{i+1}\) conflicts with every edge of this clique. For \(n\ge7\), the six-color hypothesis forces \(c(r_{i-1})=c(r_{i+1})\). Hence rung colors are two-periodic. Adjacent rungs conflict, so \(n\) is even and the two rung colors differ. Every horizontal edge conflicts with rungs of both colors, leaving four colors for the horizontals.

For each column \(i\), the four edges \(t_i,t_{i+1},b_i,b_{i+1}\) pairwise conflict and therefore use these four colors once each. Edge \(t_{i+2}\) conflicts with \(t_i,t_{i+1},b_{i+1}\); its only remaining horizontal color is \(c(b_i)\). Similarly \(c(b_{i+2})=c(t_i)\). Thus the horizontal color rows have period four; because adjacent horizontal edges have different colors, period two is impossible. Consequently \(4\mid n\). This shows that for \(n\ge7\) with \(4\nmid n\) at least seven colors are necessary.

**Three small cases.** The triangular prism has nine edges and no induced matching of size two; thus nine colors are required. The five-prism has fifteen edges, every induced matching has size at most two, and therefore at least eight colors are required. The six-prism has eighteen edges, exactly two induced matchings of cardinality three, and no induced matching of cardinality four. A seven-coloring could contain at most two classes of size three and five of size two, totaling at most sixteen edges; therefore eight colors are necessary. These small induced-matching counts are independently exhaustively certified in `exhaustive.py`; the recursion enumerates **every** independent set of the fully specified edge-conflict graph, without pruning that removes admissible sets. The resulting size histograms for sizes zero upward are \((1,9)\), \((1,15,25)\), and \((1,18,57,2)\), respectively.

**Explicit upper bound.** `construct.py` supplies a direct table for \(n\in\{3,5,6,7,9,10,11,13,14\}\), each coloring using respectively \(9,8,8,7,7,7,7,7,7\) colors, and the four-column pattern
\[
((5,0,2),(4,1,3),(5,2,0),(4,3,1))
\]
provides a six-coloring whenever \(4\mid n\). Each seed is checked by comparing every pair of edges against the exact strong-coloring condition, rather than merely checking proper edge coloring.

For each remaining \(n\ge15\) with \(4\nmid n\), choose the corresponding base \(b\in\{13,14,11\}\) when \(n\equiv1,2,3\pmod4\), respectively. In each of those base columns \(0,1,2,3,4,5\), columns \(0,1\) repeat in columns \(4,5\). Insert the four-column block previously occupying columns \(2,3,4,5\), repeated \((n-b)/4\) times, immediately after column five. All strong-color conflicts are local to at most two columns' separation (with the cyclic seam interpreted in the same way). Every local block of the enlarged word already occurs in the base word or the repeated valid four-column pattern; the seam after the repeated block is unchanged because its last two columns coincide with the original last two columns at the insertion point. Hence insertion preserves strongness, providing seven colors for every remaining order. Together with the lower bounds this proves the formula.

## Verification
Run `python3 construct.py` and `python3 exhaustive.py` from the directory containing these programs. Their exact captured standard outputs are provided as `construct_output.txt` and `exhaustive_output.txt`. `construct.py` verifies direct color conflicts for every order from 3 through 100; more importantly its base tables and four-column insertion give a symbolic all-orders construction. `exhaustive.py` reconstructs the prism graph with independent vertex labels, exhaustively enumerates induced matchings for orders 3, 5, 6, independently verifies 29 test colorings, and solves the unsatisfiable strong-coloring instances \((n,k)=(3,8),(5,7),(6,7),(7,6),(9,6),(10,6)\). These finite checks support but do not replace the all-orders period-four proof and insertion argument.

## Relationship to prior work
O. Togni, *Strong chromatic index of products of graphs*, Discrete Mathematics & Theoretical Computer Science 9 (2007), studies Cartesian products, including cycles and compatible colorings. S. Dara, S. Mishra, N. Narayanan, and Z. Tuza, *Strong Edge Coloring of Cayley Graphs and Some Product Graphs*, Graphs and Combinatorics 38 (2022), §5 and its summary table, give product bounds and exact values in several cases, including cycle lengths divisible by four, triangular prism and six-prism. Their odd-cycle bounds do not establish the asserted exact formula for every odd prism, and they record the even ten-prism as a sharp seven-color example. Here the infinite parity obstruction plus the explicit finite-seed extension gives a complete all-orders formula, including the five-prism exception.

## Limitations
The theorem applies to \(C_n\square K_2\), not to arbitrary tree-cycle products or all cubic graphs. Finite enumeration alone does not establish the infinite claim. No independent external audit has been performed. An undiscovered equivalent earlier classification in unindexed literature is a residual originality risk. The period-four insertion must be interpreted for the stated base tables and not as arbitrary concatenation of colorings.

## References
[1] O. Togni, “Strong chromatic index of products of graphs,” *Discrete Mathematics & Theoretical Computer Science* 9 (2007), 47–56, https://doi.org/10.46298/dmtcs.414 .

[2] S. Dara, S. Mishra, N. Narayanan, and Z. Tuza, “Strong Edge Coloring of Cayley Graphs and Some Product Graphs,” *Graphs and Combinatorics* 38 (2022), article 51, https://doi.org/10.1007/s00373-021-02408-4 .

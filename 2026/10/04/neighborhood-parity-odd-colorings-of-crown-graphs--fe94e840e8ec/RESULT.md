# Neighborhood-parity odd colorings of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph obtained by deleting the perfect matching \(M=\{a_i b_i:1\le i\le n\}\). For the neighborhood-parity odd chromatic number of Petruševski and Škrekovski, \[\chi_o(\operatorname{Cr}_n)=\begin{cases}2,&n\text{ even},\\3,&n=3,\\4,&n\ge5\text{ odd}.\end{cases}\] The minimum colorings are completely classified. If \(n\) is even, they are exactly the two bipartition colorings with named colors. For \(n=3\), each deleted matched pair is monochromatic and the three pairs receive three distinct colors, giving \(6\) named minimum colorings. For odd \(n\ge5\), choose two deleted matched pairs; give those pairs two distinct shared colors, color all remaining vertices in the first part with a third color, and all remaining vertices in the second part with the fourth color. These are all minimum colorings, giving \(24\binom{n}{2}=12n(n-1)\) named minimum colorings, or exactly \(\binom{n}{2}\) minimum colorings up to permutation of the four colors.

## Assumptions and scope
All graphs are finite, simple, and undirected. For an integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where the deleted perfect matching is
\[
M=\{a_i b_i:1\le i\le n\}.
\]

A proper coloring is neighborhood-parity odd when, for every non-isolated vertex, some color occurs an odd number of times in its open neighborhood. Its minimum number of colors is denoted \(\chi_o\).

## Proof
Fix a proper coloring \(\varphi\) with color set \(C\). For a part \(X\in\{A,B\}\), let
\[
P_X=\{c\in C: |\varphi^{-1}(c)\cap X|\text{ is odd}\}.
\]
For the vertex \(a_i\), its neighborhood is \(B\setminus\{b_i\}\). Thus the set of colors occurring oddly in \(N(a_i)\) is exactly
\[
P_B\triangle\{\varphi(b_i)\},
\]
where \(\triangle\) denotes symmetric difference. Hence \(a_i\) fails the odd condition exactly when
\[
P_B=\{\varphi(b_i)\}.
\]
The symmetric statement holds for \(b_i\) using \(P_A\).

If \(n\) is even, then \(|P_A|\) and \(|P_B|\) are even. Therefore neither can equal a singleton, so every proper coloring is automatically odd. Since \(\operatorname{Cr}_n\) is connected and bipartite, its chromatic number is \(2\), and
\[
\chi_o(\operatorname{Cr}_n)=2.
\]
The only named proper \(2\)-colorings are the two swaps of the bipartition colors.

Now assume \(n\) is odd. Then \(|P_A|\) and \(|P_B|\) are odd. If, say, \(|P_B|=1\), its unique color occurs on at least one vertex \(b_i\), and the matched vertex \(a_i\) fails. Therefore a proper coloring is odd exactly when
\[
|P_A|\ge3\qquad\text{and}\qquad |P_B|\ge3.
\]

A basic properness constraint for crown graphs is crucial: if one color appears in both parts, then it appears exactly on one deleted matched pair \(\{a_i,b_i\}\). Indeed, if the same color occurs at \(a_i\) and \(b_j\), properness forces \(i=j\); any additional occurrence in either part would then be adjacent to the opposite member of that pair.

Suppose only three colors are available. For oddness, each part must have all three colors occurring oddly, so all three colors occur in both parts. By the preceding constraint, each is confined to one deleted matched pair. Hence \(n=3\). Conversely, when \(n=3\), coloring the three deleted matched pairs with three distinct colors is proper and odd. Therefore
\[
\chi_o(\operatorname{Cr}_3)=3,
\]
and there are \(3!=6\) named minimum colorings.

Let now \(n\ge5\) be odd. Three colors are impossible, so \(\chi_o\ge4\). A four-coloring exists: choose distinct indices \(i,j\), give \(\{a_i,b_i\}\) and \(\{a_j,b_j\}\) two shared colors, color every other vertex of \(A\) with a third color, and every other vertex of \(B\) with the fourth. In each part the three used color classes have sizes \(1,1,n-2\), all odd, so the coloring is odd. Thus \(\chi_o=4\).

It remains to classify all minimum four-colorings. Each part uses at least three colors, so the two sets of used colors have intersection size at least two. Every common color is confined to a single deleted matched pair. The intersection cannot have size four, since that would force \(n=4\). It cannot have size three, because then the part not using the remaining exclusive color would contain only the three shared vertices. Thus exactly two colors are shared, each on a distinct deleted matched pair. The two remaining colors cannot be shared, so one fills all remaining vertices of \(A\) and the other fills all remaining vertices of \(B\). This is precisely the construction above.

For named colors, choose the two shared matched indices in \(\binom n2\) ways, assign two distinct colors to them in \(4\cdot3\) ways, and assign the two remaining colors to the two parts in \(2\) ways. Hence the number of minimum colorings is
\[
24\binom n2=12n(n-1).
\]
Modulo permutation of the four colors, there is one coloring for each unordered pair of shared matched indices, so there are \(\binom n2\) color-permutation classes.

## Verification
The included checker enumerates proper colorings directly for every \(3\le n\le9\). For each palette below the claimed minimum it finds no odd coloring. At the minimum palette it compares every odd coloring with the structural classification and verifies the exact labeled counts.

The enumeration uses only properness of the crown graph and the defining neighborhood-parity test. It does not use the theorem's classification to decide whether a coloring is odd.

## Relationship to prior work
The paper introducing this graph-coloring notion defines neighborhood-parity odd coloring, shows that it can differ sharply from ordinary coloring, and focuses mainly on planar graphs. Its full text gives examples such as cycles, a kite, and complete-edge subdivisions, but targeted inspection found no crown graph or complete-bipartite-minus-matching result.

Later work develops general sparse and planar bounds for the same parameter and for the stronger proper conflict-free coloring, where a neighborhood must contain a uniquely occurring color. Those general bounds do not determine the crown graph. A recent exact proper-conflict-free computation for crown graphs gives four colors from order four onward; that stronger parameter supplies an upper bound in the odd-order crown case but does not imply the parity-sensitive lower bound here, and it differs sharply on even crowns because every proper coloring of an even crown is already neighborhood-parity odd.

## Limitations
The theorem concerns neighborhood-parity odd coloring in the sense of Petruševski and Škrekovski, not the unrelated later use of “odd chromatic number” for partitions into odd induced subgraphs. The classification is for crown graphs \(K_{n,n}-M\) with \(n\ge3\). No claim is made for arbitrary bipartite graphs or for deleting a non-perfect matching. The finite verification is corroborative only; the all-parameter statement follows from the parity proof.

## References
1. M. Petruševski, R. Škrekovski, “Colorings with neighborhood parity condition,” arXiv:2112.13710v1, 27 December 2021; Discrete Applied Mathematics 321 (2022), 385–391, DOI 10.1016/j.dam.2022.07.018.
2. J. Anderson, H. Chau, E.-K. Cho, N. Crawford, S. G. Hartke, E. Heath, O. Henderschedt, H. Kwon, Z. Zhang, “The forb-flex method for odd coloring and proper conflict-free coloring of planar graphs,” arXiv:2401.14590v1, 26 January 2024.

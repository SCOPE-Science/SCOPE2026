# Majority C-colorings of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge 2\) and \(n_i\ge 1\) for every part. A majority C-coloring is a surjective vertex coloring in which every vertex has at least half of its neighbors in its own color class. Then
\[
\overline{\chi}_{\geqslant}(G)=
\begin{cases}
2,&\text{if every }n_i\text{ is even},\\
1,&\text{otherwise}.
\end{cases}
\]
Moreover, whenever two colors are possible, every two-color majority C-coloring places exactly \(n_i/2\) vertices of each color in every part \(V_i\). Hence the number of labeled optimal colorings with palette \(\{1,2\}\) is
\[
\prod_{i=1}^{r}\binom{n_i}{n_i/2},
\]
and the number up to interchanging the two color names is one half of this product.

## Assumptions and scope
The graph is finite, simple, and complete multipartite, with at least two nonempty partite sets. The majority threshold is exactly one half of the open neighborhood, as in the definition of majority C-coloring. No assertion is made here for non-complete multipartite graphs, for a one-part edgeless graph, or for different local thresholds.

## Proof
Write \(N=\sum_{i=1}^{r}n_i\). Fix any color used by a majority C-coloring. Let \(a_i\) be the number of vertices of this color in part \(V_i\), let \(A=\sum_i a_i\) be the size of the color class, and let \(I=\{i:a_i>0\}\).

The color cannot occur in only one part. Indeed, if \(I=\{i\}\), then a vertex of that color in \(V_i\) has no same-colored neighbor, while its degree is \(N-n_i>0\).

For every \(i\in I\), a vertex of this color in \(V_i\) has exactly \(A-a_i\) same-colored neighbors and degree \(N-n_i\). The majority condition therefore gives
\[
A-a_i\ge \frac{N-n_i}{2}.
\]
Summing these inequalities over \(i\in I\) yields
\[
(|I|-1)A
\ge \frac{|I|N-\sum_{i\in I}n_i}{2}
\ge \frac{(|I|-1)N}{2}.
\]
Because \(|I|\ge2\), every used color class has size \(A\ge N/2\). Thus no majority C-coloring can use more than two colors.

Suppose two colors are used. Their class sizes sum to \(N\), so both have size exactly \(N/2\). For either color, equality must then hold throughout the displayed chain. Hence \(\sum_{i\in I}n_i=N\), so that color occurs in every part. Equality must also hold in each individual majority inequality, and therefore
\[
a_i=\frac{n_i}{2}
\]
for every \(i\). In particular every \(n_i\) is even.

Conversely, if every \(n_i\) is even, split each part into two sets of size \(n_i/2\), one for each color. A vertex in \(V_i\) then has exactly
\[
\frac{N-n_i}{2}
\]
same-colored neighbors among its \(N-n_i\) neighbors, so the majority condition holds with equality. This proves the exact value and the structural classification.

For the count, when all part sizes are even, choosing the vertices of color \(1\) independently in each part gives \(\binom{n_i}{n_i/2}\) choices in part \(V_i\), after which color \(2\) is forced. Multiplying gives the labeled count. Interchanging the two colors has no fixed coloring, so quotienting by this involution divides the count by \(2\).

## Verification
A standalone verifier independently constructs every complete-multipartite isomorphism type through order \(8\), enumerates all canonical surjective vertex colorings, and tests the majority condition directly from graph neighborhoods. It also enumerates every labeled surjective two-color assignment and checks both the exact product count and the asserted half-splitting inside every part. The replay result is:

`ALL CHECKS PASSED; multipartite_types=58; canonical_colorings=101632; valid_canonical_colorings=128; labeled_two_assignments=7968; valid_labeled_two_assignments=140; chi_two_types=7; max_order=8`

This finite computation is a stress test only. The universal statement is proved by the counting argument above.

## Relationship to prior work
Bujtás, Dettlaff, Furmańczyk, and Laskowska introduced majority C-coloring and its maximum-color parameter in *Majority C-coloring of graphs* (arXiv:2604.20752, first version 22 April 2026). Their Observation 2(v) gives the exact complete-bipartite case: \(K_{m,n}\) has value \(2\) exactly when both parts are even, and value \(1\) otherwise. The same paper explicitly identifies two-color majority C-colorings with satisfactory partitions and arbitrary-color majority C-colorings with sum satisfactory partitions, but its exact-family list does not include arbitrary complete multipartite graphs.

Earlier satisfactory-partition literature includes Shafique and Dutton, *On Satisfactory Partitioning of Graphs*, Congressus Numerantium 154 (2002), 183–194. That source discusses complete bipartite parity as a basic obstruction and develops general partitionability conditions, but does not state an arbitrary complete-multipartite classification. The theorem here extends the bipartite parity transition to every number of parts, proves that three or more majority-C colors are impossible throughout the family, and classifies and counts all optimal two-colorings.

## Limitations
The novelty comparison is bounded by the inspected majority-C and satisfactory-partition literature and targeted searches under both terminologies. Older work may use different language for the same local-majority partition condition, so an unindexed equivalent statement remains a residual literature risk. The proof itself does not depend on computation or on unproved classification input.

## References
1. Csilla Bujtás, Magda Dettlaff, Hanna Furmańczyk, Aleksandra Laskowska, *Majority C-coloring of graphs*, arXiv:2604.20752v1, 22 April 2026.
2. Khurram H. Shafique, Ronald D. Dutton, *On Satisfactory Partitioning of Graphs*, Congressus Numerantium 154 (2002), 183–194.
3. Cristina Bazgan, Zsolt Tuza, Daniel Vanderpooten, *The satisfactory partition problem*, Discrete Applied Mathematics 154 (2006), 1236–1245.

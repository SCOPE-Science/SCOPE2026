# Sparse red/blue rainbow-connected colorings of complete bipartite graphs: all minimizers and full weight enumerator

## Finding

The following theorem simultaneously determines when a complete bipartite graph has a rainbow-connected red/blue edge coloring, the minimum number of red edges, every minimum coloring, and the entire red-edge distribution.

**Theorem.** For integers \(a,b\ge2\), set \(u=\max\{a,b\}\) and \(v=\min\{a,b\}\). The labeled graph \(K_{a,b}\) has a rainbow-connected red/blue edge coloring if and only if \(u\le2^v\).

In the feasible case let \(r\) be the unique integer with
\[
\sum_{j=0}^{r-1}\binom{v}{j}<u\le\sum_{j=0}^{r}\binom{v}{j},\qquad
 t=u-\sum_{j=0}^{r-1}\binom{v}{j}.
\]
The smallest number of red edges is
\[
 m_{a,b}=\sum_{j=0}^{r-1}j\binom{v}{j}+rt.
\]
Precisely \(u!\binom{\binom{v}{r}}{t}\) labeled colorings attain this minimum. Every minimum coloring uses, as the red-incidence signatures of vertices in the larger part, all binary words of length \(v\) with weight less than \(r\), plus an arbitrary choice of \(t\) distinct words of weight \(r\), assigned bijectively to those vertices.

For all \(a,b\ge2\), including when no rainbow-connected coloring exists, the red-edge generating polynomial is
\[
 R_{a,b}(z)=\sum_{\pi\in\Pi_a}\sum_{\sigma\in\Pi_b}
\mu(\pi)\mu(\sigma)\prod_{B\in\pi}\prod_{C\in\sigma}
(1+z^{|B||C|}),
\qquad
\mu(\pi)=\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!.
\]
Here \(\Pi_k\) is the set of set partitions of a labeled \(k\)-element set. When feasible, the least exponent of \(z\) is \(m_{a,b}\) with coefficient \(u!\binom{\binom vr}{t}\). In all cases,
\[
 z^{ab}R_{a,b}(z^{-1})=R_{a,b}(z).
\]

## Assumptions and scope

All graphs are finite, simple, and undirected. Both bipartition classes have at least two labeled vertices. Red and blue are *named* colors and a coloring need not be proper. A path is rainbow when no color is repeated, and the graph is rainbow connected when every pair of vertices has a rainbow path. Thus a rainbow path has at most two edges in any red/blue coloring. Red-incidence signatures are ordinary binary vectors with coordinate \(1\) exactly at red edges. The two vertex classes may be interchanged in applying the formulas. The number of colorings treats edges as distinguished by their endpoints.

## Proof

**1. Exact signature criterion.** Write the coloring as a binary \(a\)-by-\(b\) matrix, with entry \(1\) for a red edge. Opposite-side vertices are adjacent and therefore already have a rainbow one-edge path. Two different vertices on the same side are at graph distance two; a rainbow path with two available colors must be exactly a two-edge path. Such a path exists precisely when the corresponding two matrix rows, or respectively columns, differ at some position. Hence the coloring is rainbow connected if and only if all rows are pairwise distinct *and* all columns are pairwise distinct.

**2. Feasibility and minimum size.** Put the larger class in the rows, so there are \(u\) binary words of length \(v\). Row distinction requires \(u\le2^v\); if this holds, choose the first \(u\) distinct words in increasing order of Hamming weight, arbitrarily breaking ties. Their total weight is the displayed \(m_{a,b}\), and no collection of \(u\) distinct words can have less weight, because swapping in any unchosen word of smaller weight strictly decreases the total. Equality forces inclusion of *all* words from every lower weight layer, and exactly \(t\) words from the terminal layer \(r\).

We must still check that the minimum-weight construction separates **columns**, rather than only rows. Because \(u\ge v\ge2\), the zero word belongs to every minimizing collection. If \(u=v\), then the collection consists of the zero word and \(v-1\) different unit vectors, producing one zero column and \(v-1\) mutually distinct nonzero columns. If \(u\ge v+1\), the collection contains all \(v\) unit vectors, which ensure that every two columns differ. Thus *all* minimum-weight collections separate columns, complete the existence construction, and attain the lower bound.

The choice of terminal words has \(\binom{\binom vr}{t}\) possibilities. Every such set has \(u!\) bijections to the labeled vertices of the larger class, yielding the exact optimizer count. No other minimum coloring exists by the weight exchange argument.

**3. Complete enumerator.** Let \(\pi\in\Pi_a\) partition the row labels, and \(\sigma\in\Pi_b\) partition the column labels. Impose equal signatures on rows within every block of \(\pi\) and on columns within every block of \(\sigma\). These constraints force every rectangle \(B\times C\), for \(B\in\pi\) and \(C\in\sigma\), to be monochromatic. Choosing whether that rectangle is red contributes a factor \(z^{|B||C|}\), while choosing blue contributes \(1\); therefore the full generating function for colorings respecting these equality constraints is exactly the indicated rectangle product.

For any fixed coloring, the sum of \(\mu(\pi)\) over partitions \(\pi\) whose blocks consist of equal rows equals \(1\) when all rows differ and \(0\) otherwise: this is the elementary partition-lattice identity \(\sum_{\pi\preceq\tau}\mu(\pi)=\mathbf{1}_{\{\tau=\hat0\}}\), obtained by multiplying the inclusion-exclusion identity over blocks of the equality partition \(\tau\). The analogous statement holds for column signatures, so multiplying these two indicators and exchanging finite sums gives precisely the stated double partition sum for \(R_{a,b}(z)\). Finally swapping red with blue sends a valid coloring with \(k\) red edges to one with \(ab-k\) red edges, proving the reciprocity identity.

## Verification

The standalone file `rainbow_sparse_verifier.py` directly enumerates red/blue edge assignments; it tests graph-theoretic two-edge rainbow paths rather than assuming the signature characterization. It exhaustively checks the predicted minimum and number of labeled minimizers for \((a,b)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4)\), and independently computes the full partition-sum polynomial for \((2,2),(2,3),(2,5),(3,3),(3,4),(4,4)\). Every comparison passed. The proof above supplies the infinite quantifiers; the finite checks are independent diagnostics, not an infinite proof.

For example, \(R_{2,2}(z)=4z+2z^2+4z^3\) and \(K_{3,3}\) has minimum two red edges attained in eighteen labeled red/blue colorings. No rainbow-connected two-coloring of \(K_{2,5}\) exists.

## Relationship to prior work

Barát, Boyadzhiyska, and Freschi [1] study the existence of rainbow-connecting red/blue edge-colorings under strong degree conditions, including graphs close to balanced complete bipartite graphs. Their results concern existence and large-scale density, not the minimum budget of one named color or the entire red-edge distribution for arbitrary complete bipartite graphs. Septyanto and Sugeng [2] develop *color-code* methods for rainbow connection. We explicitly use this established signature viewpoint; the weight minimization, full optimizer classification, and weighted partition-inversion enumeration stated above are the additional results. These differences concern mathematical implication, not merely differences in titles or notation.

## Limitations

The result is for two named colors and complete bipartite graphs with both classes nontrivial. It does not cover graphs with deleted edges, multiple rainbow-disjoint paths, proper edge coloring, or more than two colors. The generating polynomial is an exact finite partition sum, not an asserted polynomial-time coefficient algorithm. Finite checks cover only the listed instances. Older or unindexed work on minimum-weight separating binary arrays, sparse twin-free bipartite graphs, or multivariate surjection enumerators could conceivably subsume parts of the formula; this is a remaining bibliographic risk. No independent audit has been performed.

## References

[1] J. Barát, S. Boyadzhiyska, A. Freschi, *Rainbow connecting \(2\)-colorings of super-Dirac graphs*, arXiv:2609.11437 (first public version 2026-09-10). https://arxiv.org/abs/2609.11437 and https://arxiv.org/pdf/2609.11437v1.

[2] F. Septyanto and K. A. Sugeng, *Color code techniques in rainbow connection*, Electronic Journal of Graph Theory and Applications 6(2) (2018), 347–361, DOI:10.5614/ejgta.2018.6.2.14. Accessible full text: https://media.neliti.com/media/publications/267141-none-773a457c.pdf.

# The full star-colouring polynomial of crown graphs

## Finding

Let \(n\ge3\) be an integer, and let \(H_n=K_{n,n}-M_n\) be the crown graph, with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\) and edges \(a_ib_j\) precisely when \(i\ne j\). A *star colouring* is a proper vertex colouring with no path of four distinct vertices using just two colours. Colourings equivalent under a permutation of their colour names are identified with partitions into nonempty colour classes.

Write \(c_{n,k}\) for the number of partitions of \(V(H_n)\) into exactly \(k\) classes that give a star colouring. With the conventions that Stirling numbers of the second kind count set partitions, and out-of-range binomial coefficients are zero, the **complete star-colouring profile** is

\[
c_{n,k}=0\quad(k<n\text{ or }k>2n),\qquad
c_{n,n+j}=2\left\{\!\begin{matrix}n+1\\j+1\end{matrix}\!\right\}
-\binom{n}{j}+\binom{n}{2}\binom{n-2}{j},\quad 0\le j\le n.
\]

Consequently the ordinary polynomial counting star colourings from a palette of \(q\) named colours (unused colours permitted) is

\[
\operatorname{SC}_{H_n}(q)=\sum_{j=0}^{n}c_{n,n+j}(q)_{n+j},
\qquad (q)_k=q(q-1)\cdots(q-k+1).
\]

A stronger structural statement underlies these formulas. Every star-colour partition comes from choosing a subset \(P\subseteq\{1,\ldots,n\}\) of *paired indices*, assigning one separate mixed colour class \(\{a_i,b_i\}\) for each \(i\in P\), and independently partitioning the remaining \(a\)-vertices and \(b\)-vertices according to one of two mutually exclusive possibilities:

1. At least one of the two remaining side partitions is discrete (all its classes are singletons).
2. Both side partitions have exactly the same one block of size two and are otherwise discrete.

In particular, the previously known star chromatic number \(\chi_s(H_n)=n\) admits a sharpened exact count: there are precisely \(1+\binom n2\) optimal unlabelled colour partitions, or \(n!\bigl(1+\binom n2\bigr)\) proper star colourings using a prescribed set of exactly \(n\) named colours. Their only types are the all-paired partition and the \(\binom n2\) partitions that replace the two mixed matched-pair colours at indices \(i,j\) by the two monochromatic classes \(\{a_i,a_j\}\), \(\{b_i,b_j\}\).

## Assumptions and scope

All graphs are finite, simple, and undirected. The star condition excludes every two-coloured path of length three, whether or not the path is induced. The ground vertices are distinguished and the two bipartition sides are fixed; the formula counts partitions of this fixed vertex set, not orbits under graph automorphisms. The polynomial \(\operatorname{SC}_{H_n}(q)\) counts functions from the vertices to a prescribed \(q\)-element palette and includes non-surjective functions. The claim holds for every integer \(n\ge3\) and every nonnegative integer palette size \(q\). By polynomial identity it also defines a polynomial in an indeterminate \(q\).

## Proof

**1. Proper colour classes.** If a proper colour class meets both sides, it contains some \(a_i,b_j\). Properness requires \(i=j\), and then no further vertex can belong to the class: each \(a_h\), \(h\ne i\), is adjacent to \(b_i\), and each \(b_h\), \(h\ne i\), is adjacent to \(a_i\). Thus every mixed class is exactly a deleted-matching pair \(\{a_i,b_i\}\), with disjoint indices \(P\). The remaining indices \(U\) occur in two ordinary set partitions \(\pi_A,\pi_B\), one on each side.

**2. Exact two-class obstruction.** A pure class \(X\subseteq A\) and a pure class \(Y\subseteq B\) induce a complete bipartite graph with only those matched edges removed whose indices belong to both associated index sets. If one class is a singleton, the two-coloured graph is a star or a collection of isolated vertices. If both have at least two vertices, it is a star forest *if and only if* their index sets coincide and both have size two. The exceptional graph is \(2K_2\). To prove necessity in every other case, choose two distinct indices from each index set such that the resulting two-element subsets are unequal. Such a choice exists unless both original sets are exactly the same two-element set. The induced four-vertex bipartite graph is \(K_{2,2}\) with at most one edge removed, hence contains a path of length three. This is forbidden in a star colouring. Mixed classes cause no additional restriction: two distinct paired classes induce \(2K_2\), and a mixed class together with a pure class induces a star (possibly with isolates).

It follows that if neither side partition is discrete, both possess non-singleton blocks. Every non-singleton block on one side must equal every non-singleton block on the other side and must have size two. Because distinct blocks within a partition are disjoint, both sides have precisely the same unique two-element block, with all remaining indices singleton. Conversely, every partition in either of the two stated forms satisfies the star condition by the preceding two-class check. This proves the characterization without assuming a colouring uses the fewest possible colours.

**3. Enumerating partitions.** Fix \(r=|U|\) and \(s=n-r=|P|\). There are \(\binom nr\) choices of \(U\). For \(r=0\), the all-paired colouring contributes one partition with \(n\) classes. For \(r\ge1\), when one side is discrete and the other has \(b\) blocks, there are \(2\left\{\!\begin{matrix}r\\b\end{matrix}\!\right\}\) choices, each using \(s+r+b=n+b\) classes. The case where both sides are discrete has been counted twice; subtract one partition with \(n+r\) classes. When neither side is discrete, the exceptional common two-block can be chosen in \(\binom r2\) ways; it contributes \(s+2(r-1)=n+r-2\) classes. Hence the class-number generating polynomial equals

\[
F_n(z)=z^n+\sum_{r=1}^n\binom nr\left[
2\sum_{b=1}^r\left\{\!\begin{matrix}r\\b\end{matrix}\!\right\}z^{n+b}
-z^{n+r}+\binom r2z^{n+r-2}\right].
\]

Partitioning \(\{1,\ldots,n+1\}\) according to the block containing the final label proves the elementary identity
\[
\sum_{r=b}^n\binom nr\left\{\!\begin{matrix}r\\b\end{matrix}\!\right\}
=\left\{\!\begin{matrix}n+1\\b+1\end{matrix}\!\right\}.
\]

Also \(\binom nr\binom r2=\binom n2\binom{n-2}{r-2}\). Therefore
\[
F_n(z)=z^n\left[
2\sum_{b=1}^n\left\{\!\begin{matrix}n+1\\b+1\end{matrix}\!\right\}z^b
+2-(1+z)^n+\binom n2(1+z)^{n-2}\right].
\]

Extracting the constant term and the coefficients of the remaining powers \(z^j\) gives exactly the announced formula (for \(j=0\), use \(\left\{\!\begin{matrix}n+1\\1\end{matrix}\!\right\}=1\)). Every valid partition has between \(n\) and \(2n\) classes, and all intermediate counts are positive because splitting colour classes preserves the star property. Every partition with \(k\) nonempty classes gives exactly \((q)_k\) distinct colourings from a fixed palette of \(q\) named colours. This proves the star chromatic polynomial.

**4. The minimum and its multiplicity.** If \(r>0\) and at least one side is discrete, there are at least \(n+1\) classes. In the exceptional common-two-block case there are \(n+r-2\) classes, minimized only at \(r=2\), when the total equals \(n\). The case \(r=0\) also uses \(n\) classes. Therefore there is one all-paired optimal partition and one for each of the \(\binom n2\) two-index choices, with no others. Choosing distinct names for the \(n\) classes multiplies this count by \(n!\). This also establishes \(\chi_s(H_n)=n\) independently of any external minimum-colour assertion.

## Verification

The standalone file `verify.py` constructs each crown-graph adjacency matrix directly and enumerates every proper set partition by a restricted-growth recursion, without imposing the structural theorem. It then explicitly generates all simple four-vertex paths and rejects every partition in which such a path uses only two colours. Comparing the resulting class counts against independent exact Stirling-number arithmetic gives full agreement for \(2\le n\le7\): 1,189,120 proper colour partitions were examined in total. For the stated domain \(3\le n\le7\), the observed optimum counts are respectively \(4,7,11,16,22\). Additional arithmetic checks compare the two algebraic coefficient forms and the optimal counts for \(3\le n\le50\). The command is `python3 verify.py`; `verify_output.txt` records its stdout. These finite checks are not substituted for the proof for arbitrary \(n\).

## Relationship to prior work

Mary, Bibi, and Julietterayan (2017, Theorem 4.11) already report the exact star chromatic number \(\chi_s(H_n)=n\) for crown graphs. The new assertion is **not** that scalar equality; it is the complete number of star-colour partitions for every class count, an explicit palette-colouring polynomial, and a full structural census of optimal partitions. Their statement and example supply one optimum but not the additional \(\binom n2\) optimal partition types or the all-colour Stirling profile.

Shalu M. A. and Antony (2022 journal article; arXiv:2309.04291v1 released in 2023) develop general bounds and structural questions for star colourings of regular graphs, including uniqueness questions; those degree-level results do not enumerate crown-graph colour partitions. Bu and collaborators (arXiv:2105.06641v1) analyze sparse-graph existence bounds under maximum-average-degree restrictions; those do not provide the present dense-family counting identity. Star colouring here is *vertex* colouring, not star edge colouring. The ordinary chromatic polynomial, strong-odd colouring, and conflict-free colouring are different invariants and do not imply these counts.

## Limitations

A scholarly priority search cannot certify absolute novelty: equivalent calculations under the terms *colour partitions with no bicoloured four-vertex path*, *star chromatic polynomial*, or *crown graphs* may be unindexed. The 2017 published minimum-colour theorem is explicitly treated as prior knowledge. The result is a closed enumeration for this graph family, not a general formula for arbitrary graphs. No independently conducted scientific validation has been performed.

## References

1. L. Jethruth Emelda Mary, K. Ameenal Bibi, and A. Lydia Mary Julietterayan, *A Study on Star Chromatic Number of Some Special Classes of Graphs*, Global Journal of Pure and Applied Mathematics **13**(9) (2017), 4569–4593, Theorem 4.11. https://www.ripublication.com/gjpam17/gjpamv13n9_15.pdf
2. Shalu M. A. and Cyriac Antony, *Star Colouring of Bounded Degree Graphs and Regular Graphs*, Discrete Mathematics **345**(6) (2022), article 112850; publicly available arXiv:2309.04291v1 copy first posted 2023-09-08. https://arxiv.org/abs/2309.04291
3. Yuehua Bu, Daniel W. Cranston, Mickaël Montassier, André Raspaud, and Weifan Wang, *Star coloring of sparse graphs*, arXiv:2105.06641v1 (repository upload dated 2021-05-14). https://arxiv.org/abs/2105.06641

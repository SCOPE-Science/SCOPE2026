# Degree spectrum and isolated simple vertices of complete-bipartite graphical zonotopes

## Finding
For all integers \(a,b\ge2\), the one-skeleton of the graphical zonotope of \(K_{a,b}\) has an explicit complete degree-generating polynomial. In particular, its simple vertices (vertices of degree exactly \(a+b-1\)) are pairwise nonadjacent, and their exact number is
\[
S(a,b)=2\sum_{j=1}^{\min(a,b)-1}(a)_{\underline j}(b)_{\underline j}
+\mathbf1_{a>b}(a)_{\underline{b-1}}b!(2^{a-b+1}-2)
+\mathbf1_{b>a}(b)_{\underline{a-1}}a!(2^{b-a+1}-2).
\]
Here \((t)_{\underline j}=t!/(t-j)!\), and \(\mathbf1_P\) is one or zero according as \(P\) holds or fails. The vertices of maximum degree \(ab\) number exactly \(2^a+2^b-2\). For \(a=b=n\),
\[
S(n,n)=2(n!)^2\sum_{j=1}^{n-1}\frac1{(j!)^2},
\]
and the proportion of simple vertices tends to zero as \(n\to\infty\).

## Assumptions and scope
Let \(A,B\) be distinct labeled sets of sizes \(a,b\). Let \(G=K_{a,b}\) on \(A\sqcup B\). Its graphical zonotope is the Minkowski sum of the segments \([e_x,e_y]\) for all \(x\in A,y\in B\); it has dimension \(a+b-1\). Vertices correspond to acyclic orientations of \(G\). The one-skeleton has an edge exactly when one graph edge may be reversed without creating a directed cycle. This is the conventional (unoriented, unweighted) graph-theoretic vertex degree. The two part sets remain labeled; vertices are not quotient by graph automorphisms.

Every acyclic orientation has a unique alternating nonempty ordered partition \(B_1|\cdots|B_r\) of \(A\sqcup B\) into monochromatic blocks, with \(r\ge2\), such that edges point from earlier to later blocks. To see uniqueness, in the binary orientation matrix the neighborhoods of rows are nested: otherwise a directed four-cycle is present. The distinct row types (and corresponding column types) determine a unique alternating sequence of equal-neighborhood blocks. This is the standard lonesum-matrix or alternating-block description.

For a block-size sequence \(s_i=|B_i|\), define \(\varepsilon\in\{A,B\}\) as its initial color. Let \(\mathcal C_{a,b}(\varepsilon,r)\) be the set of vectors \((s_1,\ldots,s_r)\) of positive integers whose alternating-color sums are \(a\) and \(b\). The entire degree polynomial is
\[
D_{a,b}(u)=\sum_{\varepsilon\in\{A,B\}}\sum_{r=2}^{a+b}
 \sum_{s\in\mathcal C_{a,b}(\varepsilon,r)}
 \frac{a!b!}{\prod_i s_i!}\,u^{\sum_{i=1}^{r-1}s_is_{i+1}}.
\]
All coefficients are nonnegative integers. The polynomial enumerates *all* labeled acyclic orientations, one per zonotope vertex.

## Proof
**Local flip rule.** An oriented edge \(x\to y\) is reversible while preserving acyclicity if and only if there is no other directed path from \(x\) to \(y\). If \(x,y\) belong to consecutive blocks, no such path exists: any intermediate directed edge advances strictly in block index. If they belong to nonconsecutive blocks, an intermediate vertex in the block directly between them has the needed opposite color, giving a directed path of length two from \(x\) to \(y\). Thus exactly the cross edges between consecutive blocks are flippable, and the degree is \(\sum_{i=1}^{r-1}s_is_{i+1}\). For fixed sizes, arbitrary internal label assignments give \(a!b!/\prod_i s_i!\) orientations. Summing yields the polynomial.

**Minimum degree and simple-block criterion.** Write \(d=a+b-1\). Expanding adjacent products yields the identity
\[
\deg(O)-d=\sum_{i=2}^{r-1}(s_i-1)
 +\sum_{i=1}^{r-1}(s_i-1)(s_{i+1}-1).
\]
Both summands are nonnegative. Hence equality holds exactly when every internal block is a singleton (for then all adjacent products of block-size excesses vanish). The two-block case has degree \(ab>d\), since \(a,b\ge2\). A three-block sequence with a singleton internal block is infeasible, because that block is the only block of its color and both parts have size at least two. Thus every simple orientation has at least four blocks, and conversely every valid alternating sequence with at least four blocks and singleton interior blocks is simple.

**Count.** For an even number \(r=2k\ge4\) of blocks, there are \(k-1\) singleton internal blocks of each color. After choosing and ordering those labels, the remaining labels of each color fill its one exterior block. The two possible starting colors give \(2(a)_{\underline{k-1}}(b)_{\underline{k-1}}\) orientations. Sum over \(1\le k-1\le\min(a,b)-1\). For odd \(r=2k+1\ge5\) starting and ending in color \(A\), the \(k\) blocks of color \(B\) are internal singletons, so necessarily \(k=b\) and \(a>b\). Choose the ordered \(b-1\) internal \(A\)-labels, order all \(b\) labels of \(B\), and split the remaining \(a-b+1\) labeled \(A\)-elements between its two nonempty exterior blocks: \(2^{a-b+1}-2\) choices. This gives the second term. Starting with color \(B\) gives the third. This exhausts all simple orientations.

**No adjacent simple vertices.** In a simple sequence the internal blocks are singletons and \(r\ge4\). A legal flip across two internal consecutive singleton blocks exchanges their order; each new singleton merges with its outer neighboring block of the same color. If \(r=4\), the result has just two blocks, which is nonsimple. If \(r\ge5\), at least one merged block is interior and has size at least two, which is nonsimple. A flip at either endpoint of the sequence exchanges one element of the exterior block with the adjacent internal singleton; the moved exterior element then merges with the next internal singleton, producing an interior block of size at least two. Every legal move out of a simple configuration therefore reaches a nonsimple one, proving the simple vertices form an independent vertex set.

**Maximum degree.** There are \(ab\) underlying graph edges, so \(\deg(O)\le ab\). Equality means every pair of opposite-colored vertices belongs to consecutive blocks. Such a block sequence has at most three blocks. Two-block sequences contribute two orientations. Three-block sequences begin/end in one color and have an arbitrary proper nonempty split of that color; the two alternatives contribute \(2^a-2\) and \(2^b-2\). Hence there are \(2^a+2^b-2\) maximum-degree orientations.

**Balanced sparsity.** Setting \(a=b=n\) removes the odd-block terms in the simple-count formula. The known number \(N_n\) of acyclic orientations of \(K_{n,n}\) is the negative-index poly-Bernoulli number
\[
N_n=\sum_{k=0}^n(k!)^2\left\{{n+1\atop k+1}\right\}^2,
\]
where brackets denote Stirling numbers of the second kind. The summands for \(k=n\) and \(k=n-1\) alone give \(N_n\ge(n!)^2\bigl(1+(n+1)^2/4\bigr)\). But \(S(n,n)\le2(n!)^2\sum_{j=1}^{\infty}1/(j!)^2\), with a convergent series. Thus \(S(n,n)/N_n=O(n^{-2})\to0\).

## Verification
The accompanying Python verifier enumerates all orientations as binary directed-edge masks, detects acyclicity by depth-first search, calculates every legal edge reversal, and compares degree multiplicities against the alternating-block polynomial for every \(1\le a\le b\le4\). It also checks that simple orientations never neighbor one another. An independently implemented C++17 verifier enumerates binary matrices with nested row neighborhoods, recomputes flips and compares degree histograms and simple counts for \(K_{1,4}\), \(K_{2,2}\), \(K_{2,3}\), \(K_{3,3}\), \(K_{4,4}\), and \(K_{4,5}\). Both checks pass. The proofs are general; finite enumeration is corroboration only. Explicit cases: \(K_{2,2}\) has 14 vertices and 8 simple ones, \(K_{3,3}\) has 230 and 90, \(K_{4,4}\) has 6902 and 1472, \(K_{4,5}\) has 41506 and 6280.

## Relationship to prior work
The poly-Bernoulli enumeration, alternating-block representation, and flippability criterion for a fixed edge in an acyclic orientation of \(K_{a,b}\) were established by Cameron, Glass, Rekvényi, and Schumacher (2014), especially their Section 4 and Theorem 4.6. The local-degree identity therefore refines, rather than replaces, this known criterion. Grujić (2016) determines general graphical-zonotope face enumerators, covering in particular totals of edges but not explicit distributions by vertex degree. Chapoton and Pilaud (2022) give a broader ordered-partition description of complete multipartite graphical zonotopes, from which local incidences can also be derived. The focus here is the closed all-parameter number of simple vertices, their pairwise nonadjacency, the full degree multiplicities and their balanced sparsity. The latter are not claimed to follow from a previously unknown orientation model.

## Limitations
This is a self-contained mathematical argument with finite checks, but no independent scholarly audit has been performed. The literature inspection did not establish exhaustive novelty against all historical/unindexed papers on simplicial chambers of graphic arrangements. The full degree polynomial is a direct refinement of known blocks and the known one-edge flippability criterion; only its explicit enumeration and the simplicial-vertex consequences are candidate new material. The balanced estimate is an upper bound, not an asymptotically sharp formula for the proportion of simple vertices.

## References
1. P. J. Cameron, D. C. Glass, D. Rekvényi, S. Schumacher, *Acyclic orientations and poly-Bernoulli numbers* (2014), arXiv:1412.3685, https://arxiv.org/abs/1412.3685 .
2. V. Grujić, *Counting faces of graphical zonotopes* (2016), arXiv:1604.06931, https://arxiv.org/abs/1604.06931 .
3. F. Chapoton, V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, and associahedra* (2022 preprint), arXiv:2201.06896, https://arxiv.org/abs/2201.06896 .

# A collision law for two-types over maximal multipartite parameter graphs in Henson structures

## Finding
Let \(r\ge4\), and let \(H_{r+1}\) be the countable universal homogeneous \(K_{r+1}\)-free graph. Name individually the vertices of the induced complete \(r\)-partite graph \(P=K_{n_1,\ldots,n_r}\), where all \(n_i\ge1\) and \(N=\sum_i n_i\). A **pair type** means a complete type of an ordered pair \((x,y)\), with \(x\ne y\) and neither coordinate among the named parameters. Write \(T_{\not\sim}\) and \(T_{\sim}\) for the numbers of pair types with, respectively, \(\neg E(x,y)\) and \(E(x,y)\).

Put
\[
U=2^N-\prod_{i=1}^r(2^{n_i}-1),\qquad
B=\sum_{i=1}^r\prod_{j\ne i}(4^{n_j}-3^{n_j}).
\]
Then the **exact orientation-refined spectrum** is
\[
\boxed{T_{\not\sim}=U^2,\qquad T_{\sim}=U^2-B,\qquad T_2=2U^2-B.}
\]
Thus the fraction \(\alpha=T_{\sim}/T_2\) of all such complete pair types with adjacent coordinates is \((U^2-B)/(2U^2-B)\).

For a fixed \(r\ge4\), suppose \(\min_i n_i\to\infty\) along any sequence of size vectors. Define
\[
p_i=2^{-n_i},\quad s=\sum_i p_i,\quad
\beta=\frac{\sum_i p_i^2}{s^2},\quad
\varepsilon=s+(3/4)^{\min_i n_i}.
\]
Then, **uniformly over the relative part sizes**,
\[
\boxed{\alpha=\frac{1-\beta}{2-\beta}+O_r(\varepsilon).}
\]
Equivalently, if \(q_i=p_i/s\), the leading adjacency fraction is the transform \((1-\sum q_i^2)/(2-\sum q_i^2)\) of the collision probability of two independent missing-part labels. The sharp asymptotic upper envelope is \((r-1)/(2r-1)\), attained when all parts have equal size. In that balanced case,
\[
\boxed{\lim_{n\to\infty}\alpha(K_{n,\ldots,n})=\frac{r-1}{2r-1}.}
\]
If one part becomes arbitrarily smaller than every other part, the adjacency fraction tends to zero. Conversely, asymptotic attainment of the upper envelope forces all part sizes to be equal eventually (for fixed \(r\)).

## Assumptions and scope
Graphs are undirected, simple, loopless and induced; the parts of \(P\) are individually named vertex sets, not merely unnamed orbits. The \(n_i\) are positive integers and \(r\ge4\). The total spectrum excludes equality types, points equal to named parameters, and repeated coordinates. No probabilistic sampling of random vertices of \(H_{r+1}\) is asserted: fractions refer to the **finite set of complete types** with equal weight. The asymptotic statements keep \(r\) fixed and require every \(n_i\) to diverge.

## Proof
**Extension and type correspondence.** A finite graph containing \(P\) realizes a distinct complete tuple type over \(P\) for each distinct labelled adjacency diagram precisely when it is \(K_{r+1}\)-free. Indeed, \(H_{r+1}\) contains every such finite graph as an induced subgraph, is homogeneous over \(P\), and its theory eliminates quantifiers (Henson 1971, Theorem 2.3; Conant 2014, Section 3). There are no additional type identifications because each vertex of \(P\) is named and \(x,y\) are ordered.

**Admissible one-point neighborhoods.** If \(S\subseteq P\) is the set of named neighbors of a new point, the extension is \(K_{r+1}\)-free exactly when \(S\) contains no \(K_r\). A complete \(r\)-partite graph contains \(K_r\) in \(S\) exactly when \(S\) meets every one of the \(r\) parts. Among \(2^N\) subsets, exactly \(\prod_i(2^{n_i}-1)\) meet every part. There are therefore exactly \(U\) possible single-coordinate neighborhoods.

**Nonadjacent pairs.** When \(x,y\) are not adjacent, no forbidden clique can contain both. The admissible neighborhoods of the two points can be selected independently, giving \(T_{\not\sim}=U^2\).

**Adjacent pairs and the unique bad part.** When \(x,y\) are adjacent, the only possible new forbidden cliques not already excluded by individual admissibility contain \(x,y\) and a \(K_{r-1}\) of common named neighbors. Each individual neighborhood misses at least one part. Therefore the common neighborhood meets at most \(r-1\) parts, and the pair fails precisely when it meets exactly \(r-1\) parts. Call the sole missing part \(i\). Since both individual neighborhoods meet every other part, individual admissibility forces *both neighborhoods to be empty in part \(i\)*. For any other part \(j\), their intersection must be nonempty. Labelling each parameter vertex by neither, only \(x\), only \(y\), or both gives \(4^{n_j}-3^{n_j}\) possibilities with nonempty intersection. Thus exactly \(\prod_{j\ne i}(4^{n_j}-3^{n_j})\) pairs are bad with missing part \(i\). The events for distinct \(i\) are disjoint, so the bad count is \(B\), whence \(T_{\sim}=U^2-B\).

**Uniform collision asymptotic.** Set \(p_i=2^{-n_i}\) and \(s=\sum p_i\). With fixed \(r\), inclusion-exclusion gives
\[
U=2^N\left(1-\prod_i(1-p_i)\right)
=2^N s(1+O_r(s)).
\]
Also, factoring \(4^N\) out of \(B\) yields
\[
B=4^N\sum_i p_i^2\prod_{j\ne i}\left(1-(3/4)^{n_j}\right)
=4^N\left(\sum_i p_i^2\right)
\left(1+O_r((3/4)^{\min_j n_j})\right).
\]
Since \(1/r\le\beta=\sum p_i^2/s^2\le1\), division yields \(B/U^2=\beta+O_r(\varepsilon)\). The rational function \(z\mapsto(1-z)/(2-z)\) is Lipschitz on a neighborhood of \([1/r,1]\), so the stated uniform estimate follows.

Cauchy--Schwarz gives \(\beta\ge1/r\), with equality only when all \(p_i\) agree. If \(\alpha\) approaches the upper envelope, the uniform approximation forces \(\beta\to1/r\), hence \(p_i/p_j\to1\) for every pair. Because \(p_i/p_j=2^{n_j-n_i}\) with integral exponents, each difference \(n_i-n_j\) must then eventually be zero. Conversely, equal part sizes realize the envelope. If one \(p_i/s\to1\), then \(\beta\to1\) and \(\alpha\to0\). This completes the proof.

## Verification
Run `python3 verification/check_counts.py` with Python 3 and no nonstandard packages. The checker independently constructs each finite adjacency graph and checks all \((r+1)\)-cliques directly for 41 size vectors with \(2\le r\le4\) and total parameter size at most six; it compares the number of valid nonedges and edges against the closed formulas, including all \(r=4\) instances in that range. It additionally prints the exact count and adjacency ratio in balanced examples. Finite tests do not prove the unbounded theorem; the preceding proof does.

## Relationship to prior work
Henson's construction establishes universal homogeneity and the forbidden-clique extension property, which make the type problem well-defined. Conant develops optimal graph-type realizations and dividing/forking, not the multipartite two-type census. A previously established general one-type count for forbidden-clique homogeneous graphs covers the \(U\) term but not the exact pair correction or its collision law. A previous explicit general formula for two-types in the four-clique-free homogeneous graph covers the lower forbidden-clique case; **this finding explicitly restricts to \(r\ge4\), i.e., forbidden cliques of order at least five**. The two-point obstruction's unique-bad-part classification and its asymptotic collision law are the assertions here, not homogeneity, quantifier elimination, or one-point realization.

## Limitations
This is a restricted complete-multipartite parameter family, not a formula for arbitrary finite parameter graphs. It concerns ordered pairs of distinct new vertices and equal weighting of realized types, not relative frequencies of randomly sampled ambient vertices. The asymptotics require fixed \(r\) and all part sizes tending to infinity. No theorem of independent priority or independent verification is claimed. General graph-encoding results may yield related counts through further computation; an equivalent explicit enumeration in unindexed specialized literature remains possible.

## References
- C. Ward Henson, *A family of countable homogeneous graphs*, Pacific Journal of Mathematics **38** (1971), 69--83, especially Section 2, Theorem 2.3. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-s.pdf ; DOI: 10.2140/pjm.1971.38.69.
- Gabriel Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570v1, first posted 2014-01-08, especially Section 3, Proposition 3.4. https://arxiv.org/html/1401.1570v1 .

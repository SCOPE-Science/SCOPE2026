# Rigidity of maximum induced matchings and optimal strong edge colorings of hypercubes

## Finding

For every integer \(d\geq3\), the binary hypercube \(Q_d\) has **exactly \(2d\) maximum induced matchings**. For each coordinate \(i\in\{1,\ldots,d\}\) and parity \(p\in\{0,1\}\), put
\[
M_{i,p}:=\bigl\{\{x,x\oplus e_i\}:x_i=0,\ \sum_{j\ne i}x_j\equiv p\pmod 2\bigr\}.
\]
These \(2d\) sets, and no others, are the maximum induced matchings. Each has exactly \(2^{d-2}\) edges. They are pairwise edge-disjoint and partition the entire edge set of \(Q_d\).

Consequently, the strong chromatic index is the previously known value \(\chi'_s(Q_d)=2d\), **and its optimal strong edge coloring is unique up to permuting color names**: the color classes must be exactly the \(M_{i,p}\). The exchange graph whose vertices are maximum induced matchings, with adjacency defined by replacing one edge while preserving maximum induced-matching status, consists of \(2d\) isolated vertices. For completeness, the two-dimensional cube also has exactly four maximum induced matchings (all singleton edges) and a unique optimal four-color strong edge coloring, but its single-edge exchange graph is complete rather than discrete.

The maximum cardinality \(2^{d-2}\) and the strong chromatic index \(2d\) were previously known. The claim here is the exhaustive equality classification and the resulting uniqueness and frozen-exchange consequences.

## Assumptions and scope

The graph \(Q_d\) has vertex set \(\{0,1\}^d\); two vertices are adjacent if and only if they differ in exactly one coordinate. Here \(e_i\) is the unit vector in coordinate \(i\), \(\oplus\) denotes coordinatewise addition modulo two, and parity is computed modulo two. An *induced matching* is an edge set whose endpoints induce precisely those edges, with no further adjacency between endpoints of different selected edges. A *strong edge coloring* partitions edges into induced matchings. The colors are labels: uniqueness is asserted after disregarding relabeling of those labels, but not after quotienting the graph by automorphisms. The result covers every \(d\ge3\) without assumptions on algorithms or computations.

## Proof

**1. Bipartite spectral bound.** Let \(U\) and \(V\) denote the even- and odd-parity vertices. Both have size \(N=2^{d-1}\). Let \(T:\mathbb R^V\to\mathbb R^U\) be the bipartite adjacency operator, \((Tg)(u)=\sum_{v\sim u}g(v)\). It satisfies \(T\mathbf1_V=d\mathbf1_U\) and \(T^*\mathbf1_U=d\mathbf1_V\). On the subspace perpendicular to constants, the operator norm is \(d-2\) for \(d\ge3\). Indeed, the Walsh characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) diagonalize the full hypercube adjacency matrix, with eigenvalues \(d-2|S|\); parity restriction identifies complementary Walsh levels, and the largest nontrivial singular value is \(d-2\).

Let \(M\) be any induced matching of size \(k\), and let \(A\subseteq U\), \(B\subseteq V\) be its endpoint sets. Then \(|A|=|B|=k\) and the number of edges from \(A\) to \(B\) is exactly \(k\). Define centered indicator vectors \(a=\mathbf1_A-(k/N)\mathbf1_U\), \(b=\mathbf1_B-(k/N)\mathbf1_V\), each of squared norm \(k(1-k/N)\). The singular-value bound gives
\[
 k=\langle\mathbf1_A,T\mathbf1_B\rangle
 =\frac{dk^2}{N}+\langle a,Tb\rangle
 \ge \frac{dk^2}{N}-(d-2)k\left(1-\frac{k}{N}\right)
 =\frac{(2d-2)k^2}{N}-(d-2)k.
\]
For nonempty \(M\), division by \(k(d-1)\) yields \(k\le N/2=2^{d-2}\).

**2. Attaining the bound.** Fix \(i,p\). The set \(M_{i,p}\) comprises all edges in direction \(i\) on which the remaining \(d-1\) coordinates have parity \(p\). Its size is \(2^{d-2}\). Distinct selected edges have distinct non-\(i\) coordinate strings with the same parity and therefore differ in at least two of those coordinates. Their endpoints cannot be adjacent. Thus \(M_{i,p}\) is induced and attains the bound.

**3. Rigidity in the equality case.** Suppose \(|M|=N/2\). Then the inequality in step 1 must be an equality. Put \(F=2a\) on \(U\), and \(G=2b\) on \(V\). Both take only the values \(\pm1\). Equality in the operator-norm and Cauchy–Schwarz inequalities forces \(F\) to lie in the nonconstant singular subspace of singular value \(d-2\), and \(G=-(d-2)^{-1}T^*F\).

For \(d\ge3\), that singular subspace on \(U\) is exactly the span of the \(d\) coordinate characters \(\chi_i(x)=(-1)^{x_i}\). To see this, the Walsh levels with adjacency eigenvalues of absolute value \(d-2\) have sizes \(1\) and \(d-1\); their restrictions to \(U\) agree in pairs because the full-parity character is \(+1\) there. Hence for real coefficients \(c_i\),
\[
F(u)=\sum_{i=1}^d c_i\chi_i(u)\quad(u\in U).
\]
Since \(T^*\chi_i|_U=(d-2)\chi_i|_V\), the same coefficients satisfy
\[
G(v)=-\sum_{i=1}^d c_i\chi_i(v)\quad(v\in V).
\]
Together, \(|F|=|G|=1\) imply that the real linear form \(L(z)=\sum_i c_i z_i\) has absolute value one on **all** \(z\in\{\pm1\}^d\). Squaring gives
\[
1=L(z)^2=\sum_i c_i^2+2\sum_{i<j}c_ic_jz_iz_j.
\]
Uniqueness of Fourier coefficients on the full Boolean cube gives \(\sum_i c_i^2=1\) and \(c_ic_j=0\) for all \(i\ne j\). Thus exactly one coefficient is \(+1\) or \(-1\); say \(F=\epsilon\chi_i\), \(G=-\epsilon\chi_i\). Consequently, \(A\) is the set of even vertices with fixed \(i\)-th bit, and \(B\) is the set of odd vertices with the opposite \(i\)-th bit. The only edges between \(A\) and \(B\) flip coordinate \(i\), so \(M=M_{i,p}\) for one of the two parities \(p\). This proves that there are precisely \(2d\) maximum matchings.

**4. Coloring and exchange consequences.** For a fixed direction \(i\), the classes \(M_{i,0}\) and \(M_{i,1}\) partition its \(2^{d-1}\) edges. Different directions have disjoint edge sets. Thus all \(2d\) classes partition the \(d2^{d-1}\) hypercube edges. Every strong edge coloring has at least \(d2^{d-1}/2^{d-2}=2d\) colors. If it uses exactly \(2d\), every class has the maximum possible cardinality and must be one of the exactly \(2d\) described matchings. This proves uniqueness up to color names. Different maxima are edge-disjoint, so for \(d\ge3\), when each has at least two edges, they cannot differ by only one edge. The maximum-matching exchange graph therefore has no edges.

**5. Small boundary.** For \(d=2\), \(Q_2=C_4\) and every edge is a singleton maximum induced matching; all four classes are canonical and all can exchange to another by replacing that one edge. The one-dimensional graph \(Q_1=K_2\) is excluded from the \(2d\) classification because it has only one edge.

## Verification

The all-dimensional proof is symbolic and does not extrapolate from computation. Executing `python verify_cubes.py` exhaustively enumerates every maximum induced matching in dimensions \(2,3,4,5\), independently testing edge-pair incompatibility against the coordinate-parity construction. The outputs report \(4,6,8,10\) maximum matchings, respectively. `python verify_vertices.py` performs a distinct exhaustive census by enumerating vertex supports inducing a one-regular subgraph on exactly half the cube vertices for dimensions \(2,3,4\), recovering the same canonical families. Both programs are self-contained and use the Python standard library. These checks test small instances only; they are supplementary to the Walsh-character proof.

## Relationship to prior work

Dabrowski's 2012 thesis, §4.3.2 and Theorem 41, proves the optimal **size** \(2^{d-2}\) and gives one coordinate-parity construction, but its hypercube section does not enumerate or characterize all maximizers. Dabrowski, Demange, and Lozin (2013) study the maximum induced matching problem in bipartite graphs and hypercubes; accessible publisher material describes a size-solving approach but does not establish uniqueness. Faudree, Gyárfás, Schelp, and Tuza (1990), as cited in the full-text 2021 article *Strong Edge Coloring of Cayley Graphs and Some Product Graphs*, determine the previously known strong chromatic index \(2d\), without an enumerative statement in the inspected summary. The 2005 semistrong-coloring paper concerns a related weakening and mentions hypercube questions but is not claimed to establish the classification. The equality-rigidity argument above supplies the new implication that none of these inspected statements entails on its face.

## Limitations

No claim of priority is proved by unsuccessful searches. The complete 1990 article and the 2013 journal full text were not available for complete comparison; they could contain unindexed equivalent statements. The 2012 thesis's relevant full-text section was inspected and supports the sharper prior-work separation. The construction is not a classification of nonmaximum induced matchings, and the exchange assertion uses one-edge replacement at fixed maximum cardinality (not intermediate smaller matchings). The result is a purely graph-theoretic classification, not an algorithmic complexity improvement. Independent external validation has not been performed.

## References

1. K. K. Dabrowski, *Structural Solutions to Maximum Independent Set and Related Problems*, University of Warwick PhD thesis, October 2012, §4.3.2, Theorem 41. https://wrap.warwick.ac.uk/54515/1/WRAP_THESIS_Dabrowski_2012.pdf
2. K. K. Dabrowski, M. Demange, and V. V. Lozin, *New results on maximum induced matchings in bipartite graphs and beyond*, Theoretical Computer Science **478** (2013), 33–40. https://doi.org/10.1016/j.tcs.2013.01.027
3. R. J. Faudree, A. Gyárfás, R. H. Schelp, and Zs. Tuza, *The strong chromatic index of graphs*, Ars Combinatoria **29B** (1990), 205–211. Bibliographic reference and hypercube result are corroborated by [5].
4. A. Gyárfás, *Semistrong edge coloring of graphs*, Journal of Graph Theory **49** (2005), 39–47. https://doi.org/10.1002/jgt.20061
5. *Strong Edge Coloring of Cayley Graphs and Some Product Graphs*, Graphs and Combinatorics (2021). https://doi.org/10.1007/s00373-021-02408-4

# Fibonacci enumeration and exact conflict-free edge-colouring threshold for spider trees

## Finding

Let \(k\ge3\), and let \(S=S(\ell_1,\ldots,\ell_k)\) be the simple spider tree formed by joining \(k\) internally vertex-disjoint paths of respective edge lengths \(\ell_i\ge1\) at their common initial vertex. An edge-colouring is *conflict-free* if, for every edge, at least one colour occurs **exactly once** among the edges incident with either endpoint (including the edge itself).

Write \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). Define, for each arm,
\[
 u_i=\begin{cases}1,&\ell_i=1,\\F_{\ell_i-2},&\ell_i\ge2,\end{cases}
 \qquad
 v_i=\begin{cases}1,&\ell_i=1,\\F_{\ell_i-1},&\ell_i\ge2.\end{cases}
\]
Let \(N_2(S)\) be the number of conflict-free edge-colourings with the two **named** colours red and blue, assigning a colour to every edge. Then
\[
\boxed{N_2(S)=2\sum_{j=1}^{k}v_j\prod_{i\ne j}u_i
 +2\,\mathbf 1_{\{\min_i\ell_i\ge2\}}\prod_{i=1}^{k}v_i.}
\]
The formula is valid for all \(k\ge3\) and all positive integer arm lengths, including length one and length two.

In particular, if \(s=|\{i:\ell_i=1\}|\) and \(t=|\{i:\ell_i=2\}|\), then
\[
\boxed{\chi'_{\mathrm{CF}}(S)=
\begin{cases}3,&s\ge1\text{ and }t\ge2,\\2,&\text{otherwise}.\end{cases}}
\]
Here \(\chi'_{\mathrm{CF}}\) is the minimum number of colours for a conflict-free edge-colouring of the entire graph, not the selective or partially coloured variant.

## Assumptions and scope

Graphs are finite, undirected, loopless and simple. The spider has exactly one vertex of degree at least three, of degree \(k\). Arms are distinguished by their vertices, even if some lengths coincide. Thus the count refers to a fixed graph with named edges and named red/blue colours; it does not quotient by graph automorphisms or by interchange of the two colours.

For the arm indexed by \(i\), denote its consecutive edges moving away from the central vertex by \(e_{i,1},\ldots,e_{i,\ell_i}\). Put \(a_i\in\{0,1\}\) for the red indicator of \(e_{i,1}\), and, when \(\ell_i\ge2\), \(b_i\) for the red indicator of \(e_{i,2}\). Let \(R=\sum_{i=1}^{k}a_i\).

The closed edge neighbourhood of an edge \(xy\) is the set union of edges incident with \(x\) or \(y\), so the edge \(xy\) is counted only once. Colourings need not be proper.

## Proof

**1. The constraint at the common vertex.** For an arm of length one, the closed neighbourhood of its single edge consists precisely of the \(k\) spokes at the common vertex. With two colours, a colour is unique in this set exactly when
\[
 R\in\{1,k-1\}.
\]
For an arm of length at least two, the closed neighbourhood of its first edge consists of the \(k\) spokes together with its second edge. It has \(k+1\) edges and exactly \(R+b_i\) red edges. Therefore its conflict-free condition is precisely
\[
 R+b_i\in\{1,k\}.
\]
As \(k\ge3\), these conditions leave only the following mutually exclusive possibilities:

- \(R=0\): all spokes are blue and every existing second edge is red;
- \(R=k\): all spokes are red and every existing second edge is blue;
- \(R=1\): exactly one spoke is red and every existing second edge is blue;
- \(R=k-1\): exactly one spoke is blue and every existing second edge is red.

The first two cases are possible only if **no** arm has length one. In the last two cases length-one arms impose no additional condition. No other value of \(R\) is allowed, since if there is a length-one arm the first constraint applies, and otherwise the second constraint applies to every arm.

**2. The path-tail lemma.** Fix an arm with length \(L\ge2\) and prescribe the colours of its first two edges. For every edge strictly between the first and last edges, its closed neighbourhood consists of three consecutive path edges. It is conflict-free exactly when those three colours are not all identical. For the last edge, the closed neighbourhood consists of the last two path edges; they must have different colours. These constraints are sufficient for every non-spoke edge.

Let \(A_L\) be the number of admissible completions when the first two colours agree and let \(B_L\) be the number when they differ. At \(L=2\), the final-edge condition gives \(A_2=0\) and \(B_2=1\). For an extension by one edge, an equal last pair must be followed by its opposite, while an unequal last pair can be followed by either colour. Equivalently, running the recurrence backwards from the required unequal final pair gives
\[
 A_{L+1}=B_L,\qquad B_{L+1}=A_L+B_L.
\]
Consequently, by induction,
\[
 A_L=F_{L-2},\qquad B_L=F_{L-1}\qquad(L\ge2).
\]
Thus the number of allowed tails is \(u_i\) if the first two colours agree and \(v_i\) if they differ. For a length-one arm there is no tail, and both factors were defined as one.

**3. Exhaustive enumeration.** Suppose first that every arm has length at least two. In each of the two monochromatic-spoke possibilities \(R=0,k\), the second edge on every arm is of the opposite colour to its spoke. By the path-tail lemma, each possibility gives \(\prod_i v_i\) distinct colourings. If any length-one arm exists, neither possibility is feasible. This yields the second summand in the boxed formula.

For \(R=1\), choose the index \(j\) of the unique red spoke. Every existing second edge is blue: the first two edges on arm \(j\) differ (factor \(v_j\)), while those on every other long arm agree (factors \(u_i\)). The length-one factors are one. Therefore the number of colourings in this case is \(\sum_j v_j\prod_{i\ne j}u_i\). Interchanging red and blue gives exactly the same number for \(R=k-1\). Because \(k\ge3\), those two cases are disjoint. Summing all four cases proves the formula, with no overcounting.

**4. Exact threshold.** Every \(v_i\) is positive, whereas \(u_i=0\) holds precisely when \(\ell_i=2\). If no arm has length one, the monochromatic-spoke term is positive. If at least one arm has length one, that term is absent, and the first sum is positive precisely when at most one factor \(u_i\) is zero: the exceptional index \(j\) may avoid the sole zero but cannot avoid two zeros. Hence \(N_2(S)=0\) exactly when \(s\ge1\) and \(t\ge2\).

A one-colour assignment cannot satisfy the edges incident with the degree-\(k\) center, so \(\chi'_{\mathrm{CF}}(S)\ge2\). Conversely, **every** tree admits a three-colour conflict-free edge-colouring: root at a leaf, and colour every edge joining levels \(h\) and \(h+1\) by \(h\bmod3\). The root edge has a uniquely occurring colour in its closed edge neighbourhood; any edge at a non-root level has the unique colour of the preceding parent edge, different from the colours of its own level and its child level. Therefore \(\chi'_{\mathrm{CF}}(S)\le3\). The criterion for \(N_2(S)>0\) finishes the proof. \(\square\)

## Verification

The included `verify.py` builds each spider independently as an edge list and directly enumerates all \(2^{|E(S)|}\) named binary edge-colourings on small instances. For each edge it constructs its closed edge neighbourhood from the graph and tests whether the red count is one or one less than the neighbourhood size; this is exactly the existence of a colour appearing once. The checker compares the resulting count with the Fibonacci formula and compares the zero-count classification with the length-one/length-two obstruction.

Run `python verify.py` using Python 3.8 or later. The recorded `verify_output.txt` lists the number of test profiles and success status. The checker tests 300 systematically enumerated unordered arm-length profiles with total edge count at most fourteen and 56 additional seeded sampled profiles with up to seventeen edges, including four to eight arms. This finite validation is corroboration, **not** the proof of the infinite-parametric theorem; the proof above is independent of those runs.

For instance, \(N_2(S(1,2,2))=0\), \(N_2(S(1,2,3))=2\), \(N_2(S(2,2,2))=2\), and \(N_2(S(1,1,1))=6\).

## Relationship to prior work

The original conflict-free edge-colouring framework, and the three-colour upper bound for trees, appear in Kamyczura, Meszka and Przybyło [1], and earlier in the work cited there. Guo, Li, Li and Li [2] study two-colour conflict-free edge-colourings of trees with no degree-two vertices and give a sufficient condition for more general trees; neither their displayed characterization nor their sufficient condition supplies this length-sensitive complete spider enumeration. Jin and Gao [3, Theorems 1.3 and 1.9] establish the sharp bipartite upper bound three and state a general feasibility condition for two-colouring trees through the existence of an edge subset satisfying local degree equations. That condition does not directly evaluate the condition for arbitrary spider subdivisions or enumerate all solutions.

The present result solves the explicit spider case, including arbitrary degree-two subdivisions, and determines all labelled two-colourings rather than just giving a decision criterion. The previous general tree upper bounds and the general local feasibility reformulation are credited rather than claimed as new.

## Limitations

Only spiders with center degree at least three are covered; a path has degree at most two and requires separate counting conventions. The theorem counts labelled red/blue colourings, not inequivalent colourings under automorphisms. It does not classify arbitrary trees or count three-colourings. The formula evaluates in arithmetic operations; writing the integer output in binary incurs its output bit-length. Formal independent mathematical validation has not been performed. Priority is subject to equivalent results possibly present in unindexed literature.

## References

[1] M. Kamyczura, M. Meszka, J. Przybyło, *A note on the conflict-free chromatic index*, arXiv:2203.02040v1, 2022; Discrete Mathematics 347 (2024), 113897. https://arxiv.org/abs/2203.02040

[2] S. Guo, E. Y. H. Li, L. Li, P. Li, *Conflict-free chromatic index of trees*, arXiv:2409.10899v1, first posted 17 September 2024; Theoretical Computer Science 1058 (2025), 115587. https://arxiv.org/abs/2409.10899

[3] Y. Jin, Y. Gao, *Conflict-free chromatic index of bipartite graphs*, arXiv:2604.24183v1, first posted 27 April 2026. https://arxiv.org/html/2604.24183

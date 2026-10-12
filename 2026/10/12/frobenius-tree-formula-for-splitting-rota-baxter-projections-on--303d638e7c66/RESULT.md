# Frobenius tree formula for splitting Rota–Baxter projections on finite étale algebras

## Finding
For any prime power \(q\), consider a nonzero finite étale algebra
\[
A=\prod_{d\ge1}\mathbb F_{q^d}^{\,r_d},\qquad r_d\in\mathbb Z_{\ge0},\quad \sum_d r_d>0,
\]
where only finitely many multiplicities are nonzero. Set
\[
s_d=\sum_{\substack{e\mid d\\1\le e<d}} e r_e.
\]
The number of \(\mathbb F_q\)-linear **idempotent weight-minus-one Rota–Baxter operators** \(P:A\to A\), i.e. maps satisfying
\[
P^2=P,\qquad P(x)P(y)=P(P(x)y+xP(y)-xy)\quad(x,y\in A),
\]
is
\[
\boxed{N(A)=\prod_{d:r_d>0}(2+s_d)(2+s_d+d r_d)^{r_d-1}.}
\]
The count depends only on the extension degrees and their multiplicities, not on the size or characteristic of the base finite field. Every operator counted is projection onto one subalgebra along another. The two subalgebras need not contain the identity of \(A\).

Particular cases include \(N(\mathbb F_q^n)=2(n+2)^{n-1}\) and \(N(\mathbb F_{q^d}^{\,m})=2(2+dm)^{m-1}\). Mixed cases include \(N(\mathbb F_q\times\mathbb F_{q^2})=6\) and \(N(\mathbb F_q^2\times\mathbb F_{q^2})=32\).

## Assumptions and scope
All algebras, subalgebras, and linear maps are over \(k=\mathbb F_q\); zero subalgebras are permitted. A subalgebra is required to be closed under multiplication but need not be unital. The weights in the formula are ordinary nonnegative integers and are not reduced modulo the characteristic. The empty product (the zero algebra) is outside the theorem; at least one field factor is required.

## Proof
**Step 1: operators and complementary subalgebras.** If \(P^2=P\), set \(B=\operatorname{im}P\) and \(C=\ker P\). For \(b,b'\in B\), the Rota–Baxter identity implies \(bb'=P(bb')\), hence \(B\) is closed. For \(c,c'\in C\), it gives \(0=-P(cc')\), so \(C\) is closed. Conversely, given \(A=B\oplus C\) as vector spaces with both summands subalgebras, write \(x=b+c\), \(y=b'+c'\). The projection \(P(b+c)=b\) satisfies \(P^2=P\) and
\[
P(P(x)y+xP(y)-xy)=P(bb'-cc')=bb'=P(x)P(y).
\]
Thus the desired maps are in bijection with ordered complementary subalgebra pairs.

**Step 2: a tree encoding after splitting.** Over an algebraic closure \(K\), the étale algebra becomes \(K^n\), \(n=\sum_d d r_d\). Every \(K\)-subalgebra of \(K^n\) is a product of copies of \(K\) supported on disjoint nonempty coordinate blocks: its primitive idempotents are characteristic vectors of these blocks. In particular, if \(B,C\subseteq K^n\) are complementary subalgebras, let their respective block families be blue and red. Form a graph with one vertex for each block and one extra root \(0\). For each coordinate \(i\), draw an edge labeled \(i\) between the unique blue and red blocks containing \(i\), using root \(0\) for a missing block of either color. Coordinates missing from both blocks cannot occur for a complementary pair.

There are \(n\) edges. The number of non-root vertices is \(\dim_K B+\dim_K C=n\). The matrix with the block indicator vectors as columns is, after changing signs on one color, the edge-versus-vertex incidence matrix with the root column deleted. Its rank is \(n\) precisely when the graph is connected. Since it has \(n+1\) vertices and \(n\) edges, this means precisely that the graph is a tree (parallel edges count as a cycle). Along every non-root edge the endpoint colors differ. Conversely, any rooted tree on edge labels \(1,\ldots,n\) with a proper two-coloring of its non-root vertices recovers the blue and red coordinate blocks and thus a complementary pair. Orient edges toward the root and label each non-root vertex by its unique edge directed toward its parent. This produces a canonical tree on the vertex set \(\{0,1,\ldots,n\}\), with root fixed and with a proper two-coloring on non-root adjacencies.

**Step 3: descent through Frobenius.** The coordinates of \(K^n\) carry the Frobenius permutation \(\sigma\) whose cycles have lengths \(d\), with \(r_d\) cycles of each length. The preceding construction is equivariant under permutations of the coordinates. By finite Galois descent, \(k\)-subalgebra decompositions are exactly the \(\sigma\)-invariant colored trees. Distinct Frobenius cycles of coordinates are considered distinct even if they have equal length. An invariant parent map on a cycle of length \(d\) either maps the entire cycle to root, or sends it into a **different** cycle of length \(e\mid d\). In the latter case there are exactly \(e\) equivariant phase choices: the image of one coordinate determines the rest. A parent map into its own cycle cannot lie in a rooted tree. The quotient parent relation on the field-factor cycles has no directed cycles and every parent chain reaches root, exactly when the original parent relation does. Each quotient component attached to root has two choices of the initial vertex color; all subsequent colors are fixed by alternation and Frobenius invariance.

**Step 4: weighted arborescence determinant.** Index the \(m=\sum_d r_d\) Frobenius cycles by \(i=1,\ldots,m\), and write \(d_i\) for cycle \(i\)'s length. Every edge from cycle \(i\) to root has weight \(2\), counting its two color choices, and an edge from \(i\) to a distinct cycle \(j\) has weight \(d_j\) if \(d_j\mid d_i\) and weight \(0\) otherwise. The weighted directed matrix-tree theorem gives the total weight of rooted arborescences as \(\det L\), with
\[
L_{ij}=\begin{cases}
2+\displaystyle\sum_{\substack{k\ne i\\d_k\mid d_i}}d_k,&i=j,\\
-d_j,&i\ne j,\ d_j\mid d_i,\\
0,&\text{otherwise}.
\end{cases}
\]
Order cycle indices by increasing degree. The matrix is block lower triangular because parent degrees divide child degrees. For a fixed degree \(d\) of multiplicity \(r_d\), its diagonal block is
\[
L_d=(2+s_d+d r_d)I_{r_d}-d J_{r_d},
\]
where \(J_{r_d}\) is the all-ones matrix. Its eigenvalues over the rational numbers are \(2+s_d\) once and \(2+s_d+d r_d\) with multiplicity \(r_d-1\), hence
\[
\det L_d=(2+s_d)(2+s_d+d r_d)^{r_d-1}.
\]
Multiplying block determinants proves the formula for all prime powers and all extension-degree multisets. The determinant is computed over the integers, so no characteristic restrictions enter.

## Verification
The accompanying standalone `verify.py` directly enumerates \(\mathbb F_2\)-linear subspaces, tests closure under the actual multiplication in finite products of \(\mathbb F_{2^d}\), then enumerates ordered complementary subalgebra pairs. For total dimensions at most four it also constructs the projection for every pair and checks idempotence and the Rota–Baxter identity on every pair of algebra elements. Tested degree multisets include \((1,1,1,1)\) yielding \(432\), \((1,1,2)\) yielding \(32\), \((2,2)\) yielding \(12\), and \((2,3)\) yielding \(4\). Execute `python3 verify.py`; successful completion prints `VERIFY_OK`. These finite checks corroborate but do not replace the general symbolic proof.

## Relationship to prior work
An and Bai, *From Rota-Baxter Algebras to Pre-Lie Algebras* (public preprint 2007), investigated weight-one operators on complex associative algebras of dimension at most three. Gubarev, *Rota–Baxter operators on a sum of fields* (public preprint 2018), classified operators on split products \(F^n\), and proved that splitting operators correspond to properly two-colored rooted trees (Theorem 2). Its Table 1 presents the split-case expression \(2(n+2)^{n-1}\) with question marks rather than as a proven general count. Here the claimed refinement is a direct proof and closed product formula for **all finite étale finite-field forms**, whose factors have nontrivial Frobenius cycles. The split-algebra tree correspondence and classical weighted matrix-tree theorem are antecedents and not claimed as new.

## Limitations
This theorem counts idempotent weight-minus-one operators, equivalently splitting operators. It does not classify all weight-minus-one Rota–Baxter maps, non-étale algebras, or operators of weight zero. The count is of actual linear operators, not their conjugacy classes under algebra automorphisms. Uncertainty remains about whether an equivalent equivariant-tree enumeration has appeared under different terminology; the comparison is not a claim of exhaustive priority.

## References
1. H. An and C. Bai, *From Rota-Baxter Algebras to Pre-Lie Algebras*, arXiv:0711.1389v1 (9 November 2007), https://arxiv.org/abs/0711.1389.
2. V. Gubarev, *Rota–Baxter operators on a sum of fields*, arXiv:1811.08219v1 (20 November 2018), especially Theorem 2 and Table 1, https://arxiv.org/abs/1811.08219.
3. The directed weighted matrix-tree theorem (classical combinatorial result), used with weights explicitly specified above.

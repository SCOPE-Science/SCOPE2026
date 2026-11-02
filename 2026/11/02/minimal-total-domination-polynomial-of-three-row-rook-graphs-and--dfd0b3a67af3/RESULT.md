# Minimal total-domination polynomial of three-row rook graphs and unbounded cardinality gaps

## Finding
For each integer \(n\ge 3\), let \(R_{3,n}=K_3\square K_n\) be the rook graph on the cells of a labeled \(3\)-by-\(n\) board. Its vertices are the cells \((i,j)\), adjacent when they share a row or a column and are distinct. A total dominating set is a set \(S\) for which every vertex, including every member of \(S\), has a neighbor in \(S\). It is *inclusion-minimal* when no proper subset remains total dominating. Let \(T_n(z)=\sum_S z^{|S|}\), where the sum is over all inclusion-minimal total dominating sets.

**Theorem.** For every integer \(n\ge3\),
\[
T_n(z)=nz^3+\frac{3n^2(n-1)}2z^4
+\mathbf{1}_{\{n\ge6\}}\frac{n!}{8(n-6)!}z^6
+3(2^n-2n-1)z^n
+18\mathbf{1}_{\{n=3\}}z^4.
\]
Terms having the same degree must be added. All other coefficients are zero. In particular, for every \(n\ge8\), the attainable cardinalities are exactly \(3,4,6,n\); none of \(7,8,\ldots,n-1\) is attained. Hence the gap between attainable cardinalities is unbounded within this connected graph family. For \(n\ge4\), the upper total domination number is \(n\), while for \(n=3\) it is \(4\). The minimum total domination number is \(3\) for every \(n\ge3\).

Equivalently, since \(R_{3,n}\cong L(K_{3,n})\), the theorem enumerates inclusion-minimal *total edge dominating* sets in the complete bipartite graph \(K_{3,n}\).

## Assumptions and scope
All graphs are finite, simple, undirected and labeled. In the term \(\mathbf{1}_{\{P\}}\), the value is one when condition \(P\) holds and zero otherwise. The polynomial counts actual subsets of the vertex set, not symmetry orbits. Minimal means inclusion-minimal, not minimum cardinality. The factor \(3(2^n-2n-1)\) includes both single-row full stars and two-row partitions; it is positive for \(n\ge3\).

## Proof
Write \(d_i\) for the selected count in row \(i\), and \(c_j\) for the selected count in column \(j\). A cell outside \(S\) has a neighbor in \(S\) precisely when its row or column is occupied. A selected cell \((i,j)\) has exactly \(d_i+c_j-2\) selected neighbors. Therefore \(S\) is total dominating if and only if (i) all rows are occupied or all columns are occupied and (ii) no selected cell is isolated in the induced rook graph \(R_{3,n}[S]\).

We use the private-neighbor criterion: a total dominating set \(S\) is inclusion-minimal if and only if, for every \(s\in S\), there is a vertex \(v\) with \(N(v)\cap S=\{s\}\). This holds because removing \(s\) destroys total domination precisely when some vertex loses its last selected neighbor.

**Lemma (full row and column coverage).** If all rows and columns are occupied, every component of \(R_{3,n}[S]\) is a single edge whenever \(S\) is inclusion-minimal. Indeed, after any selected cell is removed, at least one of full row coverage or full column coverage persists. Thus no outside cell loses all selected neighbors; a private witness for each selected cell must be another selected cell having exactly one selected neighbor. Every vertex of the induced graph must therefore have a degree-one neighbor. A degree-one vertex's sole neighbor must itself have degree one (otherwise this degree-one vertex would lack a private selected witness). Consequently, each component is \(K_2\). An induced rook-graph \(K_2\) uses two cells in one row and two distinct columns (horizontal) or one column and two rows (vertical), and distinct components use disjoint rows and columns. If there are \(a\) horizontal and \(b\) vertical components covering all rows and columns, then \(a+2b=3\), \(2a+b=n\). The only solutions with \(n\ge3\) are \((a,b,n)=(1,1,3)\) and \((3,0,6)\).

**Case I: all three rows are occupied.** Suppose first that at least one column is unoccupied. Every cell in a row containing exactly one selected cell is indispensable: an unselected cell in that row and the unoccupied column has precisely that selected neighbor. A cell in a row containing at least two selected cells cannot be indispensable through the loss of row or column coverage, so it requires a *selected* private witness: a selected cell with exactly one selected neighbor. If a row contains \(d\ge3\) selected cells, each of its \(d\) cells needs such a witness sharing its column, located in a row with selected degree one. Distinct cells require distinct witnesses, but there are only two other rows. Thus no row has selected degree at least three.

The possible row-degree patterns are therefore \((1,1,1)\), \((2,1,1)\), \((2,2,1)\), and \((2,2,2)\), up to permutation.

For \((1,1,1)\), all three selected cells must lie in one column to avoid an isolated selected cell. There are \(n\) sets, each of size three.

For \((2,1,1)\), write the two cells of the degree-two row as \((i,a)\) and \((i,b)\) with \(a\ne b\). The necessary and sufficient possibilities for both to have private selected witnesses, and for the other two selected cells not to be isolated, are: (A) the singleton-row cells occur respectively in columns \(a\) and \(b\); or (B) the singleton-row cells share a third column \(c\notin\{a,b\}\). These choices also make each singleton-row cell indispensable, either through the missing-column witness or by belonging to its own induced \(K_2\) component. Type A contributes \(3n(n-1)\) sets. Type B contributes \(3\binom n2(n-2)\) sets. Together they give \(\frac{3n^2(n-1)}2\) sets of size four.

For \((2,2,1)\), a degree-two row can only make both its cells indispensable if both selected columns are unique, or if *each* has a singleton-row private supporter in its own column. A selected column shared with a different degree-two row provides no private witness because the other selected cell already has a same-row neighbor. As there is only one singleton row, the second alternative is impossible. Both degree-two rows must thus use four distinct columns; then the remaining singleton-row cell is isolated (if placed in a fifth column) or destroys one degree-two row's required private witness (if placed in an occupied column). Therefore no such set is minimal.

For \((2,2,2)\), each selected cell must use a column containing no other selected cell: otherwise its only same-row candidate for a private selected witness has at least two selected neighbors. Conversely, three disjoint horizontal pairs are minimal total dominating sets. They exist only for \(n\ge6\), and number \(\binom n2\binom{n-2}2\binom{n-4}2=\frac{n!}{8(n-6)!}\); their size is six.

If all columns are occupied as well, the full-coverage lemma shows that only the \(n=3\) type-B configuration or the \(n=6\) three-horizontal-pair configuration can occur. These were already counted above, so the Case-I counts remain exhaustive without duplication.

**Case II: at least one row is unoccupied.** Then every column must be occupied. If exactly one row is occupied, it contains all \(n\) cells. Each is indispensable because deleting it leaves its column empty while another row remains empty. There are three such sets of size \(n\).

If exactly two rows are occupied, choose their identities in three ways. If every column contains exactly one selected cell, this is a partition of the \(n\) labeled columns into two labeled nonempty row classes. To avoid isolated selected cells, each class must contain at least two columns. Every such set is minimal, since deleting any selected cell leaves a column empty and an unoccupied row remains. Their number is \(3(2^n-2-2n)\), of size \(n\).

If a column contains both selected cells, removal of either leaves all columns occupied; hence each of these two cells requires a selected private witness. Neither can use the other as witness, because both occupied rows must have selected degree at least two. The witness must therefore be a singleton-column cell in the same row; this forces each row to have degree exactly two. Thus there is exactly one doubly occupied column and exactly two additional singly occupied columns, so necessarily \(n=3\). Choose the two occupied rows in three ways, the doubled column in three ways, and assign the remaining two columns to the two rows in two ways: exactly \(18\) additional size-four sets. They are inclusion-minimal because deleting either doubly occupied cell isolates its row partner and deleting a singly occupied column leaves it uncovered.

The two cases are disjoint and exhaust all total dominating sets. Adding the enumerations proves the polynomial. The bounds and cardinality gap follow because each displayed nonzero summand has the claimed degree, and every coefficient count is positive in its stated range. \(\square\)

## Verification
The standalone `verify.py` constructs rook adjacencies directly from shared coordinates; for every nonempty subset of the \(3n\) cells, it checks total domination using all open neighborhoods and checks inclusion-minimality via the private-neighbor criterion. It does **not** use the theorem's structural classification for acceptance. Running `python3 verify.py` exhaustively checks all \(2^{3n}-1\) nonempty subsets for each \(n=3,4,5,6,7\), totaling 2,396,667 subsets. Its observed distributions are \(T_3(z)=6z^3+45z^4\), \(T_4(z)=4z^3+93z^4\), \(T_5(z)=5z^3+150z^4+63z^5\), \(T_6(z)=6z^3+270z^4+243z^6\), and \(T_7(z)=7z^3+441z^4+630z^6+339z^7\). The verifier terminates with `VERIFY_OK cases=5 tested_subsets=2396667`. Finite checking corroborates but cannot replace the all-order proof.

## Relationship to prior work
The minimum total edge domination problem and its computational complexity were studied by Pan, Yang, Li and Xu (arXiv:1910.02431, initially public October 6, 2019), whose focus is NP-completeness and trees, rather than labeled inclusion-minimal-set polynomials of complete bicliques. Bahadır, Ekim and Gözüpek (arXiv:2010.02341, initially public October 5, 2020) study well-totally-dominated graphs and general minimal-total-domination transversals. Brešar, Cornet, Dravec and Henning (arXiv:2310.07432, initially public October 11, 2023, primary MSC 05C69) prove universal inequalities involving the upper total domination number. These general principles do not directly give the stated complete \(3\)-row polynomial or its unbounded cardinality gap. Golovach, Heggernes, Kanté, Kratsch and Villanger (DOI:10.1016/j.dam.2014.12.010) study enumeration algorithms on chordal bipartite graphs; rook graphs here contain triangles, and their results do not provide these coefficients. No assertion of universal publication priority is made.

## Limitations
The closed formula is proved for exactly three rows and \(n\ge3\), not for arbitrary rectangular rook graphs or arbitrary total edge dominating sets. It counts labeled inclusion-minimal sets rather than all total dominating sets or symmetry classes. An equivalent result could appear in unindexed or uninspected literature; the novelty comparison is limited to the inspected accessible sources and research records. No independent mathematical audit is claimed.

## References
1. Z. Pan, Y. Yang, X. Li and S.-J. Xu, *The complexity of total edge domination and some related results on trees*, arXiv:1910.02431 (first public 2019-10-06), https://arxiv.org/abs/1910.02431.
2. S. Bahadır, T. Ekim and D. Gözüpek, *Well-Totally-Dominated Graphs*, arXiv:2010.02341 (first public 2020-10-05), https://arxiv.org/abs/2010.02341.
3. B. Brešar, M. G. Cornet, T. Dravec and M. Henning, *Bounds on zero forcing using (upper) total domination and minimum degree*, arXiv:2310.07432 (first public 2023-10-11), https://arxiv.org/abs/2310.07432.
4. P. A. Golovach, P. Heggernes, M. M. Kanté, D. Kratsch and Y. Villanger, *Enumerating minimal dominating sets in chordal bipartite graphs*, Discrete Applied Mathematics 199 (2016), 30–36, DOI:10.1016/j.dam.2014.12.010.

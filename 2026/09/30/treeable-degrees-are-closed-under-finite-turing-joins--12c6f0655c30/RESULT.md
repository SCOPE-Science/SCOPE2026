# Treeable degrees are closed under finite Turing joins
## Finding
A Turing degree \(\mathbf d\) is treeable if there is a computable tree \(T\subseteq\omega^{<\omega}\) and a path \(f\in[T]\) of degree \(\mathbf d\) such that
\[
f\leq_T g\qquad\text{for every }g\in[T].
\]
Then the class of treeable degrees is closed under finite Turing joins. More precisely, if \(\mathbf d_0,\ldots,\mathbf d_{m-1}\) are treeable and \(m\geq1\), then
\[
\mathbf d_0\vee\cdots\vee\mathbf d_{m-1}
\]
is treeable.

The same product construction preserves uniqueness: if each \(\mathbf d_i\) is the degree of the unique path through a computable tree, then their finite join is again the degree of the unique path through a computable tree.

As a consequence of the Csima--Rossegger characterization, if \(\mathbf d_0,\ldots,\mathbf d_{m-1}\) are strong degrees of categoricity and
\[
\mathbf d_0\vee\cdots\vee\mathbf d_{m-1}\geq_T\mathbf 0'',
\]
then their join is again a strong degree of categoricity. In particular, the strong degrees of categoricity on the cone above \(\mathbf 0''\) are closed under finite Turing joins.

## Assumptions and scope
Trees are computable subtrees of \(\omega^{<\omega}\), and a path is Turing-least when it is Turing reducible to every path through the same tree. Finite joins are standard Turing joins; all standard computable codings have the same degree.

The categoricity consequence uses two results from Csima and Rossegger: every strong degree of categoricity is treeable, and every treeable degree computing \(\mathbf 0''\) is a strong degree of categoricity. Their corrected preprint explicitly restricts the converse characterization to strong degrees and retracts an earlier claim about all degrees of categoricity above \(\mathbf 0''\).

No countable-join statement is asserted. The finite proof can hard-code finitely many reduction indices, while an infinite family of pathwise reductions need not admit one uniform index.

## Proof
It is enough to prove the binary case and then iterate.

Let \(T,S\subseteq\omega^{<\omega}\) be computable trees. Choose paths \(f\in[T]\) and \(g\in[S]\) such that
\[
f\leq_T x\quad\text{for every }x\in[T],
\qquad
g\leq_T y\quad\text{for every }y\in[S].
\]
Fix a computable bijection \(\langle\cdot,\cdot\rangle:\omega^2\to\omega\). Define a computable tree \(U\subseteq\omega^{<\omega}\) by putting \(\sigma\in U\) exactly when the coordinate projections
\[
\pi_0(\sigma)(n)=a,
\qquad
\pi_1(\sigma)(n)=b
\]
whenever \(\sigma(n)=\langle a,b\rangle\), satisfy
\[
\pi_0(\sigma)\in T
\qquad\text{and}\qquad
\pi_1(\sigma)\in S.
\]
Because the pairing and both tree predicates are computable, \(U\) is computable. Its paths are exactly the coordinatewise pairings
\[
[U]=\{\langle x,y\rangle:x\in[T],\ y\in[S]\}.
\]

The distinguished path \(h=\langle f,g\rangle\) has degree
\[
\deg_T(h)=\deg_T(f)\vee\deg_T(g).
\]
Now let \(z\in[U]\). Its computable projections give \(x=\pi_0(z)\in[T]\) and \(y=\pi_1(z)\in[S]\). Hence
\[
f\leq_T x\leq_T z
\qquad\text{and}\qquad
g\leq_T y\leq_T z.
\]
Since there are only two reductions, they can be combined into one oracle computation of \(f\oplus g\) from \(z\). Therefore
\[
f\oplus g\leq_T z.
\]
Thus \(h\) has least Turing degree among the paths of \(U\), proving that \(\deg_T(f)\vee\deg_T(g)\) is treeable. Finite closure follows by induction.

If \([T]=\{f\}\) and \([S]=\{g\}\), then the displayed description of \([U]\) immediately gives
\[
[U]=\{\langle f,g\rangle\}.
\]
Hence the degrees of computable-tree unique paths are also closed under finite joins.

For the categoricity consequence, let \(\mathbf e=\mathbf d_0\vee\cdots\vee\mathbf d_{m-1}\). Every strong degree of categoricity is treeable by Csima--Rossegger, so finite closure makes \(\mathbf e\) treeable. If \(\mathbf e\geq_T\mathbf 0''\), their converse characterization applies and shows that \(\mathbf e\) is a strong degree of categoricity. If each \(\mathbf d_i\geq_T\mathbf 0''\), then automatically \(\mathbf e\geq_T\mathbf 0''\), yielding the stated cone closure.

## Verification
The proof was reconstructed directly from the definition of treeability and from the corrected version of the source characterization. The main quantifier issue is finite nonuniformity: for a fixed product path \(z\), leastness supplies reductions of \(f\) from \(\pi_0(z)\) and of \(g\) from \(\pi_1(z)\). Because only finitely many such reductions occur, their indices can be hard-coded into one oracle program computing the finite join. This is exactly the step that does not automatically generalize to countably many coordinates.

The source check also distinguished the valid strong-degree characterization from the claim withdrawn in the first preprint version. The arXiv record states that the current version characterizes strong degrees of categoricity above \(\mathbf 0''\) as exactly the treeable degrees on that cone.

The included `verify.py` exhaustively checks the finite combinatorics of the product construction for every pair of nonempty binary leaf sets at depth \(3\). In all \(65025\) pairs it verifies that the depth-\(6\) paths through the paired product tree are exactly the Cartesian products of the factor paths, and that the product has a unique path exactly when both factors do. The program terminates with `VERIFY_OK 65025`.

## Relationship to prior work
Csima and Rossegger introduced treeable degrees in their study of degrees of categoricity. They prove that every strong degree of categoricity is treeable and that, on the cone above \(\mathbf 0''\), the treeable degrees are exactly the strong degrees of categoricity. Their main tree-coding theorem also singles out computable trees with unique paths as a particularly rigid case.

The present result extracts an algebraic closure property of the degree class itself. The source paper develops examples and a characterization but does not state finite-join closure, an upper-semilattice property, or the resulting finite-join closure theorem for strong degrees of categoricity on the classified cone. Targeted searches for treeable degrees together with finite joins, upper semilattices, product trees, and categoricity closure did not locate an equivalent or stronger statement.

## Limitations
Only finite joins are proved. The same product-tree construction over countably many coordinates does not by itself establish that the countable join is Turing reducible to every product path, because the individual reductions witnessing leastness may be nonuniform in the coordinate.

The categoricity corollary uses the converse classification only when the joined degree computes \(\mathbf 0''\). It therefore does not settle finite-join closure of strong degrees entirely below that cone.

The finite verification program checks the tree-product coding and uniqueness behavior, not the Turing-reducibility argument or the cited categoricity theorem. No independent audit or formal proof-assistant verification was performed.

The originality assessment is best-of-knowledge rather than exhaustive.

## References
Barbara F. Csima and Dino Rossegger, “Degrees of categoricity and treeable degrees,” arXiv:2209.04524v2, first public version 9 September 2022; *Journal of Mathematical Logic* 24(3), 2450002. DOI:10.1142/S0219061324500028.

# Dual Dowker complexes first lose a bi-twin-free relation at \(3\times3\)
## Finding
Let \(R\subseteq X\times Y\) be a finite binary relation. Call \(R\) **bi-twin-free** when every row and column neighborhood is nonempty, all row neighborhoods are pairwise distinct, and all column neighborhoods are pairwise distinct. Write \(D_X(R)\) for the Dowker complex on \(X\), whose simplices are the subsets contained in a column neighborhood, and \(D_Y(R)=D_X(R^T)\) for the dual complex.

The ordered pair \(\bigl(D_X(R),D_Y(R)\bigr)\), considered up to independent simplicial isomorphism on the two vertex sets, determines every bi-twin-free relation with \(|X|+|Y|<6\). This fails first for \(|X|=|Y|=3\). Up to independent row and column permutations, the unique collision among all bi-twin-free \(3\times3\) relations is
\[
A=\begin{pmatrix}1&1&1\\1&1&0\\1&0&0\end{pmatrix},
\qquad
B=\begin{pmatrix}1&1&1\\1&0&1\\1&1&0\end{pmatrix}.
\]
There are exactly eight side-preserving isomorphism classes of bi-twin-free \(3\times3\) relations and exactly seven ordered dual-Dowker signatures; the signature shared by \(A\) and \(B\) is the pair of full \(2\)-simplices.

## Assumptions and scope
A relation isomorphism is required to preserve the two sides: it is a pair of bijections \(X\to X'\) and \(Y\to Y'\) carrying incidence to incidence. The twin-free hypothesis removes the immediate information loss caused by duplicated rows or columns, while nonempty neighborhoods remove isolated vertices that do not appear in a Dowker complex. The result concerns the two *unweighted* Dowker complexes together; weighted Dowker complexes and cosheaf representations contain more information.

## Proof
For minimality, first suppose one side has one element. Bi-twin-freeness then forces the other side to have at most one element. Suppose next that \(|X|=2\). Distinct nonempty column neighborhoods are distinct nonempty subsets of a two-element set, so \(|Y|\le3\).

For \(2\times2\), there are exactly two bi-twin-free relation types up to row and column permutations. One is the permutation matrix, for which both Dowker complexes are two isolated vertices. The other is the three-incidence matrix, for which both Dowker complexes are a full \(1\)-simplex. Their ordered dual-Dowker signatures are different. For \(2\times3\), three distinct nonempty column neighborhoods must be exactly the three nonempty subsets of the two rows, so the relation is unique up to row and column permutations. The transposed cases are identical. Hence no collision occurs when \(|X|+|Y|<6\).

For the displayed \(3\times3\) relations, every row neighborhood and every column neighborhood is nonempty and pairwise distinct. Each matrix has a column incident to all three rows, so \(D_X\) is a full \(2\)-simplex; each also has a row incident to all three columns, so \(D_Y\) is a full \(2\)-simplex. Nevertheless \(A\) and \(B\) are not side-preservingly isomorphic because row permutations and column permutations preserve the multiset of row degrees, which is \({1,2,3}\) for \(A\) and \({2,2,3}\) for \(B\).

The remaining finite statement is exhaustive. The bundled verifier enumerates all \(2^9=512\) binary \(3\times3\) matrices, keeps exactly the 174 labeled bi-twin-free matrices, quotients them by all \(3!\cdot3!\) row-column permutations, and obtains eight relation classes. It independently canonizes \(D_X\) and \(D_Y\) under all vertex permutations. The resulting seven signatures have multiplicities \(1,1,1,1,1,1,2\), and the sole size-two fiber has canonical matrix strings `001011111` and `011101111`, which are precisely \(A\) and \(B\) up to ordering conventions.

## Verification
Run `python verify_dual_dowker.py`. It exhaustively checks every bi-twin-free relation with total side size below six, verifies that every ordered dual-Dowker signature is unique there, and then verifies the complete \(3\times3\) census. It also checks the two degree multisets and that both complexes in the collision are full \(2\)-simplices. A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Robinson proves that the ordinary Dowker-complex functor is non-faithful and that integer weights, or equivalently richer cosheaf data, recover the relation up to isomorphism. The same paper shows that the cosheaf representation contains the dual Dowker complex as its space of global cosections. Those results establish why enrichment can restore information, but they do not state that retaining *both unweighted dual complexes* still fails after row and column twins are removed, nor do they identify the smallest such failure. Brun and Salbu introduce the rectangle complex and use it to relate the two Dowker complexes functorially; their construction keeps the incidence relation as its vertex set and therefore does not imply reconstruction from the two projected complexes alone. Later work on higher-order Dowker relations likewise treats duality and relational products rather than this minimal reconstruction boundary.

## Limitations
The classification is only a minimal finite boundary and the complete \(3\times3\) case; it does not classify larger fibers of the map from relations to pairs of Dowker complexes. The adjective bi-twin-free is defined here explicitly and is not asserted to be standard terminology. Originality was checked against the most directly relevant Dowker/cosheaf and rectangle-complex literature and semantic-index searches, but obscure equivalent formulations in formal concept analysis remain a residual literature risk.

## References
1. M. Robinson, “Cosheaf representations of relations and Dowker complexes,” arXiv:2005.12348, first submitted 2020-05-26; Journal of Applied and Computational Topology 6 (2022), 27–63, DOI 10.1007/s41468-021-00078-y.
2. M. Brun and L. M. Salbu, “The Rectangle Complex of a Relation,” Mediterranean Journal of Mathematics 20 (2023), article 7, DOI 10.1007/s00009-022-02213-0.
3. V. de Silva et al., “Dowker’s theorem for higher-order relations,” Journal of Applied and Computational Topology (2026), DOI 10.1007/s41468-026-00239-x.

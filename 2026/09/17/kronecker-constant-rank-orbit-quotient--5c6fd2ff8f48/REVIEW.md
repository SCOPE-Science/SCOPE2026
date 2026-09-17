# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The core correspondence can be checked directly from the representation-isomorphism equations. With the ordered arrows fixed, an elementary representation \(M\) determines an injective map
\[
M_1\to M_{n\times y}(k),\qquad m\mapsto A_m.
\]
A source change of basis only reparametrizes this image. A sink change of basis right-multiplies the entire image by one element of \(GL_y\). Conversely, a right \(GL_y\)-translate is implemented by a sink isomorphism, and any two choices of the source-to-\(H\) identification differ by a source isomorphism. Hence the fixed-arrow quotient is exactly \(\mathcal C_{x,y}/GL_y\).

A change of arrow basis forms linear combinations of the rows of every stacked matrix, giving the additional left \(GL_n\)-action. This establishes the double quotient for arrow-space orbits.

The \(K_3\) counterexample was checked independently at the level of matrices. For
\[
A(a,b)=\begin{bmatrix}a&0\\b&a\\0&b\end{bmatrix}
\]
the \(2\times2\) minors are \(a^2,ab,b^2\), so every nonzero element has rank two over any field. Swapping the first two rows preserves the constant-rank property but changes the fixed-arrow rank pattern from \((1,2,1)\) to \((2,1,1)\). Because each individual arrow rank is invariant under a representation isomorphism, the two modules are not isomorphic. Both satisfy the full-rank criterion used by Liu for elementary modules in the \(x<n\) regime.

No hidden characteristic assumption is used in this counterexample beyond the ambient assumptions of the cited results.

## Originality

**PASS, to the best of our knowledge.**

The 2023 published article explicitly states that when \(x+y=n+1\), an elementary module is of the form \(X(x,y)\). Its proof identifies two maximal constant-rank spaces after observing only that they have the same dimension; this does not justify equality or a basis-change relation in the common ambient matrix space. The explicit \(K_3\) example contradicts the literal fixed-arrow uniqueness statement.

The 2026 preprint states a bijection between elementary modules and maximal fixed-rank spaces "under the isomorphisms" but does not define the matrix-space equivalence relation. The corrected orbit statement distinguishes the right \(GL_y\) quotient from standard left-right matrix-space equivalence.

Bissinger (2025) explicitly treats the \(GL(A_n)\)-action changing the arrow basis separately from ordinary representation isomorphism, supporting the distinction but not, in the material inspected, stating this constant-rank orbit correction.

Searches for the 2023 title together with correction/erratum terms, for the 2026 title together with matrix-space equivalence, and for Kronecker constant-rank orbit classifications found no prior correction matching the statement here.

### Residual literature risk

Westwick, *Spaces of matrices of fixed rank*, Linear and Multilinear Algebra 20 (1987), DOI 10.1080/03081088708817751, was identified as a foundational source for maximal fixed-rank subspaces. Its full text was not inspected. It could contain conventions for equivalence of matrix spaces, but it predates the Kronecker-module claims at issue and is not known from the inspected metadata to formulate the representation-theoretic quotient. Because the 2026 preprint is recent, a concurrent author revision or independent correction is also possible.

## Value

**PASS.**

The correction prevents two distinct classification problems from being conflated. For fixed-arrow representation theory, the relevant moduli problem is the right-\(GL_y\) quotient. The familiar left-right quotient of constant-rank matrix spaces instead classifies after additionally forgetting the chosen basis of the Kronecker arrow space. This changes the number and geometry of isomorphism classes and explains why a single standard matrix-space orbit need not be a single module-isomorphism class.

The \(K_3\) example gives a minimal, explicit witness and directly resolves the ambiguity in the recent correspondence.

## Scope of the claim

This record does not claim novelty for matrix-space equivalence itself, for the general \(GL(A_n)\)-action on Kronecker representations, or for constant-rank spaces. It claims the orbit-level correction and its application to the cited elementary-module classification statements.

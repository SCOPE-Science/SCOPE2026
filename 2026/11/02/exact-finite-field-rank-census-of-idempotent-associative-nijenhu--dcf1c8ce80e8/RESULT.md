# Exact finite-field rank census of idempotent associative Nijenhuis operators on two-by-two matrices

## Finding
For every prime power \(q\), put \(k=\mathbb F_q\), \(A=M_2(k)\), and let \(\mathcal N_q\) consist of all \(k\)-linear maps \(P:A\to A\) obeying \(P^2=P\) and the associative Nijenhuis identity
\[
P(X)P(Y)=P(P(X)Y+XP(Y)-P(XY))\qquad(X,Y\in A).
\]
The rank-generating polynomial, over the original four-dimensional \(k\)-space \(A\), is exactly
\[
\boxed{\sum_{P\in\mathcal N_q}T^{\operatorname{rank}P}
=1+q^2(q+1)(T+T^3)+2q(q+1)(2q+1)T^2+T^4.}
\]
Thus \(\lvert\mathcal N_q\rvert=2+2q(q+1)(3q+1)\). This includes \(q\) even. As further structural data, among the rank-two projections exactly \(4q^2(q+1)\) have exactly one of their image/kernel subalgebras containing the ambient identity, and exactly \(2q(q+1)\) have neither containing that identity.

## Assumptions and scope
The field \(k\) is any finite field of order \(q\ge2\). A subalgebra means a \(k\)-linear subspace closed under ordinary matrix multiplication; it need not contain the identity of \(A\). The rank of \(P\) is the vector-space dimension of its image, in \(\{0,1,2,3,4\}\). All operators are counted as distinct linear maps, not up to conjugation. The identity above is the associative Nijenhuis identity, not the Lie-bracket Nijenhuis identity or a weight-zero Rota--Baxter identity. The equivalent Rota--Baxter formulation is the *splitting operator* of weight minus one.

## Proof
**Step 1 (reduction to ordered subalgebras).** For an idempotent linear operator \(P\), the vector space splits as \(A=U\oplus W\), where \(U=\operatorname{im}P\) and \(W=\ker P\). If the displayed identity holds, substituting \(X,Y\in U\) gives \(XY=P(XY)\), hence \(U\) is closed under multiplication. Substituting \(X,Y\in W\) gives \(P(XY)=0\), hence \(W\) is closed. Conversely, if \(U,W\) are subalgebras, use \(X=X_U+X_W\) and \(Y=Y_U+Y_W\): after canceling mixed terms and projecting products in \(U\) and \(W\), the right side is \(X_UY_U=P(X)P(Y)\). The argument does not divide by two and holds in all characteristics. Consequently the rank-\(r\) operator count equals the number of **ordered** complementary subalgebra pairs \((U,W)\) with \(\dim U=r\).

**Step 2 (one-dimensional and three-dimensional factors).** A nonzero \(2\times2\) matrix with determinant zero satisfies \(X^2=\operatorname{tr}(X)X\), so its line is a one-dimensional subalgebra. If a one-dimensional subalgebra line \(kX\) complements a three-dimensional subalgebra, it cannot contain an invertible matrix, because the inverse of \(X\) lies in \(k[X]\), so \(I\in kX\), contradicting complementarity to any three-dimensional subalgebra containing \(I\).

For completeness, every three-dimensional subalgebra of \(M_2(k)\) is a Borel subalgebra stabilizing a line in \(k^2\). Indeed, a subspace consisting entirely of singular \(2\times2\) matrices has dimension at most two: two independent rank-one matrices with determinant-zero sum must share an image line or kernel line (the determinant of their sum is the product of the two corresponding \(2\times2\) determinants); a third matrix mixing those two types would give an invertible sum. Hence a three-dimensional subalgebra contains an invertible element and therefore contains \(I\), by Cayley--Hamilton. It is noncommutative, since the centralizer of a nonscalar \(2\times2\) matrix has dimension two. A semisimple associative algebra of dimension three over a finite field is commutative (indeed a product of finite extensions of \(k\)), so the Jacobson radical of the three-dimensional algebra is nonzero. That radical consists of nilpotent matrices and must be one-dimensional, because a two-dimensional linear subspace consisting entirely of nilpotent \(2\times2\) matrices cannot exist: after choosing one nonzero nilpotent \(E_{12}\), the coefficient of \(t\) in the determinant of \(E_{12}+tB\) forces the lower-left entry of \(B\) to vanish; trace and determinant then force \(B\in kE_{12}\), in any characteristic. Conjugating the radical to \(kE_{12}\), the ideal condition \(XE_{12},E_{12}X\in kE_{12}\) forces every element \(X\) of the subalgebra to be upper triangular. Equality of dimensions gives exactly that Borel. There are \(q+1\) Borels, one for each line in \(k^2\).

For the upper triangular Borel \(B\), a complementary one-dimensional subalgebra line is spanned by a singular matrix with nonzero lower-left entry. Scaling the latter to one and imposing determinant zero gives the **unique** representative
\[
X=\begin{pmatrix}a&ad\\1&d\end{pmatrix},\qquad a,d\in k.
\]
Each such line is a subalgebra by Cayley--Hamilton, and there are exactly \(q^2\) of them. Thus the rank-one and rank-three counts are each \(q^2(q+1)\). The zero and identity operators are the unique cases of ranks zero and four.

**Step 3 (all two-dimensional subalgebras).** If a two-dimensional subalgebra \(S\) contains \(I\), it has the form \(k[I,X]\) for a nonscalar \(X\). Its quadratic minimal polynomial yields precisely three types, with the following exact numbers of distinct subalgebras:
\[
\begin{array}{c|c|c}
\text{type of }S & \#S & \text{number of ambient-nonunital two-dimensional complements}\ \hline
k_{q^2}\text{ (quadratic field)}&q(q-1)/2&2(q+1)\\
k\times k\text{ (split)}&q(q+1)/2&2(q-1)\\
k[\varepsilon]/(\varepsilon^2)\text{ (dual numbers)}&q+1&2q
\end{array}
\]
Here \(k_{q^2}\) denotes the unique degree-two extension field of \(k\). To obtain the counts in the middle column, count respectively irreducible quadratic multiplication algebras, unordered pairs of distinct rational eigenlines, and nonzero nilpotent lines; the first is \(q(q-1)/2\), the second \(\binom{q+1}{2}\), and the third \(q+1\). These three classes exhaust all two-dimensional subalgebras containing the ambient identity.

Any two-dimensional subalgebra not containing \(I\) contains no invertible matrix, hence is a two-dimensional singular matrix subspace. The rank-one determinant argument shows that such subspaces are exactly the \(q+1\) spaces \(L_\ell\) of matrices with image contained in a fixed rational line \(\ell\subset k^2\) and the \(q+1\) spaces \(K_\ell\) of matrices killing a fixed rational line. They are associative subalgebras, all distinct; the two families have \(2(q+1)\) members in total.

For a fixed identity-containing \(S\), a space \(L_\ell\) intersects \(S\) nontrivially exactly when \(S\) contains a nonzero singular matrix of image \(\ell\); similarly \(K_\ell\) meets \(S\) exactly when such a matrix has kernel \(\ell\). The three algebra types have respectively zero, two, and one rational rank-one image lines (and the same number of kernel lines). Excluding these forbidden lines in each of the two families gives the last column. Therefore the number of ordered rank-two complementary pairs with exactly one identity-containing factor equals
\[
2\left[\frac{q(q-1)}2\cdot2(q+1)+\frac{q(q+1)}2\cdot2(q-1)+(q+1)\cdot2q\right]
=4q^2(q+1).
\]
For pairs containing no ambient identity, two distinct image-line subalgebras complement one another, as do two distinct kernel-line subalgebras. An image-line space and a kernel-line space have a one-dimensional intersection and cannot be complementary. Consequently, the number of ordered pairs of this type is \(2(q+1)q=2q(q+1)\). Adding yields \(2q(q+1)(2q+1)\) rank-two projections, proving the formula.

## Verification
The standalone program `check_nijenhuis.py` constructs all four-dimensional vector-space subspaces in reduced row echelon form, filters them by closure under original matrix multiplication, and enumerates **all** ordered complementary subalgebra pairs for \(q=2,3,4,5,8\). The extension fields of orders four and eight use irreducible binary-polynomial multiplication. It verifies subalgebra-type frequencies and every coefficient of the rank polynomial. Independently, for \(q=2\), it tests all \(2^{16}=65536\) linear endomorphisms directly against \(P^2=P\) and the original associative Nijenhuis identity, recovering the same ranks. The exact run output is in `checker_output.txt`. These finite exhaustive tests corroborate but do not replace the all-prime-power proof.

The verified rank-count tuples for \(q=2,3,4,5,8\), in order of ranks zero through four, are \((1,12,60,12,1)\), \((1,36,168,36,1)\), \((1,80,360,80,1)\), \((1,150,660,150,1)\), and \((1,576,2448,576,1)\).

## Relationship to prior work
Cariñena, Grabowski, and Marmo (2006) define associative Nijenhuis tensors and explicitly show that projections arising from direct-sum subalgebra decompositions are Nijenhuis tensors. The equivalence for an idempotent is an elementary converse, so neither correspondence nor the classification of splitting operators is claimed as new. Benito, Gubarev, and Pozhidaev (2018) state the general splitting Rota--Baxter/direct-decomposition bijection and classify certain Rota--Baxter operators on two-by-two matrices; Goncharov and Gubarev (2019) clarify the complex-field classification, and Gubarev (2023) explicitly acknowledges the earlier complete complex-field decomposition classification for \(M_2(\mathbb C)\). These works are substantial antecedents. The assessed contribution is the **exact rank-sensitive count of actual operators over every finite field**, including characteristic two and the quadratic-extension subalgebra type, without claiming new geometric classification over an algebraic closure. No identical finite-field polynomial was identified in the inspected sources or mathematical-result searches; this is not a proof of global publication priority.

## Limitations
The theorem only treats idempotent associative Nijenhuis operators on \(M_2\); neither arbitrary Nijenhuis maps nor higher matrix dimensions are addressed. This is a raw operator census rather than a conjugacy-orbit classification. The subalgebra correspondence and complex-field decomposition classification are previously known, and the finite-field enumeration may be derivable from a broader unlocated arithmetic theorem. Independent validation of the claimed priority and mathematical details has not been performed.

## References
1. J. F. Cariñena, J. Grabowski, G. Marmo, *Quantum Bi-Hamiltonian Systems*, arXiv:math-ph/0610011 (first public preprint October 6, 2006), Section 3, especially the decomposition/projection construction. https://arxiv.org/abs/math-ph/0610011
2. P. Benito, V. Gubarev, A. Pozhidaev, *Rota-Baxter Operators on Quadratic Algebras*, arXiv:1801.07037 (January 22, 2018), Section 2 on splitting Rota--Baxter operators and Section 5 on matrix algebras. https://arxiv.org/abs/1801.07037
3. M. Goncharov, V. Gubarev, *Rota-Baxter operators of nonzero weight on the matrix algebra of order three*, arXiv:1911.13020 (November 29, 2019), Section 3 and the two-dimensional complex case. https://arxiv.org/abs/1911.13020
4. V. Gubarev, *Nonunital decompositions of the matrix algebra of order three*, arXiv:2308.16455 (August 31, 2023), introduction acknowledging the earlier \(M_2(\mathbb C)\) classification. https://arxiv.org/abs/2308.16455

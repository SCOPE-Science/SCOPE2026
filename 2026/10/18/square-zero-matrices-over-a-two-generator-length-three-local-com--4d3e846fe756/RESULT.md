# Square-zero matrices over a two-generator length-three local complete intersection

## Finding

For any field \(k\), consider the four-dimensional commutative local complete intersection
\[
R=k[u,v]/(u^2,v^2),\qquad \mathfrak m=(u,v),\qquad \mathfrak m^2=(uv)\ne0,\quad \mathfrak m^3=0.
\]
Let \(X_k\) be the **reduced** affine variety of solutions \(T^2=0\) in \(M_2(R)\), considered via the sixteen coefficient coordinates of \(T\) over \(k\). In \(K_0(\operatorname{Var}_k)\), put \(\mathbb L=[\mathbb A_k^1]\). Then
\[
[X_k]=\begin{cases}
\mathbb L^9+4\mathbb L^8-2\mathbb L^7-3\mathbb L^6+\mathbb L^5,&\operatorname{char}k\ne2,\\
\mathbb L^{10}+\mathbb L^9+\mathbb L^8-\mathbb L^7-\mathbb L^6,&\operatorname{char}k=2.
\end{cases}
\]
The dimensions of these reduced varieties are respectively \(9\) and \(10\). Over every finite field \(k=\mathbb F_q\), the exact labeled solution count is
\[
|X_k(k)|=\begin{cases}
q^9+4q^8-2q^7-3q^6+q^5,&q\text{ odd},\\
q^{10}+q^9+q^8-q^7-q^6,&q\text{ even}.
\end{cases}
\]
Replacing \(q\) by \(q^e\) gives the point counts over every finite extension of \(k\).

## Assumptions and scope

No characteristic restriction is imposed on \(k\). The algebra \(R\) has ordered basis \((1,u,v,uv)\), and the matrix entries commute. The objects counted are **labeled** matrices, not similarity classes. The class identity is an identity of reduced varieties and does not imply reducedness of the original zero-scheme of the four matrix-square equations. No assertion concerning irreducible components is needed.

## Proof

Write uniquely
\[
T=A+uB+vC+uvD,\qquad A,B,C,D\in M_2(k),
\]
and write \(\{P,Q\}=PQ+QP\) for the anticommutator. Expanding \(T^2\) in the displayed basis gives the equivalent system
\[
A^2=0,\qquad \{A,B\}=0,\qquad \{A,C\}=0,\qquad \{A,D\}+\{B,C\}=0.\tag{1}
\]

**Nonzero reduction.** If \(A\ne0\) and \(A^2=0\), then \(A\) has rank one and is conjugate over \(k\) to \(J=E_{12}\). The rank-one nilpotent orbit has class \(\mathbb L^2-1\): its projectivization is the split nonsingular conic parametrizing \(\operatorname{im}A=\ker A\), hence \(\mathbb P^1\), and each projective point has a \(\mathbb G_m\)-fiber. Equivalently, its finite-field size is \(q^2-1\). For \(Z=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), direct multiplication yields
\[
\{J,Z\}=\begin{pmatrix}c&a+d\\0&c\end{pmatrix},\quad
\operatorname{im}(\{J,-\})=\operatorname{span}_k\{I,J\},\quad
\ker(\{J,-\})=\left\{\begin{pmatrix}a&b\\0&-a\end{pmatrix}:a,b\in k\right\}.
\]
Thus \(B,C\) are arbitrary in a pair of two-dimensional kernels. For \(B=\left(\begin{smallmatrix}a&b\\0&-a\end{smallmatrix}\right)\) and \(C=\left(\begin{smallmatrix}c&d\\0&-c\end{smallmatrix}\right)\), one has \(\{B,C\}=2acI\), which lies in the displayed image in every characteristic (it is zero in characteristic two). Equation (1) therefore admits an affine two-plane of choices for \(D\). Since the linear maps have constant ranks and local conjugation charts exist on the nonzero nilpotent orbit, this yields a Zariski-locally trivial affine-six-space bundle of class
\[
[X_k\mid A\ne0]=(\mathbb L^2-1)\mathbb L^6.\tag{2}
\]
Its dimension is eight.

**Zero reduction.** For \(A=0\), the matrix \(D\) is unrestricted, and only \(\{B,C\}=0\) remains. Write \(Y_k=\{(B,C)\in M_2(k)^2:BC+CB=0\}_{\mathrm{red}}\). Then
\[
[X_k\mid A=0]=\mathbb L^4[Y_k].\tag{3}
\]

For \(\operatorname{char}k\ne2\), fix \(B\). The linear operator \(C\mapsto BC+CB\) has kernel dimension four if \(B=0\); dimension two if \(\operatorname{tr}B=0\) and \(B\ne0\); dimension one if \(\operatorname{tr}B\ne0\) and \(\det B=0\); and dimension zero otherwise. Indeed, a traceless nonzero two-by-two matrix has anticommutator-map rank two (check the nonzero nilpotent Jordan form and the semisimple form after extending scalars). For nonzero trace and zero determinant it is similar to \(\operatorname{diag}(0,t)\) with \(t\ne0\), giving the one-dimensional kernel. In the remaining case the determinant of the anticommutator operator is nonzero (its four eigenvalues after algebraic closure are \(2\lambda_1,2\lambda_2,\lambda_1+\lambda_2,\lambda_1+\lambda_2\)). The four loci of \(B\) have classes respectively
\[
1,\quad \mathbb L^3-1,\quad \mathbb L(\mathbb L^2-1),\quad \mathbb L^4-\mathbb L^3-\mathbb L(\mathbb L^2-1).
\]
For the third class, a rank-one matrix with nonzero trace is determined by a nonzero eigenvalue and a rank-one projector; the projector variety is the complement of the diagonal in \(\mathbb P^1\times\mathbb P^1\), of class \(\mathbb L^2+\mathbb L\). Every constant-rank kernel forms a vector bundle over its locus. Summing these fiber classes yields
\[
[Y_k]=\mathbb L^4+(\mathbb L^3-1)\mathbb L^2+\mathbb L(\mathbb L^2-1)\mathbb L+(\mathbb L^4-2\mathbb L^3+\mathbb L)
=\mathbb L^5+3\mathbb L^4-2\mathbb L^3-2\mathbb L^2+\mathbb L.\tag{4}
\]

In \(\operatorname{char}k=2\), anticommutation means commutation. The centralizer of a scalar matrix has dimension four and the centralizer of every nonscalar two-by-two matrix has dimension two (its minimal polynomial has degree two). Scalar matrices have class \(\mathbb L\); the nonscalar locus has class \(\mathbb L^4-\mathbb L\). Therefore
\[
[Y_k]=\mathbb L\cdot\mathbb L^4+(\mathbb L^4-\mathbb L)\mathbb L^2
=\mathbb L^6+\mathbb L^5-\mathbb L^3.\tag{5}
\]
Combining (2), (3), (4), and (5) proves the stated motivic identities and finite-field counts.

Finally, in odd characteristic the locus \(A=0,\operatorname{tr}B=0,B\ne0\) has dimension \(3+2+4=9\), strictly exceeding the other loci, which have dimensions at most eight. In characteristic two, \(A=0,B\text{ nonscalar}\) has dimension \(4+2+4=10\), strictly exceeding the other loci, which have dimensions at most nine. Constant-rank bundle descriptions ensure these dimensions are exact, proving the geometric dimension jump.

## Verification

A standalone C11 verifier, `verify.c`, works directly in the sixteen-entry coefficient coordinate system, with multiplication computed from \(u^2=v^2=0\). It exhaustively enumerates every two-by-two matrix over \(\mathbb F_2[u,v]/(u^2,v^2)\) and \(\mathbb F_3[u,v]/(u^2,v^2)\), then independently exhausts the finite-field anticommuting-pair equation over prime fields of orders two, three, five, and seven. It returns `VERIFY_OK` if and only if all counts match. Compile with `cc -O3 -std=c11 -Wall -Wextra verify.c -o verify && ./verify`.

The computed full counts were \(1600\) for \(q=2\) and \(39609\) for \(q=3\). The computed anticommuting-pair counts were \(88,417,4705,23233\) for \(q=2,3,5,7\) respectively. Finite enumeration is only a check; the class and dimension arguments above prove the theorem for arbitrary fields.

## Relationship to prior work

Prasad, Singla, and Spallone (arXiv:1212.6157; first made public 2012-12-26) classify similarity and centralizers of matrices over length-two local principal ideal rings. Their Section 10 treats nonprincipal local rings under the explicit hypothesis that the maximal ideal squares to zero; our nonprincipal ring satisfies \(\mathfrak m^2\ne0\) and has Loewy length three. Their framework does not state or imply the present matrix-square-zero fiber calculation. Chen and Wang (arXiv:1805.00378; first made public 2018-05-01), study the complex anticommuting-pair variety, which is the known geometric ingredient \(Y_k\) occurring on the zero-reduction stratum of this proof. The present claim is **not** novelty of the complex anticommuting-pair variety; the contribution claimed is the exact lifting to the nonchain four-dimensional coefficient ring, the characteristic-dependent motivic classes, and complete finite-field counts. Ekhad and Zeilberger (1995, DOI:10.37236/1226) count square-zero **upper triangular** matrices over finite fields, a different family. Direct comparison with these results and related published records identified no covering implication; exhaustive uniqueness is not claimed.

## Limitations

This is a theorem about the **reduced** underlying solution variety and its rational points. It does not imply that the scheme defined by \(T^2=0\) is reduced, determine a primary decomposition of its defining ideal, or classify the irreducible components. The result fixes the coefficient algebra and matrix size; extension to larger matrices or other nonchain local rings is not proved. Though inspected sources and research records did not show the same formula, a pre-existing equivalent or stronger result in unlocated literature remains a possibility.

## References

1. A. Prasad, P. Singla, S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157v1, publicly submitted 2012-12-26. Full text: https://arxiv.org/html/1212.6157v2 (especially Sections 1, 10).
2. X. Chen, W. Wang, *Anti-commuting varieties*, arXiv:1805.00378v1, publicly submitted 2018-05-01. Full text: https://arxiv.org/html/1805.00378v2 (Section 1, theorem context).
3. S. B. Ekhad, D. Zeilberger, *The Number of Solutions of \(X^2=0\) in Triangular Matrices Over \(GF(q)\)*, Electronic Journal of Combinatorics, 1995, DOI:10.37236/1226; https://www.combinatorics.org/ojs/index.php/eljc/article/view/v3i1r2.

# Complete zero-product spectrum of two-by-two finite matrix rings

## Finding

For every prime power \(q\ge 2\), let \(R=M_2(\mathbb F_q)\). Define the simple undirected zero-divisor graph \(\Gamma(R)\) to have vertices all nonzero singular matrices and an edge between distinct vertices \(X,Y\) if and only if \(XY=0\) or \(YX=0\). Write \(A_q\) for its real adjacency matrix and \(z\) for an indeterminate. Set

\[
P_q(z)=z^2-(2q(q-1)-1)z-(q-1)(2q^2+q-2),
\]
\[
Q_q(z)=z^2-q(q-2)z-(q-1)(q^2-2).
\]

**Theorem (complete characteristic polynomial).** For every prime power \(q\ge2\), including powers of two,

\[
\boxed{\begin{aligned}
\det(zI-A_q)={}&z^{q(q+1)(q-2)}(z+1)^{(q+1)(q-2)}P_q(z)Q_q(z)^q\\
&\cdot(z+q(q-1))^q(z+q-1)^{(q+1)(q-2)/2}(z-q+1)^{q(q-1)/2}.
\end{aligned}}
\]

Thus all eigenvalues, with multiplicities, are determined by two explicit quadratic equations and three explicit linear factors, together with the zero and negative-one factors. The following consequences are exact, not merely lower/upper bounds:

\[
\operatorname{nullity}(A_q)=q(q+1)(q-2),\qquad
\operatorname{rank}(A_q)=(q+1)(2q-1).
\]

The multiplicity of eigenvalue \(-1\) is exactly \((q+1)(q-2)\). Its inertia (numbers of positive, negative and zero eigenvalues, respectively) is

\[
\left(1+\frac{q(q+1)}2,\ \frac{(q+1)(3q-2)}2-1,\ q(q+1)(q-2)\right).
\]

The energy (sum of absolute adjacency eigenvalues) is

\[
\boxed{\mathcal E(\Gamma(R))
=\sqrt{4q^4-4q^2-8q+9}+q\sqrt{q^4-8q+8}
+(2q+1)(q-1)^2+(q+1)(q-2).}
\]

## Assumptions and scope

All vector-space and spectral calculations are over \(\mathbb R\), whereas the ring matrices themselves are over the finite field \(\mathbb F_q\). There is no assumption that \(q\) is odd or prime rather than a prime power. The graph excludes zero and all units. Adjacency is **symmetrized**: either zero product suffices. Only distinct matrices are adjacent, so the graph has no loops. This is not the quaternion ring modulo an even integer; that different ring does not generally identify with \(M_2(\mathbb F_q)\).

When \(q=2\), factors raised to exponent zero are interpreted as one. The graph has \((q-1)(q+1)^2\) vertices. The rank and nullity refer to the ordinary real adjacency matrix, not minimum graph rank over arbitrary zero patterns or rank over the coefficient field.

## Proof

**1. Ring-theoretic type decomposition.** Put \(n=q+1\) and \(s=q-1\). Every vertex has rank one, and therefore an image line and a kernel line in the \(n\)-element projective line \(\mathbb P^1(\mathbb F_q)\). Index the lines by \(1,\ldots,n\), and denote the type of a vertex by \((i,j)\), with kernel \(i\) and image \(j\). For each ordered type, there are exactly \(s\) matrices: they are the nonzero maps from a one-dimensional quotient to a one-dimensional image. For matrices of types \((i,j)\) and \((k,l)\), the product in that order is zero precisely when \(l=i\); the reverse product is zero precisely when \(j=k\). Hence, for **distinct vertices**, their adjacency criterion depends only on types and is \(j=k\) or \(l=i\).

Within a diagonal type \((i,i)\), all distinct elements are adjacent; within an off-diagonal type \((i,j)\), \(i\ne j\), none are. With \(H_{ij,kl}=\mathbf 1_{j=k\ \mathrm{or}\ l=i}\) and diagonal type projection \((Df)_{ij}=\mathbf 1_{i=j}f_{ii}\), the adjacency matrix is permutation-similar to \(H\otimes J_s-D\otimes I_s\). The class-constant subspace, of dimension \(n^2\), carries \(B=sH-D\). The within-class sum-zero spaces contribute \(0\) with multiplicity \(n(n-1)(s-1)\) and \(-1\) with multiplicity \(n(s-1)\). Consequently

\[
\det(zI-A_q)=z^{n(n-1)(s-1)}(z+1)^{n(s-1)}\det(zI-B).
\]

This reduction is restated here as a direct consequence of multiplication in the matrix ring, not assumed from a numerical spectrum.

**2. The entire reduced operator.** Identify the class-constant space with all real \(n\times n\) arrays \(f=(f_{ij})\), and write \(r_i=\sum_j f_{ij}\), \(c_i=\sum_j f_{ji}\). Inclusion-exclusion for the union \(j=k\) or \(l=i\) gives the explicit identity

\[
(Bf)_{ij}=s(r_j+c_i-f_{ji})-\mathbf1_{i=j}f_{ii}. \tag{1}
\]

The symmetric and skew-symmetric arrays are both invariant under \(B\). On skew arrays of the form \(f_{ij}=a_i-a_j\), with \(\sum_i a_i=0\), formula (1) gives eigenvalue \(-s(n-1)\), with multiplicity \(n-1\). On skew arrays whose row sums all vanish, formula (1) gives eigenvalue \(+s\), with dimension \((n-1)(n-2)/2\). Those two spaces span all skew arrays: their dimensions sum to \(n(n-1)/2\) and the zero-row-sum constraint has rank \(n-1\).

On symmetric arrays, consider the two constant patterns \(I\) (ones on the diagonal) and \(F=J-I\) (ones off the diagonal). In this ordered basis, equation (1) acts by

\[
T_0=\begin{pmatrix}s-1&2s(n-1)\\2s&s(2n-3)\end{pmatrix}.
\]

Next, for each vector \(a=(a_i)\) satisfying \(\sum_i a_i=0\), define the diagonal array \(D(a)_{ii}=a_i\), zero elsewhere, and the symmetric off-diagonal array \(S(a)_{ij}=a_i+a_j\) for \(i\ne j\), zero on the diagonal. For each of the \(n-1\) independent zero-sum choices of \(a\), the span of \(D(a),S(a)\) is invariant and equation (1) acts as

\[
T_1=\begin{pmatrix}s-1&2s(n-2)\\s&s(n-3)\end{pmatrix}.
\]

Finally, the symmetric, zero-diagonal arrays with zero row sums form a subspace of dimension \(n(n-3)/2\). Formula (1) acts on it by \(-s\). The row-sum map on symmetric off-diagonal arrays has full rank \(n\) for \(n\ge3\) (its transpose sends a vector \(a\) to all sums \(a_i+a_j\); all such sums can vanish only for \(a=0\)). This proves the stated dimension. It also shows the symmetric spaces described above form a direct sum, as may be checked by the diagonal and row-sum constraints; the dimensions total \(n(n+1)/2\). Together with the skew spaces, this exhausts all \(n^2\) dimensions.

**3. Characteristic polynomials of the small blocks.** Substituting \(s=q-1\), \(n=q+1\) into \(\det(zI-T_0)\) gives \(P_q(z)\). Substituting in \(\det(zI-T_1)\) gives \(Q_q(z)\). The remaining reduced eigenvalues are \(-q(q-1)\) with multiplicity \(q\), \(-(q-1)\) with multiplicity \((q+1)(q-2)/2\), and \(q-1\) with multiplicity \(q(q-1)/2\). Multiply those factors and then the sum-zero within-class factors from Step 1 to obtain the boxed characteristic polynomial. The exponents add to \((q-1)(q+1)^2\), the exact vertex count.

**4. Rank, inertia, and energy.** Neither quadratic has zero as a root because both constant terms are strictly negative for \(q\ge2\); the three linear reduced roots are nonzero. Thus the only zero eigenvalues are the within-class ones, proving rank and nullity. Both quadratic factors have one positive and one negative real root because their constant terms are negative. Counting signs gives the stated inertia. Neither quadratic vanishes at \(-1\), and no linear reduced factor contributes \(-1\) for \(q\ge2\) except the factor \(z+q-1\) when \(q=2\), whose exponent then equals zero; hence the claimed exact negative-one multiplicity. The sum of absolute values of the two roots of a quadratic with negative constant term equals the square root of its discriminant. The discriminants are \(4q^4-4q^2-8q+9\) and \(q^4-8q+8\); adding the absolute contributions of every remaining factor gives the energy identity.

## Verification

Run the standalone standard-library checker: `python3 verify.py`. It implements arithmetic in \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), including a polynomial-basis realization of the quadratic extension at \(q=4\). It constructs every nonzero singular matrix, recomputes adjacency from both matrix products, independently determines kernel/image types, and checks the complete type-incidence rule. It then computes **exact integer characteristic polynomials** of the reduced operators for all four fields by Faddeev–LeVerrier; it also computes the full graph characteristic polynomials for \(q=2,3\). Every computed coefficient matches the theorem. The expected final output is `VERIFY_OK`.

These finite tests are supporting evidence only. The theorem for unbounded field orders follows from Steps 1–4, and no experiment is used as an infinite proof.

## Relationship to prior work

Rather, *Block Structure and Spectrum of Zero-Divisor Graphs of Lipschitz Quaternion Rings Modulo* \(n\), arXiv:2603.20947v1 (public March 21, 2026), proves the kernel/image type block decomposition for the quaternion rings at **odd prime** modulus, which are isomorphic to \(M_2(\mathbb F_p)\). His Theorem 4.1 reduces the uncomputed part of the spectrum to a matrix of order \((p+1)^2\), Corollary 4.2 gives **lower** bounds for nullity and negative-one multiplicity, and Theorem 4.4 finds the spectral radius from a two-cell quotient. The present calculation explicitly diagonalizes the entire remaining quotient, proves the bounds exact, supplies inertia/energy, and holds for every prime-power field order (not to be confused with an even-modulus quaternion ring).

Masalkar, Khairnar, Lande and Kadam, *On spectrum of the zero-divisor graph of matrix ring*, arXiv:2312.09934v1 (public December 15, 2023), give equivalence-class reductions and spectral bounds for the same matrix-ring graph; they state that computing the spectrum of their diagonally corrected quotient is difficult. Their earlier joint work with Patil, *Spectra of the zero-divisor graph of finite rings*, arXiv:2106.15977v1 (public June 30, 2021), gives a general **implicit** quotient-matrix method for finite semisimple rings, including matrix rings. That general reduction makes each finite instance computable, but does not itself state the uniform two-quadratic factorization, exact nullity equality, inertia or energy formula obtained here.

A separate indexed result on domination of the same matrix-ring graph concerns domination numbers rather than adjacency spectra, and does not imply the characteristic polynomial.

## Limitations

The spectrum is for the usual simple **undirected** graph on **nonzero** singular elements and the ordinary real adjacency matrix; changing any of these conventions changes the formulas. The result does not give spectra for larger matrix sizes, nonfield coefficient rings, directed zero-product graphs, or the different Lipschitz quaternion rings modulo powers of two. The proof is elementary and exact, but independent mathematical auditing and exhaustive coverage of unindexed literature have not been performed. The earlier literature provides implicit ways to compute individual spectra, so the originality claimed is the **uniform closed form and sharp derived invariants**, not a first finite algorithm.

## References

1. B. A. Rather, *Block Structure and Spectrum of Zero-Divisor Graphs of Lipschitz Quaternion Rings Modulo* \(n\), arXiv:2603.20947v1 (March 21, 2026), https://arxiv.org/html/2603.20947v1 .
2. K. Masalkar, A. Khairnar, A. Lande, L. Kadam, *On spectrum of the zero-divisor graph of matrix ring*, arXiv:2312.09934v1 (December 15, 2023), https://arxiv.org/abs/2312.09934 .
3. K. D. Masalkar, A. Khairnar, A. Lande, A. Patil, *Spectra of the zero-divisor graph of finite rings*, arXiv:2106.15977v1 (June 30, 2021), https://arxiv.org/abs/2106.15977 .

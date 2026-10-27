# Exact maximal-radical-rank derivation census of the three-generator Grassmann algebra

## Finding

Let \(k=\mathbb F_q\) be any finite field, let \(E=\bigwedge_k(k^3)\) be the eight-dimensional associative Grassmann algebra, and let \(\mathfrak m=\bigoplus_{j=1}^3\bigwedge^j(k^3)\) be its seven-dimensional Jacobson radical. Denote by \(\operatorname{Der}_{\mathfrak m}(E)\) the \(k\)-linear **ordinary** associative derivations \(D\) satisfying \(D(\mathfrak m)\subseteq\mathfrak m\). Write
\[
R(q)=\#\{D\in\operatorname{Der}_{\mathfrak m}(E):\operatorname{rank}_k(D|_{\mathfrak m})=7\}.
\]
Then, in every finite-field characteristic,
\[
\boxed{R(q)=
\begin{cases}
q^9(q-1)(q^5-2q^4-q^3+q^2+3q+2),&\operatorname{char}k\ne2,\\
q^{15}(q-1)(q^5-2q^4-q^3+q^2+3q+1),&\operatorname{char}k=2.
\end{cases}}
\]
The dimensions of the relevant derivation spaces are \(15\) and \(21\), respectively. The characteristic-two exception reflects both six additional higher-degree parameters and an additional exceptional trace contribution of \(q^3\) to the leading-matrix census.

## Assumptions and scope

The algebra has exterior generators \(x_1,x_2,x_3\) with \(x_i^2=0\) and \(x_ix_j=-x_jx_i\). A derivation obeys \(D(ab)=D(a)b+aD(b)\) without the graded sign used for superderivations. The rank is the rank of the seven-dimensional linear map on the *radical*, not the rank of a multiplicative algebra endomorphism; no derivation here is a unital algebra automorphism. In odd characteristic every ordinary derivation automatically preserves \(\mathfrak m\). In characteristic two the preservation hypothesis is essential: unrestricted derivations can send generators to elements with nonzero constants.

## Proof

**1. Parameterization.** Every derivation is specified by its values on the three generators, subject to the defining quadratic relations. In odd characteristic the nine degree-one coefficients are arbitrary, the three degree-three coefficients are arbitrary, and the degree-two coefficients have a three-dimensional solution space. Indeed, the even-degree part of any ordinary derivation is an inner derivation \(\operatorname{ad}(a)\) with \(a\in\operatorname{span}_k\{x_1,x_2,x_3\}\): the odd degree-three component lies in the center and produces no extra inner derivations. The degree-one terms give an arbitrary matrix \(B\in M_3(k)\). Thus there are exactly \(9+3+3=15\) parameters, six of which have degree greater than one. This agrees with the known derivation decomposition of the Grassmann algebra (Bavula, Theorem 2.1); the coefficients can also be checked directly by differentiating \(x_i^2=0\) and \(x_ix_j+x_jx_i=0\). In characteristic two the algebra is commutative with square-zero generators, so *any* triple of elements of \(\mathfrak m\) extends uniquely to a derivation preserving \(\mathfrak m\). There are exactly \(3\cdot7=21\) free coefficients, of which twelve have degree greater than one.

**2. Maximal-rank criterion.** The radical-power filtration \(\mathfrak m\supset\mathfrak m^2\supset\mathfrak m^3\supset0\) is preserved by every derivation under consideration. Its three graded diagonal blocks are the infinitesimal actions of \(B\) on \(\bigwedge^1 k^3\), \(\bigwedge^2 k^3\), and \(\bigwedge^3 k^3\). Put \(t=\operatorname{tr}B\). Under the canonical identification \(\bigwedge^2 k^3\simeq(k^3)^*\otimes\bigwedge^3 k^3\), the middle action is \(tI_3-B^*\) and the top action is multiplication by \(t\). Therefore, in every characteristic,
\[
\det(D|_{\mathfrak m})=\det B\,\det(tI_3-B)\,t.
\]
All higher-degree derivation coefficients occur strictly above the filtration diagonal, so they do not influence this determinant. Consequently \(D|_{\mathfrak m}\) is bijective exactly when \(t\ne0\), \(\det B\ne0\), and \(\det(tI_3-B)\ne0\).

**3. Trace-one matrix census.** For \(t\ne0\), multiplication by \(t^{-1}\) bijects the eligible matrices of trace \(t\) with the matrices \(C\) of trace \(1\) satisfying \(\det C\ne0\) and \(\det(I_3-C)\ne0\). Write their number as \(N(q)\). To count them, use subspace-lattice Möbius inversion simultaneously for \(\ker C\) and \(\ker(C-I_3)\). The Möbius value of an \(r\)-space is \((-1)^r q^{\binom r2}\). If \(U\subseteq\ker C\) and \(V\subseteq\ker(C-I_3)\), then \(U\cap V=0\). For dimensions \(r,s\) with \(r+s<3\), the number of maps satisfying both restrictions and \(\operatorname{tr}C=1\) is \(q^{3(3-r-s)-1}\); there is at least one free diagonal entry. The number of transverse ordered subspace pairs is \({3\brack r}_q{3-r\brack s}_q q^{rs}\).

Grouping terms according to \(j=r+s=0,1,2\), with the Gaussian counts of \(j\)-subspaces and Möbius-weighted transverse splittings inside each such subspace, the positive-complement contribution is
\[
C(q)=q^8-2q^5(q^2+q+1)+q^3(q^2+q+1)(q+3)
=q^8-2q^7-q^6+2q^5+4q^4+3q^3.
\]
For \(r+s=3\) the map is the projection onto \(V\) along \(U\), so its trace is the image in \(k\) of the integer \(s\). Its Möbius-weighted contribution is
\[
-q^3\sum_{\substack{0\le s\le3\\s\cdot1_k=1_k}}{3\brack s}_q
=-q^3(q^2+q+1+\mathbf1_{\operatorname{char}k=2}).
\]
This yields the exact uniform formula
\[
N(q)=q^3\left(q^5-2q^4-q^3+q^2+3q+2-\mathbf1_{\operatorname{char}k=2}\right).
\]
Only \(s=1\) contributes in odd characteristic; \(s=1,3\) contribute in characteristic two. No assumption that \(q\) is prime is used.

**4. Completion.** For each of the \(q-1\) nonzero traces there are \(N(q)\) eligible leading matrices. Each leading matrix has \(q^6\) lifts to an ordinary derivation in odd characteristic, and \(q^{12}\) lifts to a radical-preserving derivation in characteristic two. Multiplying these independent factors gives exactly the stated formulas.

## Verification

The standalone standard-library script `verify.py` reconstructs the exterior multiplication table, computes all defining derivation equations, checks the dimension of the solution space in characteristics \(2,3,5\), and tests the rank criterion against sampled actual derivation matrices. It also enumerates **all** \(3\times3\) leading matrices of trace \(1\) over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). The resulting values of \(N(q)\) are respectively \(24\), \(1998\), \(30528\), and \(224000\), agreeing with the formula. These finite tests are supplementary; the Möbius calculation proves the count for every finite field.

## Relationship to prior work

Bavula (2007) gives the general odd-characteristic decomposition of derivations of Grassmann algebras and is used to situate the parameter count. Fulman–Stanton (2015) studies distributions of fixed-vector spaces for classical groups, which is closely related to the condition \(\det(I-C)\ne0\), but does not impose the trace-one condition or count these derivations. Gorodetsky–Rodgers (2019) studies traces and characteristic-polynomial distributions of random finite-field matrices; its general machinery is relevant to the matrix subproblem but does not explicitly provide the present exact radical-derivation census. The new result is the complete characteristic-uniform count of a canonical maximum-rank stratum in the derivation algebra; it is not a claim of a new general structure theorem for Grassmann derivations.

## Limitations

This is the three-generator Grassmann algebra only; it does not give the full rank distribution, classifications up to conjugacy, or an all-generator formula. Characteristic-two derivations not preserving the radical are not counted. Published distribution formulas for finite-field matrix characteristic polynomials may give alternate indirect derivations of the counting polynomial, so priority and independence from every possible earlier consequence are not certified. The verification script checks finite fields and samples, not an infinite family by enumeration.

## References

- V. V. Bavula, *Derivations and skew derivations of the Grassmann algebras*, arXiv:0704.3850v1 (first posted 2007-04-29), in particular Theorem 2.1 and the positive grading of the derivation algebra.
- J. Fulman and D. Stanton, *On the distribution of the number of fixed vectors for the finite classical groups*, arXiv:1505.06383v1 (first posted 2015-05-23), especially the introduction and fixed-space distribution.
- O. Gorodetsky and B. Rodgers, *Traces of powers of matrices over finite fields*, arXiv:1909.03666 (first posted 2019-09-09), especially Theorem 1.1 and the discussion of characteristic-polynomial distributions.
- P. M. Neumann and C. E. Praeger, *Derangements and Eigenvalue-Free Elements in Finite Classical Groups*, J. London Math. Soc. 58 (1998), 564–586, DOI:10.1112/S0024610798006772 (bibliographic comparison; full text not inspected).

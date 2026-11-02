# A 27-plane characteristic-two specialization of the Segre cubic

## Finding
Let \(S\subset\mathbb P^5_{\mathbb F_2}\) be the scheme defined by
\[
\sum_{i=0}^{5}X_i=\sum_{i=0}^{5}X_i^3=0.
\]
Then \(S\) is the normal projective cone over the smooth characteristic-two Clebsch cubic surface \(Y\). Its singular support is exactly the rational cone vertex \(P=[1:1:1:1:1:1]\), of multiplicity three. Its Fano scheme of projective planes is reduced and finite étale of degree \(27\), with \(15\) \(\mathbb F_2\)-rational planes and six conjugate pairs of additional planes defined over \(\mathbb F_4\). Thus the classical characteristic-zero count of \(15\) planes jumps to \(27\) for this explicit integral model.

For every integer \(m\geq1\), put \(q=2^m\). The point count and zeta function are
\[
\#S(\mathbb F_q)=1+q+\bigl(6+(-1)^m\bigr)q^2+q^3,
\qquad
Z(S/\mathbb F_2,T)=\frac{1}{(1-T)(1-2T)(1-4T)^6(1+4T)(1-8T)}.
\]
In particular, \(\#S(\mathbb F_2)=31\) and \(\#S(\mathbb F_4)=181\).

## Assumptions and scope
These claims concern exactly the mod-\(2\) fiber of the integral pair of power-sum equations displayed above; they do not describe every possible integral model of the classical Segre cubic. A geometric plane means a \(\mathbb P^2\) contained in \(S_{\overline{\mathbb F}_2}\). The Fano scheme is the scheme of such linear subspaces inside the Grassmannian; \(\mathbb F_2\)-rational planes are fixed under arithmetic Frobenius. The ordinary cubic surface theorem giving \(27\) lines on a smooth cubic surface holds in characteristic two.

## Proof
**1. Cone and singularity.** Set \(V=\{(X_i)\in\mathbb F_2^6:\sum X_i=0\}\) and \(e=(1,1,1,1,1,1)\). Because \(6=0\), \(e\in V\). In characteristic two, for all \(v\in V\) and every scalar \(t\),
\[
\sum_i(v_i+te_i)^3
=\sum_i v_i^3+t\sum_i v_i^2+t^2\sum_i v_i+6t^3
=\sum_i v_i^3.
\]
Thus the cubic depends only on \(V/\langle e\rangle\). Taking the complementary section \(X_5=0\) identifies that quotient with the five-coordinate hyperplane \(\sum_{i=0}^4X_i=0\), on which the induced cubic is \(\sum_{i=0}^4X_i^3=0\): the Clebsch diagonal surface \(Y\subset\mathbb P^3\). Over an algebraic closure, a singular point of \(Y\) would satisfy \(X_i^2=\lambda\) for all five coordinates, by the Jacobian criterion for its two defining equations. The Frobenius square map is injective, so all five \(X_i\) would equal some \(a\); their sum is \(5a=a\), forcing the zero vector. Hence \(Y\) is smooth. The projective cone has unique singular support at \(P=[e]\). Its defining equation has order three at \(P\), hence multiplicity three. It is a hypersurface, regular in codimension one and Cohen--Macaulay, so it is normal.

**2. Classification and reducedness of planes.** Every projective plane \(\Pi\) in the cone must contain the vertex: otherwise projection from \(P\) would embed \(\Pi\) as a plane contained in the smooth cubic surface \(Y\), which is impossible. Planes through \(P\) correspond bijectively to lines on \(Y\). There are exactly \(27\) such geometric lines. To verify scheme-theoretic reducedness, let \(\ell\subset Y\) be one line and choose coordinates \(u,v,w_1,w_2\) on its ambient \(\mathbb P^3\), with \(\ell=\{w_1=w_2=0\}\). Along \(\ell\), the first normal derivatives of the cubic are two binary quadrics \(Q_1(u,v),Q_2(u,v)\). Smoothness of \(Y\) gives no common zero of these quadrics on \(\mathbb P^1_{\overline{\mathbb F}_2}\), hence they are coprime. An infinitesimal deformation of the corresponding plane \(\Pi=\langle P,\ell\rangle\) is specified by two linear forms \(A(t,u,v),B(t,u,v)\), and the infinitesimal containment condition is \(Q_1A+Q_2B=0\). Coprimality, with degrees \(2\) and \(1\), forces \(A=B=0\). Hence the Fano scheme has zero tangent space at each of its \(27\) geometric points. It is reduced and, over the perfect field \(\mathbb F_2\), finite étale.

**3. Exact arithmetic of the planes.** The accompanying finite-field verifier constructs \(\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\), enumerates the \(357\) two-dimensional subspaces of \(\mathbb F_4^4\), and tests whether the Clebsch cubic vanishes on the corresponding projective line. Exactly \(27\) lines pass; they are therefore all geometric lines by Step 2. Squaring their coefficients and row-reducing shows exactly \(15\) fixed lines and six two-element Frobenius orbits. The cone correspondence gives the claimed arithmetic Fano scheme.

**4. Counts and zeta function.** Over \(\mathbb F_2\), every point of the ambient \(\mathbb P^3\) lies on \(Y\), since \(a^3=a\) and the defining cubic becomes its hyperplane equation. Consequently \(\#Y(\mathbb F_2)=15\). As all \(27\) lines are defined over \(\mathbb F_4\) and generate the geometric Picard group of the smooth cubic surface, Frobenius squared acts trivially on that rank-seven Picard group. The smooth rational-surface trace formula
\[
\#Y(\mathbb F_{2^m})=1+2^{2m}+2^m\operatorname{Tr}(\mathrm{Frob}^m\mid\operatorname{Pic}(Y_{\overline{\mathbb F}_2}))
\]
then forces Frobenius eigenvalues \(+1\) six times and \(-1\) once: for \(m=1\), the trace equals \((15-1-4)/2=5\). Thus \(\#Y(\mathbb F_q)=q^2+1+(6+(-1)^m)q\). Projection away from the cone vertex has exactly \(q\) points of \(S(\mathbb F_q)\) over each point of \(Y(\mathbb F_q)\), while \(P\) contributes one further point. Therefore \(\#S(\mathbb F_q)=1+q\#Y(\mathbb F_q)\), proving the formula. Expanding \(\exp(\sum_{m\ge1}\#S(\mathbb F_{2^m})T^m/m)\) yields the displayed zeta function.

## Verification
Run \(\texttt{python3 verify.py}\) with ordinary Python 3; no external package is needed. It enumerates all \(357\) lines of \(\mathbb P^3(\mathbb F_4)\), tests Clebsch containment exactly, computes the Frobenius action, exhaustively counts the \(\mathbb F_2\)- and \(\mathbb F_4\)-points of both the base and cone, and checks the cone-translation identity over \(\mathbb F_4\). Its output ends with \(\texttt{VERIFY_OK}\). Exhaustive finite enumeration proves the \(\mathbb F_4\) line classification only when combined with the independent theorem that a smooth cubic surface has precisely \(27\) geometric lines. The all-extension counts depend on the Picard/Frobenius proof, not numerical extrapolation.

## Relationship to prior work
Kondō (2011), Section 2, and Dolgachev (2015), Section 2, both give the six-coordinate equations and the classical \(10\)-node, \(15\)-plane configuration. The characteristic-two surface \(Y\) inherits the highly symmetric smooth cubic geometry studied for example by Kadyrsizova et al. (2020) and Vikulova (2023/2024); in particular, the latter describes the \(A_1\) Weyl involution with \(15\) fixed lines and six pairs. None of the inspected passages gives the special-fiber cone-and-plane theorem for the Segre threefold. The characteristic-two Frobenius behavior of the cubic surface, taken alone, is not claimed as new. The additional assertion is that this specific degeneration of the **threefold** has an isolated triple cone vertex, a reduced \(27\)-point plane Fano scheme and the stated arithmetic plane splitting and zeta formula. Historical priority remains provisional.

## Limitations
No assertion is made about stable reduction, alternate integral models, an explicit scheme structure for the singular Jacobian ideal, or a general formula for every characteristic-two cubic threefold. A sufficiently broad unindexed account of this particular modular Segre degeneration could cover some or all of the result. The calculations and proof have had self-review only, not independent validation.

## References
1. S. Kondō, *The Segre cubic and Borcherds products*, arXiv:1110.1126v1 (first posted 2011-10-06), especially Section 2.
2. I. Dolgachev, *Corrado Segre and nodal cubic threefolds*, arXiv:1501.06432v1 (first posted 2015-01-26), especially Section 2, Proposition 2.2 and equation (2.1).
3. Z. Kadyrsizova, J. Kenkel, J. Page, J. Singh, K. E. Smith, A. Vraciu and E. E. Witt, *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018v1 (2020), Sections 1 and 5.
4. A. V. Vikulova, *The most symmetric smooth cubic surface over a finite field of characteristic 2*, arXiv:2312.17032v1 (2023), especially Theorems 1.3--1.5 and Lemma 5.3.
5. Classical theorem of Cayley--Salmon: the \(27\) geometric lines on a smooth cubic surface, and the standard Picard lattice of a degree-three del Pezzo surface.

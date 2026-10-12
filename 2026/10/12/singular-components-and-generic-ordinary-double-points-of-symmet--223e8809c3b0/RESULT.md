# Singular components and generic ordinary double points of symmetric arrowhead determinantal hypersurfaces

## Finding

For every integer \(m\ge3\), let \(X_m\subset\mathbb P^{2m}_{\mathbb C}\) be defined by the determinant of the symmetric arrowhead matrix
\[
M_m=\begin{pmatrix}
\operatorname{diag}(a_1,\ldots,a_m)&(b_1,\ldots,b_m)^{\mathsf T}\\
(b_1,\ldots,b_m)&t
\end{pmatrix}.
\]
Let \(G_i\) denote the determinant of the arrowhead matrix after deleting the \(i\)-th leaf row and column. For distinct indices \(i,j,k\), put
\[
Y_i=V(a_i,b_i,G_i),\qquad L_{ijk}=V(a_i,a_j,a_k).
\]
Then \(X_m\) is an integral normal projective hypersurface of degree \(m+1\), and
\[
\operatorname{Sing}(X_m)_{\mathrm{red}}=\bigcup_{i=1}^mY_i\ \cup\!\bigcup_{1\le i<j<k\le m}L_{ijk}
\]
is its irredundant irreducible-component decomposition. There are exactly \(m+\binom m3\) components, all of dimension \(2m-3\), with \(\deg Y_i=m\) and \(\deg L_{ijk}=1\). In particular, the degree of the reduced singular support is \(m^2+\binom m3\).

At a general closed point on each component there is an isomorphism of complete local \(\mathbb C\)-algebras
\[
\widehat{\mathcal O}_{X_m,p}\cong
\mathbb C[[u,v,w,z_1,\ldots,z_{2m-3}]]/(uv-w^2).
\]
The normal transverse germ is an ordinary quadratic surface node of multiplicity two; the Jacobian singular scheme is generically reduced along every component.

## Assumptions and scope

Work over \(\mathbb C\), and use \(m\ge3\). All varieties are projective reduced supports unless a scheme is explicitly named. The singular locus in the decomposition is the reduction of the projective Jacobian singular scheme. “General point” means every closed point of a nonempty Zariski-open subset of the specified component. Degrees are computed in the indicated ambient projective space, with the reduced scheme structure on the singular support.

Write \(A=\prod_{i=1}^m a_i\) and \(A_i=\prod_{j\ne i}a_j\). Cofactor expansion gives the homogeneous polynomial
\[
F_m=\det M_m=tA-\sum_{i=1}^m b_i^2 A_i.
\]
It has degree \(m+1\). The notation \(G_i\) is the same expression in the \(m-1\) leaves different from \(i\), hence homogeneous of degree \(m\).

## Proof

**1. Irreducibility.** Regard \(F_m\) as a polynomial of degree one in \(t\) with coefficients in the factorial domain \(R=\mathbb C[a_1,\ldots,a_m,b_1,\ldots,b_m]\). A common irreducible divisor of its coefficient \(A\) and constant term must be some \(a_i\), yet reduction of the constant term modulo \(a_i\) gives \(-b_i^2A_i\ne0\). Thus the two coefficients are coprime. Gauss's lemma implies \(F_m\) is irreducible. The same argument, using \(m-1\ge2\) leaves, proves every \(G_i\) is irreducible. Hence \(X_m\) and each \(Y_i\) are integral.

**2. The singular-set criterion.** Every diagonal matrix entry of \(M_m\), including the central entry, is a free coordinate of the ambient projective space. For a symmetric matrix \(M\) of corank one, its adjugate is \(cqq^{\mathsf T}\), with \(q\ne0\) and \(c\ne0\). At least one diagonal adjugate entry is nonzero. Since the corresponding diagonal coordinate derivative of \(\det M\) equals that cofactor, a corank-one point is nonsingular. For corank at least two every cofactor vanishes, so every partial derivative vanishes. It follows that
\[
\operatorname{Sing}(X_m)_{\mathrm{red}}=\{[M_m]:\operatorname{rank}(M_m)\le m-1\}_{\mathrm{red}}.
\]

**3. Complete component classification.** For a point, let \(Z\) be the set of zero diagonal leaf coordinates, and let \(k=|Z|\). If \(k=0\), the leaf diagonal block is invertible, hence \(\operatorname{rank}M_m\ge m\), so the point is nonsingular. If \(k=1\), say \(Z=\{i\}\), invert the other leaf diagonal entries. Congruence elimination reduces the remaining block to \(\begin{psmallmatrix}0&b_i\\ b_i&t'\end{psmallmatrix}\), with \(t'=t-\sum_{j\ne i}b_j^2/a_j\). Its rank is at most zero exactly when \(b_i=t'=0\), equivalent to membership in \(Y_i\), because \(G_i=A_i t'\) on this open set.

If \(k=2\), say \(Z=\{i,j\}\), the residual block on the two zero-diagonal leaves and the center is \(\begin{psmallmatrix}0&0&b_i\\0&0&b_j\\b_i&b_j&t'\end{psmallmatrix}\). Its rank is at most one if and only if \(b_i=b_j=0\), which puts the point in both \(Y_i\) and \(Y_j\). If \(k\ge3\), invert the nonzero leaf diagonals, obtaining a residual \((k+1)\)-square matrix of rank at most two. Therefore the whole matrix has rank at most \((m-k)+2\le m-1\); the point belongs to at least one \(L_{ijk}\). Conversely each \(L_{ijk}\) consists entirely of matrices with corank at least two, and each \(Y_i\) has a zero row and column at index \(i\), while its remaining block is singular, so it also lies in the singular locus. This proves the set-theoretic union everywhere, not just on the coordinate torus.

The equations of \(Y_i\) define an irreducible hypersurface \(G_i=0\) within the linear subspace \(a_i=b_i=0\), of codimension three in \(\mathbb P^{2m}\) and degree \(m\). Every \(L_{ijk}\) is an irreducible linear space of the same codimension and degree one. To see that no component is redundant, a generic point of \(Y_i\) has all other \(a_j\ne0\) and no other zero leaf diagonal; a generic point of \(L_{ijk}\) has precisely the three listed zero diagonals and all three associated \(b_i,b_j,b_k\ne0\), so belongs to no \(Y_r\) and no other \(L\). Since the union has equidimensional irreducible components, degree is additive on the reduced top-dimensional cycle, giving \(m^2+\binom m3\).

**4. Ordinary nodes on the nonlinear components.** On \(a_j\ne0\) for every \(j\ne i\), the determinant is exactly
\[
F_m=a_iG_i-b_i^2A_i=A_i(a_i\tau-b_i^2),\qquad \tau=G_i/A_i=t-\sum_{j\ne i}b_j^2/a_j.
\]
The transformation replacing \(t\) by \(\tau\) is an algebraic coordinate change. Because \(A_i\) is a unit, the transverse local equation is exactly \(a_i\tau-b_i^2=0\). The other \(2m-3\) local coordinates vary freely. This yields the first completed-local-ring assertion, without approximation.

**5. Ordinary nodes on linear components.** Fix distinct \(i,j,k\), and restrict to the nonempty open subset where all \(a_\ell\) with \(\ell\notin\{i,j,k\}\), and \(b_i,b_j,b_k\), are nonzero. Eliminating the other leaves gives, up to a unit, the equation
\[
 f=\tau a_i a_j a_k-b_i^2a_ja_k-b_j^2a_ia_k-b_k^2a_ia_j,
\qquad \tau=t-\sum_{\ell\notin\{i,j,k\}}b_\ell^2/a_\ell.
\]
The lowest nonzero degree in normal coordinates \(a_i,a_j,a_k\) is the quadratic form
\[
 Q=-b_i^2a_ja_k-b_j^2a_ia_k-b_k^2a_ia_j.
\]
Its Hessian determinant is \(-2b_i^2b_j^2b_k^2\ne0\). The characteristic-zero formal Morse lemma, applied over the completed local ring of the smooth linear stratum (and valid because the Hessian determinant is a unit), eliminates the higher-order cubic term and changes \(Q\) to \(uv-w^2\). Since the center is a smooth \((2m-3)\)-dimensional stratum, the same completed local model follows. In these ordinary-node charts the Jacobian ideal cuts out the smooth stratum with reduced structure.

**6. Normality.** The hypersurface \(X_m\) is integral, hence Cohen–Macaulay and satisfies Serre's condition \(S_2\). By the decomposition, its singular locus has codimension two in \(X_m\) (all components have ambient codimension three). Thus \(X_m\) is regular in codimension one (\(R_1\)); Serre's criterion proves normality.

## Verification

The accompanying self-contained `checker.py` performs exact integer-arithmetic comparisons of the full formal gradient against the proposed union of components. It tests every coefficient vector in \(\{0,1\}^{2m+1}\) for \(3\le m\le6\), and in \(\{-1,0,1\}^{2m+1}\) for \(m=3,4\): 32,750 configurations in total. Generic points on both kinds of components and the predicted component counts and reduced-support degrees are checked for \(3\le m\le8\). Reproduce with `python3 checker.py`; the matching recorded output is in `checker_output.txt`. These finite tests are supplementary: the all-parameter assertions follow from the proof above, not enumeration.

## Relationship to prior work

Fink–Rajchgot–Sullivant investigate generic and symmetric matrix Schubert varieties and Gaussian conditional independence models (arXiv:1510.04124, first public preprint 2015-10-14). Their northeast-rank-inequality geometry does not itself state this star-pattern determinant's singular-component decomposition. Conca–Welker investigate coordinate sections of generic and symmetric determinantal varieties and graph-pattern conditions (arXiv:1801.07916); their forest zero-pattern conditions concern a different graph restriction, because the **zero pattern** here is the complete graph on the leaf vertices, whereas the **nonzero pattern** is a star. Related classical studies of eigenvalue multiplicities of symmetric tree-pattern matrices concern spectral constraints rather than projective singular components and transverse completed local rings. These results supply motivation and context, not a claim that sparse determinantal geometry was previously unknown.

## Limitations

The result determines the reduced singular support and its generic transverse completed-local rings; it does not determine the global Jacobian scheme, embedded associated components, or germs at special component intersections. The formula for the degree is for the **reduced** singular support, not a Jacobian scheme multiplicity. Full historical uniqueness is not established: Giusti–Merle's 1982 study of coordinate-plane sections of determinantal varieties is a material comparison risk because its complete original text was not available for inspection. No assertion of independent audit is made.

## References

1. A. Fink, J. Rajchgot, S. Sullivant, *Matrix Schubert varieties and Gaussian conditional independence models*, arXiv:1510.04124 (version 1, 2015-10-14).
2. A. Conca, V. Welker, *Lovász–Saks–Schrijver ideals and coordinate sections of determinantal varieties*, arXiv:1801.07916 (2018).
3. C. R. Johnson, A. Leal Duarte, C. M. Saiago, *Inverse eigenvalue problems and lists of multiplicities of eigenvalues for matrices whose graph is a tree*, Linear Algebra and its Applications (2003).
4. M. Giusti, M. Merle, *Singularités isolées et sections planes de variétés déterminantielles. II. Sections de variétés déterminantielles par les plans de coordonnées* (1982), doi:10.1007/BFb0071278 (full text not inspected).

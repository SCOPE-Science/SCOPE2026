# Exact John ellipsoid of the doubly substochastic matrix polytope

## Finding
For every integer \(n\ge2\), equip \(\mathbb R^{n\times n}\) with the Frobenius inner product and consider the complete-bipartite matching polytope
\[
\mathcal D_n=\bigl\{X:X_{ij}\ge0,\ \sum_jX_{ij}\le1,\ \sum_iX_{ij}\le1\text{ for all }i,j\bigr\}.
\]
Let \(\mathbf1\in\mathbb R^n\) be the all-ones vector, \(J=\mathbf1\mathbf1^{\mathsf T}\), \(H=J/n\), and \(F=I-H\). Define four Frobenius-orthogonal projections on the ambient matrix space:
\[
P_{00}(Y)=HYH,\qquad P_r(Y)=FYH,\qquad
P_c(Y)=HYF,\qquad P_\perp(Y)=FYF.
\]
For \(n\ge2\), put
\[
r_n=\frac{n\bigl(n-2+\sqrt{n^2+12n-4}\bigr)}{2(2n-1)},\quad
C_n=2n+(2n-1)r_n,\quad t_n=\frac{r_n}{n(1+r_n)},
\]
\[
\lambda_0=\frac{2+r_n}{(1+r_n)^2C_n},\qquad
\lambda_1=\frac{2}{(1+r_n)C_n},\qquad
\lambda_2=\frac{2+r_n}{(1+r_n)C_n},
\]
and define the positive self-adjoint shape operator
\[
\mathcal Q_n=\lambda_0P_{00}+\lambda_1(P_r+P_c)+\lambda_2P_\perp.
\]
**The unique maximum-volume ellipsoid contained in \(\mathcal D_n\)** is
\[
\boxed{\mathcal E_n=\left\{t_nJ+Y:\langle Y,\mathcal Q_n^{-1}Y\rangle_F\le1\right\}.}
\]
Every one of the \(n^2+2n\) facets of \(\mathcal D_n\) is tangent to \(\mathcal E_n\), at a distinct point. The shape spectrum, with multiplicities, is \(\lambda_0\) (once), \(\lambda_1\) (\(2n-2\) times), and \(\lambda_2\) (\((n-1)^2\) times), with \(0<\lambda_0<\lambda_1<\lambda_2\). In particular, its exact intrinsic (here full-dimensional) Euclidean volume is
\[
\boxed{\operatorname{vol}_{n^2}(\mathcal E_n)
=\frac{\pi^{n^2/2}}{\Gamma(1+n^2/2)}
\sqrt{\lambda_0\lambda_1^{2(n-1)}\lambda_2^{(n-1)^2}}.}
\]
As \(n\to\infty\), \(\lambda_0\sim2/n^3\), \(\lambda_1\sim4/n^3\), and \(\lambda_2\sim1/n^2\).

## Assumptions and scope
The matrix polytope is full-dimensional in \(\mathbb R^{n^2}\). Its vertices are the zero-one matrices having at most one nonzero entry in each row and column (partial permutation matrices), by integrality of bipartite-matching incidence inequalities; see the partial-permutation-polytope description in Heuer–Striker. Only integers \(n\ge2\) are claimed; all volumes and ellipsoids use the ambient Frobenius Euclidean metric, not normalized lattice volume. A shape operator \(\mathcal Q\) has squared principal semiaxes equal to its eigenvalues. The source of the polytope's geometric framework is the complete-bipartite matching-polytope setting of Eisley–Matsushita–Vindas-Meléndez (first public 2024-07-11).

## Proof
**1. Facets and symmetry.** The displayed inequalities give the whole polytope and are all irredundant for \(n\ge2\). A coordinate inequality can be made an equality with all other inequalities strict by assigning small positive values to the other entries; for a selected row-sum inequality, set that row to \(1/n\) and all other entries to sufficiently small positive values, and similarly for a column. Thus the \(n^2+2n\) inequalities are exactly its facets.

Uniqueness of the maximum-volume contained ellipsoid is the standard John-ellipsoid uniqueness theorem. Permutations of rows and columns and transposition preserve both \(\mathcal D_n\) and its Euclidean metric; hence the unique optimum is invariant under these actions. Its center is therefore \(tJ\) with \(0<t<1/n\). The four displayed subspaces are mutually orthogonal and exhaust the matrix space; their dimensions are \(1,n-1,n-1,(n-1)^2\). Invariance under independent permutations makes the positive shape operator scalar on each component, while transposition forces equal eigenvalues for the row and column components. Thus some \(\lambda_0,\lambda_1,\lambda_2>0\) describe the unique candidate as in the finding.

**2. Exact containment.** The support function of an ellipsoid \(c+\mathcal Q^{1/2}B\) in direction \(A\) is \(\langle A,c\rangle_F+\sqrt{\langle A,\mathcal Q A\rangle_F}\). Let \(E_{ij}\) denote a matrix unit and \(R_i=e_i\mathbf1^{\mathsf T}\), \(C_j=\mathbf1e_j^{\mathsf T}\). The squared norms of the four orthogonal components of \(E_{ij}\) are, respectively,
\[
\frac1{n^2},\quad\frac{n-1}{n^2},\quad\frac{n-1}{n^2},\quad\frac{(n-1)^2}{n^2}.
\]
For \(R_i\), only the first two components are nonzero, with squared norms \(1\) and \(n-1\); for \(C_j\), the first and third components have those norms. Consequently the ellipsoid is contained in every facet halfspace **if and only if**
\[
\lambda_0+2(n-1)\lambda_1+(n-1)^2\lambda_2\le n^2t^2,\tag{1}
\]
\[
\lambda_0+(n-1)\lambda_1\le(1-nt)^2.\tag{2}
\]
The determinant of its shape operator is \(\lambda_0\lambda_1^{2(n-1)}\lambda_2^{(n-1)^2}\); maximizing ellipsoid volume therefore maximizes its logarithm.

**3. Global determinant optimum.** Write \(z=nt\), \(s_j=\sqrt{\lambda_j}\), and define
\[
L(s)=\log(s_0)+2(n-1)\log(s_1)+(n-1)^2\log(s_2).
\]
The containment constraints become
\[
\sqrt{s_0^2+2(n-1)s_1^2+(n-1)^2s_2^2}\le z,\qquad
\sqrt{s_0^2+(n-1)s_1^2}\le1-z.\tag{3}
\]
On the region \(s_j>0\), \(0<z<1\), this is a convex optimization problem with strictly concave differentiable objective \(L\), strictly feasible points, and a bounded feasible set. Hence an interior positive solution satisfying the Karush–Kuhn–Tucker equations is the **unique global maximizer**. One may use twice \(L\), which is the logarithm of the determinant.

For transparent algebra, introduce nonnegative multipliers \(\alpha,\beta\) for the squared forms of the two active inequalities in (1)–(2). Stationarity with respect to the eigenvalues and to \(z\) is
\[
\frac1{\lambda_0}=\alpha+\beta,\quad
\frac2{\lambda_1}=2\alpha+\beta,\quad
\frac1{\lambda_2}=\alpha,\quad
\alpha z=\beta(1-z).\tag{4}
\]
These are also KKT equations for the norm constraints (3), because the squared and unsquared active constraints have the same outward normal up to a positive factor. Put \(r=\beta/\alpha>0\); then \(z=r/(1+r)\). Setting \(C=2n+(2n-1)r\), the displayed eigenvalues satisfy (4) with
\[
\alpha=\frac{(1+r)C}{2+r}>0,\qquad\beta=r\alpha>0.\tag{5}
\]
A direct substitution gives the exact identities
\[
\lambda_0+(n-1)\lambda_1-(1-z)^2=0,
\]
\[
\frac{\lambda_0+2(n-1)\lambda_1+(n-1)^2\lambda_2}{n^2}
-\left(\frac zn\right)^2
=-\frac{(2n-1)r^2-n(n-2)r-2n^2}{n^2(1+r)C}.\tag{6}
\]
Thus both inequalities become equalities precisely when
\[
(2n-1)r^2-n(n-2)r-2n^2=0.\tag{7}
\]
For \(n\ge2\), the quadratic has exactly one positive root, namely \(r_n\) in the finding. Equations (4)–(7) establish strict positivity, primal feasibility, stationarity, complementary slackness, and dual feasibility. Strict concavity proves uniqueness among invariant ellipsoids; the symmetry reduction and uniqueness of John's ellipsoid prove optimality and uniqueness among **all** contained ellipsoids.

**4. All-facet contact and volume.** Both support inequalities are equalities. Every coordinate facet is therefore tangent at
\[
t_nJ-\frac{\mathcal Q_n(E_{ij})}{t_n},
\]
and every row- or column-sum facet is tangent, respectively, at
\[
t_nJ+\frac{\mathcal Q_n(R_i)}{1-nt_n},\qquad
 t_nJ+\frac{\mathcal Q_n(C_j)}{1-nt_n}.
\]
The stated halfspace representation guarantees that these support points lie in the polytope. Strict convexity of the ellipsoid, together with nonproportional distinct facet normals, makes contact points distinct. The determinant formula gives the volume. Since \(r_n>0\), \(\lambda_1/\lambda_0=2(1+r_n)/(2+r_n)>1\) and \(\lambda_2/\lambda_1=(2+r_n)/2>1\), proving strict spectral separation. Finally \(r_n/n\to1/2\), \(C_n/n^2\to1\) and the three eigenvalue asymptotics follow by substitution.

## Verification
The standalone source file `verify.py` uses Python 3 and SymPy. Run `python verify.py` beside this document. Its universal symbolic checks verify the row-support identity, the entry-support quadratic factorization, and KKT stationarity; a finite radical-root check covers \(2\le n\le30\). A separate Frobenius-coordinate implementation checks every stated facet support and the feasibility and tangency of all \(372\) explicit contact points for \(2\le n\le9\). These finite evaluations corroborate but do not prove the infinite-family statement; global optimality follows from the convexity and KKT proof above. Output was `ALL CHECKS PASSED` when run from the delivered source path.

## Relationship to prior work
Heuer and Striker provide the partial-permutation-matrix polytope's inequality/vertex description. Kohl, Olsen, and Sanyal identify this object with the positive type-B Birkhoff polytope and study lattice invariants and triangulations. Eisley, Matsushita, and Vindas-Meléndez analyze matching polytopes from the Gorenstein and integer-decomposition viewpoints, including the complete-bipartite family. The relevant inspected parts of those primary sources do not give this Euclidean maximum-inscribed-ellipsoid operator, its three-eigenspace spectrum, or its exact contact formula. General John-ellipsoid uniqueness and convex optimization are classical tools used here, not asserted as new. The specific formula was not matched by the mathematical-result and literature searches recorded in the accompanying review; the possibility of an equivalent earlier calculation under design-theory terminology remains.

## Limitations
The formula treats only the complete-bipartite matching polytope with equal bipartition sizes and the Frobenius metric; it is not a formula for arbitrary bipartite graphs, nonuniform row/column margins, nonsquare matrices, or a minimum-volume *enclosing* ellipsoid. It neither determines the polytope's own volume nor proves absolute historical novelty.

## References
1. B. Eisley, K. Matsushita, A. R. Vindas-Meléndez, *Matching polytopes, Gorensteinness, and the integer decomposition property*, arXiv:2407.08820, initial version July 11, 2024, https://arxiv.org/abs/2407.08820. The source classifies the primary topic under MSC 52B05.
2. D. Heuer, J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, especially Section 3, https://arxiv.org/abs/2012.09901.
3. F. Kohl, M. Olsen, R. Sanyal, *Unconditional Reflexive Polytopes*, especially the positive type-B Birkhoff identification in Section 5, https://doi.org/10.1007/s00454-020-00199-8.
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant on his 60th Birthday*, 1948, pp. 187–204 (classical ellipsoid theorem).

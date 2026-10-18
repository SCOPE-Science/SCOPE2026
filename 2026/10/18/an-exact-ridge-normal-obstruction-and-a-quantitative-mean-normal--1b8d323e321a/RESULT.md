# An exact ridge-normal obstruction and a quantitative mean-normal deficit for simplices

## Finding
For a Euclidean \(d\)-simplex \(S\), \(d\ge2\), a *normal from an interior point* \(y\) is a segment joining \(y\) to a boundary point \(z\) and perpendicular to a supporting hyperplane of \(S\) through \(z\). Let \(n_S(y)\) count its distinct bases, assigning each base to the unique relative interior of a nonempty proper face. Degenerate coincidences form a set of source points of volume zero.

**Theorem (quantitative ridge obstruction).** Write \(F_i\) for the facets, \(u_i\) for their outward unit normals, and \(h_i>0\) for their opposite-vertex altitudes. Suppose two facets \(F_i,F_j\) make an obtuse interior dihedral angle, equivalently \(g=\langle u_i,u_j\rangle\in(0,1)\). For \(Y\) sampled uniformly from \(S\), their common ridge \(R_{ij}=F_i\cap F_j\) supports a normal based in its relative interior with probability at most
\[
1-Q_{ij},\qquad
Q_{ij}=\frac{g h_j}{h_i+g h_j}+\frac{g h_i}{h_j+g h_i}>0.
\]
Accordingly,
\[
\mathbb E[n_S(Y)]\le2^{d+1}-2-Q_{ij}.
\]
The ridge bound is an equality if each other facet normal \(u_k\), \(k\notin\{i,j\}\), obeys \(\langle u_k,u_i\rangle\le0\) and \(\langle u_k,u_j\rangle\le0\). In particular, \(\mathbb E[n_S(Y)]=2^{d+1}-2\) holds **if and only if all dihedral angles are nonobtuse**. In that case every interior \(y\) has exactly \(2^{d+1}-2\) normals, one in each face's relative interior.

This probability estimate is sharp in all dimensions: for \(t>1\), define
\[
S_d(t)=\operatorname{conv}\{0,e_1,\ldots,e_{d-1},e_d+t e_1\}.
\]
Exactly one pair of its facets has an obtuse interior dihedral, and its common ridge supports a normal from a uniform interior point with probability
\[
\frac{d-1}{t\,[d-1+t(t-1)]}.
\]
For fixed dimension it decreases cubically as \(t\to\infty\), with asymptotic coefficient \(d-1\).

## Assumptions and scope
All simplices are full-dimensional, Euclidean and finite-dimensional. The probability law concerns normalized \(d\)-dimensional Lebesgue measure, not a random observer direction. The ``ridge'' is a \((d-2)\)-face; for \(d=2\) it is a vertex. Right dihedral angles are allowed in the maximum-normal characterization. Normality is with respect to an actual supporting hyperplane, not merely perpendicularity to a face's affine hull. On a null set of source points multiple faces can share one base; probability and expectations use the a.e. distinct-face convention.

## Proof
Write the facet inequalities as \(\langle u_k,x\rangle\le b_k\). A uniform interior point has barycentric coordinates \(\lambda_k>0\), \(\sum_{k=0}^{d}\lambda_k=1\), with the Dirichlet law \(\operatorname{Dirichlet}(1,\ldots,1)\). Its signed distance from facet \(F_k\) is exactly \(s_k=h_k\lambda_k\).

For a normal based in \(\operatorname{relint}R_{ij}\), its foot must be
\[
z=y+\mu_i u_i+\mu_j u_j,\qquad \mu_i,\mu_j\ge0,
\]
and it must satisfy the two facet equations. Necessarily
\[
\begin{pmatrix}1&g\\g&1\end{pmatrix}
\begin{pmatrix}\mu_i\\\mu_j\end{pmatrix}
=\begin{pmatrix}s_i\\s_j\end{pmatrix}.
\]
Since \(0<g<1\), the conic coefficients can both be nonnegative only if
\[
s_i\ge g s_j\quad\text{and}\quad s_j\ge g s_i.
\]
The two strict violations are disjoint. Independent unit exponential variables \(E_0,\ldots,E_d\) yield \(\lambda_k=E_k/\sum_m E_m\); hence
\[
\Pr(s_i<g s_j)=\Pr(h_i E_i<g h_j E_j)=\frac{g h_j}{h_i+g h_j}
\]
and analogously \(\Pr(s_j<g s_i)=g h_i/(h_j+g h_i)\). Therefore the ridge-normal probability is no greater than \(1-Q_{ij}\), without assumptions on remaining facet normals.

If all remaining pairwise products with \(u_i,u_j\) are nonpositive, then \(\mu_i,\mu_j>0\) implies for each \(k\notin\{i,j\}\)
\[
\langle u_k,z\rangle=\langle u_k,y\rangle
+\mu_i\langle u_k,u_i\rangle+\mu_j\langle u_k,u_j\rangle
< b_k.
\]
Thus \(z\) belongs to the relative interior of the ridge and its normal is supported, proving equality in the ridge probability. Every proper face supplies at most one generic normal base, establishing the expectation bound.

For the converse direction, suppose all distinct facet normals satisfy \(\langle u_i,u_j\rangle\le0\). Let \(I\) be any nonempty proper set of facet indices; its intersection is a face. Its Gram matrix \(G_I=(\langle u_i,u_j\rangle)_{i,j\in I}\) is positive definite with nonpositive off-diagonal entries. Given the strictly positive distance vector \(s_I\), the solution \(\mu=G_I^{-1}s_I\) is strictly positive. Indeed, if a negative part \(\mu^-\) existed, taking its scalar product with \(G_I\mu=s_I\) would yield \(\langle\mu^-,s_I\rangle<0\), as the cross term from disjoint positive and negative supports is nonpositive and the negative quadratic part is strictly negative. This contradicts positivity of \(s_I\). A zero component is excluded by \(s_i=\sum_j(G_I)_{ij}\mu_j\le0\). Set \(z=y+\sum_{i\in I}\mu_i u_i\); it belongs to all facets in \(I\) and strictly satisfies every other facet inequality. It is thus the unique normal foot in that face's relative interior. Summing over the \(2^{d+1}-2\) faces proves full count at every interior point. If any dihedral angle is obtuse, the strictly positive \(Q_{ij}\) excludes equality of the expected count.

For sharpness, set \(S=S_d(t)\), \(t>1\). Its barycentric-coordinate gradients are
\[
\nabla\lambda_1=e_1-t e_d,\quad \nabla\lambda_d=e_d,\quad
\nabla\lambda_k=e_k\ (2\le k\le d-1),\quad
\nabla\lambda_0=-\sum_{k=1}^{d}\nabla\lambda_k.
\]
The only positive scalar product between distinct gradients is that of indices \(0,d\), equal to \(t-1\). Put \(L=\sqrt{d-1+(t-1)^2}\). Then \(h_0=1/L\), \(h_d=1\), and \(g=(t-1)/L\). All other facet normals have nonpositive scalar products with both \(u_0,u_d\), so the ridge formula is exact. Substitution and simplification give
\[
1-\frac{t-1}{t}-\frac{t-1}{d-1+t(t-1)}
=\frac{d-1}{t[d-1+t(t-1)]}.
\]
This completes the claimed probability, rigidity and sharpness statements.

## Verification
The included standalone script `verification/check_ridge.py` uses independently generated uniform barycentric samples for dimensions \(2\) through \(6\) and shear parameters \(5/4,2,3\), checks full-dimensional ridge membership and normal-cone inequalities, enumerates every proper face of right-coordinate simplices, and checks exact rational simplifications for integer shears. It reports 1,204,808 successful individual consistency checks. The infinite-dimensional-parameter result rests on the preceding algebraic proof, **not** on sample counts.

## Relationship to prior work
Nasonov, Panina and Siersma (2024) develop active normal regions and define the average number of normals. They characterize maximum average normals in dimensions two and three; their results do not give the explicit dimension-independent ridge loss \(Q_{ij}\), its exact equality criterion, or the sheared-simplex probability. Nasonov and Panina (2026) prove a lower bound on the maximum number of normals from a **specially chosen** point of a four-simplex; this does not imply a sharp **uniformly random source-point** deficit. Their 2024 and 2025 works on guaranteed numbers of normals also address existence rather than this explicit chance/mean bound.

## Limitations
The sharp expression applies to **one specified ridge** under the stated cross-normal hypothesis. For a simplex with several obtuse dihedral pairs, the expression is a valid lower bound on its global mean-normal deficit, but it does not determine the complete distribution of the total number of normals. Right-angle coincidences affect nongeneric source points, not the expectation. This self-review is not an independent mathematical audit; historical priority cannot be absolutely guaranteed by the available literature search.

## References
1. I. Nasonov and G. Panina, *Each simplex in \(\mathbb R^4\) has a point with at least 14 emanating normals to its boundary*, arXiv:2610.13475, submitted 9 October 2026.
2. I. Nasonov, G. Panina and D. Siersma, *Concurrent normals problem for convex polytopes and Euclidean distance degree*, arXiv:2406.01773, first posted 3 June 2024; Acta Mathematica Hungarica **174** (2024), 522–538.
3. I. Nasonov and G. Panina, *Each generic polytope in \(\mathbb R^3\) has a point with ten normals to the boundary*, arXiv:2411.12745, first posted October 2024.
4. I. Nasonov and G. Panina, *On \(2n+4\) normals conjecture for convex polytopes in \(\mathbb R^n\)*, arXiv:2510.22695, first posted October 2025.

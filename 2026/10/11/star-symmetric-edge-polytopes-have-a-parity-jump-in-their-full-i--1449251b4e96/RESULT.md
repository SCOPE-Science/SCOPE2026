# Star symmetric-edge polytopes have a parity jump in their full incenter locus
## Finding
For every integer \(m\ge1\), take the star graph \(K_{1,m}\), with central vertex \(0\) and leaves \(1,\ldots,m\). Its standard symmetric-edge polytope is
\[
P_m=\operatorname{conv}\{\pm(e_0-e_i):1\le i\le m\}\subset H_m,
\qquad
H_m=\left\{z\in\mathbb R^{m+1}:\sum_{i=0}^m z_i=0\right\}.
\tag{1}
\]
All distances are Euclidean distances within \(H_m\) induced from \(\mathbb R^{m+1}\). Put \(n=m+1\) and define
\[
\delta_m=\begin{cases}0,&m\text{ even},\\1,&m\text{ odd}.\end{cases}
\]
The exact Euclidean inradius is
\[
\boxed{\rho_m=\frac1{\sqrt{m-\delta_m/(m+1)}}.}
\tag{2}
\]
The origin is always an incenter, but **the uniqueness of the incenter depends on parity**.

If \(m\) is odd, the origin is the **unique incenter**. Its inscribed sphere is tangent to exactly
\[
\boxed{2\binom{m}{(m-1)/2}}
\tag{3}
\]
facets.

If \(m\) is even, the **complete incenter set** is the nondegenerate line segment
\[
\boxed{\mathcal I_m=
\left\{(-mu,u,\ldots,u): -u_m\le u\le u_m\right\},
\qquad
u_m=\frac{1-\sqrt{1-4/(m(m+1))}}2.}
\tag{4}
\]
At every incenter strictly inside the segment, the maximal inball touches exactly
\[
\boxed{\binom{m}{m/2}}
\tag{5}
\]
facets. At either endpoint, precisely
\[
\boxed{\binom{m}{m/2-1}}
\tag{6}
\]
additional facets become tangent.

In both parity regimes, the unique minimum enclosing ball has center \(0\) and radius
\[
\boxed{R_{\mathrm{out}}(P_m)=\sqrt2.}
\tag{7}
\]
All \(2m\) vertices are contacts. The exact ratio of outer to inner radii is therefore
\[
\boxed{\frac{R_{\mathrm{out}}(P_m)}{\rho_m}
=\sqrt{2\left(m-\frac{\delta_m}{m+1}\right)}.}
\tag{8}
\]
Thus a family that is combinatorially a crosspolytope in every dimension has an even-versus-odd transition between a unique incenter and an entire segment of incenters, together with a jump in the number of tangent facets at the segment endpoints.

## Assumptions and scope
The realization of a graph symmetric-edge polytope is the canonical one:
\[
P_G=\operatorname{conv}\{\pm(e_i-e_j):ij\in E(G)\}.
\]
This realization is standard in D'Alì--Delucchi--Michałek. For a tree with \(n\) vertices they record unimodular equivalence to the \((n-1)\)-dimensional crosspolytope, but not Euclidean isometry. The present calculations depend on the Euclidean metric of the **specific signed-incidence embedding** (1), rather than an arbitrary unimodular model.

The vectors
\[
v_i=e_0-e_i\qquad(1\le i\le m)
\]
form a basis of \(H_m\), so (1) is full-dimensional in \(H_m\), of dimension \(m\). The case \(m=1\) is a line segment, and all statements concerning facets use the intrinsic meaning of a facet in its affine span.

## Proof
Because the \(m\) edge vectors \(v_i\) are linearly independent, \(P_m\) is a linear image of the standard \(m\)-crosspolytope. Every facet selects exactly one vertex from each antipodal pair \(\{v_i,-v_i\}\). Thus facets are naturally indexed by sign vectors
\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_m)\in\{\pm1\}^m.
\]
Put
\[
S=\sum_{i=1}^m\varepsilon_i,
\qquad n=m+1.
\tag{9}
\]
The unique vector \(f^\varepsilon\in H_m\) with
\[
\langle f^\varepsilon,v_i\rangle=\varepsilon_i
\qquad(1\le i\le m)
\]
is
\[
\boxed{
f^\varepsilon=
\left(\frac Sn,\frac Sn-\varepsilon_1,\ldots,\frac Sn-\varepsilon_m\right).
}
\tag{10}
\]
Therefore the corresponding facet inequality is
\[
\langle f^\varepsilon,z\rangle\le1,
\tag{11}
\]
with equality at all selected vertices \(\varepsilon_i v_i\).

Directly expanding (10) gives
\[
\begin{aligned}
\|f^\varepsilon\|^2
&=\left(\frac Sn\right)^2+
\sum_{i=1}^m\left(\frac Sn-\varepsilon_i\right)^2\\
&=m-\frac{S^2}{n}.
\end{aligned}
\tag{12}
\]
When \(m\) is even, the smallest possible \(|S|\) is zero, attained by exactly \(\binom{m}{m/2}\) sign vectors. When \(m\) is odd, the smallest possible \(|S|\) is one, attained by exactly \(2\binom{m}{(m-1)/2}\) sign vectors. Hence
\[
\max_{\varepsilon}\|f^\varepsilon\|
=M_m:=\sqrt{m-\frac{\delta_m}{m+1}}.
\tag{13}
\]

For an inscribed Euclidean ball of center \(c\in H_m\) and radius \(\rho\), the complete facet-clearance conditions are
\[
\langle f^\varepsilon,c\rangle+
\rho\|f^\varepsilon\|\le1
\qquad\text{for every }\varepsilon\in\{\pm1\}^m.
\tag{14}
\]
In particular, the opposite pair of facets with normals \(f^\varepsilon\) and \(-f^\varepsilon\) yields
\[
\rho\le\frac{1-|\langle f^\varepsilon,c\rangle|}{\|f^\varepsilon\|}
\le\frac1{\|f^\varepsilon\|}.
\]
Taking a normal of maximum norm proves \(\rho\le1/M_m\) for every possible center. Conversely \(c=0\) with \(\rho=1/M_m\) satisfies every inequality in (14). This proves (2) globally.

It remains to characterize **all** equality centers. If \(\rho=1/M_m\), every maximally long normal in (13) and its opposite must satisfy
\[
\langle f^\varepsilon,c\rangle=0.
\tag{15}
\]
Since \(c\in H_m\), (10) gives the useful simplification
\[
\boxed{\langle f^\varepsilon,c\rangle
=-\sum_{i=1}^m\varepsilon_i c_i.}
\tag{16}
\]

Suppose \(m\) is odd. The sign vectors with \(S=1\) span \(\mathbb R^m\). Indeed, for \(m\ge3\), differences of such vectors under a transposition of an opposite-sign pair span the coordinate-difference subspace \(\{w:\sum_iw_i=0\}\), while any one sign vector with \(S=1\) has nonzero coordinate sum. The case \(m=1\) is immediate. By (15)--(16), all leaf coordinates of \(c\) vanish; their sum and the zero-sum condition also force \(c_0=0\). The incenter is unique, and (3) counts its tangent facets.

Now suppose \(m\) is even. The sign vectors with \(S=0\) span exactly the \((m-1)\)-dimensional subspace \(\{w:\sum_iw_i=0\}\): differences of balanced sign vectors with a switched plus and minus entry generate every coordinate difference. Thus (15)--(16) force all leaf coordinates of \(c\) to equal a common scalar \(u\). The zero-sum condition gives
\[
\boxed{c(u)=(-mu,u,\ldots,u).}
\tag{17}
\]
From (16), a facet indexed by a sign vector with sum \(S\) then imposes
\[
-Su+\frac{\sqrt{m-S^2/n}}{\sqrt m}\le1.
\]
Because sign sums \(S\) and \(-S\) both occur, the pair of inequalities is equivalent to
\[
|S u|\le1-\sqrt{1-\frac{S^2}{mn}}.
\tag{18}
\]
For \(S=0\) this is automatically an equality. For the possible positive values
\[
S\in\{2,4,\ldots,m\},
\]
(18) becomes
\[
|u|\le g(S):=
\frac{1-\sqrt{1-S^2/(mn)}}S
=\frac{S}{mn\left(1+\sqrt{1-S^2/(mn)}\right)}.
\tag{19}
\]
The numerator \(S\) strictly increases, while the positive denominator's factor \(1+\sqrt{1-S^2/(mn)}\) strictly decreases. Hence \(g(S)\) is strictly increasing on this range, and the **only strongest nonzero sign-sum constraint** is \(S=2\). This proves the exact segment (4). Its half-length parameter is strictly positive for every even \(m\ge2\), so the incenter set has affine dimension one.

At an interior segment point, all constraints with \(|S|\ge2\) are strict and precisely the \(S=0\) facets are contacts. At the positive endpoint, the constraints for \(S=-2\) also become equalities, and at the negative endpoint the analogous facets have \(S=+2\). Each new class has \(\binom{m}{m/2-1}\) sign vectors, proving the contact counts (5)--(6).

Finally, each vertex of \(P_m\) has squared norm
\[
\|\pm(e_0-e_i)\|^2=2.
\]
Thus the radius-\(\sqrt2\) ball centered at the origin contains all vertices and hence the entire polytope. For any alternative center \(y\), averaging the squared distances to any opposite pair gives
\[
\frac{\|v_i-y\|^2+\|-v_i-y\|^2}{2}
=2+\|y\|^2.
\tag{20}
\]
At least one member of that pair is at squared distance at least this average. Hence no enclosing ball has radius less than \(\sqrt2\), and equality forces \(y=0\). This gives the unique outer ball and its entire contact set, completing the proof.

## Verification
The formulas hold for all integers \(m\ge1\), by the symbolic proof above. The standalone `verify.py` independently enumerates all \(2^m\) facets for \(1\le m\le11\), reconstructs each normal from signed edge pairings, checks the squared norm formula and the equality count, solves the **full** inradius linear program with arbitrary centers, and optimizes the full set of center clearances at the claimed maximum radius. It also tests the segment endpoints and the endpoint contact counts. These finite computations are corroborative only.

## Relationship to prior work
D'Alì, Delucchi, and Michałek prove the general facet-labeling criterion for symmetric edge polytopes and observe that the symmetric edge polytopes of **all trees** are unimodularly equivalent to crosspolytopes. Their discussion connects these polytopes to Kantorovich--Rubinstein fundamental polytopes of graph metrics and the Kuramoto adjacency-polytope construction. Their results focus on faces, Ehrhart data, and graph transformations, not Euclidean inballs.

D'Alì, Juhnke-Kubitzke, and Koch generalize symmetric edge polytopes to regular matroids and show their uniqueness up to unimodular equivalence; their theory of facets and polar Ehrhart data likewise does not determine the Euclidean incenter set in a fixed embedding. Cuchilla and collaborators subsequently show that canonical graph symmetric-edge polytopes are unitarily equivalent exactly when their graphs are isomorphic, underlining why Euclidean geometry may distinguish tree shapes even though their polytopes are unimodularly equivalent. Their paper treats equivariant volumes and group actions, not the present inradius or all-incenter classification.

For the star, the dual facet lengths depend **only** on the imbalance \(S\) of a sign vector. Its parity-constrained minimum directly creates the inradius formulas, while the linear span of those extremal sign vectors is either full-dimensional or codimension one, creating the incenter-locus parity jump. This is a metric effect not specified by the abstract crosspolytope combinatorics or by unimodular equivalence.

## Limitations
The theorem concerns only unweighted stars in their canonical signed-incidence realization and the Euclidean metric inherited from the zero-sum hyperplane. It does not claim affine invariance, a classification of incenter loci for every tree, or a formula for weighted tree metrics. All star polytopes have the same combinatorial type, but applying arbitrary linear transformations generally changes their inradius and incenter locus.

The facet-normal calculation is elementary after the realization is chosen. Consequently an independent equivalent observation under finite-metric, root-system, or Lipschitz-free terminology remains a residual literature-indexing risk. Failure of targeted searches is not a mathematical proof of global novelty.

## References
1. Alessio D'Alì, Emanuele Delucchi, and Mateusz Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, first publicly posted 2019-10-11; *Electronic Journal of Combinatorics* 29 (2022), P3.24, DOI 10.37236/10387.
2. Alessio D'Alì, Martina Juhnke-Kubitzke, and Melissa Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933v1 (2023).
3. Tito Augusto Cuchilla, Joseph Hound, Cole Plepel, Andrés R. Vindas-Meléndez, and Louis Ye, *Unitary actions and equivariant volumes of symmetric edge polytopes*, arXiv:2507.18846v2 (2025).

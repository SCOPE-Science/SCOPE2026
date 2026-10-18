# A persistent \(3\)-sphere in the first Euclidean Rips stages of the \(F_4\) roots

## Finding
Let \(R\subset\mathbb R^4\) be the standard unrescaled crystallographic root system of type \(F_4\): its \(24\) short roots are \(\{\pm e_i\}_{i=1}^4\cup\{(\pm\tfrac12,\pm\tfrac12,\pm\tfrac12,\pm\tfrac12)\}\), and its \(24\) long roots are \(\{\pm e_i\pm e_j:1\le i<j\le4\}\). Define \(K_r=\operatorname{VR}_{\le r}(R)\) by the inclusive Euclidean-diameter convention.

**Theorem.** The inclusions give the following first stages, with all indicated homotopy information integral:
\[
K_r\cong\bigsqcup^{48}\mathrm{pt}\quad(0\le r<1),\qquad
K_1\cong\operatorname{sd}_{\mathrm{facets}}\partial P\cong S^3,
\]
where \(P\) is the regular \(24\)-cell on the short roots and the middle symbol denotes stellar subdivision of every octahedral facet. Moreover, \(K_{\sqrt2}\) **simplicially collapses onto its subcomplex \(K_1\)** by exactly \(1704\) explicit elementary pairs. Consequently
\[
K_r\simeq S^3\quad(1\le r<\sqrt3),
\qquad K_1\longrightarrow K_{\sqrt2}\text{ is a homotopy equivalence}.
\]
The full Weyl group \(W(F_4)\), of order \(1152\), acts on the unique nonzero reduced integral homology group \(\widetilde H_3(K_r;\mathbb Z)\cong\mathbb Z\) by the orientation character \(g\mapsto\det(g)\), for \(1\le r<\sqrt3\). The inclusion-induced map is an isomorphism of integral \(W(F_4)\)-modules. This is an assertion about the induced representation, not an equivariant collapse certificate.

## Assumptions and scope
The \(48\) roots are not radially normalized: short roots have squared norm \(1\), long roots squared norm \(2\). The metric is the ambient Euclidean metric, not graph distance. Vertices in the supplied checker are ordered as \(8\) signed coordinate short roots, \(16\) half-integral short roots, and \(24\) two-coordinate long roots. Its coordinates are all multiplied by \(2\) to avoid fractions, so squared thresholds \(4\) and \(8\) correspond exactly to Euclidean radii \(1\) and \(\sqrt2\). The next squared distance is \(3\), so there are no further simplicial changes before \(\sqrt3\).

The respective face vectors, from vertices upward, are
\[
f(K_1)=(48,240,384,192),\qquad
f(K_{\sqrt2})=(48,408,1224,1560,840,168,24).
\]

## Proof
**The first stage and the \(24\)-cell.** Let \(S\) denote the short roots and \(L\) the long roots. The regular \(24\)-cell \(P=\operatorname{conv}S\) has the exact half-space description
\[
P=\{x\in\mathbb R^4:\ell\cdot x\le1\text{ for every }\ell\in L\}.
\]
For completeness, these inequalities are equivalent to \(|x_i|+|x_j|\le1\) for all distinct coordinates. In the chamber \(x_1\ge x_2\ge x_3\ge x_4\ge0\), this polytope is a simplex with vertices \(0\), \(e_1\), \((\tfrac12,\tfrac12,0,0)\), \((\tfrac12,\tfrac12,\tfrac12,0)\), and \((\tfrac12,\tfrac12,\tfrac12,\tfrac12)\), each lying in \(\operatorname{conv}S\); symmetry proves the description. Each supporting hyperplane \(\ell\cdot x=1\) meets \(S\) at exactly six points forming an octahedral facet, hence the \(24\) long roots index all \(24\) facets.

Distinct long roots are at Euclidean distance at least \(\sqrt2\). Two short roots have distance at most \(1\) precisely when they form an edge of \(P\). A short root \(s\) is distance at most \(1\) from a long root \(\ell\) precisely when \(\ell\cdot s=1\), namely when \(s\) is a vertex of the indexed facet. The short-root clique complex is exactly the \(2\)-skeleton of \(\partial P\): all \(96\) triangles are facet triangles, and there are no four-vertex short cliques. Each long-root link is the octahedral \(2\)-sphere on its facet's six vertices. Thus \(K_1\) replaces each octahedral \(3\)-cell of \(\partial P\) by the cone on its boundary. Sending the long-root vertex \(\ell\) abstractly to the facet interior point \(\ell/2\) identifies this with the facet-stellar subdivision of \(\partial P\), proving \(K_1\cong S^3\). It is essential that this is a geometric realization of the *abstract* complex: the original long roots themselves lie outside \(P\).

**The next stage.** At radius \(\sqrt2\), enumerate all cliques using the exact distance inequality (no floating point arithmetic). Exactly \(3408\) new nonempty simplices appear. File `collapse_pairs.txt` lists \(1704\) pairs of face masks in removal order, each pair consisting of a free simplex \(\sigma\) and its unique immediate coface \(\tau\), with \(\sigma\subset\tau\) and \(\dim\tau=\dim\sigma+1\). The standalone checker recomputes the entire complex, verifies that each \(\sigma\) is free at the instant of deletion, and confirms that no \(K_1\) simplex is ever removed. After all deletions the remaining face set equals precisely \(K_1\). The counts by free-face dimension \(1,2,3,4,5\) are \(168,672,696,144,24\), respectively. Therefore \(K_{\sqrt2}\searrow K_1\) by elementary simplicial collapses, proving the homotopy and persistent-homology assertions without using homology rank calculations as substitutes for homotopy arguments.

**Weyl action.** Every \(g\in W(F_4)\) is an orthogonal transformation preserving \(R\), the two root lengths, and the metric filtration. The facet-stellar identification of \(K_1\) with \(\partial P\) is \(W(F_4)\)-equivariant because \(g(\ell/2)=g(\ell)/2\). The degree of its action on \(H_3(\partial P;\mathbb Z)\) is \(\det(g)\). The inclusion \(K_1\hookrightarrow K_{\sqrt2}\) is equivariant and, by the preceding collapse, a homotopy equivalence. This transports the determinant representation to \(K_{\sqrt2}\) and all unchanged intervening stages.

## Verification
Execute `python3 verify.py` from the directory containing `verify.py` and `collapse_pairs.txt` (or execute the script by its actual path). It uses only the Python standard library. It constructs all \(48\) roots, compares exact squared Euclidean distances, enumerates all cliques, checks the \(24\)-cell facet incidences, and replays each of the \(1704\) free-face deletions. Success prints `VERIFY_OK` with both face vectors and all five pair counts. Unlike a rank-only calculation, the pair-by-pair replay directly verifies the claimed inclusion-preserving collapse.

The checker uses hex-encoded \(48\)-bit face masks. The list `collapse_pairs.txt` is a finite certificate specific to the stated coordinates and vertex ordering. No outside package, computation at an unmentioned scale, or preexisting runtime artifact is required.

## Relationship to prior work
Cohn, Conway, Elkies and Kumar (2006) explicitly identify the \(D_4\) root configuration with the \(24\)-cell and study its spherical-code geometry, not the \(48\)-point \(F_4\) Rips filtration. Ardila, Beck, Hosten, Pfeifle and Seashore (2008) construct root-polytope triangulations for classical types \(A,C,D\); their theorems concern root-polytopal boundary triangulations and lattice growth, not the Euclidean \(F_4\) radius-\(\sqrt2\) inclusion. Chachólski, Jin, Scolamiero and Tombari (2021) establish general tools for homotopical decompositions of Rips complexes but do not supply the displayed \(F_4\) collapse. Related finite-polytope Rips computations and a root-system \(D_n\) calculation involve different point sets or different metrics and do not imply the explicit inclusion-preserving \(F_4\) result.

The radius-one facet subdivision is a geometric identification following from standard \(24\)-cell incidence; the point asserted beyond those standard facts is the **explicit relative elementary collapse at radius \(\sqrt2\)** and its resulting integral, symmetry-compatible persistence statement.

## Limitations
No scale at or above \(\sqrt3\) is classified, and no death time for the surviving degree-three persistence class is asserted. The certificate is an ordinary (not Weyl-equivariant) collapse; equivariance is claimed only for the homology isomorphism induced by the canonical inclusion. Existing literature under a dual-\(24\)-cell or root-graph alias could still contain an equivalent collapse, so the literature comparison is not a uniqueness proof. Independent scientific validation has not been performed.

## References
1. H. Cohn, J. H. Conway, N. D. Elkies and A. Kumar, *The \(D_4\) root system is not universally optimal*, arXiv:math/0607447, first public submission 2006-07-19, https://arxiv.org/abs/math/0607447.
2. F. Ardila, M. Beck, S. Hosten, J. Pfeifle and K. Seashore, *Root polytopes and growth series of root lattices*, arXiv:0809.5123, first public submission 2008-09-30, https://arxiv.org/abs/0809.5123.
3. W. Chachólski, A. Jin, M. Scolamiero and F. Tombari, *Homotopical decompositions of simplicial and Vietoris Rips complexes*, Journal of Applied and Computational Topology 5 (2021), 215–248, https://doi.org/10.1007/s41468-021-00066-2.

# Exact cone-direction spectrum and pyramidal core of convex bodies

## Finding

For every integer \(n\ge 2\), let \(K\subset\mathbb R^n\) be a compact convex body with nonempty interior. Call a unit vector \(u\in S^{n-1}\) a **cone direction** when there is a point \(a\notin H_u\) such that
\[
K=\operatorname{conv}((K\cap H_u)\cup\{a\}),\qquad H_u=\{x:\langle x,u\rangle=h_K(u)\},
\]
where \(h_K\) is the support function. Let \(c(K)\) be the number of its distinct cone directions.

The **exact spectrum** is
\[
\boxed{c(K)\in\{0,1,\ldots,n-2\}\cup\{n+1\}.}
\]
Every listed value occurs, and \(c(K)=n+1\) holds exactly for simplices. In particular, a nonsimplex body has at most \(n-2\) cone directions, two fewer than the sharp general maximum.

More precisely, if \(K\) is nonsimplicial and its \(k\ge1\) cone directions have apexes \(a_1,\ldots,a_k\) and base supporting hyperplanes \(H_1,\ldots,H_k\), then \(k\le n-2\), the apexes are affinely independent, the hyperplane normals are linearly independent, and
\[
B:=K\cap\bigcap_{i=1}^k H_i\quad\text{has dimension }n-k,\qquad K=\operatorname{conv}(B\cup\{a_1,\ldots,a_k\}).
\]
Thus the cone directions determine a canonical \(k\)-fold pyramidal decomposition over a convex base. (When \(k=0\) the decomposition assertion is vacuous.)

## Assumptions and scope

The dimension is an integer \(n\ge2\); all bodies are compact, convex, and full-dimensional in Euclidean space. Cone direction is the outer normal to a full-dimensional base face of a genuine cone, with its opposite apex off that face; opposite normals are not counted together unless they independently satisfy the definition. The assertion concerns exact cone directions, not approximate conicality, normal cones, or arbitrary supporting directions. The base \(B\) in the structural statement is defined only for nonsimplicial bodies with \(k\ge1\).

## Proof

**1. An apex is unique to its cone direction.** If \(K=\operatorname{conv}(F\cup\{a\})\) with \(F=K\cap H\), then full dimensionality forces \(\dim F=n-1\). The apex \(a\) is exposed: it is the unique point in the supporting hyperplane parallel to \(H\) on the opposite side. All other extreme points of \(K\) belong to \(F\), and every extreme point of the exposed face \(F\) is extreme in \(K\). Consequently \(F\) is determined by the extreme points of \(K\) other than \(a\), by the finite-dimensional theorem that a compact convex set is the closed convex hull of its extreme points. If two cone directions had the same apex, they would have the same full-dimensional base face, hence the same base supporting hyperplane and its unique outer unit normal. Thus distinct directions have distinct apexes.

**2. The apexes are affinely independent.** Write the distinct apexes as \(a_1,\ldots,a_k\), with bases \(F_i=K\cap H_i\). Each \(a_j\) is an extreme point. For \(j\ne i\), it must lie in \(F_i\), hence in \(H_i\). Define an affine functional \(\ell_i\) vanishing on \(H_i\) and positive at \(a_i\). If \(\sum_j t_j a_j=0\) and \(\sum_j t_j=0\), applying \(\ell_i\) yields \(t_i\ell_i(a_i)=0\), so every \(t_i=0\). The apexes are therefore affinely independent and \(k\le n+1\).

**3. The maximal case is exactly a simplex.** If \(k=n+1\), each \(H_i\) contains the \(n\) affinely independent apexes other than \(a_i\), so it is the corresponding facet hyperplane of their simplex. Those \(n+1\) hyperplanes have empty common intersection: in barycentric coordinates all coordinates would have to vanish although their sum is one. Any extreme point of \(K\) other than the apexes would have to lie in every \(H_i\), which is impossible. Thus \(K\) is precisely their simplex. Conversely each vertex of an \(n\)-simplex is an apex over the opposite facet, furnishing \(n+1\) cone directions.

**4. The canonical residual base.** Suppose \(1\le k\le n\). The apexes alone cannot span a full-dimensional body, so there exists an extreme point \(b\) other than them. Necessarily \(b\in H_i\) for every \(i\). Write \(\ell_i(x)=\langle v_i,x-b\rangle\), with \(\ell_i(a_i)>0\). If \(\sum_i t_i v_i=0\), evaluating the zero affine function \(\sum_i t_i\ell_i\) at \(a_j\) yields \(t_j\ell_j(a_j)=0\). Thus \(v_1,\ldots,v_k\) are linearly independent, and \(L=\bigcap_iH_i\) has dimension \(n-k\). Let \(B=K\cap L\). Every extreme point of \(K\) is either an apex or in \(B\), hence compact convexity gives \(K=\operatorname{conv}(B\cup\{a_1,\ldots,a_k\})\). Since this set has dimension \(n\), while its affine dimension is at most \(\dim B+k\), we have \(\dim B\ge n-k\). Therefore \(\dim B=n-k\). The construction of \(B\) from all cone directions is intrinsic, making the decomposition canonical.

**5. The two forbidden counts.** If \(k=n\), then \(\dim B=0\); \(K\) is the full-dimensional convex hull of \(n\) apexes and one point, thus a simplex, contradicting \(k=n\) rather than \(n+1\). If \(k=n-1\), then \(\dim B=1\), so \(B\) is a nondegenerate segment; the full-dimensional hull of its two endpoints and the \(n-1\) apexes is again a simplex, the same contradiction. Consequently every nonsimplex satisfies \(k\le n-2\).

**6. Realizing all remaining counts.** Fix \(k\in\{0,1,\ldots,n-2\}\) and put \(m=n-k\ge2\). In \(\mathbb R^n\), take
\[
K_{n,k}=\operatorname{conv}\bigl(\{\pm e_j:1\le j\le m\}\cup\{e_{m+1},\ldots,e_n\}\bigr).
\]
For each of the last \(k\) coordinate vertices, all other vertices lie on the supporting hyperplane where that coordinate is zero, so each is a cone apex. None of the first \(2m\) vertices is a cone apex: after removing any one of the vertices \(\pm e_j\), the remaining cross-polytope vertices still affinely span its full \(m\)-dimensional coordinate space (use the pairs \(\pm e_\ell\) for \(\ell\ne j\) and the opposite point \(\mp e_j\)). Consequently they cannot all lie in a supporting hyperplane excluding the removed vertex. There are no other extreme points. Hence \(c(K_{n,k})=k\), completing the spectrum and sharpness.

## Verification

The proof is valid for every integer \(n\ge2\) without relying on finite sampling. An independent exact-rank implementation of the vertex criterion is supplied as `verify_cones.py`; its asserted finite instances include all \(K_{n,k}\) for \(2\le n\le8\), every permitted \(k\), and simplices in the same dimensions. The implementation checks that a vertex is a cone apex precisely when the other listed vertices have affine rank \(n-1\). This computation tests examples, not the infinite-dimensional-parameter quantifiers proved above.

## Relationship to prior work

Feldman, *Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment*, arXiv:2608.04516v1 (first public August 5, 2026), Lemma 8, proves only that the number of cone directions of a full-dimensional convex body is finite. Immediately after that proof, the text conjectures the upper bound \(n+1\) and simplex-only equality. The present result proves that bound and rigidity, strengthens it to the exact forbidden-gap spectrum, and identifies the residual pyramidal base.

The standard notion of a multifold pyramid/free join appears in the polytope literature, including Pineda-Villavicencio, Ugon, and Yost, *Lower bound theorems for general polytopes* (2019), but the cited discussion concerns polytope face counts and specialized constructions, not the exact count of all supporting cone directions for arbitrary convex bodies. The decomposition here uses only elementary affine geometry and the classical extreme-point representation; no new convexity inequality or improved centroid-overlap constant is claimed.

## Limitations

The result does not quantify near-cone directions or stability under perturbations, and does not resolve the two-body overlap problem or other open questions in the originating paper. Its proof is short and structural; the full cone-direction spectrum could have appeared implicitly in unindexed earlier work on free joins and pyramids. Exact-rank tests check only finite examples. The finding is not an independently validated publication.

## References

1. D. V. Feldman, *Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment*, arXiv:2608.04516v1 (August 5, 2026), especially §3.1, Lemma 8, and §5. https://arxiv.org/html/2608.04516v1
2. G. Pineda-Villavicencio, J. Ugon, D. Yost, *Lower bound theorems for general polytopes*, European Journal of Combinatorics (2019), https://doi.org/10.1016/j.ejc.2018.12.003 .
3. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press (2014), for standard extreme-point convexity background.

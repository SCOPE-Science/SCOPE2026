# Which edges pin the Minkowski centers of a cut polytope?

## Finding

Let \(G=(V,E)\) be a finite simple undirected graph with \(E\ne\varnothing\), and let \(P_G\) be the convex hull of its ordinary cut-indicator vectors in \(\mathbb R^E\). Isolated vertices and disconnected graphs are allowed. Write \(h=\tfrac12\mathbf1_E\). If \(\mathcal M_G\) is the set of minimizing Minkowski centers, the following criterion determines its affine hull without imposing edge transitivity.

For \(\sigma\in\{-1,1\}^V\), let \(x^\sigma_{uv}=\sigma_u\sigma_v\), and define the polytope
\[
 D_G=\{a\in\mathbb R^E:1+a\cdot x^\sigma\ge0\text{ for all }\sigma\}.
\]
Let \(D_G^*\) be the face maximizing \(\sum_e a_e\), and let \(E_*\subseteq E\) be the union of the supports of the vectors in \(D_G^*\) (support means the set of nonzero coordinates). Then
\[
 \operatorname{aff}\mathcal M_G=\{c\in\mathbb R^E:c_e=1/2\ (e\in E_*)\},
 \qquad \dim\mathcal M_G=|E\setminus E_*|.
\]
In particular the center is unique if and only if the dual optimum admits a vector of full support. Equivalently, \(E_*\) is the union of the supports of the normals of the facets of the signed cut polytope incident to its negative diagonal radial endpoint. The criterion is about the affine hull, not the global extent of the center set along free coordinates.

## Proof

**Switching and the dual problem.** Pass by the affine map \(x\mapsto\mathbf1_E-2x\) to the signed cut polytope \(K=\operatorname{conv}\{x^\sigma\}\). Multiplication by \(x^\sigma\) coordinatewise defines an invertible diagonal map \(T_\sigma\) preserving \(K\), since \(T_\sigma x^\eta=x^{\sigma\eta}\). Under uniform vertex signs, the edge characters are mean zero and pairwise orthogonal (edges are distinct unordered pairs). If a linear functional is constant on the signed cut vectors, averaging makes that constant zero and pairing with each character makes all coefficients zero. Thus \(K\) is full dimensional, and its average \(0\) over the signed cuts is interior.

For dilation \(s\), a center \(b\) for \(K\) is feasible if \(((s+1)b-x^\sigma)/s\in K\) for all \(\sigma\). This defines a convex, switching-invariant set. Consequently, if any center is feasible at \(s\), so is its switching average \(0\). At \(0\) the membership tests reduce by switching to \(-\mathbf1_E/s\in K\). Let \(s=s(K)\) be the least admissible dilation and \(p=-\mathbf1_E/s\). It is the negative-diagonal radial endpoint; no point further along that ray can belong to \(K\), even if \(s=1\), because \(K\subset[-1,1]^E\). Now \(D_G=-K^\circ\), where \(K^\circ=\{q:q\cdot y\le1\text{ for all }y\in K\}\). The polar membership tests at \(p\) show \(s=\max_{a\in D_G}a\cdot\mathbf1_E\). The active facet tests at \(p\) are exactly the vertices of the dual face \(D_G^*\), with the facet normal sign reversed.

**Pins.** For a feasible \(b\) at this optimal \(s\), switching the reflected point for \(x^\sigma\) produces
\[
  p+\frac{s+1}{s}T_\sigma b\in K.
\]
Apply any \(a\in D_G^*\): it satisfies \(1+a\cdot p=0\), so \(a\cdot T_\sigma b\ge0\) for every \(\sigma\). This signed sum has expectation zero, hence it vanishes for every \(\sigma\). Pairing with the edge character \(x_e^\sigma\) gives \(a_e b_e=0\) for every \(e\). Consequently every minimizing \(b\) vanishes on \(E_*\).

**No further affine constraints.** Let \(L=\{b:b_e=0\ (e\in E_*)\}\). For \(b\in L\), every active facet constraint at \(p\) remains an equality at \(p+((s+1)/s)T_\sigma b\), for each \(\sigma\). Every other facet has strict slack at \(p\); the list is finite, and \(\|T_\sigma b\|_2=\|b\|_2\). Thus all the remaining tests hold for every sufficiently small \(b\in L\), uniformly in \(\sigma\). These \(b\) are feasible; the affine hull is exactly \(L\) in the signed coordinates and gives the displayed formula in the original coordinates. A full-support optimal vector exists when \(E_*=E\), since a nonempty polytope cannot be covered by finitely many coordinate hyperplanes none of which contains its affine hull. This proves the uniqueness criterion.

## Examples and the edge-transitive specialization

If \(G\) is edge-transitive, write \(m=|E|\) and \(M=\operatorname{MaxCut}(G)\). The average of the signed cut vectors of maximum cuts is \((1-2M/m)\mathbf1_E\). The inequality \(\sum_e y_e\ge m-2M\) on \(K\) shows that this point is the negative diagonal endpoint. Here \(M>m/2\), since a uniformly random cut has mean size \(m/2\) and includes the empty cut with positive probability. Hence \(s=m/(2M-m)\), and \(a=(2M-m)^{-1}\mathbf1_E\) belongs to \(D_G^*\) and has full support. The criterion gives the unique center \(h\). For a balanced complete \(r\)-partite graph of part size \(t\), \(m=t^2\binom r2\) and \(M=t^2\lfloor r^2/4\rfloor\): the cut size is affine separately in the number of selected vertices from each part, so a maximizing choice can be made at an endpoint in each part. The quantitative specialization therefore gives \(r-1\) for even \(r\) and \(r\) for odd \(r\).

For a nontransitive example, attach \(q\) pendant edges to one vertex of a triangle. The signed cut polytope is the product of the signed triangle cut polytope with \([-1,1]^q\), since each leaf sign can choose its bridge coordinate independently for each triangle cut. The triangle has \(s=3\) and a unique center at zero in signed coordinates. By projecting a reflected containment to each factor, and taking products for the reverse direction, the product has \(s=3\). The cube factor has precisely \(|b_e|\le1/2\) as its factor-three center condition, since \(\max_{x_e\in[-1,1]}|4b_e-x_e|=4|b_e|+1\). Thus the original centers have the triangle edges pinned at \(1/2\) and the \(q\) bridge coordinates ranging independently in \([1/4,3/4]\). This illustrates why having a switching-invariant center does not suffice to prove uniqueness.

## Relationship to prior work and scope

Switching symmetries are standard in cut-polytope geometry (Deza and Dutour Sikirić, [arXiv:1501.05407](https://arxiv.org/abs/1501.05407)). The numerical optimization \(\max_{D_G}\sum_e a_e\) is the Boolean edge-shell Turán constant minus one, by finite-group Fourier positivity. The edge-transitive MaxCut value for this optimization was given in *Turán constants of Boolean edge shells on edge-transitive graphs* ([Resultary](https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-tur-n-constants-of-boolean-edge-shells-on-edge-transitive-graphs--8b1ea7ca3db1/RESULT.md)); it also equals the cubical chromatic number minus one on that class by Šámal, [arXiv:0911.2589](https://arxiv.org/abs/0911.2589), Lemma 2.1 and the cubical-coloring normalization. The numerical specialization here is an application, not a claim of a new MaxCut formula. Center-dimension results for a specified minor-free family with pentagonal and triangle constraints appear in *A fivefold asymmetry barrier and center-dimensional transition for \(K_{3,3}\)-minor-free cut polytopes* ([Resultary](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-fivefold-asymmetry-barrier-and-center-dimensional-transition-f--230587b7259c/RESULT.md)). The criterion here describes the affine hull for general simple graphs through the support of the full optimum face; it does not give that face without solving a cut optimization problem, nor does it decide publication priority exhaustively.

## Verification

The support criterion is proved above by the switched facet tests, character orthogonality and finite slack. It needs no computational hypothesis. The accompanying original finite checker corroborates only the numerical edge-transitive and balanced multipartite specializations.

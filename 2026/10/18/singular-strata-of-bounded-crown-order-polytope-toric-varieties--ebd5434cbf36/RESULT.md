# Singular strata of bounded-crown order-polytope toric varieties

## Finding

Let \(n\ge4\). The bounded crown \(P_n\) has elements \(\bot,\top,a_1,\ldots,a_n,b_1,\ldots,b_n\) and covers \(\bot\lessdot a_i\), \(a_i\lessdot b_j\) for \(i\ne j\), and \(b_j\lessdot\top\). Write \(X_n\) for the \((2n+2)\)-dimensional normal projective toric variety of the **normal fan** of the order polytope \(\mathcal O(P_n)\), over any algebraically closed field.

**Theorem.** Its reduced singular locus has exactly
\[
N_n=2n+\binom n2\binom{n-2}{2}+\binom n3
\]
irreducible components, partitioned into the following three explicitly indexed families:

1. **Boundary components** \(L_j,U_j\), one of each for \(1\le j\le n\): codimension \(n\), dimension \(n+2\). The transverse affine toric singularity at the generic point is the affine cone over the Segre embedding \((\mathbb P^1)^{n-1}\hookrightarrow\mathbb P^{2^{n-1}-1}\), of Hilbert--Samuel multiplicity \((n-1)!\).
2. **Middle quadrangle components** \(Q_{A,B}\), for disjoint two-element subsets \(A,B\subseteq[n]\): codimension \(3\), dimension \(2n-1\), generic transverse conifold \(\operatorname{Spec}k[u,v,w,z]/(uv-wz)\), multiplicity \(2\).
3. **Middle hexagon components** \(H_T\), for three-element subsets \(T\subseteq[n]\): codimension \(5\), dimension \(2n-3\), generic transverse rank-one determinantal cone \(\operatorname{Spec}k[z_{ij}:1\le i,j\le3]/I_2(z_{ij})\), multiplicity \(6\).

All the components contain the same torus-invariant projective line, and their set-theoretic total intersection is precisely that line. The singular locus is not equidimensional: for \(n=4\), its \(18\) components have dimensions \(7\) (six), \(6\) (eight), and \(5\) (four). Of the \(2^{n+1}+n+1\) torus-fixed points of \(X_n\), exactly **one** is smooth. These claims concern the reduced singular locus, not its scheme structure.

## Assumptions and scope

We use the full coordinate lattice \(M=\mathbb Z^{P_n}\) and the convention
\[
\mathcal O(P_n)=\{x\in[0,1]^{P_n}:x_u\le x_v\text{ whenever }u<v\}.
\]
For a face \(F\) of this polytope, let \(\sigma_F\) be its outward normal cone and \(Y_F=V(\sigma_F)\) the torus-invariant orbit closure. Toric dimension is \(d=2n+2\); the codimension of \(Y_F\) is \(\dim\sigma_F\). Every family in the theorem is indexed without repetitions. The transverse models are isomorphisms after restricting to an invariant neighborhood of the generic orbit, up to a smooth torus factor.

More explicitly, \(L_j=Y_{F_j}\) where the equal-value block defining \(F_j\) is \(\{\bot,b_j\}\cup\{a_i:i\ne j\}\); \(U_j\) is the order-dual block \(\{\top,a_j\}\cup\{b_i:i\ne j\}\). The block for \(Q_{A,B}\) is \(\{a_i:i\in A\}\cup\{b_j:j\in B\}\), and that for \(H_T\) is \(\{a_i,b_i:i\in T\}\). Each face is obtained by imposing equality of the coordinates within its stated block and no additional equalities.

## Proof

**1. Primitive fan normals and smoothness.** Stanley's facet theorem supplies the primitive normals of \(\mathcal O(P_n)\): the two exterior normals for \(x_\bot=0\) and \(x_\top=1\), and the vectors \(e_u-e_v\) for every Hasse cover \(u\lessdot v\). Think of the two exterior normals as extra edges linking \(\bot\) to an artificial bottom and \(\top\) to an artificial top. For any face the active normals form a signed vertex-edge incidence matrix of a graph \(G_F\). The rank is the number of vertices minus the number of its connected components. Incidence matrices are totally unimodular; any forest subset is an integral part of a basis of the ambient lattice. Hence \(\sigma_F\) is smooth precisely when \(G_F\) is a forest. In particular a nonsmooth normal cone has a cycle; no simplicial but nonunimodular cones occur.

**2. Minimal cyclic equality blocks.** Active cover edges identify equal coordinates, and equalities are transitively closed along poset intervals. The two artificial exterior edges cannot participate in a cycle. If a cyclic equality block contains \(\bot\), a cycle requires \(b_j\) for some \(j\); the equalities \(x_\bot=x_{b_j}\) force \(x_{a_i}\) to have the same value for **all** \(i\ne j\). Thus every such block contains the complete \(K_{2,n-1}\) incidence configuration for \(L_j\). Conversely this block is feasible: choose the remaining \(a_j\) and \(b_i\), \(i\ne j\), strictly above it. It has \(2(n-1)\) active edges, rank \(n\), and is minimal among cyclic feasible active-edge sets. The order-dual argument gives the \(U_j\). If an equality block contains both \(\bot\) and \(\top\), it forces every coordinate equal and already contains these boundary configurations.

A cyclic equality block involving only middle-rank elements has the induced bipartite active graph \(K_{A,B}\) minus its matching edges. Every shortest cycle in this graph is chordless. An induced four-cycle exists exactly for disjoint \(A,B\) of size two, and its four-edge equality block is feasible. There can be no induced cycle of length at least eight: a left-hand vertex would have at least two nonneighbors on the selected right side, whereas only its matched partner is ever a nonneighbor. An induced six-cycle has three vertices on each side and requires the three omitted matching edges to lie inside the selected sets, forcing identical three-element index sets \(T\) on both sides. Its six-edge equality block is feasible by assigning lower values to all outside \(a\)'s and higher values to all outside \(b\)'s. The resulting \(Q_{A,B}\) and \(H_T\) blocks contain no smaller cyclic feasible equality block. Consequently **every** nonsmooth cone contains a cone from exactly these indexed minimal families, and every listed cone is inclusion-minimal among nonsmooth cones. The corresponding invariant orbit closures are therefore precisely the irreducible components of the reduced singular locus.

Counting gives \(2n\) boundary blocks, \(\binom n2\binom{n-2}2\) disjoint ordered-side quadrangles, and \(\binom n3\) hexagons. The graph ranks are \(n,3,5\), giving the stated dimensions and codimensions.

**3. Generic transverse affine models.** In a normal cone of boundary type, subtract the common \(\bot\)-coordinate. The dual integral semigroup is
\[
\{(t,s_1,\ldots,s_{n-1})\in\mathbb Z^{n}_{\ge0}:0\le s_i\le t\ \text{for all }i\}.
\]
It is generated by the \(2^{n-1}\) degree-one exponent vectors \((1,\varepsilon_1,\ldots,\varepsilon_{n-1})\) with \(\varepsilon_i\in\{0,1\}\). Its semigroup algebra is the standard homogeneous coordinate ring of the Segre product of \(n-1\) projective lines. Its projective degree, hence vertex Hilbert--Samuel multiplicity, is \((n-1)!\).

For a middle quadrangle or hexagon, the primitive normal rays are the edges of one coherently oriented even cycle of length \(2r\), with \(r=2\) or \(3\). Any spanning-tree subset is an integral lattice basis, and the sole primitive ray relation has \(r\) coefficients \(+1\) and \(r\) coefficients \(-1\). The saturated affine toric semigroup ring is consequently the invariant subring of a polynomial ring in \(2r\) variables under a one-dimensional torus of weights \((1^r,-1^r)\). It is generated by pair-products \(z_{ij}\) with defining equations the \(2\times2\) minors of the \(r\times r\) matrix \((z_{ij})\). The rank-one determinantal cone has dimension \(2r-1\) and Hilbert--Samuel multiplicity \(\binom{2r-2}{r-1}\). These yield the conifold and \(3\times3\) models and multiplicities. The incidence lattices are saturated, so all identifications hold integrally and in every characteristic.

**4. Intersections and torus-fixed points.** Every minimal block identifies only coordinate values, and the one-dimensional order-polytope face \(\{x_u=t\text{ for all }u\in P_n,\ 0\le t\le1\}\) lies in every corresponding face. Conversely, the union of the equality constraints across all quadrangles and boundary blocks identifies every coordinate (for \(n\ge4\)), making this the exact common face. The common set-theoretic toric orbit-closure intersection is therefore its projective toric variety \(\mathbb P^1\).

Vertices of an order polytope are order-preserving \(\{0,1\}\)-assignments. The two constant assignments account for two. With \(x_\bot=0,x_\top=1\), choose the index set \(A\) of \(a\)'s assigned \(1\) and the index set \(B\) of \(b\)'s assigned \(0\). The constraints say either \(A=\varnothing\), \(B=\varnothing\), or \(A=B=\{i\}\). There are \(2^{n+1}+n-1\) such assignments, hence \(2^{n+1}+n+1\) vertices altogether. All assignments except \(A=B=\varnothing\) have an active boundary singular block, or are constant assignments with one, whereas that single remaining assignment has an active forest consisting of two stars plus two exterior edges. Thus exactly one torus-fixed point is smooth.

## Verification

Run \(\texttt{python3 verify_capped_crown.py}\) with Python 3, using only its standard library. The checker constructs all \(\{0,1\}\)-vertices and true facet masks directly from the poset inequalities. It exhausts **all** \(1615\) nonempty faces at \(n=3\) and all \(18447\) at \(n=4\), computing active-normal ranks as exact graph ranks and confirming that the predicted cones are exactly the maximal-dimensional singular orbit closures. It also verifies each predicted minimal cone and the unique smooth fixed point at \(n=5\), without exhausting all faces there. The output ends in \(\texttt{VERIFY_OK}\). These finite tests supplement, but do not replace, the all-parameter proof above.

## Relationship to prior work

Stanley's work supplies the order-polytope facets and face descriptions, and Wagner gives a general forest criterion for projective Hibi toric varieties. Brown--Lakshmibai and Lakshmibai--Mukherjee study singularities and local toric structures of particular and general Hibi varieties; their cited results should not be attributed to this theorem. The new claim is the **specific all-parameter classification** for the bounded-crown family: its three component families, their sharp codimensions and local Segre models, exact component formula, common intersection, and unique smooth fixed-point property. In particular the known pure-codimension-three conclusion for Grassmann--Hibi varieties does not cover this family.

## Limitations

The assertion is about the reduced set-theoretic singular support and generic transverse local structure; it does not calculate scheme-theoretic intersections or nongeneric singularity multiplicities. It is restricted to \(n\ge4\). A full-text comparison with Wagner (1996) remains unresolved because the original article was not accessible; an equivalent worked-out example there or in unindexed sources is a residual originality risk. No independent audit or external certification is claimed.

## References

- R. P. Stanley, *Two poset polytopes*, Discrete Comput. Geom. **1** (1986), 9--23, DOI:10.1007/BF02187680; author manuscript: https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf .
- D. G. Wagner, *Singularities of toric varieties associated with finite distributive lattices*, J. Algebraic Combin. **5** (1996), 149--165, DOI:10.1023/A:1022469218716 (abstract available; original full text not inspected).
- J. A. Brown and V. Lakshmibai, *Singular loci of Grassmann--Hibi toric varieties*, arXiv:math/0612289 (first posted 2006-12-11), especially the introduction and Theorem 6.19.
- V. Lakshmibai and H. Mukherjee, *Singular loci of Hibi toric varieties*, arXiv:0706.2686 (first posted 2007-06-18), especially Theorems 6.7 and 6.9.

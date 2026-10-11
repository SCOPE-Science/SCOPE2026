# Minimum-support codimension-one homology in Kühnel’s \(2d+3\)-vertex sphere-bundle family
## Finding
For every integer \(d\ge 3\), write \(n=2d+3\) and let \(K=K^d_n\) be Kühnel’s cyclic \(n\)-vertex triangulation of the \(S^{d-1}\)-bundle over \(S^1\). Then \(H_{d-1}(K;\mathbf F_2)\cong\mathbf F_2\). The unique nonzero class has minimum vertex support \(d+1\), and exactly \(n\) supports attain that minimum. They are the cyclic blocks
\[
Q_i=\{i,i+1,\ldots,i+d\},\qquad i\in\mathbb Z/n\mathbb Z.
\]
For every \(i\), \(K[Q_i]=\partial\Delta^d\), and its fundamental mod-two cycle is the nonzero class. Equivalently, the \(Q_i\) are exactly the missing \(d\)-simplices of \(K\).

## Assumptions and scope
The cyclic model is the one described by Bagchi and Datta: let \(B\) be the pure \(d+1\)-complex on \(\mathbb Z/n\mathbb Z\) with facets
\[
F_i=\{i,i+1,\ldots,i+d+1\},
\]
with indices modulo \(n\), and put \(K=\partial B\). Their construction identifies \(K\) with Kühnel’s \(K^d_{2d+3}\) and with an \(S^{d-1}\)-bundle over \(S^1\). The assertion is only for \(d\ge3\); the two-dimensional seven-vertex torus behaves differently because its first mod-two homology has rank two.

The vertex support of a simplicial chain is the union of the vertices of simplices carrying nonzero coefficients. All homology in the finding is taken over \(\mathbf F_2\).

## Proof
First, \(Q_i=F_{i-1}\cap F_i\) is an interior \(d\)-face of \(B\). Hence \(Q_i\notin K\), while every proper face of \(Q_i\) lies in \(K\); therefore \(K[Q_i]=\partial\Delta^d\). In the strip model used before the end spheres are identified, one such consecutive \(d+1\)-vertex sphere is a fiber \(S^{d-1}\). Cyclic symmetry carries it to every \(Q_i\). The Wang sequence of the sphere-bundle mapping torus, with mod-two coefficients, gives
\[
H_{d-1}(K;\mathbf F_2)\cong\operatorname{coker}(1-f_*:H_{d-1}(S^{d-1};\mathbf F_2)\to H_{d-1}(S^{d-1};\mathbf F_2))\cong\mathbf F_2,
\]
because every sphere monodromy acts as the identity on top mod-two homology. Thus every \(\partial Q_i\) represents the unique nonzero class.

It remains to prove that there are no other minimum supports. A nonzero simplicial \(d-1\)-cycle needs at least \(d+1\) vertices: fewer than \(d\) vertices support no \(d-1\)-simplex, while on exactly \(d\) vertices there is at most one such simplex and its boundary is nonzero. If a nonzero cycle has support exactly \(d+1\) vertices \(Q\), then once one \(d-1\)-simplex occurs, the cycle condition along each of its ridges forces every \(d\)-element subset of \(Q\) to occur. Hence the cycle is exactly \(\partial Q\), so \(Q\) is a missing \(d\)-simplex of \(K\).

We classify those missing simplices. List the \(d+1\) vertices of \(Q\) cyclically and let \(g_1,\ldots,g_{d+1}\) be the positive cyclic gaps, so
\[
\sum_j g_j=2d+3.
\]
A vertex set is contained in a cyclic interval of \(d+2\) vertices exactly when its largest cyclic gap is at least \(d+2\). Suppose every \(d\)-element subset of \(Q\) is a face of \(K\), but \(Q\) is not contained in any facet \(F_i\) of \(B\). Then every \(g_j\le d+1\). Deleting the vertex between \(g_{j-1}\) and \(g_j\) merges those two gaps. Since the remaining \(d\)-set lies in some \(F_i\), we must have
\[
g_{j-1}+g_j\ge d+2
\]
for every \(j\). Summing gives
\[
2(2d+3)\ge(d+1)(d+2),
\]
which is impossible for \(d\ge3\), since \(d^2-d-4>0\). Therefore \(Q\) is a \(d\)-face of \(B\). Because it is not a face of \(K=\partial B\), it must be an interior \(d\)-face. Two cyclic \(d+2\)-vertex facets of \(B\) share a \(d\)-face only when they are consecutive, so the interior \(d\)-faces are exactly the \(Q_i\). This proves both completeness and the support minimum.

## Verification
The standalone `verify.py` reconstructs the cyclic complexes directly for dimensions \(3\le d\le7\), identifies all missing \(d\)-simplices, computes the relevant mod-two boundary ranks, and checks that every missing-simplex boundary increases the image rank by one. Its finite replay agrees with the theorem in every tested dimension. The all-dimensional conclusion does not rely on this finite experiment; it follows from the gap argument and mapping-torus homology above.

## Relationship to prior work
Kühnel introduced the \(2d+3\)-vertex family. Lutz’s survey records its vertex minimality, topology, and dihedral transitivity. Bagchi and Datta give the cyclic boundary model used here and prove that, for \(d\ge3\), it is the unique non-simply-connected \(d\)-manifold on \(2d+3\) vertices. Later tightness work records that the family is mod-two tight in the non-orientable dimensions and tight in the orientable dimensions. Those results establish the family’s extremal status and explain why induced homology is natural, but the inspected sources do not state the exact list of all missing \(d\)-simplices, the minimum support \(d+1\), or the complete \(2d+3\)-element set of minimizers.

## Limitations
The theorem concerns only codimension-one homology over \(\mathbf F_2\) and only Kühnel’s \(K^d_{2d+3}\) for \(d\ge3\). It does not classify larger supports, integral representatives, or analogous support spectra for the \(2d+4\)-vertex sphere-bundle triangulations. The original 1986 article was identified bibliographically but its full text was not directly inspected; the construction itself was checked in the later full-text sources listed below.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372, submitted 2005-06-18. Theorem 5 records Kühnel’s \(2d+3\)-vertex sphere-bundle family and its vertex minimality.
2. B. Bagchi and B. Datta, *Minimal triangulations of sphere bundles over the circle*, arXiv:math/0610829. The construction gives the cyclic interval model; Section 4 gives uniqueness for \(d\ge3\).
3. B. Bagchi and B. Datta, *On stellated spheres and a tightness criterion for combinatorial manifolds*, arXiv:1207.5599. Example 3.14 records the family’s tightness properties.
4. W. Kühnel, *Higher dimensional analogues of Császár’s torus*, Results in Mathematics 9 (1986), 95–106, DOI 10.1007/BF03322352.

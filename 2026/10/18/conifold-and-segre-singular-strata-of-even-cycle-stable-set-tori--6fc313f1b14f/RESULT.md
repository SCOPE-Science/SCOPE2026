# Conifold and Segre singular strata of even-cycle stable-set toric varieties

## Finding

Let \(k\) be algebraically closed, let \(m\ge4\), put \(n=2m\), and let \(Q_n=\operatorname{STAB}(C_n)\subset\mathbb R^n\) be the lattice polytope of independent sets of the simple cycle on \(n\) vertices. Write \(X_n\) for the normal projective toric \(n\)-fold of the normal fan of \(Q_n\), in its full lattice \(\mathbb Z^n\).

**Theorem.** The reduced singular locus of \(X_n\) has precisely \(n+1\) irreducible components: \(n\) distinct codimension-three orbit closures \(Y_1,\ldots,Y_n\) and one additional invariant projective line \(Z\). Indices are cyclic. The component \(Y_i\) is the orbit closure of the face \(Q_n\cap\{y_i=1\}\), and is isomorphic to the normal-fan toric variety of the stable-set polytope of a path on \(n-3\) vertices. The generic transverse affine germ along \(Y_i\) is the threefold conifold \(\operatorname{Spec}k[a,b,c,d]/(ad-bc)\), of multiplicity two and divisor class group \(\mathbb Z\). The generic transverse affine germ along \(Z\) is the rank-at-most-one determinantal cone of \(m\times m\) matrices, of multiplicity \(\binom{2m-2}{m-1}\) and divisor class group \(\mathbb Z\). Thus the singular locus is not equidimensional: the \(Y_i\) have dimension \(n-3\) while \(Z\) has dimension one.

For a nonempty subset \(S\subseteq\{1,\ldots,n\}\), the reduced intersection \(\bigcap_{i\in S}Y_i\) is nonempty exactly when \(S\) has no cyclically consecutive indices. Whenever nonempty, this intersection is irreducible and isomorphic to a product of normal-fan toric varieties of order polytopes of alternating paths. Hence the intersection nerve of the \(Y_i\) is the independence complex of \(C_n\). The number of nonempty intersections involving exactly \(r\) distinct components of this family is
\[
\frac{n}{n-r}\binom{n-r}{r},\qquad 1\le r\le m.
\]
The line \(Z\) is the orbit closure of the edge joining the two alternating maximum independent sets. It meets each \(Y_i\) in one point. Its intersection with \(\bigcap_{i\in S}Y_i\) is nonempty precisely when all indices in \(S\) have the same parity: the common point is one endpoint of \(Z\) for even \(i\), the other for odd \(i\). Both parity classes have \(m\) members.

There are \(F_{n-1}+F_{n+1}\) torus-fixed points, where \(F_0=0\), \(F_1=1\) are Fibonacci numbers. Exactly **one** is smooth. Every simplicial cone of the normal fan is unimodular, so the non-\(\mathbb Q\)-factorial locus has the same support as the singular locus. These statements hold in arbitrary characteristic.

## Assumptions and scope

Use the ordinary stable-set polytope, not the symmetric-edge polytope, the cut polytope, or the face fan over a reflexive polytope. The graph is the simple cycle \(C_n\), with \(n=2m\ge8\). The claims concern reduced singular support, its orbit-closure intersection geometry, and the transverse germs at generic points of components; no description of the nonreduced singular scheme or arbitrary nongeneric analytic germs is asserted. Earlier small cases \(C_4\) and \(C_6\) are not claimed as new.

Define the *circular fence* order polytope
\[
P_n=\{x\in[0,1]^n:x_i\le x_{i+1}\ (i\text{ odd}),\quad x_{i+1}\le x_i\ (i\text{ even})\},
\]
where subscripts are modulo \(n\). Coordinates with odd index are minimal, those with even index maximal. The integral affine substitution \(y_i=x_i\) for odd \(i\), \(y_i=1-x_i\) for even \(i\), identifies \(P_n\) with \(Q_n\): \(y_i\ge0\), \(y_i+y_{i+1}\le1\) for all cyclic edges, with integrality by bipartiteness of the even cycle. Thus it suffices to analyze the normal fan of \(P_n\).

## Proof

**1. Facets and network matrix.** The irredundant facets of \(P_n\) are \(x_i\ge0\) for odd \(i\), \(x_i\le1\) for even \(i\), and \(x_v\le x_p\) for every cycle edge from an odd vertex \(v\) to an even vertex \(p\). Their primitive outward normals are respectively \(-e_v\), \(e_p\), and \(e_v-e_p\). These are signed vertex-edge incidence columns of the graph obtained by adjoining a root \(0\) to the cycle: a bound-facet column is an edge to \(0\), and a comparison-facet column is a cycle edge. Every submatrix is totally unimodular, since it is a directed incidence matrix with the root row removed.

At a vertex \(x\in\{0,1\}^n\) satisfying the comparisons, the active cycle edges join successive equal bits, and the active root spokes attach each zero-valued odd vertex and each one-valued even vertex to the root. Every maximal run of equal bits on the cycle has at least one root spoke of the indicated type. The active graph is therefore connected. A cone is nonsimplicial exactly when this graph has a cycle; any forest's columns are an integral basis of their saturated span. Consequently, every simplicial cone is smooth and every nonsmooth cone is nonsimplicial.

**2. Exhaustion of minimal nonsmooth cones.** If the binary vertex is not constant, the active cycle edges form disjoint paths. A cycle in its augmented active graph must use two root spokes attached within one equal-bit run. Between two successive spokes of that type lie exactly two comparison edges, giving a four-edge cycle. It comes from the triple \(i-1,i,i+1\) pinned to \(0\) when \(i\) is even, or pinned to \(1\) when \(i\) is odd. Denote this four-ray, three-dimensional cone by \(\tau_i\). If the binary vertex is constant, the active graph can also contain the full \(n\)-edge cycle without the root; denote its \((n-1)\)-dimensional cone by \(\tau_*\). Conversely all these cones occur as normal cones to faces: the triple-pinned faces and the diagonal segment \(D=\{x_1=\cdots=x_n=t:0\le t\le1\}\), respectively. Set all remaining free odd coordinates to \(1/3\) and even coordinates to \(2/3\) to see that no additional facet is forced at the relative interior of a triple-pinned face. The \(n\) cones \(\tau_i\) and \(\tau_*\) are pairwise distinct, and each is minimal nonsmooth, as every proper subgraph of its defining simple cycle is a forest. For an arbitrary (not necessarily vertex) face, use its relative-interior point: active comparison edges connect only equal-valued coordinates, so they form paths, or the whole cycle when all coordinates agree. Active root spokes occur only at value zero on minima or value one on maxima. Any cycle in the active graph is consequently either the entire cycle without the root or a root-to-root circuit through an equal-value path. In the second case two nearest root spokes are separated by exactly two comparison edges, producing one of the four-ray cones above. Hence every nonsmooth cone contains one of the listed cones as a face. Their orbit closures are therefore exactly the irreducible components of the reduced singular locus.

**3. Integral transverse models.** For even \(i\), the four rays of \(\tau_i\), in the three consecutive coordinate positions, are
\[
-e_{i-1},\quad -e_{i+1},\quad e_{i-1}-e_i,\quad e_{i+1}-e_i.
\]
They satisfy the primitive square relation
\[
(-e_{i-1})+(e_{i-1}-e_i)=(-e_{i+1})+(e_{i+1}-e_i).
\]
For odd \(i\) the same integral configuration occurs with bound rays \(e_{i-1},e_{i+1}\) and comparison rays \(e_i-e_{i-1},e_i-e_{i+1}\). In either case every three rays form a basis of their saturated rank-three lattice, identifying the cone with the unimodular square cone. Its dual semigroup algebra is \(k[a,b,c,d]/(ad-bc)\).

The rays of \(\tau_*\) are the \(n\) cyclic incidence columns \(e_v-e_p\). They span the primitive hyperplane lattice \(\{z\in\mathbb Z^n:\sum z_i=0\}\), and their unique relation is the sum of the alternating \(m\) edge columns on one perfect matching equal to the sum on the other matching. Deleting any one edge leaves a spanning tree and hence an integral basis of this lattice. Thus this integral cone is the standard cone with \(2m\) primitive rays satisfying exactly one primitive \(m\)-versus-\(m\) relation, dual to the semigroup generated by the \(m^2\) vectors \(u_a+v_b\). This semigroup is the coordinate semigroup of rank-one \(m\times m\) matrices, whose defining prime ideal is generated by all \(2\times2\) minors. Its projectivized cone is the Segre \(\mathbb P^{m-1}\times\mathbb P^{m-1}\), with degree \(\binom{2m-2}{m-1}\); that is the Hilbert–Samuel multiplicity at the vertex. The local divisor class group for each transverse cone is free of rank one, since its primitive ray matrix has one more column than its rank and torsion-free cokernel.

**4. Components and all intersections.** Let \(F_i\subset P_n\) be the face fixing \(x_{i-1}=x_i=x_{i+1}=0\) for even \(i\), or all three coordinates to \(1\) for odd \(i\). The corresponding orbit closure is \(Y_i=V(\tau_i)\). Removing the three fixed consecutive coordinates leaves a path with \(n-3\) vertices. All inequalities between fixed and free coordinates are automatically satisfied (a fixed zero is a minimal element at a boundary; a fixed one is maximal). Therefore \(F_i\) is integrally equivalent to the order polytope of that alternating path. Similarly, \(Z=V(\tau_*)\) is the toric variety of the diagonal lattice segment \(D\), hence \(\mathbb P^1\).

In the original stable-set coordinates, the face \(F_i\) is simply \(y_i=1\), which forces its two neighbors to zero. For several centers \(S\), the face \(\bigcap_{i\in S}F_i\) is nonempty exactly if no consecutive cyclic centers occur. Consecutive centers impose contradictory zero and one values on overlapping coordinates. Conversely, in the absence of consecutive centers, overlapping pinned triples necessarily have equal values, and every cyclic inequality between distinct pinned blocks is consistent; freely assign \(1/3\) to remaining minima and \(2/3\) to remaining maxima. Equivalently in stable-set coordinates, the intersection face is exactly the stable-set polytope of the induced graph left after deleting the closed neighborhood of \(S\). This induced graph is a disjoint union of paths, so the face is integrally a product of their stable-set polytopes (and equivalently of alternating-path order polytopes). For a polytopal normal fan, the reduced intersection of orbit closures is the orbit closure of the intersection face, proving irreducibility and product geometry. Counting independent \(r\)-subsets of a cycle gives \(\frac n{n-r}\binom{n-r}{r}\).

The diagonal \(D\) maps in stable-set coordinates to the edge between the two alternating maximum independent sets. On \(D\), a triple pinned to zero forces \(t=0\), while a triple pinned to one forces \(t=1\). Thus \(Z\cap Y_i\) is the appropriate endpoint and a joint intersection with \(Z\) exists precisely when all selected centers have the same parity.

**5. Fixed points and singular support.** The vertices of \(Q_n\) are characteristic vectors of independent sets of \(C_n\), counted by the Lucas number \(F_{n-1}+F_{n+1}\). In circular-fence coordinates, a zero-valued peak forces its two neighboring minima to zero, creating \(\tau_i\); a one-valued minimum forces its two neighboring peaks to one, also creating \(\tau_i\). Thus any smooth binary vertex must have every odd coordinate zero and every even coordinate one, which is feasible and has exactly \(n\) active facets forming a unimodular basis. It is the only smooth torus-fixed point. As every simplicial cone is unimodular, singularity and failure of \(\mathbb Q\)-factoriality occur on the same torus orbits, completing the proof.

## Verification

The standalone `VERIFY_CYCLE.py` performs exact integral tests for \(n=4,6,8,10\). It enumerates every binary vertex, constructs every active primitive facet normal, compares smoothness with the local-triple criterion, checks Smith normal forms for integral primitivity, reconstructs all local four-ray circuits and the global cycle circuit, verifies unit saturated minors, and independently tests every subset of component indices against the cyclic independence condition and the two endpoints of the diagonal. Its output terminates with `VERIFY_OK`.

The enumerated pairs (torus-fixed vertices, nonsmooth fixed vertices) are \((7,6)\), \((18,17)\), \((47,46)\), and \((123,122)\) respectively. Finite enumeration does not prove the all-parameter statements; those follow from the preceding network-graph and face arguments.

## Relationship to prior work

Stanley's 1986 order-polytope facets, vertices, and face-partition theorem supply the general background. Lakshmibai and Mukherjee (arXiv:0706.2686) give a general affine Hibi singular-locus criterion, not the explicit all-even-cycle projective normal-fan decomposition, integral generic Segre model, or cyclic intersection nerve stated here. The stable-set toric ring literature studies different algebraic invariants and does not by itself imply these orbit-closure calculations.

The case of the four-cycle coincides with a complete-bipartite stable-set instance; the six-cycle coincides with a six-element crown-poset instance. Both small cases and the corresponding previously known singular profiles are excluded from novelty. Earlier path-graph results do not imply the extra cycle cone \(\tau_*\), which is the key new global obstruction. Results about toric varieties of symmetric-edge or cut polytopes concern different fans.

## Limitations

The theorem identifies reduced support and generic transverse germs, not scheme-theoretic singular ideals, all local germs at component intersections, or global divisor class groups. A general Hibi singular-locus criterion exists and is stronger as an algorithm across posets; the present contribution is the explicit cycle-wide geometric, arithmetic-multiplicity and incidence classification. Different terminology in indexed or unindexed papers may hide an equivalent specialized result; no claim of proof of uniqueness from a failed search is made. The two small even cycles are covered by earlier special cases. No independent validation is represented.

## References

1. R. P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI:10.1007/BF02187680; author-hosted PDF: https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf.
2. V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi Toric Varieties*, arXiv:0706.2686 (initial public arXiv posting 2007-06-18), https://arxiv.org/abs/0706.2686.
3. K. Matsuda, H. Ohsugi and K. Shibata, *Toric Rings and Ideals of Stable Set Polytopes*, arXiv:1603.01850 (initial posting 2016-03-06), https://arxiv.org/abs/1603.01850.

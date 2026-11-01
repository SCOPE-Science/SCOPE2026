# A two-coordinate diagonal-cycle reduction for multinary Hamming Rips fixed filtrations

## Finding

**Theorem.** Fix integers \(q\ge3\) and \(n\ge2\). Put \(Q_{n,q}=(\mathbb Z/q\mathbb Z)^n\) with Hamming distance, and let \(X_{n,q}(r)=\operatorname{VR}_{\le r}(Q_{n,q})\) denote the finite Vietoris--Rips complex at real scale \(r\ge0\), with a simplex for every subset of diameter at most \(r\). Let \(C_q\) act by simultaneously adding \(1\) to the first two coordinates, leaving the other coordinates unchanged. The following assertions hold for the **geometric** fixed-point spaces, not merely the subcomplexes of pointwise-fixed vertices:

1. If \(0\le r<2\), then \(|X_{n,q}(r)|^{C_q}=\varnothing\).
2. For every \(r\ge2\), the fixed polyhedron is canonically PL homeomorphic to the realization of the clique blow-up of \(X_{n-2,q}(r-2)\): every base vertex is replaced by a \(q\)-clique, and every base edge by all \(q^2\) cross-edges. This orbit-barycenter complex **strongly simplicially collapses** to \(X_{n-2,q}(r-2)\).
3. The collapse and its homotopy inverse are compatible with the inclusions as \(r\) increases. Consequently, for every coefficient ring \(R\) and every degree, the fixed-point persistent homology after scale \(2\) is naturally isomorphic to the ordinary Hamming Rips persistent homology in \(n-2\) coordinates with scale shifted by \(2\). The same holds for integral homology and its torsion, without any field assumption.

Here \(Q_{0,q}\) is a singleton, so the boundary case \(n=2\) is included. The restriction \(q\ge3\) is sharp: for \(q=2,n=3,r=2\), the geometric fixed space is a circle instead of the two-component scale-zero Rips complex of \(Q_{1,2}\).

**Consequences.** Write \(m=n-2\). At scale \(r=2\), the fixed space has exactly \(q^m\) contractible components. For \(m\ge1\), at scale \(r=3\) it is homotopy equivalent to a wedge of
\[
\beta(m,q)=1-q^m+m q^{m-1}(q-1)
\]
circles (interpreted as contractible when \(\beta=0\)). For \(m=0\), the fixed space is contractible at every \(r\ge2\). In particular, when \(q=3,n=4\), the fixed filtration is empty below scale \(2\), consists of nine contractible components at scale \(2\), has homotopy type \(\bigvee^4 S^1\) at scale \(3\), and is contractible at scale \(4\). Its complete reduced integral barcode has eight degree-zero intervals \([2,3)\) and four degree-one intervals \([3,4)\), with no other intervals.

## Assumptions and scope

The alphabet is the additive cyclic group of any integer order \(q\ge3\), not necessarily a finite field. The Hamming distance counts unequal coordinates, and the Rips threshold is **inclusive**. The group action is the order-\(q\) diagonal addition on exactly two coordinates. Scales are arbitrary nonnegative real numbers, with changes only at integers. A \(C_q\)-fixed point in the geometric realization can be the barycenter of a moved orbit of vertices; the fixed locus must not be confused with the simplicial complex on fixed vertices (there are none).

## Proof

**Step 1: geometric fixed points as orbit simplices.** The action on vertices is free. For a point of the realization of a simplicial complex, the uniquely determined set of vertices with positive barycentric coefficients is preserved under a simplicial automorphism precisely when its support is permuted and its positive coefficients are constant on vertex orbits. Hence the geometric fixed locus admits a triangulation with one vertex for each group orbit that is itself a simplex. A set of orbit vertices spans a simplex exactly when the union of those orbits is a simplex of the original complex: the embedding sends each orbit vertex to the arithmetic mean of the original vertices of its orbit. Disjoint supports make this embedding injective, and the invariant barycentric-coordinate description makes it surjective.

**Step 2: exact orbit diameter and cross-distance.** Every orbit has a unique label \((a,u)\), with \(a\in\mathbb Z/q\mathbb Z\) and \(u\in Q_{n-2,q}\), and has vertex set
\[
O_{a,u}=\{(t,t+a,u):t\in\mathbb Z/q\mathbb Z\}.
\]
Each orbit has diameter exactly \(2\). For any two labels \((a,u)\) and \((b,v)\), compare \((t,t+a,u)\) and \((s,s+b,v)\). With \(\delta=s-t\) their distance equals
\[
d_H(u,v)+\mathbf1_{\delta\ne0}+\mathbf1_{\delta\ne a-b}.
\]
There are at most two excluded values for \(\delta\); because \(q\ge3\), some \(\delta\) avoids both. Therefore the maximum cross-distance, even for two different orbit labels with identical \(u\), is **exactly**
\[
\max_{x\in O_{a,u},\,y\in O_{b,v}}d_H(x,y)=2+d_H(u,v).
\]
The case of a single orbit uses the same computation with different vertices and gives diameter \(2\). This equality is the nonbinary step where the theorem fails for \(q=2\).

**Step 3: exact blow-up and strong collapse.** For \(r<2\), no orbit is an admissible simplex, so the geometric fixed locus is empty. For \(r\ge2\), all orbit labels are admissible. By Step 2, two distinct orbit vertices \((a,u),(b,v)\) form an edge of the orbit complex if and only if \(d_H(u,v)\le r-2\). Thus each fixed \(u\) gives a complete \(q\)-clique, and cross-fiber edges are present in their entirety precisely when \(\{u,v\}\) is an edge of \(X_{n-2,q}(r-2)\). Because Rips complexes are flag, this determines all faces, proving the exact clique blow-up description.

Fix the representative label \((0,u)\) in every fiber. The closed graph neighborhoods of \((a,u)\) and \((0,u)\) are equal. Consequently, in the flag complex every vertex \((a,u)\), for \(a\ne0\), is dominated by \((0,u)\). Removing these dominated vertices one by one is a strong simplicial collapse onto the full subcomplex on the labels \((0,u)\), which is exactly \(X_{n-2,q}(r-2)\).

Equivalently, the projection \(p_r:(a,u)\mapsto u\) and section \(s_r:u\mapsto(0,u)\) are simplicial maps with \(p_rs_r=\operatorname{id}\), while \(s_rp_r\) is contiguous to the identity: for any face \(F\), the union \(F\cup s_rp_r(F)\) is still a face. All these maps commute strictly with inclusions of scale \(r\) into scale \(r'\ge r\) within \([2,\infty)\). They therefore induce mutually inverse natural isomorphisms of homology persistence modules, over every coefficient ring. This proves the theorem.

**Step 4: low-scale topology and the binary boundary.** At shifted scale zero, \(X_{m,q}(0)\) is a discrete set of \(q^m\) points. At shifted scale one, \(X_{m,q}(1)\) is the clique complex of the Hamming graph, whose maximal cliques are coordinate lines of \(q\) vertices. Distinct coordinate lines share at most one vertex. Collapsing each coordinate-line simplex to a chosen spanning tree gives a connected graph on \(q^m\) vertices with \(m q^{m-1}(q-1)\) edges; hence its first Betti number is \(1-q^m+m q^{m-1}(q-1)\), and no higher homology remains. For \(m=0\), the Rips complex is a point.

For \(q=2,n=3,r=2\), four orbit labels arise. The two missing edges are a perfect matching on these labels, so the orbit complex is the unfilled four-cycle \(S^1\). The would-be shifted base \(X_{1,2}(0)\) consists of two isolated points and cannot be homotopy equivalent to that circle. This proves sharpness of the alphabet restriction.

## Verification

The accompanying standalone `checker.py` reconstructs each orbit by explicit coordinates, computes exact maximum Hamming distances, and independently compares all orbit-graph edges to the reduced-parameter criterion for ten parameter pairs with \(q\in\{3,4,5\}\). It also enumerates all simplices and mod-two boundary ranks of the geometric fixed orbit complex for \(q=3,n=4\) at scales \(2\) and \(3\), giving reduced Betti vectors \((8,0,\ldots)\) and \((0,4,0,\ldots)\), respectively, and explicitly verifies the four-cycle boundary at \(q=2,n=3,r=2\). The checker uses no third-party packages. These are finite corroborations; the unrestricted statements follow from Steps 1--4 rather than extrapolation.

To reproduce the computation, run `python3 checker.py` from the directory containing the extracted file. Its final lines are `ALL_HOMOLOGY_CHECKS_PASSED` and `BINARY_BOUNDARY_OK q=2 n=3 r=2 fixed_orbit_graph=C4`.

## Relationship to prior work

Recent work on Vietoris--Rips complexes of Hamming hypercubes studies connectivity, cohomology and rational symmetry representations [1,2]; the original scale-two hypercube homotopy classification is in [3]. Those papers concern the binary alphabet and do not state the present nonbinary geometric fixed-locus reduction. The present result does not recompute the ordinary Rips homology of arbitrary multinary cubes: it identifies an entire symmetry-fixed filtration with a dimension-reduced ordinary Rips filtration, by a natural and compatible strong collapse. General facts about barycentric descriptions of geometric fixed points and dominated-vertex collapses are used as standard ingredients, not claimed as discoveries.

## Limitations

The exact reduction requires an alphabet with at least three symbols and an order-\(q\) diagonal cycle acting simultaneously on two coordinates. It does not classify other group actions, non-Hamming metrics, or the unreduced ambient Rips homotopy type for arbitrary scales. Homotopy equivalence is asserted for the fixed space, while the orbit-complex model itself is PL homeomorphic to it. The homology calculations in `checker.py` are mod two and finite; the integral persistence assertion rests on the coefficient-independent proof. Independent validation and exhaustive exclusion of equivalent literature remain outstanding.

## References

[1] M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris--Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (initial public posting 2026-05-01), https://arxiv.org/abs/2605.00705 ; later open-access journal version, DOI:10.1017/prm.2026.10175.

[2] F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (initial public posting 2026-06-18), https://arxiv.org/abs/2606.20784 .

[3] M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040 (initial public posting 2021-03-01), https://arxiv.org/abs/2103.01040 .

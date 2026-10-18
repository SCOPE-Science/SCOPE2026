# Singular rational curves and Segre transversals in cycle cut toric varieties

## Finding
Let \(k\) be an algebraically closed field of arbitrary characteristic, and let \(n\geq4\). Write
\[
L_n=\{z\in\mathbb Z^n:\textstyle\sum_{i=1}^n z_i\equiv0\pmod2\},\qquad
P_n=\operatorname{conv}\{x\in\{0,1\}^n:\textstyle\sum_i x_i\equiv0\pmod2\}.
\]
The lattice polytope \(P_n\) is the cut polytope of the cycle graph \(C_n\), with cut-edge coordinates. Let \(X_n\) denote the normal projective toric variety defined by the normal fan of \(P_n\) in the dual lattice \(L_n^*\).

**Theorem.** The reduced singular locus of \(X_n\) is precisely the union of the torus-invariant curves corresponding to *all* edges of \(P_n\). Each curve is isomorphic to \(\mathbb P_k^1\), and these curves are exactly the irreducible components. Their number is
\[
\#\operatorname{Irr}(\operatorname{Sing}(X_n)_{\mathrm{red}})
=2^{n-2}\binom n2.
\]
The components intersect only at torus-fixed points. There are \(2^{n-1}\) fixed points, and exactly \(\binom n2\) distinct singular components pass through each one.

At the generic point of *every* singular curve, the transverse toric singularity is the affine cone of rank-at-most-one \(2\times(n-2)\) matrices. More precisely, if \(\sigma_E\) is the normal cone to an edge \(E\), then
\[
U_{\sigma_E}\cong\mathbb G_m\times
\operatorname{Spec}\frac{k[z_{1j},z_{2j}:1\le j\le n-2]}
{(z_{1j}z_{2\ell}-z_{1\ell}z_{2j}:j<\ell)}.
\]
Thus the generic transverse Hilbert--Samuel multiplicity is exactly \(n-2\). The reduced singular locus equals the non-\(\mathbb Q\)-factorial locus. For \(n=4\) the transverse singularities are ordinary threefold conifolds, while for \(n\ge5\) these edge charts are not \(\mathbb Q\)-Gorenstein. The global variety is Gorenstein for \(n=4\) and not \(\mathbb Q\)-Gorenstein for \(n\ge5\); the global Gorenstein cutoff itself is consistent with and already implied by Ohsugi's published classification, and is **not** asserted as an independent novelty claim.

## Assumptions and scope
The field is algebraically closed, of any characteristic, and \(n\) is an integer at least four. \(X_n\) means the *normal* toric variety of the normal fan, not a possibly nonnormal monomial model. The character lattice is the even-sum lattice \(L_n\), not the larger ambient \(\mathbb Z^n\); this distinction is essential for primitive facet normals and for the Segre local rings. In fact, the cycle cut model is normal by known cut-polytope results, but normality is built into the fan definition here. Statements about singular loci refer to reduced support unless specifically described by the affine coordinate ring. A generic transverse ring is the factor remaining after removing the smooth \(\mathbb G_m\) orbit direction, not a claim that the whole singular curve has a product neighborhood globally.

## Proof
**1. Cut vertices, facet normals, and lattice.** Every cut of a cycle crosses an even number of edges. Conversely, prescribing any even edge subset determines a vertex bipartition up to complement. Hence the cut polytope in edge coordinates is exactly \(P_n\), and its difference lattice is \(L_n\). The Barahona--Mahjoub cycle facet description (as quoted in Ohsugi's Proposition 2.1, or Proposition 1.4 in his later paper) consists, for \(n\ge4\), of the coordinate inequalities \(0\le x_i\le1\) and the odd-set inequalities
\[
\sum_{i\in S}x_i-\sum_{i\notin S}x_i\le|S|-1
\qquad(S\subseteq\{1,\ldots,n\},\ |S|\text{ odd}).
\]
At the vertex \(0\), the only tight facets are the \(n\) coordinate facets \(x_i=0\) and the \(n\) singleton odd-set facets \(x_i-\sum_{j\ne i}x_j=0\). Put \(h=\tfrac12\sum_i e_i\). In \(N_n=L_n^*=\mathbb Z^n+\mathbb Zh\), their *primitive* inward/outward normals up to consistent sign are
\[
u_i=-e_i,\qquad v_i=e_i-h\qquad(1\le i\le n).
\]
These are primitive because \(N_n\) admits the basis consisting of \(h\) and any \(n-1\) standard basis vectors. For every even subset \(T\), flipping the coordinates \(x_i\mapsto1-x_i\) for \(i\in T\) preserves \(P_n\) and its lattice, and sends \(0\) to the vertex indexed by \(T\). Thus all vertices, their incident face systems and their normal cones are lattice-equivalent.

**2. Exhaustive classification of faces through a vertex.** Every face containing \(0\) is the intersection of some of those \(2n\) incident facets. Let \(A\) be the indices of the coordinate facets selected, and \(B\) those of the singleton odd-set facets selected. At an even-support vertex \(1_T\), the singleton condition for index \(i\) holds exactly when \(T=\varnothing\), or \(T=\{i,j\}\) for some \(j\ne i\).

If \(B=\varnothing\), the face consists of even-support vertices supported in the \(m=n-|A|\) remaining coordinates. It has dimension \(m\) when \(m\ge3\), is an edge when \(m=2\), and is a vertex otherwise. For \(m\ge3\), its normal cone has exactly the rays \(u_a\) for \(a\in A\).

If \(B=\{b\}\) with \(b\notin A\), the face is the simplex with vertices \(0\) and \(e_b+e_j\) for \(j\notin A\cup\{b\}\). When \(m\ge3\) it has dimension \(m-1\) and its normal cone has rays \(\{u_a:a\in A\}\cup\{v_b\}\). For \(m=2\) it is an edge; if \(b\in A\), it is just \(0\). If \(|B|\ge2\), the only possibility other than \(0\) is the edge \([0,e_i+e_j]\), occurring when \(B=\{i,j\}\) and \(A\cap\{i,j\}=\varnothing\). This enumerates *every* face containing \(0\) and hence, by coordinate-flip symmetry, all faces.

Each normal cone of a face of dimension at least two is regular. Indeed, in the first case \(\{u_a:a\in A\}\) extends to a lattice basis of \(N_n\): choose an index \(t\notin A\) and complete with \(h\) and \(e_j\) for \(j\notin A, j\ne t\). In the second case choose \(t\notin A\cup\{b\}\) and complete \(\{u_a\}\cup\{v_b\}\) with \(e_j\) for \(j\notin A,j\ne t\); since \(h=e_b-v_b\), this too is a basis. These argument also establish full integral saturation, not just real linear independence.

**3. Edge cones and smoothness stratification.** An edge through \(0\) joins \(0\) to \(e_i+e_j\) for a unique unordered pair \(i\ne j\). Its normal cone has precisely the \(n\) rays
\[
\sigma_{ij}=\operatorname{cone}\bigl(v_i,v_j,u_k\ (k\ne i,j)\bigr).
\]
It has dimension \(n-1\) and satisfies the unique ray relation
\[
v_i+v_j=\sum_{k\ne i,j}u_k.
\]
Since \(n\ge4\), the cone is nonsimplicial and therefore singular, as is every vertex cone (with \(2n\) rays in dimension \(n\)). By Step 2 all normal cones corresponding to faces of dimension at least two are regular. The toric orbit--cone smoothness criterion therefore proves that the singular support is exactly the union of one-dimensional torus-orbit closures, i.e. those belonging to the edges. Each closure is the complete normal toric curve \(\mathbb P^1\), and no one of these curves contains another. Distinct one-dimensional orbit closures can meet only in fixed points, with intersection precisely when their polytope edges have a common endpoint. At any vertex there are \(\binom n2\) adjacent edges. Since \(P_n\) has \(2^{n-1}\) vertices, its edges number \(2^{n-2}\binom n2\). This proves the singular-component count and incidence statements.

**4. Exact transverse coordinate ring.** Put \(M_n=L_n\) and fix \(\sigma_{ij}\). For \(z\in M_n\), write \(s=\tfrac12\sum_kz_k\in\mathbb Z\) and
\[
a=z_i-s,\quad b=z_j-s,\quad c_k=-z_k\ (k\ne i,j).
\]
The inequalities defining \(\sigma_{ij}^{\vee}\) are precisely \(a,b,c_k\ge0\), and the identity \(a+b=\sum_{k\ne i,j}c_k\) follows by summation. Conversely, any nonnegative integral tuple with this identity and any \(s\in\mathbb Z\) yields \(z_i=s+a\), \(z_j=s+b\), \(z_k=-c_k\), an element of \(M_n\). Thus the dual affine semigroup is the direct sum of a free \(\mathbb Z\) factor with the nonnegative row/column-degree semigroup of a \(2\times(n-2)\) matrix. That semigroup is generated by elementary entries \(z_{1k},z_{2k}\), with all relations generated by \(2\times2\) minor swaps: any two matrices of nonnegative integral multiplicities with the same row and column sums are connected by such swaps. This proves the displayed isomorphism of affine charts, integrally and in any characteristic.

The rank-one determinantal cone is smooth away from its vertex and has dimension \(n-1\). Its projectivization is \(\mathbb P^1\times\mathbb P^{n-3}\) in the Segre embedding, of degree \(n-2\); that degree equals the Hilbert--Samuel multiplicity at the cone vertex. Since \(\sigma_{ij}\) is nonsimplicial, its chart is not \(\mathbb Q\)-factorial. All remaining cones are regular, proving the equality of singular and non-\(\mathbb Q\)-factorial supports. The relation among its primitive rays would give \(2=n-2\) if their heights against a rational canonical support functional were all \(1\); hence for \(n\ge5\) the chart is not \(\mathbb Q\)-Gorenstein. For \(n=4\), at a vertex the lattice element \((-1,-1,-1,-1)\in M_4\) pairs to \(1\) with every \(u_i,v_i\), and vertex symmetry shows the whole fan is Gorenstein.

## Verification
Run the accompanying self-contained Python 3 script `parity_cut_toric_verify.py` with `python3 parity_cut_toric_verify.py`. It enumerates every face through \(0\) by exact intersections of incident facet-vertex sets for \(4\le n\le7\), computes rational ranks and integral maximal minors in the correct dual lattice, and verifies that all faces of dimension at least two have saturated simplicial normal cones, whereas all edges have nonsimplicial cones. It also checks the primitive edge ray relation and the predicted Hilbert functions of the Segre semigroup. It reports `VERIFY_OK`; its exact output and limitations are recorded in `VERIFICATION.md`. This finite computation is **not** used to extend the proof to all \(n\); the quantifiers in the theorem follow from the symbolic Steps 1--4.

## Relationship to prior work
Sturmfels and Sullivant (2006, Section 1 Example 1.2 and Corollary 2.4) identify the four-cycle cut variety as a complete intersection of three quadrics, identify its crosspolytope, and prove that a cut variety is smooth exactly when the graph has no \(C_4\) minor. These statements establish nonsmoothness for cycle lengths at least four, but not the complete singular locus, component counts, incidence, or transverse Segre matrices. Ohsugi (2009, Proposition 2.1) quotes the Barahona--Mahjoub facet inequalities on which the present geometric computation starts, and his work establishes normality in large cut-graph classes. Ohsugi (2013, Theorem 3.4) independently establishes the general cut-polytope Gorenstein criterion, which already implies the \(n=4\) cutoff; that cutoff is background consistency, not the claim of novelty. The present contribution is the all-length singular-curve and local-ring classification.

Brennan and Chen's 2009 paper on toric geometry of series-parallel graphs concerns the same cut-variety framework and is a plausible overlapping source. Its accessible abstract describes generators of cut ideals, not complete singular supports, but its full text was not accessible for examination in this review; the possibility that it contains an equivalent statement is specifically left open. Also distinguished from the cut polytope is the *graphical zonotope* of the same cycle, whose fan and toric singularities concern a different lattice polytope.

## Limitations
The singular set is classified as a reduced subset. No assertion is made about the full Jacobian singular scheme at torus-fixed intersections, its embedded components, or the scheme-theoretic intersections of the curves. The displayed Segre charts are genuine affine charts associated with edge cones, but the normal-crossing pattern at points where many curves meet is not claimed to be a product of edge charts. The argument concerns the normal cut toric variety for a single cycle, not arbitrary graphs, and claims no singularity classification for graphs outside that family. The analysis is complete for all \(n\ge4\), but priority against all unpublished or inaccessible documents is not certified and independent human review remains outstanding.

## References
1. B. Sturmfels and S. Sullivant, *Toric geometry of cuts and splits* (first public arXiv version 2006-06-27), arXiv:math/0606683, especially Example 1.2 and Corollary 2.4. https://arxiv.org/abs/math/0606683
2. H. Ohsugi, *Normality of cut polytopes of graphs is a minor closed property* (2009), arXiv:0906.5303, especially Proposition 2.1. https://arxiv.org/abs/0906.5303
3. H. Ohsugi, *Gorenstein cut polytopes* (2013), arXiv:1302.2899, especially Proposition 1.4 and Theorem 3.4. https://arxiv.org/abs/1302.2899
4. J. Brennan and G. Chen, *Toric Geometry of Series-Parallel Graphs*, SIAM J. Discrete Math. 23 (2009), 754--764, DOI:10.1137/070703247. Full text not inspected here.

# Non-pure singular strata and intersection degrees for even-cycle stable-set toric varieties

## Finding
For every even integer \(n=2m\ge6\), let \(P_n\subset\mathbb R^n\) be the stable-set polytope of the cycle \(C_n\), with coordinates indexed cyclically by \(\mathbb Z/n\mathbb Z\), and let \(X_n\) be its normal complex projective toric variety in the complete lattice-point embedding. For each vertex \(i\), let \(Y_i\subset X_n\) be the orbit closure corresponding to \(F_i=P_n\cap\{x_i=1\}\). Let \(L\) correspond to \(F_{\mathrm{alt}}=P_n\cap\bigcap_i\{x_i+x_{i+1}=1\}\).

**Theorem.** The reduced singular locus has the following complete, non-equidimensional decomposition:
\[
\operatorname{Sing}(X_n)_{\mathrm{red}}=L\cup\bigcup_{i\in\mathbb Z/n\mathbb Z}Y_i.
\]
The \(n+1\) displayed members are distinct irreducible components. Each \(Y_i\) has codimension \(3\), dimension \(n-3\), and projective degree \(E_{n-3}\), where \(E_d\) is the number of alternating permutations of \(d\) letters (\(E_0=1\)). The remaining component \(L\cong\mathbb P^1\) has codimension \(n-1\) and degree \(1\). In particular, the top-dimensional reduced singular cycle has degree \(nE_{n-3}\).

The transverse affine toric germ at the generic point of any \(Y_i\) is the ordinary threefold node \(uv-wz=0\). At the generic point of \(L\), the transverse germ is the affine variety of complex \(m\times m\) matrices of rank at most \(1\), with Hilbert--Samuel multiplicity \(\binom{2m-2}{m-1}\). The component \(L\) meets every \(Y_i\) in exactly one of its two torus-fixed endpoints; exactly \(m\) of the \(Y_i\)'s pass through each endpoint.

All intersections of the codimension-three components admit a uniform description. For each **nonempty** subset \(S\) of vertices, \(Y_S=\bigcap_{i\in S}Y_i\) is nonempty exactly when \(S\) is an independent set of \(C_n\). In that case, let the graph induced by the vertices outside the closed neighborhood \(N[S]\) be the disjoint union of paths with \(d_1,\ldots,d_r\) vertices; empty union is allowed and has \(r=0\). Set \(d=\sum_j d_j\). Then \(Y_S\) is a projective toric variety of dimension \(d\), canonically polarized by the product polytope of the path stable-set polytopes, and
\[
\deg Y_S=\binom{d}{d_1,\ldots,d_r}\prod_{j=1}^r E_{d_j}.
\]
An empty product and the empty multinomial coefficient equal \(1\). Moreover \(L\cap Y_S\ne\varnothing\) if and only if all vertices of \(S\) have the same parity; then the intersection is the corresponding single endpoint of \(L\).

For example, the top singular degree is \(12\), \(128\), and \(2720\) for \(n=6\), \(8\), and \(10\), respectively; the transverse multiplicities along \(L\) are \(6\), \(20\), and \(70\).

## Assumptions and scope
All varieties are over \(\mathbb C\). The cycle graph is simple, undirected, and of even order at least \(6\). A stable set contains no adjacent vertices. The polytope is
\[
P_n=\operatorname{conv}\{\boldsymbol1_S:S\subset\mathbb Z/n\mathbb Z\text{ independent}\}
=\{x\in\mathbb R^n:x_i\ge0,\ x_i+x_{i+1}\le1\text{ for all }i\}.
\]
The equality is the standard bipartite stable-set-polytope description, and each displayed inequality is a facet. The complete embedding uses all lattice points of \(P_n\), which are precisely its stable-set incidence vectors. The normal fan is taken with outward-pointing primitive facet normals. Singular components and intersections are considered with reduced structures unless specifically stated otherwise. Local analytic type refers to a normal transverse toric slice along the indicated dense orbit, not to arbitrary nongeneric intersection points.

## Proof
**1. Normal rays and integral regularity.** Write \(r_i=-e_i\) for \(x_i\ge0\) and \(s_i=e_i+e_{i+1}\) for \(x_i+x_{i+1}\le1\). These are the primitive outward normals to the \(2n\) facets. Negating coordinates on one color class of the even cycle turns every \(s_i\) into a signed incidence vector of a directed rim edge, and each \(r_i\) into a signed incidence vector of an edge from \(i\) to an added apex. Thus the complete ray matrix is a signed, row-deleted oriented graph-incidence matrix; in particular it is totally unimodular. Every linearly independent collection of these rays extends to a primitive direct summand of the ambient lattice. Therefore a normal cone of \(P_n\) is smooth if and only if its active facet normals are linearly independent. This is also why none of the local cones below conceals a lattice quotient.

**2. Exhaustion of minimal dependent active sets.** Any circuit among the ray columns of the same incidence matrix is supported on a simple graph cycle: either the entire rim cycle, or the added apex together with a rim path whose endpoints carry \(r\)-rays. Suppose the latter is active at a face \(F\). Then the facet equations along that path are \(x_j+x_{j+1}=1\), and its two endpoint equations are \(x_p=x_q=0\). Alternation forces the path length to be even; a path of length \(2\) or more has its first internal coordinate \(1\), and its two neighbors \(0\). Consequently \(F\subset F_{p+1}\), and its normal cone contains
\[
\sigma_{p+1}=\operatorname{cone}(r_p,s_p,s_{p+1},r_{p+2}).
\]
The four rays have rank \(3\) and relation \(r_p+s_p=r_{p+2}+s_{p+1}\). Conversely they are exactly the active facet normals on the relative interior of \(F_{p+1}\); this face fixes \(x_{p+1}=1\) and its neighbors at zero and permits all remaining independent-set coordinates of a path on \(n-3\) vertices.

If instead the entire rim is active, its equations yield \(x_i=t\) on one color class and \(x_i=1-t\) on the other with \(0\le t\le1\). Thus \(F_{\mathrm{alt}}\) is precisely the segment joining the two alternating maximal stable sets, with normal cone
\[
\sigma_{\mathrm{alt}}=\operatorname{cone}(s_0,s_1,\ldots,s_{n-1}).
\]
It has rank \(n-1\) and sole primitive ray relation \(\sum_{i\text{ even}}s_i=\sum_{i\text{ odd}}s_i\). These cones are non-simplicial and neither contains the other as a face: the former has negative-coordinate rays and the latter has none. There are no other minimal non-simplicial feasible normal cones. The orbit--face correspondence therefore gives exactly the stated \(n+1\) irreducible components of the reduced singular locus. For \(n\ge6\), the one-dimensional \(L\) has strictly smaller dimension than any \(Y_i\).

**3. Transverse analytic models.** At the dense orbit of \(Y_i\), the normal cone \(\sigma_i\) has four primitive rays and one relation with all coefficients \(1\) on either side. The lattice-saturation argument in step 1 identifies its affine toric transverse slice with the cone over \(\mathbb P^1\times\mathbb P^1\), equivalently \(uv-wz=0\). At the dense orbit of \(L\), the \(2m\) saturated rays of \(\sigma_{\mathrm{alt}}\) satisfy one relation that sets the sums of the \(m\) even and \(m\) odd rays equal. This is the standard cone for the Segre embedding of \(\mathbb P^{m-1}\times\mathbb P^{m-1}\). Its coordinate ring is \(\mathbb C[z_{ab}:1\le a,b\le m]/I_2(z)\), where \(I_2(z)\) is the ideal of all \(2\times2\) minors. The vertex multiplicity is the degree of this Segre variety, \(\binom{2m-2}{m-1}\). The generic transverse germ along \(L\) is singular because \(m\ge3\).

**4. Incidence and degrees.** A torus-orbit closure for a polytope face \(F\) is the toric variety of \(F\) under the restricted polarization. Its intersections with other such orbit closures correspond to intersections of faces. The face \(F_i\) fixes \(x_i=1\) and \(x_{i-1}=x_{i+1}=0\), leaving precisely a path on \(n-3\) vertices. More generally, \(\bigcap_{i\in S}F_i\) is empty if \(S\) contains adjacent vertices; otherwise it is the stable-set polytope of the induced graph on vertices outside \(N[S]\), with forced coordinates fixed. Since \(S\ne\varnothing\), that graph is a disjoint union of paths. Products of these path polytopes give the stated product toric geometry and dimension.

For a path with \(d\) vertices, complementing the coordinates in one bipartition takes its stable-set polytope to the order polytope of the alternating fence poset. The change is integral affine unimodular. Stanley's linear-extension volume theorem gives its normalized volume as the Euler zigzag number \(E_d\). Since normalized volume of a Cartesian product of lattice polytopes in dimensions \(d_1,\ldots,d_r\) is \(\binom{d}{d_1,\ldots,d_r}\) times the product of their normalized volumes, this proves the intersection-degree formula. For \(S=\{i\}\), the graph is the single path on \(n-3\) vertices, giving \(\deg Y_i=E_{n-3}\); summing the degrees of the \(n\) top-dimensional components gives \(nE_{n-3}\). Finally each coordinate of the alternating edge runs from zero to one, so its intersection with \(x_i=1\) consists of the unique corresponding endpoint. Simultaneous such requirements are compatible exactly when all selected indices have the same parity.

## Verification
A standalone exact-arithmetic checker `verify_crown.py` enumerates all \(18\) binary stable-set vertices and \(403\) nonempty faces for \(n=6\), and all \(47\) vertices and \(3075\) nonempty faces for \(n=8\). It determines active facet columns and exact rational ranks, recovering respectively \(7\) and \(9\) maximal singular faces, including the exceptional alternating face. It also exhausts all subsets of cycle vertices to test the component intersection poset and alternating-edge incidences. Independently, it counts lattice points in dilates of path stable-set polytopes and takes exact finite differences to obtain normalized volumes \(E_1=1\), \(E_3=2\), \(E_5=16\), \(E_7=272\), cross-checking with direct alternating-permutation enumeration. The checker prints `CHECKER_OK (finite instances only)` when these finite tests pass. Reproduce with `python3 verify_crown.py` using Python 3.10+ and SymPy. These checks are not an exhaustive proof in unbounded \(n\); the argument in the previous section handles all \(n=2m\ge6\).

## Relationship to prior work
Wagner's 1996 general Hibi-variety singular-orbit criterion, also recalled as Theorem 2.20 in Miura's arXiv:1301.7632, already determines singular components abstractly from minimal convex cycles. The number of components in a particular poset is therefore **not** claimed as a new general criterion. Lakshmibai--Mukherjee (arXiv:0706.2686, Theorem 6.9) give a different general affine Hibi singular-locus construction via cotangent spaces. Stanley (1986, Corollary 4.2 and Example 4.3) already proved the order-polytope linear-extension volume formula and the identification of fence extensions with alternating permutations. Miura also computes singular-component degrees for a distinct minuscule-poset example (Section 4). Matsuda--Ohsugi--Shibata (arXiv:1603.01850) study stable-set-polytope toric ideals and normality.

The present claim concerns their **simultaneous explicit specialization to every even cycle**, including the non-pure residual singular line, both generic transverse determinantal models with multiplicities, all component intersections, and a closed formula for the degrees of every nonempty intersection. The formulas require identification of the complete feasible circuit structure and its face lattice, not merely the general existence of a singular-locus algorithm. A decisive textual exclusion of an equivalent calculation in every earlier work is not asserted.

## Limitations
Only reduced singular loci, incidence strata, their projective degrees, and the stated generic transverse germs are classified. The scheme-theoretic singular locus, embedded associated primes, and analytic singularities at the nongeneric intersection points are not determined. The full 1996 Wagner article was not materially available for line-by-line inspection, despite searches for an authorized open version; its abstract already covers the general singular-orbit criterion and local-ring methodology, creating a specific residual originality risk. An equivalent specialized computation may appear under crown-poset, Hibi, or perfect-graph terminology. The finite checker tests \(n=6,8\) directly and does not certify the all-parameter assertions. No independent review or certification is claimed.

## References
1. D. G. Wagner, *Singularities of Toric Varieties Associated with Finite Distributive Lattices*, J. Algebraic Combinatorics 5 (1996), 149--165, DOI: 10.1023/A:1022469218716.
2. V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi Toric Varieties*, arXiv:0706.2686 (first posted 18 June 2007), especially Theorem 6.9, https://arxiv.org/abs/0706.2686.
3. M. Miura, *Minuscule Schubert Varieties and Mirror Symmetry*, arXiv:1301.7632, Theorem 2.20 and Section 4, https://arxiv.org/abs/1301.7632.
4. R. P. Stanley, *Two Poset Polytopes*, Discrete Comput. Geom. 1 (1986), 9--23, Corollary 4.2 and Example 4.3, https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf.
5. K. Matsuda, H. Ohsugi, and K. Shibata, *Toric Rings and Ideals of Stable Set Polytopes*, arXiv:1603.01850 (first posted 6 March 2016), https://arxiv.org/abs/1603.01850.

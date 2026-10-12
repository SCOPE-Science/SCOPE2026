# Padovan local class groups and exceptional Gorenstein charts for wheel edge-toric varieties

## Finding
Let \(n\ge4\), let \(W_n\) be the wheel with hub \(h\) and rim the cycle \(C_n\), and let \(X_n\subset\mathbb P^{2n-1}_{\mathbb C}\) be the projective toric variety parametrized by its \(2n\) edge monomials. Write \(p_i^{\mathrm{sp}}\) and \(p_i^{\mathrm{rim}}\) for the torus-fixed points indexed by the spoke \(\{h,i\}\) and rim edge \(\{i,i+1\}\), respectively (indices modulo \(n\)). Let \(a_0=1\), \(a_1=0\), \(a_2=a_3=1\), and \(a_n=a_{n-2}+a_{n-3}\) for \(n\ge4\).

For every \(n\ge4\) and every rim index \(i\), these local rings are normal, with **torsion-free** local Weil-divisor class groups
\[
\operatorname{Cl}(\mathcal O_{X_n,p_i^{\mathrm{sp}}})\cong\mathbb Z^{a_n},\qquad
\operatorname{Cl}(\mathcal O_{X_n,p_i^{\mathrm{rim}}})\cong\mathbb Z^{2a_n-2+\mathbf1_{\{n\text{ odd}\}}}.
\]
The canonical divisor is \(\mathbb Q\)-Cartier at \(p_i^{\mathrm{sp}}\) exactly for \(n=4\), and at \(p_i^{\mathrm{rim}}\) exactly for \(n\in\{4,5,7\}\). In **every** such case it is already Cartier: these are precisely the Gorenstein fixed-point charts. Among these fixed points, only the four rim points at \(n=4\) are smooth. Thus the exceptional \(n=7\) rim charts are Gorenstein but singular; all spoke charts with \(n\ge5\), and all rim charts with \(n\notin\{4,5,7\}\), are not \(\mathbb Q\)-Gorenstein.

## Assumptions and scope
Work over \(\mathbb C\) with the normal projective toric variety given by the edge subalgebra of the wheel graph. Identify the edge polytope, after eliminating the hub coordinate from the equation that all graph-edge vectors have coordinate sum two, with
\[
P_n=\operatorname{conv}\{e_i,\ e_i+e_{i+1}:i\in\mathbb Z/n\mathbb Z\}\subset\mathbb R^n,
\]
where \(e_i\) are the standard coordinate vectors. Its ambient affine lattice is \(\mathbb Z^n\): the difference \((e_i+e_{i+1})-e_i=e_{i+1}\) realizes every lattice direction. All displayed \(2n\) vectors are distinct vertices, hence define the asserted torus-fixed points. The toric variety has dimension \(n\). We assert results only for its torus-fixed points, **not** the full non-\(\mathbb Q\)-Gorenstein or singular loci.

## Proof
**1. Normality and facet enumeration.** Every minimal odd cycle of \(W_n\) is either a hub-containing triangle or, for odd \(n\), the entire rim cycle. Hub triangles share their hub, and the rim cycle intersects every hub triangle. Thus \(W_n\) satisfies the Ohsugi--Hibi odd-cycle condition, which ensures normality of the edge semigroup. Ohsugi--Hibi's facet theorem for a connected nonbipartite graph says that the facets are its regular-vertex coordinate facets and the facets attached to fundamental independent sets. For \(W_n\), every rim vertex is regular, while the hub is regular exactly when \(n\) is odd. The hub singleton is fundamental. Any other independent set is a nonempty rim independent set \(S\): its bipartite neighborhood subgraph is connected via the hub, and after removing \(S\), its neighbors and the hub, the leftover rim induced subgraph is a disjoint union of paths. Such a remainder contains no odd cycle, so \(S\) is fundamental exactly when \(S\) dominates the rim, i.e. is inclusion-maximal independent in \(C_n\). (If the remainder is empty, the condition holds.) The complete, irredundant system of supporting facet inequalities in \(\mathbb R^n\) is therefore
\[
x_j\ge0\ (0\le j<n),\qquad 1\le\sum_jx_j,
\qquad\sum_jx_j\le2\ (n\text{ odd only}),\qquad
\sum_{j\in S}x_j\le1\ (S\in\mathcal M_n),
\]
where \(\mathcal M_n\) denotes the collection of maximal independent sets of \(C_n\). Every displayed facet normal is primitive in \(\mathbb Z^n\).

**2. Composition enumeration.** A nonempty independent set \(S\) of the rim cycle is maximal exactly when every clockwise gap between consecutive elements of \(S\) is either two or three edges: gap one violates independence, while gap four or more leaves an undominated vertex. Fixing \(0\in S\), clockwise gaps give a bijection with **ordered compositions of \(n\) into parts two and three**, whose count is \(a_n\). The empty composition counts \(a_0=1\), and the recurrence follows by separating the first part. Consequently precisely \(a_n\) members of \(\mathcal M_n\) contain vertex zero. By rotation, the same holds for vertex one; by independence none contains both. Hence exactly \(2a_n\) maximal independent sets contain exactly one endpoint of rim edge \(\{0,1\}\).

**3. Spoke chart class group and canonical class.** At the vertex \(e_0\) the active facets are the \(n-1\) coordinate inequalities \(x_j\ge0\) for \(j\ne0\), the lower-sum facet, and the \(a_n\) independent-set facets with \(0\in S\). Thus its normal cone has \(n+a_n\) primitive rays. In the lattice \(N\cong\mathbb Z^n\), choose outward normals \(-e_j\) for \(j\ne0\), \(-\mathbf1\) for the lower-sum facet, and \(+\mathbf1_S\) for the maximal-independent facets. The first \(n\) rays form a unimodular basis. The toric divisor exact sequence
\[
0\longrightarrow M\xrightarrow{(\langle\cdot,u_\rho\rangle)_\rho}\mathbb Z^{\{\rho\}}\longrightarrow\operatorname{Cl}(\mathcal O_{X_n,p_0^{\mathrm{sp}}})\longrightarrow0
\]
therefore has free cokernel of rank \(a_n\). The toric canonical class is represented by minus the sum of invariant prime divisors; it is \(\mathbb Q\)-Cartier exactly when a rational support function has value one on every outward ray (changing all signs does not change feasibility). The coordinate rays require \(m_j=-1\) for \(j\ne0\); the lower-sum ray requires \(\sum_jm_j=-1\), hence \(m_0=n-2\). Every independent-set ray through \(e_0\) requires \(m_0=|S|\), since every other selected coordinate has coefficient \(-1\). If \(n\ge5\), then \(|S|\le\lfloor n/2\rfloor<n-2\), contradiction. If \(n=4\), every such \(S\) has size two, and the vector with entries \((2,-1,-1,-1)\) is an integral support function. This proves the spoke assertion.

**4. Rim chart class group and Gorenstein criterion.** At \(e_0+e_1\), the active facets are the \(n-2\) coordinate facets with \(j\ne0,1\), all \(2a_n\) maximal-independent facets containing exactly one of \(0,1\), and, if \(n\) is odd, the upper-sum facet. Their count is \(n-2+2a_n+\mathbf1_{\{n\text{ odd}\}}\). The \(n-2\) coordinate normals together with any one independent-set normal containing \(0\) and one containing \(1\) have determinant \(\pm1\). This again makes the divisor-class cokernel torsion-free, now of rank \(2a_n-2+\mathbf1_{\{n\text{ odd}\}}\).

For the canonical support equations, \(m_j=-1\) for \(j\ge2\). A maximal-independent set \(S\) with \(0\in S\) gives \(m_0=|S|\), and one with \(1\in S\) gives \(m_1=|S|\). Consequently solvability requires all maximal independent sets of the rim cycle to have equal cardinality: every such set can be rotated to contain vertex zero. Conversely, if they all have size \(k\), put \(m_0=m_1=k\) and all remaining entries \(-1\); this solves every independent-set equation. If \(n\) is odd, the additional upper-sum equation is \(\sum_jm_j=1\), or \(2k-(n-2)=1\), satisfied precisely when \(k=(n-1)/2\), as occurs in the exceptional odd cycles below.

To classify when all maximal rim independent sets have the same size, use their cyclic gap compositions. For \(n=4,5,7\), the only possible gap-multisets are, respectively, \((2,2)\), \((2,3)\), and \((2,2,3)\), so the sizes are uniformly \(2,2,3\). For every even \(n\ge6\), the gap compositions consisting of all twos and one obtained by replacing three twos by two threes have different lengths. For every odd \(n\ge9\), the gap compositions with one three and the remainder twos and with three threes and the remainder twos have different lengths. Thus exactly \(n\in\{4,5,7\}\) satisfy the equal-size condition, and the support solutions in those cases are integral, proving Gorensteinness rather than mere \(\mathbb Q\)-Gorensteinness.

**5. Smoothness.** An affine normal toric chart is smooth if and only if its cone has exactly \(n\) primitive rays forming a unimodular basis. Every spoke has \(a_n\ge1\) extra rays. The rim chart has class-group rank zero precisely for \(n=4\), where the determinant-one basis above proves smoothness. For all other rim charts the rank is positive, and they are singular. Rotation proves the result at every indexed point.

## Verification
Run `python check_wheel.py` with Python 3, NumPy, SymPy, and SciPy. The included recorded output enumerates rim maximal independent sets and candidate facet incidences for \(4\le n\le11\). For each \(n\), it verifies integer facet support and exact facet affine rank; compares all floating convex-hull simplices against the proposed complete exact facet family; checks the claimed ranks using exact integer ray matrices, finds rational canonical-support feasibility using symbolic linear algebra, and explicitly checks determinant-one ray bases. The terminal line reads `ALL EXACT FACET, LATTICE AND Q-GORENSTEIN TESTS PASSED`. The convex-hull enumeration uses numerical Qhull as a **finite sanity check**, not as evidence for the all-parameter facet theorem. The universal proof is the five steps above.

## Relationship to prior work
The graph-theoretic odd-cycle normality criterion and the full facet description belong to Ohsugi and Hibi (1998); none of those statements are new here. Their 2008 classification concerns **globally simple edge polytopes** and associated Gröbner, Ehrhart, and volume properties, and does not itself supply the local class-group rank formulas or the separate spoke/rim canonical thresholds. The fact that the only well-covered cycles with length at least four are \(C_4,C_5,C_7\) is established graph theory; the novel geometric inference asserted here is the exact wheel toric fixed-point \(\mathbb Q\)-Gorenstein criterion together with the corresponding class-group ranks. Other toric fixed-point calculations for different graph families do not imply these formulas. This is an explicit derivation from established polyhedral and toric machinery, not a claim of a new foundational theorem.

## Limitations
The classification covers only the \(2n\) torus-fixed points of this particular normal projective edge-toric variety, not all its singular strata or the full canonical sheaf. Its counting sequence is an elementary composition sequence; no novelty is claimed for the recurrence alone. Independent external proof review has not been performed. An equivalent specialization in uncatalogued work on wheel edge-polytopes or toric singularities remains a literature risk. Finite checker cases are not a proof of the infinite statement.

## References
1. H. Ohsugi and T. Hibi, *Normal Polytopes Arising from Finite Graphs*, Journal of Algebra **207** (1998), 409–426, DOI: `10.1006/jabr.1998.7476`, particularly Theorem 1.7 and Corollary 2.3. Public text: https://www.researchgate.net/publication/243020498_Normal_Polytopes_Arising_from_Finite_Graphs
2. H. Ohsugi and T. Hibi, *Simple polytopes arising from finite graphs*, arXiv:0804.4287, initially submitted 2008-04-27. Full text: https://arxiv.org/html/0804.4287v1
3. M. D. Plummer, *Well-covered graphs: a survey*, Quaestiones Mathematicae **16** (1993), 253–287, DOI: `10.1080/16073606.1993.9631737` (background on well-coveredness, not the toric classification).

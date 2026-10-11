# Four-subset sphere cycles give the rational top-homology permutation character of covering complexes

## Finding

For every integer \(m\ge4\), let \(K_m=\operatorname{Cov}_{m,2}\) be the simplicial complex on the \(\binom m2\) unordered edges of the complete graph on \([m]\): an edge family is a face precisely when some set of at most two graph vertices meets every edge. The natural relabeling action of \(S_m\) has

\[
\widetilde H_4(K_m;\mathbb Q)\cong \mathbb Q\left[\binom{[m]}{4}\right]
\]

as rational representations. The geometric basis consists of the fundamental classes \(z_T\) of the induced five-simplex boundaries on the six graph edges of each four-element vertex set \(T\). Every permutation acts by \(g_*z_T=z_{gT}\), without a sign.

If \(c_j(g)\) is the number of cycles of length \(j\) in \(g\), then

\[
\operatorname{tr}\bigl(g\mid\widetilde H_4(K_m;\mathbb Q)\bigr)
=[t^4]\prod_{j\ge1}(1+t^j)^{c_j(g)}.
\]

Consequently \(\dim H^4(|K_m|/S_m;\mathbb Q)=1\). The covering complex is also the two-subset Čech complex studied for the distance parameter \(4\le r<8\) in [2].

## Assumptions and scope

All graphs are simple with a fixed labeled vertex set \([m]=\{1,\ldots,m\}\). A graph-edge family has *covering number at most two* if two graph vertices (possibly one) intersect every graph edge. A face of \(K_m\) is such a family. Simplicial homology is reduced in positive degree, with rational coefficients unless specified. The four-vertex subcomplex \(K_T\subset K_m\) is induced on the six graph edges with endpoints in \(T\). The action of \(S_m\) permutes the graph-edge vertices of the simplicial complex, inducing ordinary signed simplicial-chain maps.

## Proof

**Four-vertex cycles.** When \(|T|=4\), the complete six-edge graph on \(T\) has minimum vertex-cover size three, whereas deleting any one edge leaves a graph covered by its two complementary vertices. Thus every proper subset of the six edge-vertices is a simplex and the full six-set is not. Hence \(K_T=\partial\Delta^5\), and its oriented boundary \(z_T\) is an integral four-cycle in \(K_m\).

**Coloring retractions.** Let \(f:[m]\to\{0,1,2,3\}\) be any four-coloring. Define a map on graph-edge vertices by sending \(\{u,v\}\) to \(\{f(u),f(v)\}\) when the colors differ, and to \(\{c,c+1\pmod4\}\) when both colors are \(c\). Each image edge contains the color of each of its preimage endpoints whenever that endpoint is used as a cover witness. Therefore the image of any face whose edges are covered by a set \(C\), \(|C|\le2\), is covered by \(f(C)\); this gives a simplicial map

\[
\Phi_f:K_m\longrightarrow K_4=\partial\Delta^5.
\]

For a four-set \(T\), if the restriction of \(f\) to \(T\) is injective, its six edge-vertices map bijectively onto the six edge-vertices of \(K_4\). The induced simplicial orientation sign is \(+1\): a transposition of the four graph vertices fixes two graph edges and exchanges two pairs of graph edges, hence is even on the six edge-vertices, and transpositions generate \(S_4\). If \(f|_T\) is not injective, the images of these six vertices number at most four (at most three distinct-color edges and at most one extra loop-replacement edge in the three-color case). Thus \(\Phi_f\) kills the fundamental four-cycle. Writing \(z\) for the common generator of \(\widetilde H_4(K_4;\mathbb Z)\), we have the exact rule

\[
(\Phi_f)_*(z_T)=\mathbf1_{\{f(x):x\in T\}=\{0,1,2,3\}}\,z.
\]

**Independence by four-color Fourier isolation.** Suppose \(\sum_{|T|=4}a_Tz_T=0\) in rational homology. Applying every coloring map yields

\[
\sum_{|T|=4} a_T\,\mathbf1_{f|_T\ \mathrm{injective}}=0
\qquad\text{for every } f:[m]\to\{0,1,2,3\}.
\]

Fix a four-set \(U\), multiply this equality by \(i^{\sum_{u\in U}f(u)}\), and sum over the \(4^m\) colorings. For \(T\ne U\), choose \(u\in U\setminus T\); the rainbow indicator for \(T\) is independent of \(f(u)\), and \(\sum_{c=0}^3i^c=0\), so its term vanishes. For \(T=U\) there are exactly \(4!\) bijections on \(U\), each contributing \(i^{0+1+2+3}=-1\), while colors outside \(U\) are arbitrary. Therefore

\[
-24\,4^{m-4}\,a_U=0.
\]

As the coefficient is nonzero over \(\mathbb Q\), every \(a_U=0\). Thus the \(\binom m4\) classes \(z_T\) are rationally independent.

**Completeness and action.** Jonsson's integral homology theorem [1, Theorem 7.1] establishes \(\widetilde H_4(K_m;\mathbb Z)\cong\mathbb Z^{\binom m4}\) for \(m\ge4\). The independent family therefore is a basis over \(\mathbb Q\). Graph-vertex permutations preserve each four-vertex boundary orientation, by the same transposition calculation, so \(g_*z_T=z_{gT}\). A fixed four-set is exactly a union of cycles of \(g\) totaling length four; this gives the character formula.

**Quotient consequence.** For a finite group action on a finite simplicial complex, barycentric subdivision and rational averaging identify the quotient's rational cohomology with invariant cohomology. The invariant subspace of the four-set permutation module is one-dimensional, generated by the sum of all basis vectors. Hence \(H^4(|K_m|/S_m;\mathbb Q)\cong\mathbb Q\).

## Verification

The accompanying standalone Python program enumerates covering faces and all four-vertex simplicial boundaries; checks the orientation sign for all 24 permutations of four vertices; tests that 21,412 facet/induced-sphere coloring images are well defined or have the stated rank-collapse behavior for small dimensions; computes full column rank of the rainbow evaluation matrices modulo 101 for \(4\le m\le8\), with columns counts \(1,5,15,35,70\); and checks the Fourier coefficient for \(4\le m\le7\). These are independent finite corroborations. The assertion for every \(m\ge4\) follows from the displayed exact argument and the cited integral homology-rank theorem, not from finite enumeration.

Run: `python3 verify.py` (Python standard library only). Expected final line begins `VERIFY_OK`.

## Relationship to prior work

Jonsson [1] proves the integral Betti-number formula \(\operatorname{rank}\widetilde H_4(K_m;\mathbb Z)=\binom m4\) and the concentration of homology in degrees three and four. This *rank formula is not new*. Biswas [2] identifies the same covering complex with a finite-set Čech complex and proposes a stronger homotopy wedge description, but its accessible final section treats nonequivariant homotopy. The present result adds a geometric rational basis and the complete \(S_m\)-action on degree-four homology, which neither a rank formula nor a nonequivariant sphere-wedge count determines. The proposed homotopy conjecture is not proved here.

## Limitations

The orientation and basis are established over rational coefficients. Although the cycles themselves are integral, we do not assert they form a \(\mathbb Z\)-basis, determine their possible integral lattice index, describe the degree-three representation, or construct an equivariant homotopy decomposition. The full text of the older covering-complex reference was not available for a page-by-page equivalence check; its exact published homology-rank theorem was independently identified and explicitly credited. Equivalent unindexed equivariant results cannot be excluded by database searches.

## References

[1] Jakob Jonsson, *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*, SIAM Journal on Discrete Mathematics 19 (2005), 633–650, Theorem 7.1. DOI: 10.1137/S0895480104443680. An author-preprint indexed excerpt records the theorem's integral rank statement.

[2] Anamitro Biswas, *Čech complexes for finite sets*, arXiv:2609.32786v1, first publicly submitted 2026-09-26, especially Section 1 and Section 5.

# Complete homotopy classification of bidirected-cycle multipath complexes

## Finding
Let \(B_n\) be the bidirected simple cycle on \(n+1\) vertices (both arrows on every cycle edge), with \(n\ge2\), and let \(X_n\) be its multipath complex: a simplex is a collection of directed arrows whose selected digraph is a disjoint union of directed simple paths and isolated vertices.

For \(n\ge3\), define
\[
k(n)=\begin{cases}
 n/2,&n\equiv0\pmod4,\\
 \lfloor(n-1)/2\rfloor,&n\not\equiv0\pmod4,
\end{cases}
\qquad
b(n)=\begin{cases}3,&n\equiv3\pmod4,\\1,&\text{otherwise}.\end{cases}
\]
Then the complete integral homotopy classification is
\[
\boxed{X_n\simeq\left(\bigvee^{b(n)}S^{k(n)}\right)\vee\left(\bigvee^2S^{n-1}\right)\quad(n\ge3).}
\]
The exceptional bidirected triangle has \(X_2\cong S^1\sqcup S^1\), where each circle is the boundary of an abstract triangle. In particular, the previously open sphere-wedge prediction holds for every bidirected polygon on at least four vertices, with explicit sphere multiplicities and dimensions. Examples are \(X_3\simeq(\bigvee^3S^1)\vee(\bigvee^2S^2)\), \(X_4\simeq S^2\vee(\bigvee^2S^3)\), \(X_5\simeq S^2\vee(\bigvee^2S^4)\), and \(X_7\simeq(\bigvee^3S^3)\vee(\bigvee^2S^6)\).

## Assumptions and scope
Fix the standard finite simple cycle \(C_{n+1}\), with \(n\ge2\). Write its forward arcs as \(f_i:i\to i+1\), and backward arcs as \(b_i:i+1\to i\), with indices modulo \(n+1\). Loops and multiple parallel arrows are absent. A face must have indegree and outdegree at most one at each vertex and contain no directed cycle. All topological realizations are those of finite abstract simplicial complexes; the displayed homotopy equivalences are nonequivariant and integral.

The high-connectivity statement and the integral homology groups used below are those proved by Caputi–Collari–Smith (2026), Theorems 2.8 and 2.10, with exactly their parameter \(n\). Their Theorem 2.10 gives, for \(n\ge3\), reduced homology \(\mathbb Z^{b(n)}\) in degree \(k(n)\), \(\mathbb Z^2\) in degree \(n-1\), and zero otherwise. Their Theorem 2.8 states that \(X_n\) is \(\bigl(\lfloor(n-1)/2\rfloor-1\bigr)\)-connected. The homotopy equivalence asserted here is not assumed from those statements.

## Proof
**1. The two top spheres represent the entire top homology integrally.** Write \(m=n+1\). A multipath of \(m-1=n\) arrows has one connected component, because a forest on \(m\) vertices with \(m-1\) edges is a tree. In a cycle, it is therefore a directed Hamiltonian path. Such a path is obtained by removing one edge from the underlying polygon and consistently orienting all remaining edges. Hence every \((n-1)\)-simplex of \(X_n\) consists either of all forward arrows except one or all backward arrows except one. There are exactly \(2m\) such simplices and no \(n\)-simplices.

The full subcomplexes on \(\{f_0,\ldots,f_{m-1}\}\) and on \(\{b_0,\ldots,b_{m-1}\}\) are both boundaries \(\partial\Delta^{m-1}\cong S^{m-2}=S^{n-1}\): every proper subset is a multipath, while the full set is a directed cycle. Let \(z_+\) and \(z_-\) be their oriented fundamental cycles. The top chain group is the direct sum of the chains on the \(m\) forward and \(m\) backward facets. The boundaries of forward top facets involve only forward arcs, and the boundaries of backward top facets only backward arcs. These supports are disjoint. Within each collection, the only top cycle is an integer multiple of the alternating boundary of the omitted full simplex: compare coefficients at faces missing any two arcs. It follows that
\[
\widetilde H_{n-1}(X_n;\mathbb Z)=\mathbb Z[z_+]\oplus\mathbb Z[z_-]
\]
for every \(n\ge2\). In particular, **both primitive top generators are represented by actual embedded spheres**. This is the homotopy-relevant fact, not a mere calculation of the top Betti number.

**2. Connectivity and realization of the lower-degree classes.** For \(n\ge5\) put \(k=k(n)\). When \(n\not\equiv0\pmod4\), the cited connectivity theorem gives \((k-1)\)-connectedness. When \(n\equiv0\pmod4\), necessarily \(n\ge8\), and it gives \((k-2)\)-connectedness. The cited integral homology theorem gives \(H_{k-1}(X_n;\mathbb Z)=0\); the Hurewicz theorem at degree \(k-1\ge3\) therefore upgrades the latter case to \((k-1)\)-connectedness too. Thus for every \(n\ge5\), \(X_n\) is simply connected and the Hurewicz homomorphism
\[
\pi_k(X_n)\longrightarrow H_k(X_n;\mathbb Z)\cong\mathbb Z^{b(n)}
\]
is an isomorphism. Choose maps from \(b(n)\) copies of \(S^k\) representing a basis. Wedge these maps with the two inclusions of the top spheres from Step 1, arranging the finite domains to have a common base point by paths in the connected target. The resulting map
\[
F:\left(\bigvee^{b(n)}S^k\right)\vee\left(\bigvee^2S^{n-1}\right)\longrightarrow X_n
\]
induces an isomorphism on every integral homology group. Both spaces are simply connected CW complexes. The homological Whitehead theorem (or the acyclic simply-connected mapping cone plus Hurewicz and Whitehead) makes \(F\) a homotopy equivalence.

**3. The five-vertex polygon, \(n=4\).** The two consistently oriented arc sets span embedded \(S^3\)'s, say \(A\) and \(B\). Any mixed edge in \(X_4\) connects \(f_i\) to either \(b_{i+2}\) or \(b_{i+3}\) (indices modulo five), so there are ten such bridges. There are ten mixed triangles: five \(\{f_i,b_{i+2},b_{i+3}\}\) and five \(\{f_i,f_{i+1},b_{i+3}\}\), and there are no higher-dimensional mixed simplices. Each mixed triangle identifies the homotopy class of its two bridge edges, relative to the simply connected subspaces \(A\) and \(B\). The ten bridge edges and the ten relations form one cyclic chain of equalities:
\[
\{f_i,b_{i+2}\}\sim\{f_i,b_{i+3}\}\sim\{f_{i+1},b_{i+3}\}\qquad(i\bmod5).
\]
Thus all bridges are homotopic relative to \(A\) and \(B\). Take any one bridge to connect them; the other nine potential fundamental-group generators are killed, so \(X_4\) is simply connected by van Kampen. By the cited integral homology theorem \(H_2(X_4)=\mathbb Z\), and Hurewicz supplies a sphere map representing its generator. Adding the two embedded top spheres gives a homology equivalence \(S^2\vee S^3\vee S^3\to X_4\) between simply connected CW complexes, hence a homotopy equivalence by Whitehead.

**4. The four- and three-vertex polygons.** For \(n=3\), the two consistently oriented four-arrow subcomplexes are disjoint copies of \(\partial\Delta^3=S^2\). The only mixed simplices are the four bridge edges \(\{f_i,b_{i+2}\}\), indexed modulo four. The homotopy type of the resulting space—two spheres joined by four disjoint bridges—is \(S^2\vee S^2\vee\bigvee^3S^1\). For \(n=2\), no mixed edge is allowed, and the two oriented three-arrow boundaries are disjoint circles. This proves the remaining cases.

## Verification
The companion, dependency-free `verify.py` enumerates multipaths by an undirected-edge ternary-state method for all \(2\le n\le9\). For \(n\le7\), it independently re-enumerates all directed-arrow subsets and checks degree constraints and directed cycles. It checks that the top-dimensional facets consist **exactly** of the \(2(n+1)\) consistently oriented Hamiltonian paths, computes the signed boundaries of both top cycles, and reduces all mod-two simplicial boundary matrices exactly. The mod-two reduced Betti numbers agree with the theorem in each case. It also directly checks the bridge patterns and absence of mixed higher-dimensional faces at the three small parameters, including connectivity of the ten-bridge relation graph for \(n=4\).

Executed output ends with `ALL_VERIFY_OK top_sphere_cycles small_n_geometry and_mod2_chain_ranks`. These finite checks are corroboration, not a replacement for Steps 1–4 or for the cited integral homology and connectivity theorems.

## Relationship to prior work
Caputi, Collari and Smith, *Multipath complexes of bidirectional polygonal digraphs* (2026), Theorems 2.8 and 2.10, prove the connectivity and integral homology information used here. Section 3 explicitly leaves the sphere-wedge homotopy question open and establishes non-shellability, so their homology theorem alone does not state the claimed homotopy type. Earlier work by Caputi, Collari, Di Trani and Smith treats differently oriented polygonal digraphs, not this all-bidirected family.

The publicly available result *Dihedral rational homology of bidirectional-polygon multipath complexes* already identifies the two consistently oriented top cycles while calculating the dihedral **rational homology representations**. Those top cycles are therefore not claimed as a new representation-theoretic discovery. The additional topological step in the present result is to use their embedded sphere representatives together with integral connectivity, Hurewicz and homological Whitehead to obtain an actual all-parameter homotopy equivalence, with an explicit van Kampen argument for the five-vertex case. No equivariant splitting is asserted.

## Limitations
This result concerns the ordinary multipath complex of a **bidirected simple cycle**, not a bidirected graph of arbitrary shape and not the multipath complex of a complete digraph. The proof depends on the published integral homology and connectivity theorems cited above, which were checked against the primary preprint but not independently reproved here. The sphere maps from lower homology in the uniform range are existential via Hurewicz; the result does not provide canonical or equivariant lower-sphere generators. The two-circle exception is disconnected and therefore is not a single based wedge. Independent mathematical validation has not been performed.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first public 2026-01-09, Theorems 2.8 and 2.10, Section 3. https://arxiv.org/html/2601.05670v1
2. *Dihedral rational homology of bidirectional-polygon multipath complexes*, publicly available published-finding corpus research result (2026), especially Proof Step 4 concerning top cycles. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-dihedral-rational-homology-of-bidirectional-polygon-multipath-co--627013477864
3. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (2022). https://arxiv.org/abs/2208.04656

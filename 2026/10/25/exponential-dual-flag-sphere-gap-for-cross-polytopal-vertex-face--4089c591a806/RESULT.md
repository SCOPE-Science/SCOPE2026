# Exponential dual flag-sphere gap for cross-polytopal vertex–facet spaces

## Finding
For every integer \(m\ge 3\), a canonical finite \(T_0\) Alexandrov space \(X_m\), formed by the vertex–facet incidences of the \(m\)-dimensional cross-polytope, has
\[
|\operatorname{Cl}(\operatorname{Cm}(X_m))|\simeq S^{m-1},\qquad
|\operatorname{Cl}(\operatorname{Ins}(X_m))|\simeq S^{2^{m-1}-1}.
\]
Here \(\operatorname{Cl}\) is the graph clique/flag complex, \(\operatorname{Cm}\) is the closure-meeting graph, and \(\operatorname{Ins}\) is the inseparability graph. By contrast, the *joint-intersection nerves* satisfy
\[
|\mathcal N_{\mathrm{cm}}(X_m)|\simeq
|\mathcal N_{\mathrm{ins}}(X_m)|\simeq S^{m-1}.
\]
Thus the homotopy duality of the genuine nerves does not extend to the flag completions of their one-skeleta; the gap in sphere dimensions is \(2^{m-1}-m\).

## Assumptions and scope
Fix \(m\ge3\). Let \(C_m\subset\mathbb R^m\) be the convex hull of the \(2m\) signed coordinate vectors. Its vertices are \(v_{i,\varepsilon}\), with \(1\le i\le m\) and \(\varepsilon\in\{-1,+1\}\). Its facets correspond to sign vectors \(s=(s_1,\ldots,s_m)\in\{-1,+1\}^m\), each containing precisely the \(m\) vertices \(v_{i,s_i}\). Define \(X_m\) to be the **two-rank vertex–facet incidence poset**, not the full face poset: in addition to equality its only order relations are
\[
v_{i,\varepsilon}<f_s\quad\Longleftrightarrow\quad\varepsilon=s_i.
\]
Give it the finite Alexandrov topology whose opens are down-sets, and hence point closures are up-sets. Its cardinality is \(2m+2^m\). In this convention two points are inseparable precisely when they have a common lower bound, and are closure-meeting precisely when they have a common upper bound. All clique complexes below have the full graph vertex set initially; the homotopy reductions remove dominated vertices.

## Proof
**Domination lemma.** In a finite simple graph \(G\), if distinct adjacent vertices \(a,b\) satisfy \(N_G[a]\subseteq N_G[b]\) for closed neighborhoods, then the inclusion \(\operatorname{Cl}(G-a)\hookrightarrow\operatorname{Cl}(G)\) is a homotopy equivalence, in fact a simplicial collapse. To see this, every clique \(\sigma\) containing \(a\) but not \(b\) extends to \(\sigma\cup\{b\}\). Pair these simplices in descending order of the size of \(\sigma\); after the larger pairs have been removed, each pair is a free-face elementary collapse. The remaining complex is exactly \(\operatorname{Cl}(G-a)\).

**Closure-meeting graph.** Fix a facet point \(f_s\) and any incident vertex point \(v_{i,s_i}\). Because \(f_s\) is maximal, every point sharing an upper bound with \(f_s\) is \(f_s\) itself or a vertex below \(f_s\). Every such point shares the upper bound \(f_s\) with \(v_{i,s_i}\). Hence
\[
N_{\operatorname{Cm}}[f_s]\subseteq N_{\operatorname{Cm}}[v_{i,s_i}].
\]
Delete the facet points successively using the domination lemma. (Domination persists under vertex deletion.) The induced graph on the remaining signed vertex points joins \(v_{i,\varepsilon}\) and \(v_{j,\delta}\) precisely if \(i\ne j\), since a facet contains at most one vertex from each opposite pair, but contains any choice on different coordinates. Thus it is the complete multipartite graph with \(m\) parts, each of size two. Its clique complex is the simplicial join of \(m\) two-point discrete complexes, \((S^0)^{*m}\), which is a triangulated \(S^{m-1}\).

**Inseparability graph.** Fix a vertex point \(v_{i,\varepsilon}\) and any facet \(f_s\) incident to it. Since \(v_{i,\varepsilon}\) is minimal, a point shares a lower bound with it if and only if it lies above \(v_{i,\varepsilon}\). All such points also share this lower bound with \(f_s\); hence
\[
N_{\operatorname{Ins}}[v_{i,\varepsilon}]\subseteq N_{\operatorname{Ins}}[f_s].
\]
Remove all \(2m\) vertex points. Two distinct remaining facets \(f_s,f_t\) have a common lower bound precisely when they agree in at least one coordinate. For two sign vectors this fails exactly when \(t=-s\). Consequently the resulting graph is the complete graph on the \(2^m\) sign vectors with the \(2^{m-1}\) antipodal pairs deleted. Its clique complex is the join of \(2^{m-1}\) copies of \(S^0\), hence is a triangulated \(S^{2^{m-1}-1}\).

**Genuine joint-intersection nerves.** The associated incidence Dowker complex \(\mathcal D(X_m)\) has the signed coordinate vertices as its vertex set and a simplex on a nonempty set precisely when all vertices in that set lie below some common facet. This is equivalent to choosing at most one sign in each coordinate, so \(\mathcal D(X_m)=(S^0)^{*m}\cong S^{m-1}\). The finite-space Dowker duality theorem (Cameron–Kumar, Theorem 9.2(a)) gives
\[
|\mathcal N_{\mathrm{ins}}(X_m)|\simeq|\mathcal D(X_m)|\simeq|\mathcal N_{\mathrm{cm}}(X_m)|.
\]
The two flag spheres have different dimensions because \(2^{m-1}-1>m-1\) for \(m\ge3\), witnessed by their integral reduced homology in those distinct degrees. This finishes all claimed statements.

## Verification
A standalone standard-library script `check_incidence.py` builds the finite incidence posets for \(m=2,3,4\), independently recomputes both graphs by intersections of lower/upper sets, checks all proposed closed-neighborhood dominations, and verifies the induced-graph adjacency formula and their face vectors. For \(m=2,3\) it additionally obtains the reduced homology groups by exact mod-two boundary-matrix ranks. For \(m=3\) the output gives \(\widetilde H_3\cong\mathbf F_2\) on the inseparability side and \(\widetilde H_2\cong\mathbf F_2\) on the closure-meeting side. These finite calculations are supplementary; the proof above establishes the statements for all \(m\ge3\) without an extrapolation from experiments.

## Relationship to prior work
Cameron and Kumar's *Graphs on Topological Spaces* (arXiv:2610.14783, initially public 2026-10-10) introduces the two graphs and proves homotopy equivalence of their joint-intersection nerves for finite spaces (Theorem 9.2). Their Example 9.4 identifies a different, six-point face-poset example in which an inseparability clique completion changes the nerve's homotopy type to a point. The present calculation treats both **dual** clique completions simultaneously for a natural growing family of vertex–facet spaces and finds two noncontractible spheres of exponentially separated dimensions; neither the general nerve equivalence nor that example specifies these flag-completion types. The known topological fact that a clique complex is unchanged up to homotopy under closed-neighborhood domination is used as a proof tool, not asserted to be new.

## Limitations
These spaces are **not** the entire face posets of the cross-polytopes, and the assertion about the two nerves does **not** claim that the finite space \(X_m\) itself is weakly homotopy equivalent to a sphere. The result is restricted to the graph clique complexes of this incidence family, not all finite Alexandrov spaces or arbitrary poset dimensions. The mathematical novelty claim is qualified by the possibility of an equivalent previously published graph/hypergraph construction under different terminology; this work does not establish exhaustive priority. The provided computer checks cover only \(m\in\{2,3,4\}\).

## References
1. P. J. Cameron and Vinod Kumar P. B., *Graphs on Topological Spaces*, arXiv:2610.14783 (first public 2026-10-10), especially Definitions 9.1, Theorem 9.2, and Example 9.4. https://arxiv.org/abs/2610.14783
2. A. Dochtermann and T. Matsushita, *Simple homotopy of flag simplicial complexes and contractible contractions of graphs*, arXiv:2312.10976 (2023), for background on simple-homotopy operations on flag complexes. https://arxiv.org/abs/2312.10976

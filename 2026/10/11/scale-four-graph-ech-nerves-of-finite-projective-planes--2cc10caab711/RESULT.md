# Scale-four graph Čech nerves of finite projective planes

## Finding
Let \(\Pi\) be **any finite projective plane** of order \(q\ge 2\), and let \(G_\Pi\) be its bipartite point–line incidence graph, with every edge of length one. The intrinsic graph Čech nerve of closed metric balls centered at vertices satisfies
\[
\mathcal N(G_\Pi,4)\simeq\bigvee^{q^6}S^4.
\]
Equivalently, its reduced integral homology is \(\widetilde H_4\cong\mathbb Z^{q^6}\) and \(\widetilde H_i=0\) for every \(i\ne4\). The complex has \(2(q^2+q+1)\) vertices, \(2(q^2+q+1)\) maximal simplices and simplicial dimension \((q+1)^2\), despite having the homotopy type of a four-dimensional CW complex. It remains unchanged for \(4\le r<5\) and becomes a full simplex for \(r\ge5\).

## Assumptions and scope
A projective plane of order \(q\) has \(v=q^2+q+1\) points \(P\) and \(v\) lines \(L\). Every line contains \(q+1\) points, every point lies on \(q+1\) lines, every two distinct points determine exactly one line, and every two distinct lines meet at exactly one point. These axioms alone are used; no coordinatization or Desarguesian assumption is made. The theorem is conditional on the existence of the plane for its order.

For every \(r\ge0\), \(\mathcal N(G_\Pi,r)\) is the abstract nerve of closed balls of radius \(r/2\) about the \(2v\) graph vertices, in the **geometric realization** of \(G_\Pi\) with its shortest-path metric. In particular, this is not the Vietoris–Rips complex and is not a Čech nerve formed by balls only in the vertex set. Intersections at geometric edge interiors are included in the definition.

## Proof
**1. Exact scale-four facets.** Distinct points have graph distance \(2\), as do distinct lines; an incident point–line pair has distance \(1\) and a nonincident pair has distance \(3\). Thus the closed vertex-neighborhood of radius \(2\) around a point \(p\) is \(P\cup L(p)\), where \(L(p)\) consists of the \(q+1\) lines through \(p\). Around a line \(\ell\) it is \(L\cup P(\ell)\), where \(P(\ell)\) is its set of \(q+1\) points.

At integral ball radius \(2\), any nonempty common intersection of vertex-centered closed balls contains a graph vertex (see also Adams–Shukla–Singh, Lemma 2.2). Consequently, with \(\Delta(S)\) the full simplex on the vertex set \(S\),
\[
K:=\mathcal N(G_\Pi,4)=A\cup B,\qquad
 A=\bigcup_{p\in P}\Delta(P\cup L(p)),\quad
 B=\bigcup_{\ell\in L}\Delta(L\cup P(\ell)).
\]
Every face of \(A\) may be enlarged by any fixed point of \(P\), so \(A\) is a cone. Similarly, \(B\) is a cone with any fixed line as apex. The displayed \(2v\) generators are distinct maximal simplices: each has \(v+q+1\) vertices, whereas \(q+1<v\) prevents cross-type containment. Thus the simplicial dimension is \(v+q=(q+1)^2\).

**2. The exact intersection.** Define the point-collinearity and line-concurrency complexes
\[
J_P=\bigcup_{\ell\in L}\Delta(P(\ell)),\qquad
J_L=\bigcup_{p\in P}\Delta(L(p)).
\]
A set \(X\sqcup Y\), where \(X\subseteq P\) and \(Y\subseteq L\), is a face of \(A\) exactly when \(Y\) is contained in the lines through some point; it is a face of \(B\) exactly when \(X\) is contained in the points on some line. These independent conditions give the **simplicial equality**
\[
A\cap B=J_P*J_L,
\]
where \(*\) denotes the simplicial join of complexes on the disjoint vertex sets \(P,L\). The empty face is included when constructing joins.

**3. Uniform collapses of the two factors.** On each line \(\ell\), choose an arbitrary distinguished point \(a_\ell\in P(\ell)\). Within \(\Delta(P(\ell))\), order nonempty subsets \(\sigma\subseteq P(\ell)\setminus\{a_\ell\}\) having \(|\sigma|\ge2\) by decreasing cardinality. Pair each \(\sigma\) with \(\sigma\cup\{a_\ell\}\) and remove the pair. At removal, all strictly larger cofaces have been removed, and the only remaining coface properly containing \(\sigma\) is \(\sigma\cup\{a_\ell\}\); hence this is an elementary free-face collapse. Each pair of distinct points belongs to a **unique** line, so distinct line simplices have no common face of dimension at least one. Therefore the collapses can be applied across all lines without interference. Each line simplex is reduced to the star tree whose edges join \(a_\ell\) to the other \(q\) points of that line.

The resulting graph \(T_P\) has \(v\) vertices and \(qv\) edges, with no repeated edges. It is connected because every pair of points lies on a line and is connected by a length-at-most-two path through that line's star. Its cycle rank is
\[
qv-v+1=(q-1)(q^2+q+1)+1=q^3.
\]
Thus \(J_P\searrow T_P\simeq\bigvee^{q^3}S^1\). The dual construction, choosing one line through each point, gives \(J_L\searrow T_L\simeq\bigvee^{q^3}S^1\). Each factor collapse uses exactly \(v(2^q-q-1)\) elementary pairs.

**4. Homotopy pushout and join.** As \(A,B\) are contractible finite subcomplexes and \(J_P*J_L\) is connected, the cofibration pushout \(A\cup B\) is homotopy equivalent to the unreduced suspension of \(A\cap B\). Homotopy invariance of joins and the formula \(X*Y\simeq\Sigma(X\wedge Y)\) for connected based CW complexes give
\[
\begin{aligned}
K&\simeq\Sigma(J_P*J_L)\\
 &\simeq\Sigma\!\left(\bigvee^{q^3}S^1*\bigvee^{q^3}S^1\right)\\
 &\simeq\bigvee^{q^6}S^4.
\end{aligned}
\]
The integral-homology assertion follows from this homotopy equivalence; it does not require a field computation.

**5. Endpoint beyond scale four.** The general graph Čech nerve is constant between successive integer values of \(r\) (Adams–Shukla–Singh, Lemma 2.2). For any incidence edge \(p\ell\), its midpoint is at distance at most \(5/2\) from every graph vertex: every point is at distance at most \(2\) from \(p\), and every line at distance at most \(2\) from \(\ell\). Hence all radius-\(5/2\) balls meet at that midpoint, and \(\mathcal N(G_\Pi,r)\) is a full simplex for \(r\ge5\).

## Verification
A standalone standard-library program (`verify_projective_cech.py`) constructs the classical projective planes of prime orders \(2\) and \(3\) from normalized homogeneous triples, checks all incidence axioms, computes all graph distances by breadth-first search, and checks that the distance-two balls give exactly the \(2v\) displayed generating facets. It verifies the elementary free-face deletions in both collinearity complexes and their graph cycle ranks.

For \(q=2\), it also constructs **all 7,919 nonempty faces** of the 14-vertex Čech complex, verifies the exact join formula for \(A\cap B\), and calculates every mod-two boundary rank independently. It obtains reduced Betti rank \(64\) in degree \(4\) and zero in all other degrees. For \(q=3\), it checks 26 distance-ball facets, both 52-pair factor collapses, cycle rank \(27\), and the consequent uniform prediction of \(729\) four-spheres. Execute `python3 verify_projective_cech.py`; the successful output ends with `VERIFY_OK`. The finite computations are corroboration, **not** the proof for all orders or for non-Desarguesian planes.

## Relationship to prior work
Adams, Shukla and Singh introduce this precise intrinsic graph Čech convention and establish the even/odd scale facet formula (their Lemma 2.2); their principal homotopy calculations concern **hypercube graphs**, not finite projective-plane incidence graphs. Previte's earlier \(D\)-neighborhood construction includes the same even-radius nerve as a particular distance set, but her studied graph classes and general propositions do not give this order-uniform projective-plane computation.

The published scale-two Vietoris–Rips theorem for projective-plane incidence graphs computes \(\bigvee^{q^3}S^2\), a **different graph complex**: it is a clique complex at threshold \(2\), whereas the present claim concerns the ball-intersection nerve at threshold \(4\). The previous theorem establishes no implication for the Čech homotopy type without the new intersection-join analysis above. At \(q=2\), the present formula specializes to the Heawood graph's count of \(64\) four-spheres; the assertion's substantive scope is the exact infinite-family theorem for arbitrary existing projective-plane orders, including non-Desarguesian ones.

## Limitations
The theorem applies only to genuine finite projective planes, not arbitrary partial planes, incidence graphs of general block designs, or higher-dimensional projective spaces. It does not classify the full Čech filtration at smaller scales or determine maps between its homology groups below scale four. The proof does not establish the existence of a projective plane at any prescribed order. The originality search cannot exclude unindexed or differently named equivalent results, and no independent mathematical audit has been performed.

## References
1. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first public version 2022-12-12; especially Lemmas 2.2 and 2.6, and §3. Primary MSC 55N31.
2. C. Previte, *The D-neighborhood complex of a graph*, PhD dissertation, Colorado State University, 2014, DOI 10.25675/3.018305; especially Chapter 3, §3.3, and Chapter 8.
3. *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, published finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3 ; especially its statements and proof distinguishing its clique construction.

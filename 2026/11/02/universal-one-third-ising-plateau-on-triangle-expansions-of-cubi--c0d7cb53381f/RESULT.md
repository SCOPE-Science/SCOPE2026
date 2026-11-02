# Universal one-third Ising plateau on triangle expansions of cubic graphs

## Finding
Let \(G\) be any finite simple cubic graph on \(n\) vertices with a perfect matching. Replace each vertex by a triangle, with its three new vertices indexed by the three incident edges of \(G\); join corresponding vertices across each original edge. On this triangle-expanded graph \(T(G)\), take the classical antiferromagnetic Ising Hamiltonian
\[
H(\sigma)=J\sum_{\{i,j\}\in E(T(G))}\sigma_i\sigma_j-h\sum_i\sigma_i,
\qquad \sigma_i\in\{-1,+1\},\quad J>0,\quad h\in\mathbb R.
\]
There are \(3n\) spins. For every admissible integer magnetization \(M\in\{-3n,-3n+2,\ldots,3n\}\), the exact least exchange energy among all states of magnetization \(M\) is
\[
\boxed{E_{\min}(M)=J\max\left\{|M|-\frac{5n}{2},\;3|M|-\frac{9n}{2}\right\}.}
\]
Consequently the zero-temperature ground-state magnetization for strictly positive field has only the following strict plateaux:
\[
\boxed{M=0\ (0<h<J),\qquad M=n\ (J<h<3J),\qquad M=3n\ (h>3J).}
\]
The intermediate plateau is universally one third of saturation; the only positive critical fields are \(h=J\) and \(h=3J\). At \(h=J\), precisely the sectors \(M=0,2,\ldots,n\) coexist; at \(h=3J\), precisely \(M=n,n+2,\ldots,3n\) coexist. Negative fields follow by simultaneous spin reversal, and at \(h=0\) only \(M=0\) minimizes energy.

Ground-state counts have an exact combinatorial classification. For \(Q=(3n-M)/2\le n\), every fixed-magnetization minimizer is a matching of size \(Q\) in the bipartite vertex-edge incidence graph of \(G\). For \(n\le Q\le3n/2\), minimizers are partial orientations of exactly \(Q\) edges of \(G\), with no edge oriented twice and with the number of selected edge-ends at every vertex equal to one or two. Counts for negative \(M\) follow by spin reversal.

For \(G=Q_3\), the ordinary cube, \(T(G)\) is the 24-vertex truncated-cube graph. Its fixed-magnetization degeneracies for \(Q=0,1,\ldots,12\) are exactly
\[
(1,24,240,1296,4092,7632,8056,4272,828,3312,4572,2520,450).
\]
Thus zero field has \(450\) ground states, the positive one-third plateau has \(828\), and the critical fields \(h=J\) and \(h=3J\) have respectively \(11682\) and \(26441\) ground states. These are counts of labelled spin configurations, not symmetry orbits.

## Assumptions and scope
A *cubic graph* is finite, simple, and three-regular. Its perfect matching \(F\) consists of disjoint edges covering all \(n\) original vertices; \(n\) must therefore be even. The complementary spanning subgraph \(G\setminus F\) is a union of disjoint cycles. The triangle expansion has one spin at each incidence \((v,e)\) and has two edge types: the three internal triangle bonds for each original vertex and the single bridge bond across each original edge. All bonds have the same antiferromagnetic coupling \(J>0\). No thermodynamic-limit or finite-temperature assertion is made.

For a fixed configuration let \(Q\) count negative spins; then \(M=3n-2Q\). Let \(T\) be the number of monochromatic internal triangles. Let \(B\) count original edges whose two associated spins are equal; these are the frustrated bridge bonds. The graph has \(n\) triangles and \(3n/2\) bridges.

## Proof
**1. Exact energy identity.** In each internal triangle the sum of three bond products is \(-1\) when both spin signs occur and \(+3\) when monochromatic. Each bridge contributes \(-1\) for opposite signs and \(+1\) for equal signs. Hence, writing \(E\) for the exchange portion of \(H\),
\[
E/J=-\frac{5n}{2}+4T+2B.
\]

**2. Two counting bounds.** Restrict first to \(0\le Q\le3n/2\), equivalently \(M\ge0\). An original edge has zero, one, or two negative endpoints. Denote the numbers with zero or two negatives by \(B_{++}\) and \(B_{--}\). Then \(B=B_{++}+B_{--}\) and \(Q=3n/2-B_{++}+B_{--}\), giving
\[
B\ge\frac{3n}{2}-Q,
\]
with equality precisely when no bridge has two negative endpoints. Moreover at most \(Q\) triangles can contain a negative spin, so
\[
T\ge\max\{0,n-Q\}.
\]
Substitution gives
\[
E/J\ge
\begin{cases}
9n/2-6Q,&0\le Q\le n,\\
n/2-2Q,&n\le Q\le3n/2.
\end{cases}
\]

**3. Simultaneous sharpness for every \(Q\).** Delete a perfect matching \(F\) from \(G\). The remaining edges form disjoint cycles. Orient each cycle consistently, and mark the spin at the tail incidence of each cycle edge as negative. There is exactly one marked incidence at each vertex, no original edge is marked twice, and there are \(n\) marks in total. To achieve \(Q\le n\), retain any \(Q\) of these marks. Then exactly \(n-Q\) triangles are monochromatic and exactly \(3n/2-Q\) bridges are frustrated; both bounds in step 2 are equalities. To achieve \(n\le Q\le3n/2\), retain all \(n\) cycle marks and choose \(Q-n\) edges of \(F\), marking just one arbitrarily chosen endpoint on each. The perfect matching guarantees at most two negative spins per triangle. Every triangle is mixed and no bridge has two negatives; again both bounds are equalities. Thus the lower bounds are attained at *every* allowed \(Q\).

**4. All magnetizations and fields.** Under global spin reversal, exchange energy is unchanged and magnetization changes sign. Replace \(Q=(3n-M)/2\) in step 2 and apply reversal to obtain the claimed piecewise formula in \(|M|\). Minimizing \(E_{\min}(M)-hM\) over its two linear pieces gives the stated plateaux and critical fields. At a critical field an entire linear segment ties; no other magnetization sector does.

**5. Complete equality-case description.** When \(0\le Q\le n\), equality forces \(T=n-Q\) and \(B=3n/2-Q\). Thus each negative spin lies in its own original triangle and no original edge has two negatives: the selected incidences form a matching in the vertex-edge incidence graph. Conversely every such matching realizes equality. When \(n\le Q\le3n/2\), equality forces \(T=0\), so each triangle contains one or two negatives, and it forces \(B=3n/2-Q\), so no original edge has two negatives. This is exactly a partial orientation of \(Q\) original edges with one or two selected edge-ends at each vertex. This bijection proves the degeneracy classification.

**6. Cube-specific exact counts.** Label original cube vertices by \(v\in\{0,\ldots,7\}\), and edges by \(\{v,v\oplus2^a\}\), for \(a\in\{0,1,2\}\) and \(v\)'s \(a\)-th binary bit equal to zero. Enumerate the three states of each of the twelve original edges: no selected end, first end selected, or second end selected. Count assignments with at most one selected end at each vertex for \(Q\le8\), or one or two selected ends at each vertex for \(8\le Q\le12\). This is an exhaustive \(3^{12}\)-case characterization, producing the displayed thirteen coefficients. The two critical degeneracies are the sums over \(Q=8,\ldots,12\) and \(Q=0,\ldots,8\), respectively.

## Verification
The accompanying standalone scripts implement independent finite checks. `verify_ground.py` checks the general energy formula against *every* spin configuration of the triangle-expanded \(K_4\) (\(4096\) states) and triangular prism (\(262144\) states). It independently counts the cube's constrained partial orientations. `verify_cube_full.cpp` exhausts *all* \(16777216\) spin configurations on the truncated cube via a Gray-code energy update and verifies all \(25\) fixed-magnetization minima and their degeneracies. Both programs were executed and printed `PASS`; full output is provided. These finite calculations check specific graphs and do not establish the theorem for arbitrary graph order: the proof above does.

## Relationship to prior work
Strečka, Karľová and Madaras (2015) established exact magnetization and degeneracies for the five Platonic Ising polyhedra. Their source explicitly restricts the model geometries to those five regular solids and does not contain the triangle expansion of an arbitrary cubic graph or the truncated-cube census. Yu (2015, arXiv manuscript 2016) studied the Ising antiferromagnet on *infinite periodic two-dimensional* Archimedean lattices, including the star (\(3,12,12\)) lattice, with zero-field ground-state entropy but without the asserted all-field, all-graph fixed-magnetization theorem. Barry and Khatun (1995) analyzed Ising correlations of the infinite 3–12 lattice; its publisher abstract was available, but the full text was not inspected. The present exact result may overlap specialized Fisher/star-lattice results not located in this search; priority remains provisional pending independent literature review. The general techniques of classical Ising energy minimization, perfect matchings, and graph decoration are not claimed as new.

## Limitations
The theorem requires equal positive bond strengths on all internal and bridge edges, a perfect matching in the original simple cubic graph, and strictly zero temperature. It does not determine the finite-temperature partition function or every individual zero-temperature correlation. The cube degeneracy table is a finite exact enumeration and is not a thermodynamic-limit residual-entropy estimate. The analytic plateau law is not asserted for arbitrary cubic graphs lacking a perfect matching, nor for Heisenberg or transverse-field variants. Historical originality is assessed only against the material described above and relevant searchable records; no independent audit or priority certification is claimed.

## References
- J. Strečka, K. Karľová, T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449, first public 2015-02-16. https://arxiv.org/abs/1502.04449
- U. Yu, *Ising antiferromagnet on the Archimedean lattices*, Physical Review E 91, 062121 (2015); arXiv:1606.08191, first arXiv 2016-06-27. https://arxiv.org/html/1606.08191v1
- J. H. Barry and M. Khatun, *Exact solutions for Ising-model correlations in the 3-12 (extended kagomé) lattice*, Physical Review B 51, 5840 (1995). https://doi.org/10.1103/PhysRevB.51.5840
- B. D. Metcalf and C. P. Yang, *Degeneracy of antiferromagnetic Ising lattices at critical magnetic field and zero temperature*, Physical Review B 18, 2304 (1978). https://doi.org/10.1103/PhysRevB.18.2304

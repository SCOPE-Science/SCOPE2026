# Complete perfect-edge-domination polynomial of generalized Petersen graphs with inner step three

## Finding
For every integer \(n\ge7\), consider the simple generalized Petersen graph \(G=GP(n,3)\) on vertices \(u_i,v_i\) with edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\) (indices modulo \(n\)). An edge set \(F\) is *perfect edge dominating* if **each edge outside \(F\) shares an endpoint with exactly one edge of \(F\)**. No condition is imposed on edges inside \(F\). The complete cardinality polynomial of these sets is
\[
P_n(z)=\begin{cases}
z^{3n},&5\nmid n,\\
z^{3n}+5z^{3n/5},&n\equiv5\pmod{10},\\
z^{3n}+5z^{3n/5}+20z^{6n/5}+10z^{9n/5},&10\mid n.
\end{cases}
\]
Thus proper perfect edge dominating sets occur precisely when \(5\mid n\). Every such graph has exactly five minimum sets, all of cardinality \(3n/5\), and these five are induced matchings. The additional cardinalities \(6n/5\) and \(9n/5\), with multiplicities twenty and ten, appear exactly when \(10\mid n\).

## Assumptions and scope
Graphs are simple, undirected and labelled as above; \(n\ge7\) ensures the inner step three defines distinct nonduplicated edges. The polynomial counts edge subsets, not edge-set orbits under automorphisms. This is the external-edge definition of perfect edge domination, not the stronger requirement that every edge (including selected edges) be dominated exactly once.

## Proof
**1. A cubic correspondence.** For an arbitrary simple cubic graph \(H\), let \(F\) satisfy the edge condition and let \(d_F(w)\) denote the number of selected edges incident with vertex \(w\). If an unchosen edge has endpoints \(w,t\), its number of adjacent chosen edges is \(d_F(w)+d_F(t)\). A vertex of selected degree two is impossible: its remaining incident edge would meet at least two chosen edges. Thus the possible selected degrees are \(0,1,3\). Any vertex of selected degree zero has all three neighbors of selected degree one; and each selected-degree-one vertex has its two unselected edges joined to selected-degree-zero vertices. Consequently the set \(L\) of degree-zero vertices is independent and every vertex outside \(L\) has zero or two neighbors in \(L\). In other words its indicator \(\mathbf 1_L\) satisfies \(A_H\mathbf 1_L=0\) over \(\mathbb F_2\), in addition to independence.

Conversely, if \(L\) is independent and \(A_H\mathbf 1_L=0\), every vertex outside \(L\) has zero or two neighbors in \(L\), hence selected degree three or one in the edge set induced by \(V(H)\setminus L\). Every unselected edge then has one endpoint in \(L\) and exactly one neighboring selected edge at its other endpoint. This establishes a bijection. As the graph has \(3n\) edges and the independent set \(L\) is incident with exactly \(3|L|\) edges, the corresponding selected edge count is \(3n-3|L|\).

**2. An exact periodicity lemma.** Put \(a_i=\mathbf1_L(u_i)\) and \(b_i=\mathbf1_L(v_i)\) over \(\mathbb F_2\). The adjacency-kernel equations are
\[
a_{i-1}+a_{i+1}+b_i=0,\qquad b_{i-3}+b_{i+3}+a_i=0.
\]
Eliminating \(b_i=a_{i-1}+a_{i+1}\) gives
\[
a_{i-4}+a_{i-2}+a_i+a_{i+2}+a_{i+4}=0.
\]
If \(T\) is the cyclic shift operator, this is \((1+T^2+T^4+T^6+T^8)a=0\) after shifting indices. Multiplication over \(\mathbb F_2\) by \(1+T^2\) gives \((1+T^{10})a=0\) because
\[(1+T^2)(1+T^2+T^4+T^6+T^8)=1+T^{10}.\]
Thus \(a\), and hence \(b\), have period dividing ten. Their pre-existing cyclic period \(n\) reduces them to period dividing \(d=\gcd(n,10)\), one of \(1,2,5,10\). This derivation does not assume an invertibility of the shift or a primitive characteristic root.

**3. Finite complete classification.** For each \(d\in\{1,2,5,10\}\), examine all \(2^d\) binary words \(a_0,\ldots,a_{d-1}\), define \(b_i=a_{i-1}+a_{i+1}\pmod2\), and impose the \(d\) lower adjacency equations together with the three exact independence tests \(a_ia_{i+1}=0\), \(a_ib_i=0\), \(b_ib_{i+3}=0\) for every residue \(i\). Every possible subset is represented exactly once, including patterns whose least period is a proper divisor of \(d\). The exhaustive integer calculation, reproduced by `verify.py`, yields the following exact pairs \((|L|\text{ in a period of }d,\text{number of distinct labelled words})\):
\[
\begin{array}{c|l}d&\text{pairs}\\\hline1&(0,1)\\2&(0,1)\\5&(0,1),(4,5)\\10&(0,1),(4,10),(6,20),(8,5)\end{array}.
\]
The test is a complete finite proof component, not a sample: its source enumerates every one of the \(2^{10}=1024\) possible ten-bit words, with no pruning or randomness. The formula for \(|F|\) above, with each valid pattern repeated \(n/d\) times, now gives the polynomial exactly. When \(d=5\), the five nonzero patterns have \(|L|=4n/5\) and \(|F|=3n/5\). When \(d=10\), the three nonzero classes have \(|L|=2n/5,3n/5,4n/5\), respectively. The size \(3n/5\) instances have selected degree at most one at every vertex, so they are induced matchings. QED.

## Verification
Run `python3 verify.py` with Python standard library. It checks the four complete cyclic-word enumerations, directly reconstructs graph edges and independently tests every admissible independent subset on \(n=7,8,9,10\) against the original external-edge domination definition, and verifies the binary-polynomial identity. Recorded output includes `PERIOD 10 LOW_VERTEX_COUNTS {0: 1, 4: 10, 6: 20, 8: 5}`, `DIRECT_EDGE_DEFINITION 10 {6: 5, 12: 20, 18: 10, 30: 1}` and `VERIFY_OK`. The periodic-word exhaustive certificate proves the unbounded parameter statement; the direct graph enumeration is an independent bounded consistency check.

## Relationship to prior work
Grippo, Lin, Moyano, and Vera (2026, arXiv:2607.03894, first publicly submitted July 4, 2026) study enumeration of perfect edge dominating sets and efficient algorithms for particular graph classes. Their available abstract does not report this size-refined generalized-Petersen formula. The 2025 paper by Grippo, Lin, and Vera addresses algorithmic questions for \(P_6\)-free graphs. Georges, Halsey, Sanaulla, and Whittlesey (1990) study *efficient* (selected-neighborhood-disjoint) edge domination in generalized Petersen graphs, especially existence; that stronger condition concerns the five minimum induced matchings here but does not itself imply counts of the additional thirty *nonmatching* perfect edge dominating sets for \(10\mid n\). The 1990 full text and the 2026 preprint full text were not accessible for comprehensive inspection, so an equivalent earlier formula is a residual priority risk. The new claim is only the full polynomial and its structural arithmetic transition, not a general cubic reduction or the existence of efficient dominating matchings.

## Limitations
The theorem does not count automorphism orbits and does not extend to arbitrary inner step \(k\). The special cubic adjacency-kernel correspondence is elementary and may already occur in the literature; novelty is claimed only for its complete \(GP(n,3)\) cardinality classification. Historical priority and the inaccessible full texts require independent review.

## References
1. L. N. Grippo, M. C. Lin, V. Moyano, C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894 (first public July 4, 2026), https://arxiv.org/abs/2607.03894.
2. L. N. Grippo, M. C. Lin, C. Vera, *Perfect Edge Domination in P6-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598 (2025), https://arxiv.org/abs/2509.04598.
3. J. P. Georges, M. D. Halsey, A. M. Sanaulla, M. A. Whittlesey, *Edge domination and graph structure*, Congressus Numerantium (1990), conference abstract available in the 1990 Florida Atlantic University combinatorics conference program.

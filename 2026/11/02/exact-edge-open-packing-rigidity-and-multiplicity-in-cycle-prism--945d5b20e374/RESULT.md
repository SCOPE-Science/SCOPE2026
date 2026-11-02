# Exact edge-open packing rigidity and multiplicity in cycle prisms

## Finding

For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the prism with two labelled rim cycles and \(n\) labelled rungs. An *edge-open packing* is an edge set containing no two edges \(e,f\) for which a third edge joins an endpoint of \(e\) to a **distinct** endpoint of \(f\). This is the injective-edge-colouring colour-class condition, not the induced-matching condition: an induced star may contribute multiple selected edges.

Write \(\rho_e^o(P_n)\) for the maximum cardinality and \(M_n\) for the number of distinct maximum sets of labelled edges. Then

\[
\rho_e^o(P_n)=\begin{cases}n,&n\equiv0\pmod6,\\n-1,&n\not\equiv0\pmod6,\end{cases}
\qquad
M_n=\begin{cases}6,&n\equiv0\pmod6,\\4n,&n\equiv3,5\pmod6,\\2n,&n\equiv1,2,4\pmod6.\end{cases}
\]

In particular, when the circumference is a multiple of six, the optimum has exactly six phases, while for all other circumferences the deficiency is exactly one and the number of optima is linear.

## Assumptions and scope

Graphs are finite, simple and undirected. Let \(u_i,v_i\), \(i\in\mathbb Z/n\mathbb Z\), be the labelled vertices. The horizontal edges are \(T_i=u_i u_{i+1}\) and \(B_i=v_i v_{i+1}\); rungs are \(R_i=u_i v_i\). The three edges with subscript \(i\) form *column* \(i\). Each edge belongs to exactly one column; there are \(3n\) edges. Every edge subset is regarded as distinct when it differs as a set of labelled edges. The standard edge-open packing definition allows several edges from one induced star.

## Proof

**1. Exact finite-range compatibility.** First suppose \(n\ge4\). Assign column \(i\) a mask \(x_i\in\{0,\ldots,7\}\), using bit values \(1\) for \(T_i\), \(2\) for \(B_i\), and \(4\) for \(R_i\). The forbidden unordered pairs of selected edges have cyclic column separation at most two. Their complete local list (the first type belongs to column \(i\)) is:

- Same column: \((T,B)\).
- From column \(i\) to \(i+1\): \((B,T),(R,B),(R,R),(R,T),(T,B)\).
- From column \(i\) to \(i+2\): \((B,B),(B,R),(T,R),(T,T)\).

Reverse orientation or cyclic index changes give the other descriptions of the same forbidden pairs. This table follows directly by listing third edges that connect distinct endpoints; in particular, adjacent edges in one star are **not** automatically forbidden. Conversely, every third-edge witness uses columns at cyclic separation at most two. Thus the packing condition is equivalent to requiring all cyclic triples \((x_i,x_{i+1},x_{i+2})\) to be among the \(37\) admissible triples obtained from this table. The standalone verifier generates all \(37\) triples directly from the prism's actual edges, independently of the table.

**2. Transfer graph and upper certificate.** Make a directed graph whose vertices are the \(17\) occurring pairs \((a,b)\) of consecutive masks, with an arc \((a,b)\to(b,c)\) for each of the \(37\) admissible triples. Assign the arc weight \(w=\operatorname{popcount}(c)\). Define an integer potential \(\phi(a,b)=1\) on precisely the four states

\[
(0,5),\quad(0,6),\quad(1,5),\quad(2,6),
\]

and \(\phi=0\) on all other states. For **each** of the \(37\) arcs \(p\to q\), exact inspection yields

\[
\delta(p,q):=1+\phi(q)-\phi(p)-w(p,q)\in\{0,1\}.
\]

There are \(24\) zero-slack arcs and \(13\) unit-slack arcs. On a closed walk of length \(n\), potential contributions telescope, so its total selected-edge weight is exactly \(n-s\), where \(s\) is its number of unit-slack arcs. Consequently every edge-open packing has cardinality at most \(n\).

Let \(A\) and \(B\) be the \(17\times17\) integer adjacency matrices of respectively zero-slack and unit-slack arcs, in lexicographic state order. Direct integer matrix multiplication gives the finite certificate

\[
 A^8=A^2.
\]

For lengths \(n=4,5,6,7,8,9\), the exact integer traces are, respectively,

\[
\operatorname{tr}(A^n):\quad 0,0,6,0,0,0,
\]

and

\[
\operatorname{tr}(A^{n-1}B):\quad2,4,6,2,2,4.
\]

The six-step matrix identity implies both trace sequences repeat every six steps for all \(n\ge4\). These statements are finite exact integer identities, reproduced by the accompanying standard-library Python verifier. They are not extrapolations from the first few graph orders.

**3. Exact optimum and multiplicity.** A cyclic mask word corresponds bijectively to a closed walk of length \(n\) in this pair-state graph, with a designated starting column. No slack occurs precisely when the word has \(n\) selected edges. Therefore such words exist exactly for \(6\mid n\); there are then \(\operatorname{tr}(A^n)=6\) of them.

When \(6\nmid n\), every admissible word has positive slack and hence at most \(n-1\) selected edges. For each \(n\ge4\), the positive values of \(\operatorname{tr}(A^{n-1}B)\) above prove existence of a closed walk with exactly one unit-slack arc. Such a word has \(n-1\) edges. Every such word has a **unique** unit-slack position, so the number of optimum words is exactly

\[
 n\,\operatorname{tr}(A^{n-1}B)
 =\begin{cases}4n,&n\equiv3,5\pmod6,\\2n,&n\equiv1,2,4\pmod6.\end{cases}
\]

This completes the theorem for \(n\ge4\).

**4. Triangular prism.** For \(n=3\), direct classification gives exactly \(12\) compatible unordered pairs of edges: each of the three top rim edges can pair with either of its two endpoint rungs, and the same holds for each bottom rim edge. No three selected edges are jointly admissible. Thus \(\rho_e^o(P_3)=2=3-1\) and \(M_3=12=4\cdot3\), completing the universal statement.

## Verification

Run `python3 verify.py` with Python 3.8 or later; it requires no external libraries. The exact replay output is

`VERIFY_OK states=17 triples=37 tight_arcs=24 slack_one_arcs=13 A8_eq_A2=True exact_trace_classes=6 direct_brute_n=3..8`

The program independently constructs prism edge sets and third-edge conflicts, verifies the explicit local forbidden-pair table, enumerates the entire \(37\)-triple transfer, checks every slack inequality, reproduces the matrix identity and residue-class traces, and directly enumerates **all** feasible selected edge subsets for circumferences \(3\) through \(8\). The independent brute-force enumerations yield \((2,12),(3,8),(4,20),(6,6),(6,14),(7,16)\) as (maximum size, optimum count). Finite brute force supports the all-length theorem; the all-length argument comes from the displayed exact matrix identity and potential.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan (2022) introduced edge-open packing and computed the scalar invariant for several standard families, including paths, cycles and the Petersen graph, but not circular ladders. Bhanupriya, Dominic and Sunitha (2023), Theorem 2.20 and Proposition 2.19, determine the **injective edge chromatic index** of cycle prisms; this is a minimum number of colour classes, not the size and multiplicity of a *largest single class*. Their period-six three-colouring case is consistent with, but does not enumerate, the six optimum classes here. Brešar, Dravec, Hedžet and Samadi (2025 preprint 2024), Section 5, provide general Cartesian-product bounds and hypercube results, but their product bounds do not imply the optimum-set multiplicities. Das and Santra (2026) develop algorithms for maximum edge-open packing on selected graph classes without reporting the labelled circular-ladder extremal enumerator. The finite certificate therefore supplies stronger and different information than these previously inspected statements.

## Limitations

The result applies only to labelled circular ladders \(C_n\square K_2\), not to wider cylindrical grids or all generalized Petersen graphs. It counts only largest edge-open packings, not all cardinalities or automorphism orbits. Historical priority is assessed against inspected primary literature and available research records, not independently or exhaustively certified. A general algorithm might be specialised to recover the numbers even though those numbers are not stated in the examined sources.

## References

1. G. K. Das and K. Santra, *Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs*, arXiv:2610.02275, first public version 2026-10-01. https://arxiv.org/abs/2610.02275
2. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching versus edge open packing: Trees and product graphs*, arXiv:2406.04020 (2024); *Discrete Mathematics* 348 (2025), 114458. https://arxiv.org/abs/2406.04020
3. G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, *RAIRO Operations Research* 56 (2022), 3765–3776. https://doi.org/10.1051/ro/2022171
4. C. K. Bhanupriya, C. Dominic and M. S. Sunitha, *Injective edge coloring of product graphs and some complexity results*, *Filomat* 37 (2023), 3963–3983. https://doi.org/10.2298/FIL2312963K

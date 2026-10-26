# Exact extinction basins and six-step entry for four-state Greenberg–Hastings dynamics on bicliques

## Finding
Let \(a,b\ge1\) be integers, and let \(F\) be the synchronous four-state threshold-one Greenberg–Hastings map on the loopless labelled complete bipartite graph \(K_{a,b}\). Let \(U_j(n)=\sum_{h=0}^j(-1)^h\binom jh(j-h)^n\), the number of maps from \(n\) labelled vertices onto a prescribed palette of \(j\) colors. Put \(u_j=U_j(a)\) and \(v_j=U_j(b)\).

**Theorem (complete first-entry census).** For every initial configuration, its first periodic-entry time \(\tau\) is at most six; the only possible eventual periods are one (all resting) and four. The number \(S(a,b)\) of initial configurations that eventually enter a nonzero four-cycle is exactly
\[
S(a,b)=8u_2v_2+10(u_2v_3+u_3v_2)+3(u_2v_4+u_4v_2)+12u_3v_3+4(u_3v_4+u_4v_3)+u_4v_4.
\]
The complementary \(4^{a+b}-S(a,b)\) configurations extinguish to all zero within at most five updates. The bound five is sharp except on \(K_{1,1}\), where it is four. The bound six for first entry into a periodic orbit is sharp precisely when \(\min(a,b)\ge3\) and \(\max(a,b)\ge4\).

More precisely, the associated file `gh4_biclique_depth_table.csv` supplies every coefficient \(h_{e,t,i,j}\) in the complete first-entry census
\[
N_{e,t}(a,b)=\sum_{i=1}^4\sum_{j=1}^4h_{e,t,i,j}U_i(a)U_j(b),
\quad e\in\{\mathrm{extinct},\mathrm{period4}\},\quad 0\le t\le6.
\]
Coefficients not listed in that complete table are zero. Here \(N_{e,t}\) counts labelled initial configurations of eventual type \(e\) whose least time to periodicity is exactly \(t\); therefore the displayed formula is not limited to the final basin totals.

For the balanced family \(a=b=n\ge1\), the exact extinction count is
\[
4^{2n}-S(n,n)=4\cdot9^n+6\cdot8^n-20\cdot6^n+12\cdot4^n+16\cdot3^n-28\cdot2^n+12.
\]
Consequently, under independent uniform initial colors,
\[
\Pr(\mathrm{extinction}\text{ on }K_{n,n})\sim 4(9/16)^n.
\]
The latter is an exact basin-probability exponent, not merely a count of recurrent configurations.

## Assumptions and scope
The four colors are \(0,1,2,3\). Every excited vertex in color \(1\) moves to \(2\), every \(2\) to \(3\), and every \(3\) to \(0\). A resting vertex in color \(0\) moves to \(1\) exactly when at least one adjacent vertex is in color \(1\); otherwise it stays resting. There are no self-loops, vertex labels are retained, and the graph has all cross-part edges and no within-part edges. The result concerns deterministic, parallel, threshold-one dynamics, with neither random forcing nor higher contact thresholds.

The least periodic-entry time is \(\tau(x)=\min\{t\ge0:F^{t+p}(x)=F^t(x)\text{ for some integer }p\ge1\}\). An eventually extinct configuration has type `extinct`; every other one has type `period4`. No assertions are made for arbitrary graphs, other numbers of states, or stochastic dynamics.

## Proof
**1. A finite exact factor.** For any configuration, define its two color supports \(A,B\subseteq\{0,1,2,3\}\), both nonempty. The new support in the left part is obtained by replacing every \(c>0\) by \(c+1\pmod4\) and every occurrence of \(0\) by \(1\) if \(1\in B\), or by \(0\) otherwise. The right support follows the same formula with the parts exchanged. Because each vertex sees the entire opposite part, this support evolution is an exact factor of the labelled system, irrespective of the numbers of vertices of each color. There are exactly \((2^4-1)^2=225\) possible pairs of nonempty supports.

**2. Exhaustive finite transition certificate.** Enumerate all 225 support pairs under the explicitly defined transition, recording the first repeated pair, its cycle, and its transient length. There are exactly three support cycles: the fixed pair \((\{0\},\{0\})\); the fixed pair \((\{0,1,2,3\},\{0,1,2,3\})\); and the two-cycle between \((\{0,2\},\{1,3\})\) and \((\{1,3\},\{0,2\})\). Their support-pair basins have sizes 170, 1, and 54 respectively, with maximal first-entry depths five, zero, and six. These are complete exhaustive finite statements, not empirical estimates: the standalone verifier `gh4_biclique_verify.py` constructs the entire transition function and checks every support pair, as well as the exact 80-row coefficient table. The displayed table gives a compact full certificate of the enumeration, and the short source code is part of the proof specification.

**3. Recovering the labelled dynamics.** If support enters the all-zero fixed pair, every site is exactly zero then. In either nonzero recurrent support class, each side contains color \(1\) whenever a color \(0\) occurs on the opposite side. Therefore *every* site changes by addition of \(1\) modulo four at every subsequent step. Its labelled configuration has exact period four. Conversely, a labelled configuration cannot become periodic before its supports are periodic. Hence its exact first-periodic-entry time equals the support-pair first-entry time, and the finite factor controls the complete labelled temporal classification. This also proves the global bounds, and supports of sizes \((3,4)\) or \((4,3)\) reach the two-cycle at depth six; the indicated sizes yield exactly the sharpness criterion. An extinction-basin support pair of sizes \((1,2)\) reaches zero at depth five, proving sharpness whenever \(\max(a,b)\ge2\); on \(K_{1,1}\) the largest depth is four.

**4. Lifting coefficients to all sizes.** An initial left support of cardinality \(i\) has exactly \(U_i(a)\) realizations on its labelled shore; similarly an initial right support of cardinality \(j\) has \(U_j(b)\). For a fixed support pair these factors multiply. Grouping the finite census of all 225 pairs by eventual type, transient depth, and ordered support cardinalities produces exactly the recorded \(h_{e,t,i,j}\) and the displayed complete-depth formula. Summing its nonextinguishing rows gives the survival coefficient matrix, indexed by \(i,j\in\{2,3,4\}\):
\[
\begin{pmatrix}8&10&3\\10&12&4\\3&4&1\end{pmatrix}.
\]
This proves the exact basin expression. For \(a=b=n\), substitution of \(U_2(n)=2^n-2\), \(U_3(n)=3^n-3\cdot2^n+3\) and \(U_4(n)=4^n-4\cdot3^n+6\cdot2^n-4\), followed by collecting powers, yields the seven-term extinction formula. Since \(9>8,6,4,3,2,1\), dividing by \(16^n\) yields the stated asymptotic.

## Verification
The self-contained script `gh4_biclique_verify.py` exhausts the 225 support pairs, reconstructs the coefficient table, evaluates its lifted polynomials, and independently simulates every labelled initial state for \(1\le a,b\le4\). This is 115,600 direct configurations across 16 graphs. It checks the exact future period, entry time, final extinction or survival and periodic-at-time-zero census. It also compares the finite support sum with the displayed survival polynomial for all \(1\le a,b\le6\) and verifies the seven-term balanced identity exactly through \(n=30\). Its recorded output is `gh4_biclique_verify.out`.

## Relationship to prior work
Fisch, Gravner and Griffeath established the multicolor Greenberg–Hastings rule and analyzed lattice waves and stable periodic objects [1]. Their article treats lattice-scale thresholds and patterns, rather than the exact labelled extinction basin of a four-state complete bipartite graph. Durrett and Griffeath provide historical multitype excitable-model analysis on lattices [2]. Doba's finite-graph theory [3] addresses **three** states, not four.

Previously established complete-biclique results include a general number-of-colors classification of *periodic* Greenberg–Hastings configurations and a full first-entry census for the three-state rule [4]. Thus the four-state recurrent-period list or recurrent-state count **is not claimed as new** here. What is proved beyond those statements is the four-state basin enumeration from **arbitrary transient states**, the full first-entry distribution for both eventual types, a sharp six-update cutoff, and the balanced extinction exponent \(9/16\). The four-color cyclic cellular automaton [5] is also a different local rule: every color in that model requires a neighboring successor before moving, whereas three of the four colors advance automatically here.

## Limitations
The 225-pair finite classification and its lift are exact mathematical proofs for this specified graph family, but do not imply novelty across unindexed papers or other graph families. The 1995 Fisch–Gravner article [6] was inspected in full text: its one-dimensional spatial asymptotics do not supply a complete-bipartite all-state first-entry table; unindexed equivalents remain possible. The closest accessible general result [4] subsumes the recurrent-state portion, which is explicitly excluded from the originality claim. No independent audit has yet been performed. This analysis does not establish any new result for stochastic activation, graph perturbations, or five or more color states.

## References
[1] R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39. https://math.ucdavis.edu/~gravner/papers/fgg.pdf

[2] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first public 1993-03-22. https://arxiv.org/abs/patt-sol/9303002

[3] N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126. https://doi.org/10.25088/ComplexSystems.27.2.101

[4] Prior mathematical research record, *Parity-selective periodic excitation on complete bipartite graphs*, identifier `54f87932-6e9f-408d-9197-a829b84e91d9`, and *A four-step relaxation law and complete orbit-depth census for bipartite excitable dynamics*, identifier `3a7e2d67-1cfb-4a1f-bec4-e4a1b10d0275`.

[5] Prior mathematical research record, *A complete fixed-, four-, and six-cycle census for four-color cyclic competition on bicliques*, identifier `16b5edf9-fbe6-41da-99cc-cdcdcce676a3`.

[6] R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348. https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf

# Exact four-state excitation orbits and basins on complete bipartite graphs

## Finding
For every pair of integers \(a,b\ge2\), synchronous, threshold-one, four-state Greenberg–Hastings dynamics on the labelled complete bipartite graph \(K_{a,b}\) has exactly one fixed state (all vertices in state zero). Every other periodic state has **least period four**. Put
\[
U_j(n)=\sum_{r=0}^{j}(-1)^r\binom jr(j-r)^n\qquad(1\le j\le4).
\]
Then its exact number of primitive temporal four-cycle **orbits** is
\[
Q_4(a,b)=\frac{U_4(a)U_4(b)+2U_2(a)U_2(b)}4.
\]
The number \(B_4(a,b)\) of all labelled initial states eventually entering a four-cycle is
\[
\begin{aligned}
B_4(a,b)={}&U_4(a)U_4(b)+8U_2(a)U_2(b)\\
&+10[U_2(a)U_3(b)+U_3(a)U_2(b)]\\
&+3[U_2(a)U_4(b)+U_4(a)U_2(b)]\\
&+12U_3(a)U_3(b)\\
&+4[U_3(a)U_4(b)+U_4(a)U_3(b)].
\end{aligned}
\]
The remaining \(4^{a+b}-B_4(a,b)\) initial states reach the all-zero fixed configuration. Writing \(\tau(x)\) for the smallest nonnegative number of updates after which the actual labelled state is periodic, the sharp maximal transient is
\[
\max_x\tau(x)=
\begin{cases}
6,&\min(a,b)\ge3\text{ and }\max(a,b)\ge4,\\
5,&\text{otherwise, for }a,b\ge2.
\end{cases}
\]
For instance \(K_{3,3}\) has \(1,440\) initial states in four-cycle basins versus \(2,656\) in the fixed basin, whereas \(K_{4,4}\) has \(36,704\) in four-cycle basins versus \(28,832\) in the fixed basin. Moreover \(B_4(a,b)/4^{a+b}\to1\) if both part sizes tend to infinity.

## Assumptions and scope
The graph \(K_{a,b}\) is simple, undirected, and has two labelled vertex shores of respective sizes \(a,b\ge2\). Each vertex holds one of \(\{0,1,2,3\}\). At each simultaneous update, state \(0\) becomes \(1\) iff **at least one** vertex in the opposite shore has state \(1\), remaining \(0\) otherwise; state \(1\to2\), state \(2\to3\), and state \(3\to0\) unconditionally. In particular the vertex itself is not counted as a neighbor and there is no randomness. Basins count **labelled microscopic configurations**, not support pairs or orbits. All periods are least positive temporal periods. These rules are not three-state excitation or four-color cyclic successor-contact dynamics.

## Proof
**1. Exact 225-state support quotient.** For any configuration, let its left and right occupied-color masks be \((L,R)\) with \(L,R\in\{1,\ldots,15\}\), each mask's bit numbered by its color. The one-step image of a mask \(M\), given the opposite mask \(N\), is
\[
\Phi(M,N)=\{(c+1)\bmod4:c\in M\setminus\{0\}\}
\cup\begin{cases}\{1\},&0\in M,\ 1\in N,\\\{0\},&0\in M,\ 1\notin N,\\\varnothing,&0\notin M.\end{cases}
\]
Here sets of colors and binary masks are interchangeable. Thus the exact quotient transition is \((L,R)\mapsto(\Phi(L,R),\Phi(R,L))\), independent of \(a,b\) apart from which masks are initially realizable.

**2. A complete finite certificate, not sampled trajectories.** The included `support_table.csv` explicitly gives the image, first-entry tail and terminal support class of **all 225** pairs of nonempty masks. For replay, `verify.py` computes each transition by the local rule, follows every support orbit until a repeat and verifies that the only recurrent support cycles are (i) fixed \((1,1)\); (ii) alternating \((5,10)\leftrightarrow(10,5)\); (iii) fixed \((15,15)\). The maximum first entry into these support classes is six. Every support pair enters one of them; the table lists the exact entry time. This exhausts all possible supports, not a bounded sample of graph sizes.

**3. From supports to actual microscopic periods.** The recurrent support \((1,1)\) contains only the all-zero configuration, which is fixed. On support \((15,15)\), every vertex increases its color by one modulo four at every update; all microscopic configurations are periodic of least period four. On alternating supports, one shore occupies colors \(\{0,2\}\), the other \(\{1,3\}\), and the subsequent support swaps these sets. In each shore the zero-to-one transition is enabled whenever a zero is present, so again **every vertex rotates through all four states**. Consequently every microscopic configuration on either recurrent four-cycle support is periodic of least period four, and its first microscopic periodic-entry time equals the first support entry time in the certificate. No fixed, two-, or three-cycles have been omitted.

**4. Exact counting of recurrent points and basins.** The inclusion–exclusion value \(U_j(n)\) counts surjections of the \(n\) labelled vertices onto any prescribed set of \(j\) colors. There is one all-zero periodic state. The alternating support cycle consists of two ordered pairs of masks, each requiring two colors on each shore, for \(2U_2(a)U_2(b)\) periodic microscopic states. The full-color recurrent support contributes \(U_4(a)U_4(b)\) more states. All are four-periodic, so division by four proves \(Q_4\).

To count full basins, group **initial** support pairs by their occupied-color cardinalities. The 225-row exhaustive certificate reports exactly the following cardinality-class multiplicities attracted to alternating support: \((2,2):8\), \((2,3):10\), \((3,2):10\), \((2,4):3\), \((4,2):3\), \((3,3):12\), \((3,4):4\), \((4,3):4\). The full-support attractor has only initial mask pair \((15,15)\), and all other \(170\) mask pairs enter \((1,1)\). Multiplication by \(U_i(a)U_j(b)\) and summation gives the displayed formula for \(B_4\), without overcounting: every initial configuration has a unique support pair. The complementary fixed-basin formula follows by partitioning all \(4^{a+b}\) microscopic states.

**5. Sharp transients.** The support certificate's six-step cases include \((11,15)\) and its shore transpose, requiring at least three vertices on one shore and at least four on the other. Inspecting every 225 rows in the supplied table shows *every* six-step case has one mask of cardinality at least three and the other of cardinality four; hence these size conditions are necessary. The two explicit six-step supports establish sufficiency. If the size condition fails and \(a,b\ge2\), the table gives maximal feasible depth exactly five; this is also asserted directly in `verify.py` for all distinct possible mask-capacity regimes, each determined by truncating a shore's size at four.

Finally, \(U_4(n)/4^n\to1\) by the union bound on missing any of four colors, so \(B_4(a,b)\ge U_4(a)U_4(b)\) implies \(B_4(a,b)/4^{a+b}\to1\) jointly as \(a,b\to\infty\).

## Verification
Run `python3 verify.py` from a directory containing the included files. It enumerates all 225 quotient states, independently detects every support cycle, verifies all cardinality-class coefficients, exhaustively checks \(115,600\) **labelled** microscopic configurations over the \(16\) ordered shore-size pairs from one through four, and crosschecks the basin/orbit formulas and sharp transient regime on all \(36\) ordered pairs with sizes between two and seven. `verification_output.txt` records the reproduced output. `support_table.csv` supplies the exhaustive 225-row transition certificate. The finite checks certify the finite support reduction; they are not extrapolated as direct enumeration of all large graphs.

## Relationship to prior work
Gravner, Lyu and Sivakoff (public preprint October 24, 2016) formulate general finite-state Greenberg–Hastings excitation but concentrate on three-color dynamics, using covering-space comparison rather than an exact four-state complete-bipartite recurrent-orbit/basin census. Doba (2018) analyzes finite graphs for the **three-valued** excitation rule and gives convergence criteria, not this four-valued labelled biclique count. An earlier complete-tripartite four-state census assumes **all three shore sizes are positive**, so does not logically imply the two-shore formula or its sharp five-versus-six transient boundary: deleting the entire third shore changes the local neighborhoods. The three-state biclique census likewise concerns a different state alphabet. No claim of general discovery of the Greenberg–Hastings rule, period-four phenomenon or support-quotient method is made here.

## Limitations
The theorem assumes deterministic synchronous updates, four states, threshold one and exactly two nonempty complete shores. It neither asserts the same formulas for more general graphs nor supplies a complete transient-by-time distribution. The finite certificate has only 225 rows and can be audited exhaustively; separate labelled-state tests corroborate but do not substitute for the quotient proof. Historical mathematical priority remains provisional because unindexed or inaccessible work might contain an equivalent all-size four-state biclique census. No independent external audit has been performed.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first publicly submitted 2016-10-24, https://arxiv.org/abs/1610.07320 .
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf .
3. J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523.

# A parity fracture in synchronous majority dynamics on crown graphs

## Finding

For every integer \(n\ge1\), let \(\operatorname{Cr}_n=K_{n,n}\setminus M\), where \(M\) is a fixed perfect matching between labelled shores \(L=\{\ell_1,\ldots,\ell_n\}\) and \(R=\{r_1,\ldots,r_n\}\). Under synchronous binary strict-neighbor majority with retention on ties, let \(F_n\) be the update map. An initial configuration has **first periodic-entry time** \(T\) when \(F_n^{T+p}(x)=F_n^T(x)\) for some positive period \(p\) and no smaller nonnegative \(T\); its eventual least period is the smallest such \(p\).

Write \(C_n=\binom{n}{\lfloor n/2\rfloor}\) and \(B_n\) for the number of the \(4^n\) labelled configurations eventually entering a *primitive* two-cycle. The only possible eventual least periods are \(1\) and \(2\) for every \(n\ge2\); both occur. Precisely:

**Even shores:** If \(n=2m\ge2\), put \(H=\sum_{j=0}^{m-1}\binom nj=(2^n-C_n)/2\). The fixed-state number, primitive two-cycle *orbit* number, and two-cycle basin size are respectively
\[
P_1=2+C_n,\qquad N_2=\frac{(C_n+1)(C_n+2)}2,\qquad B_n=2H^2+4HC_n+C_n^2-C_n.
\]
The sharp worst-case first periodic-entry time is \(0\) at \(n=2\), and \(1\) for every even \(n\ge4\).

**Odd shores:** The graph at \(n=1\) consists of two isolated vertices and all four states are fixed, so \(B_1=0\). If \(n=2m+1\ge3\), then
\[
P_1=2+2(m+2)C_n,\qquad N_2=1,\qquad
B_n=2^{2n-1}-2C_n\bigl(2(m+2)2^m-(m^2+3m+3)\bigr).
\]
The unique primitive two-cycle consists of the two opposing unanimous shore configurations \((0^n,1^n)\) and \((1^n,0^n)\). The sharp worst-case first periodic-entry time equals \(2\) at \(n=3\) and \(3\) for every odd \(n\ge5\).

Consequently \(F_n^3=F_n\) for every even \(n\ge2\), whereas \(F_n^5=F_n^3\) for every odd \(n\ge3\) (both uniform iterate identities, including transient states). With uniformly random independent initial bits, the chance to enter a primitive two-cycle has contrasting limiting approaches:
\[
\frac{B_{2m}}{4^{2m}}=\frac12+\frac1{\sqrt{\pi m}}+O(m^{-1}),\qquad
\frac{B_{2m+1}}{4^{2m+1}}=\frac12-2\sqrt{\frac m\pi}\,2^{-m}(1+o(1)).
\]
Thus the even-shore graph has exponentially many primitive two-cycles and a basin probability approaching one-half at square-root rate, whereas the odd-shore graph has exactly one such cycle yet a basin covering asymptotically half its states, approaching one-half exponentially fast.

## Assumptions and scope

The graph is simple, loopless, and labelled, and every \(\ell_i\) is adjacent to exactly the vertices \(r_j\) with \(j\ne i\). Opinions are the symbols \(0\) and \(1\). A vertex updates to \(1\) when strictly more than half of its \(n-1\) neighbors hold \(1\), to \(0\) when strictly fewer than half do, and retains its current bit at equality. The update is simultaneous at all \(2n\) vertices. Counts use fixed labelled vertex positions; a cycle is an orbit modulo temporal rotation, not graph automorphisms. The result concerns this precise tie rule, not randomized, self-inclusive, or asynchronous variants.

Represent a configuration by paired bit vectors \(A=(a_i)\) on \(L\) and \(B=(b_i)\) on \(R\); write \(s_A=\sum_i a_i\), \(s_B=\sum_i b_i\). Complements of vectors are written \(\neg A\); union and intersection are coordinatewise OR and AND. The two cycle phases \((0^n,1^n)\) and \((1^n,0^n)\) remain distinct labelled states, counted as one orbit.

## Proof

**Exact neighbor rule.** The left vertex \(\ell_i\) sees \(s_B-b_i\) occupied neighbors; the right vertex \(r_i\) sees \(s_A-a_i\). Its degree is \(n-1\). This is an exact expression, not a probabilistic or mean-field approximation.

**Even case.** Put \(n=2m\) and let \(0^n\) and \(1^n\) denote constant vectors. The degree is odd, so no ties arise. The update of one shore when the opposite shore is \(X\), with \(s=\sum X_i\), is \(0^n\) if \(s<m\), \(1^n\) if \(s>m\), and \(\neg X\) if \(s=m\). Therefore:

* If both initial shore populations lie strictly on the same side of \(m\), the next state is unanimous and fixed. If they lie on opposite strict sides, the next state is one of the two phases \((0^n,1^n)\), \((1^n,0^n)\).
* If exactly one shore has population \(m\), the first iterate is on a two-cycle, since the balanced pattern alternates with its complement while the opposite shore alternates between unanimous states.
* If both shores have population \(m\), the update is \((A,B)\mapsto(\neg B,\neg A)\), an involution. A fixed state in this subspace requires \(A=\neg B\).

This proves the \(F_n^3=F_n\) identity, the period restriction and the counts. There are \(C_n\) balanced complementary fixed states plus the two unanimities. Primitive period-two *states* are the \(C_n^2-C_n\) nonfixed double-balanced states, the \(4C_n\) states with one balanced and one unanimous shore, and the two opposing unanimous states, totaling \((C_n+1)(C_n+2)\). Every two-cycle orbit has two states. The two-cycle basin consists of opposite strict populations (\(2H^2\) states), configurations with exactly one balanced shore (\(4HC_n\)), and both balanced except complementary fixed pairs (\(C_n^2-C_n\)). For \(m=1\), the crown is a disjoint union of two edges and the map is already an involution. For \(m\ge2\), the configuration with all zeros on one shore and a single one on the other reaches a fixed state after exactly one update.

**Odd case: complete six-case reduction.** Put \(n=2m+1\) with \(m\ge1\). Classify a shore by its total population: \(L\) for \(s<m\), \(U\) for \(s=m\), \(V\) for \(s=m+1\), and \(H\) for \(s>m+1\). If opposite-shore vector \(X\) has occupancy \(s\), its contribution to the new shore vector \(Y\) is: constant \(0^n\) for \(L\), \(Y\wedge\neg X\) for \(U\), \(Y\vee\neg X\) for \(V\), and constant \(1^n\) for \(H\). Here \(Y\) is the shore's old vector. This formula includes retention at exact ties.

Swapping the two shores and complementing all bits commute with the update; these symmetries reduce all \(16\) pairs of population classes to the following six representatives. Let \(d=\#\{i:a_i=b_i=1\}\).

1. \((L,L)\): in one step both shores are all zero and remain fixed.
2. \((L,H)\): in one step the shores are unanimously opposed and hence form a primitive two-cycle.
3. \((L,U)\): after one step, one shore is zero and the other has at most \(m-1\) ones; the following step reaches all zero.
4. \((L,V)\): after one step the state is \((A\vee\neg B,0^n)\), with left count \(m+d\). If \(d=0\), unanimity zero follows at time two; if \(d=1\), unanimity zero follows at time three; if \(d\ge2\), the opposing unanimous two-cycle is entered at time two.
5. \((U,U)\): the first step removes every coincident pair of ones, leaving both shore counts \(m-d\). If \(d=0\), the initial state is fixed; if \(d\ge1\), the state becomes all zero by time two.
6. \((U,V)\): the first step makes all matched pairs complementary, with new shore counts \(m+d\) and \(m+1-d\). For \(d=0\) or \(d=1\) the first iterate is fixed; for \(d\ge2\) the opposing unanimous two-cycle is entered at time two.

The six representatives and their images under the two symmetries exhaust the possible states. Every orbit is fixed or enters the single opposing unanimous two-cycle by time three, which proves \(F_n^5=F_n^3\). At \(n=3\), no \((L,V)\) configuration can have \(d=1\), so the bound drops to two; \((U,U)\) with \(d=1\) attains two. For every \(m\ge2\), choose a \((L,V)\) state with one initial occupied left vertex and with that vertex among the \(m+1\) occupied right positions: \(d=1\) attains three. At \(n=1\) there are no edges and all states are fixed.

**Odd fixed-state count.** Besides the two unanimous states, a fixed state must have shore totals \((m,m)\), \((m+1,m+1)\), \((m,m+1)\), or \((m+1,m)\). In the first category there may be no matched pair with two ones; the second forbids matched pairs with two zeros. Each has \(n!/(m!m!)=(m+1)C_n\) states. The last two categories require complementary bits in each matched pair, and each has \(C_n\) states. Summing gives \(2+2(m+2)C_n\). No other initial state is recurrent except the single unanimous-opposition two-cycle.

**Odd attraction-basin count.** Let \(H_0=\sum_{j=0}^{m-1}\binom nj=2^{n-1}-C_n\). The opposite extreme classes \((L,H)\) and \((H,L)\) contribute \(2H_0^2\) basin states. The four symmetry-related classes \((L,V)\), \((V,L)\), \((U,H)\), \((H,U)\) contribute four times the number \(Q\) of \((L,V)\) states with matched overlap \(d\ge2\). The two classes \((U,V)\), \((V,U)\) contribute twice the number \(R\) of \((U,V)\) states with \(d\ge2\).

Count their complementary obstructions \(Q_{\le1}\) and \(R_{\le1}\): fixing the \(m+1\) occupied right vertices gives
\[
Q_{\le1}=C_n\left[(2^m-1)+(m+1)(2^m-m-1)\right]
=C_n\left[(m+2)2^m-m^2-2m-2\right],
\]
and fixing one central occupied shore gives
\[
R_{\le1}=C_n\left[1+m(m+1)\right].
\]
Since \(Q=H_0C_n-Q_{\le1}\) and \(R=C_n^2-R_{\le1}\), the total is
\[
B_n=2H_0^2+4Q+2R
=2(H_0+C_n)^2-4Q_{\le1}-2R_{\le1}
=2^{2n-1}-2C_n\left[2(m+2)2^m-(m^2+3m+3)\right].
\]

**Asymptotic inversion.** Stirling's formula gives \(\binom{2m}{m}/2^{2m}=1/\sqrt{\pi m}+O(m^{-3/2})\) and \(\binom{2m+1}{m}\sim2^{2m+1}/\sqrt{\pi m}\). Substitution into the exact basin counts proves the two displayed asymptotic laws. In particular the odd deficit is dominated by the \(4C_n(m+2)2^m\) term; the lower-order polynomial multiple of \(C_n\) is exponentially smaller relative to that term.

## Verification

The standalone program `verify_majority_crown.py` implements the two exact formulas and performs two different finite checks. First, it follows *all four initial matched-pair categories separately*, with multinomial weights for every nonnegative four-part composition of \(n\). This preserves microscopic periods even when aggregate pair populations repeat. It verifies every count and sharp transient for all \(1\le n\le50\). Second, an independent explicit-neighborhood simulator enumerates every labelled state for \(1\le n\le7\) and compares the resulting periods, basin counts and maximum transients. The recorded output ends with `CROWN_MAJORITY_PARITY_VERIFY_OK`. These finite checks supplement, and do not substitute for, the preceding infinite-family case proof.

For illustration, at \(n=5\) there are \(82\) fixed states, one primitive two-cycle orbit and \(132\) initial states in its basin; at \(n=6\) there are \(22\) fixed states, \(231\) primitive two-cycle orbits and \(3108\) initial basin states. All counts distinguish labelled configurations from temporal orbits.

## Relationship to prior work

Goles and Olivos (1980) prove the general fixed-or-two-cycle eventual-period restriction for finite symmetric threshold dynamics. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, 2014) review that theorem and study infinite transitive and random graphs; their finite-graph background does not give the crown-graph census. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, 2015) establish general voting-time bounds through graph modules and an \(O(r^2)\) consequence for Turán graphs; the inspected theorem and applications do not give the sharp parity-dependent \(0/1/2/3\) cutoff, the primitive orbit counts or the exact two-cycle basin law for crown graphs. Crown graphs are not the same as complete multipartite graphs: deleting the matching makes each paired exclusion decisive at a tied local majority.

The exact parity discontinuity between one and exponentially many primitive oscillations, together with the distinct polynomial and exponential rates of basin-probability convergence, is the asserted contribution. A general period-two theorem alone cannot determine these invariants; similarly a bound on convergence time cannot imply the exact orbit/basin populations.

## Limitations

The theorem uses retention on ties, strict neighbor majority, labelled matching pairs, and synchronous updates; changing any of these may change the formulas. The sharp small cases \(n=1,2,3\) are stated separately. The asymptotic probability concerns unbiased independent initial bits only. No claim is made about distinct dynamical systems or arbitrary bipartite graphs. Originality was checked against accessible records and relevant primary literature, but an unindexed equivalent historical treatment remains possible. Independent expert validation has not been performed.

## References

1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* **30** (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1, first public version 2014-05-11.
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, “On the Voting Time of the Deterministic Majority Process,” arXiv:1508.03519v1, first public version 2015-08-14.

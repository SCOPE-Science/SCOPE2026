# A factorial ordinal potential and equilibrium census for diversity jumps with arbitrary vacancies on complete bipartite graphs

## Finding
For any complete bipartite graph \(K_{A,B}\), with integers \(A,B\ge2\), any \(1\le q\le A+B-2\) vacant vertices and any finite set of agent types, fractional diversity-seeking jumps have a strictly increasing ordinal potential. Thus *every* sequence of strictly improving unilateral jumps terminates. For two types, equilibria admit a complete structural characterization and an exact red-population enumerator for every \(A,B,q\). An immediate consequence is that, for each fixed positive \(q\), the equilibrium fraction on \(K_{m,m}\) is \(2^{2-q-m}(1+o(1))\) as \(m\to\infty\). These claims are a single package about the multi-vacancy game; the single-vacancy case is included for consistency but is not claimed as new.

## Assumptions and scope
The vertices of \(K_{A,B}\) are labeled. One part has \(A\) vertices and the other \(B\) vertices, each without internal edges; all cross-part edges are present. Each of the \(A+B-q\ge2\) occupants has one of \(k\ge2\) fixed types, all occupants are strategic, and each vertex holds at most one occupant. The number of vacancies is conserved. An occupant may relocate to any vacant vertex. Its utility is the fraction of its occupied neighbors belonging to types different from its own; if it has no occupied neighbors, its utility is \(0\). A jump is improving only when this utility **strictly increases**. Intrapart jumps are never strictly improving because their open neighborhoods are identical.

Let \(n_{S,t}\) be the number of type-\(t\) occupants in part \(S\in\{L,R\}\), and \(n_S=\sum_{t=1}^k n_{S,t}\). Put \(N=A+B\), \(Q=N+1\), \(h(0)=Q\) and \(h(j)=(j-1)!\) for every integer \(j\ge1\). Define the positive rational-valued function
\[
\Phi(C)=\prod_{S\in\{L,R\}}\frac{\prod_{t=1}^{k}h(n_{S,t})}{h(n_S)}.
\]

For the equilibrium census specialize to two distinguishable types, red and blue. Let \(E_{A,B,q}(z)\) count stable assignments by number of red occupants, including labeled vacancy locations. Set \(n=N-q\) and use the convention \(\binom uv=0\) unless \(0\le v\le u\), with each term involving \((1+z)^{M-q}\) included **only** when \(q\le M\). Then
\[
\begin{aligned}
E_{A,B,q}(z)={}&\binom Nq(1+z^n)\\
&+\mathbf1_{q\le B}\binom Bq\big[(1+z^A)(1+z)^{B-q}-1-z^n\big]\\
&+\mathbf1_{q\le A}\binom Aq\big[(1+z^B)(1+z)^{A-q}-1-z^n\big]\\
&+\sum_{\substack{1\le e<A\\1\le q-e<B}}\binom Ae\binom B{q-e}\big(z^{A-e}+z^{B-q+e}\big).
\end{aligned}
\]
Here the two indicators mean that the entire second or third term is omitted when its displayed inequality fails; no negative-power polynomial is meant.

**Equilibrium classification.** A two-color assignment is stable exactly in one of these disjoint classes: (i) it is globally monochromatic; (ii) all vacancies lie in just one part and the completely occupied *other* part is monochromatic, but the assignment is not globally monochromatic; (iii) both parts contain at least one vacancy and at least one occupant, and each occupied part is monochromatic with **opposite** colors. The convention in (ii) excludes the globally monochromatic configurations already counted in (i).

## Proof
**Strict ordinal potential.** Consider a cross-part jump of type \(t\) from a source with \(a\) occupants including \(c\) of type \(t\) to a destination containing \(b\) occupants including \(d\) of type \(t\), before the jump. A strict improvement requires \(a\ge2\); otherwise the destination has no occupied neighbors after the jump and utility cannot increase. When \(b\ge1\), the original and new utilities are
\[
u_{\mathrm{old}}=1-\frac d b,\qquad u_{\mathrm{new}}=1-\frac{c-1}{a-1}.
\]
Strict improvement is equivalent to \(d/b>(c-1)/(a-1)\); this forces \(d\ge1\). If \(c\ge2\), the factorial ratios give
\[
\frac{\Phi(C')}{\Phi(C)}=\frac{(a-1)d}{(c-1)b}>1.
\]
If \(c=1\), the factor crossing the zero-count boundary gives
\[
\frac{\Phi(C')}{\Phi(C)}=\frac{Q(a-1)d}{b}>1,
\]
because \(Q=N+1>b\).

When \(b=0\), old utility is zero and new utility is \((a-c)/(a-1)\), so improvement requires \(c<a\). The destination's type and total factors cancel exactly. If \(c\ge2\),
\[
\frac{\Phi(C')}{\Phi(C)}=\frac{a-1}{c-1}>1;
\]
if \(c=1\), this ratio is \(Q(a-1)>1\). There are no additional strictly improving moves: jumps within one part preserve utility, and a source with \(a=1\) offers new utility zero. Every strict jump increases the displayed positive rational potential. There are only finitely many placements (at most \(\binom Nq k^n\) with labeled vertices and a fixed number of occupants), so improvement paths cannot repeat and terminate in at most \(\binom Nq k^n-1\) jumps.

**Classification.** First, if a part with \(a\ge2\) occupants contains both colors and the opposite part has a vacancy, there is an improving jump to that vacancy. If the opposite part is empty, any agent on the mixed part sees a different color after moving and improves from zero. Otherwise write \(r\) for red occupants of the mixed source, \(a-r\) for blue, and \(d\) for red occupants among the \(b\ge1\) occupants of the opposite part. If neither color could improve by jumping across, the utility-comparison inequalities would require simultaneously
\[
\frac db\le\frac{r-1}{a-1},\qquad
1-\frac db\le\frac{a-r-1}{a-1}.
\]
Adding gives \(1\le(a-2)/(a-1)<1\), a contradiction. Thus every occupied mixed part *opposite a vacancy* is unstable.

If all vacancies are in one part, its completely occupied opposite part must therefore be monochromatic. This condition is sufficient: the only cross-part jumps into vacant sites originate in the monochromatic full part, and after any such jump the mover has utility zero, no better than before. If both parts have vacancies, neither occupied part can be mixed. If both contain occupants, opposite monochromatic colors give each occupant utility one and hence stability, whereas equal colors are globally monochromatic. If one occupied part is empty, stability forces the other to be monochromatic; these are already globally monochromatic. A globally monochromatic assignment has utility zero everywhere and no move can create neighbors of a different type. This proves the classification with all occupancy boundary cases.

**Enumerator.** There are \(\binom Nq\) ways to mark vacancies in a global monochromatic assignment and exactly one red count of \(0\) or \(n\), giving the first term. If the first part is full (so vacancies all lie in the second), it must be red or blue. Choose the \(q\) vacancies of the second part in \(\binom Bq\) ways; its remaining occupants contribute \((1+z)^{B-q}\). Choosing the color of the full first part contributes \(1+z^A\), and deleting the globally monochromatic cases gives the second term. Exchanging the parts gives the third term. Finally, when there are \(e\) vacancies in the first part and \(q-e\) in the second, with both parts occupied and vacant, choose the vacancies in \(\binom Ae\binom B{q-e}\) ways and assign opposite pure colors to the parts, yielding the two monomials of the last term. All cases are disjoint and exhaustive.

**Asymptotic.** For fixed \(q\ge1\) and \(A=B=m>q\), evaluating at \(z=1\) yields
\[
E_{m,m,q}(1)=2\binom{2m}q+2\binom mq(2^{m-q+1}-2)
+2\sum_{e=1}^{q-1}\binom me\binom m{q-e}.
\]
The last sum is polynomial in \(m\) for fixed \(q\), while the second summand dominates exponentially. Divide by the total number \(\binom{2m}q2^{2m-q}\) of vacancy-marked binary assignments and use \(\binom mq/\binom{2m}q\to2^{-q}\). The claimed \(2^{2-q-m}(1+o(1))\) follows.

## Verification
The standalone `verify.py` computes every player's utility directly from labeled adjacency data and independently evaluates \(\Phi\) with exact integer factorials and rational arithmetic. It checks all strictly improving *cross-part* jumps (same-part jumps have identically unchanged utility) on every admissible two-color state of \(K_{A,B}\) for \(2\le A,B\le5\), and compares each equilibrium red-count polynomial to direct enumeration. It also checks four further three-/four-type parameter families. Its completed run reported: **125760 two-color configurations; 80 exact equilibrium polynomials; 18965 three-/four-type configurations; 508416 strictly improving cross-part moves; no discrepancy**. These are finite checks only; the preceding algebra supplies the universal proof.

For \(K_{3,5}\) with \(q=2\), the enumerator is
\[
28+33z+45z^2+20z^3+45z^4+33z^5+28z^6.
\]
Hence exactly \(232\) of \(1792\) states are stable. With the same network and \(q=1\), \(184\) of \(1024\) are stable, whereas with \(q=3\), \(262\) of \(1792\) are stable. Vacancy-count monotonicity of the equilibrium fraction does not hold even on this natural unequal bipartite graph.

## Relationship to prior work
Narayanan, Sabbagh and Voudouris introduced this fractional diversity-seeking utility and proved the finite-improvement property for regular graphs **with one vacancy**, alongside a one-vacancy spider result and a maximum-degree-two result with arbitrary vacancies. Their full article also constructs improving cycles on certain regular graphs with at least four vacant vertices and explicitly poses broader bipartite cases as a question. The degree-two theorem covers the exceptional four-cycle \(K_{2,2}\), but these results neither imply an all-vacancy theorem for general complete bipartite graphs of unequal sizes nor enumerate their two-color equilibria. The exactly-one-vacancy \(K_{A,B}\) case has also been established separately, and is not claimed as new here.

Monaco, Moscardelli and Velaj analyze modified fractional hedonic games with a related average-over-other-coalition-members utility, including a counterexample to finite improvement on a general unweighted interaction graph (Theorem 9). In nonempty parts, the present gain comparison has a related same-type-coalition interpretation, but their model permits different coalitional moves and handles singleton/empty receiving groups differently; their result does not give this fixed-capacity, multi-vacancy factorial potential or stable-coloring enumerator. Narayanan and collaborators' later *variety*-seeking jump model counts distinct neighboring types rather than their fraction and therefore has a different preference ordering for at least three types and at variable occupancy. An equivalent proof in other network-game or coalition-game terminology remains a bibliographic risk; absence of a search hit is not a proof of uniqueness.

## Limitations
The theorem assumes exactly two fully interconnected independent vertex classes, all occupants strategic, an unweighted uniform fraction of occupied neighbors and strictly improving unilateral vacancy jumps. The potential is **ordinal**, not an exact utility-difference potential, and no polynomial convergence bound is claimed. The finite colored equilibrium polynomial requires **two** agent types, though the potential covers any finite number. The asymptotic fixes \(q\) before sending the balanced part size to infinity. No assertion is made for arbitrary bipartite graphs, other utility normalizations, simultaneous moves, or multilateral swaps. Independent verification and literature completeness are not claimed.

## References
1. L. Narayanan, Y. Sabbagh and A. A. Voudouris, *Diversity-Seeking Jump Games in Networks*, first publicly posted 2023-05-28, arXiv:2305.17757, https://arxiv.org/abs/2305.17757 ; open full article https://doi.org/10.1007/s10458-025-09714-8 (journal version 2025).
2. G. Monaco, L. Moscardelli and Y. Velaj, *Stable Outcomes in Modified Fractional Hedonic Games*, Autonomous Agents and Multi-Agent Systems 34 (2020), https://doi.org/10.1007/s10458-019-09431-z ; lawful open PDF https://www.isi.it/wp-content/uploads/2024/01/stable-outcomes-in-modified-fractional-hedonic-games_Velaj.pdf .
3. L. Narayanan, J. Opatrny, S. Tummala and A. A. Voudouris, *Variety-Seeking Jump Games on Graphs*, arXiv:2505.10005, https://arxiv.org/abs/2505.10005 (different payoff model).

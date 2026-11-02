# Exact two-cluster orbit census and nonmonotone synchronization in an entry-trigger quorum oscillator

## Finding

For the precisely defined parallel, flash-entry quorum automaton below, the entire asymptotic dynamics on its equal-size, two-cluster invariant sector has an exact classification for every integer clock length \(C\ge4\) and flashing-window size \(1\le w<C\). Write
\[
J(C,w)=\max\{0,C-2w+1\},\qquad K(C,w)=\max\{0,2w-C-2\}.
\]
There is exactly one synchronized primitive orbit, of period \(C-1\); exactly \(J(C,w)\) nonsynchronized *coasting* primitive orbits of period \(C\); and exactly \(K(C,w)\) nonsynchronized *mutually accelerated* primitive orbits of period \(C-1\). Every state eventually reaches one of these orbits, with no others. Each coasting orbit has precisely \(C\) states in its full basin (only the orbit itself); each mutually accelerated orbit has precisely \(C+1\) states in its basin; and the synchronized orbit has precisely
\[
B(C,w)=C^2-CJ(C,w)-(C+1)K(C,w)
\]
initial two-cluster phase states in its basin. These counts hold regardless of the even population size. For independent uniform initial phases of the two pre-synchronized clusters, the eventual exact-synchrony probability is \(B(C,w)/C^2\). The Artin–Mazur dynamical zeta function of the finite two-cluster map is
\[
\zeta_{C,w}(z)=(1-z^C)^{-J(C,w)}(1-z^{C-1})^{-[K(C,w)+1]}.
\]
In particular, synchrony is not monotone in flash duration: for \(C=10\), its basin fractions at \(w=3,6,9\) are respectively \(1/2,1,17/50\). An all-synchronizing interval occurs at the junction of the coasting and mutually accelerated regimes, whereas broad short or long flashing windows sustain distinct locked cycles.

## Assumptions and scope

Take a complete loopless graph on \(N=2m\ge2\) labelled vertices, divided into two fixed equal sets of size \(m\). Restrict initial configurations to those in which clocks within each set agree; their phases are \((x,y)\in(\mathbb Z/C\mathbb Z)^2\). All clocks advance simultaneously by one modulo \(C\). A clock is flashing exactly when its *nominally incremented* phase belongs to \(\{s,s+1,\ldots,C-1\}\), where \(s=C-w\). A clock whose nominal phase is the **first** flashing phase \(s\) then makes one additional unit advance if and only if strictly more than half of its \(N-1\) neighbors are nominally flashing. All decisions use the same nominal-phase snapshot; there is no noise, no sequential neighbor update, and no delay. The extra advance does not cause a second decision at the same time step. This convention defines a specific parallel flash-entry system; it should not be identified with a sequential implementation that tests one phase *after* flash entry.

Because the \(m-1\) neighbors in a clock's own group are fewer than half of \(2m-1\), the extra advance happens precisely when the other group is nominally flashing. Therefore the exact two-clock map is
\[
F_{C,w}(x,y)=\bigl(a+\mathbf1_{\{a=s,\ b\ge s\}},\ b+\mathbf1_{\{b=s,\ a\ge s\}}\bigr)\pmod C,
\quad a=x+1\pmod C,\ b=y+1\pmod C.
\]
The ordering comparisons use the canonical representatives \(0,\ldots,C-1\). Internal group equality is invariant. The theorem concerns **all** \(C^2\) such phase pairs, not generic unconstrained \(N\)-oscillator initial data, and asserts eventual exact equality of clock phases, not merely overlapping flashing windows.

## Proof

**1. One-step difference rule.** Let \(d=y-x\pmod C\), represented in \(\{0,\ldots,C-1\}\), and set \(s=C-w\). When \(d=0\), both groups accelerate together whenever they nominally enter phase \(s\), yielding a single diagonal cycle of length \(C-1\). If \(d\ne0\), the two groups cannot accelerate at the same step: their nominal phases cannot both equal \(s\). An advance of the first group is possible exactly when its original phase is \(s-1\) and
\[
1\le d\le w-1;
\]
then \(d\mapsto d-1\). An advance of the second group is possible exactly when its original phase is \(s-1\) and
\[
s+1\le d\le C-1;
\]
then \(d\mapsto d+1\pmod C\). Otherwise the difference stays fixed. This follows by substituting \(y=x+d\) into the displayed definition of \(F_{C,w}\), including modular wraparound.

**2. Coasting cycles.** Every difference \(d\) with \(w\le d\le s\) lies outside both active trigger ranges. Consequently the \(C\) phase pairs having this difference form one coasting orbit, and its primitive period is \(C\). This interval has \(\max(0,s-w+1)=J(C,w)\) elements. No trajectory with a different difference can enter the interval: on the low side only downward moves occur; on the high side only upward moves occur; and the trigger intervals do not overlap when the coasting interval is nonempty. Thus each coasting basin consists of exactly its \(C\) periodic states.

**3. Accelerated locked cycles.** For every integer
\[
s+2\le k\le w-1
\]
form the following set of phase pairs, with the second coordinate interpreted modulo \(C\):
\[
\begin{split}
\mathcal O_k={}&\{(x,x+k):0\le x\le s-1\}\ 
\cup\ \{(x,x+k):C+s-k+1\le x\le C-1\}\\
&\cup\ \{(x,x+k-1):s+1\le x\le C+s-k\}.
\end{split}
\]
The disjoint first and second ranges together have \(k-1\) states; the last range has \(C-k\), giving \(C-1\) states in total. Starting with \((0,k)\), ordinary advancement follows the listed pairs, except at two events: at \(x=s-1\) the first clock skips \(s\), changing the difference from \(k\) to \(k-1\); at \(y=s-1\) the second clock skips \(s\), restoring difference \(k\). Direct substitution into \(F_{C,w}\) shows that all \(C-1\) states form a single primitive orbit. The number of admissible integers \(k\) is \(K(C,w)=\max(0,w-s-2)\).

**4. Exhaustiveness of periodic orbits.** If \(d\) is strictly below \(s+1\) and is not a neutral coasting difference, only the first group can receive extra advances. Its repeated entries into the flashing window strictly decrease positive \(d\) until synchronization; neither clock can avoid encountering its trigger location because every clock advances at least one unit at every time step. The symmetric argument holds when \(d>w-1\): only the second group can be accelerated and \(d\) increases to \(C\), that is, zero. When the trigger intervals overlap, a nonzero orbit must have \(s+1\le d\le w-1\). In this region \(2\le d\le C-2\), so the two clocks' successive entries at phase \(s-1\) alternate in cyclic order (a single one-step acceleration cannot overtake the other clock). The first group's event decreases \(d\) by one and the second group's event increases it by one. If either event pushes \(d\) outside the overlap, the preceding one-sided argument implies eventual synchronization. Otherwise these events repeat in alternation, with \(d\) toggling between \(k\) and \(k-1\) for exactly one integer \(s+2\le k\le w-1\), and the orbit must be \(\mathcal O_k\) from step 3. Since the state space is finite, every trajectory is eventually periodic; these are all its possibilities.

**5. Exact basin sizes.** All pairs on \(\mathcal O_k\) have first and second coordinates avoiding phase \(s\). The one-step map increments each coordinate normally except that it sometimes sends \(s-1\) directly to \(s+1\). Solving \(F_{C,w}(u)=v\) for \(v\) on the displayed wave shows there are exactly two incoming states outside the wave:
\[
U_k=(s,s+k-1),\qquad V_k=(C+s-k,s).
\]
They feed respectively into the wave states with first coordinate \(s+1\) and with second coordinate \(s+1\). To see there are no other outside predecessors, a target coordinate other than \(s+1\) has only its ordinary predecessor (one step earlier), while a target coordinate equal to \(s+1\) may also arise by a skipped phase \(s-1\). Each wave has exactly one state with its first coordinate \(s+1\) and one (distinct) state with its second coordinate \(s+1\), giving precisely the two alternatives displayed above. Both outside states have zero predecessors: reaching the first coordinate \(s\) of \(U_k\), or the second coordinate \(s\) of \(V_k\), would require failing an acceleration while the other nominal coordinate is flashing. Thus the full basin of \(\mathcal O_k\) is precisely its \(C-1\) cycle states plus these two one-step predecessors, or \(C+1\) states. All remaining states go to the unique diagonal cycle by step 4. Subtraction from the \(C^2\) initial phase pairs gives \(B(C,w)\). The zeta formula follows from the disjoint primitive orbit census and the Euler product for finite dynamical systems.

## Verification

The included standalone file `verification/check_firefly.py` implements the two-clock map and, separately, the original \(N\)-agent parallel majority test on two equal-size clock blocks. The two implementations agree on \(81{,}330\) explicitly checked configurations. Exhaustive functional-graph enumeration for \(4\le C\le72\) and \(1\le w<C\) covers \(2{,}553\) parameter pairs and \(6{,}779{,}342\) phase states; it checks every primitive cycle label and length, exact basins, explicit wave coordinates, and the two source states of each wave. All checks passed. These finite checks are separately implemented cross-tests; steps 1–5 prove the theorem for every admissible integer pair and every even group population.

For \(C=10\), the exact synchrony-basin counts at widths \(w=3,5,6,7,9\) are respectively \(50,90,100,78,34\) out of \(100\), giving a nonmonotone order-of-limits warning: a broader flash interval need not increase exact phase convergence even without noise.

## Relationship to prior work

Aust, Zhang, Reina, and Hamann (2026) study a discrete, quorum-controlled firefly system and report multi-cluster trapping and nonmonotone benefits from interventions. Their publicly readable main text establishes the motivation for exact subgroup-locking analysis but does not give the present all-width, all-initial-phase primitive-cycle and basin census. Its prose describes acceleration upon entering the flashing interval, whereas the printed algorithm tests at the subsequent phase and loops sequentially over individuals. The theorem here explicitly fixes the parallel, flash-entry convention and **does not assert that these formulas apply to that printed sequential algorithm**. Consequently this is a mathematical classification of a natural, expressly specified convention inspired by that framework, not a correction or replication claim about its implementation.

Lyu (2015) studies a different finite-state pulse system with inhibitory, rather than entry-triggered accelerating, coupling. O'Keeffe, Krapivsky, and Strogatz (2015) quantify cluster aggregation in a different pulse-coupled oscillator model. Neither statement implies these phase- and flash-width-specific exact orbit counts. Existing general facts on finite deterministic maps do not supply the explicit census or the all-synchronizing boundary window without an analysis of this map.

## Limitations

The theorem treats noiseless simultaneous updates, strict half-neighbor quorum, complete-graph interactions, two **equal** pre-synchronized groups, and the precise **flash-entry** trigger. It does not describe arbitrary initial phases of all individual agents, smaller-degree graphs, unequal groups, the sequence-dependent asynchronous algorithm, or an alternative after-entry trigger. It does not address robustness of locked cycles under changing the network or adding stochastic perturbations. A finite-state basin count is not a statement about continuous-state volume. Historical priority cannot be ruled out against all unindexed or inaccessible specialized literature; no independent audit has been performed.

## References

1. T. Aust, T. Zhang, A. Reina, and H. Hamann, *Bimodal Synchronization Performance: Why Noise and Sparse Connectivity Can Improve Collective Timing*, arXiv:2605.17206v1, publicly submitted 17 May 2026. Full HTML: https://arxiv.org/html/2605.17206v1 ; abstract https://arxiv.org/abs/2605.17206 .
2. H. Lyu, *Synchronization of finite-state pulse-coupled oscillators*, arXiv:1407.1103 (2014 preprint; published in Physica D, 2015). https://arxiv.org/abs/1407.1103 .
3. K. P. O'Keeffe, P. L. Krapivsky, and S. H. Strogatz, *Synchronization as Aggregation: Cluster Kinetics of Pulse-Coupled Oscillators*, arXiv:1501.04115 (2015). https://arxiv.org/abs/1501.04115 .

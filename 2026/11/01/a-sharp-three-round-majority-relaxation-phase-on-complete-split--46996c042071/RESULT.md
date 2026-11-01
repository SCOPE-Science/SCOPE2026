# A sharp three-round majority-relaxation phase on complete split graphs

## Finding
Let \(a,b\ge1\) be integers and let \(G_{a,b}=K_a\vee\overline K_b\), the graph consisting of an \(a\)-vertex clique joined to an independent set of \(b\) vertices. In synchronous binary *neighbor-majority* dynamics, a vertex adopts the strict majority of its neighbors' states and retains its own state when its neighbors tie. Let \(F\) denote one simultaneous update and define the first periodic-entry time
\[
T(x)=\min\{t\ge0:F^{t+2}(x)=F^t(x)\}.
\]
Then \(T(x)\le3\) for every initial binary configuration \(x\). Three rounds are actually required for some configurations **if and only if** \(a>b\), \(a+b\) is even, and \(b\ge3\).

More precisely, write \(c\) for the number of initial ones in the clique, \(p\) for the number of initial ones in the independent set, and \(r=(a+b)/2\). An initial state has \(T(x)=3\) if and only if
\[
a>b,\quad a+b\text{ is even},\quad c+p=r,\quad
\frac{a-b}{2}<c<r,\quad c\ne\frac a2.
\]
Consequently, the **exact number of labelled initial configurations requiring three rounds** is
\[
E_3(a,b)=
\begin{cases}
\displaystyle\binom{a+b}{r}-2\binom a r
-\mathbf1_{2\mid a}\binom a{a/2}\binom b{b/2},
& a>b,\ a+b=2r,\\[4pt]
0,&\text{otherwise}.
\end{cases}
\]
Here the last term is included only when \(a\) is even; in the displayed first case \(a\) and \(b\) then both are even.

The only fixed states are the two constant states. The number of states already on a fixed point or a primitive two-cycle is
\[
R(a,b)=2+2\mathbf1_{a\le b}
+2\mathbf1_{a>b,\,2\mid(a+b)}\binom a{(a+b)/2}
+\mathbf1_{2\mid a,\,2\mid b}\binom a{a/2}\binom b{b/2}.
\]
Thus the number of distinct primitive two-cycle orbits is \((R(a,b)-2)/2\). No primitive period greater than two occurs.

If \(a>b\), \(a+b\) is even, and \(b\to\infty\) along any sequence of such parameter pairs, then for a uniformly random initial state,
\[
\Pr(T=3)\sim\sqrt{\frac{2}{\pi(a+b)}}.
\]
The maximum transient time is therefore three throughout a natural asymmetric regime, but the proportion of states attaining that maximum tends to zero.

## Assumptions and scope
The graph is finite, simple and labelled. All \(a\) clique vertices are adjacent to one another and to every independent-set vertex; independent-set vertices are pairwise nonadjacent. The state alphabet is \(\{0,1\}\), all vertices update **simultaneously**, and ties preserve the vertex's prior bit. Both part sizes are positive. The entry time is measured in complete synchronous updates from time zero, not by individual vertex changes. The formula counts labelled binary configurations, not their orbits under graph automorphisms.

## Proof
**One-step formulas.** Let \(C\in\{0,1\}^a\) and \(I\in\{0,1\}^b\) be the current words, with populations \(c,p\) and total \(s=c+p\); let \(\mathbf0,\mathbf1\) denote constant words of the indicated lengths. A clique vertex currently in state \(u\) sees \(s-u\) ones among its \(a+b-1\) neighbors. A vertex of the independent set sees exactly \(c\) ones among its \(a\) clique neighbors. Direct comparison with half these degrees yields:

- If \(a+b\) is odd, the new clique word is \(\mathbf1\) for \(2s>a+b\) and \(\mathbf0\) otherwise.
- If \(a+b\) is even, the new clique word is \(\mathbf0\), \(\mathbf1-C\), or \(\mathbf1\), respectively, as \(2s<a+b\), \(2s=a+b\), or \(2s>a+b\).
- Independently of the parity of \(a+b\), the new independent-set word is \(\mathbf0\), \(I\), or \(\mathbf1\), respectively, as \(2c<a\), \(2c=a\), or \(2c>a\).

Call a state a *corner* if both part words are constant. Two corners, all-zero and all-one, are fixed. The other corners \((\mathbf1_a,\mathbf0_b)\) and \((\mathbf0_a,\mathbf1_b)\) exchange under \(F\) when \(a\le b\). When \(a>b\), the first of these goes to all-one and the second to all-zero. Thus a corner is immediately periodic if \(a\le b\), and enters a fixed point after at most one further update if \(a>b\).

**All states enter by time three.** If \(a+b\) is odd, the clique is constant after one update. The independent set is also constant then unless \(a\) is even and the initial clique population is \(a/2\). In that exceptional case, \(b\) is odd; the clique becomes all-zero for \(p<b/2\) and all-one for \(p>b/2\), with the independent-set word retained for one step. At the next update both parts become the same constant word, and the system is fixed. Otherwise it is a corner after one update. Hence the entry time is at most two when \(a+b\) is odd.

Suppose \(a+b=2r\). Off the critical initial total \(s=r\), the clique becomes constant after one step. The independent set also becomes constant unless \(a\) is even and \(c=a/2\). In that exceptional case \(b\) is even, \(p\ne b/2\), and the next two updates produce all-zero if \(p<b/2\) or all-one if \(p>b/2\). Hence off the central total, \(T\le2\).

On the critical total \(s=r\), if \(c=a/2\), necessarily \(p=b/2\); the clique complements every round and the independent set is unchanged. This is an immediate two-cycle. For \(c\ne a/2\), the independent set becomes constant after one update and the clique complements its initial word. Write \(\ell=a-r=(a-b)/2\). If \(c<a/2\), the first update has clique population \(a-c\) and zero independent ones. The requirement \(p=r-c\le b\) implies \(c\ge\ell\). Equality \(c=\ell\) gives an immediate two-cycle (the independent set was initially all-one). For \(c>\ell\), the second update is the corner \((\mathbf0_a,\mathbf1_b)\). If instead \(c>a/2\), the first update has clique population \(a-c\) and all-one independent set. Since \(p=r-c\ge0\), one has \(c\le r\). Equality \(c=r\) gives an immediate two-cycle (the independent set was initially all-zero). For \(c<r\), the second update is the corner \((\mathbf1_a,\mathbf0_b)\). All cases have reached a corner or a two-cycle after two updates. The corner behavior already established proves \(T\le3\), and the corners require a third step exactly when \(a>b\). This proves the stated if-and-only-if characterization of \(T=3\).

**Counting the third layer.** In the three-round regime \(a>b\), \(2r=a+b\), the inequalities \(\ell<c<r\) are equivalent to having \(1\le p\le b-1\) on the critical population level \(c+p=r\). Vandermonde's identity counts all \(\binom{a+b}{r}\) states at that level. Removing the two endpoint populations \((c,p)=(\ell,b),(r,0)\) subtracts \(2\binom a r\), since \(\binom a\ell=\binom ar\). If \(a,b\) are even, removing the central tie population \((a/2,b/2)\) subtracts the displayed product of binomial coefficients. This gives \(E_3(a,b)\). The interval has \(b-1\) integer clique populations; precisely one is excluded by the central tie when both parts are even. Thus it is nonempty exactly for \(b\ge3\) under the stated parity and size conditions.

**Recurrent-state census.** The corner classification supplies the two fixed states and a two-cycle of corner states if and only if \(a\le b\). Off the critical total there can be no other periodic state: the arguments above force a corner or a fixed state without returning to the initial mixed pattern. On the critical total \(s=r\), the only remaining recurrent families are the central tie states \((c,p)=(a/2,b/2)\) when both sizes are even, and—when \(a>b\)—the two endpoint families \((\ell,b)\) and \((r,0)\). Their populations are respectively \(\binom a{a/2}\binom b{b/2}\), \(\binom a\ell\) and \(\binom ar\). Each endpoint pair forms temporal two-cycles, with disjoint classes because \(a>b\). These counts give \(R(a,b)\). All listed nonfixed recurrent states have period exactly two, proving the orbit formula.

**Asymptotic.** Under \(a>b\) and \(a+b=2r\), the endpoint ratio satisfies
\[
\frac{\binom ar}{\binom{a+b}r}
=\prod_{j=0}^{b-1}\frac{r-j}{a+b-j}\le2^{-b}.
\]
When \(a,b\) are even, Stirling's formula yields
\[
\frac{\binom a{a/2}\binom b{b/2}}{\binom{a+b}r}
\sim\sqrt{\frac{2(a+b)}{\pi ab}}=O(b^{-1/2}).
\]
Since \(a>b\) and \(b\to\infty\), both corrections are negligible relative to \(\binom{a+b}r\). The central binomial asymptotic \(\binom{2r}r/2^{2r}\sim1/\sqrt{\pi r}\) completes the proof.

## Verification
A standalone Python checker independently implements the graph's neighbor-majority update, compares every binary initial state with its state two steps later after each of the first four times, and checks the exact third-layer and recurrent-state formulas. It exhaustively checks 120 positive ordered size pairs with \(a+b\le16\), representing 1,835,012 initial binary configurations. A separate word-level update implementation checks 313,600 within-part population signatures from 1,024 parameter pairs with \(1\le a,b\le32\). Both checks pass. Run `python verify_majority_split.py`; recorded output is in `verification_output.txt`.

## Relationship to prior work
The established theorem of Goles and Olivos (1980) supplies eventual period at most two for symmetric threshold networks. Kaaser, Mallmann-Trenn and Natale (2015, arXiv:1508.03519; MFCS 2016) study sharp voting-time questions on graphs and prove module-contraction upper bounds. Their results motivate examination of graphs with a clique module and an independent module; the inspected full texts do not state the present complete-split three-round phase boundary or its labelled central-binomial census. An earlier balanced complete-split classification determines recurrent and transient counts when \(a=b\), including a two-round bound; that restricted case does not imply the strictly asymmetric three-round phase. The vertex-update convention here agrees with the cited voting-time work, including tie retention.

## Limitations
The result concerns only completely joined split graphs, not arbitrary split graphs with missing join edges. It assumes binary, synchronous, unweighted neighbor-majority updating with lazy ties. The formulas do not automatically transfer to asynchronous updates, self-inclusive majority, random tie-breaking, or weighted graphs. Finite checks support but do not establish the infinite-parameter proof. The novelty assessment is bounded by the accessible literature: the earliest general period-two theorem was checked through bibliographic and abstract-level information, not its entire publisher full text; an undiscovered equivalent family-specific statement cannot be excluded.

## References
1. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, first submitted 2015-08-14; MFCS 2016, LIPIcs 58, Article 55, DOI: 10.4230/LIPIcs.MFCS.2016.55. Full texts: https://arxiv.org/abs/1508.03519 and https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.55.
2. E. Goles, J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
3. S. Poljak, M. Sůra, *On periodical behaviour in societies with symmetric influences*, Combinatorica 3 (1983), 119–121, DOI: 10.1007/BF02579347.

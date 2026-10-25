# A sharp Condorcet-exclusion criterion and two support transitions for stable two-lotteries

## Finding
Consider three alternatives \(A,B,C\) in the single-peaked order \(A\prec B\prec C\). An arbitrary finite electorate has proportions \(u,v,m,n\) of the four admissible strict rankings \(A\succ B\succ C\), \(C\succ B\succ A\), \(B\succ A\succ C\), and \(B\succ C\succ A\), respectively, where the proportions are nonnegative and sum to one. Suppose \(u<1/2\) and \(v<1/2\); equivalently, \(B\) is the strict Condorcet winner. Put \(s=u+m\).

**Condorcet-exclusion criterion.** Under the independently sampled, uniformly tie-broken stable two-lottery rule, the unique equilibrium distribution gives the Condorcet winner \(B\) zero probability if and only if
\[
\frac13<s<\frac23\quad\text{and}\quad m+n+u(2-3s)^2+v(3s-1)^2\le\frac13.
\]
Whenever the criterion holds, the unique distribution, in the order \((A,B,C)\), is
\[
D=(3s-1,\,0,\,2-3s).
\]
This is a semialgebraic description of the entire Condorcet-exclusion region within the three-candidate single-peaked profile simplex, not merely an example.

**Symmetric sharp phase law.** For \(0\le p\le1/2\), set \(u=v=p\) and \(m=n=(1-2p)/2\). The unique stable two-lottery is
\[
D_p=\begin{cases}
(0,1,0),&0\le p\le1/3,\\
(x_p,1-2x_p,x_p),\quad x_p=\dfrac{3p-1}{2-3p},&1/3<p<4/9,\\
(1/2,0,1/2),&4/9\le p\le1/2.
\end{cases}
\]
Thus the support changes sharply from only \(B\), to all three candidates, to exactly \(A,C\). For \(4/9\le p<1/2\), \(B\) is a strict Condorcet winner even though the unique stable two-lottery never selects it. The endpoint \(p=4/9\) is realized by \(18\) voters: eight of each extreme ranking and one of each middle-first ranking. The threshold example is a specialization of an earlier general lower-bound construction (see Relationship to prior work); the new result is the full exclusion criterion and support law.

## Assumptions and scope
A voter draws a favorite among a pure attacking alternative and two independent defending alternatives, sampled with replacement from a lottery \(D\). If two or three drawn copies name the same alternative, copies are distinguished and their ordering is uniformly randomized. For an attacking alternative \(j\), define \(F_j(D)\) as its probability of being the voter's favored *copy*, averaged over all voters and both defending draws. The defender chooses \(D\) to minimize \(\max_jF_j(D)\). This is the independent-draw stable two-lottery formulation, not the distinct-committee version of proportional representation and not the unrelated recursive rule called Stable Voting.

Rankings are complete and strict, except that copies of the same alternative are tied and randomized. The statement covers all finite unweighted electorates with the stated ranking proportions; the same algebra holds for arbitrary nonnegative real-valued ranking weights. Single-peakedness requires exactly the four displayed rankings. The general criterion assumes \(B\) is the strict Condorcet winner; the symmetric phase formula also covers \(p=1/2\), where strict Condorcet status need not hold.

## Proof
**1. Exact score and stability identity.** For a voter \(w\), write \(r_{w,j}\) for the \(D\)-mass of alternatives the voter ranks strictly below \(j\), and write \(d_j=D(j)\). Conditional on that voter, the attacker-copy win probability is
\[
Q(r_{w,j},d_j)=\int_0^1(r_{w,j}+td_j)^2\,dt=r_{w,j}^2+r_{w,j}d_j+\frac{d_j^2}{3}.
\]
Consequently \(F_j(D)=\sum_w\pi_w Q(r_{w,j},d_j)\), where \(\pi_w\) is the voter-ranking proportion. Three exchangeable independent copies from \(D\) each win with probability \(1/3\), giving
\[
\sum_{j\in\{A,B,C\}}D(j)F_j(D)=\frac13.
\]
Thus \(\max_jF_j(D)\ge1/3\) for every lottery. Every lottery satisfying \(F_A,F_B,F_C\le1/3\) is stable, and each positively supported candidate then satisfies equality. The quadratic \(Q(r,d)\) is strictly convex in \((r,d)\), since its quadratic-form matrix \(\left(\begin{smallmatrix}1&1/2\\1/2&1/3\end{smallmatrix}\right)\) has positive leading minor and determinant \(1/12\). Because \((r_{w,j},d_j)\) depends affinely on \(D\), each \(F_j\) is convex.

**2. Uniqueness.** If \(D,E\) are both stable, their midpoint \(M=(D+E)/2\) is stable by convexity. Every \(j\) in the support of \(M\) has \(F_j(M)=1/3\), while convexity gives \(F_j(M)\le(F_j(D)+F_j(E))/2\le1/3\). If \(D(j)\ne E(j)\), strict convexity of \(Q\) at every voter ranking makes the first inequality strict, a contradiction. Hence the masses agree for all supported candidates and vanish elsewhere, so \(D=E\). This argument reproduces the previously established general uniqueness principle [2, Lemma 9]; uniqueness itself is not claimed as novel.

**3. Necessary criterion.** Since \(u,v<1/2\), a pure lottery on \(A\) is defeated by \(B\) with probability \(1-u>1/2\), and a pure lottery on \(C\) is defeated by \(B\) with probability \(1-v>1/2\). Neither can be stable. If a stable lottery excludes \(B\), both extremes therefore have positive mass; write \(D=(t,0,1-t)\) with \(0<t<1\). The score identity implies \(F_A=F_C=1/3\). Direct calculation by the four rankings yields
\[
F_A=s(1-t)+\frac{t^2}{3},\qquad
F_C=(1-s)t+\frac{(1-t)^2}{3},\qquad
F_B=m+n+u(1-t)^2+vt^2.
\]
Subtracting the first two gives \(F_A-F_C=s-(1+t)/3\). Thus equality forces \(t=3s-1\) and, because \(0<t<1\), the strict bounds \(1/3<s<2/3\). Substitution gives \(F_A=F_C=1/3\), and stability further requires the stated inequality \(F_B\le1/3\).

**4. Sufficiency.** Conversely suppose the bounds and inequality hold. Set \(t=3s-1\); this belongs to \((0,1)\). The preceding exact formulas give \(F_A=F_C=1/3\) and \(F_B\le1/3\). By step 1 the lottery is stable; step 2 proves it is the unique one. This establishes both directions, including the equality boundary in the second inequality.

**5. Symmetric phase transitions.** Now \(s=1/2\), so the excluded-middle candidate is \((1/2,0,1/2)\) and its attacker score is \(F_B=1-3p/2\). The exclusion criterion is therefore exactly \(p\ge4/9\) within the strict Condorcet range. For \(p\le1/3\), the pure center lottery has attacker scores \((p,1/3,p)\) and is stable. For \(1/3<p<4/9\), put \(x=(3p-1)/(2-3p)\). With \(D=(x,1-2x,x)\), direct calculation gives
\[
3F_A-1=3F_C-1=-(2x-1)f,\qquad 3F_B-1=-2xf,
\]
where \(f=(3p-2)x+3p-1=0\); all three scores equal \(1/3\), establishing stability. The regions join continuously at their endpoints, and uniqueness from step 2 eliminates other lotteries. The strict Condorcet statement follows because the center beats each extreme candidate by voter proportion \(1-p>1/2\) whenever \(p<1/2\).

## Verification
`verify.py` uses only Python standard-library exact rational arithmetic. It independently computes attacker scores by explicitly enumerating two defending draws with randomized duplicate-copy ties, and compares them with the integrated-rank formula. It checks the symmetric piecewise candidate at rational parameter values, verifies the self-play identity and supported-candidate score equalities, and cross-checks the full exclusion criterion on bounded rational four-ranking profiles. Its observed run reports \(10{,}788\) exact attacker-score comparisons and \(1{,}866\) general Condorcet-exclusion tests. The finite tests corroborate the formulas; the universal result is established by the proof, not by finite enumeration.

## Relationship to prior work
Cai, Charikar, Hastings, Ramakrishnan, Wang, and Ye [1] analyze distortion and generalizations of stable lotteries and state the general stability and self-play conditions; the present argument applies their independently sampled \(k=2\) rule to strict single-peaked three-candidate profiles, for which we obtain a complete support phase diagram and exact Condorcet-exclusion region. Shah [2, Lemma 9] already proves global uniqueness for nondegenerate random-size stable lotteries, which strictly subsumes step 2 as a uniqueness claim. More importantly, the \(N=2\), \(r=1/2\) specialization of Shah [2, Lemma 10] implicitly produces the exact symmetric critical profile \(p=4/9\): an excluded central alternative appears at the top with probability \(1/9\) and between the extremes with probability \(8/9\), with balanced extreme ranking orders. **The critical eighteen-voter example itself is therefore not claimed as independently new.** That construction does not state the iff criterion for arbitrary four-type single-peaked profiles or the complete two-transition phase law. Earlier maximal-lottery treatments concern the one-draw game; maximal lotteries concentrate on the strict Condorcet winner here and do not imply the two-draw exclusion region. Distinct recursive rules also called Stable Voting are not the present game.

## Limitations
No general formula is claimed for the positive middle-candidate mass on arbitrary asymmetric profiles outside the exclusion region. The profile domain has precisely three alternatives, four possible single-peaked rankings, and independent defending draws. The full exclusion criterion is exact; the symmetric phase formula does not extend to arbitrary rankings without qualification. General historical-priority uncertainty remains because some earlier literature on stable lottery variants was accessible only by abstract. Uniqueness and the sharp symmetric endpoint construction are explicitly credited to their relevant antecedents. Independent validation has not been performed.

## References
[1] Z. Cai, M. Charikar, J. Hastings, P. Ramakrishnan, K. Wang, and Q. Ye, *Stable Voting Rules on the Edge of Optimal Metric Distortion*, arXiv:2609.08259v1, September 8, 2026, https://arxiv.org/html/2609.08259v1 (Definitions 2 and 3, Theorem 3, Section 5, Appendix A).

[2] N. Shah, *Improving Randomized Metric Distortion to 2.1441*, arXiv:2608.29308v2, 2026, https://arxiv.org/html/2608.29308v2 (Appendix C.1, Lemmas 9 and 10).

[3] Y. Cheng, Z. Jiang, K. Munagala, and K. Wang, *Group Fairness in Committee Selection*, ACM Transactions on Economics and Computation 8(4), 2020 (original stable-lottery perspective, with a distinct committee interpretation).

[4] F. Brandt, M. Matthäus, and C. Saile, *Minimal voting paradoxes*, 2022, https://doi.org/10.1177/09516298221122104 (general Condorcet paradox terminology, not a result about stable two-lotteries).

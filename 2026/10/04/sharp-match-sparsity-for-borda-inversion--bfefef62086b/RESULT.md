# Sharp match sparsity for Borda inversion
## Finding
For every integer \(n\ge3\), consider a finite tournament on players \(P_1,\ldots,P_n\) in which Borda ranks players by their total numbers of victories. Suppose the full tournament has the strict order
\[
P_1\succ P_2\succ\cdots\succ P_n,
\]
and, after deleting every match involving \(P_n\), the remaining strict order is
\[
P_{n-1}\succ P_{n-2}\succ\cdots\succ P_1.
\]
Then the total number \(M\) of matches satisfies
\[
M\ge 3\binom{n-1}{2}.
\]
This is sharp for every \(n\ge3\). If \(\Delta\) denotes the largest number of matches played by any player, then the exact minimum possible value is
\[
\Delta_{\min}(3)=3,
\qquad
\Delta_{\min}(n)=(n-1)(n-2)\quad(n\ge4).
\]
The construction below attains the sharp total-match and maximum-player bounds simultaneously.

## Assumptions and scope
A tournament is a finite list of matches, so repeated meetings are allowed. A victory contributes one Borda win and a tie contributes none; therefore every match contributes at most one total victory. The ranking is required to be strict before and after deletion. Only the matches involving \(P_n\) are deleted. No restriction is imposed on schedules or on the number of meetings between a fixed pair. The extremal construction uses only decisive \(1\)-to-\(0\) outcomes.

## Proof
Let \(r_i\) be the number of victories of \(P_i\) after deleting \(P_n\), let \(q_i\) be the number of victories of \(P_i\) over \(P_n\), and let \(w_i=r_i+q_i\) be the full-tournament victory count of \(P_i\), for \(1\le i\le n-1\).

The reversed reduced ranking gives
\[
r_1<r_2<\cdots<r_{n-1}.
\]
Since these are nonnegative integers,
\[
r_i\ge i-1,
\qquad
r_{n-1}\ge n-2.
\]
The full strict ranking gives
\[
w_1>w_2>\cdots>w_{n-1}>w_n\ge0.
\]
Consequently
\[
w_i\ge w_{n-1}+n-1-i\ge r_{n-1}+n-1-i\ge 2n-3-i.
\]
Every match contributes at most one victory, hence
\[
M\ge\sum_{i=1}^{n}w_i\ge\sum_{i=1}^{n-1}(2n-3-i)
=\frac{3(n-1)(n-2)}2
=3\binom{n-1}{2}.
\]

For sharpness, among \(P_1,\ldots,P_{n-1}\) play one match for every unordered pair, with the player of larger index winning. Thus
\[
r_i=i-1.
\]
For each \(1\le i\le n-1\), let \(P_i\) defeat \(P_n\) exactly
\[
q_i=2(n-1-i)
\]
times, and give \(P_n\) no victories. Then
\[
w_i=(i-1)+2(n-1-i)=2n-3-i,
\qquad w_n=0,
\]
so the full ranking is \(P_1\succ\cdots\succ P_n\), while deletion of \(P_n\) gives the exact reverse order on the survivors. The construction has
\[
\binom{n-1}{2}+\sum_{i=1}^{n-1}2(n-1-i)
=3\binom{n-1}{2}
\]
matches.

For the per-player bound, compare adjacent survivors. Strictness gives
\[
r_{i+1}-r_i\ge1
\]
and
\[
w_i-w_{i+1}\ge1.
\]
Using \(w_i=r_i+q_i\),
\[
q_i-q_{i+1}
=(w_i-w_{i+1})+(r_{i+1}-r_i)
\ge2.
\]
Therefore
\[
q_i\ge2(n-1-i)
\]
and
\[
\sum_{i=1}^{n-1}q_i\ge(n-1)(n-2).
\]
All these victories are matches involving \(P_n\), so every inversion has
\[
\Delta\ge(n-1)(n-2).
\]
In the sharp construction, \(P_n\) plays exactly \((n-1)(n-2)\) matches, while \(P_i\) plays
\[
(n-2)+2(n-1-i)\le3(n-2).
\]
For \(n\ge4\), \((n-1)(n-2)\ge3(n-2)\), proving \(\Delta_{\min}(n)=(n-1)(n-2)\). For \(n=3\), the reduced reversal requires at least one match won by \(P_2\) over \(P_1\), and the adjacent inequality forces \(q_1\ge2\); hence \(P_1\) plays at least three matches. The construction has exactly three, so \(\Delta_{\min}(3)=3\).

## Verification
The accompanying `verify.py` reconstructs the explicit family for \(3\le n\le100\), checks both rankings, checks the exact total-match formula, and checks the claimed maximum-player count. It also verifies the integer identities used in the lower-bound argument. The program is a replay of finite arithmetic; the all-\(n\) lower bounds are established by the proof above, not by finite enumeration.

For \(n=5\), the sharp construction has \(18\) matches in total and maximum player load \(12\). The motivating paper's displayed Borda example has victory totals \(24,23,22,21,20\), hence \(110\) decisive matches, and its general construction at \(n=5\) has \(44\) matches per player.

## Relationship to prior work
Chèze and Fieux define the inversion paradox exactly as the complete reversal of the surviving ranking after deleting the last-ranked player. They define their tournament Borda method as ranking by numbers of victories and prove that Borda admits the paradox. Their five-player Example 20 gives an explicit Borda inversion. They then open a section titled “Inversion with few matches,” ask whether the paradox can occur when each player has few matches, and obtain sparse families for Massey and Colley. In their later remarks they state that their particular sparse family does not give the same result for Borda. The exact Borda sparsity thresholds above are not stated there.

Fishburn's 1981 work studies inverted collective orders for monotone positional scoring rules when an object is removed, but its objects are judge-ranking profiles and positional score vectors rather than finite sports-match lists ranked by victory counts; the inspected abstract does not give an extremal number of matches or a maximum player load. Kondratev, Ianovski, and Nesterov study invariance under removing extremely strong or weak candidates for generalized scoring rules in rank aggregation; their setting likewise does not imply the two tournament-match extrema proved here.

## Limitations
The theorem concerns the win-count version of Borda used in the motivating tournament paper. It does not concern classical ballot Borda with a fixed electorate, Massey, Colley, or Markov rankings. It minimizes total matches and maximum player load without requiring a balanced schedule. The extremal construction is deliberately unbalanced: the deleted player bears the quadratic match load for \(n\ge4\). No uniqueness classification of extremal tournaments is claimed.

## References
1. G. Chèze and E. Fieux, “The Inversion Paradox and Ranking Methods in Tournaments,” arXiv:2503.02429, first public version 4 March 2025; *The American Mathematical Monthly* 133 (2026), 316–340, DOI: 10.1080/00029890.2025.2601470.
2. P. C. Fishburn, “Inverted orders for monotone scoring rules,” *Discrete Applied Mathematics* 3 (1981), 27–36, DOI: 10.1016/0166-218X(81)90025-1.
3. A. Y. Kondratev, E. Ianovski, and A. S. Nesterov, “How Should We Score Athletes and Candidates: Geometric Scoring Rules,” *Operations Research* 72 (2024), 2507–2525, DOI: 10.1287/opre.2023.2473; arXiv:1907.05082.

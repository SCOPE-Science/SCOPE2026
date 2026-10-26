# Sharp nonwasteful boundary for strong EJR+ up-to-one in approval committees

## Finding

In unit-cost approval-based committee elections, there is an exhaustive, Pareto-efficient committee in the ordinary (strict-blocking) core that satisfies ordinary EJR+ but violates **strong EJR+ up-to-one** with only **three voters, four seats, and five candidates**. No such separation is possible with at most two voters when every elected candidate has a supporter, or with three voters and at most three seats even without that nonwastefulness assumption. Consequently, the electorate size, seat count at the minimal electorate size, and candidate count of this witness are sharp within nonwasteful outcomes. The separation also persists after any positive integer replication of the three voter types.

The two proportionality properties are distinct: ordinary EJR+ is the approval-committee axiom of Brill and Peters [2]; strong EJR+ **up-to-one** is the strict payment-bound condition (6) of Skowron [1], not the stronger exact condition (5).

## Assumptions and scope

An election has a finite set of candidates \(C\), \(n\ge1\) voters with approval sets \(A_i\subseteq C\), and a committee \(W\subseteq C\) of \(k\ge1\) elected unit-cost candidates, with \(k\le |C|\). Write \(t_i=|W\cap A_i|\). **Nonwasteful** means every member of \(W\) is approved by at least one voter. For an unelected candidate \(x\in C\setminus W\), ordinary EJR+ requires that every nonempty \(T\subseteq\{i:x\in A_i\}\) contain a voter \(i\) satisfying \(t_i+1>k|T|/n\).

For any nonempty group \(S\) and unelected \(x\) with \(a=|\{i\in S:x\in A_i\}|>0\), define \(s_S(d)=|\{i\in S:d\in A_i\}|\) and the payment expression

\[
P_i(S,x)=\sum_{d\in W\cap A_i}\min\!\left\{\frac1{s_S(d)},\frac1a\right\}+\frac{\mathbf1_{\{x\in A_i\}}}{a},\qquad i\in S.
\]

Every displayed denominator in a summand is positive. The committee satisfies **strong EJR+ up-to-one** exactly when for every \((S,x)\) as above, some \(i\in S\) satisfies \(P_i(S,x)>k/n\), as in [1, Definition 4, (6)]. Ordinary strict-blocking core stability means no nonempty \(S\) can choose \(T\subseteq C\) with \(|T|\le k|S|/n\) and \(|T\cap A_i|>t_i\) for **all** \(i\in S\). Pareto efficiency means there is no feasible \(T\) giving every voter at least \(t_i\) and some voter strictly more.

## Proof

**Explicit sharp witness.** Let \(C=\{a,b,c,d,e\}\), \(W=\{a,b,c,d\}\), and set

\[
A_1=A_2=\{a,d,e\},\qquad A_3=\{a,b,c\}.
\]

The satisfaction vector is \((t_1,t_2,t_3)=(2,2,3)\). Every winner has a supporter. The only unelected candidate is \(e\), whose supporters are voters 1 and 2. For either singleton supporter group the EJR+ inequality is \(3>4/3\); for their pair it is \(3>8/3\). Thus ordinary EJR+ holds.

Now take \(S=\{1,2,3\}\) and \(x=e\). The numbers of supporters within \(S\) of \(a,b,c,d,e\) are respectively \(3,1,1,2,2\). Therefore

\[
P_1(S,e)=P_2(S,e)=\frac13+\frac12+\frac12=\frac43,
\qquad P_3(S,e)=\frac13+\frac12+\frac12=\frac43.
\]

Since \(k/n=4/3\), **no** voter satisfies the required strict inequality. Hence strong EJR+ up-to-one fails.

Any proposed strict-blocking coalition containing voter 3 fails because that voter already receives all three candidates they approve. Every other coalition is contained in \(\{1,2\}\) and can afford at most \(\lfloor 4\cdot2/3\rfloor=2\) candidates, while each member already receives utility 2. This proves membership in the ordinary strict core. For Pareto efficiency, preserving voter 3's utility 3 forces any weak Pareto improvement to contain \(a,b,c\). Strictly improving voters 1 or 2 further forces \(d,e\) as well, demanding five seats. Thus no feasible Pareto improvement exists.

**At most two voters: nonwastefulness precludes separation.** For one voter the strong payment expression equals \(t_i+1\), precisely the quantity tested by ordinary EJR+. With two voters, consider any pair \((S,x)\) with \(a>0\). If \(|S|=1\), ordinary EJR+ again gives \(P_i(S,x)=t_i+1>k/2\). Suppose \(S\) contains both voters. If \(a=1\), the contributions to \(P_1+P_2\) from each elected candidate total exactly 1 because every elected candidate has a supporter; the contribution from \(x\) also totals 1. Thus \(P_1+P_2=k+1>k\), so some voter exceeds \(k/2\). If \(a=2\), both voters approve \(x\); ordinary EJR+ applied to these two voters yields an \(i\) with \(t_i+1>k\). Each elected candidate approved by that voter contributes precisely \(1/2\) to \(P_i\), as does \(x\), giving \(P_i=(t_i+1)/2>k/2\). Thus ordinary EJR+ implies strong EJR+ up-to-one for every nonwasteful committee with at most two voters, regardless of committee size.

**Three voters: at most three seats preclude separation.** Here no nonwastefulness is needed. Given \((S,x)\), put \(a=|S\cap V_x|\in\{1,2,3\}\) and apply ordinary EJR+ to \(S\cap V_x\). Some approving voter \(i\) satisfies \(t_i+1>ka/3\), hence \(t_i\ge\lfloor ka/3\rfloor\). Every selected candidate approved by \(i\) contributes at least \(1/3\) to \(P_i(S,x)\), and \(x\) contributes \(1/a\), so

\[
P_i(S,x)\ge\frac{\lfloor ka/3\rfloor}{3}+\frac1a>\frac{k}{3}
\qquad(k=1,2,3;\ a=1,2,3).
\]

For transparency, the nine respective lower bounds, ordered by \(a=1,2,3\), are \((1,1/2,2/3)\) when \(k=1\), \((1,5/6,1)\) when \(k=2\), and \((4/3,7/6,4/3)\) when \(k=3\); each triple strictly exceeds \(k/3\). Thus ordinary EJR+ implies strong EJR+ up-to-one whenever \(n=3\) and \(k\le3\). A violation requires at least one unelected candidate, so \(|C|\ge k+1=5\) at the sharp four-seat boundary.

**Replication.** For each integer \(r\ge1\), replace each displayed voter by \(r\) identical copies; keep \(W,C\) fixed. Satisfaction per voter remains \(2,2,3\). The ordinary EJR+ bound for any coalition of at most \(2r\) supporters of \(e\) is at most \(8/3<3\), so the axiom holds. The full \(3r\)-voter coalition has strong payment expression \(4/(3r)\) for every voter, equal to its per-voter entitlement \(k/(3r)\), so the strengthened axiom fails. Every strict-blocking coalition either contains a fully satisfied type-three voter or consists of at most \(2r\) voters, who cannot afford three candidates, proving core stability. Pareto efficiency is unchanged.

## Verification

The accompanying `checker.py` independently implements both axioms from their quantified definitions using exact rational arithmetic, tests the explicit witness and replication factors 1 through 3, and directly enumerates strict-core deviations and Pareto improvements. It also exhaustively checks 12,746 small profile/committee-size cases with one to three voters and four candidates (requiring nonwastefulness for at most two voters), consistently finding that ordinary EJR+ implies strong EJR+ up-to-one below the stated threshold. This finite exploration checks implementation and low-dimensional boundaries; the proof above, not finite enumeration, establishes the universal statements and the infinite replication family. Run: `python checker.py` with Python 3.10 or later and no external dependencies.

## Relationship to prior work

Brill and Peters [2] introduced ordinary EJR+ for approval committees. Skowron [1] introduced the payment-based strong EJR+ up-to-one criterion and supplied a separation from ordinary EJR+ and the ordinary core in Example 4, using 1000 voters, 30 candidates, and 20 seats. The present claim is **not** the existence of that separation: it is the sharp small-electorate/seat/candidate boundary under nonwastefulness, a five-candidate Pareto-efficient core-stable witness, and its replication family. Example 4 in [1] implies neither these minima nor Pareto efficiency of the much smaller witness. The result does not establish uniqueness of the witness or minimality without nonwastefulness.

## Limitations

These are approval-additive, unit-cost committee elections with the strict payment definition in [1, (6)] and the strict-blocking ordinary core, not other similarly named strong representation axioms. The two-voter lower bound specifically needs nonwastefulness; without it, ordinary EJR+ can differ from strong EJR+ up-to-one with two voters. The three-voter small-seat bound does not need nonwastefulness. This is a same-study mathematical proof and a finite independent-definition checker, not external certification; unindexed equivalent small examples could affect novelty.

## References

[1] Piotr Skowron, *Robust Proportionality Axioms for Additive Utilities*, arXiv:2610.15516v1, first submitted 11 October 2026, particularly Definition 4 (6) and Example 4. https://arxiv.org/html/2610.15516v1

[2] Markus Brill and Jannik Peters, *Robust and Verifiable Proportionality Axioms for Multiwinner Voting*, arXiv:2302.01989v1, first submitted 3 February 2023, Section 3.2. https://arxiv.org/html/2302.01989v1

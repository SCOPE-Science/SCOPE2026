# Sharp monotonicity boundary for full justified representation plus

## Finding
For the Hare-quota form of full justified representation plus (FJR+) of Teh (2026), increasing approvals for members of a fixed elected committee cannot destroy FJR+ at committee sizes \(k=1\) or \(k=2\). At \(k=3\), FJR+ is also monotone whenever the electorate has \(n\le3\) voters or the candidate set has \(m\le4\) candidates. These three sharp restrictions fail simultaneously: with \(n=4\), \(k=3\), and \(m=5\), adding exactly one approval for an elected candidate can turn a valid FJR+ committee into an invalid one.

This establishes the first possible number of seats, voters (at that seat count), and candidates (at that seat count) for a witness of nonmonotonicity, strengthening the previously published six-voter, four-seat example without changing the FJR+ definition.

## Assumptions and scope
Let \(N\) be a nonempty finite voter set of cardinality \(n\), \(C\) a finite candidate set of cardinality \(m\ge k\ge1\), and \(W\subseteq C\) a fixed \(k\)-member committee. Voter \(i\) has approval ballot \(A_i\subseteq C\) and selected satisfaction \(u_i=|A_i\cap W|\). Put \(q=n/k\). A **winner-approval expansion** replaces each \(A_i\) by \(A'_i\supseteq A_i\) with \(A'_i\setminus A_i\subseteq W\), retaining \(W\).

For a representation level \(\ell\in\{1,\dots,k\}\), a fractional violation consists of nonnegative weights \(z_i,y_c,x_{ic}\), with \(Z=\sum_i z_i>0\) and \(Y=\sum_c y_c\), satisfying:

1. \(z_i=0\) whenever \(u_i\ge\ell\).
2. \(x_{ic}=0\) whenever \(c\notin A_i\).
3. \(\sum_c x_{ic}=\ell z_i\) for each voter.
4. \(x_{ic}\le y_c\) for all voters and candidates.
5. \(x_{iw}\le z_i\) for every selected candidate \(w\in W\).
6. \(Z\ge qY\).

A committee is FJR+ if no such certificate exists at any level. **The cap in item 5 is essential.** This is the source's Hare FJR+, not Droop FJR+, ordinary FJR, or temporal FJR+.

## Proof
**1. The first and last representation levels.** At level \(\ell=1\), no newly approved elected candidate is approved by any voter still below level one. Thus a violation after a winner-approval expansion is already a violation before it. At \(\ell=k\), for every putative fractional violation, summing conditions 3 and 4 gives
\[
 kZ=\sum_{i,c}x_{ic}\le\sum_{c}|\{i:z_i>0,\ c\in A_i\}|y_c\le nY.
\]
Since the violation also requires \(Z\ge(n/k)Y\), equality holds throughout. For some voter with \(z_i>0\), fewer than \(k\) selected candidates are approved, and condition 5 means that the full required \(kz_i\) cannot be assigned exclusively to elected candidates. Consequently some unelected \(d\in C\setminus W\) has \(y_d>0\). Equality in the degree bound forces this \(d\) to be approved by all \(n\) voters, each of whom must still have utility below \(k\). They were also below \(k\) before the expansion; hence \(d\) already yielded a level-\(k\) EJR+ (and therefore FJR+) violation before the expansion: set \(z_i=1/k\) for all voters, \(y_d=1\), \(x_{id}=1\), and all other weights zero. Thus the top level cannot newly violate FJR+. Combining the two levels proves monotonicity for \(k\le2\).

**2. At three seats, at most one unelected candidate.** Only level \(\ell=2\) remains. If \(m=k=3\), each underrepresented voter approves at most one member of \(W\) and no unelected candidate, so condition 5 precludes positive voter weight. If \(m=4\), let \(d\) be the unique unelected candidate, and let \(S\) contain all post-expansion voters below level two who approve \(d\). A voter below level two who does not approve \(d\) cannot carry positive weight: they have at most one approved elected candidate, whose assignment is at most their weight. Since the original profile satisfies FJR+, its EJR+ consequence gives \(|S|<2q\), for otherwise the group \(S\) and unelected \(d\) already violate EJR+ at level two before the expansion. All positive voter weights lie in \(S\), so conditions 3 and 4 imply
\[
 2Z=\sum_{c}\sum_{i\in S}x_{ic}\le |S|\sum_c y_c<2qY,
\]
contradicting \(Z\ge qY\). Hence no nonmonotonicity is possible with \(m\le4\).

**3. At three seats, at most three voters.** Here \(q=n/3\le1\). In an initially FJR+ profile, any voter with no approved elected candidate must approve no candidate at all: otherwise that voter and one unelected approved candidate form a level-one EJR+ violation, since one voter meets the Hare quota. Under winner-approval expansion, such a voter remains irrelevant to a level-two fractional violation: if still below level two, they approve at most one newly approved elected candidate and no unelected candidates, and condition 5 prevents \(2z_i\) being assigned when \(z_i>0\). Any other voter below level two after expansion had exactly one initially approved elected candidate; if their selected utility remains below two, their ballot has not changed. Thus every positive-weight post-expansion level-two certificate is already a feasible pre-expansion certificate. The level-one and level-three cases were addressed in Step 1. Therefore \(n\le3\) forbids nonmonotonicity at \(k=3\).

**4. The minimal four-voter, five-candidate witness.** Set
\[
 C=\{a,b,c,d,e\},\quad W=\{a,b,e\},\quad
 (A_1,A_2,A_3,A_4)=(\{c\},\{a,c\},\{a,d\},\{a,d\}).
\]
Here \(q=4/3\). Write \(A=y_a\), \(B=y_c\), and \(D=y_d\). At level one only voter one is underrepresented; its possible assignment gives \(Z\le y_c\le Y<qY\). At level two, all four voters are underrepresented and conditions 2–5 imply
\[
 z_1\le B/2,\quad
 z_2\le\min\{B,(A+B)/2\},\quad
 z_3+z_4\le\min\{2D,A+D\}.
\]
Convex combinations of these valid upper bounds give
\[
 \begin{aligned}
 z_2&\le A/4+3B/4,\\
 z_3+z_4&\le3A/4+5D/4,\\
 Z&\le A+5(B+D)/4\le (5/4)Y<(4/3)Y.
 \end{aligned}
\]
At level three, candidate \(a\) has three approvers, candidates \(c,d\) have two each, and \(b,e\) none. Hence \(3Z\le3y_a+2y_c+2y_d\le3Y\), which excludes \(Z\ge qY\). The original committee satisfies FJR+ at every level.

Now let voter one add approval of the elected candidate \(a\), so the four ballots are \(\{a,c\},\{a,c\},\{a,d\},\{a,d\}\). For \(\ell=2\) choose \(z_i=1\) for all four voters, \(y_a=y_c=y_d=1\) and all other candidate weights zero. Assign \(x_{ia}=1\) to each voter, and assign one further unit to \(c\) for voters one and two or to \(d\) for voters three and four. All constraints, including elected-candidate caps, hold, while \(Z=4=(4/3)\cdot3=qY\). This is an FJR+ violation caused by exactly one winner-approval addition. Steps 1–3 prove simultaneous minimality of \(k=3\), \(n=4\), and \(m=5\) in their stated senses. \(\square\)

## Verification
An accompanying pure-Python exact-rational script verifies the witness, the level-two fractional certificate, and the coefficient identities used in the initial-profile bound. An additional finite grid check is a consistency test only; the universal impossibility statements for smaller parameters follow from the proof, not enumeration. Run \(\texttt{python verify.py}\).

## Relationship to prior work
Teh (2026, arXiv:2608.11500v1), Definition 3.1 and Proposition 5.5 with Appendix D.1, introduced the precise FJR+ constraints and proved nonmonotonicity with six voters, four seats and seven candidates. The result above strengthens that statement to a sharp minimal parameter frontier; it does not purport to reintroduce the source's general nonmonotonicity observation. Dong and Peters (2026) studied monotonicity of related proportionality notions, especially EJR+ and PJR+, before the Teh FJR+ definition. No searched source established this three-seat/four-voter/five-candidate boundary or the universal two-seat preservation, but absence from a search is not a proof of priority.

## Limitations
All claims concern the stated Hare FJR+ certificate and winner-approval expansions. No statement about the source's Droop variant, temporal FJR+, strategic manipulation, individual voting rules, or random profiles is implied. The fractional certificate and analytic inequalities establish mathematical correctness, not independent validation or comprehensive literary priority. A particular hidden or inaccessible earlier treatment of low-parameter FJR+ monotonicity remains a residual possibility.

## References
- Nicholas Teh. *Strengthening Full Justified Representation: Efficient Verification and Computation*. arXiv:2608.11500v1, first submitted 11 August 2026. Definition 3.1, Theorem 3.3, Proposition 5.5, Appendix D.1. https://arxiv.org/html/2608.11500v1
- Chris Dong and Jannik Peters. *An Axiomatic Analysis of Proportionality Notions in Approval-Based Multiwinner Voting*. arXiv:2605.04612, first submitted 6 May 2026. https://arxiv.org/abs/2605.04612

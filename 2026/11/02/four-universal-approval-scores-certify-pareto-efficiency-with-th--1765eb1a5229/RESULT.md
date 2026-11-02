# Four universal approval scores certify Pareto efficiency with three voters

## Finding
Let an approval election have at most three voters, an arbitrary finite candidate set \(C\), and a fixed committee size \(0\le k\le |C|\). A candidate's approval vector is \(a(c)\in\{0,1\}^3\), padding missing voters with zero coordinates. A committee \(W\subseteq C\) has utility vector \(u(W)=\sum_{c\in W}a(c)\). The following are equivalent:

1. \(W\) is Pareto optimal among all size-\(k\) committees: no \(T\subseteq C\) with \(|T|=k\) has \(u(T)\ge u(W)\) coordinatewise and strict inequality in at least one coordinate.
2. \(W\) maximizes \(w\cdot u(T)\) over size-\(k\) committees for **at least one** of the four positive, election-independent weight vectors
   \[
   \mathcal W=\{(1,1,1),(2,1,1),(1,2,1),(1,1,2)\}.
   \]
3. \(W\) is fractionally Pareto optimal: no \(x\in[0,1]^C\) with \(\sum_{c\in C}x_c=k\) yields coordinatewise utility at least \(u(W)\) with a strict improvement for some voter.

Thus the ordinary and fractional Pareto frontiers coincide for any number of candidates and any committee size with at most three voters. The four fixed score vectors give a direct certificate and an \(O(|C|\log|C|)\) test for membership in the Pareto frontier (sort the candidate scores and compare to the four top-\(k\) sums).

## Assumptions and scope
Each voter either approves or disapproves each candidate. Utilities are *additive unit approval counts*, not arbitrary positive weights or nonlinear satisfaction functions. A committee is a distinct-candidate subset of exactly \(k\) candidates; multiple candidates may have identical approval patterns. Pareto improvement requires weak improvement for every voter and strict improvement for at least one. All counts, ties and boundary committee sizes \(k=0\) and \(k=|C|\) are included. The fractional benchmark is the cardinality-\(k\) hypersimplex \(\{x\in[0,1]^C:\sum x_c=k\}\).

## Proof
It suffices to consider exactly three coordinates, using zero padding otherwise. Write \(e_i\) for the singleton approval vector of voter \(i\), \(p_i=\mathbf1-e_i\) for the pair approved by the other two voters, and \(\mathbf0,\mathbf1\) for the empty and full approval types.

**Dominance observation.** If \(c\in W\) and \(d\notin W\) satisfy \(a(d)\ge a(c)\) coordinatewise with one strict coordinate, replacing \(c\) by \(d\) Pareto-dominates \(W\). Thus, in a Pareto-optimal committee, no unselected \(\mathbf1\)-candidate can coexist with a selected candidate of another type; similarly, no selected \(\mathbf0\)-candidate can coexist with an unselected nonzero candidate. Moreover, if a selected singleton has type \(e_i\) and an unselected pair has type \(p_j\) with \(i\ne j\), then
\[
p_j-e_i=\mathbf1-e_j-e_i=e_h>0
\]
for the third voter \(h\), again a strict Pareto improvement. This observation is valid for each individual candidate, even when types repeat.

Fix a Pareto-optimal \(W\). **Case 1:** no selected candidate has singleton type, or every pair-type candidate is selected. Then \(W\) contains the highest-scoring candidates for \(w=(1,1,1)\). Indeed, the score levels are \(3\) for full approval, \(2\) for pair approval, \(1\) for singleton approval and \(0\) for no approval. In the first subcase, any omitted higher-scoring candidate would dominate a selected zero type or a selected lower type (a full type dominates any pair); a selected pair may coexist with omitted singleton candidates because its score is larger. In the second subcase, every pair is already selected, and the dominance observation excludes an omitted full type alongside a lower selected type and excludes selected zero types alongside omitted positive types. Hence no excluded candidate has a strictly higher score than an included one; \(W\) maximizes total approvals.

**Case 2:** some selected singleton exists and some pair candidate is not selected. Choose an unselected pair of type \(p_j\). The dominance observation forces *every* selected singleton to have type \(e_j\). Applying the same observation to the chosen selected singleton shows that *every* unselected pair must be of type \(p_j\); all pair candidates \(p_i\) with \(i\ne j\) are selected. Use the weight vector \(w^{(j)}\) assigning weight \(2\) to voter \(j\) and weight \(1\) to the other voters. Its score levels are:
\[
\begin{array}{c|ccccc}
\text{candidate type}&\mathbf1&p_i\ (i\ne j)&e_j,\ p_j&e_i\ (i\ne j)&\mathbf0\\\hline
w^{(j)}\cdot a(c)&4&3&2&1&0.
\end{array}
\]
All score-\(3\) candidates are selected. No full-approval candidate is omitted while a lower-scoring candidate is selected. Every selected singleton has score \(2\). A selected zero candidate would force every nonzero candidate to be selected, contradicting the existence of an omitted pair. Therefore no unselected candidate has higher \(w^{(j)}\)-score than a selected candidate. The committee maximizes this positive weighted score. This covers all possible Pareto-optimal committees, proving (1) implies (2).

For any strictly positive \(w\), a maximizer of \(w\cdot u\) cannot be Pareto-dominated, so (2) implies (1). The same maximizer is also optimal over the fractional hypersimplex because that hypersimplex is the convex hull of size-\(k\) indicator vectors: every fractional feasible point is a convex combination of integral committees, and a linear score cannot exceed its maximum at a vertex. A fractional Pareto improvement would strictly increase \(w\cdot u\), contradicting weighted optimality. Hence (2) implies (3). Conversely an integral Pareto dominator is also a feasible fractional dominator, so (3) implies (1). The three assertions are equivalent.

For \(k=0\), \(k=|C|\), or \(C=\varnothing\), the unique committee is optimal for every weight, and the same reasoning applies.

## Verification
Run `python3 verify_three_voter.py` in the same directory. The checker independently computes all attainable three-coordinate utility vectors and exact integral Pareto dominance, then tests equality with the union of four weighted maximizer sets. It exhausts all \(3^8=6561\) candidate-type capacity vectors with multiplicities \(0,1,2\) for all eight approval types and all feasible committee sizes, and additionally 400 deterministic, seeded higher-multiplicity profiles. The completed check reported **1,620,453** utility-profile comparisons and no disagreement. This is a finite stress test only; the proof above covers arbitrary numbers and multiplicities of candidates.

## Relationship to prior work
Schünke, *Pareto Optimality in Approval-Based Multiwinner Voting* (first posted May 28, 2026, arXiv:2605.30490), establishes committee reconfiguration and monotonicity for candidate-interval and voter-interval domains, and discusses open structural questions on unrestricted approval domains. Becker, Boehmer, Frank and Glessen, *Fractional Pareto-Optimality in Multiwinner Voting* (first posted June 9, 2026, arXiv:2606.11160), identify positive weighted welfare maximization as a characterization of fractional Pareto optimality and establish its structural properties. The present theorem states an additional uniform implication, *integral Pareto optimality implies fractional Pareto optimality*, for **every** approval profile with at most three voters; the four explicit universal weights are stronger than merely an instance-dependent separating weight.

This domain is not covered simply by the standard interval assumptions: take three candidates each approved by a different pair of three voters, so the three pairwise two-element approval sets occur. No linear order on the three voters makes all three two-element sets intervals, and no linear order on the three candidates makes all three voters' two-element approval sets intervals. A separate sparse-ballot coincidence theorem restricts each voter's *number of approved candidates* rather than the *number of voters*, so it does not imply the present unrestricted three-voter result.

## Limitations
The result is specialized to at most three unit-approval voters. No extension to four or more voters, arbitrary additive approval intensities, costs or budget constraints is asserted. The checker covers only the stated finite families and is not an infinite proof. The full text of the directly relevant fractional Pareto-optimality paper was not available in this examination, so an uninspected equivalent observation or appendix remains a publication-priority risk; the novelty comparison is qualified accordingly. No independent validation has been performed.

## References
- Joshua Schünke (2026), *Pareto Optimality in Approval-Based Multiwinner Voting*, arXiv:2605.30490, https://arxiv.org/abs/2605.30490 (v1 May 28, 2026).
- Patrick Becker, Niclas Boehmer, Fabian Frank and Lara Glessen (2026), *Fractional Pareto-Optimality in Multiwinner Voting*, arXiv:2606.11160, https://arxiv.org/abs/2606.11160 (v1 June 9, 2026).

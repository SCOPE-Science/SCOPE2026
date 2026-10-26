# Five voters are necessary and sufficient for Pareto failure of exact local PAV with two seats

## Finding

**Theorem (sharp electorate threshold and unique minimal obstruction).** Consider any finite unweighted approval election, with any number of candidates, committee size exactly \(2\), and at most \(4\) voters. Every committee that admits no **strictly PAV-improving one-candidate swap** is Pareto optimal for approval-count utilities. This fails with exactly \(5\) voters and \(4\) candidates. If an exact one-swap-local committee of size \(2\) is Pareto dominated in an election of exactly \(5\) voters, the two committees are disjoint; on their four candidates the five ballots are, up to relabeling the two members of each committee,

\[
\{w_0,a_0\},\quad\{w_0,a_1\},\quad\{w_1,a_0\},\quad\{w_1,a_1\},\quad\{w_0,a_0,a_1\}.
\]

For elections with additional candidates, the uniqueness statement concerns ballot restrictions to the four candidates in the two committees, not irrelevant approvals of outside candidates. Four candidates are necessary for any such failure. The boundary counts local maxima with ties allowed, not only strict local maxima.

## Assumptions and scope

An approval election comprises a finite candidate set \(C\), a set \(N\) of \(n\ge1\) equally weighted voters, and approval subsets \(A_i\subseteq C\), which may be empty. The feasible committees are pairs \(W\subseteq C\) of size \(2\). Define approval utility \(u_i(W)=|A_i\cap W|\). Define \(H_0=0\), \(H_1=1\), \(H_2=3/2\), and \(\operatorname{PAV}(W)=\sum_{i\in N}H_{u_i(W)}\). An **exact swap-local maximum** has \(\operatorname{PAV}((W\setminus\{w\})\cup\{a\})\le\operatorname{PAV}(W)\) for every \(w\in W\), \(a\in C\setminus W\). A committee \(O\) **Pareto dominates** \(W\) if \(u_i(O)\ge u_i(W)\) for every voter and the inequality is strict for at least one voter. No fractional committees or approximate local-search tolerances are considered.

## Proof

**Step 1: reduce to four distinguished candidates.** Suppose a swap-local \(W\) is dominated by \(O\). If \(|W\cap O|=1\), replacing the unique member of \(W\setminus O\) by the member of \(O\setminus W\) is a single swap. Because harmonic scores strictly increase with each voter's approval utility, this Pareto improvement strictly raises PAV, contradiction. Hence \(W\cap O=\varnothing\). Name their candidates \(W=\{w_0,w_1\}\) and \(O=\{a_0,a_1\}\). All of the four swap comparisons between \(W\) and \(O\), as well as the dominance comparison, depend only on each ballot's restriction to these four candidates. Thus other candidates cannot invalidate the following lower bound.

**Step 2: total-swap contribution table.** For a voter write \(u=|A_i\cap W|\), \(v=|A_i\cap O|\), and let \(S_i\) be the sum of this voter's PAV-score changes over the four swaps replacing one member of \(W\) by one member of \(O\). Pareto dominance forces \(v\ge u\). Directly evaluating the four harmonic differences gives the complete table

| \((u,v)\) | \((0,0)\) | \((0,1)\) | \((0,2)\) | \((1,1)\) | \((1,2)\) | \((2,2)\) |
|---|---:|---:|---:|---:|---:|---:|
| \(S_i\) | \(0\) | \(2\) | \(4\) | \(-1/2\) | \(1\) | \(0\) |

For transparency, when \(u=0\), a swap that elects an approved alternative increases the harmonic score by \(1\) and either alternative can replace either winner, giving \(S_i=2v\). When \(u\in\{1,2\}\), dropping an approved current winner yields a loss \(1/u\) unless an approved alternative restores it; swapping in an approved alternative while retaining current utility \(u\) yields a gain \(1/(u+1)\). Summing these four changes gives \(S_i=3v/(u+1)-2\). A local maximum has all four swap gains nonpositive, and consequently \(\sum_iS_i\le0\).

**Step 3: rule out small electorates.** A strict Pareto improvement must include a voter of one of three types \((0,1)\), \((0,2)\), or \((1,2)\).

If there is a \((0,1)\) voter, its positive total-swap contribution is \(2\), while every other voter contributes at least \(-1/2\). Therefore at least four further voters are needed: \(n\ge5\). If there is a \((0,2)\) voter, its contribution \(4\) requires at least eight others: \(n\ge9\).

Suppose there is a voter of type \((1,2)\), and rename the winners so that this voter approves \(w_0,a_0,a_1\) but not \(w_1\). She contributes \(1/2\) to each of the swaps \(w_1\to a_0\) and \(w_1\to a_1\). Within the Pareto-compatible type table, a **negative** contribution to \(w_1\to a_0\) is possible only from the cross voter with ballot \(\{w_1,a_1\}\), and a negative contribution to \(w_1\to a_1\) only from the cross voter with ballot \(\{w_1,a_0\}\). Thus both distinct voters are necessary. The first cross voter also makes a positive \(1/2\) contribution to \(w_0\to a_1\), which can be offset only by the cross voter \(\{w_0,a_0\}\). Similarly, the second makes a positive \(1/2\) contribution to \(w_0\to a_0\), requiring the distinct cross voter \(\{w_0,a_1\}\). These four cross voters together with the original strict-improvement voter prove \(n\ge5\). This argument does not assume that all other voters have a particular type; it uses the complete possibilities for negative single-swap contributions.

We have therefore proved that no Pareto-dominated exact swap-local committee exists with fewer than five voters.

**Step 4: classify all five-voter equality cases.** A \((0,2)\) voter cannot occur. If a \((0,1)\) voter occurs, there must be exactly four other voters, all of type \((1,1)\), and the total four-swap gain equals zero. Hence each individual gain must be zero. Rename the alternatives so the strict-improvement voter approves only \(a_0\). Let \(x\) be the number of \(\{w_0,a_0\}\) ballots and \(y\) the number of \(\{w_1,a_1\}\) ballots. The zero-gain equations for \(w_0\to a_1\) and \(w_1\to a_0\) read

\[
-x+\frac{y}{2}=0,\qquad 1-y+\frac{x}{2}=0.
\]

They force \(x=2/3\), incompatible with integer ballot counts. Thus the five-voter case must contain a \((1,2)\) voter. The necessity argument in Step 3 forces the other four ballots to be exactly the four different cross ballots. This is the claimed unique restricted profile, up to the symmetry of the selected and alternative candidate pairs.

**Step 5: establish sharpness.** Take exactly those five ballots and four candidates. Each voter has utility \(1\) under \(W\), so \(\operatorname{PAV}(W)=5\). The four cross voters still have utility \(1\) under \(O\), while the fifth has utility \(2\), giving \(\operatorname{PAV}(O)=11/2\). The four swaps \(w_0\to a_0\), \(w_0\to a_1\), \(w_1\to a_0\), \(w_1\to a_1\) have respective PAV-score changes \(-1/2,-1/2,0,0\), so \(W\) is indeed an exact swap-local maximum despite Pareto domination. If there were only three candidate names, any two distinct size-two committees would overlap and Pareto domination would contradict swap locality, proving candidate minimality as well. \(\square\)

## Verification

The self-contained `VERIFY.py` uses twice the PAV objective, so every comparison is performed with exact integers. It enumerates every unlabeled-voter multiset of Pareto-compatible ballot restrictions on four candidates for electorate sizes \(1\) through \(5\), retaining only profiles that have at least one strictly improved voter and whose four single-swap scores are all nonpositive. It finds exactly \(0,0,0,0,2\) labeled-candidate multiset profiles, respectively. The two profiles differ by swapping the names of the current winners and form one symmetry orbit. The code independently checks the complete six-type swap-sum table, verifies the witness utilities and four swap gains, and raises an assertion on any disagreement. Run from the extracted package directory with `python VERIFY.py` using Python 3 and no additional packages. The infinite candidate-count assertion relies on the analytic reduction and proof, **not** on the finite census.

## Relationship to prior work

Peters, Vaish and Yadav (arXiv:2609.07554v1, publicly available 2026-09-07), Section 3.1 and Appendix B, prove weak Pareto optimality for local PAV and explicitly construct exactly local-optimal yet Pareto-dominated committees for arbitrary committee size. Their Appendix B counterexample at size \(2\) has \(4M+2\) voters with \(M\ge2\), hence at least \(10\) voters, and they do not prove a universal minimum electorate or classify the first witness. The new statement sharpens this *electorate-size obstruction*, not the established failure of full Pareto optimality. Schünke (arXiv:2605.30490v1, 2026-05-28) characterizes Pareto committees on interval domains and studies reconfiguration, not swap-local PAV's sharp voter threshold. Kraiczy and Elkind (ESA 2024, DOI:10.4230/LIPIcs.ESA.2024.82) investigate local PAV convergence complexity rather than this PO boundary.

## Limitations

The theorem concerns unweighted voters, integral committee size \(2\), additive approval-count utility, the harmonic PAV objective, and exact one-swap local maxima (no strict-gain swaps); different objective scores, approximate tolerances, and larger committees are not covered. The five-voter uniqueness claim is for ballot restrictions to the four candidates of a specified dominated/local-maximum pair. The proof does not classify irrelevant approvals outside those candidates or independent voting profiles at larger sizes. The comparison with available indexed literature does not establish formal publication priority; unindexed equivalent statements remain a residual risk. This is a mathematical statement and reproducibility check, not an independently audited certificate.

## References

1. Dominik Peters, Rohit Vaish, and Jatin Yadav, *Finding Representative and Approximately Efficient Committees*, arXiv:2609.07554v1, 2026-09-07. https://arxiv.org/html/2609.07554v1. Especially Section 3.1 and Appendix B (exact local-PAV counterexample).
2. Joshua Schünke, *Pareto Optimality in Approval-Based Multiwinner Voting*, arXiv:2605.30490v1, 2026-05-28. https://arxiv.org/html/2605.30490v1.
3. Sonja Kraiczy and Edith Elkind, *A Lower Bound for Local Search Proportional Approval Voting*, ESA 2024, DOI:10.4230/LIPIcs.ESA.2024.82. https://doi.org/10.4230/LIPIcs.ESA.2024.82.

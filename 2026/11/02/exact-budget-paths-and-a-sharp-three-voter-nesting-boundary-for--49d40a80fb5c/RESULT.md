# Exact budget paths and a sharp three-voter nesting boundary for equal shares

## Finding

The uncompleted approval-based Method of Equal Shares (MES) has an exact, budget-monotone solution on every *sunflower approval profile*: all distinct voter ballots consist of the same common core and pairwise-disjoint private petals. For arbitrary real virtual budgets, each candidate has an explicit entry threshold; in particular, no funded candidate is ever removed when the virtual budget increases. This property holds for every profile with at most two distinct approval ballots and is sharp with respect to the number of voters: a three-voter, four-candidate profile can lose a funded candidate when the budget increases from \(3\) to \(4\).

More precisely, let the finite candidate universe have a fixed strict priority order \(\prec\). Suppose that \(h\geq1\) nonempty groups of \(n_j\geq1\) voters, for \(j=1,\ldots,h\), each approve exactly \(C\cup P_j\), where \(C,P_1,\ldots,P_h\) are pairwise disjoint candidate sets except that the common \(C\) occurs in every ballot. The private petals \(P_j\) may be empty; candidates approved by no one are never selected. Let \(n=\sum_{j=1}^h n_j\) and \(u=|C|\). Each candidate costs one, and each voter initially receives virtual budget \(B/n\), for any \(B\geq0\).

For a finite candidate set \(S\), write \(S^{[q]}\) for its first \(\min\{|S|,q\}\) candidates under \(\prec\), where \(q\) is a nonnegative integer. The uncompleted MES outcome is exactly

\[
W(B)=\begin{cases}
C^{[\lfloor B\rfloor]},&0\leq B<u,\\[2pt]
C\ \cup\displaystyle\bigcup_{j=1}^h P_j^{[\lfloor n_j(B-u)/n\rfloor]},&B\geq u.
\end{cases}
\]

Equivalently, common candidates enter at budgets \(1,2,\ldots,u\), and the \(\ell\)-th priority-ranked private candidate in group \(j\) enters at budget \(u+n\ell/n_j\), for \(1\leq\ell\leq |P_j|\). Hence \(B\leq B'\) implies \(W(B)\subseteq W(B')\) for every nonnegative real pair of budgets. These thresholds describe the entire parametric output path, including nonintegral group quotas and budget values.

This is sharp in voter count. With candidates ordered \(A\prec B\prec C\prec D\), three voters respectively approving \(\{A,B\}\), \(\{A,B,D\}\), and \(\{C,D\}\), uncompleted MES returns
\[
W(3)=\{A,B,C\},\qquad W(4)=\{A,B,D\}.
\]
No profile with one or two voters exhibits such a failure under the specified rule, since every such profile has at most two distinct approval ballots and therefore admits a sunflower representation. The counterexample uses the specified fixed candidate tie priority; no tie-independent phenomenon or minimum candidate count is asserted.

## Assumptions and scope

Only the **uncompleted** approval-based MES purchase phase is studied, not any subsequent completion by sequential Phragmén, greedy funding, or virtual-budget optimization. At each iteration a candidate with the smallest feasible per-supporter price \(\rho\) is chosen; a supporter with remaining balance \(b_i\) contributes \(\min(b_i,\rho)\). Feasibility means that the sum of these contributions equals the candidate's unit cost. A single strict candidate priority \(\prec\), independent of the total budget, breaks every price tie. Budgets are nonnegative real numbers; finite exact checks use rational budgets. All costs are one, and each group's voters have identical ballots. There are no constraints on the number of groups, petal sizes, total candidates, or group populations beyond finiteness and positivity of group populations.

## Proof

**Common-core phase.** Initially, all voter balances are \(B/n\). After \(q\) funded core candidates, each voter has paid exactly \(q/n\), hence has remaining balance \((B-q)/n\), provided \(B-q\geq0\). If the remaining total \(B-q\) is at least one and any core candidate is available, its price is exactly \(1/n\). A private candidate of group \(j\) has exactly \(n_j\) supporters; if feasible, its minimum price is at least \(1/n_j\), which is strictly larger than \(1/n\) whenever there is more than one distinct ballot type. In the one-type case all approved candidates belong to the common core. Thus an available affordable core candidate always wins over a private one; ties within the core follow \(\prec\). If \(B-q<1\), no candidate can be afforded because the aggregate remaining virtual budget is less than its unit cost. Therefore precisely \(\min(u,\lfloor B\rfloor)\) core candidates are selected before the process either stops or exhausts the core.

**Private-petal phase.** If \(B\geq u\), all core candidates are funded. Each voter then has \((B-u)/n\) remaining. The supporters of each private candidate in \(P_j\) are exactly the \(n_j\) voters of group \(j\), and no other candidate outside the core draws on their balances. Those group balances stay equal to one another. After \(\ell\) private purchases in \(P_j\), each group voter has paid an additional \(\ell/n_j\). A further private candidate in \(P_j\) is affordable exactly when
\[
n_j(B-u)/n-\ell\geq1.
\]
Every such purchase costs \(1/n_j\) per supporter; candidates within that petal have identical current affordability and are chosen in priority order. Because different petals have disjoint supporter groups, their cross-petal interleaving cannot alter either purchase count or within-petal prefix. Thus group \(j\) buys exactly \(\min\{|P_j|,\lfloor n_j(B-u)/n\rfloor\}\) projects. This proves the closed form. Taking budget thresholds of these nondecreasing integer-valued prefix counts proves nesting for all \(B\).

**At most two distinct ballots.** For arbitrary two distinct ballots \(A_1,A_2\), take \(C=A_1\cap A_2\), \(P_1=A_1\setminus A_2\), and \(P_2=A_2\setminus A_1\). These sets satisfy the assumptions. Repeated ballots only change the respective population counts. One distinct ballot is the special case \(h=1\).

**Sharp witness.** For the three listed approval ballots at budget \(3\), each voter starts with one unit. MES chooses \(A\) at price \(1/2\), then \(B\) at price \(1/2\) (lexicographic ties), exhausting the first two voters, then \(C\) at price \(1\), producing \(\{A,B,C\}\). At budget \(4\), each voter starts with \(4/3\); MES again chooses \(A,B\) at price \(1/2\) apiece. The first two balances are now \(1/3\), while the third is \(4/3\). Candidate \(D\), approved by the second and third voters, has feasible price \(2/3\) (the second contributes \(1/3\), the third \(2/3\)), strictly below candidate \(C\)'s price \(1\). Hence \(D\) enters and \(C\) does not; the remaining third-voter balance is less than one, so the phase stops. This is a strict nonnesting between budgets \(3\) and \(4\). By the two-ballot case, no profile with fewer than three voters can fail nesting; the bound is therefore exact in the number of voters.

## Verification

The standalone file `verify_mes.py` implements the actual, uncompleted MES price-minimization and payment procedure with Python rational numbers, independent of the closed-form predictor. It compares the rule against the sunflower formula in 156,245 exact cases, including all pairs of ballot patterns on up to four candidates with group multiplicities through four, and all three-petal classifications on five candidates under three population splits. It also checks the witness and its three exact candidate-price decisions at each budget. Executing `python3 verify_mes.py` prints:

```
PASS: 156245 exact sunflower formula cases; three-voter nonnesting witness, budgets 3 and 4.
```

These finite tests are not offered as a proof for infinitely many budgets, voters, or candidates; that scope follows from the argument above. The code uses no external dependencies.

## Relationship to prior work

Peters and Skowron's work establishing laminar proportionality for the Method of Equal Shares covers integral party-list quotas at a fixed committee size, including profiles consisting of a universally approved core and disjoint parties. Its definition expressly excludes nonintegral party-list instances from laminarity; the result above gives an all-real-budget output and event formula, not just fixed-size integral proportionality. The original MES literature supplies the purchase rule and its representation guarantees.

Lackner and Skowron's *Multi-Winner Voting with Approval Preferences*, Appendix A, Proposition A.2, establishes general failure of MES committee monotonicity by a four-voter example. The three-voter counterexample above sharpens that voter count specifically for the **uncompleted** purchase phase; it does not claim the published general nonmonotonicity phenomenon as new.

Kraiczy and Elkind study a distinct Adaptive Method of Equal Shares (AMES), motivated by successive virtual-budget increases, and note that MES is fragile under budget modification. Their adaptive rule and stability analysis do not supply the particular sunflower output formula, event thresholds, or three-voter boundary. Freeman, Kahng, and Pennock study proportionality for voting rules whose number of winners is itself variable, but not the MES budget-parametric problem.

## Limitations

The theorem does not extend to arbitrary intersecting support sets, as the explicit witness demonstrates. The guarantee requires unit costs, approval utilities, unchanged ballots, a common strict priority for price ties, and **no completion step**. In particular, it does not assert committee-size monotonicity for a rule completed to exactly \(k\) seats, general-cost budgeting, cardinal utilities, or tie-breaking policies that vary with the budget. It does not claim minimum candidate count or tie-independent failure. The full specialist literature may contain an equivalent structural observation that was not recovered by the searches; external priority review remains warranted. Reproducibility tests do not replace the infinite-domain proof.

## References

1. Sonja Kraiczy and Edith Elkind, *An Adaptive and Verifiably Proportional Method for Participatory Budgeting*, arXiv:2310.10215v1 (first posted 16 October 2023), https://arxiv.org/pdf/2310.10215 . Section 2 defines approval MES, Sections 3–5 study AMES and virtual-budget changes.
2. Dominik Peters and Piotr Skowron, *Proportionality and the Limits of Welfarism*, arXiv:1911.11747 (first posted 26 November 2019), https://www.dominik-peters.de/publications/proportionality.pdf . Section 3.1–3.2 defines integral laminar profiles and proves laminar proportionality.
3. Martin Lackner and Piotr Skowron, *Multi-Winner Voting with Approval Preferences*, Springer, DOI:10.1007/978-3-031-09016-5 (electronic edition first published 17 November 2022), https://link.springer.com/book/10.1007/978-3-031-09016-5 . Appendix A, Proposition A.2, gives a four-voter MES nonmonotonicity example.
4. Grzegorz Pierczyński, Dominik Peters, and Piotr Skowron, *Proportional Participatory Budgeting with Additive Utilities*, arXiv:2008.13276, https://dominik-peters.de/publications/equal-shares.pdf . Defines the extended MES rule for participatory budgeting.
5. Rupert Freeman, Anson Kahng, and David M. Pennock, *Proportionality in Approval-Based Elections With a Variable Number of Winners*, IJCAI 2020, https://ansonkahng.com/docs/papers/vnw.pdf . Different variable-size committee objectives.

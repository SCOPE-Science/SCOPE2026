# Complete EJR-1 spectra and a sharp cost-premium boundary in symmetric participatory budgets

## Finding

**Theorem (two-tier symmetric approval budgets).** Fix integers \(k\ge 2\) and \(h\ge 1\). There are \(k\) voters, \(k\) common projects each costing \(h\), and, for each voter \(i\), exactly \(h\) private projects each costing \(1\). Every voter approves all common projects and precisely her prior projects. The available budget is \(kh\).

For a feasible outcome \(W\), write \(c\) for the number of funded common projects and \(x_i\) for the number of funded private projects of voter \(i\). Thus \(hc+\sum_{i=1}^k x_i\le kh\), and \(0\le x_i\le h\). Put \(z_i=c+x_i\), and sort these scores as \(z_{(1)}\le\cdots\le z_{(k)}\). Using extended justified representation up to one project (EJR-1) in the strict-augmentation sense defined below, the following complete characterizations hold.

1. **Cost satisfaction:** \(W\) is EJR-1 for cost-based satisfaction if and only if \(c=k\), or \(c=k-1\) and \(\sum_i x_i\ge1\). The number of labeled feasible outcomes satisfying this criterion is exactly
   \[
   1+k\sum_{j=1}^{h}\binom{kh}{j}.
   \]
2. **Cardinality satisfaction:** \(W\) is EJR-1 for cardinality-based satisfaction if and only if
   \[
   z_{(j)}\ge\max\{h,j\}\quad\text{for every }1\le j\le k.
   \]
3. **Simultaneous fairness:** An outcome satisfying both versions exists if and only if \(h\le k\). For \(h>k\), the unique cardinality-EJR-1 outcome funds all private projects and no common project; it violates cost-EJR-1. For \(h\le k\), funding all common projects and no private projects satisfies both.
4. **Quantified unavoidable shortfall:** Define the private-bundle cardinality shortfall
   \[
   \delta(W)=\max_{1\le i\le k}\bigl(h-z_i\bigr)_+,
   \qquad (t)_+=\max\{t,0\}.
   \]
   Among cost-EJR-1 outcomes, its exact minimum is
   \[
   \min_{W\text{ cost-EJR-1}}\delta(W)
   =\max\left\{0,h-k+1-\left\lfloor\frac hk\right\rfloor\right\}.
   \]
   For \(h>k\), this minimum is strictly positive and is achieved by selecting \(k-1\) common projects and distributing \(h\) private project selections as evenly as possible among voters.

## Assumptions and scope

An approval-based participatory budget consists of a finite project set \(P\), a positive cost for each project, voter approval sets \(A_i\subseteq P\), and a budget \(B\). An outcome is any \(W\subseteq P\) of total cost at most \(B\); **exhaustiveness is not required**. For a voter \(i\), cardinality satisfaction is \(u_i^{\#}(W)=|W\cap A_i|\) and cost satisfaction is \(u_i^{c}(W)=\sum_{p\in W\cap A_i}\operatorname{cost}(p)\).

For a nonempty voter group \(G\) and project set \(T\), call \((G,T)\) cohesive when \(T\subseteq\bigcap_{i\in G}A_i\) and \(\operatorname{cost}(T)\le (|G|/k)B\). An outcome \(W\) satisfies \(u\)-EJR-1 when, for every such pair, either \(T\subseteq W\), or there are \(i\in G\) and \(p\in P\setminus W\) with
\[
 u_i(W\cup\{p\})>u_i(T).
\]
The hypothetical addition of \(p\) in this definition **need not itself be budget-feasible**. This is the EJR-1 variant used in Brill--Forster--Lackner--Maly--Peters (2023), not full EJR or the stronger EJR-x axiom. In particular, the strict inequality cannot be changed to a weak inequality.

The theorem concerns the specified symmetric family, integer premium \(h\), and two additive approval-satisfaction measures. The cost and cardinality conditions concern all feasible outcomes, including nonexhaustive ones. Labeling treats the individual projects as distinct.

## Proof

**Step 1 (cost criterion, necessity).** Let \(C\) contain the \(k\) common projects. The full voter group \(G=[k]\) is cohesive for \(T=C\), since \(\operatorname{cost}(C)=kh=B\). If \(c\le k-2\), at least one common project is missing. Each voter obtains cost utility \(ch+x_i\). Adding one missing common project gives at most \((c+1)h+x_i\le(c+2)h\le kh\). Adding one missing private project gives at most \(ch+x_i+1\le(c+1)h\le kh\), since a missing private project implies \(x_i\le h-1\). Adding an unapproved project does not increase utility. Thus no voter can meet the required strict inequality, and \(T\nsubseteq W\); EJR-1 fails.

If \(c=k-1\) and every \(x_i=0\), then adding the sole missing common project gives exactly \(kh\), while adding a private project gives \((k-1)h+1\le kh\). Again EJR-1 fails for \(([k],C)\). Hence cost-EJR-1 requires one of the two stated alternatives.

**Step 2 (cost criterion, sufficiency).** Suppose \(c=k\). Every cohesive group of at least two voters approves only common projects jointly, so its cohesive \(T\) is already selected. A singleton voter has budget share \(h\). Her cohesive \(T\) is either a single common project (already selected) or at most \(h\) private unit-cost projects. In the latter case, if \(T\nsubseteq W\), some approved private project is missing; adding it raises her already at-least-\(kh\) utility strictly above \(\operatorname{cost}(T)\le h\).

Suppose instead \(c=k-1\) and some \(x_i>0\). For the full group and \(T=C\), adding the missing common project yields utility \(kh+x_i>kh\) for that voter. For any group of size \(2\le g\le k-1\), every cohesive \(T\) is made of at most \(g\) common projects; if it is not already selected, it contains the sole missing common project. Adding that project yields each member utility at least \(kh>gh\ge\operatorname{cost}(T)\). For singleton groups, every cohesive \(T\) is either one common project or a set of at most \(h\) private projects; any unselected approved project strictly raises current utility, which is already at least \((k-1)h\ge h\). This proves cost-EJR-1.

To count the cost-EJR-1 outcomes, \(c=k\) forces all \(x_i=0\), giving one outcome. For \(c=k-1\), choose the omitted common project in \(k\) ways. The remaining budget is \(h\), so select any nonempty subset of at most \(h\) among the \(kh\) distinct private projects. This gives the binomial sum.

**Step 3 (cardinality criterion, necessity).** The \(h\) private projects of any one voter form a cohesive set \(T\) for that singleton, since they cost exactly her budget share \(h\). If \(T\subseteq W\), then \(z_i\ge h\). Otherwise adding any one project raises cardinality utility by at most one, and strict EJR-1 requires \(z_i+1>h\), again giving \(z_i\ge h\). Thus every \(z_i\ge h\).

If \(c<k\), select any group \(G\) of \(g\ge2\) voters and a set \(T\) of \(g\) common projects including at least one unselected common project. It is cohesive because its cost is \(gh\), exactly the group's budget share. Since \(T\nsubseteq W\), strict EJR-1 requires that some member of \(G\) have \(z_i+1>g\), or \(\max_{i\in G}z_i\ge g\). Taking the group of the \(g\) lowest-score voters gives \(z_{(g)}\ge g\). If \(c=k\), the same inequalities hold automatically because every score is at least \(k\). Together with \(z_i\ge h\), the sorted criterion follows.

**Step 4 (cardinality criterion, sufficiency).** Suppose the sorted criterion holds. A singleton cohesive \(T\) is either a common project, of size one, or a set of at most \(h\) private projects. If it is not selected, there is an approved missing project whose hypothetical addition gives cardinality at least \(z_i+1>h\ge|T|\). For a group \(G\) of \(g\ge2\), any cohesive \(T\) consists of at most \(g\) common projects. If \(T\) is not selected, a common project is missing. The largest cardinality score of a member of \(G\) is at least \(z_{(g)}\ge g\); adding the missing common project yields utility greater than \(g\ge|T|\). Therefore every cohesive pair satisfies cardinality-EJR-1.

**Step 5 (compatibility and sharpness).** If \(h>k\), the singleton conditions \(x_i+c\ge h\) imply \(\sum_i x_i\ge k(h-c)\). Budget feasibility gives \(\sum_i x_i\le(k-c)h\), hence \(c(h-k)\le0\). Since \(h>k\) and \(c\ge0\), necessarily \(c=0\), and then \(x_i=h\) for all voters. This unique feasible outcome satisfies the full cardinal criterion because \(z_i=h>k\), but fails the cost criterion. If \(h\le k\), funding all common projects has \(c=k\), \(x_i=0\), and all \(z_i=k\ge\max\{h,j\}\), so it satisfies both criteria.

**Step 6 (sharp shortfall).** Among cost-EJR-1 outcomes, either \(c=k\), forcing \(x_i=0\) and \(\delta=(h-k)_+\), or \(c=k-1\) with at least one private project selected. In the latter case \(\sum_i x_i\le h\) and thus \(\min_i x_i\le\lfloor h/k\rfloor\). Consequently
\[
\delta\ge\bigl(h-k+1-\lfloor h/k\rfloor\bigr)_+.
\]
Choose exactly \(h\) private projects, distributing their counts to differ by at most one: each count is \(\lfloor h/k\rfloor\) or \(\lceil h/k\rceil\). With \(c=k-1\) this is feasible and cost-EJR-1, and it attains the displayed bound. For \(h>k\), the bound is at most \(h-k\) because \(\lfloor h/k\rfloor\ge1\); for \(h\le k\), selecting all common projects attains zero. The stated minimum follows. For integer \(h>k\), the bound is positive. \(\square\)

## Verification

The standalone `verify_ejr1.py` recomputes the EJR-1 predicate **directly from the quantifiers**: for each tested parameter pair it enumerates all feasible funded project subsets, all voter groups, all affordable jointly approved project subsets, and every hypothetical single-project addition. It independently compares both mathematical characterizations, the exact cost-EJR-1 outcome count, the simultaneous-existence boundary, and the minimal private-bundle deficit.

Run `python3 verify_ejr1.py` with Python 3.10 or later; no third-party packages are needed. The recorded run passed for \((k,h)\) in \(\{(2,1),\ldots,(2,5),(3,1),\ldots,(3,4),(4,1),\ldots,(4,3),(5,1)\}\), covering **63,191 feasible outcomes**. These finite checks are consistency tests, not an infinite-family proof; Steps 1--6 above establish the result for all integers in its scope.

## Relationship to prior work

Brill, Forster, Lackner, Maly and Peters (2023), Proposition 3.6, establish that cost-based and cardinality-based EJR-1 can be incompatible, using a two-voter example with two common projects costing \(5\), five private unit-cost projects per voter, and budget \(10\). That instance is the \((k,h)=(2,5)\) member of the present family. The earlier proposition proves qualitative incompatibility at one parameter point; it does not state the all-size cost-EJR-1 spectrum, the sorted-score criterion, the sharp \(h=k\) threshold, or the optimal shortfall formula. The present theorem credits and generalizes the example, rather than claiming the underlying incompatibility phenomenon as new.

Peters, Pierczyński and Skowron (2020/2021) establish EJR and EJR-1 guarantees for individual additive satisfaction functions via the Method of Equal Shares; those results do not assert compatibility between distinct satisfaction functions on one outcome. Later papers on additive-utility proportionality study broader algorithmic or axiom systems, but no direct coverage of this exact symmetric-family theorem was identified in the material available for comparison. This is a best-knowledge statement, not a proof of publication priority.

## Limitations

This is a complete answer **only** for the stated symmetry class with \(k\) shared projects of common cost \(h\), \(k\) disjoint private blocks of \(h\) unit-cost projects, and budget \(kh\). It does not claim a universal sharp threshold for arbitrary approval profiles, real-valued costs, other fairness axioms (including EJR-x), or optimality of a particular voting rule. The shortfall \(\delta\) measures violation of the singleton private-bundle test; it is not an overall cardinality-EJR-1 violation metric outside this family. Publication precedence beyond the inspected sources remains uncertain. No independent external audit has been performed.

## References

- Markus Brill, Stefan Forster, Martin Lackner, Jan Maly and Jannik Peters, *Proportionality in Approval-Based Participatory Budgeting*, arXiv:2302.03672, first publicly posted 2023-02-07. In particular Section 3, Definition 3.5 and Proposition 3.6; https://arxiv.org/abs/2302.03672.
- Dominik Peters, Grzegorz Pierczyński and Piotr Skowron, *Proportional Participatory Budgeting with Additive Utilities*, arXiv:2008.13276, first publicly posted 2020-08-30; https://arxiv.org/abs/2008.13276.
- Carmel Baharav, Jakob de Raaij and Agnès Totschnig, *The Complexity of Justified Representation with Additive Utilities*, arXiv:2609.02030 (related broader complexity scope; abstract comparison only); https://arxiv.org/abs/2609.02030.

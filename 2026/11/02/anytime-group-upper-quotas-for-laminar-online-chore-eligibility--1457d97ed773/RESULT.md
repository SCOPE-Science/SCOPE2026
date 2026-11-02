# Anytime group upper quotas for laminar online chore eligibility

## Finding
Let a finite set of agents receive an arbitrary-length online sequence of unit-cost indivisible chores. Each chore is eligible for assignment to a nonempty member of a **fixed, known laminar family** of agent subsets; the current eligibility set is revealed when the chore arrives, and assignments are immediate and irrevocable. There is a deterministic algorithm that, after **every prefix**, simultaneously guarantees for every group \(T\) in the laminar family (and for all singleton groups),
\[
L_t(T)-Q_t(T)<1, \qquad Q_t(T)=\sum_{j=1}^{t}\frac{|T\cap S_j|}{|S_j|},
\]
where \(L_t(T)\) counts chores actually assigned to agents in \(T\), and \(S_j\) is chore \(j\)'s eligibility set. In particular, every agent \(i\) satisfies \(L_t(\{i\})<Q_t(\{i\})+1\), hence every prefix is eligibility-aware Prop1 for unit chores. The uniform constant \(1\) is optimal: no universal smaller constant applies over all population sizes, even for a single chore.

## Assumptions and scope
There are \(n\geq1\) labeled agents \(N\) and a known, nonempty, fixed laminar family \(\mathcal F\) of subsets of \(N\). Laminar means that any two members are disjoint or one contains the other. Every arriving chore has unit cost to every eligible agent and arrives with a nonempty eligible set \(S_j\in\mathcal F\). It must be allocated immediately to exactly one eligible agent, with no moves of previous chores. An adversary may choose eligibility sets adaptively, and neither the sequence length nor its future members are known to the algorithm. The eligibility-aware proportional benchmark for each individual is \(Q_t(\{i\})\). The theorem assumes **identical unit costs**; it does not assert the Prop1 result for arbitrary unequal sizes, crossing eligibility sets, or unknown changes to the family.

Augment \(\mathcal F\) by \(N\) and all singleton sets. This changes neither which arriving chores are eligible nor laminarity, and the resulting sets form a rooted inclusion tree whose children partition their parent. The group guarantee applies to this augmented family.

## Proof
For every group \(T\) of the augmented laminar family, maintain its **excess**
\[
e_t(T)=L_t(T)-\sum_{j\leq t}\frac{|T\cap S_j|}{|S_j|}.
\]
Initially each excess is \(0<1\). Suppose inductively that \(e_{t-1}(T)<1\) for all groups, and the next eligibility set is \(S\). We select a singleton leaf of \(S\) along an inclusion-tree path. The original eligibility set \(S\), rather than a changing current subtree, determines all the thresholds.

At the root \(S\), \(e_{t-1}(S)<1=|S|/|S|\). At a current subtree \(U\subseteq S\) satisfying
\[
e_{t-1}(U)<\frac{|U|}{|S|},
\]
consider its children \(C_1,\ldots,C_r\) (if it is not a leaf). Since the children partition \(U\), finite additivity of \(e_{t-1}\) gives
\[
\sum_{a=1}^{r}e_{t-1}(C_a)=e_{t-1}(U)<\frac{|U|}{|S|}=\sum_{a=1}^{r}\frac{|C_a|}{|S|}.
\]
Thus at least one child satisfies \(e_{t-1}(C_a)<|C_a|/|S|\). Choose the first such child in a fixed deterministic ordering and continue until reaching an eligible singleton \(\{i\}\). Assign the chore to agent \(i\).

For each strict descendant \(T\subsetneq S\) on the selected path, the new excess equals
\[
e_t(T)=e_{t-1}(T)+1-\frac{|T|}{|S|}<1.
\]
For each other strict descendant \(T\subsetneq S\), the chore is not allocated into \(T\), so \(e_t(T)=e_{t-1}(T)-|T|/|S|<1\). For \(T\supseteq S\), the entire chore and its entire proportional share both lie in \(T\), so its excess is unchanged. Every set outside these cases is disjoint from \(S\), so its excess is also unchanged. These are all possibilities by laminarity. Hence the invariant holds at the next prefix. Induction proves all the simultaneous group inequalities for every finite prefix; the algorithm uses only revealed history.

For \(T=\{i\}\), if \(i\)'s bundle is nonempty, dropping any one unit chore lowers its cost from \(L_t(\{i\})\) by \(1\), so \(L_t(\{i\})-1<Q_t(\{i\})\). Empty bundles are already below the nonnegative proportional benchmark. Thus Prop1 holds at every prefix. Finally, with one chore eligible for all \(n\) agents, whichever agent receives it has excess \(1-1/n\). These examples rule out a bound \(e_t(\{i\})\le c\) for any fixed \(c<1\) valid uniformly in \(n\).

## Verification
`verify_laminar.py` is a standalone Python 3 program using exact rational arithmetic. It rebuilds inclusion trees and checks both each group upper quota and each individual's Prop1 property after each assignment. Its tests comprise exhaustive short eligibility sequences for four representative laminar hierarchies and seeded diverse hierarchies with long trajectories. In the actual packaged replay it reported `VERIFY_OK histories=50983 group_inequalities=2198655`. This finite checking exercises implementation and boundaries, **not** the proof of the all-size theorem; the induction above supplies that proof. Run `python3 verify_laminar.py` from the extracted package directory.

## Relationship to prior work
Biburger, Megow, and Shahkarami (2026) introduced the eligibility-aware proportional share and proved an \(\Theta(\sqrt m)\) deterministic online approximation barrier for unit-size chores with **unrestricted** eligibility sets, alongside offline Prop1 existence; the online laminar-class result here is a structural restriction rather than a contradiction. The reviewed synopsis does not mention a laminar upper-quota theorem; the complete motivating preprint could not be inspected, so possible coverage in its detailed treatment remains an originality risk. Earlier scheduling literature treats nested processing-set restrictions, particularly makespan optimization, but the excerpted results do not establish the **simultaneous, prefixwise, group-proportional quota** asserted here. General offline rounding and hierarchical service scheduling alone do not directly give an irrevocable guarantee for every time prefix under eligibility-aware shares.

## Limitations
The fixed eligible-set family must be known before allocations begin; the theorem does not handle an adversary introducing previously unknown crossing or newly nested eligibility sets after assignments. Chores are unit-cost and identical. The theorem gives one-sided group excess, not two-sided group discrepancy, envy-freeness, or an unrestricted-eligibility bound. The result has not undergone independent scientific review. Full primary text of the closely related 2026 eligibility-constraints preprint was not available for comparison; the originality assessment is necessarily provisional.

## References
1. J. Biburger, N. Megow, G. Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064, first submitted 2026-10-06. https://arxiv.org/abs/2610.08064
2. K. Lim and coauthors, *Improved Bounds for Online Scheduling with Eligibility Constraints* (2011), nested and interval machine-eligibility scheduling. https://core.ac.uk/download/pdf/82731667.pdf
3. J. Y.-T. Leung and C.-L. Li, *Scheduling with Processing Set Restrictions: A Survey*, discussion of nested restriction and unit-job makespan, https://ira.lib.polyu.edu.hk/bitstream/10397/1849/1/60%20Final-Version.pdf

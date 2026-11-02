# Exact action profiles for partition-valued two-agent effectivity

## Finding
Fix two agents and a nonempty finite outcome set \(U\). Suppose their local actual-effectivity families are partitions \(\mathcal P=\{P_1,\ldots,P_r\}\) and \(\mathcal Q=\{Q_1,\ldots,Q_s\}\) of \(U\), with every intersection \(C_{ij}=P_i\cap Q_j\) nonempty. Write \(q_{ij}=|C_{ij}|\). For a deterministic concurrent-game realization at the chosen state, let \(d_i\) denote the number of first-agent actions with output set \(P_i\), and let \(e_j\) denote the number of second-agent actions with output set \(Q_j\).

**Complete action-count classification.** For positive integers \(d_i,e_j\), such a realization exists with exactly these action counts if and only if
\[
\boxed{d_i\ge q_{ij}\quad\text{and}\quad e_j\ge q_{ij}\qquad\text{for every }i,j.}
\]
Consequently the entire feasible action-count region has a unique componentwise minimum
\[
\boxed{d_i^{\min}=\max_j q_{ij},\qquad e_j^{\min}=\max_i q_{ij}.}
\]
The simultaneous minimum total number of actions is
\[
\boxed{\sum_i\max_j q_{ij}+\sum_j\max_i q_{ij}.}
\]

**Exact structural census.** When individual copies of each action type and outcomes are labelled, the number of realizing deterministic outcome functions for any feasible action-count vector is
\[
\boxed{\prod_{i=1}^{r}\prod_{j=1}^{s}T(q_{ij},d_i,e_j),}
\]
where \(T(q,a,b)\) is the number of \(a\)-by-\(b\) arrays on a fixed \(q\)-symbol alphabet in which every row and every column contains all \(q\) symbols. An explicit finite inclusion-exclusion expression for \(T\) appears below. If \(q_{ij}=d_i=e_j\), that block is exactly a Latin square; in the uniform case \(q_{ij}=q\) for all \(i,j\), the optimal realizations are precisely independently chosen Latin squares in each of the \(rs\) blocks, giving \(L(q)^{rs}\) labelled outcome tables, where \(L(q)\) is the number of labelled Latin squares of order \(q\).

## Assumptions and scope
An action profile is a pair of actions, one of each agent, and has a single outcome. The output set of one action is the set of its possible outcomes as the other agent varies their action. Multiple distinguishable actions are permitted to have identical output sets. We specify one local state, with outcomes restricted to \(U\); unrelated local states can be realized independently. The two given effectivity families are genuine partitions of the same \(U\), meaning nonempty blocks, pairwise disjoint within a family, and union \(U\). All cross intersections are nonempty, ensuring the independence condition required for a deterministic concurrent-game representation. The theorem makes no claim for overlapping (nonpartition) neighborhood families or for coalition effectivities.

## Proof
Let \(A_i\) be the set of first-agent actions whose output set is \(P_i\), and \(B_j\) the set of second-agent actions whose output set is \(Q_j\), so \(|A_i|=d_i\) and \(|B_j|=e_j\). The outcome of a profile \((a,b)\in A_i\times B_j\) belongs to \(P_i\) (because \(a\) has output set \(P_i\)) and to \(Q_j\) (because \(b\) has output set \(Q_j\)). It therefore belongs to \(C_{ij}\).

Fix \(a\in A_i\) and a column type \(j\). Every element of \(C_{ij}\) must occur as the outcome of \((a,b)\) for some \(b\in B_j\): it must occur somewhere in the output set \(P_i\) of \(a\), and an occurrence in \(C_{ij}\subseteq Q_j\) cannot come from an action of a different column type because the \(Q_j\) partition \(U\). There are only \(e_j\) such profiles, so \(e_j\ge |C_{ij}|=q_{ij}\). The symmetric argument fixing \(b\in B_j\) gives \(d_i\ge q_{ij}\). This establishes necessity for every \(i,j\).

Conversely suppose all these inequalities hold. Label the copies of type \(P_i\) by \(a\in\{0,\ldots,d_i-1\}\) and those of \(Q_j\) by \(b\in\{0,\ldots,e_j-1\}\). Choose a bijection \(h_{ij}:\{0,\ldots,q_{ij}-1\}\to C_{ij}\) for each pair. Define the deterministic outcome by
\[
\operatorname{out}((i,a),(j,b))=h_{ij}((a+b)\bmod q_{ij}).
\]
For fixed \((i,a)\) and \(j\), the \(e_j\ge q_{ij}\) column indices give every element of \(C_{ij}\). Hence the output set of \((i,a)\), varying all second-agent actions, is exactly \(\bigcup_j C_{ij}=P_i\). Symmetrically, every \((j,b)\) has output set \(Q_j\) since \(d_i\ge q_{ij}\) for every \(i\). Thus every feasible vector has a realization. The simultaneous componentwise minimum follows because all constraints are independent coordinatewise lower bounds and the construction attains all of them together.

For fixed action counts, the rectangle \(A_i\times B_j\) must be colored by elements of \(C_{ij}\), and every row and column of this rectangle must encounter every color of \(C_{ij}\). Conversely, those local conditions guarantee all required action output sets, because the \(C_{ij}\) partition each \(P_i\) by \(j\) and each \(Q_j\) by \(i\). The rectangles form a disjoint partition of all action profiles, so their choices are independent, proving the product enumeration.

For completeness, write \([a]=\{1,\ldots,a\}\), and for each color \(t\in[q]\) choose sets \(R_t\subseteq[a]\) and \(D_t\subseteq[b]\), interpreted as selected events that row \(u\) or column \(v\) omits \(t\). Inclusion-exclusion gives
\[
T(q,a,b)=\sum_{\substack{R_t\subseteq[a],\ D_t\subseteq[b]\\t\in[q]}}
(-1)^{\sum_t(|R_t|+|D_t|)}
\prod_{u=1}^{a}\prod_{v=1}^{b}
\left(q-\left|\{t\in[q]:u\in R_t\ \text{or}\ v\in D_t\}\right|\right).
\]
Indeed, after choosing which omission events to impose, each cell \((u,v)\) may use any color not forbidden by its selected row or column events. At \(a=b=q\), every row and column contains each color exactly once, so \(T(q,q,q)=L(q)\). This proves the Latin-square consequence.

## Verification
The bundled standard-library `checker.py` constructs the cyclic outcomes and checks both agents' exact output sets for all \(21{,}297\) positive \(1\)- to \(3\)-by-\(1\)- to \(3\)-cell intersection-size matrices with entries in \(\{1,2,3\}\). Independently, exhaustive array enumeration is compared to the inclusion-exclusion formula for six small \((q,a,b)\) combinations, including \(T(2,2,2)=2\), \(T(2,3,3)=102\), and \(T(3,3,3)=12\). The heterogeneous matrix \(\begin{pmatrix}2&1\\1&3\end{pmatrix}\) gives minimum action multiplicities \((2,3)\) for both agents and exactly \(2\cdot12=24\) labelled minimum-size outcome functions. The checker prints `ALL_CHECKS_OK`. Finite tests are corroboration; the proof establishes all finite instances.

## Relationship to prior work
Ciardelli's representation theorem (arXiv:2606.31866, Theorem 2.2) characterizes representable individual-agent actual-effectivity neighborhoods by nonemptiness, common union and nonempty intersections across simultaneous choices. Its construction uses a separate outcome label for each neighborhood action. A later universal finite action-multiplicity bound, *Sharp root-size action realization for finite actual-effectivity frames* (2026), reduces this to a uniform root-size copy factor and proves its worst-case sharpness. In the two-agent case its factor is the full number of outcomes, and it expressly leaves instance-by-instance minimization unresolved. The theorem here determines the **entire feasible multiplicity vector and exact outcome-table count** for two-agent *partition-valued* instances. The one-block, homogeneous full-range case of the bound is already covered and is not presented as new. The Latin-square equivalence for individual square arrays is classical; the result is the exact resource-and-count classification for heterogeneous effectivity partitions, not a new statement about Latin-square existence.

Goranko and Jamroga's 2015/2016 representation theorems concern primarily monotone effectivity for coalitions and temporal paths, rather than the exact one-step, individual-action output-set multiplicities considered here.

## Limitations
The partition hypothesis is essential to the row/column lower bounds: if neighborhoods overlap within one family, the same outcome can be produced via several different block types and the formula need not apply. The theorem concerns deterministic actions, fixed local outcome sets and labelled copies; it does not classify isomorphism classes of games or optimal costs for arbitrary overlapping neighborhoods. The existence of Latin squares and surjective rectangular arrays is classical. An equivalent optimization under different game-form terminology is a residual historical-priority risk. No independent audit has been performed.

## References
1. Ivano Ciardelli, *Inquisitive Action Logic*, arXiv:2606.31866v1, first publicly posted 2026-06-30, especially Section 2 and Theorem 2.2. https://arxiv.org/html/2606.31866.
2. *Sharp root-size action realization for finite actual-effectivity frames*, publicly available mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-root-size-action-realization-for-finite-actual-effectivity--114a0e0912e6.
3. Valentin Goranko and Wojciech Jamroga, *State and path coalition effectivity models of concurrent multi-player games*, Autonomous Agents and Multi-Agent Systems 30 (2016), 446–485, open access, DOI 10.1007/s10458-015-9294-4.
4. Standard Latin-square definition and bipartite edge-coloring viewpoint, https://en.wikipedia.org/wiki/Latin_square.

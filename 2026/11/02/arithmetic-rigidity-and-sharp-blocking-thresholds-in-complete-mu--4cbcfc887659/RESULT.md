# Arithmetic rigidity and sharp blocking thresholds in complete-multipartite friend-appreciation games

## Finding

For any integer \(t\ge 2\), let \(V_1,\ldots,V_t\) be disjoint nonempty types of labeled individuals, of sizes \(n_1,\ldots,n_t\). Every two agents in different types regard each other as friends. Every two agents in the same type are either enemies (the FE variant) or neutrals (the FEN variant). All agents use *friend-appreciation* preferences: first maximize the number of friends in their own coalition; among equal friend counts, minimize the number of enemies. The two variants have **exactly the same Nash-stable partitions**.

A partition is Nash stable if no agent strictly gains by entering another existing coalition or becoming a singleton, without an acceptance restriction. Put \(g=\gcd(n_1,\ldots,n_t)\). Then the complete characterization is
\[
 \Pi\text{ Nash stable}\quad\Longleftrightarrow\quad
 \exists r\mid g:\ |\Pi|=r,\quad |C\cap V_i|=\frac{n_i}{r}\quad
 (\forall C\in\Pi,\ \forall i=1,\ldots,t).
\]
The number of such partitions, with labeled individuals and unordered coalitions, is
\[
 E(n_1,\ldots,n_t)=\sum_{r\mid g}
 \frac{\prod_{i=1}^{t}n_i!}{r!\,\prod_{i=1}^{t}[(n_i/r)!]^r}.
\]
For example, \(E(2,2,2)=5\) and \(E(3,3,3)=37\). In particular, if \(g=1\), the grand coalition is the **unique** Nash-stable outcome.

For any nongrand Nash-stable partition, let \(r\ge 2\) be its number of coalitions, \(x_i=n_i/r\), and \(s=\sum_i x_i\). A *core blocker* is a nonempty set of individuals whose members all strictly prefer forming that set to their current coalitions. A *strict-core blocker* has every member weakly prefer it, and at least one member strictly prefer it. The respective minimum blocker cardinalities are exactly
\[
 \begin{array}{c|cc}
 &\text{core blocker}&\text{strict-core blocker}\\\hline
 \text{FE (within-type enemies)}&s+2&s+2\\
 \text{FEN (within-type neutrals)}&s+2&s+1
 \end{array}.
\]
The grand-coalition partition has neither kind of blocker, and is the unique strictly-core-stable Nash-stable partition. Thus replacing same-type enemies by neutrals does not change unilateral Nash stability, but makes some collective deviations feasible with exactly one fewer participant.

## Assumptions and scope

All type sizes are positive integers and \(t\ge 2\). The underlying friendship graph is the complete multipartite graph with vertex classes \(V_i\). Every pair of distinct agents is related symmetrically: friend across classes and either enemy within classes (FE) or neutral within classes (FEN). Coalition scores for agent \(v\in V_i\) in coalition \(S\ni v\) are the lexicographically compared pairs
\[
 \left(F_i(S),-H_i(S)\right),\qquad
 F_i(S)=|S|-|S\cap V_i|,
 \quad H_i(S)=\begin{cases}|S\cap V_i|-1,&\mathrm{FE},\\0,&\mathrm{FEN}.\end{cases}
\]
No costs, acceptance consent, connectedness restrictions, or other coalition limits apply. A blocking coalition can have any nonempty size, including the entire population. These definitions distinguish core blocking (every member strictly benefits) from strict-core blocking (all members weakly benefit and at least one strictly benefits).

## Proof

**1. A largest coalition contains every type.** Let \(C_0\) be a largest coalition of an arbitrary Nash-stable partition, with \(M=|C_0|\). Suppose some type \(V_i\) is absent from \(C_0\). An \(i\)-agent belongs to a coalition of size at most \(M\), so has at most \(M-1\) friends there. On joining \(C_0\) the agent would have exactly \(M\) friends and would strictly gain, contradicting Nash stability. Thus \(C_0\) meets every type.

**2. All coalitions have identical compositions.** Let another coalition \(C\) have size \(u\le M\), and let \(I\) be its set of represented types, with \(p=|I|\ge1\). Write \(m_i=|C_0\cap V_i|>0\) and \(c_i=|C\cap V_i|\). For each \(i\in I\), an \(i\)-agent can move from \(C\) to \(C_0\), and another \(i\)-agent can move in the reverse direction. Absence of strict gain in either direction requires equality of the respective *friend counts*, independent of the tie-breaker:
\[
 M-m_i=u-c_i,\qquad\text{hence}\qquad m_i-c_i=M-u=:\Delta\ge0.
\]
(If one of these friend counts were larger, the agent in the other coalition would strictly gain.) Summing over the types gives, with \(H=\sum_{j\notin I}m_j\ge0\),
\[
 M=\sum_{i\in I}(c_i+\Delta)+H=u+p\Delta+H,
 \qquad \text{so }(1-p)\Delta=H.
\]
If any type were omitted from \(C\), then \(H>0\) since all types occur in \(C_0\), contradicting the last equality. Hence \(I=\{1,\ldots,t\}\), \(p=t\ge2\), and \(H=0\). The same equality forces \(\Delta=0\), and then \(m_i=c_i\) for every type. Therefore every coalition has identical positive type counts. With \(r\) coalitions, they must be \(n_i/r\), proving the necessary divisibility.

Conversely, suppose there are \(r\mid g\) coalitions each containing \(x_i=n_i/r\) of type \(i\). Every agent has \(s-x_i\ge1\) friends because \(t\ge2\). Entering another coalition preserves this count of friends; the FE mover acquires one more same-type enemy, and the FEN mover is indifferent. Becoming singleton loses all friends. Thus no move strictly improves utility and the partition is Nash stable.

**3. Exact count.** For a fixed allowed \(r\), temporarily order the \(r\) coalitions. For type \(i\), the multinomial number of assignments with \(x_i\) people in each coalition is \(n_i!/(x_i!)^r\). Multiplying across types and dividing by \(r!\) (every coalition is nonempty and therefore distinct) gives the fixed-\(r\) term in \(E\). Different \(r\) give disjoint families.

**4. Core and strict-core blocker minima.** Consider an \(r\ge2\) Nash-stable partition. Each old coalition has type counts \(x_i\) and size \(s\). Let a purported weakly blocking set \(S\) have size \(U\), represented type set \(I\) of size \(p\), and type occupancies \(u_i\ge1\) for \(i\in I\). Its members of type \(i\) had \(s-x_i\) friends and would have \(U-u_i\) friends. They can weakly benefit only if
\[
 U-u_i\ge s-x_i \quad(i\in I).
\]
A single-type coalition cannot weakly block because its agents would have no friends, against \(s-x_i>0\). So \(p\ge2\). Summing the inequalities and using \(\sum_{i\in I}u_i=U\),
\[
 (p-1)U\ge p s-\sum_{i\in I}x_i
 =(p-1)s+\sum_{j\notin I}x_j.
\]
Consequently \(U\ge s\). If \(U=s\), the positive type counts force \(I\) to contain **all** types, and summation equality forces \(u_i=x_i\) for every type. Everyone would then be indifferent in both variants. Hence no strict-core blocker has \(U\le s\).

At \(U=s+1\), a **core blocker** would need \(U-u_i>s-x_i\), hence integer \(u_i\le x_i\) for all represented types. Then \(U=\sum_{i\in I}u_i\le\sum_{i\in I}x_i\le s\), impossible. Thus no all-strict blocker has fewer than \(s+2\) members.

For FE, even a *weak* blocker of size \(s+1\) requires \(u_i\le x_i\) for each represented type. Indeed if \(u_i\ge x_i+2\), friends decrease, while if \(u_i=x_i+1\), the friend count is equal but the number of enemies increases by one, a strict loss. Thus a weak FE blocker of size \(s+1\) is impossible.

For FEN, take \(x_i\) agents of every type and **one additional agent of any chosen type**. This is feasible because \(r\ge2\) implies \(n_i=r x_i\ge x_i+1\). The enlarged type's agents have their old friend count and are indifferent, while agents from every other type gain one friend. Thus there is a strict-core blocker of size \(s+1\) for FEN.

Finally, choose two distinct types and take \(x_i+1\) agents from each, and \(x_j\) agents from all other types. This is feasible for \(r\ge2\), has size \(s+2\), and gives **every** member at least one additional friend. It is an all-strict blocker in both FE and FEN, proving the remaining sharp upper bounds.

**5. Grand-coalition protection.** In the grand coalition, each type-\(i\) agent has all \(n-n_i\) agents outside that type as friends, where \(n=\sum_i n_i\). In any proper nonempty subset \(S\), if it contains members of at least two types, some member loses a friend: take an omitted agent of type \(j\) and a selected agent of a different type. If \(S\) has just one type, its members lose every friend. Thus no proper subset weakly blocks, and the full coalition only gives indifference. The grand-coalition partition is strictly core stable. Together with step 4, it is uniquely so among Nash stable partitions.

## Verification

The self-contained program `verify_multipartite.py` enumerates all set partitions of labeled type profiles with \(2\le t\le4\), all type sizes in \(\{1,2,3\}\), and total size at most \(9\), under **both** FE and FEN rules. It independently computes Nash eligibility by checking all unilateral deviations and compares with the divisibility/composition criterion and the exact equilibrium count. For profiles with total size at most \(7\) it also enumerates all potential core and strict-core blockers and compares their minimum sizes to the theorem. Its output is `PASS 102 type-size profiles; 948546 set partitions; 316 Nash instances; 300 blocking minima`. These finite checks do **not** establish the universal claim; steps 1–5 provide the all-size proof.

## Relationship to prior work

Chen, Csáji, Roy and Simola's 2022 preprint, updated in 2023, formalizes the friend–enemy–neutral model and proves that symmetric friendship admits a Nash-stable partition (Observation 2). Its proof constructs an existence witness using isolated friendship vertices; it does not give this complete multipartite all-equilibrium count or the sharp deviation sizes. Dimitrov and Sung give older general existence results for mutual friend preferences; Ota and collaborators develop the friends/enemies/neutrals model and core stability. Their general framework supplies the definitions and prior grand-coalition protection (the strong connectedness of complete multipartite friendship graphs implies that property in earlier work). The present contribution is the exact characterization and count of *all* Nash outcomes and the two distinct blocking-radius laws. Related complete-bipartite signed-additive and fractional games address different preference representations or special parameter layers and do not yield the arbitrary-multipartite statement.

## Limitations

All types must be nonempty, friendship must be symmetric and complete between distinct types, and agents must have identical lexicographic priorities over friend counts and same-type enemies. The result is not a characterization for arbitrary friendship graphs, directed preferences, costs, coalition-size restrictions, or consensual entry. The finite verifier covers only small labeled instances; novelty cannot be guaranteed against all unindexed or inaccessible literature. General strong-core protection of the grand coalition and the existence of a Nash outcome are prior knowledge, not independent new claims here. No independent external audit is claimed.

## References

- Jiehua Chen, Gergely Csáji, Sanjukta Roy, and Sofia Simola, *Hedonic Games With Friends, Enemies, and Neutrals: Resolving Open Questions and Fine-Grained Complexity*, first posted 2022-03-17, https://arxiv.org/abs/2203.09655 (especially Observation 2 and its proof in Appendix B.3 of v2).
- Hirotaka Ota and collaborators, *Core Stability in Hedonic Games among Friends and Enemies: Impact of Neutrals*, IJCAI 2017, https://www.ijcai.org/proceedings/2017/0051.pdf.
- Dinko Dimitrov and Shao Chin Sung, *Enemies and Friends in Hedonic Games: Individual Deviations, Stability and Manipulation*, working paper 2004, https://doi.org/10.2139/ssrn.639483.

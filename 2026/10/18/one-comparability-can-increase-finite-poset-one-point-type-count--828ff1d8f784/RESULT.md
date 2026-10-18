# One comparability can increase finite-poset one-point type counts exponentially

## Finding

**Theorem.** Let \(a,b\ge 1\), and let \(Q_{a,b}\) be the strict height-two partial order on disjoint antichains \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\), with every point of \(A\) below every point of \(B\). Let \(P_{a,b}\) be obtained by deleting just \(a_1<b_1\) from \(Q_{a,b}\). Write \(c(P)\) for the number of distinct one-point extensions of a finite poset \(P\) over its *fixed* underlying set, with the new point named but the old elements fixed. Then
\[
 c(Q_{a,b})=2^{a+b}+2^a+2^b-2,
 \qquad c(P_{a,b})=3\cdot 2^{a+b-2}+2^a+2^b,
\]
so
\[
 \boxed{c(Q_{a,b})-c(P_{a,b})=2^{a+b-2}-2.}
\]
Thus adding one comparability can **increase**, rather than decrease, the number of one-point extensions, by an unbounded amount. The least size of a finite poset admitting any comparability addition that strictly increases this count is **four**. On four labeled points there are \(219\) strict partial orders, and the increases occur in precisely \(120\) directed order-addition instances, belonging to six isomorphism classes of ordered pairs \((P,Q)\).

For the countable universal homogeneous (random) partial order \(\mathbb D\), \(c(P)\) is equivalently the number of nonalgebraic complete one-types over a fixed finite parameter set inducing \(P\). The theorem therefore also describes a nonmonotonicity of finite-parameter orbit counts of \(\operatorname{Aut}(\mathbb D)\).

## Assumptions and scope

All partial orders here are finite, nonempty, antisymmetric, and transitive; all written relations \(<\) are strict. A *one-point extension over* \(P\) is a partial order on \(P\cup\{x\}\) inducing exactly the original order on \(P\), with \(x\notin P\). Two such extensions are different if they impose different relations between \(x\) and a fixed old element. Equivalently they are considered up to isomorphisms fixing each point of \(P\) and fixing \(x\). In contrast, this is not a count of unpointed isomorphism types of the enlarged poset.

For an extension by \(x\), define \(L=\{p\in P:p<x\}\) and \(U=\{p\in P:x<p\}\). These are disjoint, \(L\) is a down-set, \(U\) is an up-set, and every element of \(L\) lies below every element of \(U\). Conversely, these conditions uniquely define a one-point extension. Thus \(c(P)\) counts the admissible ordered ideal/filter pairs. The count of *all* complete one-types over a finite parameter set of size \(n\) is \(n+c(P)\): the extra \(n\) types are algebraic equality types. Accordingly the difference in the theorem is unchanged whether one counts all or only nonalgebraic one-types.

A comparison of posets \(P\subseteq Q\) on the same vertex set means inclusion of strict order relations. For the general four-point minimality statement, one chooses incomparable \(u,v\in P\), adds \(u<v\), and takes transitive closure, rejecting choices creating a cycle. The family in the theorem requires no additional transitive edges.

## Proof

**1. The complete two-level order.** An extension of \(Q= A\oplus B\) has three disjoint kinds. If \(x<a_i\) for at least one \(a_i\in A\), then \(x<b_j\) for every \(b_j\in B\), and the statuses of the points of \(A\) are independently *above* or *incomparable* to \(x\), with at least one above. There are \(2^a-1\) possibilities. Dually, if \(b_j<x\) for at least one \(b_j\in B\), then every point of \(A\) is below \(x\), and there are \(2^b-1\) possibilities. In all remaining extensions, no point of \(A\) lies above \(x\) and no point of \(B\) lies below \(x\); each point of \(A\) can independently be below or incomparable to \(x\), and each point of \(B\) above or incomparable. There are \(2^{a+b}\) possibilities. Summing gives the displayed expression for \(c(Q)\).

**2. Comparison with one deleted relation.** Put \(u=a_1\) and \(v=b_1\). Their only missing relation in \(P\) is \(u<v\), and \(u\) and \(v\) are incomparable in \(P\). Partition all possible assignments of the three statuses relative to \(x\) according to whether they are legal over \(P\) or over \(Q\).

Exactly \(2^{a+b-2}\) assignments are legal over \(Q\) but not \(P\): they have \(u<x<v\). Indeed, every remaining point of \(A\) can be independently below or incomparable to \(x\), and every remaining point of \(B\) independently above or incomparable; these assignments respect all old relations in \(Q\). But \(u<x<v\) would require the missing \(u<v\) in \(P\).

Conversely, exactly **two** assignments are legal over \(P\) but not \(Q\). They are (i) \(x<u\), \(x\parallel v\), with every other point of \(A\) incomparable to \(x\) and every other point of \(B\) above \(x\); and (ii) \(u\parallel x\), \(v<x\), with every other point of \(A\) below \(x\) and every other point of \(B\) incomparable to \(x\). Here \(\parallel\) denotes incomparability. To see completeness, adding \(u<v\) can invalidate an old extension only when \(x<u\) without \(x<v\), or when \(v<x\) without \(u<x\). The case \(v<x<u\) is impossible already over \(P\). In the first remaining case, the existing relations \(u<B\setminus\{v\}\) force every other maximal point above \(x\), while relations \(A\setminus\{u\}<v\) and the incomparabilities within \(A\) force every other minimal point incomparable to \(x\). The second case is dual. Hence
\[
 c(Q)-c(P)=\underbrace{2^{a+b-2}}_{\text{new assignments}}-\underbrace{2}_{\text{lost assignments}}.
\]
Combining with Step 1 proves both formulas for every pair of positive integers \(a,b\). For \(a=b=2\), this yields \(c(P)=20\) and \(c(Q)=22\); for fixed positive \(a\), the gain grows exponentially in \(b\).

**3. Sharpness and full first layer.** With at most three old points, exhaust all strict partial orders and all permissible additions of one comparability, including closure. The complete generator takes every unordered vertex pair, chooses one of no relation, forward relation, or backward relation, closes transitively, and rejects cycles; duplicates are removed by exact edge-set identity. This yields exactly \(1,3,19\) labeled posets on \(1,2,3\) vertices. Evaluating all three-status assignments and checking transitivity of the extended relation gives no strictly positive count change. On four vertices the generator gives \(219\) labeled posets. Among its \(1044\) valid directed single-comparability additions, \(120\) yield an increase; canonicalizing both old and new relations under the same permutation of four vertices produces exactly six classes: two with changes \(22\to24\), one \(20\to22\), one \(19\to20\), and two \(18\to19\). Their labeled multiplicities are respectively \(12,12,24,24,24,24\). The fully specified enumerator, transitivity checker, and canonical representatives are in `verify.py`. It checks all \(3^n\) possible statuses for each generated poset and thereby supplies an exhaustive finite certificate for the sharp minimum and first-layer census.

## Verification

Run `python3 verify.py` with a Python 3 standard-library installation. Its one-point-extension counter constructs the expanded relation on \(n+1\) vertices from each ternary assignment, independently takes transitive closure, and accepts exactly the assignments whose relations are already transitively closed and irreflexive. It generates the base posets by three-way decisions on every unordered pair, and uses complete vertex permutations to canonicalize the ordered pairs of relations. The verifier checks the sharpness statements for \(n\le4\), all six first-failure isomorphism classes, and the two infinite-family formulas for all \(1\le a,b\le4\), completing with `PASS: all independently generated finite checks`. The finite calculations confirm the formulas but do not replace the all-parameter proof in Steps 1–2.

## Relationship to prior work

The order-ideal/upper-filter description of one-point extensions is classical. Dolinka and Mašulović, Lemma 4.3, explicitly use the sets of points below and above an inserted point, and Pretzel's 1980 paper studies the poset of possible insertion positions, including a complete two-level order. A published mathematical record proves that counting complete finite-parameter one-types of the random poset is \(\#P\)-complete and gives the same ideal/filter characterization and some exact chain and antichain counts. Those foundational results and the one-point-extension characterization are **not** asserted to be new.

The present claim concerns a different, relationally comparative question: what happens to **the count** when one modifies the parameters by introducing an additional comparability? The exact jump \(2^{a+b-2}-2\), the least counterexample size, and the full first failure layer do not follow from the cited general one-point-extension characterization or the hardness theorem, and were not located in the inspected material. The sources do not justify a claim of global priority; see limitations.

## Limitations

The displayed formulas concern the specific near-complete height-two family, not all single-relation additions. The full classification covers only the **first** order admitting an increase. The precise first publication of an identical observation cannot be ruled out. Pretzel's relevant 1980 full text was not accessible during the comparison; its abstract concerns insertion-poset **dimension**, but its uninspected content poses a specific residual originality risk. Source searches and accessible primary readings do not establish uniqueness of the result in the literature. The scientific statement is proved and computationally checked here, but it has not received independent review.

## References

1. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892v1 (first publicly posted 15 September 2010), subsequently *Proceedings of the Edinburgh Mathematical Society* 55 (2012), 635–656, DOI: 10.1017/S0013091510001161. Lemma 4.3 gives the insertion ideal/filter description. https://arxiv.org/abs/1009.2892.
2. O. Pretzel, *A construction for partially ordered sets*, *Discrete Mathematics* 32 (1980), 59–68, DOI: 10.1016/0012-365X(80)90100-4. The abstract addresses the dimension of insertion-position posets; full text not inspected. https://doi.org/10.1016/0012-365X(80)90100-4.
3. *Finite-parameter 1-type counting in the random poset is #P-complete*, published mathematical record `3b955f4020e1` (2026). The accessible full text establishes the generic-poset ideal/filter correspondence, \(\#P\)-completeness, and exact chain and antichain counts; the present jump formula is not stated there. The publicly indexed record has opaque identifier `3b955f4020e1`.

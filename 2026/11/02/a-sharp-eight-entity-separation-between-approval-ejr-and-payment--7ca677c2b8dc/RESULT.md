# A sharp eight-entity separation between approval EJR+ and payment-strong EJR+

## Finding

For a size-\(k\) approval-based committee elected from \(m\) distinct candidates by \(n\) voters, assume each elected candidate has at least one approving voter, and the committee is full (it contains exactly \(k\) candidates). If the committee satisfies the usual EJR+ axiom but violates payment-based **strong EJR+ up-to-one**, then
\[
n+m\ge 8.
\]
The bound is attained with \((n,m,k)=(3,5,4)\) and \((4,4,3)\). At total size eight there are **exactly five** such approval configurations up to renaming voters and permuting elected candidates: four in the former regime and one in the latter. Exactly **two** of the five configurations have a Pareto-efficient committee. These assertions allow distinct candidates to have identical approver sets, but do not allow unapproved elected candidates.

For three voters, four winners \(a,b,c,d\) and one unelected candidate \(x\), one Pareto-efficient witness is
\[
A_a=A_b=\{1\},\qquad A_c=A_x=\{2,3\},\qquad A_d=\{1,2,3\}.
\]
For four voters, three winners \(a,b,c\) and an unelected \(x\), the second Pareto-efficient witness is
\[
A_a=\{1\},\qquad A_b=\{2\},\qquad A_c=\{1,2,3,4\},\qquad A_x=\{3,4\}.
\]
In the first witness the strong-payment score for the full-voter coalition is exactly \(4/3\) for each voter, equal to the entitlement \(k/n\). In the second it is exactly \(3/4\) for each voter. Since the strong axiom requires a **strict** greater-than inequality, both are violations.

## Assumptions and scope

There are \(n\ge1\) voters, \(m\ge k\ge1\) distinguishable unit-cost candidates, and budget \(b=k\). Every voter assigns each candidate utility zero or one. Let \(W\) contain exactly \(k\) elected candidates, and for each candidate \(d\) denote its approver set by \(A_d\subseteq\{1,\ldots,n\}\). All elected candidates have \(A_d\ne\varnothing\). When \(m=k\), both criteria hold vacuously. The minimum-separation and census statements consider outcomes with at least one unelected candidate; at total size eight, the only potentially separating cases have exactly one unelected candidate.

For a voter \(i\), write \(u_i=|\{d\in W:i\in A_d\}|\). Standard approval EJR+ is equivalent [1, Theorem 1; 2, Section 3.2] to the following **weak EJR+ up-to-one** test: for every unelected \(x\) and every nonempty coalition \(T\subseteq A_x\), at least one \(i\in T\) satisfies
\[
n(u_i+1)>k|T|. \tag{1}
\]
The payment-strong EJR+ up-to-one test [1, Definition 4, Eq. (6)] requires, for every unelected \(x\) and every coalition \(S\) with \(t=|S\cap A_x|>0\), at least one \(i\in S\) satisfying
\[
F_i(S,x)=\frac{\boldsymbol{1}_{i\in A_x}}{t}
 +\sum_{d\in W}\frac{\boldsymbol{1}_{i\in A_d}}{\max\{t,|S\cap A_d|\}} >\frac{k}{n}. \tag{2}
\]
This is the source's payment expression specialized to unit costs and binary utilities. In (2), non-approvers of \(x\) may belong to \(S\); that freedom is essential. A candidate with no supporting voter in \(S\) contributes zero to all coalition members, so its denominator is immaterial.

The term **Pareto-efficient** means no other committee of size at most \(k\) weakly increases every voter's utility while strictly increasing at least one. At the sharp boundary, every elected candidate and the omitted candidate is supported by someone, so allowing smaller committees cannot create a Pareto improvement that adding available winners does not cover.

## Proof

**Lower bound independent of electorate size for one or two seats.** Fix a nonempty \(T=S\cap A_x\) of size \(t\) and a voter \(i\in T\) certified by (1). Every selected candidate supported by voter \(i\) has at most \(n\) supporters in \(S\); hence its contribution to (2) is at least \(1/n\), whereas the omitted candidate contributes \(1/t\). Consequently,
\[
F_i(S,x)\ge\frac1t+\frac{u_i}{n}. \tag{3}
\]
For \(k=1\), when \(t<n\) the first term alone exceeds \(1/n\); when \(t=n\), (1) forces \(u_i\ge1\), proving strictness. For \(k=2\): if \(t<n/2\), the first term exceeds \(2/n\). At \(t=n/2\), (1) forces \(u_i\ge1\). At \(n/2<t<n\), it again forces \(u_i\ge1\), and \(n/t>1\). At \(t=n\), (1) forces \(u_i\ge2\). In every case (3) is strictly greater than \(2/n\). Therefore a usual EJR+ committee cannot fail (2) when \(k\le2\).

**At most two voters.** For \(n=1\), the only eligible coalition is the singleton, for which (1) and (2) are identical. Now take \(n=2\). For a singleton coalition supported by \(x\), (1) again coincides with (2), because each positively supported winner contributes one. For \(S=\{1,2\}\) and \(t=1\), every supported selected candidate contributes a total of exactly one to the two scores, because its denominator equals its number of approvers; the candidate \(x\) contributes another one. Thus \(F_1+F_2=k+1>k\), so one voter has score greater than \(k/2\). Here it is essential that all \(k\) winners are approved by someone. For \(t=2\), each selected approval contributes \(1/2\) and each voter approves \(x\), so \(F_i=(u_i+1)/2\); (1) for \(T=S\) directly establishes (2). Thus every usual EJR+ full committee with \(n\le2\) satisfies payment-strong EJR+ up-to-one.

**Three voters and three seats.** With \(n=k=3\), (1) for a nonempty \(T\) of size \(t\in\{1,2,3\}\) gives a voter \(i\in T\) with \(u_i\ge t\). Inequality (3) yields \(F_i\ge1/t+t/3>1\) for all three possible values of \(t\).

**Consequent sharp lower bound.** A separation needs \(n\ge3\), \(k\ge3\), \(m\ge k+1\); the case \((n,k)=(3,3)\) is excluded. Thus either \(n=3\) and \(m\ge5\), or \(n\ge4\) and \(m\ge4\). In both cases \(n+m\ge8\). The two explicit configurations in the Finding attain equality.

**Verification of the two Pareto-efficient witnesses.** For \(n=3\), the unelected candidate is approved by voters 2 and 3. Both already have utility two; for either nonempty \(T\subseteq\{2,3\}\), \(n(u_i+1)=9>4|T|\), giving (1). At \(S=\{1,2,3\}\), \(t=2\), the scores are respectively \(1/2+1/2+1/3=4/3\), \(1/2+1/3+1/2=4/3\), and \(4/3\), violating strict (2). For \(n=4\), voters 3 and 4 have selected utility one; for all nonempty \(T\subseteq\{3,4\}\), \(4(1+1)=8>3|T|\). With \(S\) all four voters and \(t=2\), voters 1 and 2 each receive \(1/2+1/4=3/4\), while voters 3 and 4 each receive \(1/4+1/2=3/4\), violating strict (2).

With exactly one omitted candidate \(x\), a committee of \(k\) approved winners is Pareto-efficient if and only if no winner \(d\) has \(A_d\subsetneq A_x\). Indeed, replacing such a winner by \(x\) is a strict Pareto improvement. Conversely, if at least one winner is removed in any alternative committee, all voters approving that winner must approve the sole new candidate \(x\), so that winner's supporters must be a subset of \(A_x\); if equality holds, the exchange does not strictly benefit anyone. Both displayed configurations satisfy this criterion.

**Complete boundary census.** At \(n+m=8\), the lower-bound proof leaves precisely \((n,m,k)=(3,5,4)\) and \((4,4,3)\). Label approver subsets by nonzero bit masks. Up to permutation of selected candidates, a committee is a nondecreasing multiset of \(k\) masks, together with the mask of its one unelected candidate. There are respectively
\[
\binom{7+4-1}{4}\,7=1470,\qquad
\binom{15+3-1}{3}\,15=10200
\]
such signatures. The exact-integer enumeration in `verify.py` tests (1) and (2) for all nonempty coalitions, then forms orbits under every voter permutation. It finds 18 separating signatures in four orbits (sizes \(6,3,3,6\)) in the first regime and six signatures in one orbit in the second. The canonical orbit representatives (selected masks; omitted mask) are
\[
\begin{array}{ll}
(1,1,2,7);6 &(\text{not PO}),\\
(1,1,6,7);6 &(\text{PO}),\\
(1,2,4,7);3 &(\text{not PO}),\\
(1,2,5,7);6 &(\text{not PO}),\\
(1,2,15);12 &(\text{PO, four voters}).
\end{array}
\]
The exhaustive finite census together with the analytical lower bound establishes all claimed minimality, orbit, and Pareto-efficiency assertions.

## Verification

`verify.py` is a Python 3 standard-library-only, standalone exact-integer checker. Run `python3 verify.py` from the directory containing this file. It computes the denominator-clearing least common multiple, evaluates all coalitions for weak and strong axioms independently, enumerates every candidate-approver signature at the two sharp boundary regimes, canonicalizes every separating profile under voter relabeling, and tests the displayed Pareto-efficiency criterion. It also scans 19,448 smaller canonical signatures as cross-checks. The expected concluding line is `VERIFY_OK sharp_boundary=8 pareto_witnesses=2`. The exhaustive certificate covers all of the stated finite boundary classification, while the proof above (not finite sampling) establishes the infinite lower bound.

## Relationship to prior work

Skowron [1] introduces the payment-based strong EJR+ conditions, proves that his weak up-to-one formulation recovers ordinary approval EJR+, and already shows a separation using 1,000 voters and twenty elected candidates (Example 4). Those definitions, the implication, and the existence of some separation are **not** new here. Brill and Peters [2] introduced ordinary EJR+. Dong and Peters [3] studied axiomatic characterizations of the earlier EJR+ and PJR+ notions. The present result determines a sharp smallest voter-plus-candidate boundary, enumerates all five minimal types, and distinguishes the Pareto-efficient ones. It does not claim a new general existence theorem or a stronger voting axiom.

## Limitations

The sharp count uses the total \(n+m\) with a full size-\(k\) committee, strictly positive support for each selected candidate, candidate approval duplicates allowed, and exactly the source's strong up-to-one (not its stronger exact) axiom. No statement about minimality under arbitrary weighted candidate costs, fractional utilities, or a different size metric is made. The finite census relies on the fully included checker and exact-integer arithmetic. The publication-priority comparison covers relevant accessible sources but cannot exclude all unpublished or unindexed equivalent classifications. Independent verification has not been performed.

## References

[1] P. Skowron, *Robust Proportionality Axioms for Additive Utilities*, arXiv:2610.15516, first public 2026-10-11. https://arxiv.org/abs/2610.15516 . Definitions 3–4, Theorem 1, Example 4.

[2] M. Brill and J. Peters, *Robust and Verifiable Proportionality Axioms for Multiwinner Voting*, arXiv:2302.01989, first public 2023-02-03. https://arxiv.org/abs/2302.01989 . Section 3.

[3] C. Dong and J. Peters, *An Axiomatic Analysis of Proportionality Notions in Approval-Based Multiwinner Voting*, arXiv:2605.04612, first public 2026-05-06. https://arxiv.org/abs/2605.04612 . Sections 2–4.

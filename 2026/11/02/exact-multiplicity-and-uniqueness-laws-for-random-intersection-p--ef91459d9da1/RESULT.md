# Exact multiplicity and uniqueness laws for random intersection-priority school assignments

## Finding

**Theorem (stable-assignment multiplicity).** Fix integers \(n\ge 1\) and \(t\ge 2\). There are \(n\) students and \(n\) unit-capacity schools, all mutually acceptable. Every student has the same strict preference \(s_1\succ s_2\succ\cdots\succ s_n\). Independently for every school and every one of its \(t\) priority criteria, draw a uniform random strict ordering of the students. A student has unanimous priority over another at a school precisely when all \(t\) orders rank the first student higher. A perfect matching is *intersection-priority stable* if no student prefers a school assigned to someone she unanimously outranks there. Let \(Z_{n,t}\) count these matchings. Then

\[
\mathbb E Z_{n,t}=\prod_{m=1}^{n}\Phi_t(m),\qquad
\Phi_t(m)=\sum_{j=1}^{m}(-1)^{j-1}\binom mj\frac{1}{j^{t-1}},
\qquad
\Pr(Z_{n,t}=1)=\frac{1}{(n!)^{t-1}}.
\]

For two criteria, \(\Phi_2(m)=H_m=\sum_{j=1}^{m}1/j\), yielding the especially simple law

\[
\mathbb E Z_{n,2}=\prod_{m=1}^{n}H_m,\qquad \Pr(Z_{n,2}=1)=1/n!.
\]

For each *fixed* \(t\ge2\), these formulas further imply

\[
\Phi_t(m)\sim\frac{(\log m)^{t-1}}{(t-1)!},\qquad
\log\mathbb E Z_{n,t}=(t-1)n\log\log n-n\log((t-1)!)+o(n).
\]

The factorization itself has a more general structural form. Suppose independently drawn school priorities have a common label-exchangeable, restriction-consistent random strict-partial-order law. Let \(a_m\) be the expected number of maximal students and \(b_m\) the probability of a unique maximal student under that law on \(m\) labels. Then \(\mathbb E Z_n=\prod_{m=1}^{n}a_m\) and \(\Pr(Z_n=1)=\prod_{m=1}^{n}b_m\). This statement is about the total number of stable assignments, not the number of Pareto-undominated stable assignments.

## Assumptions and scope

Students and schools are labeled. Priorities have no ties within each constituent order, although their intersection need not compare every pair. Distinct priority criteria, including those of the same school, are independent; priorities of distinct schools are also independent. Every complete assignment is individually rational and non-wasteful. Weak stability for two criteria agrees with the intersection-priority notion in Kitahara and Okumura (2026), Proposition 1; for multiple criteria, the intersection formulation agrees with weak M-stability in Kitahara and Okumura (2023), Appendix A.1. The independent-random-priority assumption is a mathematical null model, not a claim that actual original and adjusted priorities are independent. Degenerate equal orders are included in the sampling space.

A maximal element of a strict partial order on a finite set \(R\) is an element of \(R\) that no other member of \(R\) outranks. A restriction-consistent family of priority laws means that restriction to any \(m\)-element labeled subset has the same relabeled law for all supersets; label exchangeability means permutation invariance of that law.

## Proof

**Step 1: Sequential characterization.** Identify a matching with the permutation \(\pi=(\pi_1,\ldots,\pi_n)\), assigning student \(\pi_i\) to school \(s_i\). At school \(s_i\), every student placed at a later school prefers \(s_i\) to her own assignment, whereas a student placed earlier prefers her own assignment. Consequently the matching is stable if and only if, for every \(i\), \(\pi_i\) is maximal under the intersection priority at \(s_i\) among the remaining students \(R_i=\{\pi_i,\ldots,\pi_n\}\). This characterization is exact in both directions, and every partial sequence of maximal choices can be completed because every nonempty finite partial order has a maximal element.

**Step 2: General expectation factorization.** For one prescribed permutation \(\pi\), the event of maximality at stage \(i\) depends only on the random priority at \(s_i\). These events are independent across schools. Exchangeability gives probability \(a_m/m\) that the specific prescribed student is maximal among the prescribed \(m\) remaining students. Therefore

\[
\Pr(\pi\text{ stable})=\prod_{m=1}^{n}\frac{a_m}{m}.
\]

There are exactly \(n!\) prescribed permutations. Summing their indicators, \(\mathbb E Z_n=n!\prod_m(a_m/m)=\prod_m a_m\).

**Step 3: General uniqueness factorization.** If the set of maximal students at the first school has two or more members, selecting either one leads to a distinct complete stable assignment by Step 1. Thus exactly one stable assignment exists if and only if there is exactly one maximal choice at every school along its necessarily unique sequential path. Conditional on all earlier choices, the set remaining before a school is determined, but that school's priority is fresh and independent. Restriction consistency makes the conditional probability of having a single maximal choice equal to \(b_m\) when \(m\) students remain. Multiplying conditional probabilities gives \(\Pr(Z_n=1)=\prod_{m=1}^{n}b_m\).

**Step 4: Random intersections.** Realize \(t\) independent uniform linear orders on \(m\) students by ranking \(t\) independent uniform coordinates in \([0,1]\) for each student. A student with coordinates \((u_1,\ldots,u_t)\) is maximal, when larger coordinates are better, exactly if no other point lies in the box with coordinates larger than all her coordinates. Her conditional maximality probability is \((1-\prod_{r=1}^{t}(1-u_r))^{m-1}\). With \(v_r=1-u_r\), symmetry and expansion yield

\[
\begin{aligned}
a_m&=m\int_{[0,1]^t}\left(1-\prod_{r=1}^{t}v_r\right)^{m-1}\,dv_1\cdots dv_t\\
&=m\sum_{k=0}^{m-1}(-1)^k\binom{m-1}{k}(k+1)^{-t}\\
&=\sum_{j=1}^{m}(-1)^{j-1}\binom mj j^{-(t-1)}=\Phi_t(m).
\end{aligned}
\]

The last equality is \(m\binom{m-1}{j-1}/j=\binom mj\). A finite intersection partial order has exactly one maximal element if and only if all \(t\) constituent orderings have the same first-ranked element: the first-ranked element of every constituent order is maximal under the intersection, while a common first-ranked element dominates everyone. The first elements of the independent uniform orders are independent uniform student labels, so \(b_m=m^{-(t-1)}\). Steps 2 and 3 now establish both exact formulas. For \(t=2\), the standard finite identity \(\sum_{j=1}^{m}(-1)^{j-1}\binom mj/j=H_m\) follows, for example, by integrating \((1-(1-x)^m)/x\) on \([0,1]\).

**Step 5: Fixed-criterion asymptotics.** A product of \(t\) independent uniform random variables has density \(( -\log u)^{t-1}/(t-1)!\) on \((0,1)\). Therefore

\[
\Phi_t(m)=\frac{m}{(t-1)!}\int_0^1(1-u)^{m-1}(-\log u)^{t-1}\,du.
\]

Substituting \(z=mu\) and dividing by \((\log m)^{t-1}\), the integrand becomes \((1-z/m)^{m-1}(1-\log z/\log m)^{t-1}\) on \(0<z<m\). For \(m\ge2\), the first factor is at most \(e^{-z/2}\). For \(0<z\le1\), the second factor is at most \((1+|\log z|)^{t-1}\); for \(1\le z<m\), it is at most one. These bounds provide an integrable majorant independent of \(m\). Pointwise the integrand tends to \(e^{-z}\). Dominated convergence therefore gives the stated leading term. Summing \(\log\Phi_t(m)=(t-1)\log\log m-\log((t-1)!)+o(1)\) over \(m\ge3\) and using Cesàro averaging proves the formula for \(\log\mathbb E Z_{n,t}\). The finitely many smaller indices contribute only \(O(1)\).

## Verification

The standalone pure-Python verifier `verify_counts.py` enumerates *every* priority profile for \((n,t)=(2,2),(3,2),(2,3)\) and tests all perfect matchings directly for blocking pairs, independently of a second recursive maximal-choice enumeration. For \((3,2)\), it checks all \(6^{6}=46{,}656\) labeled priority profiles. The complete distribution of \(Z_{3,2}\) has multiplicities \((7776,14256,11664,9072,2592,1296)\) for values \((1,2,3,4,5,6)\), respectively. It follows that \(\mathbb E Z_{3,2}=11/4\), \(\Pr(Z_{3,2}=1)=1/6\), and \(\operatorname{Var}(Z_{3,2})=227/144\). These are exact finite computations, not substitutes for the all-size proof.

The separate `verify_local.py` enumerates local random intersection posets for \(m\le4\) and up to three criteria where computationally bounded, verifying the predicted \(a_m\) and \(b_m\) using exact rational arithmetic. Both scripts require only Python 3. Run `python3 verify_counts.py` and `python3 verify_local.py` from the directory containing these files.

## Relationship to prior work

Kitahara and Okumura (2023, *School Choice with Multiple Priorities*, Appendix A.1, Proposition 3) establish that weak M-stability under several priority lists is ordinary stability under their intersection; their September 2026 paper (*School Choice Problems with Priority Adjustments*, Proposition 1) formulates the two-list weak-stability condition. The sequential maximal-choice criterion uses that established formulation, but the product law for the *number* of stable matchings, its uniqueness probability, and its growth for independent random priorities are not stated in those inspected works.

Bentley, Kung, Schkolnick, and Thompson (1978) independently analyze the expected number of maximal vectors under independent coordinate orderings. The local factor \(\Phi_t(m)\), including \(H_m\) for \(t=2\), is therefore known mathematics; novelty is not claimed for that local factor. The result here combines the local law with a new school-by-school multiplicity/uniqueness factorization. Pittel (2019), Section 3, studies stable matchings under *independently randomized preference lists on both sides*; it does not give the present common-student-order specialization, whose student-side preferences are perfectly correlated. Earlier partial-priority school-choice extension theorems likewise do not provide this random multiplicity formula.

## Limitations

Only complete balanced, one-seat markets with a common strict ranking of schools, and statistically independent exchangeable school priorities, are covered. The model does not establish typical concentration of \(Z_{n,t}\); the expectation may differ greatly from a typical outcome. It does not describe cases with correlated original and adjusted priorities, distinct student school preferences, quotas greater than one, incomplete lists, or market-specific constraints. Weak stability is not strong or super stability. The contribution is a theorem under a mathematical null model; it is not an empirical claim or an independent scientific audit. The local maxima identity is pre-existing; unindexed equivalent school-matching computations remain a priority risk.

## References

1. M. Kitahara and Y. Okumura, *School Choice Problems with Priority Adjustments*, arXiv:2609.12558, first posted 2026-09-11, https://arxiv.org/abs/2609.12558. Proposition 1 and Section 2.
2. M. Kitahara and Y. Okumura, *School Choice with Multiple Priorities*, arXiv:2308.04780, first posted 2023-08-09, https://arxiv.org/abs/2308.04780. Appendix A.1, especially Proposition 3.
3. M. Kitahara and Y. Okumura, *On Extensions of Partial Priorities in School Choice*, arXiv:2305.00641, first posted 2023-05-01, https://arxiv.org/abs/2305.00641. Section 2.
4. B. Pittel, *On Random Stable Matchings: Cyclic Matchings with Strict Preferences and Two-Side Matchings with Partially Ordered Preferences*, arXiv:1911.07425, 2019, https://arxiv.org/abs/1911.07425. Section 3.
5. J. L. Bentley, H. T. Kung, M. Schkolnick and C. D. Thompson, *On the Average Number of Maxima in a Set of Vectors and Applications*, Journal of the ACM 25(4), 536–543, 1978, https://doi.org/10.1145/322092.322095. Section 2.

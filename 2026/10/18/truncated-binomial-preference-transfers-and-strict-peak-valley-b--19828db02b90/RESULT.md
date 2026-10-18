# Truncated-binomial preference transfers and strict peak–valley bias in random parking functions

## Finding

Let \(n\ge 2\) and let \(\Pi=(\Pi_1,\ldots,\Pi_n)\) be a uniformly chosen classical parking function on \(\{1,\ldots,n\}\). Write \(M_j=\#\{i:\Pi_i=j\}\). For **every** pair \(1\le a<b\le n\), condition on the loads at all values other than \(a,b\), and on \(T=M_a+M_b\). Whenever this conditioning event has positive probability, set

\[
R=\max\left\{0,\max_{a\le k<b}\left(k-\sum_{\substack{1\le j\le k\\j\notin\{a,b\}}}M_j\right)\right\}.
\]

Then \(0\le R\le T\), and the **exact conditional law** is

\[
M_a\mid\bigl((M_j)_{j\notin\{a,b\}},T\bigr)
\ \overset{d}{=}\
\operatorname{Bin}(T,1/2)\mid\{\operatorname{Bin}(T,1/2)\ge R\}.
\]

In particular, for all integers \(r>s\ge0\),

\[
\Pr(M_a=r,M_b=s)\ge\Pr(M_a=s,M_b=r),
\]

and \(M_a\) stochastically dominates \(M_b\). The pairwise inequality also holds **conditional on every feasible set of the other loads and on \(T=r+s\)**.

For \(n\ge3\), define the strict central-peak and central-valley probabilities

\[
p_n^+=\Pr(\Pi_1<\Pi_2>\Pi_3),\qquad
p_n^-=\Pr(\Pi_1>\Pi_2<\Pi_3),
\]

and the common corresponding probability for three independent uniforms on \(\{1,\ldots,n+1\}\),

\[
p_n^0=\frac{n(2n+1)}{6(n+1)^2}.
\]

The **sharp direction** of the finite-sample ensemble discrepancy is

\[
\boxed{p_n^+>p_n^0>p_n^-},\qquad
\boxed{p_n^++p_n^-=2p_n^0}.
\]

More precisely,

\[
\boxed{
 p_n^+-p_n^-=
 \frac{1}{n(n-1)(n-2)}\,
 \mathbb E\!\left[
 \sum_{1\le a<b\le n} M_aM_b(M_a-M_b)
 \right] >0.
}
\]

The difference is at least \((n+1)^{-(n-1)}\); this simple explicit bound is not claimed to be asymptotically sharp. The theorem concerns **preferences**, not the order in which cars ultimately occupy parking spaces.

## Assumptions and scope

A length-\(n\) classical parking function is a word \(\pi\in\{1,\ldots,n\}^n\) for which the sorted preferences satisfy \(\pi_{(k)}\le k\) for all \(1\le k\le n\). Equivalently its loads \(m_j\) are nonnegative, sum to \(n\), and satisfy

\[
\sum_{j=1}^k m_j\ge k,\qquad k=1,\ldots,n.
\]

All such words have equal probability; their number is \((n+1)^{n-1}\). Indices \(a,b,k\) refer to preferred parking-space **values**. Coordinates \(1,2,3\) refer to three **cars** (exchangeable because the success condition is invariant under permutations of cars). No independence is assumed between their preferences. The truncation theorem also includes \(n=2\); the peak–valley theorem begins at \(n=3\).

## Proof

**1. Conditional truncated-binomial law.** Fix \(a<b\), feasible other counts \((m_j)_{j\notin\{a,b\}}\), and \(T=m_a+m_b\). If \(m_a=r\), the final load is \(m_b=T-r\). The load-prefix inequalities with \(k<a\) depend only on the fixed other counts, and those with \(k\ge b\) depend on the fixed other counts and \(T\). The remaining inequalities, for \(a\le k<b\), are exactly

\[
r\ge k-\sum_{\substack{1\le j\le k\\j\notin\{a,b\}}}m_j.
\]

Hence the feasible values of \(r\) are precisely the integers \(R,R+1,\ldots,T\). Since a load vector has \(n!/\prod_jm_j!\) realizing words, its conditional weight is proportional to \(1/[r!(T-r)!]\), or \(\binom{T}{r}\). Normalization proves the asserted truncated-binomial law, including \(T=0\).

For any \(r>s\ge0\) with \(r+s=T\), the conditional mass at \(r\) is no smaller than that at \(s\): if \(s\) is feasible then so is \(r\), and their unnormalized binomial coefficients are equal; otherwise the latter mass may be positive while the former is zero. Average over the other counts and \(T\) to obtain the joint probability inequality. Pairing configurations with load pairs \((r,s)\) and \((s,r)\) proves \(\mathbb E[h(M_a)]\ge\mathbb E[h(M_b)]\) for any nondecreasing \(h\), i.e. stochastic dominance.

**2. Exact peak-minus-valley identity.** Conditional on the load vector \(m\), every order of its multiset of \(n\) labels is equally likely. Among the ordered triples of **distinct car indices**, a triple with three distinct preference values contributes equally to the number of central peaks and valleys: for any unordered triple of distinct values there are two arrangements of each type. A triple with two equal low values \(a\) at the endpoints and one higher value \(b\) at the center is a peak; the reversed load pattern, with two high values \(b\) at the endpoints and one lower \(a\) at the center, is a valley. Their respective ordered counts are \(m_a(m_a-1)m_b\) and \(m_b(m_b-1)m_a\). All-equal triples contribute to neither. Therefore

\[
\Pr(\Pi_1<\Pi_2>\Pi_3\mid M=m)-
\Pr(\Pi_1>\Pi_2<\Pi_3\mid M=m)
=\frac{\sum_{a<b}m_am_b(m_a-m_b)}{n(n-1)(n-2)}.
\]

Taking expectations yields the exact identity.

For each \(a<b\), pair the load configurations with \((m_a,m_b)=(r,s)\) and \((s,r)\), \(r>s\). The contribution to \(\mathbb E[M_aM_b(M_a-M_b)]\) is

\[
rs(r-s)\,[\Pr(M_a=r,M_b=s)-\Pr(M_a=s,M_b=r)]\ge0.
\]

At \(a=1,b=n\), take the feasible load vector \(m_1=n-1,m_n=1\), all other loads zero. Its swapped vector \(m_1=1,m_n=n-1\) violates the prefix inequality at \(k=2\) when \(n\ge3\). This single strictly unmatched pair contributes \(n(n-1)(n-2)\) to the unnormalized expectation of the sum above (there are \(n\) words realizing the first vector). Dividing by \((n+1)^{n-1}n(n-1)(n-2)\) establishes both strict positivity and the stated lower bound.

**3. Exact peak-plus-valley identity.** Pollak's classical cyclic-shift correspondence partitions all \((n+1)^n\) words over \(\{1,\ldots,n+1\}\) into free orbits of length \(n+1\) by adding the same constant to each coordinate modulo \(n+1\). Exactly one member of each orbit is a classical parking function. Thus every statistic invariant under a common cyclic shift of the **preference values** has the same law for a uniform parking function as for \(n\) independent uniform \(\{1,\ldots,n+1\}\) preferences. In particular, the equality partition of the first three preferences has exactly the same distribution.

Conditional on all three preferences being distinct, their order is uniformly one of six possibilities, and the probability of peak *or* valley is \(2/3\). Conditional on exactly two equal preferences, exchangeability of car coordinates makes the repeated value appear in the two endpoint positions with probability \(1/3\), which is precisely the event of a strict peak or valley. If all three agree, neither event occurs. Hence the peak-plus-valley probability depends only on the equality partition and agrees with the independent-uniform model. In that model exchangeability of **value order** gives equal peak and valley probabilities, each equal to

\[
\sum_{v=1}^{n+1}\frac1{n+1}\left(\frac{v-1}{n+1}\right)^2
=\frac{n(2n+1)}{6(n+1)^2}.
\]

Therefore \(p_n^++p_n^-=2p_n^0\). Combining with strict positivity from step 2 proves \(p_n^+>p_n^0>p_n^-\) for all \(n\ge3\).

## Verification

The included `verify.py` uses only Python's standard library. Run `python3 verify.py` to reproduce exact integer and rational checks; the script requires no input files or internet access. It enumerates every feasible load profile through \(n=7\), validates the conditional truncated-binomial support and relative weights for every pair and feasible conditioning, verifies the pair rearrangement inequality, and exhaustively enumerates all preference words through \(n=6\) to check the peak-minus-valley identity and peak-plus-valley formula. It also evaluates the count, quadratic-load and signed-cubic-load recurrences through \(n=40\).

For the last computation, after processing load values through \(j-1\), maintain weighted sums \(W,B,Q\) over profiles, with \(B=\sum_i m_i^2\) and \(Q=\sum_{a<b}m_am_b(m_a-m_b)\). If the previous total is \(s\), appending a load \(t\) with \(s+t\ge j\) multiplies the weight by \(\binom{n-s}{t}\) and transforms these weighted sums via

\[
(W,B,Q)\mapsto\binom{n-s}{t}
\bigl(W,\ B+t^2W,\ Q+tB-t^2sW\bigr).
\]

Summing over all feasible state transitions produces the exact unnormalized third-order contrast \(Q\). Finite tests are checks of the derivation, not a proof for arbitrary \(n\): the proof is in the preceding section.

## Relationship to prior work

Diaconis and Hicks [1, Section 4, remarks following Theorem 11] explicitly observe that **strict peaks** fail their finite-sample equivalence-of-ensembles phenomenon; they prove equal-distribution statements for weak peaks and equality patterns, and describe the classical cyclic-rotation principle. The new result is not the known failure of strict-peak equidistribution, but the **direction for every sample size**, the exact signed load-moment identity, and a general **conditional truncated-binomial law** for moving preference mass between arbitrary earlier and later values.

Kenyon and Yin [2] establish a generalized parking-function forest construction, single-coordinate laws and some two-coordinate covariances. Bellin [3] analyzes asymptotic first-coordinate uniformity. Yin [4] establishes general multi-coordinate formulas using multi-shuffles. These concern coordinate preferences and related combinatorics, but their inspected statements do not give the conditional joint law of two **occupancy counts** nor the complete strict peak–valley ordering above. The ballot-prefix criterion, multinomial weight and Pollak cyclic rotation are classical ingredients; those inputs are not claimed to be new.

## Limitations

The result concerns ordinary classical parking functions and three strict preference orderings; it does not claim the exact closed form or asymptotic rate of the positive gap beyond its moment identity and elementary lower bound. The conditional law requires feasible conditioning data. Finite computations cannot independently establish an all-\(n\) theorem. As with any literature comparison, older multivariate parking-function generating functions might imply a formula in another guise; the inspected sources did not furnish a dominating statement.

## References

1. Persi Diaconis and Angela Hicks, *Probabilizing Parking Functions*, arXiv:1611.09821 (first posted 2016-11-29); https://arxiv.org/abs/1611.09821 . Especially Section 4 on strict versus weak peaks and species.
2. Richard Kenyon and Mei Yin, *Parking functions: From combinatorics to probability*, arXiv:2103.17180 (first posted 2021-03-31); https://arxiv.org/html/2103.17180v1 . Especially Sections 2.1, 3.3–3.4.
3. Etienne Bellin, *Asymptotic behaviour of the first positions of uniform parking functions*, arXiv:2108.08661 (first posted 2021-08-19); https://arxiv.org/abs/2108.08661 . Especially Section 1 and its main asymptotic statements.
4. Mei Yin, *Parking functions, multi-shuffle, and asymptotic phenomena*, arXiv:2112.02251 (first posted 2021-12-04); https://arxiv.org/abs/2112.02251 . Especially Theorem 2.7 on multiple fixed-coordinate counts.

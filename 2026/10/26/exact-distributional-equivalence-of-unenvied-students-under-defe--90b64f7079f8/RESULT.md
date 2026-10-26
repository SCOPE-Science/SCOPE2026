# Exact distributional equivalence of unenvied students under deferred acceptance and random serial dictatorship

## Finding

In the square random school-choice model with independent uniformly random complete strict student preferences and independent uniformly random strict school priorities, let \(U_n^{\mathrm{DA}}\) and \(U_n^{\mathrm{RSD}}\) be the numbers of students whom no other student envies under student-proposing deferred acceptance (DA) and random serial dictatorship (RSD), respectively. For every integer \(n\geq 1\),
\[
 U_n^{\mathrm{DA}}\ \overset{d}=\ U_n^{\mathrm{RSD}}\ \overset{d}=\ S_n,
\]
where \(S_n\) is the number of coupon types appearing exactly once when independent uniform coupon draws stop upon first observing all \(n\) types. This is equality of the entire finite-market distributions, not merely of their known expectations.

More strongly, order RSD students by their random serial priority, and for each position \(i\in\{1,\ldots,n\}\) let \(I_i\) indicate that the student at position \(i\) is unenvied. Order coupon types by first appearance and let \(J_i\) indicate that the type first seen at position \(i\) occurs exactly once before completion. Then
\[
 (I_1,\ldots,I_n)\ \overset{d}=\ (J_1,\ldots,J_n).
\]
For every \(1\leq k_1<\cdots<k_r\leq n\), this joint law has the explicit inclusion probabilities
\[
 \Pr(I_{k_1}=\cdots=I_{k_r}=1)
 = \Pr(J_{k_1}=\cdots=J_{k_r}=1)
 = \frac{r!}{\prod_{s=1}^{r}(n-k_s+s)}.
\]

Consequences include nonnegative and typically strictly positive dependence among unenvied-position indicators. Writing \(a=n-i+1\), \(b=n-j+1\) for \(i<j\),
\[
 \operatorname{Cov}(I_i,I_j)=\frac{b-1}{ab(b+1)},
\]
which is strictly positive when \(j<n\). With \(H_n=\sum_{a=1}^{n}a^{-1}\) and \(H_n^{(2)}=\sum_{a=1}^{n}a^{-2}\), the exact variance under both mechanisms is
\[
 \operatorname{Var}(U_n)
 =H_n-H_n^{(2)}+2\sum_{b=2}^{n-1}\frac{b-1}{b(b+1)}(H_n-H_b).
\]
In particular, the variance is asymptotic to \((\log n)^2\), and
\[
 \frac{U_n^{\mathrm{DA}}}{\log n}\ \overset{d}\longrightarrow\ \operatorname{Exp}(1),\qquad
 \frac{U_n^{\mathrm{RSD}}}{\log n}\ \overset{d}\longrightarrow\ \operatorname{Exp}(1).
\]
The exponential coupon-collector limit is previously established; its transfer to these two school-choice mechanisms is a consequence of the distributional equivalence proved here.

## Assumptions and scope

There are exactly \(n\) students and \(n\) unit-capacity schools, and every student finds every school acceptable. Each student's strict ranking of all schools is drawn independently and uniformly from all \(n!\) permutations. For DA, schools' strict priority lists are independent uniform permutations, independent of students' preferences. For RSD, the serial order is uniform and independent of preferences; exchangeability permits conditioning on its realized order and relabeling positions \(1,\ldots,n\). An agent envies a different agent if they strictly prefer that agent's assigned school to their own. No notion of justified envy or school-side utility is used.

The coupon process consists of independent uniform draws from an \(n\)-type alphabet, stopped upon the first draw completing the full collection. Each coupon type has a distinct first-appearance rank. No result is claimed for unequal school quotas, correlated or nonuniform preferences, incomplete rankings, or arbitrary nonuniform priorities.

## Proof

**Step 1 (RSD joint inclusion probability).** Fix any subset \(K\subseteq\{1,\ldots,n\}\) of serial positions whose students are required to be unenvied. An earlier serial chooser cannot envy a later one: when choosing, the earlier student could have selected the school later assigned, and instead chose a strictly preferred available school.

At stage \(t\geq2\), there are \(m_t=n-t+1\) schools remaining. Define \(a_t=|K\cap\{1,\ldots,t-1\}|\). Each earlier selected position has a different, already assigned school. To ensure that all previously selected students are unenvied by student \(t\), the student's most preferred item among the \(m_t+a_t\) schools consisting of the currently available schools and these \(a_t\) assigned schools must belong to the currently available set. Conditional on every past choice and every past satisfaction of the required events, student \(t\)'s preference ranking is still independent and uniform. The conditional success probability is therefore exactly
\[
 \frac{m_t}{m_t+a_t}=\frac{n-t+1}{n-t+1+a_t}.
\]
Multiplication over stages gives
\[
 \Pr(K\subseteq\{i:I_i=1\})
 =\prod_{t=2}^{n}\frac{n-t+1}{n-t+1+|K\cap\{1,\ldots,t-1\}|}.
\]
Notice that this product includes constraints imposed on selected positions themselves by *later* students; it does not assert independence of the unenvied indicators.

**Step 2 (coupon joint inclusion probability).** Order coupon types by first appearance. Fix the same subset \(K\) of first-appearance positions and require each designated type to remain a singleton until cover time. Between the arrival of the \((t-1)\)-st and \(t\)-th new types, \(m_t=n-t+1\) types are unseen and exactly \(a_t\) previously seen types are designated. Irrelevant repetitions of previously seen, undesignated types can be ignored. The next draw belonging either to an unseen type or to a designated type is unseen with exact probability \(m_t/(m_t+a_t)\), by independent uniform coupon draws. The requirement holds precisely if this success occurs at every stage. Hence the coupon joint inclusion probability is the identical product from Step 1.

For every subset \(K\), the probabilities of the events \(K\subseteq\{i:I_i=1\}\) and \(K\subseteq\{i:J_i=1\}\) coincide. Inclusion-exclusion on the finite Boolean cube uniquely reconstructs the joint mass of the two indicator vectors, proving \((I_i)_i\overset d=(J_i)_i\) and therefore \(U_n^{\mathrm{RSD}}\overset d=S_n\).

**Step 3 (DA coupon representation).** This representation is established in Ortega, Ziegler, Arribillaga, and Zhao (2026), and it also admits the following direct reconstruction. Generate each independent uniform student preference permutation by successively deleting repeated entries from that student's infinite independent uniform coupon stream. Regardless of which currently unmatched student next proposes, the next unused raw draw of that student's stream is uniform and independent of past raw draws. Consequently, the concatenated adaptive raw stream is independent uniform coupon sampling. In an equal-size one-to-one DA market, the algorithm terminates exactly when every school has received a proposal, which is exactly the first time every school has appeared in the raw stream: the first occurrence of a school cannot be discarded as a repeated choice of the proposing student. A school receives exactly one distinct student's proposal if and only if its type occurs exactly once before that cover time. Indeed, a discarded repeat can only concern a school to which that student already proposed and from which the student was subsequently displaced by some *different* proposer.

Every school holds one student at termination. A matched student is envied by another student if and only if that other student previously proposed to the matched school's school: a rejected proposer ends with a strictly less preferred school, and a student who prefers a school to their final assignment must have proposed to it. Thus the count of unenvied matched students equals the number of single-proposer schools, which equals \(S_n\) in law. Combining this with Step 2 proves the principal distributional equivalence.

**Step 4 (closed forms and fluctuations).** For \(K=\{k_1<\cdots<k_r\}\), grouping the factors in Step 1 between successive marked positions and telescoping factorials gives
\[
 \Pr(K\subseteq\{i:I_i=1\})=\frac{r!}{(n-k_1+1)(n-k_2+2)\cdots(n-k_r+r)}.
\]
For a singleton this is \(\Pr(I_i=1)=1/(n-i+1)\). For \(i<j\) it is \(2/[(n-i+1)(n-j+2)]\), yielding the displayed covariance after subtracting the product of the marginals. Summing variances and pairwise covariances proves the exact variance identity. Since \((b-1)/(b(b+1))=1/b+O(b^{-2})\), the double harmonic sum has leading term \(\tfrac12(\log n)^2\), yielding \(\operatorname{Var}(U_n)\sim(\log n)^2\).

For any fixed positive integer \(r\), the joint inclusion identity gives
\[
 \mathbb E\binom{U_n}{r}=r!\!\sum_{n\geq a_1>\cdots>a_r\geq1}\ \prod_{s=1}^{r}\frac1{a_s+s-1}.
\]
For fixed \(r\), terms having one \(a_s\) bounded contribute only \(O_r((\log n)^{r-1})\). On unbounded indices the fixed shifts \(s-1\) are negligible; symmetry of distinct-index harmonic sums then gives \(\mathbb E\binom{U_n}{r}\sim (\log n)^r\). Therefore every fixed normalized ordinary moment converges to \(r!\), the moments of a unit-mean exponential law; this distribution is moment-determinate. The stated convergence in distribution follows. This limit is also known for the equivalent coupon-collector singleton count, and is included here as a transferred consequence rather than as a new coupon-collector theorem.

## Verification

Run the included `verify.py` with Python 3; it requires only the standard library. It performs exact-rational computations of coupon-collector singleton laws through \(n=8\), checks the telescoped joint inclusion formula for every subset through \(n=8\), exhausts all \(331{,}997\) strict-profile RSD instances summed over \(1\leq n\leq4\), and exhausts all \(46{,}673\) complete student-preference/school-priority DA instances summed over \(1\leq n\leq3\). The checks were executed successfully (551 exact assertions in addition to profile enumeration). The exhaustive computations cover only these finite sizes; the mathematical proof above establishes the result for every \(n\geq1\).

For illustration, both mechanisms have for \(n=3\) the distribution \((7/18,7/18,2/9)\) at counts \((1,2,3)\). At \(n=4\), the distribution of RSD unenvied counts and of coupon singletons is \((97/288,97/288,67/288,3/32)\) at counts \((1,2,3,4)\).

## Relationship to prior work

Ortega, Ziegler, Arribillaga, and Zhao (2026) derive the exact harmonic-number expectation for the unenvied count under DA and RSD. Their full-text DA argument identifies the count with coupon singletons and their RSD argument computes one-position marginals. The new statement is that the **full joint indicator law** under RSD is the coupon first-appearance singleton law, yielding equality of the full DA/RSD *count distributions*. The known equality of expectations alone does not imply this result.

Myers and Wilf (2003/2006) obtained the distribution of coupon singletons, so the coupon probability law itself is not new. Papanicolaou and Doumas (2020) established the exponential limit for the coupon collector's younger sibling's missing types, equivalent to the singleton count, so that coupon limit is also credited. The contribution is the explicit, proof-supported matching-mechanism distributional bridge and the resulting finite-market joint inclusion and covariance formulas for RSD positions. No claim is made that the underlying coupon collector formulas or the earlier expected-value identity were newly discovered.

## Limitations

This proof compares distributions across random markets, not their outcomes on a fixed identical preference profile. DA and RSD can and do produce different matchings. The equivalence concerns the **count** of unenvied students (and RSD's indicators when indexed by serial position), not the full envy graph, the set of students by identity, or the count of students who envy nobody. Nonuniform or correlated preference models may break the equivalence. The result has received only self-review, and historical-priority uncertainty remains, particularly for differently named distributional identities in older matching literature.

## References

1. J. Ortega, G. Ziegler, R. P. Arribillaga, and G. Zhao (2026), *The Distribution of Envy in Matching Markets*, Economics Letters 263, 112936, DOI: 10.1016/j.econlet.2026.112936; first publicly available online 2026-03-12; arXiv:2603.23385. See especially sections 2.1 and 3.
2. A. N. Myers and H. S. Wilf (2003), *Some New Aspects of the Coupon Collector's Problem*, SIAM Journal on Discrete Mathematics 17(1), 1–17, DOI: 10.1137/S0895480102403076; reprinted in SIAM Review 48(3) (2006), 549–565, DOI: 10.1137/060654438; arXiv:math/0304229.
3. V. G. Papanicolaou and A. V. Doumas (2020), *The Coupon Collector's Brother*, arXiv:2005.05270.
4. A. Abdulkadiroğlu and T. Sönmez (1998), *Random Serial Dictatorship and the Core from Random Endowments in House Allocation Problems*, Econometrica 66(3), 689–701.

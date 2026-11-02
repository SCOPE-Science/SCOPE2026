# Distributional equality of unenvied agents under deferred acceptance and random serial dictatorship

## Finding
Fix an integer \(n\ge 1\). In a one-to-one market of \(n\) students and \(n\) unit-capacity schools, take independent uniformly random complete strict student rankings; for student-proposing deferred acceptance (DA), take independent uniformly random strict school priorities. Define a student to be **unenvied** when no other student ranks that student's assigned school above their own assigned school. Let \(X_n^{\mathrm{RSD}}\) and \(X_n^{\mathrm{DA}}\) be the numbers of unenvied students under random serial dictatorship (RSD) and DA, respectively. Let \(S_n\) count the coupon types occurring exactly once in an independent uniform coupon stream, stopped as soon as all \(n\) types have appeared.

**Theorem (complete count-law equivalence and indexed RSD joint law).** For every \(n\ge 1\),
\[
X_n^{\mathrm{RSD}}\ \stackrel{d}{=}\ X_n^{\mathrm{DA}}\ \stackrel{d}{=}\ S_n.
\]
Further, fix the RSD picking order and denote by \(I_i\) the indicator that its student in position \(i\) is unenvied. For any integer \(r\) with \(1\le r\le n\) and any positions \(1\le i_1<\cdots<i_r\le n\),
\[
\Pr(I_{i_1}=\cdots=I_{i_r}=1)
=\frac{r!}{\prod_{t=1}^{r}(n-i_t+t)}.
\]
These statements are independent of which fixed student order is used, and therefore also hold when the order is uniformly randomized.

For \(1\le j\le n\), an exact form of the common count distribution is
\[
\Pr(X_n^{\mathrm{RSD}}=j)
=j\binom nj\int_0^\infty t^{j-1}(e^t-1-t)^{n-j}e^{-nt}\,dt.
\]
This integral is the pre-existing coupon-singleton formula of Myers and Wilf; the asserted extension to RSD and the mechanism-to-mechanism count-law equality are the results here.

Writing \(H_n=\sum_{a=1}^n a^{-1}\) and \(H_n^{(2)}=\sum_{a=1}^n a^{-2}\), the common mean and variance are
\[
\mathbb E X_n^{\mathrm{RSD}}=H_n,\qquad
\operatorname{Var}(X_n^{\mathrm{RSD}})=H_n^2+2H_n^{(2)}-3H_n.
\]
The same holds for DA, and, as \(n\to\infty\),
\[
\frac{X_n^{\mathrm{RSD}}}{\log n}
\ \Longrightarrow\ \operatorname{Exp}(1),\qquad
\frac{X_n^{\mathrm{DA}}}{\log n}
\ \Longrightarrow\ \operatorname{Exp}(1).
\]
The coupon-singleton variance and exponential limit were known before this matching-model application. In particular, equality of means is much weaker than the equality at every finite-market threshold established here.

## Assumptions and scope
All preferences are independent uniformly random permutations of the same \(n\) schools; there are no ties, incomplete lists, vacancies or capacity constraints beyond one seat per school. RSD allocates one distinct school to each student in serial order. DA means the usual student-proposing algorithm with strict priorities sampled independently of student preferences. Envy is unqualified ordinal envy, not justified envy under priorities. This theorem concerns the **number** of unenvied students, not an equality in distribution of the entire assignments, all envy edges or the identities of unenvied students. The indexed joint law applies to RSD positions, not DA positions.

## Proof
**1. A distribution-preserving coupon exposure for RSD.** Fix an RSD picking order. Generate each student's independent uniformly random strict ranking as follows: give that student an independent infinite sequence of independent uniform school labels, and order schools by first occurrence in that sequence. Every first-occurrence ordering is uniform over permutations, and the orderings are independent across students. For each student expose only the initial portion of their sequence up to and including the first label not yet allocated. This is precisely that student's highest-ranked available school, so it implements RSD.

Concatenate all exposed portions in picking order. At each exposed draw the next school label is independent and uniform, including when the draw is the first one for the next student. Exactly one previously unseen school is allocated by each student's final exposed draw. Consequently the concatenated stream is an independent uniform coupon stream stopped at its first complete collection of all \(n\) labels. This statement concerns the stopped sequence; individual unused tails of the students' sequences are irrelevant.

No earlier RSD student envies a later student, since the later student's school was still available when the earlier student chose. A later student envies the school allocated in position \(i\) exactly when that earlier school occurs in the later student's exposed prefix: its first occurrence in the later student's preference sequence must precede the first available school, which is the later student's allocation. Thus the position-\(i\) student is unenvied exactly when their allocated school is never drawn after its discovery. As its discovery is its first draw in the concatenated sequence, this is precisely the event that its coupon type occurs **once** before stopping. The representation identifies the RSD unenvied count pathwise with the coupon singleton count.

**2. The DA side of the common law.** Ortega, Ziegler, Arribillaga and Zhao (2026, Proposition 1 and its proof) construct an independent uniform raw school-draw sequence by exposing student proposals in the sequential DA implementation. Their argument establishes that an under-demanded school, meaning one receiving exactly one student's proposal, is exactly a coupon label occurring once in those raw draws up to first coverage. A school receiving only one proposal is the assigned school of an unenvied student: other students never preferred it to the school to which they were finally assigned under DA. Conversely, if some student preferred it to their final assigned school, DA would have involved a proposal to it (unless it was their own final assignment). Hence the DA unenvied count has the same coupon-singleton distribution. Combining this previously established DA correspondence with Step 1 proves the distributional equality without requiring a coupling of the full DA and RSD allocations.

**3. The indexed RSD joint probabilities.** Fix \(1\le i_1<\cdots<i_r\le n\). At picking position \(k\), suppose \(b_k=|\{t:i_t<k\}|\) of the designated positions have already selected. There are \(m_k=n-k+1\) available schools. Conditional on earlier selections, the position-\(k\) student's independent uniform ranking places its highest-ranked element of the union of those \(m_k\) available schools and the \(b_k\) designated earlier schools in the available subset with probability \(m_k/(m_k+b_k)\). This is exactly the requirement that student \(k\) envy no designated earlier school. Taking the product of these conditional probabilities over positions yields
\[
\Pr(I_{i_1}=\cdots=I_{i_r}=1)
=\prod_{k=1}^{n}\frac{n-k+1}{n-k+1+b_k}.
\]
The factors are one through position \(i_1\). On each interval \(i_t<k\le i_{t+1}\) the numerator is \(n-k+1\) and the denominator is \(n-k+1+t\); after \(i_r\), the denominator shift is \(r\). Expanding these finite products into factorial ratios cancels all interior factorials and leaves
\[
\prod_{k=1}^{n}\frac{n-k+1}{n-k+1+b_k}
=\frac{r!}{\prod_{t=1}^r(n-i_t+t)},
\]
including when the last designated position is \(n\), when the last product block is empty.

**4. Exact moments and limit.** The case \(r=1\) of Step 3 gives \(\mathbb E X_n=H_n\). For \(i<j\), the joint probability is \(2/((n-i+1)(n-j+2))\). Thus
\[
\sum_{i<j}\mathbb E[I_iI_j]
=2\sum_{a=2}^{n}\frac{H_a-1}{a}
=H_n^2+H_n^{(2)}-2H_n,
\]
using \(\sum_{a=1}^n H_a/a=(H_n^2+H_n^{(2)})/2\). Since \(X_n=\sum_i I_i\), this proves the stated variance.

The integral distribution follows by applying the established coupon-singleton formula (Myers and Wilf, 2003, Section 4, equation (47)) to Step 1. The exponential limit follows directly from the known coupon-singleton limit (Papanicolaou and Doumas, 2020); alternatively, Step 3 gives a self-contained moment route. Indeed, for fixed positive integer \(r\),
\[
\mathbb E\binom{X_n}{r}
=r!\sum_{a_1>\cdots>a_r\ge1}^{a_1\le n}
\prod_{t=1}^{r}\frac{1}{a_t+t-1}
=H_n^r+O_r(H_n^{r-1}).
\]
To justify the last estimate, replacing \(1/(a_t+t-1)\) by \(1/a_t\) produces an error bounded by \(O_r(H_n^{r-1})\) since \(\sum_{a\ge1}a^{-2}<\infty\); the ordered-distinct sum of \(\prod_t1/a_t\) equals \(H_n^r/r!+O_r(H_n^{r-1})\). Hence all ordinary moments of \(X_n/H_n\) converge to \(r!\), the moments of a mean-one exponential law. This law is moment-determinate, and \(H_n/\log n\to1\).

## Verification
The standalone file `verify_rsd_coupon.py` performs three independent rational-arithmetic checks. First, for \(n=1,2,3,4\) it enumerates all preference-rank tuples conditional on one specified sequence of RSD assignments, totaling 13,863 tuples, and counts unenvied positions directly from the preference comparisons. Second, a finite-state coupon-collection recursion, with irrelevant repeat draws eliminated, computes the coupon-singleton count law for \(n=1,\ldots,12\). Third, a distinct computation expands the indexed joint law into a probability generating polynomial and compares its coefficients with the coupon recursion for those twelve sizes; it also checks the exact first two moments. The direct enumerations agree with both other computations. The result printed by the included program is:

```
VERIFY_OK n=1..12 coupon_exact=joint_probability_exact direct_ranks_n=1..4 count=13863
```

For example, when \(n=3\), the probabilities of exactly \(1,2,3\) unenvied students are \(7/18,7/18,2/9\); when \(n=4\), the probabilities are \(97/288,97/288,67/288,3/32\). These finite computations check the formulas but do not establish them for general \(n\); the preceding proof does.

## Relationship to prior work
Ortega, Ziegler, Arribillaga and Zhao (2026) prove the coupon-singleton interpretation for DA and establish \(\mathbb E X_n^{\mathrm{DA}}=\mathbb E X_n^{\mathrm{RSD}}=H_n\). Their RSD calculation treats one serial position at a time and only then sums expectations; it does not establish a common full count law or joint probabilities for multiple positions. Myers and Wilf (2003) derive the complete coupon-singleton distribution, and Papanicolaou and Doumas (2020) derive its variance and exponential limiting law; these coupon results are used and credited rather than represented as new. The distinct contribution is the RSD pathwise coupon correspondence, hence the finite-market **distributional**, not merely mean, equality across the two assignment mechanisms, together with explicit position-indexed RSD joint probabilities. Existing findings on RSD lottery supports, efficiency, or small-market DA/TTC differences do not imply this statistic's count-law equality.

## Limitations
The theorem requires independent uniform strict complete student preferences. Correlated preferences, nonuniform preference distributions, multi-seat schools, unequal market sides and imperfect lists are not treated; the DA part uses its standard independent-priority random model. Count-law equality does not imply identical allocations, identical envy graphs or a pathwise coupling of the two matching mechanisms. The integral, coupon variance and exponential law were already known on the coupon side. The possibility of an unindexed earlier matching-market distributional identity has not been excluded by exhaustive literature verification, and access to the publisher's final PDF was restricted even though the complete author preprint was inspected. No independent audit has been performed.

## References
- J. Ortega, G. Ziegler, R. P. Arribillaga and G. Zhao, *The Distribution of Envy in Matching Markets*, Economics Letters 263 (2026), article 112936; arXiv:2603.23385, https://arxiv.org/abs/2603.23385. Early online March 12, 2026.
- A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229 (first public April 16, 2003), Section 4, https://arxiv.org/abs/math/0304229.
- V. G. Papanicolaou and A. V. Doumas, *The Coupon Collector's Brother*, arXiv:2005.05270 (2020), https://arxiv.org/abs/2005.05270.

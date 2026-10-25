# Opposite conditional and unconditional covariance signs for color-separated singleton runs

## Finding

Let a uniformly sampled linear binary word contain \(a\ge2\) ones and \(b\ge2\) zeros, with \(n=a+b\). Let \(X\) be the number of maximal one-symbol runs consisting of a single one, \(Y\) the analogous singleton zero-run count, and \(R\) the total number of maximal constant runs. Their means and mixed moment are exactly

\[
\begin{aligned}
\mathbb E[X]&=\frac{ab(b+1)}{n(n-1)},\\
\mathbb E[Y]&=\frac{ab(a+1)}{n(n-1)},\\
\mathbb E[XY]&=\frac{ab\bigl((ab)^2+ab(n-7)+4\bigr)}{n(n-1)(n-2)(n-3)}.
\end{aligned}
\]

The **unconditional** covariance is strictly positive:

\[
\operatorname{Cov}(X,Y)=\frac{2ab(a-1)(b-1)\bigl(ab(2n-3)-2n\bigr)}{n^2(n-1)^2(n-2)(n-3)}>0.
\]

In contrast, the **conditional** covariance given the total run count is always nonpositive. It vanishes for every attainable even \(R=2t\). For each attainable odd \(R=2t+1\), define

\[
w_1=\binom{a-1}{t}\binom{b-1}{t-1},\qquad
w_0=\binom{a-1}{t-1}\binom{b-1}{t},
\]

where out-of-range binomial coefficients are zero. Then

\[
\operatorname{Cov}(X,Y\mid R=2t+1)
=-\frac{4t^2w_1w_0}{(a-1)(b-1)(w_1+w_0)^2}\le0.
\]

It is strictly negative exactly when both endpoint orientations occur. In particular, for every \(a,b\ge2\), \(R=3\) is attainable and

\[
\operatorname{Cov}(X,Y\mid R=3)=-\frac{4}{(n-2)^2}<0.
\]

Thus positive unconditional association reverses to nonpositive association at **every** fixed total-run count, and to strict negative association already at three runs.

## Assumptions and scope

The sample space consists of the \(\binom n a\) binary words with exactly \(a\) ones and \(b\) zeros, all with equal probability. Runs are maximal consecutive identical symbols in a *linear*, not cyclic, word. An endpoint bit may be a singleton run. Each assumption \(a,b\ge2\) is essential to the displayed nondegenerate positive/negative signs; cases with fewer of either symbol are not part of the theorem. Conditioning is only on attainable \(R\), so the event has positive probability. The integers \(a,b\) need not be equal.

## Proof

**1. Unconditional moments.** For nonnegative integers \(p,q\) define the exact probability of prescribing \(p\) ones and \(q\) zeros at distinct fixed positions by

\[
P_{p,q}=\frac{(a)_{p}(b)_{q}}{(n)_{p+q}},
\]

with falling factorials and zero probability when a prescription is infeasible. Writing \(X=\sum_iX_i\), where \(X_i\) indicates an isolated one at position \(i\), the two boundary positions contribute \(2P_{1,1}\), and the \(n-2\) interior positions contribute \((n-2)P_{1,2}\). Therefore

\[
\mathbb E[X]=2P_{1,1}+(n-2)P_{1,2}=\frac{ab(b+1)}{n(n-1)}.
\]

Interchanging the two symbols gives the formula for \(\mathbb E[Y]\).

For \(n\ge6\), enumerate the ordered pairs \((i,j)\) for which an isolated one at \(i\) and an isolated zero at \(j\) can coexist. Coincident positions and pairs at distance two are incompatible. Adjacent positions at distance one contribute

\[
2P_{2,1}+2P_{1,2}+2(n-3)P_{2,2}.
\]

Pairs at distance at least three contribute

\[
2P_{2,2}+2(n-4)(P_{3,2}+P_{2,3})+(n-4)(n-5)P_{3,3}.
\]

The factors distinguish whether each indicated singleton is at an endpoint or an interior position. Adding and simplifying yields

\[
\mathbb E[XY]=\frac{ab\bigl((ab)^2+ab(n-7)+4\bigr)}{n(n-1)(n-2)(n-3)}.
\]

For \(n=4\) or \(n=5\), the only admissible compositions are \((a,b)=(2,2),(2,3),(3,2)\). Directly enumerating their \(6\) or \(10\) words gives the same formula; the standalone finite verifier independently checks each configuration. Subtracting the product of the means and factoring yields the stated covariance identity.

Since \(ab-2(n-2)=(a-2)(b-2)\ge0\),

\[
ab(2n-3)-2n\ \ge\ 4(n-1)(n-3)>0
\]

for \(n\ge4\), establishing strict unconditional positivity.

**2. Conditional run compositions.** Fix the starting bit and the two run counts \(r_1,r_0\). Then the positive lengths of the one-runs form a uniformly chosen composition of \(a\) into \(r_1\) positive parts. Independently, the positive lengths of the zero-runs form a uniformly chosen composition of \(b\) into \(r_0\) positive parts. This follows from a bijection between those pairs of compositions and fixed-start binary words with given run counts. If \(s\) positive parts sum to \(m\ge2\), the probability that a specified part equals one is \((s-1)/(m-1)\). Consequently

\[
\mathbb E[X\mid r_1,r_0,\text{start}]=\frac{r_1(r_1-1)}{a-1},\qquad
\mathbb E[Y\mid r_1,r_0,\text{start}]=\frac{r_0(r_0-1)}{b-1}.
\]

Moreover, \(X\) and \(Y\) are conditionally independent given the fixed starting bit and both run counts.

If \(R=2t\), necessarily \(r_1=r_0=t\), irrespective of the starting bit; thus conditional component means are the same and the covariance is zero. If \(R=2t+1\), the two possible endpoint orientations have respective counts \((r_1,r_0)=(t+1,t)\) and \((t,t+1)\). The numbers of words with these two orientations are exactly

\[
w_1=\binom{a-1}{t}\binom{b-1}{t-1},\quad
w_0=\binom{a-1}{t-1}\binom{b-1}{t}.
\]

Within either orientation, the covariance is zero, while moving from the second orientation to the first changes the conditional mean of \(X\) by \(2t/(a-1)\) and that of \(Y\) by \(-2t/(b-1)\). The two-component covariance identity therefore gives

\[
\operatorname{Cov}(X,Y\mid R=2t+1)
=\frac{w_1w_0}{(w_1+w_0)^2}
\frac{2t}{a-1}\frac{-2t}{b-1}.
\]

This proves the odd-run formula and its strictness criterion. For \(t=1\), the weights are \(w_1=a-1\), \(w_0=b-1\), giving \(-4/(n-2)^2\). The theorem follows.

## Verification

Run `python3 verify.py` alongside this document. Its independent enumerator explicitly constructs every fixed-composition binary word for \(4\le n\le13\), computes its complete run decomposition, groups by total run count, and compares exact rational empirical covariances with both analytic formulas. It also checks the algebraic covariance factorization and strict sign for all \(2\le a,b\le49\). The reproducible execution passed **5,648 exact rational and sign assertions** and enumerated **16,178 words**. These finite tests are corroboration, not a proof for unbounded parameters.

## Relationship to prior work

The Wald–Wolfowitz fixed-composition runs-test framework concerns the total number of runs; Smeeton and Cox (2003) give an explicit permutation-shuffling exposition and the run-count distribution. Doğanaksoy et al. (2015) study length-one, length-two, and length-three runs for randomness tests, motivating singleton runs of distinct colors as interpretable clustering diagnostics. The result here relates **the joint counts of singleton one-runs and singleton zero-runs under fixed composition** and contrasts the marginal covariance sign with the covariance after conditioning on the total number of runs. This statement is not asserted by either inspected source.

The older works of Barton and David (1957) on multiple runs and Barton (1967) on completed runs above and below the median are especially plausible sources for joint run-count methods; their complete primary texts were inaccessible during the comparison. They may contain more general generating-function machinery from which part of the present covariance calculation could be derived. Historical priority remains subject to further evaluation. No claim is made that elementary run-composition or factorial-moment identities are themselves new.

## Limitations

The result applies only to finite uniformly shuffled binary strings with fixed counts of each symbol; it does not imply such a sign reversal for arbitrary independent Bernoulli strings, Markov words, cyclic runs, or nonuniform permutations. Covariance sign is not a claim of stochastic order or statistical independence. Conditional covariance can vanish for degenerate odd orientations as specified. General historical-priority risk remains for older multiple-run literature and independently uninspected full texts.

## References

1. N. Smeeton and N. J. Cox (2003), *Do-it-yourself Shuffling and the Number of Runs under Randomness*, *Stata Journal* 3, 270–277. DOI: `10.1177/1536867X0300300304`.
2. A. Doğanaksoy, F. Sulak, M. Uğuz, O. Şeker, Z. Akcengiz (2015), *New Statistical Randomness Tests Based on Length of Runs*, *Mathematical Problems in Engineering*, article 626408, first public April 9, 2015. DOI: `10.1155/2015/626408`.
3. D. E. Barton and F. N. David (1957), *Multiple Runs*, *Biometrika* 44, 168–178. DOI: `10.1093/biomet/44.1-2.168` (full text not inspected).
4. D. E. Barton (1967), *Completed Runs of Length k above and below Median*, *Technometrics* 9, 682–694. JSTOR: `1266207` (full text not inspected).

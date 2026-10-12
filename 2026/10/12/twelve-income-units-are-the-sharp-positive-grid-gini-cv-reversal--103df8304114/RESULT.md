# Twelve income units are the sharp positive-grid Gini–CV reversal boundary
## Finding
Consider two income distributions with the same number
\[
n\ge2
\]
of households and the same total income
\[
S>0.
\]
Assume every household income is a strictly positive integer.

Use the ordinary finite-population Gini coefficient
\[
G
=
\frac{1}{2n^2\mu}
\sum_{i=1}^n\sum_{j=1}^n |x_i-x_j|,
\qquad
\mu=\frac{S}{n},
\]
and the population coefficient of variation
\[
V=\frac{\sigma}{\mu}.
\]
Larger values mean greater inequality for both measures.

Across all household counts, the two weak orderings first differ at total income
\[
S=10.
\]
Up to permutation, the unique first disagreement is
\[
(1,4,5)
\quad\text{versus}\quad
(2,2,6).
\]
The Gini coefficients tie:
\[
G(1,4,5)=G(2,2,6)=\frac4{15},
\]
but
\[
V^2(1,4,5)=\frac{13}{50}
<
\frac8{25}=V^2(2,2,6).
\]

Opposite strict rankings are impossible for every
\[
S\le11.
\]

At
\[
S=12,
\]
strict reversal occurs for the first time, and the reversing pair is unique up to household permutation:
\[
A=(1,2,4,5),
\qquad
B=(2,2,2,6).
\]
Their Gini coefficients are
\[
G(A)=\frac7{24}
>
\frac14=G(B),
\]
so Gini ranks \(A\) as more unequal.

Their squared coefficients of variation are
\[
V(A)^2=\frac5{18}
<
\frac13=V(B)^2,
\]
so the coefficient of variation ranks \(B\) as more unequal.

Thus twelve positive income units are necessary and sufficient for a strict Gini–coefficient-of-variation ranking reversal when household count and total income are held fixed.

For two households, reversal is impossible at every resolution because
\[
V=2G.
\]

## Assumptions and scope
The two distributions being compared have the same household count and the same total income.

Every household income is a strictly positive integer multiple of a common unit. This is a discrete-resolution statement; allowing zero incomes or arbitrary real incomes gives a different boundary problem.

The coefficient of variation uses population standard deviation. If sample standard deviation is used instead, every profile of the same household count is multiplied by the same factor
\[
\sqrt{\frac{n}{n-1}},
\]
so every ranking in this result is unchanged.

Likewise, replacing the ordinary Gini by the common finite-sample correction
\[
\frac{n}{n-1}G
\]
does not change rankings when household count is fixed.

The theorem concerns ordinal inequality comparisons. It does not claim that one measure is normatively preferable.

## Proof
For a fixed household count \(n\) and fixed total income \(S\), write the incomes in nondecreasing order.

The Gini coefficient is
\[
G
=
\frac{1}{nS}
\sum_{i<j}|x_i-x_j|.
\]
Therefore Gini ordering at fixed \((n,S)\) is exactly ordering by the integer quantity
\[
D(x)=\sum_{i<j}|x_i-x_j|.
\]

For the coefficient of variation,
\[
V^2
=
\frac{1}{nS^2}
\sum_{i=1}^n (nx_i-S)^2.
\]
Thus coefficient-of-variation ordering at fixed \((n,S)\) is exactly ordering by the integer quantity
\[
Q(x)=\sum_{i=1}^n (nx_i-S)^2.
\]

Because all incomes are positive integers, every admissible unlabeled profile is an integer partition of \(S\) into exactly \(n\) positive parts. Also
\[
2\le n\le S.
\]
Consequently, to prove a global lower cutoff at \(S=12\), it is enough to enumerate every integer partition for all
\[
2\le S\le12
\]
and compare every unordered profile pair having the same \((n,S)\).

The exact census contains \(762\) such pair comparisons through \(S=12\). The strict-reversal count by total income is
\[
0,0,0,0,0,0,0,0,0,0,1
\]
for
\[
S=2,3,\ldots,12.
\]

The unique strict pair at \(S=12\) is
\[
(1,2,4,5)
\quad\text{and}\quad
(2,2,2,6).
\]
For these vectors,
\[
D(1,2,4,5)=14,
\qquad
D(2,2,2,6)=12,
\]
while
\[
Q(1,2,4,5)=160,
\qquad
Q(2,2,2,6)=192.
\]
The inequalities therefore point in opposite directions.

The first weak-order disagreement is earlier. At \(S=10\), the unique pair is
\[
(1,4,5)
\quad\text{and}\quad
(2,2,6),
\]
with equal Gini numerator but unequal coefficient-of-variation numerator.

For two households, if the incomes are \(a\) and \(b\), then
\[
G=\frac{|a-b|}{2(a+b)}
\]
and
\[
V=\frac{|a-b|}{a+b}=2G,
\]
so the two rankings agree identically.

## Verification
The embedded `verify_gini_cv_integer_boundary.py` uses only exact integer and rational arithmetic.

It generates every nondecreasing positive integer partition of every total
\[
2\le S\le12
\]
for every admissible household count, compares every unordered pair at fixed \((n,S)\), and checks the Gini and coefficient-of-variation orderings through the exact integer quantities \(D\) and \(Q\).

The exact number of pair comparisons through the sharp layer is
\[
762.
\]

It verifies that no strict reversal exists below total \(12\), that exactly one exists at total \(12\), and that the first weak-order disagreement is the unique total-\(10\) Gini tie described above.

It also checks the exact displayed fractions and independently verifies the two-household identity over totals through \(100\).

Run:

`python3 verify_gini_cv_integer_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Sen's treatment of economic inequality discusses the coefficient of variation and the Gini coefficient among the standard positive measures of inequality.

Allison gives explicit formulas for both measures, treats both as scale-invariant inequality measures satisfying the transfer principle, and emphasizes their different transfer sensitivities: the coefficient of variation responds uniformly to equal-sized transfers while Gini sensitivity depends on ranks.

Bendel, Higgins, Teberg, and Pyke directly compare the coefficient of variation and Gini coefficient. Their full paper gives constructed and real-data examples, states that the coefficient of variation is more sensitive to the right tail, and shows that conclusions can depend on which statistic is used.

These sources establish that the measures are distinct and can order empirical populations differently. The accepted claim is narrower: it identifies the exact smallest positive-integer total at fixed household count and fixed total income where a strict reversal is possible, together with the unique first strict pair and the preceding first tie-splitting layer.

Targeted searches using both index names, fixed mean, fixed total income, integer incomes, smallest examples, exact witness vectors, and generalized-entropy language did not locate this finite boundary.

## Limitations
The cutoff is for strictly positive integer incomes. If zero incomes are allowed, strict reversal can occur at a smaller total.

Arbitrary real-valued income vectors do not have an intrinsic smallest total because scale can be changed continuously.

The theorem fixes both population size and total income within each comparison. It does not classify reversals when either quantity differs.

The result concerns only ordinal rankings, not welfare dominance. Lorenz-dominance-consistent inequality measures agree whenever one distribution Lorenz-dominates another; the reversing pair is therefore necessarily outside that dominance relation.

Although the full 1989 Gini–coefficient-of-variation comparison was inspected, an unindexed exercise or computational note could still contain the same small integer witness.

## References
1. A. Sen, *On Economic Inequality*, chapter “Measures of Inequality,” Oxford University Press, published 13 December 1973. DOI: 10.1093/0198281935.003.0002.
2. P. D. Allison, “Measures of Inequality,” *American Sociological Review* 43(6), 865–880, 1978. DOI: 10.2307/2094626.
3. R. B. Bendel, S. S. Higgins, J. E. Teberg, and D. A. Pyke, “Comparison of skewness coefficient, coefficient of variation, and Gini coefficient as inequality measures within populations,” *Oecologia* 78(3), 394–400, 1989. DOI: 10.1007/BF00379115.

# Eleven income units are the sharp Theil-T–mean-log-deviation reversal boundary
## Finding
Consider income profiles with a common number
\[
n\ge2
\]
of households, common total income
\[
S,
\]
and strictly positive integer incomes
\[
x_1,\ldots,x_n.
\]

Theil \(T\), or \(GE(1)\), is
\[
T(x)=\frac1n\sum_{i=1}^n\frac{x_i}{\mu}\log\left(\frac{x_i}{\mu}\right),
\qquad
\mu=\frac Sn.
\]

The mean log deviation, or \(GE(0)\), is
\[
L(x)=\frac1n\sum_{i=1}^n\log\left(\frac{\mu}{x_i}\right).
\]

For every
\[
S\le10,
\]
the two indices induce exactly the same weak inequality ordering on every fixed-\((n,S)\) profile set.

At
\[
S=11,
\]
strict disagreement appears for the first time. Across all household counts, there are exactly three unordered reversal pairs up to household permutation:
\[
(1,4,6)\quad\text{versus}\quad(2,2,7),
\]
\[
(1,5,5)\quad\text{versus}\quad(2,2,7),
\]
and
\[
(1,3,3,4)\quad\text{versus}\quad(2,2,2,5).
\]

For example,
\[
Q(1,5,5)=9765625<13176688=Q(2,2,7),
\]
so Theil \(T\) ranks \((2,2,7)\) as more unequal. But
\[
P(1,5,5)=25<28=P(2,2,7),
\]
and mean log deviation is larger when \(P\) is smaller. Hence mean log deviation ranks \((1,5,5)\) as more unequal.

## Assumptions and scope
Profiles are compared only when household count and total income are identical. All incomes are strictly positive integers, and household labels do not matter.

Strict positivity is required because mean log deviation contains the logarithm of every income. The logarithm base is irrelevant to ranking.

The theorem is a finite-resolution statement. For arbitrary positive real-valued incomes, common rescaling can move the same normalized profiles to any absolute monetary level.

## Proof
At fixed \(n,S\),
\[
T(x)=\frac1S\sum_i x_i\log x_i+\log\left(\frac nS\right).
\]

Define
\[
Q(x)=\prod_i x_i^{x_i}.
\]
Then
\[
T(x)=\frac1S\log Q(x)+\log\left(\frac nS\right),
\]
so Theil \(T\) ranks profiles exactly as the positive integer \(Q(x)\).

For mean log deviation,
\[
L(x)=\log\left(\frac Sn\right)-\frac1n\sum_i\log x_i.
\]

Define
\[
P(x)=\prod_i x_i.
\]
Then
\[
L(x)=\log\left(\frac Sn\right)-\frac1n\log P(x),
\]
so mean log deviation ranks profiles in the reverse order of the positive integer \(P(x)\).

Therefore strict reversal occurs exactly when \(Q\) and \(P\) order a pair in the same direction.

Because positive integer profiles of total \(S\) are precisely integer partitions of \(S\) into \(n\) positive parts, the global lower boundary can be checked exhaustively.

For every
\[
2\le n\le S\le10,
\]
no pair has either a strict reversal or a tie under one index split by the other.

At
\[
S=11,
\]
the complete reversal layer consists of the three pairs stated above.

Their exact integer statistics are
\[
Q(1,4,6)=11943936,\qquad P(1,4,6)=24,
\]
\[
Q(1,5,5)=9765625,\qquad P(1,5,5)=25,
\]
\[
Q(2,2,7)=13176688,\qquad P(2,2,7)=28,
\]
\[
Q(1,3,3,4)=186624,\qquad P(1,3,3,4)=36,
\]
and
\[
Q(2,2,2,5)=200000,\qquad P(2,2,2,5)=40.
\]

In each pair, the profile with larger \(Q\) also has larger \(P\), exactly the reversal condition.

## Verification
The embedded `verify_theil_mld_boundary.py` uses only exact integer arithmetic.

It enumerates every positive integer partition for every
\[
2\le n\le S\le11
\]
and checks all
\[
408
\]
unordered within-\((n,S)\) profile pairs through the sharp layer.

It finds no weak-order disagreement through
\[
S=10
\]
and exactly three strict reversals at
\[
S=11.
\]

Run:

`python3 verify_theil_mld_boundary.py`

The first output line must be `VERIFY_OK`.

No floating-point logarithm comparison is used in the proof of the cutoff.

## Relationship to prior work
Generalized entropy measures are a classical family of decomposable inequality indices.

Biewen and Jenkins treat generalized entropy indices as standard applied inequality measures and develop sampling-variance formulas for complex survey data.

Talih gives the generalized-entropy limiting cases explicitly: mean log deviation and Theil \(T\) arise as logarithmic endpoint measures and weight different parts of the distribution differently.

Shorrocks supplies the classical decomposability background for the generalized-entropy family.

Thus the measures and their differing sensitivities are established prior work. The claim here is narrower: under common household count, common total income, and positive integer incomes, the two endpoint measures have identical weak orderings through total ten, then acquire exactly three strict reversal pairs at total eleven.

Targeted searches using both index names, \(GE(0)\) and \(GE(1)\), ranking-reversal language, fixed-total integer incomes, and the exact sharp profiles did not locate this finite boundary.

## Limitations
The eleven-unit threshold belongs to the positive-integer grid and is not an absolute monetary threshold for real-valued data.

The theorem compares only Theil \(T\) with mean log deviation and does not classify all generalized-entropy parameters.

The full text of Shorrocks' 1980 article was not available through the checked open route, so no whole-document noncoverage claim is made for that source.

An unindexed teaching example or software regression test could contain an individual small witness even though the sharp global boundary was not located.

## References
1. M. Biewen and S. P. Jenkins, “Variance Estimation for Generalized Entropy and Atkinson Inequality Indices: the Complex Survey Data Case,” *Oxford Bulletin of Economics and Statistics* 68(3), 371–383, first published online 10 May 2006. DOI: 10.1111/j.1468-0084.2006.00166.x.
2. M. Talih, “A reference-invariant health disparity index based on Rényi divergence,” arXiv:1312.2363, first submitted 9 December 2013; later *Annals of Applied Statistics* 7(2), 1217–1243. DOI: 10.1214/12-AOAS621.
3. A. F. Shorrocks, “The Class of Additively Decomposable Inequality Measures,” *Econometrica* 48(3), 613–625, 1980. DOI: 10.2307/1913126.

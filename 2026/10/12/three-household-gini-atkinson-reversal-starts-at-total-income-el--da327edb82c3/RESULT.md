# Three-household Gini–Atkinson reversal starts at total income eleven
## Finding
Consider positive household incomes with a fixed common total.

Let \(G\) denote the ordinary finite-population Gini coefficient, and let \(A_1\) denote the Atkinson inequality index with inequality-aversion parameter
\[
\epsilon=1.
\]

With two households, \(G\) and \(A_1\) induce exactly the same weak inequality ordering.

With three households, write the sorted incomes as
\[
a\le b\le c,
\qquad
a+b+c=S.
\]
Then
\[
G=
\frac{2(c-a)}{3S},
\]
while the \(\epsilon=1\) Atkinson index is
\[
A_1
=
1-
\frac{(abc)^{1/3}}{S/3}
=
1-
\frac{3(abc)^{1/3}}{S}.
\]

Thus, at fixed total \(S\), Gini inequality increases exactly with the range
\[
R=c-a,
\]
whereas Atkinson inequality increases exactly as the product
\[
P=abc
\]
decreases.

Consequently two equal-total three-household distributions \(x\) and \(y\) receive opposite strict inequality rankings if and only if
\[
(R_x-R_y)(P_x-P_y)>0.
\]

On the positive-integer grid, the two weak orderings first differ at total income
\[
S=9.
\]
The pair
\[
(1,4,4)
\quad\text{and}\quad
(2,2,5)
\]
has the same Gini coefficient,
\[
G=\frac29,
\]
but different products,
\[
16<20,
\]
so \(A_1\) ranks \((1,4,4)\) as more unequal.

Strict reversal remains impossible through
\[
S=10.
\]

At total income
\[
S=11,
\]
strict reversal appears for the first time. Up to household permutation, the unique reversing pair is
\[
X=(1,5,5),
\qquad
Y=(2,2,7).
\]
Their Gini coefficients are
\[
G(X)=\frac8{33}
<
\frac{10}{33}
=G(Y),
\]
so Gini ranks \(Y\) as more unequal.

But
\[
1\cdot5\cdot5=25
<
28=2\cdot2\cdot7,
\]
so the geometric-mean equivalent income is smaller for \(X\), and therefore
\[
A_1(X)>A_1(Y).
\]
Atkinson with \(\epsilon=1\) ranks \(X\) as more unequal.

## Assumptions and scope
All incomes are strictly positive.

Comparisons are made at the same population size and the same total income, so both indices compare distributional shape rather than mean income.

The Gini coefficient is the ordinary finite-population version without the optional small-sample rescaling factor. Multiplying all Gini values at a fixed household count by the same positive correction would not change any ranking result.

The Atkinson parameter is fixed at
\[
\epsilon=1,
\]
for which equally distributed equivalent income is the geometric mean.

The sharp total-income boundary concerns positive integer incomes. For unrestricted positive real incomes, three households already suffice for strict reversal without an integer-resolution threshold.

## Proof
For two households, let the sorted incomes be
\[
a\le S-a.
\]
Put
\[
d=S-2a\ge0.
\]
The Gini coefficient is a positive constant multiple of \(d\), so it increases with the income gap.

The product is
\[
a(S-a)
=
\frac{S^2-d^2}{4},
\]
which decreases with \(d\). Since the \(\epsilon=1\) Atkinson index increases as the geometric mean decreases, it also increases with \(d\). Hence the two indices induce exactly the same weak ordering for two households.

For three sorted incomes \(a\le b\le c\), the standard finite-population Gini formula reduces to
\[
G
=
\frac{2(c-a)}{3S}.
\]
This follows directly from the weighted-order-statistic form of the Gini coefficient.

For \(\epsilon=1\), Atkinson's equally distributed equivalent income is the geometric mean, so
\[
A_1
=
1-
\frac{3(abc)^{1/3}}{S}.
\]
At fixed \(S\), therefore, Gini order is exactly range order and Atkinson order is exactly reverse product order. The strict-reversal criterion
\[
(R_x-R_y)(P_x-P_y)>0
\]
follows immediately.

For the integer boundary, every unlabeled positive three-household distribution of total \(S\) has a unique sorted representative
\[
1\le a\le b\le c,
\qquad
a+b+c=S.
\]
The embedded verifier enumerates all such representatives for
\[
3\le S\le11
\]
and compares every unordered pair by exact rational Gini values and exact integer products.

It finds no strict reversal for
\[
3\le S\le10
\]
and exactly one at
\[
S=11,
\]
namely
\[
(1,5,5)
\quad\text{versus}\quad
(2,2,7).
\]
Because the enumeration contains every sorted positive integer triple and every unordered pair, this is an exhaustive finite proof of the sharp integer boundary.

## Verification
The embedded `verify_gini_atkinson1_boundary.py` uses only the Python standard library and exact arithmetic.

For each total
\[
3\le S\le11,
\]
it generates every sorted positive integer triple, computes the exact Gini coefficient, records the exact product, and checks every unordered pair.

The strict-reversal counts are
\[
0,0,0,0,0,0,0,0,1
\]
for totals
\[
S=3,4,\ldots,11.
\]

The first Gini-tie split occurs at
\[
S=9
\]
with
\[
(1,4,4)
\quad\text{versus}\quad
(2,2,5).
\]

The first strict reversal occurs at
\[
S=11
\]
and is unique up to permutation.

The script also replays the two-household monotonicity relation through total income \(500\) and checks the three-household range-product criterion through total income \(79\). These finite replays supplement the symbolic proofs rather than replace them.

Run:

`python3 verify_gini_atkinson1_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Atkinson's 1970 paper explicitly frames inequality measurement as an ordinal ranking problem and argues that choosing an inequality summary necessarily encodes social-welfare judgments. For equal means, it proves that noncrossing Lorenz curves force agreement across increasing concave welfare functions, whereas crossing Lorenz curves permit different rankings.

The same paper treats the Gini coefficient among the conventional summary measures and introduces the equally distributed equivalent-income family that became the Atkinson index. For constant relative inequality aversion, it identifies logarithmic utility at
\[
\epsilon=1,
\]
which yields the geometric-mean equivalent income used here.

Atkinson also reports empirical disagreement between Gini rankings and the equally distributed equivalent measure: among fifty pairwise country comparisons with crossing Lorenz curves, the \(\epsilon=1\) measure differs from Gini in five cases. Thus generic Gini–Atkinson disagreement is firmly prior work.

The finding here is narrower: it gives the exact two-household nonreversal theorem, the complete three-household range-product criterion, the first positive-integer weak-order split, and the sharp unique first strict reversal at total income eleven. Targeted searches by metric names, three-household language, smallest-integer language, and the exact witness did not locate this finite boundary.

## Limitations
The integer cutoff is specific to three equally weighted households with strictly positive integer incomes and equal totals.

Different Atkinson aversion parameters have different product or power-mean orderings and therefore different finite boundaries.

Allowing zero incomes makes the \(\epsilon=1\) Atkinson index degenerate at one and changes the problem substantially.

The theorem is about disagreement between summary inequality indices. It does not identify a uniquely correct social welfare ranking; Atkinson's original analysis emphasizes that such rankings embody normative sensitivity choices.

An unindexed teaching example or software test could contain the same eleven-unit witness even though the sharp exhaustive boundary was not located.

## References
1. A. B. Atkinson, “On the Measurement of Inequality,” *Journal of Economic Theory* 2(3), 244–263, published 1 September 1970. DOI: 10.1016/0022-0531(70)90039-6.

# The smallest primitive three-household Gini–Theil reversal has total income thirteen
## Finding
Consider two income distributions over exactly three households. All incomes are positive, and the two distributions have the same total income.

Because both the relative Gini coefficient and Theil's \(T\) index are scale invariant, a rational pair can be scaled uniquely up to a common integer factor. Call the pair primitive when all six incomes are positive integers with joint greatest common divisor \(1\).

Let
\[
G(x)
=
\frac{\sum_{i<j}|x_i-x_j|}{3\sum_i x_i}
\]
be the relative Gini coefficient for three households, and let
\[
T(x)
=
\frac13\sum_{i=1}^3
\frac{x_i}{\mu}
\ln\!\left(\frac{x_i}{\mu}\right),
\qquad
\mu=\frac{x_1+x_2+x_3}{3},
\]
be Theil's \(T\) index.

No pair with common primitive total income at most \(12\) is ranked strictly in opposite directions by \(G\) and \(T\).

At total income
\[
13,
\]
a strict reversal occurs for the first time, and it is unique up to permuting households:
\[
A=(8,3,2),
\qquad
B=(6,6,1).
\]

The Gini coefficients are
\[
G(A)=\frac4{13},
\qquad
G(B)=\frac{10}{39},
\]
so
\[
G(A)>G(B).
\]

For Theil,
\[
T(A)\approx0.1734832051,
\qquad
T(B)\approx0.1875947490,
\]
so
\[
T(A)<T(B).
\]

Thus Gini judges \(A\) more unequal, while Theil judges \(B\) more unequal.

Moreover, this is the first member of an infinite family. For every integer
\[
x\ge6,
\]
set
\[
A_x=(x+2,x-3,2),
\qquad
B_x=(x,x,1).
\]
Both have total income
\[
2x+1.
\]
Then
\[
G(A_x)>G(B_x)
\]
but
\[
T(A_x)<T(B_x).
\]

## Assumptions and scope
There are exactly three households.

All incomes are strictly positive.

Only pairs with equal total income are compared. This removes mean-income effects and isolates the inequality ordering.

The primitive convention removes arbitrary changes of monetary denomination: multiplying both distributions by the same positive rational factor does not alter either index.

The Gini convention is the standard relative mean-difference form. The Theil convention is Theil's \(T\), not the mean logarithmic deviation.

The theorem concerns strict rank reversal. The two indices can cease to have identical weak orderings earlier because Gini ties can be resolved by Theil.

## Proof
Write a sorted three-household distribution as
\[
a\ge b\ge c>0,
\qquad
S=a+b+c.
\]

For three households,
\[
\sum_{i<j}|x_i-x_j|
=
(a-b)+(a-c)+(b-c)
=
2(a-c).
\]
Hence
\[
G(a,b,c)
=
\frac{2(a-c)}{3S}.
\]
At fixed total income, Gini ordering is therefore exactly ordering by the range
\[
a-c.
\]

For Theil,
\[
T(x)
=
\frac1S\sum_i x_i\ln x_i+\ln\!\left(\frac3S\right).
\]
Thus, at fixed \(S\), Theil ordering is exactly the ordering of
\[
\sum_i x_i\ln x_i
=
\ln\!\left(\prod_i x_i^{x_i}\right).
\]
Define the exact integer key
\[
P(x)=\prod_i x_i^{x_i}.
\]

The exhaustive finite classification of all positive integer partitions of
\[
3\le S\le13
\]
shows that no pair with \(S\le12\) has opposite strict order under range and \(P\). At \(S=13\), exactly one unordered pair does:
\[
(8,3,2)
\quad\text{and}\quad
(6,6,1).
\]

Their ranges are
\[
8-2=6
\quad\text{and}\quad
6-1=5,
\]
so Gini ranks the first distribution as more unequal.

Their exact Theil keys are
\[
P(8,3,2)
=
8^8\,3^3\,2^2
=
1811939328
\]
and
\[
P(6,6,1)
=
6^{12}
=
2176782336.
\]
Therefore Theil ranks the second distribution as more unequal.

For the infinite family, \(A_x\) has range
\[
x
\]
while \(B_x\) has range
\[
x-1,
\]
so
\[
G(A_x)>G(B_x).
\]

For Theil it is enough to prove
\[
4(x+2)^{x+2}(x-3)^{x-3}
<
x^{2x}.
\]
Let
\[
f(x)
=
2x\ln x
-
(x+2)\ln(x+2)
-
(x-3)\ln(x-3)
-
2\ln2.
\]
Then
\[
f'(x)
=
\ln\!\left(
\frac{x^2}{(x+2)(x-3)}
\right).
\]
For
\[
x>3,
\]
the denominator is
\[
x^2-x-6<x^2,
\]
so
\[
f'(x)>0.
\]
At \(x=6\), the exact integer comparison is
\[
6^{12}>4\cdot8^8\cdot3^3.
\]
Hence
\[
f(x)>0
\]
for every integer \(x\ge6\), proving
\[
T(A_x)<T(B_x).
\]

## Verification
The embedded `verify_gini_theil_minimal_reversal.py` uses only the Python standard library.

It constructs every positive integer partition of a three-household total in two independent ways:
- recursive nonincreasing partition generation;
- direct enumeration of all positive ordered triples followed by sorting and deduplication.

For every pair at a fixed total it compares:
- Gini exactly as a rational number;
- Theil exactly through the integer order key
  \[
  P(x)=\prod_i x_i^{x_i}.
  \]

The replay verifies:
- no strict reversal for totals \(3\) through \(12\);
- exactly one reversal at total \(13\);
- the unique pair \((8,3,2)\) versus \((6,6,1)\);
- exact Gini values \(4/13\) and \(10/39\);
- exact Theil keys \(1811939328\) and \(2176782336\);
- the infinite-family inequality for every integer \(6\le x\le500\) as a finite consistency check.

The general infinite-family statement is proved analytically in the previous section; the finite replay is not used as a substitute for that proof.

Run:

`python3 verify_gini_theil_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Classical inequality measurement already recognizes that different scalar indices can embody different distributional judgments, especially when Lorenz curves cross.

Cowell's treatment of Theil inequality places the Gini coefficient and Theil's entropy-based index on explicitly different conceptual foundations. It presents Gini as a pairwise-distance style measure and derives Theil's index from information content, while emphasizing that the resulting approaches differ in their implications for inequality.

De Maio's review likewise stresses that the Gini coefficient is only one of several important inequality measures and that generalized-entropy measures provide a different view of where inequality lies in the income distribution.

Those sources motivate comparison of the indices but do not state the smallest primitive equal-total three-household pair on which Gini and Theil reverse, nor the infinite family above.

Targeted literature searches using Gini/Theil aliases, Lorenz-crossing language, three-household equal-total distributions, minimal integer witnesses, and the exact patterns \((8,3,2)\) and \((6,6,1)\) did not locate this boundary theorem.

## Limitations
The smallest-total statement uses primitive positive rational distributions represented by positive integers; it is a lattice-complexity statement, not a claim that monetary units have intrinsic meaning.

Only three-household distributions are classified.

The exact finite classification stops at the first strict reversal total.

Earlier weak-order differences can occur through ties. The theorem isolates strict reversal.

The result does not claim that either Gini or Theil is normatively preferable.

An unindexed exercise, historical table, or software test suite could contain the same minimal pair.

## References
1. F. A. Cowell, “Theil, Inequality Indices and Decomposition,” ECINEQ Working Paper 2005-01, posted 1 October 2005; later published in *Research on Economic Inequality* 13, 341–356, 2006. DOI: 10.1016/S1049-2585(06)13012-4.
2. F. G. De Maio, “Income inequality measures,” *Journal of Epidemiology and Community Health* 61(10), 849–852, published online 14 September 2007. DOI: 10.1136/jech.2006.052969.
3. H. Theil, *Economics and Information Theory*, North-Holland, 1967.

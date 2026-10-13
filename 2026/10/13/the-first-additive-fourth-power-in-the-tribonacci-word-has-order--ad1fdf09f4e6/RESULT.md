# The first additive fourth power in the Tribonacci word has order six
## Finding
Let \(\mathbf{tr}\) be the Tribonacci word, the fixed point beginning in \(0\) of
\[
0\mapsto 01,\qquad 1\mapsto 02,\qquad 2\mapsto 0.
\]
An additive fourth power of order \(n\) is a factor
\[
X_1X_2X_3X_4
\]
with \(|X_i|=n\) for all \(i\) and with the four symbol sums equal.

The minimum order of an additive fourth power in \(\mathbf{tr}\) is
\[
6.
\]
Moreover, there is exactly one distinct length-\(24\) factor of \(\mathbf{tr}\) that is an additive fourth power of order \(6\):
\[
\mathtt{102010102010010201010201}.
\]
Its four blocks are
\[
\mathtt{102010},\quad
\mathtt{102010},\quad
\mathtt{010201},\quad
\mathtt{010201},
\]
and every block has symbol sum \(4\).

## Assumptions and scope
Letters \(0,1,2\) are interpreted as their integer values when taking a symbol sum. The order of an additive power is the common block length, following the standard convention for additive powers.

The statement determines only the first order at which an additive fourth power occurs and completely classifies the factors at that order. It does not characterize all orders of additive fourth powers, nor orders of additive \(k\)-powers for arbitrary \(k\).

A standard published property of the Tribonacci word used for finite exhaustion is its factor complexity
\[
p(m)=2m+1
\]
for every \(m\ge1\).

## Proof
For each candidate order
\[
n\in\{1,2,3,4,5,6\},
\]
an additive fourth power has length \(4n\). Therefore it is enough to inspect the complete sets of Tribonacci factors of lengths
\[
4,\ 8,\ 12,\ 16,\ 20,\ 24.
\]

Iterating the Tribonacci morphism eight times gives a prefix of length \(149\). The numbers of distinct factors of the six required lengths already appearing in this prefix are respectively
\[
9,\ 17,\ 25,\ 33,\ 41,\ 49.
\]
These are exactly
\[
2(4n)+1
\]
for \(n=1,\ldots,6\). Since the Tribonacci word has factor complexity \(p(m)=2m+1\), each observed factor set is therefore the complete factor set of that length in the infinite word.

For every factor of length \(4n\), split it into its four consecutive length-\(n\) blocks and compute the four symbol sums. The numbers of factors for which all four sums are equal are
\[
0,\ 0,\ 0,\ 0,\ 0,\ 1
\]
at orders \(1,2,3,4,5,6\), respectively.

Thus no additive fourth power has order below \(6\). At order \(6\), the sole factor passing the test is
\[
\mathtt{102010102010010201010201},
\]
whose four blocks have sums
\[
4,\ 4,\ 4,\ 4.
\]
This proves both minimality and uniqueness at the minimum order.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The checker constructs the length-\(149\) finite prefix in two equivalent ways: direct morphism iteration and the finite Tribonacci recurrence
\[
W_r=W_{r-1}W_{r-2}W_{r-3}.
\]
It reconstructs all factors at the six relevant lengths, checks that their counts attain the published factor-complexity totals \(2m+1\), and therefore verifies that each finite factor list is exhaustive.

It then independently recomputes each four-block symbol-sum test. It verifies the zero counts through order \(5\), the unique order-\(6\) witness, its block decomposition and sums, and its first occurrence at index \(76\) in the certified prefix.

## Relationship to prior work
Popoli, Shallit, and Stipulanti study additive complexity and additive powers in the Tribonacci word. They prove that the orders of additive cubes are recognized by a \(4927\)-state Tribonacci automaton. For additive fourth powers, they report that the analogous Walnut computation requires much more memory and appears beyond a simple desktop computation, and they explicitly pose the problem of characterizing orders of additive \(k\)-powers in the Tribonacci word.

An earlier presentation by Shallit gives the additive-cube order sequence and the same finite-automaton framework, but does not state an additive-fourth-power order.

Lejeune, Rigo, and Rosenfeld prove that the ordinary factor complexity of the Tribonacci word is
\[
p(m)=2m+1.
\]
That theorem supplies the finite-exhaustion certificate used here, but concerns factor counting rather than additive fourth powers.

Targeted searches under “additive fourth power”, “additive 4-power”, the Tribonacci word, the candidate order, and the explicit witness located the direct open-problem paper and cube-order material, but no published statement of the minimum order \(6\) or the unique shortest factor.

## Limitations
This is a sharp first-occurrence result, not a solution of the full order-characterization problem. Orders larger than \(6\) can exhibit substantially more complicated behavior.

The proof relies on the published global factor-complexity formula \(p(m)=2m+1\) to certify that the finite factor lists are exhaustive.

An unindexed note, computation, or unpublished dataset could contain the same minimum-order observation even though the inspected direct literature and targeted searches do not report it.

## References
1. P. Popoli, J. Shallit, and M. Stipulanti, “Additive Word Complexity and Walnut,” arXiv:2410.02409v1, first public version 2024-10-03; FSTTCS 2024, LIPIcs 323, Article 32, DOI 10.4230/LIPIcs.FSTTCS.2024.32.
2. M. Lejeune, M. Rigo, and M. Rosenfeld, “Templates for the \(k\)-Binomial Complexity of the Tribonacci Word,” Advances in Applied Mathematics 112 (2020), 101947, DOI 10.1016/j.aam.2019.101947.
3. J. Shallit, “Abelian and Additive Powers in the Tribonacci Word,” Combinatorics on Words presentation, 2021-11-22.

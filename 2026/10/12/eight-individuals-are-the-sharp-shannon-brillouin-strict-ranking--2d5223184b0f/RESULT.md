# Eight individuals are the sharp Shannon–Brillouin strict-ranking boundary
## Finding
Let an ecological abundance profile be an unlabeled multiset of strictly positive integer species abundances
\[
n_1,\ldots,n_S,\qquad \sum_i n_i=N,
\]
with
\[
p_i=\frac{n_i}{N}.
\]

Shannon diversity is
\[
H_S=-\sum_i p_i\log p_i.
\]

Brillouin diversity is
\[
H_B=\frac{\log(N!)-\sum_i\log(n_i!)}{N}.
\]

For every
\[
N\le6,
\]
the two indices induce exactly the same weak ordering on all abundance profiles of total \(N\).

At
\[
N=7,
\]
weak-order agreement first fails, but only through a tie:
\[
(1,1,1,4)\quad\text{and}\quad(2,2,3)
\]
have the same Brillouin diversity, while Shannon ranks \((1,1,1,4)\) strictly higher.

No opposite strict ranking occurs through \(N=7\).

At
\[
N=8,
\]
strict reversal appears for the first time. Up to species permutation there are exactly two unordered reversing pairs:
\[
(1,1,1,5)\quad\text{versus}\quad(2,2,4),
\]
and
\[
(1,1,6)\quad\text{versus}\quad(4,4).
\]

For the first pair,
\[
H_S(1,1,1,5)-H_S(2,2,4)
=
\frac18\log\left(\frac{4096}{3125}\right)>0,
\]
but
\[
H_B(1,1,1,5)-H_B(2,2,4)
=
\frac18\log\left(\frac45\right)<0.
\]

For the second pair,
\[
H_S(1,1,6)-H_S(4,4)
=
\frac18\log\left(\frac{1024}{729}\right)>0,
\]
but
\[
H_B(1,1,6)-H_B(4,4)
=
\frac18\log\left(\frac45\right)<0.
\]

Thus Shannon ranks the first profile in each pair as more diverse, while Brillouin ranks the second as more diverse.

## Assumptions and scope
Species labels are ignored, so abundance profiles are integer partitions of the census total.

All represented species have strictly positive integer abundance.

The result compares raw Shannon and Brillouin diversity, not normalized evenness variants.

The logarithm base is irrelevant to the ordering.

The theorem is a finite-census statement. Brillouin diversity is designed for finite counted collections, whereas Shannon's formula is commonly used as the corresponding large-sample information measure. The result does not claim that either index is universally preferable.

## Proof
At fixed total \(N\), Shannon diversity can be rewritten as
\[
H_S
=
\log N
-
\frac1N
\sum_i n_i\log n_i.
\]

Define
\[
Q(n)=\prod_i n_i^{n_i}.
\]

Then
\[
H_S=\log N-\frac1N\log Q(n),
\]
so Shannon diversity is strictly decreasing in the integer invariant \(Q(n)\).

For Brillouin diversity, define
\[
F(n)=\prod_i n_i!.
\]

Then
\[
H_B=\frac{\log(N!)-\log F(n)}{N},
\]
so at fixed \(N\), Brillouin diversity is strictly decreasing in the integer invariant \(F(n)\).

Consequently the two diversity indices have the same weak ranking on a profile pair exactly when \(Q\) and \(F\) have the same weak ordering.

Every unlabeled positive-integer abundance profile of total \(N\) is an integer partition of \(N\). The complete partition counts for \(N=1,\ldots,8\) are
\[
1,2,3,5,7,11,15,22.
\]

Exact comparison of every unordered profile pair gives no weak-order disagreement through \(N=6\).

At \(N=7\), the unique disagreement is
\[
(1,1,1,4)\quad\text{versus}\quad(2,2,3),
\]
for which
\[
Q=256<432,\qquad F=24=24.
\]

At \(N=8\), exactly two pairs have opposite strict orderings of \(Q\) and \(F\).

For
\[
(1,1,1,5)\quad\text{and}\quad(2,2,4),
\]
the invariants are
\[
Q=3125<4096,\qquad F=120>96.
\]

For
\[
(1,1,6)\quad\text{and}\quad(4,4),
\]
the invariants are
\[
Q=46656<65536,\qquad F=720>576.
\]

These are therefore exactly the first two strict Shannon–Brillouin ranking reversals.

## Verification
The embedded `verify_shannon_brillouin_boundary.py` uses only the Python standard library and exact integer arithmetic.

It independently generates every integer partition through \(N=8\) and cross-checks each profile count by a dynamic-programming partition-number calculation.

For every unordered profile pair it compares
\[
Q=\prod_i n_i^{n_i}
\]
with
\[
F=\prod_i n_i!.
\]

It verifies complete weak-order agreement through \(N=6\), the unique Brillouin tie split by Shannon at \(N=7\), and exactly two strict reversals at \(N=8\).

Run:

`python3 verify_shannon_brillouin_boundary.py`

The first output line must be `VERIFY_OK`.

No floating-point logarithm comparison is used.

## Relationship to prior work
Peet's ecological treatment writes both the Brillouin and Shannon formulas side by side, notes their different sample-size behavior, and explains that the Brillouin index approaches the Shannon index as sample size grows.

Palaghianu likewise treats Shannon and Brillouin as distinct ecological diversity indices. In the tested data, their numerical behavior is extremely highly correlated, and the Brillouin value is described as generally close to but lower than Shannon.

Those observations establish closeness and asymptotic relation, not ordinal identity. The present result isolates the exact smallest integer census at which the two formulas cease even to preserve strict diversity ranking, after first separating through a tie one individual earlier.

Targeted searches using both index names, rank-reversal terminology, integer abundance profiles, exact first-layer vectors, and multinomial formulations did not locate this sharp finite boundary.

## Limitations
The result concerns exact integer abundance profiles and exact index values.

It does not address sampling error, estimated population abundances, normalized evenness indices, or asymptotic rank disagreement probabilities.

The first strict reversals occur at very small census sizes. Their value is as exact boundary cases and reproducibility tests rather than as claims about typical large ecological surveys.

An unindexed teaching example or software regression test could contain one of the same profile pairs even though the sharp boundary was not located in the checked literature.

## References
1. R. K. Peet, “Relative Diversity Indices,” *Ecology* 56(2), 496–498, first published 1 March 1975. DOI: 10.2307/1934984.
2. C. Palaghianu, “A tool for computing diversity and consideration on differences between diversity indices,” *Journal of Landscape Management* 5(2), 78–82, 2014; public preprint deposited 12 February 2016, arXiv:1602.04005.
3. L. Brillouin, *Science and Information Theory*, Academic Press, 1956.

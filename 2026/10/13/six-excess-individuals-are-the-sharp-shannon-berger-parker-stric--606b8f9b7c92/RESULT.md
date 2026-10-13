# Six excess individuals are the sharp Shannon–Berger–Parker strict-ranking boundary
## Finding
Fix a species richness
\[
k\ge3,
\]
and let
\[
n_1,\ldots,n_k
\]
be strictly positive integer species abundances with
\[
N=\sum_i n_i.
\]

Write
\[
r=N-k
\]
for the number of individuals beyond the mandatory one individual per represented species.

Compare Hill diversity of order \(1\),
\[
{}^1D=\exp(H),
\qquad
H=-\sum_i p_i\log p_i,
\qquad
p_i=\frac{n_i}{N},
\]
with Hill diversity of order \(\infty\),
\[
{}^{\infty}D=\frac{1}{\max_i p_i}.
\]

The latter is the reciprocal Berger–Parker dominance index.

For every fixed
\[
k\ge3,
\]
the two indices induce exactly the same weak ordering whenever
\[
r\le3.
\]

At
\[
r=4,
\]
weak-order agreement first fails, but only through a tie. The profiles
\[
(1^{k-2},3,3)
\]
and
\[
(1^{k-3},2,2,3)
\]
have the same maximum abundance \(3\), so Berger–Parker ties them, while Shannon ranks the second profile as more diverse.

No opposite strict ranking occurs for
\[
r\le5.
\]

At
\[
r=6,
\]
strict reversal appears for the first time.

For
\[
k=3,
\]
the unique reversing pair is
\[
(1,4,4)
\quad\text{versus}\quad
(2,2,5).
\]

For every
\[
k\ge4,
\]
the complete first strict layer consists of exactly two pairs:
\[
(1^{k-2},4,4)
\quad\text{versus}\quad
(1^{k-3},2,2,5),
\]
and
\[
(1^{k-3},3,3,3)
\quad\text{versus}\quad
(1^{k-4},2,2,2,4).
\]

In the first family the profile with maximum abundance \(4\) has larger order-\(\infty\) diversity than the profile with maximum abundance \(5\), but the Shannon ranking is reversed.

The same happens in the second family, with maxima \(3\) and \(4\).

## Assumptions and scope
Species labels are ignored, so profiles are considered up to permutation.

Every represented species has positive integer abundance, and comparisons use a common richness \(k\) and common total \(N=k+r\).

The order-\(\infty\) Hill diversity is the reciprocal of Berger–Parker dominance. Using Berger–Parker dominance itself reverses the direction of that axis but describes the same strict disagreement.

The result is a finite-census resolution theorem. It does not claim an absolute biological threshold for arbitrary real-valued relative-abundance vectors.

## Proof
At fixed total
\[
N,
\]
Shannon entropy satisfies
\[
H
=
\log N
-
\frac1N\sum_i n_i\log n_i.
\]

Define
\[
Q(n)=\prod_i n_i^{n_i}.
\]

Then
\[
H
=
\log N
-
\frac1N\log Q(n).
\]

Thus order-\(1\) Hill diversity is strictly decreasing in the exact integer invariant
\[
Q(n).
\]

Order-\(\infty\) Hill diversity is
\[
{}^{\infty}D
=
\frac{N}{\max_i n_i},
\]
so at fixed \(N\) it is strictly decreasing in the maximum abundance.

For the first strict-reversal family,
\[
Q(1^{k-2},4,4)=4^8=65536,
\]
whereas
\[
Q(1^{k-3},2,2,5)=2^4 5^5=50000.
\]

Therefore
\[
{}^1D(1^{k-2},4,4)
<
{}^1D(1^{k-3},2,2,5),
\]
while
\[
{}^{\infty}D(1^{k-2},4,4)
>
{}^{\infty}D(1^{k-3},2,2,5).
\]

Equivalently, the Shannon-entropy gap is
\[
H(1^{k-3},2,2,5)-H(1^{k-2},4,4)
=
\frac1N\log\left(\frac{4096}{3125}\right)>0.
\]

For the second family,
\[
Q(1^{k-3},3,3,3)=3^9=19683,
\]
whereas
\[
Q(1^{k-4},2,2,2,4)=2^6 4^4=16384.
\]

Hence the profile with maximum abundance \(3\) has larger order-\(\infty\) diversity but smaller order-\(1\) diversity than the profile with maximum abundance \(4\).

It remains to prove sharpness for every richness.

Subtract one baseline individual from every species:
\[
y_i=n_i-1.
\]
Then
\[
y_i\ge0,
\qquad
\sum_i y_i=r.
\]

Ignoring zero entries, the excess vector is an integer partition of \(r\). Conversely every partition of \(r\) into at most \(k\) parts determines exactly one abundance profile after restoring the baseline ones.

For fixed \(r\), at most \(r\) excess coordinates are nonzero. Therefore once
\[
k\ge r,
\]
increasing \(k\) merely pads every profile with additional entries equal to \(1\). Such padding changes neither the maximum abundance nor \(Q\), because
\[
1^1=1.
\]

Thus the all-richness question for
\[
r\le6
\]
reduces to a finite set of excess partitions.

Exact enumeration gives no weak-order disagreement for
\[
r\le3,
\]
a unique tie split at
\[
r=4,
\]
no strict reversal for
\[
r\le5,
\]
and precisely the stated strict-reversal families at
\[
r=6.
\]

## Verification
The embedded `verify_shannon_berger_parker_boundary.py` uses only exact integer arithmetic.

It generates positive-integer abundance profiles directly and also reconstructs them independently from excess partitions.

For richness values
\[
3\le k\le12
\]
it checks every profile pair through excess
\[
r=6.
\]

It verifies the first weak disagreement at excess \(4\), absence of strict reversal through excess \(5\), and the complete first strict layer at excess \(6\).

It also checks the stabilization identity showing why the finite computation covers every
\[
k\ge3.
\]

Run:

`python3 verify_shannon_berger_parker_boundary.py`

The first output line must be `VERIFY_OK`.

No floating-point logarithm comparison is used.

## Relationship to prior work
Berger and Parker introduced their dominance measure in ecological species-abundance analysis. In modern Hill-number language, its reciprocal is the order-\(\infty\) diversity, which depends only on the most abundant species.

Shannon diversity is the order-\(1\) Hill diversity and depends on the complete abundance distribution.

Morris and coauthors analyze Shannon and Berger–Parker side by side, explicitly placing them at Hill orders \(1\) and \(\infty\). They emphasize that the indices weight abundance differently and that index choice can alter ecological interpretation.

A metagenomic diversity study likewise treats Shannon and Berger–Parker as distinct points of a Rényi/Hill diversity profile and directly compares sample rankings produced by the indices.

Those sources establish that the measures are not interchangeable. The result here is narrower and exact: for fixed richness and an integer census, it identifies the smallest excess abundance at which the order-\(1\) and order-\(\infty\) diversity rankings can strictly cross, and it classifies the entire first crossing layer for every richness.

Targeted searches using both index names, Hill orders \(1\) and \(\infty\), fixed richness, integer abundance, rank reversal, and the exact first-layer profiles did not locate this finite boundary.

## Limitations
The theorem fixes species richness and compares exact integer census profiles.

The excess threshold is not a scale-invariant statement about arbitrary real abundance vectors.

The original Berger–Parker article was verified bibliographically and by its abstract, but a complete lawful full text was not available through the checked route. Whole-document noncoverage is therefore not asserted for that source.

An unindexed ecological teaching example or software test could contain one of the small reversing profile pairs without identifying the universal excess-\(6\) minimality theorem.

## References
1. W. H. Berger and F. L. Parker, “Diversity of Planktonic Foraminifera in Deep-Sea Sediments,” *Science* 168(3937), 1345–1347, published 12 June 1970. DOI: 10.1126/science.168.3937.1345.
2. E. K. Morris et al., “Choosing and using diversity indices: insights for ecological applications from the German Biodiversity Exploratories,” *Ecology and Evolution* 4(18), 3514–3524, first published 28 August 2014. DOI: 10.1002/ece3.1155.
3. A. Carrigg et al., “Understanding microbial community diversity metrics derived from metagenomes: performance evaluation using simulated data sets,” *FEMS Microbiology Ecology* 82(1), 37–49, published 1 October 2012. DOI: 10.1111/j.1574-6941.2012.01405.x.

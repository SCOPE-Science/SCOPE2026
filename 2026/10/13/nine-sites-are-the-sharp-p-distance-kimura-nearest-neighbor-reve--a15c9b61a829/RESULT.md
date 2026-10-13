# Nine sites are the sharp p-distance–Kimura nearest-neighbor reversal boundary
## Finding
Consider ungapped, unambiguous aligned DNA sequence pairs of a common length
\[
L.
\]
Let
\[
t
\]
be the number of transition differences and
\[
v
\]
the number of transversion differences.

The uncorrected p-distance is
\[
p=\frac{t+v}{L}.
\]

The Kimura two-parameter distance is
\[
K=-\frac12\log\left(1-\frac{2t+v}{L}\right)-\frac14\log\left(1-\frac{2v}{L}\right).
\]
We restrict to its finite real domain
\[
2t+v<L,
\qquad
2v<L.
\]

No two admissible transition/transversion signatures receive opposite strict distance rankings from p-distance and K2P when
\[
L\le 8.
\]

Weak-order agreement first fails at
\[
L=3.
\]
A single transition and a single transversion both have p-distance
\[
\frac13,
\]
but their K2P distances differ.

Strict reversal appears for the first time at
\[
L=9.
\]
There is exactly one unordered reversing pair of count signatures:
\[
(t,v)=(2,3)
\quad\text{and}\quad
(t,v)=(4,0).
\]
Their p-distances satisfy
\[
\frac59>\frac49,
\]
so p-distance regards the four-transition sequence as nearer.

K2P gives the opposite ordering:
\[
K(2,3)=\frac14\log\left(\frac{243}{4}\right)
<
\log 3=K(4,0).
\]

Thus, against the common reference `AAAAAAAAA`, the sequence `GGCCCAAAA` is farther by p-distance but nearer by K2P than `GGGGAAAAA`.

## Assumptions and scope
Alignments have equal length, no gaps, and no ambiguous bases.

A transition is an adenine–guanine or cytosine–thymine substitution; every other nucleotide mismatch is a transversion.

The K2P formula is used only where both logarithm arguments are strictly positive. Signatures at or beyond the model-correction singularity are not assigned a finite real K2P distance.

The theorem compares exact pairwise distances from a common query or reference. It therefore gives a sharp finite boundary for a nearest-neighbor ordering reversal.

It is not a claim that nine-base sequences are useful barcodes, nor that the witness occurs in the low-divergence regime typical of many barcode-identification applications.

## Proof
Write
\[
P=\frac{t}{L},
\qquad
Q=\frac{v}{L}.
\]
Then
\[
K=-\frac12\log(1-2P-Q)-\frac14\log(1-2Q).
\]
Combining the logarithms gives
\[
K
=
-\frac14\log\left(\frac{(L-2t-v)^2(L-2v)}{L^3}\right).
\]
Define the exact positive integer
\[
F_L(t,v)=(L-2t-v)^2(L-2v).
\]
At fixed \(L\), K2P is strictly decreasing in \(F_L\), whereas p-distance is strictly increasing in the mismatch count
\[
t+v.
\]
Therefore two signatures give opposite strict rankings exactly when their mismatch-count difference and their \(F_L\)-difference have the same nonzero sign.

For
\[
L=9,
\]
the signatures
\[
(2,3)
\quad\text{and}\quad
(4,0)
\]
have mismatch counts \(5\) and \(4\), while
\[
F_9(2,3)=12
\quad\text{and}\quad
F_9(4,0)=9.
\]
Hence p-distance increases but K2P decreases from the second signature to the first.

The exact K2P values follow from
\[
\frac{F_9(2,3)}{9^3}=\frac{12}{729}=\frac4{243}
\]
and
\[
\frac{F_9(4,0)}{9^3}=\frac9{729}=\frac1{81}.
\]
Thus
\[
K(2,3)=\frac14\log\left(\frac{243}{4}\right)
<
\frac14\log(81)=\log 3=K(4,0).
\]

For the lower bound, enumerate every integer pair
\[
t,v\ge0,
\qquad
t+v\le L,
\qquad
2t+v<L,
\qquad
2v<L
\]
for each
\[
1\le L\le8.
\]
For every unordered pair, compare the integer mismatch counts and the integer values \(F_L\). No same-sign nonzero difference occurs, so no strict reversal occurs.

The same exhaustive calculation shows that at \(L=9\) the displayed pair is the only unordered strict reversal.

Every count signature is realizable relative to a common reference: choose distinct sites for the required transitions and transversions. The displayed strings provide an explicit simultaneous realization.

## Verification
The embedded `verify_k2p_pdistance_boundary.py` uses only the Python standard library and exact integer or rational arithmetic for all ordering decisions.

It enumerates every admissible transition/transversion signature for
\[
1\le L\le9
\]
and every unordered pair of signatures.

It verifies complete weak-order agreement through length \(2\), the first tie split at length \(3\), absence of strict reversal through length \(8\), and the unique strict pair at length \(9\).

It also checks the explicit common-reference sequences and the exact witness invariants
\[
F_9(2,3)=12,
\qquad
F_9(4,0)=9.
\]

Run:

`python3 verify_k2p_pdistance_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Kimura introduced the two-parameter correction by distinguishing transition and transversion substitutions in nucleotide-sequence comparisons.

DNA-barcoding literature has directly compared K2P with uncorrected p-distance. Srivathsan and Meier reported that uncorrected distances gave similar or higher identification success than K2P in their barcode data and questioned routine K2P use for closely related sequences.

Collins and coauthors likewise compared p-distance with K2P and more complex substitution models. Their specimen-identification procedure explicitly used nearest-neighbor distances, and they found that p-distance performed as well as or marginally better than the model-corrected alternatives in their tested data.

Those studies establish that the two distance choices are scientifically consequential and need not be treated as interchangeable. The result here is narrower and exact: it identifies the shortest admissible alignment at which the two formulas can strictly reverse a common-reference nearest-neighbor ordering, and it classifies the entire first reversal layer.

Targeted searches using both distance names, transition/transversion counts, nearest-neighbor ordering, exact witness counts, and shortest-alignment language did not locate this finite boundary.

## Limitations
The unique nine-site witness is highly divergent and lies near the K2P correction boundary. Collins and coauthors observed that p-distance and K2P scarcely differ in many low-divergence barcode comparisons, so this theorem should not be read as evidence that nearest-neighbor reversals are common in routine barcoding.

The theorem concerns the standard K2P closed-form distance and uncorrected p-distance only. Gaps, ambiguous bases, unequal site weights, rate heterogeneity, or other substitution models define different problems.

The foundational Kimura article was verified at month-level publication metadata rather than a day-resolved public date, so it is not used as the day-level metadata anchor.

An unindexed pedagogical example or software regression test could contain the same nine-site witness without identifying the sharp minimality statement.

## References
1. M. Kimura, “A simple method for estimating evolutionary rates of base substitutions through comparative studies of nucleotide sequences,” *Journal of Molecular Evolution* 16, 111–120, 1980. DOI: 10.1007/BF01731581.
2. A. Srivathsan and R. Meier, “On the inappropriate use of Kimura-2-parameter (K2P) divergences in the DNA-barcoding literature,” *Cladistics* 28(2), 190–194, first published 6 September 2011. DOI: 10.1111/j.1096-0031.2011.00370.x.
3. R. A. Collins, L. M. Boykin, R. H. Cruickshank, and K. F. Armstrong, “Barcoding's next top model: an evaluation of nucleotide substitution models for specimen identification,” *Methods in Ecology and Evolution* 3(3), 457–465, first published 23 January 2012. DOI: 10.1111/j.2041-210X.2011.00176.x.

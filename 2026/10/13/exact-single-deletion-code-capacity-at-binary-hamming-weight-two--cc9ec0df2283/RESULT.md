# Exact single-deletion code capacity at binary Hamming weight two

## Finding
For every integer \(n\geq 3\), the largest binary length-\(n\), constant-Hamming-weight-two code capable of correcting one arbitrary symbol deletion has exactly
\[
A^{\mathrm{del}}_2(n,2)=\left\lfloor\frac{3n-2}{4}\right\rfloor
=\left\lfloor\frac n2\right\rfloor+\left\lfloor\frac{n-1}{4}\right\rfloor
\]
codewords. Both an explicit optimal family and a two-output transversal giving a matching upper bound are provided for every \(n\).

## Assumptions and scope
Positions are numbered \(0,\ldots,n-1\). The word \(w_{a,b}\), for \(0\leq a<b<n\), has ones exactly at positions \(a,b\). For a binary word \(w\) of length \(n\), let \(D(w)\) be the **set of distinct** length-\(n-1\) words obtainable by deleting exactly one coordinate of \(w\), either zero or one. A code \(C\) corrects one deletion exactly when \(D(u)\cap D(v)=\varnothing\) for every distinct \(u,v\in C\). Repeated deletion positions producing the same output count only once.

The theorem optimizes cardinality among **all** such codes whose words have exactly two ones, with no linearity, cyclicity, balancedness, or other restrictions. It does not optimize unconstrained binary codes or codes correcting multiple deletions.

## Proof
**1. A lower-bound construction.** Form \(C_n\) from two disjoint families:
\[
\mathcal A_n=\{w_{2j,2j+1}: 2j+1<n\},\qquad
\mathcal B_n=\{w_{4j+1,4j+4}:4j+4<n\},\qquad
C_n=\mathcal A_n\cup\mathcal B_n.
\]
These contain respectively \(\lfloor n/2\rfloor\) and \(\lfloor(n-1)/4\rfloor\) words.

For an arbitrary input \(w_{a,b}\), deleting one of its two ones yields a weight-one output with its remaining one at index \(a\) or \(b-1\). The two indices coincide exactly when \(b=a+1\). Deleting a zero, when that location exists, yields a weight-two output with one-position pair among
\[
(a-1,b-1),\qquad (a,b-1),\qquad(a,b).
\]
The first requires a zero before position \(a\); the middle requires a zero strictly between \(a\) and \(b\); the last requires a zero after position \(b\).

Each \(\mathcal A_n\) word has a single distinct weight-one output, with its one at an even index. Its weight-two outputs always have adjacent ones. For \(w_{2j,2j+1}\), their possible starting indices are \(2j-1\) and \(2j\), so these output sets are mutually disjoint for different \(j\).

Each \(\mathcal B_n\) word has two distinct weight-one outputs, at indices \(4j+1\) and \(4j+3\); all are odd and distinct across the family, and avoid the weight-one outputs of \(\mathcal A_n\). Its weight-two outputs have one-position pairs among
\[
(4j,4j+3),\quad(4j+1,4j+3),\quad(4j+1,4j+4),
\]
subject to endpoint existence. Their one-position gaps are at least two, so they cannot coincide with the adjacent-one outputs from \(\mathcal A_n\). Their first-one positions lie in \(\{4j,4j+1\}\), disjoint for distinct \(j\). Hence all deletion-output sets of distinct codewords in \(C_n\) are disjoint, proving the constructive lower bound.

**2. A universal upper-bound transversal.** Let \(U_1\) consist of **all** length-\(n-1\) binary outputs of weight one, so \(|U_1|=n-1\). There are \(n-1\) possible adjacent-one input words \(w_{i,i+1}\), labeled by \(i=0,\ldots,n-2\). A length-\(n-1\) adjacent-one output whose pair starts at \(p\) can be produced from adjacent input \(i=p\) (by deleting a following zero) or \(i=p+1\) (by deleting a preceding zero); boundary cases are valid whenever those words exist. Therefore a minimum edge cover of the path on these \(n-1\) input labels gives a set \(U_2\) of exactly \(\lceil(n-1)/2\rceil\) such adjacent-one outputs, with at least one output from every adjacent input word.

Every nonadjacent input \(w_{a,b}\), where \(b\geq a+2\), has two **distinct** weight-one outputs in \(U_1\). Every adjacent input has one weight-one output in \(U_1\) and at least one weight-two output in \(U_2\). Consequently,
\[
\lvert D(w)\cap(U_1\cup U_2)\rvert\geq 2
\quad\text{for every weight-two input }w.
\]
If \(C\) corrects one deletion, its deletion-output sets are pairwise disjoint. Thus no member of \(U_1\cup U_2\) can be counted for two codewords, and
\[
2\lvert C\rvert\leq\lvert U_1\cup U_2\rvert
=n-1+\left\lceil\frac{n-1}{2}\right\rceil.
\]
Taking integer parts gives \(\lvert C\rvert\leq\lfloor(3n-2)/4\rfloor\), matching the construction for all \(n\geq3\). This completes the proof.

## Verification
The self-contained `verify.py` constructs \(C_n\), independently computes deletion-output sets directly from strings, and checks disjointness, cardinality, and the two-output covering inequality for the stated finite test ranges. The separate `verify.cpp` builds the complete confusability graph and enumerates maximal compatible codeword sets for lengths three through twelve, confirming their exact maximum sizes. These finite tests check implementation and boundary cases; the all-length conclusion follows from the preceding proof, not from finite extrapolation.

Run with Python 3: `python3 verify.py`. Optionally compile `verify.cpp` using `c++ -O2 -std=c++17 verify.cpp -o verify` and run `./verify`. Neither checker needs external packages.

## Relationship to prior work
Cullina, Kulkarni, and Kiyavash (arXiv:1211.4056) introduce the constant-weight deletion confusability graphs and prove optimal **chromatic numbers**, including the relevant weight-two layer. Their coloring statements do not determine its maximum independent-set cardinality: color classes need not be maximum independent sets. Kulkarni and Kiyavash (arXiv:1211.3128) establish general and constrained-source bounds using deletion-output hypergraph transversals; the constrained-source application examined there concerns run-length limitations. Their bounds do not give this sharp weight-two formula. The present result determines the exact maximum independent-set cardinality of the weight-two one-deletion graph and supplies a matching integral two-output cover for every length.

## Limitations
The theorem applies only to the binary constant-weight-two input layer and exactly one deletion. No assertion is made about all maximum-code classifications, robust synchronization, multiple deletion correction, or higher Hamming weights. Bibliographic searches cannot rule out an earlier unindexed equivalent formula. No independent external mathematical audit has been performed.

## References
1. D. Cullina, A. A. Kulkarni, and N. Kiyavash, “Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings,” arXiv:1211.4056 (first public preprint November 16, 2012). https://arxiv.org/abs/1211.4056
2. A. A. Kulkarni and N. Kiyavash, “Non-asymptotic Upper Bounds for Deletion Correcting Codes,” arXiv:1211.3128 (first public preprint November 13, 2012). https://arxiv.org/abs/1211.3128
3. D. Cullina, A. A. Kulkarni, and N. Kiyavash, “A Coloring Approach to Constructing Deletion Correcting Codes from Constant Weight Subgraphs,” IEEE ISIT (2012), DOI:10.1109/ISIT.2012.6284242.

# Complete covering-distance spectrum of a new binary length-22 code

## Finding

Let \(C\subseteq\{0,1\}^{22}\) be the explicit 84-word code constructed by Ota, Osa and Harada in their October 2026 article. Its 84 integer-encoded words are reproduced, with attribution, in `codewords.txt`. For each ambient word \(x\), put
\[
\delta(x,C)=\min_{c\in C}d_H(x,c),\qquad N_j=\#\{x\in\{0,1\}^{22}:\delta(x,C)=j\}.
\]
The exact complete distribution is:

| Distance \(j\) | Number \(N_j\) |
|---:|---:|
| 0 | 84 |
| 1 | 1848 |
| 2 | 19404 |
| 3 | 129360 |
| 4 | 614460 |
| 5 | 1712308 |
| 6 | 1566756 |
| 7 | 149908 |
| 8 | 176 |

All other \(N_j\) vanish. In particular, the covering radius is \(8\), exactly \(176\) ambient words attain that maximum, and the mean nearest-codeword distance for a uniformly random ambient word equals
\[
\frac{\sum_j jN_j}{2^{22}}=\frac{2737427}{524288}.
\]
The smallest integer-encoded ambient word at distance \(8\) is \(78501\).

## Assumptions and scope

The alphabet is binary, the block length is exactly \(22\), and Hamming distance is used. Integers in `codewords.txt` are interpreted as 22-bit binary words, with position zero the least significant bit. The underlying code is the specific published list, not an arbitrary optimal or linear code. The original work provides an 84-word code with minimum pairwise distance \(9\). Both the cardinality and minimum distance are also independently recomputed from the supplied list.

## Proof

For each integer \(x\) from \(0\) through \(2^{22}-1\), the file `verify.cpp` computes the exact distance
\[
\delta(x,C)=\min_{c\in C}\operatorname{popcount}(x\mathbin{\mathrm{xor}}c)
\]
by direct inspection of all \(84\) listed codewords. A fixed loop visits every one of the \(2^{22}\) ambient words exactly once, and increments exactly one distance bucket. Thus, unlike a partial sample, these exact integer counts exhaust the entire finite domain.

As an algorithmically independent cross-check, the same file performs multi-source breadth-first search in the 22-dimensional Hamming cube, starting at every codeword with distance zero and traversing all 22 one-bit-flip edges from each visited vertex. Every edge changes one bit, so shortest-path distance to the source set equals Hamming distance to the code. The FIFO search visits exactly \(2^{22}\) different vertices, yielding the same bucket counts as direct enumeration. The verifier checks agreement at all \(23\) possible distances, including zeros beyond \(8\).

In both computations the counts sum exactly to \(4194304=2^{22}\), the distance-weighted sum is \(21899416\), and the maximum occupied bucket is \(8\), containing \(176\) elements. The checks of 84 distinct codewords, their admissible range and minimum pairwise distance \(9\) ensure the experiment uses the stated source code. Therefore all asserted finite quantities follow exactly, without inference from numerical approximation.

## Verification

With a C++17 compiler, run from the directory containing both embedded files:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify codewords.txt
```

The program outputs `VERIFY_OK`, the exact nine buckets, `TOTAL 4194304`, `FIRST_DEEP 78501`, and the unreduced mean numerator and denominator. The two methods use distinct traversals: direct all-word minimum Hamming distances and a full breadth-first search of the cube. No external library or downloadable source file is needed to replay this embedded certificate.

## Relationship to prior work

Ota, Osa and Harada, *Three Improved Lower Bounds for Binary Error-Correcting Codes*, arXiv:2610.11609v1 (first posted October 8, 2026), give the 84-word \((22,84,9)\) construction and its minimum-distance role in lower bounds for \(A_2(22,9)\). Their displayed article and supporting list do not report the all-ambient covering-distance distribution or the count of deepest holes. The published codewords are therefore an input, not claimed as a new construction. Code cardinality and minimum distance alone do not mathematically imply this covering-distance spectrum for a particular code. The new contribution is the exhaustive covering-profile determination for that input.

## Limitations

This result does not establish that covering radius \(8\) is optimal among binary length-22 codes of size \(84\) or distance \(9\); nor does it give an asymptotic family or a complete decoding algorithm beyond the nearest-distance statistic. The certificate is exhaustive only because the fixed ambient domain has \(2^{22}\) words. Independent mathematical audit is not yet performed, and previously unindexed equal calculations remain a priority risk.

## References

1. Ota, Osa and Harada, *Three Improved Lower Bounds for Binary Error-Correcting Codes*, arXiv:2610.11609v1, https://arxiv.org/abs/2610.11609 (first public October 8, 2026).
2. The authors' 84-codeword ancillary list, https://arxiv.org/src/2610.11609v1/anc/code_22_84_9.txt (reproduced in `codewords.txt`).

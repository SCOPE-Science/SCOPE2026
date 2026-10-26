# Exact two-read single-deletion capacity in the binary weight-two layer

## Finding

Let \(D_1(w)\) denote the set of distinct length-\(n-1\) words obtainable by deleting exactly one symbol from a binary word \(w\) of length \(n\). A *two-read reconstruction code* is a set \(C\) such that
\[
|D_1(u)\cap D_1(v)|\le1\qquad(u,v\in C,\ u\ne v).
\]
For every integer \(n\ge2\), the maximum cardinality of a two-read reconstruction code contained in the Hamming-weight-two layer is
\[
R_2(n)=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]
An optimum contains exactly those words whose two one-positions \(0\le i<j<n\) have an odd difference \(j-i\).

## Assumptions and scope

The alphabet is \(\{0,1\}\), words have exactly two ones, and coordinates are numbered from zero. Two distinct channel reads are required to identify a codeword uniquely; consequently two codewords may share one deletion descendant but not two. An outcome is counted once even if several deletion positions produce it. The theorem covers every \(n\ge2\), without assumptions on run lengths or coding linearity. For \(n=2\), the single weight-two word gives size one, consistent with the formula.

## Proof

Identify a weight-two word with its one-positions \((i,j)\), where \(0\le i<j<n\). For every fixed \(i\) and each \(i+1\le j\le n-2\), the two words \((i,j)\) and \((i,j+1)\) have two *distinct* common descendants. Deleting the rightmost one from each produces the same word having its lone one at position \(i\). Furthermore, the weight-two word having ones at \((i,j)\) is a descendant of \((i,j)\) by deleting a zero to the right of \(j\), and a descendant of \((i,j+1)\) by deleting the zero at position \(j\). Hence the allowed second-one positions for any fixed first-one position form an independent set in a path on \(n-i-1\) vertices. At most \(\lceil(n-i-1)/2\rceil\) can be selected. Summing over \(0\le i<n-1\) yields
\[
|C|\le\sum_{i=0}^{n-2}\left\lceil\frac{n-i-1}{2}\right\rceil
=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]

Now select every pair \((i,j)\) for which \(j-i\) is odd. This selects \(\sum_i\lceil(n-i-1)/2\rceil\) words, so only the two-read condition remains to be proved. For an odd-gap pair \((i,j)\), its weight-one descendants have the one at \(i\) or \(j-1\); both positions have parity equal to that of \(i\). Its weight-two descendants (when the relevant zero-deletion locations exist) have one-position pairs among
\[
(i-1,j-1),\quad(i,j-1),\quad(i,j).
\]
Their ordered parity patterns are, respectively, \((1-p,p)\), \((p,p)\), and \((p,1-p)\), where \(p=i\bmod2\).

Take two *distinct* selected pairs \((i,j)\) and \((i',j')\). If \(i\) and \(i'\) have the same parity, each of the three parity patterns is distinct, so a common weight-two descendant would have to arise in the same position of the displayed triple on both sides. Equality in any one of those three positions implies \((i,j)=(i',j')\), a contradiction. Therefore the pair has no common weight-two descendant. Its weight-one descendant sets have at most one common element: each is the ordered set of endpoints \(\{i,j-1\}\) (possibly a singleton when \(j=i+1\)), which determines the pair uniquely whenever both elements occur.

If \(i\) and \(i'\) have opposite parity, their sets of weight-one descendants are disjoint. For the weight-two descendants, the parity patterns on the two sides can agree only between the first pattern on one side and the third on the other (the equal-parity middle pattern cannot agree). Both orientations cannot simultaneously give equality, since they would require both \(i'=i-1\) and \(i'=i+1\). Thus at most one weight-two descendant is common. In either parity case the intersection of full deletion-descendant sets has size at most one. The proposed family is therefore two-read reconstructible and meets the upper bound. \(\square\)

## Verification

The accompanying `verification.py` computes all distinct one-deletion outputs and checks the proposed family and every adjacent-second-position obstruction for all lengths \(2\le n\le18\). These checks are finite consistency tests; the universal assertion is established by the proof above.

## Relationship to prior work

The single-deletion coding literature develops deletion-descendant graphs, constant-weight restrictions, and optimal colorings for *one-read* unique deletion correction. Two-read reconstruction weakens disjointness to at most one shared descendant. The present result computes the exact capacity on the natural two-one slice, rather than giving a coloring, a bound for the unrestricted binary space, or an edge count for the entire reconstruction graph. The older foundational reconstruction work explains the model but was not available in complete full text for a decisive all-theorems comparison.

## Limitations

This result does not determine two-read capacities of other constant-weight layers or of the unrestricted binary space, and it does not classify all maximum codebooks. It assumes two distinct deletion outputs, not two independent observations that may coincide. The computation tests finite lengths only and is not an infinite certificate. Historical-priority assessment is limited to inspected literature and records; the full text of the foundational 2001 work was not examined.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197v1, 22 July 2002 (sections 1, 2, and 6).
2. D. Cullina, A. A. Kulkarni, and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056v1, 16 November 2012.
3. V. I. Levenshtein, *Efficient reconstruction of sequences*, IEEE Transactions on Information Theory 47 (2001), 2–22, DOI: 10.1109/18.904499.

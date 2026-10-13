# Exact single-deletion capacity on the binary length-\(15\), weight-\(3\) layer

## Finding

Let \(\mathcal B=\{x\in\{0,1\}^{15}:\operatorname{wt}(x)=3\}\). For each \(x\in\mathcal B\), let \(D(x)\) be the **set of distinct length-\(14\) strings** obtained by deleting exactly one bit. A one-deletion-correcting code is a subset \(C\subseteq\mathcal B\) for which \(D(x)\cap D(z)=\varnothing\) whenever \(x,z\in C\) are distinct. Then

\[
\max_{C\subseteq\mathcal B\,:\,D(x)\cap D(z)=\varnothing\;\forall x\ne z\in C}|C|=37.
\]

An explicit attaining code of \(37\) words is supplied in `code_triples.csv`; each row gives the three one-based positions of its ones, with all other positions zero. A standard-library exact checker is supplied in `verify.py`.

## Assumptions and scope

All codewords are **ordered binary strings**, not subsets considered up to permutations. One adversarial deletion may remove either a zero or a one. Deleting equal symbols at different positions can give the same received string, so \(D(x)\) is a set rather than a multiset. The receiver knows the original block length and that exactly one bit was deleted. Optimality is asserted only at length \(15\) and composition \(3\) ones.

## Proof

**Upper bound.** Assign nonnegative weights \(q(y)\) to length-\(14\) binary strings \(y\). If \(y\) has exactly two ones, assign \(2/3\) when they are adjacent and \(1/3\) otherwise. If \(y\) has exactly three ones, assign \(1/3\) precisely when they are consecutive and the first one is at a position in \(S=\{1,3,5,7,9,11,12\}\). Assign zero in every other case. Positions are one-based.

We show that, for every \(x\in\mathcal B\),
\[
\sum_{y\in D(x)}q(y)\ge 1.
\]

There are three cases according to the number of consecutive-one runs in \(x\).

* If \(x\) has three singleton runs, delete each of the three ones in turn. The three resulting length-\(14\), weight-\(2\) words are distinct. Each has weight at least \(1/3\).
* If \(x\) has two runs, one consists of two adjacent ones and one of an isolated one. Deleting the isolated one produces a weight-\(2\) word with adjacent ones, hence weight \(2/3\). Deleting either one from the adjacent pair produces a **different** weight-\(2\) word of weight at least \(1/3\).
* If all three ones of \(x\) form a single run beginning at \(i\in\{1,\ldots,13\}\), deleting any of the three ones produces a weight-\(2\) word whose ones are adjacent and therefore has weight \(2/3\). Deleting an adjacent zero on one side of the run leaves a three-one run starting at either \(i-1\) or \(i\) in the length-\(14\) result (at a boundary only one of these is possible). The set \(S\) meets those permitted positions for every \(i\in\{1,\ldots,13\}\). Such a received word has weight \(1/3\) and differs from the weight-\(2\) output.

The total weight of *all* length-\(14\) outputs is
\[
\sum_y q(y)=\frac{\binom{14}{2}-13}{3}+\frac{2\cdot13}{3}+\frac{7}{3}=\frac{78+26+7}{3}=37.
\]
Indeed, \(13\) pairs of positions are adjacent, \(78\) are nonadjacent, and exactly \(7\) consecutive-three patterns receive positive weight. Because the deletion sets of distinct codewords are disjoint, summing the displayed local inequality over \(x\in C\) yields \(|C|\le\sum_yq(y)=37\).

**Attainment.** The attached CSV specifies \(37\) distinct triples of one-based positions between \(1\) and \(15\). The checker `verify.py` constructs the binary words, computes all distinct one-deletion outputs two different ways (direct string removal and coordinate-adjusted one-positions), checks that these representations agree for all \(\binom{15}{3}=455\) possible inputs, and verifies that the outputs from the \(37\) listed words are pairwise disjoint. This is a finite complete check of the explicit construction, not a claim based on partial sampling. It proves \(|C|\ge37\), matching the upper bound.

## Verification

Place `verify.py` and `code_triples.csv` in the same directory. Execute `python3 verify.py`. It uses only Python's standard library and checks all \(455\) possible length-\(15\), weight-\(3\) inputs for the fractional bound, both deletion-output representations, the codeword list, the pairwise disjointness of its deletion outputs, and the exact total dual weight \(37\). The expected output begins `VERIFY_OK N=15 W=3 candidates=455 selected=37 dual_weight=37`. It also verifies the familiar modified-VT checksum partition on this layer: the sum of the three one-based positions modulo \(13\) yields exactly \(35\) words in each of the \(13\) classes.

## Relationship to prior work

Cullina, Kulkarni, and Kiyavash [1,2] formulate constant-weight deletion-code graphs and prove an **optimal chromatic-number** formula, using the modified Varshamov--Tenengolts coloring. An optimal coloring does not generally establish the size of a maximum independent set. For this specific graph their \(13\) checksum classes each have \(35\) words, while the explicit \(37\)-word code and its matching upper certificate establish the exact independence number.

Kulkarni and Kiyavash [3] develop the general fractional-transversal framework for deletion-code upper bounds, including constrained sources; the specialized exact fractional cover and matching construction above are the distinguishing content here. Sloane [4] gives background on single-deletion independent-set problems. The authors of these earlier works are not credited with this exact claim unless an equivalent result is located independently.

## Limitations

The claim is only about **one deletion**, **binary alphabet**, **length \(15\)** and **weight \(3\)**. It gives no error guarantee for two deletions or substitutions, no decoding-time bound, and no assertion about sizes at other lengths or weights. The code is an explicit finite list, not an algebraic construction for arbitrary length. An earlier unindexed numerical classification remains possible, and the historical literature has not been exhaustively bibliographically cleared.

## References

[1] D. Cullina, A. A. Kulkarni, N. Kiyavash, *A Coloring Approach to Constructing Deletion Correcting Codes from Constant Weight Subgraphs*, IEEE ISIT (2012), `https://www.sc.iitb.ac.in/~ankur/docs/isit-weight-final.pdf`.

[2] D. Cullina, A. A. Kulkarni, N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056 (first version 2012-11-16), `https://arxiv.org/abs/1211.4056`.

[3] A. A. Kulkarni, N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128 (first version 2012-11-13), `https://arxiv.org/abs/1211.3128`.

[4] N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197 (2002), `https://arxiv.org/abs/math/0207197`.

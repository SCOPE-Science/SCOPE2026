# Oddtown families of two-bounded multisets: the first excess and a six-coordinate amplifier

## Finding

Let \(O_2(n)\) be the maximum size of a family \(\mathcal F\subseteq\{0,1,2\}^n\) such that every vector has odd coordinate sum and every two **distinct** vectors have even multiset-intersection size, with
\[
I(x,y)=\sum_{i=1}^n\min\{x_i,y_i\}.
\]
Then the following statements hold.

1. The complete initial extremal profile is
   \[
   (O_2(1),O_2(2),O_2(3),O_2(4),O_2(5))=(1,2,3,6,7).
   \]
   Thus four coordinates give the first strict excess over the classical Oddtown bound \(n\).
2. For every integer \(n\ge1\), writing \(n=6q+r\), with \(q\ge0\) and \(0\le r<6\),
   \[
   10q+r\le O_2(n)\le 2n.
   \]
   In particular \(\liminf_{n\to\infty} O_2(n)/n\ge5/3\).

The following ten words form the six-coordinate amplifier (one digit is one multiplicity; commas separate words):

```text
000111  001011  002120  011201  101201
111220  112210  121102  211102  221101
```

## Assumptions and scope

Multisets have ground set \([n]\) and multiplicity at most two. Total cardinality is the **sum of multiplicities**, not support size. Intersection cardinality is the **sum of coordinatewise minima**, not a dot product of multiplicity vectors and not intersection of their supports. The odd condition applies to each member, and the even condition only to distinct members. The exact determination is restricted to \(1\le n\le5\); the other statements are bounds for arbitrary \(n\).

## Proof

**Initial-segment encoding and universal upper bound.** Encode \(x\in\{0,1,2\}^n\) as the subset
\[
\Phi(x)=\{(i,j):1\le i\le n,\ 1\le j\le x_i\}\subseteq[n]\times[2].
\]
The map is injective and preserves both cardinalities and intersections:
\[
|\Phi(x)|=\sum_i x_i,\qquad
|\Phi(x)\cap\Phi(y)|=\sum_i\min\{x_i,y_i\}.
\]
For any admissible family, the binary incidence vectors of its encoded sets have odd self-inner-product and zero mutual inner-products over \(\mathbb F_2\). Taking the inner product of a putative linear dependence with each incidence vector in turn shows that every coefficient is zero. Hence there are at most \(2n\) such vectors. This is the standard Oddtown argument after encoding and is not claimed as an original bound.

**Ten-element amplifier.** The displayed ten words are all pairwise distinct and have odd coordinate sum. For any pair of different displayed words, the six-term sum of their coordinatewise minima is even. This is a finite claim checked directly by all \(45\) pairs in `verify.py` (with an independent initial-segment-bitmask comparison). Therefore these words form an admissible family on six coordinates. Place independent zero-padded copies of this family on \(q\) disjoint blocks of six coordinates. Add the \(r\) singleton vectors on the remaining coordinates. Every word is odd; two words from different blocks have intersection size zero. The resulting family has \(10q+r\) distinct words, proving the lower bound at all orders. Dividing by \(n=6q+r\) yields the asserted lower limiting density.

**Exact small-order certificate.** For each \(1\le n\le5\), construct all odd-weight vectors in \(\{0,1,2\}^n\) in lexicographic order. Their number is \((3^n-1)/2\): for one coordinate, the signed even-minus-odd count is \(1-1+1=1\), and multiplication over coordinates preserves this difference. Two candidate vertices are adjacent precisely when their multiset-intersection sum is even. Thus admissible families are exactly the cliques of this finite graph.

To certify exhaustion, use the following recurrence. Let `C` be an increasing-index list of possible next vertices and let `A[j]` contain **only** neighbours of vertex `j` having greater index. Start with all candidate vertices. Every recursive call replaces `C` by the intersection of the candidates **after** the chosen vertex with `A[j]`. All unordered cliques are visited in exactly one increasing-index sequence. Therefore a zero count at depth \(k\) proves that no admissible family of size \(k\) exists; a positive count at depth \(k-1\) witnesses the attained maximum when the counts stop there. The exact integer counts of cliques of sizes zero through the first forbidden size are:

```text
n=1: [1, 1, 0]
n=2: [1, 4, 2, 0]
n=3: [1, 13, 30, 14, 0]
n=4: [1, 40, 332, 744, 450, 72, 8, 0]
n=5: [1, 121, 3300, 27020, 73200, 68874, 24640, 3040, 0]
```

The last zero in each row, together with the preceding positive count, proves the exact profile. The traversal and predicate appear in the included executable `verify.py` and do not use randomized or heuristic pruning. As explicit attained witnesses, order-four has the six words `0012,0102,1002,1121,1211,2111`, while order-five has `00001,00120,01020,10020,11210,12110,21110`. Each listed collection passes the defining parity conditions. The executable also compares every compatibility decision for \(n\le5\) with a separate two-bit-per-coordinate representation to catch any discrepancy in the min-intersection predicate.

## Verification

Run `python3 verify.py` using Python 3 and no third-party packages. The included `verification_output.txt` records the exhaustive clique counts, a check of all 45 pair intersections in the amplifier, independent bitmask checks for every candidate pair through \(n=5\), and tests of the disjoint-support construction at all orders \(1\le n\le48\). Exact arithmetic uses integers and bitsets. The infinite encoding argument and block construction are mathematical proofs rather than consequences of finite tests.

## Relationship to prior work

Zou's 2026 work [1] studies Oddtown-type congruences for **ordinary subsets** of an \(n\)-point ground set and establishes the \(n\)-element upper bound in the off-diagonal case. Applying this to the initial-segment representation yields the known \(2n\) upper bound here, but not the 10-word amplifier, the first strict excess over \(n\), or the 2-bounded exact initial profile. Shankar's 2026 path analogue [2] instead uses common edges of North-East lattice paths; the corresponding objects and intersection operation are different. Berlekamp's classical Oddtown theorem [3] provides the linear-independence step, not the multiset constructions.

A later paper by Banerjee and Dewan [4] treats the **even-cardinality** Eventown problem for bounded multisets and explicitly uses the coordinatewise-minimum intersection. Its theorem has different self-parity and does not imply the odd-family conclusions here. The result is a concrete lower-bound construction and exact finite cutoff, not an assertion of an optimal asymptotic constant or of a general exact formula.

## Limitations

The exact values for \(n\ge6\), including whether \(O_2(6)=10\), are **not** determined. The upper and lower slopes remain separated. The small-order exact profile relies on an exhaustively specified finite graph and a reproducible exact clique enumeration; no purely symbolic classification of all extremal families is claimed. No independent audit or definitive bibliographic-priority certification has been performed. An earlier equivalent result in a different formulation of constrained set-system Oddtown remains a residual risk.

## References

1. H. Zou, *On the maximum size of (a,b)-town (mod k) families*, arXiv:2606.03613, initially public 2026-06-02, https://arxiv.org/abs/2606.03613.
2. U. Shankar, *Oddtown and eventown theorems for lattice paths*, arXiv:2607.23117, initially public 2026-07-25, https://arxiv.org/abs/2607.23117.
3. E. R. Berlekamp, *On subsets with intersections of even cardinality*, Canadian Mathematical Bulletin 12 (1969), 471–474.
4. A. Banerjee and A. Dewan, *An Eventown Result for Multisets*, arXiv:2610.21636, initially public 2026-10-15, https://arxiv.org/abs/2610.21636 (comparison only, not the source-period anchor).

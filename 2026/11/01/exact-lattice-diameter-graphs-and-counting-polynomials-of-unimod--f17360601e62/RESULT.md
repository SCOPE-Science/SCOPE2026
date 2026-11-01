# Exact lattice-diameter graphs and counting polynomials of unimodular boxes

## Finding

Let \(d\geq 1\), let \(a_1,\ldots,a_d\) be positive integers, let \(U\in\mathrm{GL}_d(\mathbb Z)\), and let \(z\in\mathbb Z^d\). For every positive integer \(t\), consider the lattice-point set
\[
S_t=t\left(z+U\prod_{i=1}^{d}[0,a_i]\right)\cap\mathbb Z^d.
\]
Write \(a=\max_i a_i\), \(I=\{i:a_i=a\}\), \(k=|I|\), \(L=ta\), and
\[
B=\prod_{i\notin I}(ta_i+1),
\]
with the empty product equal to one. The *lattice diameter* is the largest number of unit lattice steps in a segment joining two points of \(S_t\), or equivalently \(\max_{x,y\in S_t}\gcd(y_1-x_1,\ldots,y_d-x_d)\). The *lattice Borsuk graph* has vertex set \(S_t\), and an edge joins distinct points precisely when their lattice segment has maximal lattice diameter.

**Complete component theorem.** The lattice diameter is \(L\). The Borsuk graph is a disjoint union of complete graphs, with exactly
\[
N_s(t)=B\binom{k}{s}(L-1)^{k-s}
\]
components isomorphic to \(K_{2^s}\) for each \(0\le s\le k\). Here \(0^0=1\), and a term with zero multiplicity is absent. In particular, the graph's largest clique is \(K_{2^k}\).

Consequently the exact number of distinct lattice-diameter segments (equivalently, lattice-diameter lines) is
\[
\boxed{\operatorname{LD}_{P}(t)
=\frac{B}{2}\big[(L+3)^k-(L+1)^k\big].}
\]
The segment count is an integer-valued polynomial of degree exactly \(d-1\) in \(t\), with leading coefficient \(k\prod_{i=1}^d a_i/a\). There are precisely \((3^k-1)/2\) unoriented diameter directions. The discrete lattice Borsuk partition number is exactly
\[
\boxed{\beta_{\mathbb Z}(S_t)=2^k.}
\]
More generally, for every positive integer \(q\), the number of proper colorings with \(q\) labeled colors is given by the chromatic polynomial
\[
\boxed{\chi_{S_t}(q)
=\prod_{s=0}^{k}\left[(q)_{2^s}\right]^{B\binom{k}{s}(L-1)^{k-s}},}
\]
where \((q)_m=q(q-1)\cdots(q-m+1)\). Thus every term in the lattice-diameter graph's clique spectrum, segment-counting function, coloring polynomial, and minimal partition size is explicit, in arbitrary dimension and at *every* integer dilation, without quasipolynomial exceptions.

The number \(k\) of longest integer edge directions produces a sharp partition transition: if one edge becomes strictly longer than all others, the partition number becomes two; if exactly \(k\) edges tie for the longest, it is \(2^k\), irrespective of all shorter integer lengths.

## Assumptions and scope

All \(a_i\) and \(t\) are positive integers, \(U\) is an integer matrix with determinant \(\pm 1\), and \(z\) is integral. A lattice diameter of \(L\) means a segment with exactly \(L+1\) lattice points. The lattice Borsuk partition number is defined by partitions into parts of strictly smaller lattice diameter. Both the affine unimodular map and its inverse preserve lattice points, collinearity, greatest common divisors of coordinate differences, and adjacency in the diameter graph. It suffices to prove the theorem for the integer box \(S=\prod_i\{0,\ldots,ta_i\}\).

The formulas do not cover non-unimodular integer shears, rational vertices with nonintegral dilations, or arbitrary lattice polytopes. There is no asymptotic limiting hypothesis.

## Proof

**1. Sharp diameter and directions.** For any two different integer points \(x,y\) in the box, let \(g=\gcd(y_1-x_1,\ldots,y_d-x_d)\). The absolute coordinate differences do not exceed \(ta_i\le L\), so \(g\le L\). Along any longest coordinate edge there are \(L+1\) lattice points, proving equality. For \(g=L\), each coordinate difference is an integer multiple of \(L\). A shorter-side coordinate has \(|y_i-x_i|\le ta_i<L\) and hence must agree. In each longest-side coordinate, the difference is one of \(-L,0,L\). At least one longest coordinate differs. Conversely, every such nonzero difference vector has greatest common divisor \(L\). Every nonzero signed ternary vector on \(k\) coordinates is realized, with opposite signs describing the same unoriented direction. Hence the direction count is \((3^k-1)/2\).

**2. Complete component classification.** Fix the values of all shorter coordinates. For the longest coordinates of a point \(x\), let \(J\subseteq I\) be exactly those whose value is an endpoint \(0\) or \(L\). Fix all remaining longest coordinates at their actual interior values in \(\{1,\ldots,L-1\}\). By Step 1 every diameter-neighbor has exactly the same frozen coordinates and endpoint-index set \(J\), and may differ only by independently exchanging \(0\) and \(L\) on at least one coordinate of \(J\). Conversely, *every two distinct* endpoint assignments on the same \(J\) are joined by an edge, since their difference has gcd \(L\). They form a full clique of order \(2^{|J|}\), with no edge leaving it. Thus the connected components are exactly the cliques specified by these frozen data.

For \(|J|=s\), choose the \(s\) endpoint coordinate positions in \(\binom{k}{s}\) ways; there are \((L-1)^{k-s}\) assignments of interior values and \(B\) assignments of shorter coordinates. This proves the asserted multiplicity \(N_s(t)\). The largest component has \(2^k\) vertices because \(s=k\) occurs with multiplicity \(B>0\). The vertex count is consistent:
\[
\sum_{s=0}^{k}2^sN_s(t)=B(L+1)^k=|S_t|.
\]

**3. Counting segments and lines.** In this graph, an edge is by definition precisely a diameter segment, so the number of diameter segments is
\[
\begin{aligned}
\sum_{s=0}^{k}N_s(t)\binom{2^s}{2}
&=\frac B2\sum_{s=0}^k\binom ks(L-1)^{k-s}(4^s-2^s)\\
&=\frac B2\big[(L+3)^k-(L+1)^k\big].
\end{aligned}
\]
A line through two vertices of an axis-aligned binary cube contains no third distinct binary-cube vertex: if three points were collinear, choose a coordinate in which the first two differ, and the third could only have the first or the second endpoint parameter. This also applies to each clique above. Thus distinct diameter segments cannot occupy the same diameter line. This verifies equality of the line and segment counts. The polynomial degree and its leading coefficient follow by taking the first binomial difference, \((L+3)^k-(L+1)^k=2kL^{k-1}+O(L^{k-2})\) for \(k\ge2\), with the \(k=1\) case immediate; multiplying by \(B\) gives \(k\prod_i a_i/a\) as the coefficient of \(t^{d-1}\).

**4. Partitions and all color counts.** A partition into subsets of strictly smaller lattice diameter is exactly a proper vertex coloring of the diameter graph. Every complete component of size \(2^s\) admits \((q)_{2^s}\) labeled proper \(q\)-colorings; choices across disjoint components are independent. Multiplying with the multiplicities just proved yields the chromatic polynomial. The minimum number of colors equals the maximum component order \(2^k\), proving the exact Borsuk number. This proves all conclusions.

## Verification

A standalone standard-library Python program, `verify.py`, is provided. Invoke `python3 verify.py`. It independently enumerates all lattice-point pairs, computes coordinate-difference gcds without using the claimed adjacency characterization, finds the actual maximum and all maximizing pairs, constructs connected components by graph traversal, verifies each is complete, and compares the diameter, number of segments, complete-component multiplicities, largest clique, and number of directions with the formulas.

The program passed 207 distinct finite test instances: all axis boxes with \(1\le d\le4\), integer sides from \(1\) through \(3\), with dilations \(t=1\) (and \(t=2\) when \(d\le3\)), plus independent test cases under integral unimodular shears and reflections in dimensions two and three. For example, a three-dimensional cube of side \(4\) has clique multiplicities \(27,27,9,1\) for clique orders \(1,2,4,8\), respectively, and has \(109\) diameter segments.

The computer checks are finite corroboration. The proof above, not enumeration, establishes every dimension, side-length vector, and dilation.

## Relationship to prior work

Averkov, Brose, De Loera, Lopez-Campos and Torres, *On Lattice Diameter Segments: Algorithms and Structure* (arXiv:2508.20009), establish the general eventual quasipolynomial nature of lattice-diameter-segment counts for lattice polytopes, and a universal \(2^d\) discrete Borsuk bound. Their general clique-structure argument and the fact that a cube attains the universal bound are prior results; neither is claimed as new here. Their Example 4.7 explicitly exhibits a nontrivial period-three quasipolynomial for a skew lattice parallelogram.

The present theorem instead gives the *full explicit component-size multiplicities*, complete coloring polynomial, and an exact all-dilation **polynomial** for the canonical family of unimodular boxes, with a dimension-sensitive \(2^k\) optimal partition number. The formulas are not obtained merely by substituting a box into the published general theorem: they follow from an exact coordinatewise equality classification. An equivalent specialized box enumeration could nevertheless exist in earlier combinatorial or lattice-point literature; historical priority is not independently certified.

## Limitations

Only affine unimodular images of integral axis boxes are classified. Other lattice parallelepipeds may exhibit genuinely quasipolynomial behavior, and the theorem does not settle the general quasi-polynomial period, degree, or direction-count problems. The published universal upper bound and its cube sharpness are background, not new contributions. The verifier is an implementation check rather than independent mathematical validation.

## References

1. G. Averkov, A. E. Brose, J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On Lattice Diameter Segments: Algorithms and Structure*, arXiv:2508.20009, first public version 27 August 2025; version 2, 3 October 2026. https://arxiv.org/abs/2508.20009
2. S. Rabinowitz, *A theorem about collinear lattice points*, Utilitas Mathematica **36** (1989), 93–95 (as cited and used for context in Reference 1).

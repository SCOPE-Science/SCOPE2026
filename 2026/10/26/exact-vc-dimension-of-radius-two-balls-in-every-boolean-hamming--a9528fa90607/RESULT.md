# Exact VC dimension of radius-two balls in every Boolean Hamming cube

## Finding

Let \(d\geq1\), let \(Q_d=\{0,1\}^d\), and let \(\operatorname{dist}_H\) be Hamming distance. Consider the range family consisting of **all closed balls of the fixed radius two**, with centers restricted to vertices of the same cube:
\[
\mathcal B_{d,2}=\{B_2(c):c\in Q_d\},\qquad B_2(c)=\{x\in Q_d:\operatorname{dist}_H(x,c)\leq2\}.
\]
Its exact Vapnik--Chervonenkis dimension is
\[
\boxed{\operatorname{VCdim}(Q_d,\mathcal B_{d,2})=\begin{cases}
0,&d\leq2,\\
1,&d=3,\\
3,&d=4,\\
4,&d\geq5.
\end{cases}}
\]
Here a finite point set is shattered if its intersections with the specified balls realize every subset. The radius is fixed at two; the family is **not** the union of balls of different radii. Equivalently, this is the closed-neighborhood VC dimension of the square of the \(d\)-cube graph. The upper bound is dimension-independent and is proved by a support-reduction lemma followed by a finite *exhaustive* certificate, not by extrapolating from small dimensions.

## Assumptions and scope

All cube dimensions are positive integers, all vectors are binary, and distances are integer Hamming distances. Balls use the weak inequality \(\leq2\). Centers may be any cube vertex. The family contains the whole cube for \(d=1,2\), while in dimension three each radius-two ball omits exactly its antipode. Only the binary alphabet and fixed radius two are covered; no assertion is made about larger alphabets, varying radii, or arbitrary metric balls.

## Proof

**Step 1: reduce a hypothetical shattered five-set to ten coordinates.** Suppose \(S\subseteq Q_d\) is shattered and \(|S|=5\). One of its realizing balls contains all five points. Translate the cube by bitwise XOR with that ball's center, sending the center to the zero vector. Each of the five translated sample vectors now has at most two nonzero coordinates. Therefore their combined support \(U\) has cardinality at most ten.

For any center \(c\in Q_d\), write \(c_U\) for its restriction to the coordinates in \(U\), and let \(t\) count its nonzero coordinates outside \(U\). Since every sample point vanishes outside \(U\), for each \(x\in S\)
\[
\operatorname{dist}_H(x,c)=\operatorname{dist}_H(x_U,c_U)+t.
\]
For \(t\in\{0,1,2\}\), the trace on \(S\) is therefore the trace of a radius-\(2-t\) ball on the coordinates in \(U\). For \(t>2\), the trace is empty; the ten-cube enlarged family also realizes the empty trace on five sample points by taking radius zero at any center not among them. Pad \(U\) with zeros to a set of ten coordinates; allowing **all** projected centers and the three radii \(0,1,2\) can only increase the available traces. It consequently suffices to establish the following finite statement:

> In \(\{0,1\}^{10}\), no five distinct vectors of Hamming weight at most two are shattered by the **enlarged** family of all balls with radii \(0,1,2\) and arbitrary centers.

The enlarged family is used only as an upper-bound device. No equality between its VC dimension and the fixed-radius-two family's VC dimension is assumed.

**Step 2: exhaustive finite lemma.** The weight-at-most-two layer in ten coordinates contains exactly \(1+10+\binom{10}{2}=56\) points. Encode the complete universe of the \(3\cdot2^{10}=3072\) possible ball parameters (one radius and one center) by the bits of a nonnegative integer. For each sample point \(x\), calculate its exact incidence mask \(M(x)\) using the predicate
\[
\operatorname{bitcount}(x\mathbin{\mathrm{XOR}}c)\leq r,
\qquad r\in\{0,1,2\},\quad c\in\{0,\ldots,1023\}.
\]
For a sorted \(k\)-set of sample points, maintain the \(2^k\) masks identifying ball parameters inducing each of its Boolean membership patterns. The set is shattered exactly when none of these masks is empty. On adding a new point \(x\), each existing mask \(C\) must split into two nonempty masks \(C\cap M(x)\) and \(C\setminus M(x)\). Starting from all singletons, enumerate sorted extensions, retaining only shattered prefixes. This pruning is logically exhaustive: every subset of a shattered set is itself shattered, and the sorted \((k-1)\)-prefix is among those subsets.

The attached standalone file `verify.py` implements these finite integer operations. Its complete four-step exhaustive counts, for shattered subsets of size two, three, four, and five, are respectively
\[
1540,\quad27720,\quad49830,\quad\boxed{0}.
\]
In particular, the reduced finite statement is established. Coupled with Step 1, this rules out a shattered five-set in **every** dimension \(d\). This is a computer-assisted finite exhaustive proof of the upper bound, based on a mathematically proved dimension reduction; merely checking finitely many full cubes without that reduction would not suffice.

**Step 3: exact lower bounds and small dimensions.** When \(d\leq2\), every radius-two ball is the entire cube and the VC dimension is zero. When \(d=3\), each ball is the complement of the antipodal singleton. Any singleton is shattered, but no two-element set is (a ball omits at most one point), so the dimension is one.

In dimension four the three points represented by binary integers \(0,1,2\) are shattered. For each desired three-bit trace encoded as an integer from zero to seven, centers witnessing those traces in ascending trace order are
\[
(15,12,13,5,14,6,7,0).
\]
No four-point set is shattered in dimension four. This follows from the same complete trace-mask procedure with radius fixed at two, and the independent dimension-four exhaustive check in `verify.py` (the finite cube has only 16 vertices).

In dimension five the four points represented by binary integers \(0,1,2,4\) are shattered. Centers witnessing the sixteen traces in ascending trace order are
\[
(15,24,25,9,26,10,11,3,28,12,13,5,14,6,7,0).
\]
Each binary integer here denotes its usual five-coordinate bit vector. Appending zero coordinates to both sample points and their chosen centers preserves every Hamming distance. Thus the same shattered four-set exists for all \(d\geq5\). Together with the universal upper bound, this gives the claimed exact values.

## Verification

Execute `python3 verify.py` with Python 3.10 or later; it requires only the standard library. The program recomputes every bit of the enlarged ten-coordinate incidence relation, enumerates all potentially shattered sorted subsets through size five, and asserts the exact counts \(1540,27720,49830,0\). It separately verifies the fixed-radius-two VC dimensions in cubes of dimensions one through eight using translation symmetry for dimensions at least four, and checks both explicit lower-bound witnesses against **all** relevant ball centers.

The decisive computation is the size-five zero count for the *enlarged* family after an exact kernel reduction. The small-cube checks are independent corroboration and are not by themselves an infinite-dimensional proof. All loops are finite and have explicit parameter ranges; there is no random sampling, timeout-as-proof argument, or unverified optimizer.

## Relationship to prior work

Adler, Benediktsson, and Macpherson [1] study the **edge relation** of Hamming graphs, i.e. open neighborhoods determined by distance exactly one. Their Hamming-graph upper bound of three and their analysis of two-neighborhood structure do not determine VC dimension for the closed distance-at-most-two ball relation. In particular, the fact that a graph has VC dimension three for its open neighborhoods does not imply the present value four for closed neighborhoods in its graph square.

Coudert, Csikós, Ducoffe, and Viennot [2] develop algorithms for VC dimension of general graph closed-neighborhood systems. These apply in principle to any fixed finite cube-square graph, but do not constitute an all-dimension radius-two classification. Chalopin, Chepoi, Mc Inerney, Ratel, and Vaxès [3] treat sample compression of balls in selected graph classes; their general high-dimensional median-graph discussion does not provide the radius-two Boolean-cube VC formula. General results for balls at arbitrary radii, such as [4], are about broader set systems and do not directly imply the exact fixed-radius result here.

## Limitations

The upper bound depends on an exhaustively replayable finite certificate over 56 candidate sample points and 3,072 radius-center parameters. It is **not** an entirely hand-derived obstruction; independent implementations would improve confidence. The proof only concerns binary cubes and one fixed radius. No general formula is claimed for arbitrary radii, other alphabets, or unrestricted ball families. The literature comparison did not locate an equivalent exact theorem, but omission from searched indexes does not prove publication priority, and an equivalent result under metric learning or hypercube-power terminology remains possible. There has been no independent external audit.

## References

[1] I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs* (first arXiv public date 2020-07-31), arXiv:2007.16042, https://arxiv.org/abs/2007.16042; later *Discrete Applied Mathematics* 312 (2022), 29--44.

[2] D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension* (first arXiv public date 2024-05-13), arXiv:2405.07588, https://arxiv.org/abs/2405.07588.

[3] J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel, Y. Vaxès, *Sample compression schemes for balls in graphs* (first arXiv public date 2022-06-27), arXiv:2206.13254, https://arxiv.org/abs/2206.13254.

[4] N. Bousquet, S. Thomassé, *VC-dimension and Erdős--Pósa property*, *Discrete Mathematics* 338 (2015), 2302--2317, https://doi.org/10.1016/j.disc.2015.05.026.

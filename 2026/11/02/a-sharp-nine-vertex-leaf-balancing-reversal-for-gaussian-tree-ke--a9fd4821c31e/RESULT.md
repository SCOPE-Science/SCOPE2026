# A sharp nine-vertex leaf-balancing reversal for Gaussian tree kernels

## Finding

**Theorem (complete three-hub, six-leaf extremum).** Let \(T(a,b,c)\) be the unweighted tree obtained from a three-vertex path \(u_0-u_1-u_2\) by attaching \(a\), \(b\), and \(c\) new pendant leaves to its respective vertices, where \(a,b,c\) are positive integers and \(a+b+c=6\). Write \(d_T\) for graph distance and
\[
\wp(T)=\sup\left\{p\geq0:\ \sum_{x,y\in V(T)}\xi_x\xi_y d_T(x,y)^p\leq0\ \text{for every real }\xi\text{ with }\sum_x\xi_x=0\right\}.
\]
At the separating exponent \(p_0=137/100\), the metric of \(T(2,1,3)\) has **strict** \(p_0\)-negative type, whereas every other three-hub, six-leaf tree in this class, apart from its reversal \(T(3,1,2)\), fails \(p_0\)-negative type. In particular,
\[
\wp(T(a,b,c))<\frac{137}{100}<\wp(T(2,1,3))
\quad\text{for }(a,b,c)\notin\{(2,1,3),(3,1,2)\}.
\]
Thus \(T(2,1,3)\) and its reversal are the **only maximizing triples** among all ten positive triples of sum six. The perfectly balanced configuration \(T(2,2,2)\) is strictly suboptimal.

Equivalently, the kernel \(K_{t,p}(x,y)=\exp(-t d_T(x,y)^p)\) is positive semidefinite for *every* \(t>0\) exactly on the interval \(0\leq p\leq\wp(T)\); the nine-vertex optimizer therefore has a strictly larger admissible Gaussian exponent than all other members of the class.

## Assumptions and scope

Distances are ordinary shortest-path distances with all edges of length one. Every tree has nine distinct vertices: three path vertices and six leaves. The assertion compares only the ten triples of positive integers with total six, treating a reversal of the path as the same unrooted tree. It does not claim a maximizer among all nine-vertex trees or among arbitrary three-hub leaf totals. Positive semidefiniteness refers to the full nine-by-nine kernel matrix simultaneously at every positive scale; it is not a single-scale statement.

## Proof

**Step 1 (reduction to an eight-dimensional exact sign test).** Number the spine vertices \(0,1,2\) in order and append the pendant leaves, first those at \(0\), then at \(1\), then at \(2\). Use vertex \(8\) as a basepoint. For any \(p>0\), form the real symmetric matrix
\[
B_p(i,j)=\tfrac12\left(d(i,8)^p+d(j,8)^p-d(i,j)^p\right),\qquad 0\leq i,j<8.
\]
For every \(v\in\mathbb R^8\), let \(\xi_i=v_i\) for \(i<8\) and \(\xi_8=-\sum_{i<8}v_i\). Direct expansion yields
\[
\sum_{i,j=0}^8\xi_i\xi_jd(i,j)^p=-2v^{\mathsf T}B_pv.
\]
Hence \(p\)-negative type is equivalent to \(B_p\succeq0\), and strict \(p\)-negative type to \(B_p\succ0\). The Schoenberg correspondence identifies \(p\)-negative type with positive semidefiniteness of \(\exp(-t d^p)\) for every \(t>0\).

**Step 2 (algebraic enclosures without floating point).** Set \(p_0=137/100\) and \(Q=10^{12}\). All nonzero distances belong to \(\{1,2,3,4\}\). For each such distance \(m\), let \(r_m\) be the *unique* integer for which
\[
r_m^{100}\leq m^{137}Q^{100}<(r_m+1)^{100}.
\]
Integer-root bisection provides these \(r_m\) and verifies both inequalities using integer arithmetic, whence \(r_m/Q\leq m^{p_0}<(r_m+1)/Q\). Treat \(0^{p_0}=0\) and \(1^{p_0}=1\) exactly. Ordinary outward rational interval operations therefore enclose every entry of \(B_{p_0}\).

**Step 3 (a certified \(LDL^{\mathsf T}\) sign table).** Carry out unpivoted interval \(LDL^{\mathsf T}\) elimination with the above vertex order. Every division is by a pivot already proven strictly positive. For the six possibilities modulo reversal, the following table lists the first nonpositive pivot index \(k\) (starting at zero), or \(8\) if all eight are positive; it also gives a strict rational interval containing the final pivot. These bounds are outputs of exact fraction arithmetic, and all prior pivots in every row are certified positive.

| \((a,b,c)\) | \(k\) | Final pivot belongs to |
|---|---:|---|
| \((1,1,4)\) | 7 | \((-7,-6)\) |
| \((1,2,3)\) | 7 | \((-3,-2)\) |
| \((1,3,2)\) | 6 | \((-4,-3)\) |
| \((1,4,1)\) | 6 | \((-4,-3)\) |
| \((2,1,3)\) | 8 | \((0,1/20)\) |
| \((2,2,2)\) | 7 | \((-1,0)\) |

The standalone `verify.py` implements the interval class, integer roots, nine-vertex graph distances, Schoenberg matrices, and the exact elimination. Its assertions check the signs and rational bounds of the table, as well as the ten ordered triples and their six reversal classes. For \((2,1,3)\), every actual pivot is strictly positive, so \(B_{p_0}\) is positive definite. Each other representative has a strictly negative pivot preceded solely by positive pivots, so its matrix is not positive semidefinite. The same holds for reversed triples by graph isometry.

**Step 4 (sharp optimizer comparison).** In a finite metric space, the set of admissible negative-type exponents is a closed initial interval (the interval property and continuity of the distance-power matrix). Since \(B_{p_0}\succ0\) for \(T(2,1,3)\), continuity makes \(B_p\succ0\) for some \(p>p_0\), hence \(\wp(T(2,1,3))>p_0\). For each other representative, \(B_{p_0}\not\succeq0\), so its supremal admissible exponent is **strictly below** \(p_0\), by closedness of the initial interval. This proves the exact extremal classification and its Gaussian-kernel equivalent.

## Verification

Run `python verify.py` with a standard Python 3 interpreter. The checker uses only `fractions.Fraction` and integer arithmetic, contains no numerical eigensolver or floating-point decision, reconstructs all six representatives, proves every root enclosure, and checks every \(LDL^{\mathsf T}\) pivot sign used above. The computation is finite and exhaustive **only for the ten triples in the stated class**, while the Schoenberg and interval arguments prove the exponent assertions, including their strictness, without approximating the critical exponents themselves.

## Relationship to prior work

Doust and Weston developed quantitative strict negative type for finite metric trees and showed that it persists above exponent one. Li and Weston proved the strict-negative-type interval principle. Caffarelli, Doust, and Weston studied roundness bounds for metric trees, particularly large or infinite families. Sánchez gave a general distance-matrix method for finding the supremal negative-type exponent of a finite metric space. Those results justify the mathematical setting and the matrix method; the claim here is specifically the **exhaustive, certified six-leaf three-hub extremal comparison**, which is not an assertion about the general numerical method or earlier known tree bounds. In contrast to the natural expectation that equal leaf counts improve Gaussian admissibility, the middle-light asymmetric triple is optimal in this complete small family.

## Limitations

The result is a sharp finite-family classification, not an all-size theorem or a proof of the globally smallest counterexample. The exact thresholds themselves are not claimed in closed form. The integer-interval certificate can be independently replayed, but no independent mathematical audit has been performed. An equivalent previously published small-tree table or computational classification may have escaped the bounded literature search.

## References

- I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411v1, first public 2007-05-03.
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695v1, first public 2009-01-06.
- E. Caffarelli, I. Doust and A. Weston, *Metric trees of generalized roundness one*, arXiv:1008.3418v1, first public 2010-08-20.
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first public 2011-08-02.

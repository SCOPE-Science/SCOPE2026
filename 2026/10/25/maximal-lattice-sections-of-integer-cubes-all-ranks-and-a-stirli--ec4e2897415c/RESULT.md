# Maximal lattice sections of integer cubes: all ranks and a Stirling-number count

## Finding
For integers \(d\ge 2\), \(k\ge1\), and \(1\le \ell\le d-1\), put \(C_{d,k}=[0,k]^d\), and let \(A_{d,\ell}(k)\) count the **distinct affine \(\ell\)-dimensional subspaces** \(L\subset\mathbb R^d\) on which \(|L\cap C_{d,k}\cap\mathbb Z^d|\) is as large as possible. Then the maximum is \((k+1)^\ell\), and
\[
 A_{d,\ell}(k)=\sum_{m=\ell}^{d}\binom dm\!\left\{\!\begin{matrix}m\\\ell\end{matrix}\!\right\}2^{m-\ell}(k+1)^{d-m}
 =\frac{1}{2^\ell\ell!}\sum_{j=0}^{\ell}(-1)^{\ell-j}\binom\ell j(k+1+2j)^d.
\]
Here the braces are Stirling numbers of the second kind. Thus the section-count function is an **exact polynomial** of degree \(d-\ell\) for every \(k\ge1\), with leading coefficient \(\binom d\ell\), not merely an eventual quasi-polynomial.

Equality has a complete structural classification: partition some \(m\ge\ell\) active coordinate positions into exactly \(\ell\) nonempty unlabeled blocks. On each block all coordinates equal either one free parameter \(t_i\in[0,k]\) or its complement \(k-t_i\), with one free parameter per block; the remaining \(d-m\) coordinates are fixed at arbitrary integers in \(\{0,\dots,k\}\). These and only these affine subspaces maximize the lattice-point count.

In particular, for hyperplanes, \(A_{d,d-1}(k)=d(k+d)\). For lines, \(A_{d,1}(k)=((k+3)^d-(k+1)^d)/2\). For all ranks, the exponential generating function (including the natural zero- and full-dimensional boundary cases) is
\[
\sum_{d\ge0}\sum_{\ell=0}^{d}A_{d,\ell}(k)u^\ell\frac{z^d}{d!}
=\exp\!\left((k+1)z+\frac u2(e^{2z}-1)\right).
\]

## Assumptions and scope
An affine \(\ell\)-flat is an actual affine subspace of dimension exactly \(\ell\); distinct subspaces are counted once regardless of which coordinate projection or lattice points are used to describe them. Only lattice points of the closed integral cube are counted. The restrictions \(k\ge1\) and \(1\le\ell\le d-1\) avoid degeneracy. The zero-dimensional extension is \(A_{d,0}(k)=(k+1)^d\) (the individual grid points); the full-dimensional extension is \(A_{d,d}(k)=1\).

## Proof
**Projection bound.** The direction space of any affine \(\ell\)-flat \(L\) has rank \(\ell\). Some set of \(\ell\) coordinate restrictions is linearly independent, so the coordinate projection \(\pi_I:L\to\mathbb R^\ell\) is bijective. Consequently it injects \(L\cap\{0,\ldots,k\}^d\) into \(\{0,\ldots,k\}^\ell\), proving the upper bound \((k+1)^\ell\). A coordinate \(\ell\)-flat through grid positions attains it.

**Equality classification.** If equality holds, \(\pi_I\) maps the lattice-point intersection *onto the entire* \(\{0,\ldots,k\}^\ell\). Writing the remaining coordinates of \(L\) as affine functions \(f_j(t)=b_j+\sum_{i=1}^\ell a_{ji}t_i\), integer-valuedness at \(t=0\) and \(t=e_i\) (these points are available because \(k\ge1\)) implies \(b_j,a_{ji}\in\mathbb Z\). Because \(0\le f_j(t)\le k\) on all grid points, the difference of its maximum and minimum values is
\[
 k\sum_{i=1}^\ell |a_{ji}|\le k.
\]
Thus every row either has all coefficients zero, or has exactly one coefficient equal to \(1\) or \(-1\). In the first case \(f_j\) is an integer constant in \(\{0,\ldots,k\}\). In the second case the range restriction forces respectively \(f_j(t)=t_i\) or \(f_j(t)=k-t_i\). The selected free coordinate positions themselves realize \(f_i(t)=t_i\). Hence the coordinates decompose uniquely into \(\ell\) active equivalence classes, where two coordinates in a class are identical or complementary, and a remaining set of constant positions. Conversely any such construction provides a dimension-\(\ell\) flat with exactly \((k+1)^\ell\) grid points.

**No double counting.** Whether a coordinate is constant on \(L\) is intrinsic to \(L\), and among the active coordinates, the equivalence relation that two coordinates vary together up to complementation is also intrinsic. Each active block has a unique sign assignment modulo simultaneous complementation of the free parameter; if its size is \(r\), there are exactly \(2^{r-1}\) choices. Thus, fixing \(m\) active positions yields \(\binom dm\) choices of their set, \(\left\{\!\begin{smallmatrix}m\\\ell\end{smallmatrix}\!\right\}\) set partitions into blocks, \(2^{m-\ell}\) sign choices, and \((k+1)^{d-m}\) assignments to constant coordinates. Summing gives the first formula.

**Closed form and degree.** The exponential generating function of a signed nonempty block is
\[
\sum_{r\ge1}2^{r-1}\frac{z^r}{r!}=\frac{e^{2z}-1}{2},
\]
while a fixed coordinate has \(k+1\) choices. The exponential formula for an unordered set of \(\ell\) active blocks proves the displayed generating function. Extracting the coefficient of \(u^\ell\) and expanding \((e^{2z}-1)^\ell\) yields the finite-difference formula. In the first formula the term \(m=\ell\) has degree \(d-\ell\) and positive leading coefficient \(\binom d\ell\), while all later terms have lower degree. The hyperplane and line specializations follow by direct substitution. This completes the proof for all \(d,k,\ell\) in the stated domain.

## Verification
A self-contained Python 3 standard-library script, `verify_maximal_grid_flats.py`, independently enumerates the affine spans of all \((\ell+1)\)-tuples of points of small cubical grids and computes their intersection cardinalities using exact rational reduced row echelon forms. It compares each actual maximizing-flat count with both combinatorial and finite-difference formulas for ten cases, including \((d,k,\ell)=(4,1,2)\) (exactly \(100\) maximizers) and \((3,2,2)\) (exactly \(15\)). Additional exact integer arithmetic compares the two formulas in 231 parameter cases. The computation gives `CUBICAL_MAXIMAL_FLATS_OK exhaustive_cases=10 formula_identities=231`.

The general theorem depends on the preceding infinite-domain proof; finite enumeration is neither an exhaustive test of arbitrary dimension nor a substitute for that proof.

## Relationship to prior work
Lê Thành Dũng Nguyên (2019) proves the **maximum cardinality** \((k+1)^\ell\) for affine grid sections; the bound, but not the equality classification or number of maximizing flats, is prior work. Melo and Winter (2017/2018) treat intersections with the binary hypercube and prove a second-largest-cardinality gap; their maximum-cardinality arguments are related, but they do not state the all-grid-size, all-rank enumerative formula here. Averkov, Brose, De Loera, Lopez-Campos, and Torres (first public version August 27, 2025; revised October 3, 2026), Conjecture 4.8, propose an eventual quasi-polynomial law of degree \(d-\ell\) for numbers of maximal lattice-point sections of general lattice polytopes. The formula above verifies the conjectural behavior for **cubes only**, for every positive dilation, and additionally supplies the complete equality classification.

## Limitations
This result does not prove the conjecture for arbitrary lattice polytopes, for general rectangular boxes with unequal side lengths, or for sections with nearly maximal but not maximal numbers of grid points. The maximum-count inequality and the binary-cube maximum have established precursors; the claimed addition is the explicit complete all-rank equality classification and enumerative polynomial for integral cubes. Historical priority is based on the cited inspected sources and targeted searches, not an independent exhaustive literature review.

## References
1. Lê Thành Dũng Nguyên, *When lattice cubes meet affine subspaces: a short note* (2019), arXiv:1909.03542, https://arxiv.org/abs/1909.03542.
2. Nolmar Melo and Andreas Winter, *Intersection patterns of linear subspaces with the hypercube* (2017; revised 2018), arXiv:1712.01763, https://arxiv.org/abs/1712.01763.
3. Gennadiy Averkov, Anouk E. Brose, Jesús A. De Loera, Gyivan Lopez-Campos, Antonio J. Torres, *On Lattice Diameter Segments: Algorithms and Structure* (first posted August 27, 2025; revised October 3, 2026), arXiv:2508.20009, Section 4, Conjecture 4.8, https://arxiv.org/html/2508.20009v2.

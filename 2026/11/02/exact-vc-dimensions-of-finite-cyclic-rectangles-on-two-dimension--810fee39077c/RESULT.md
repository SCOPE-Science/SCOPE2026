# Exact VC dimensions of finite cyclic rectangles on two-dimensional tori

## Finding

For an integer \(m\ge1\), write \(\mathbb Z_m\) for the cycle of \(m\) ordered residue positions. A *cyclic interval* is the empty set, the whole cycle, or the positions encountered on a nonempty consecutive run around the cycle. Let
\[
\mathcal R_{m,n}=\{I\times J:I\subseteq\mathbb Z_m,\ J\subseteq\mathbb Z_n\text{ are cyclic intervals}\}.
\]
The domain is \(\mathbb Z_m\times\mathbb Z_n\). A finite support is *shattered* when every one of its subsets is the intersection with some member of \(\mathcal R_{m,n}\). Put \(a=\min\{m,n\}\) and \(b=\max\{m,n\}\). Then, for **all** positive integers \(m,n\),
\[
\boxed{
\operatorname{VCdim}(\mathcal R_{m,n})=
\begin{cases}
\min\{b,a+2\},&a\le2,\\
4,&a=3,\\
5,&a=4,\\
5,&a=b=5,\\
6,&a=5,\ b\ge6,\text{ or }a\ge6.
\end{cases}}
\]
In particular, six-point shattering occurs if and only if both sides have at least five positions and at least one has six. The **first** side-size pair, up to interchange, attaining the continuous-torus VC dimension six is \((5,6)\); among square grids the first is \((6,6)\). The one-dimensional cyclic-interval boundary is included for completeness, not asserted as a novel result.

## Assumptions and scope

The coordinate cycles are finite ordered sets, not graph-geodesic arcs; when \(m\) or \(n\) is at most two the same cyclic-consecutiveness definition still applies. The empty and complete cyclic intervals are permitted, as are rectangles having a complete factor. The theorem concerns ordinary VC dimension, not Littlestone dimension, the number of shattered supports, or boxes with fixed side length. It uses no generic-position assumption: repeated coordinate values are included.

## Proof

**Arc-trace lemma.** Let \(S=\{p_0,\ldots,p_{k-1}\}\) be an ordered list of distinct sample points with \(p_i=(x_i,y_i)\). For \(0\le r<m\) and \(1\le\ell<m\), the mask
\[
A_{r,\ell}=\{i:x_i\in\{r,r+1,\ldots,r+\ell-1\}\pmod m\}
\]
is the trace of a proper nonempty cyclic interval on the first coordinate; the empty and full masks complete this family. Define \(B_{s,h}\) analogously for the second coordinate. The trace masks of \(\mathcal R_{m,n}\) on \(S\) are **exactly** the intersections \(A\cap B\). Thus \(S\) is shattered if and only if this finite intersection family has precisely \(2^k\) members. This establishes the meaning of every test in the accompanying executable certificate.

**Order compression and enlargement.** Suppose the first-coordinate projection of a support uses exactly \(c\) distinct positions, and the second uses \(d\). Replacing the occupied positions in each cyclic order by the successive labels \(0,\ldots,c-1\) and \(0,\ldots,d-1\) preserves every cyclic-interval trace on the support. Conversely, embedding one finite cyclic order into a longer order in the same cyclic sequence preserves every old interval trace on the embedded support. Therefore the existence of a shattered \(k\)-support depends only on two cyclic weak orders on its points; in particular, every such support can be compressed into a \(\min\{m,k\}\)-by-\(\min\{n,k\}\) grid without losing any trace. A non-shattering result for a grid \(u\times v\) forbids shattered \(k\)-supports for all grids whose first side is at most \(u\) and second side is arbitrary when \(v\ge k\); similarly after interchanging coordinates. These statements also apply to singleton cycles.

**Removing coordinate ties to bound the dimension.** For any seven distinct points, split each group of equal first coordinates into consecutive new positions, and independently split groups of equal second coordinates. Every previous cyclic-interval trace remains available because the new interval may include or exclude entire groups. After splitting, each coordinate projection contains seven distinct positions. Relabeling first-coordinate positions by \(0,\ldots,6\) makes the second-coordinate positions a permutation of these labels. The executable certificate tests all \(7!=5040\) permutations and shows that **none** gives all \(128\) rectangle traces. Hence no seven-point support is shattered for any positive \(m,n\). Because shattering is hereditary, the VC dimension is always at most six. This is an independent finite-order-type proof of the known continuous two-dimensional torus upper bound.

**Complete finite obstructions.** Translating a support by an element of \(\mathbb Z_m\times\mathbb Z_n\) preserves the entire rectangle family. Thus any nonempty \(k\)-point support can be translated so that one designated point is \((0,0)\). The certificate enumerates all \(\binom{mn-1}{k-1}\) choices of the remaining points. The following are the complete absence results; the fourth column is the number of checked supports, not an estimate.

| Grid | Forbidden shattered support size | Complete origin-fixed cases |
|---|---:|---:|
| \(1\times4\) | 4 | 1 |
| \(2\times2\) | 3 | 3 |
| \(2\times3\) | 4 | 10 |
| \(2\times5\) | 5 | 126 |
| \(3\times5\) | 5 | 1,001 |
| \(4\times6\) | 6 | 33,649 |
| \(5\times5\) | 6 | 42,504 |

The compression lemma extends these obstructions to all larger unlisted second coordinates when the first coordinate stays small. In the exceptional \(5\times5\) case it prohibits a sixth point. The seven-permutation check supplies the universal remaining upper bound.

**Explicit matching witnesses.** The following supports are shattered; all coordinates use zero-based residue labels. The accompanying program verifies all \(2^k\) traces of each witness using *two independent implementations* of cyclic-rectangle traces.

| Grid | Support size | Coordinates |
|---|---:|---|
| \(1\times1\) | 1 | \((0,0)\) |
| \(1\times2\) | 2 | \((0,0),(0,1)\) |
| \(1\times3\) | 3 | \((0,0),(0,1),(0,2)\) |
| \(2\times2\) | 2 | \((0,0),(0,1)\) |
| \(2\times3\) | 3 | \((0,0),(0,1),(0,2)\) |
| \(2\times4\) | 4 | \((0,0),(0,2),(1,1),(1,3)\) |
| \(3\times3\) | 4 | \((0,0),(0,1),(1,2),(2,2)\) |
| \(4\times4\) | 5 | \((0,0),(0,2),(1,1),(2,3),(3,1)\) |
| \(5\times6\) | 6 | \((0,0),(0,2),(1,1),(2,3),(3,4),(4,5)\) |

Enlargement and coordinate interchange propagate these witnesses to all parameter ranges in the formula. The obstruction table and the six-dimensional universal bound give matching upper bounds, completing the classification.

## Verification

Run `python3 torus_grid_certificate.py` using Python 3 and the standard library only. The executable runs deterministically and does not sample or depend on external packages. It generates every origin-fixed support in the seven finite obstruction cases (77,294 supports), every one of the 5,040 generic seven-point cyclic order types, and verifies all nine lower-bound witnesses. It also independently constructs actual rectangle subsets on small grids and compares their traces with the optimized bit-mask intersection method on 1,119 supports. The expected final marker is `ALL_FINITE_TORUS_VC_CHECKS_PASS`. The full output is reproduced in `VERIFICATION.md`.

The infinite-parameter statement is obtained from the proved compression, tie-splitting, translation, and enlargement lemmas plus these exhaustive finite certificates. It is **not** an inference that a finite experimental pattern continues indefinitely.

## Relationship to prior work

Gillibert, Lachmann, and Müllner, *The VC-Dimension of Axis-Parallel Boxes on the Torus* (first public preprint 28 April 2020), establish the asymptotic high-dimensional result and report that unrestricted continuous two-dimensional torus boxes have VC dimension six. That continuous dimension is prior work and is not claimed here. The present result answers the distinct discrete question of precisely which **finite cyclic coordinate resolutions** realize each VC dimension, including the sharp \(5\times6\) threshold and all degeneracies. The ordinary non-periodic planar rectangle class has VC dimension four; it does not imply the cyclic classification. Searches of related discretized-box and cyclic-rectangle literature did not identify a matching full two-parameter classification.

## Limitations

This classification is specific to Cartesian products of arbitrary cyclic intervals, including the empty and complete sets. It does not determine numbers of shattered supports, online dimensions, or the fixed-width box problem. The negative cases are computer-assisted but exhaustively certified after mathematical finite reductions; the script and complete reduction arguments are necessary parts of the proof. Exhaustive historical priority has not been established, especially for equivalent formulations using circular-arc range spaces or combinatorial order types. Independent validation has not been performed.

## References

1. P. Gillibert, T. Lachmann, C. Müllner, *The VC-Dimension of Axis-Parallel Boxes on the Torus*, arXiv:2004.13861 (initial version 2020-04-28), https://arxiv.org/abs/2004.13861 ; *Journal of Complexity* 68 (2022), 101600, doi:10.1016/j.jco.2021.101600.
2. V. N. Vapnik and A. Ya. Chervonenkis, *On the uniform convergence of relative frequencies of events to their probabilities*, *Theory of Probability and Its Applications* 16 (1971), 264–280, doi:10.1137/1116025.

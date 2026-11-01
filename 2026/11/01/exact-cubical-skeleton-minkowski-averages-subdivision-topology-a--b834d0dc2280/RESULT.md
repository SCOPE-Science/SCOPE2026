# Exact cubical-skeleton Minkowski averages: subdivision, topology, and sharp Hausdorff profile

## Finding

Let \(d\geq2\), \(0\leq k<d\), \(m\geq1\) be integers, and let \(a_1,\ldots,a_d>0\). Put \(Q=\prod_{i=1}^d[-a_i,a_i]\). Denote its closed \(k\)-skeleton, the union of faces of dimensions at most \(k\), by \(S_k(Q)\), and its \(m\)-fold equal-weight Minkowski average by
\[
A_m=\frac1m\big(S_k(Q)+\cdots+S_k(Q)\big).
\]
Define \(G_{m,i}=\{a_i(-1+2j/m):0\leq j\leq m\}\), \(t=\min\{mk,d\}\), and \(r=d-t\). Then **the exact set identity** is
\[
\boxed{A_m=\{x\in Q:\#\{i:x_i\notin G_{m,i}\}\leq mk\}.}
\]
Thus for \(mk<d\), \(A_m\) is the entire \(mk\)-dimensional skeleton of the uniform \(m\)-by-\(\cdots\)-by-\(m\) cubical subdivision of \(Q\), while for \(mk\geq d\), \(A_m=Q\).

Let \(a_{(1)}\leq\cdots\leq a_{(d)}\) be the sorted half-widths. For every \(1\leq p<\infty\), the sharp Hausdorff distance in the coordinate \(\ell_p\) metric is
\[
\boxed{d_{H,p}(A_m,Q)=m^{-1}\left(\sum_{i=1}^r a_{(i)}^p\right)^{1/p}.}
\]
For the \(\ell_\infty\) metric it equals \(a_{(r)}/m\) when \(r>0\) and zero otherwise. Each supremum is attained at centers of subdivision cells. In particular, for \(k\geq1\), exact convexification first occurs at \(m=\lceil d/k\rceil\); for \(k=0\), no finite sum is convex, although the Hausdorff gap decreases as \(1/m\).

The integral homotopy type of every *subcritical* average is also exact:
\[
\boxed{A_m\simeq\bigvee^{\beta_{d,m,t}}\mathbb S^t,\qquad
\beta_{d,m,t}=\sum_{j=t+1}^{d}(-1)^{j-t-1}\binom dj m^j(m+1)^{d-j},\quad t<d.}
\]
The wedge-of-zero-spheres convention means \(\beta+1\) components. All reduced integral homology is free and concentrated in degree \(t\). At and beyond the convexification threshold the space is contractible. These claims hold for every positive side-length vector, including repeated lengths.

## Assumptions and scope

A face of \(Q\) is obtained by fixing some coordinates to their signed endpoints and leaving the others unrestricted; hence \(x\in S_k(Q)\) precisely when at most \(k\) coordinates satisfy \(|x_i|<a_i\). The sums consist of exactly \(m\) terms from this same *nonconvex* skeleton. The closed-face convention includes all boundary strata. Hausdorff distance uses the ambient coordinate \(\ell_p\) norm for the stated \(p\); one always has \(A_m\subseteq Q\). Empty sums of nonnegative quantities are zero. Critical equality \(mk=d\) is included in convexification. No genericity, rationality, or symmetry of the side lengths beyond orthogonality is assumed.

## Proof

**Step 1: the necessary count.** In each of the \(m\) summands, at most \(k\) coordinates lie in the interior of their one-dimensional intervals. If all \(m\) summands have endpoint values in coordinate \(i\), the averaged coordinate belongs to the grid \(G_{m,i}\). Therefore every non-grid coordinate in the average requires at least one interior coordinate among the summands. There are at most \(mk\) such slots, proving necessity of the displayed set identity.

**Step 2: constructive sufficiency.** Let \(x\in Q\) have at most \(mk\) non-grid coordinates. Assign each such coordinate to one of \(m\) summands so that no summand receives more than \(k\) assigned coordinates (distribute them consecutively into \(m\) blocks of size at most \(k\)). For a coordinate \(i\) on the grid, choose endpoint signs on all \(m\) summands whose average is \(x_i\). For a non-grid coordinate, take its assigned summand as its sole free coordinate and use endpoint signs on the other \(m-1\) summands. With \(j=0,\ldots,m-1\) positive endpoints among those \(m-1\), the allowable averaged values form
\[
\left[\frac{a_i(2j-m)}m,\frac{a_i(2j-m+2)}m\right].
\]
These \(m\) intervals tile \([-a_i,a_i]\) exactly, so choose \(j\) and a value of the single free summand giving the prescribed \(x_i\). Coordinates are independent: every constructed summand has at most \(k\) free coordinates, and therefore belongs to \(S_k(Q)\). Their average is \(x\). This proves the set identity for all parameters, including \(k=0\) and \(mk\geq d\).

**Step 3: exact metric profile.** Write \(\delta_i(x_i)=\operatorname{dist}(x_i,G_{m,i})\), and order the \(d\) nonnegative distances increasingly, with indices in parentheses. By the set identity, the distance from any \(x\in Q\) to \(A_m\) is
\[
\operatorname{dist}_p(x,A_m)=\left(\sum_{j=1}^r\delta_{(j)}(x)^p\right)^{1/p}
\]
for finite \(p\), and is \(\delta_{(r)}(x)\) for \(p=\infty\) and \(r>0\). Indeed one must round at least \(r\) coordinates to the nearest grid points, and doing so on the \(r\) cheapest coordinates is optimal. Each \(\delta_i(x_i)\leq a_i/m\). Since all coordinates can independently be placed at grid-cell midpoints, these upper bounds can hold simultaneously. Maximizing the ordered \(r\)-term expression yields precisely the displayed half-width formulas. Since \(A_m\subseteq Q\), this point-to-set supremum equals the Hausdorff distance.

**Step 4: topology.** In the uniform \(m\)-subdivision, the number of closed \(j\)-cells is
\[
f_j=\binom dj m^j(m+1)^{d-j}.
\]
For \(t<d\), the set identity says \(A_m\) is the \(t\)-skeleton of this regular cubical CW complex. Its full complex is a contractible \(d\)-ball. The inclusion of the \(t\)-skeleton induces isomorphisms on homotopy groups in dimensions below \(t\) (since all omitted cells have dimensions at least \(t+1\)), so this skeleton is \((t-1)\)-connected for \(t\geq1\). A connected graph is a wedge of circles when \(t=1\), and for \(t\geq2\) a \((t-1)\)-connected finite \(t\)-complex is homotopy equivalent to a wedge of \(t\)-spheres by Hurewicz and the Whitehead theorem. For \(t=0\), it is a finite set of \((m+1)^d\) vertices. Hence reduced homology is concentrated in degree \(t\), and the number of spheres is \((-1)^t(\sum_{j=0}^t(-1)^jf_j-1)\). Since the full cube has Euler characteristic \(1=\sum_{j=0}^d(-1)^jf_j\), rearrangement gives the displayed tail sum. When \(t=d\), \(A_m=Q\) is contractible. The proof is independent of the aspect ratios.

As one check, a four-dimensional box's edge skeleton averaged twice becomes the two-skeleton of its \(2\)-subdivision, a wedge of \(80\) two-spheres. With half-widths \((1,2,3,4)\), its Euclidean Hausdorff defect is \(\sqrt5/2\).

## Verification

The standalone `verify.py`, included alongside this result, runs using Python's standard library. Execute `python verify.py` after extraction. It independently enumerates exact integer-lattice Minkowski sums and the predicted subdivision-skeleton membership (23 cases, 23,988 counted target lattice points), computes cellular boundary ranks over \(\mathbb F_2\) for 23 low-dimensional grids, and evaluates six exact rational deep-hole checks. It reports `PASS`. These finite diagnostics do **not** establish any universal quantifier; the construction, distance minimization, and CW argument above establish the theorem in all dimensions and all summand counts.

## Relationship to prior work

Van Hintum's 2026 paper investigates general sharp thresholds for Hausdorff convexification of arbitrary compact sets under repeated Minkowski averaging. Its generic contraction bound does not specify the exact shape, metric deficit, or homotopy type for an orthotope skeleton. The earlier systematic work of Fradelizi, Madiman, Marsiglietti, and Zvavitch gives general convexification phenomena and convergence bounds, likewise not this cubical subdivision identity. Meyer's 2026 finite-convexification study instead adds a scaled *convex* body to an arbitrary compact set and is not an iteration of a nonconvex skeleton.

An earlier exact theorem for *simplex* skeleta gives the same numerical saturation threshold \(\lceil d/k\rceil\), but the nonconvex sets, coordinate combinatorics, intermediate average shapes, metric formulas, and homology are different. In particular, that equality of cutoff numbers alone does not imply any of this theorem's exact cubical subdivision or all-order geometric-topological profiles. Separate results on convex-body offsets of orthotope skeleta likewise concern a different summand operation.

## Limitations

The exact identity relies on Cartesian-coordinate independence and equal weights. It does not assert comparable formulas for nonorthogonal parallelotopes in an ambient Euclidean norm, unequal averaging weights, or general polytopes. The homotopy statement is not a claim that the filtration maps between averages realize a particular persistent-homology barcode. Search and comparison cannot exclude an unindexed or older equivalent combinatorial result. No independent mathematical audit has been performed.

## References

1. Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1, first public 2026-06-09. https://arxiv.org/abs/2606.10815 .
2. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, and Artem Zvavitch, *The convexification effect of Minkowski summation*, arXiv:1704.05486. https://arxiv.org/abs/1704.05486 .
3. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1, first public 2026-10-19. https://arxiv.org/abs/2610.26744 .
4. *Sharp finite convexification thresholds for every skeleton of a simplex*, publicly available mathematical research record, 2026-10-11.

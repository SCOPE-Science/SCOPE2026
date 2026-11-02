# Small-order endpoint stability and a regular-face obstruction for Euclidean Birkhoff projection

## Finding

For an integer \(n\ge 2\), let
\[
\mathcal B_n=\{X\in\mathbb R^{n\times n}:X_{ij}\ge0,\ \sum_jX_{ij}=\sum_iX_{ij}=1\}
\]
be the Birkhoff polytope. Write \(\Pi_n\) for Euclidean (Frobenius-metric) nearest-point projection onto \(\mathcal B_n\), but measure perturbations in the entrywise norm \(\|X\|_{\max}=\max_{ij}|X_{ij}|\). Its global Lipschitz modulus is
\[
L_n=\sup_{U\ne V}\frac{\|\Pi_n(U)-\Pi_n(V)\|_{\max}}{\|U-V\|_{\max}}.
\]
The following statements hold.

**Exact small orders.** For \(n=2,3,4\), respectively,
\[
\boxed{L_2=1,\qquad L_3=\frac{16}{9},\qquad L_4=\frac94.}
\]
For these three orders the unique support orbit attaining the largest local operator norm is the full support, and the quotient is attained by distinct finite input matrices. Equivalently, the nonnegativity constraints do not increase the endpoint modulus beyond the affine doubly-stochastic projection for these orders.

**A regular active-face obstruction.** At \(n=12\) let
\[
S=\{0,2,3,6,8,9\}\subset\mathbb Z/12\mathbb Z,\qquad
E=\{(i,j):j-i\pmod {12}\in S\},
\]
with indices \(0,\ldots,11\). The tangent-space orthoprojector corresponding to this (six-regular, cyclically symmetric) support has a row of absolute sum \(41/12\), at coordinate \((0,2)\). Consequently
\[
\boxed{L_{12}\ge\frac{41}{12}>\frac{121}{36}=4\left(1-\frac1{12}\right)^2.}
\]
The strict gap \(1/18\) disproves the proposed universal rule that the full-support affine piece always controls the entrywise Lipschitz modulus of Euclidean Birkhoff projection. Both the exact small-order constants and the exhibited lower bound are realized by finite input pairs. No exact value of \(L_{12}\), nor an exact first failing dimension, is asserted.

## Assumptions and scope

All matrices are real and unrestricted in their input entries; the projection output is nonnegative with every row and column sum one. Projection minimizes the **Frobenius** squared distance, not maximum distance, and the Lipschitz ratio uses the **entrywise maximum norm**, not the matrix induced \(\ell_\infty\) norm. The result concerns the full (not symmetry-constrained) doubly stochastic polytope. An allowed-edge set \(E\subseteq\{0,\ldots,n-1\}^2\) is called *totally supported* when it is the union of supports of one or more permutation matrices. For such \(E\), define
\[
V_E=\left\{H:\operatorname{supp}H\subseteq E,\ \sum_jH_{ij}=\sum_iH_{ij}=0\right\}
\]
and let \(R_E\) denote Frobenius-orthogonal projection onto \(V_E\), extended by zeros to forbidden coordinates.

## Proof

### 1. Reduction to all support-face projectors

Every face of \(\mathcal B_n\) is obtained by imposing coordinate equations \(X_{ij}=0\). Its relative interior has a positive entry exactly at the coordinates of a totally supported set \(E\): one direction follows from the Birkhoff–von Neumann convex-hull theorem; conversely, averaging the permutation matrices whose union is \(E\) gives a relative-interior point \(Y\) positive precisely on \(E\). The tangent linear space to this face is exactly \(V_E\).

Orthogonal projection onto a polyhedron is continuous and piecewise affine. On a full-dimensional projection cell associated with a face \(E\), its linear part is \(R_E\). Thus, by decomposing any segment into finitely many such cells,
\[
L_n\le\max_{E\text{ totally supported}}\|R_E\|_{\max\to\max}.
\]
Each term on the right also occurs as a local Lipschitz quotient. Indeed choose \(Y\) strictly positive on \(E\) and zero elsewhere, and let \(G=Y-\mathbf1_{E^c}\). Then \(\Pi_n(G)=Y\). The point \(Y\) lies in the relative interior of its face and the forbidden-coordinate normal coefficients are strictly positive; hence in a sufficiently small neighborhood of \(G\), projection is the affine projection onto this face. Choosing a sign perturbation of a norming row of \(R_E\) realizes its absolute row sum as a finite difference quotient. Therefore
\[
\boxed{L_n=\max_{E\text{ totally supported}}\max_{e\in E}\sum_{f\in E}|(R_E)_{ef}|.}\tag{1}
\]
This formula uses only ordinary real Euclidean orthogonality; no nonlinear differential regularity beyond polyhedral piecewise affinity is assumed.

For the full edge set \(E_*=\{0,\ldots,n-1\}^2\), double centering gives
\[
(R_{E_*}H)_{ij}=H_{ij}-\frac1n\sum_bH_{ib}-\frac1n\sum_aH_{aj}+\frac1{n^2}\sum_{a,b}H_{ab}.
\]
Its row kernel consists of \((n-1)^2/n^2\) at the target entry, \(-(n-1)/n^2\) at each of its \(2(n-1)\) row/column neighbors, and \(1/n^2\) at the remaining \((n-1)^2\) positions. Hence
\[
\|R_{E_*}\|_{\max\to\max}=4\left(1-\frac1n\right)^2.\tag{2}
\]

### 2. Exhaustion through four rows and columns

There are exactly \(3\), \(49\), and \(7443\) totally supported labeled edge sets for \(n=2,3,4\), respectively. Under the independent row and column permutation group their orbit counts are \(2\), \(6\), and \(42\). These are not sampling counts: each subset of the \(n^2\) possible edges is tested against all \(n!\) perfect matchings, and an edge set passes exactly when it equals the union of its contained perfect matchings. Every orbit is then generated explicitly.

For each representative \(E\), form its bipartite vertex-edge incidence matrix \(B_E\) with a \(1\) at both incident endpoints of every permitted edge. Drop one redundant vertex equation in each connected component, yielding a full-row-rank matrix \(\widehat B_E\). Exact rational elimination computes
\[
R_E=I-\widehat B_E^{\mathsf T}
(\widehat B_E\widehat B_E^{\mathsf T})^{-1}\widehat B_E.
\tag{3}
\]
The resulting maxima of the absolute row sums over all representatives are exactly \(1\), \(16/9\), and \(9/4\). In each size the unique maximizing orbit is the full edge set; every proper face has strictly smaller norm. Formula (2) provides the matching attained lower bounds. The included standalone `verify.py` performs the complete enumeration, orbit reduction and rational inversion from first principles and prints every orbit-norm distribution.

### 3. The twelve-by-twelve regular obstruction

Use the cyclic set \(E\) in the finding. It is totally supported because for each \(s\in S\), the cells \((i,i+s\bmod 12)\) form a permutation matrix. In particular \(Y_{ij}=1/6\) on \(E\) and zero outside is a relative-interior point of the associated face.

For this connected bipartite support, reduce its \(24\)-row incidence matrix by deleting one redundant row. Formula (3) then uses an invertible \(23\)-by-\(23\) rational Gram matrix. At the target \(e=(0,2)\) the \(72\) exact entries of the resulting projector row have this complete value-multiplicity table:

| Entry value | Multiplicity |
| ---: | ---: |
| \(97/144\) | 1 |
| \(1/144\) | 1 |
| \(-23/144\) | 2 |
| \(-5/144\) | 4 |
| \(-37/288\) | 8 |
| \(11/288\) | 8 |
| \(-1/72\) | 16 |
| \(1/36\) | 16 |
| \(5/288\) | 16 |

All multiplicities sum to \(72\). Multiplying their absolute values and adding yields exactly \(41/12\). By contrast, formula (2) gives the full-support value \(121/36\). Let \(H\) equal the sign of the displayed projector row on its allowed coordinates and zero elsewhere. It satisfies \(\|H\|_{\max}=1\), while \((R_EH)_{0,2}=41/12\). The strict-complementarity construction in part 1 supplies finite inputs \(G\) and \(G+\varepsilon H\) for all sufficiently small positive \(\varepsilon\), with projection difference exactly \(\varepsilon R_EH\). This proves the asserted strict inequality.

## Verification

Run `python3 verify.py` using Python's standard library only. The program exhausts all labeled support patterns for orders two through four and computes their exact orbit-representative projection norms using fractions, without floating point or optimization oracles. It also reconstructs the regular \(72\)-edge support, checks row/column degrees, obtains the nine exact row-entry multiplicities, verifies the idempotent-row identity, and verifies the sign-witness equality and rational gap. All assertions passed on the included source. The finite enumeration establishes the complete small-order theorem because the proof of (1) covers every possible input; the twelve-dimensional calculation is a rigorous lower bound, not a claim of exhaustive higher-dimensional search.

## Relationship to prior work

Bai–Chu–Tan (2007, publicly online April 6) treat nearest doubly stochastic matrices **with an additional prescribed entry**, via a dual Newton method. Their available June 2006 manuscript provides the underlying projection problem, but not the endpoint-norm constants or the regular-face counterexample. Zass–Shashua (NIPS 2006) study Frobenius-optimal normalization of **symmetric** doubly stochastic matrices for clustering; their projection domain is narrower. Li–Sun–Toh (arXiv 1702.05934, first posted February 20, 2017) provide a general Jacobian construction for Euclidean Birkhoff projection; the paper supplies a framework compatible with formula (3) but does not evaluate the exact entrywise Lipschitz constants for orders two through four or the explicit regular twelve-by-twelve obstruction. The affine double-centering map and its norm are standard background, not claimed as new.

## Limitations

The result does not determine \(L_n\) for \(n\ge5\) except for the stated dimension-twelve lower bound, nor locate the smallest order where the affine full-face norm fails. It does not concern symmetric doubly stochastic matrices, different metric projections, weighted entrywise norms, or the induced matrix \(\ell_\infty\) norm. The novelty comparison is bounded by the inspected primary sources and available indexing; a previously unindexed exact stability calculation could alter publication priority. No independent validation has been performed.

## References

1. Z.-J. Bai, D. Chu, R. C. E. Tan, *Computing the Nearest Doubly Stochastic Matrix with A Prescribed Entry*, SIAM Journal on Scientific Computing 29 (2007), 635–655, doi:10.1137/050639831, published online 2007-04-06. Author manuscript: https://ccam.xmu.edu.cn/teacher/zjbai/papers/BaiCT_DS.pdf.
2. R. Zass, A. Shashua, *Doubly Stochastic Normalization for Spectral Clustering*, Advances in Neural Information Processing Systems 19 (2006), https://papers.neurips.cc/paper_files/paper/2006/hash/4fa177df22864518b2d7818d4db5db2d-Abstract.html.
3. X. Li, D. Sun, K.-C. Toh, *On the efficient computation of a generalized Jacobian of the projector over the Birkhoff polytope*, arXiv:1702.05934 (initially posted 2017-02-20), https://arxiv.org/abs/1702.05934.
4. W. Glunt, T. L. Hayden, R. Reams, *The nearest doubly stochastic matrix to a real matrix with the same first moment*, Numerical Linear Algebra with Applications 5 (1998), 475–482 (background for affine least-squares conditions).

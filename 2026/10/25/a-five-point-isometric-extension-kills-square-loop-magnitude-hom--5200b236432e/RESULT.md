# A five-point isometric extension kills square-loop magnitude homology

## Finding

Let \(X=\{A,B,C,D\}\subset\mathbb R^2\) be the four corners of a Euclidean square of side \(2\), and let \(Y=X\cup\{O\}\) add its center. For the isometric inclusion \(i:X\hookrightarrow Y\),

\[
\mathrm{MH}_{2,4\sqrt2}(X;\mathbb Z)\cong\mathbb Z^4,
\qquad
\mathrm{MH}_{2,4\sqrt2}(Y;\mathbb Z)=0,
\qquad i_*=0.
\]

Thus one point added without changing any old distances kills an entire rank-four magnitude-homology group in a single bidegree.

## Assumptions and scope

For a finite metric space \(M\), the magnitude chain group \(\mathrm{MC}_{k,\ell}(M)\) is the free abelian group on tuples \((x_0,\ldots,x_k)\) with consecutive entries distinct and total length \(\sum_{j=1}^{k}d(x_{j-1},x_j)=\ell\). Its differential deletes an interior entry only when that deletion preserves total length; equivalently, the deleted point lies on a geodesic between its two neighbors. We use integer coefficients and the Euclidean metric. The length parameter is the real number \(\ell=4\sqrt2\).

## Proof

Write \(\bar A\) for the corner opposite \(A\). Among distinct points of \(X\), the distances are \(2\) and \(2\sqrt2\). A two-edge chain of total length \(4\sqrt2\) must therefore use two diagonals. Since each corner has exactly one opposite corner, the only such chains are

\[
\sigma_A=(A,\bar A,A),\qquad A\in\{A,B,C,D\}.
\]

There are exactly four. Each has zero boundary: its endpoints coincide, so its middle entry is not geodesic between them. Every three-edge chain in \(X\) has length at least \(6>4\sqrt2\), hence \(\mathrm{MC}_{3,4\sqrt2}(X)=0\). It follows that \(\mathrm{MH}_{2,4\sqrt2}(X;\mathbb Z)\cong\mathbb Z^4\), with basis \([\sigma_A]\).

In \(Y\), the additional distances are \(d(O,A)=\sqrt2\) for each corner. A two-edge chain of length \(4\sqrt2\) still must consist of two diagonal edges, so the same four \(\sigma_A\) form the entire degree-two chain group at this length, and its differential is zero.

For each corner \(A\), consider the three-edge chain

\[
\tau_A=(A,O,\bar A,A).
\]

Its length is \(\sqrt2+\sqrt2+2\sqrt2=4\sqrt2\). The center \(O\) lies on the diagonal segment from \(A\) to \(\bar A\), so deleting \(O\) preserves length and contributes \(-\sigma_A\) to the boundary. Deleting \(\bar A\) does not preserve length, and endpoint deletions cannot preserve the positive total length. Consequently \(\partial\tau_A=-\sigma_A\). Every basis element of \(\mathrm{MC}_{2,4\sqrt2}(Y)\) is therefore a boundary, and \(\mathrm{MH}_{2,4\sqrt2}(Y;\mathbb Z)=0\). The inclusion sends each source generator to a boundary, proving \(i_*=0\).

## Verification

The standalone checker `verify_square_center.py` represents each distance exactly as \(a+b\sqrt2\) with integers \(a,b\), enumerates the relevant tuples in both spaces, and checks the four source generators and their explicit boundary certificates. Running `python verify_square_center.py` prints three `PASS` lines. The proof above is finite and exact; it does not rely on floating-point rank calculations.

## Relationship to prior work

Bi, Feng, Li, and Wu introduce persistent magnitude homology for finite metric spaces and discuss the role of maps induced by isometric inclusions. Their Example 4.7 illustrates a degree-one change under a point perturbation; it does not give this degree-two isometric extension or its exact groups. The present claim is the specific square-and-center calculation, not a general theorem about injectivity of magnitude-homology maps.

## Limitations

The result concerns one finite metric inclusion and one homological degree and length. It does not classify other isometric inclusions, other bidegrees, or the full weighted barcode of a general metric filtration. Independent external validation has not been performed.

## References

1. W. Bi, H. Feng, J. Li, and J. Wu, *Persistent magnitude homology on finite metric spaces*, arXiv:2601.03685v1 (first posted 2026-01-07), Sections 2.1–2.2 and Example 4.7.
2. R. Hepworth and S. Willerton, *Categorifying the magnitude of a graph*, *Homology, Homotopy and Applications* 19(2) (2017), 31–60, DOI 10.4310/HHA.2017.v19.n2.a3.

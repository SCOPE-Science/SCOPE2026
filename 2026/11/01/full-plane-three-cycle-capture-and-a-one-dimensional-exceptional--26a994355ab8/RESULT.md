# Full-plane three-cycle capture and a one-dimensional exceptional set in an absolute-value map

## Finding
For every irrational \(b\in[10,\infty)\), the planar continuous piecewise-affine map
\[
F_b(x,y)=(|x|-y-1,\;x-|y|+b)
\]
has a full-Lebesgue-measure basin whose points enter the three-cycle
\[
\mathcal X_b=\{(-b,1),(b-2,-1),(b-2,2b-3)\}
\]
in **finite** time. This basin contains an open dense subset of the entire plane. Every point outside it eventually enters the distinct three-cycle
\[
\mathcal Q_b=\left\{\left(\frac{2-b}{3},-1\right),\left(\frac{b-2}{3},\frac{2b-1}{3}\right),\left(-\frac{b+4}{3},\frac{2b-1}{3}\right)\right\}.
\]
The exact exceptional basin \(E_b=\bigcup_{n\ge0}F_b^{-n}(\mathcal Q_b)\) is contained in countably many straight lines, includes a nondegenerate ray, and therefore has Hausdorff dimension **exactly one**. This supplies a full-plane, rather than merely invariant-graph, basin statement for an uncountable full-parameter-measure region of the three-cycle regime.

## Assumptions and scope
The parameter is a fixed irrational real \(b\ge10\). All assertions are for the original two-dimensional map on \(\mathbb R^2\), with planar Lebesgue measure and Euclidean Hausdorff dimension. A forward orbit *enters a cycle* if some finite iterate is exactly one of its three points; no asymptotic approach assumption is substituted for finite entry. The two displayed cycles are distinct in the specified parameter range. We use the published global finite-time capture theorem for a compact invariant graph and the graph-dynamics classification for \(b\ge10\), both for the normalization \(a=-1\) [1, Theorem B and Proposition 41]. Those quoted premises are not asserted as new here.

## Proof
**Step 1: Reduction to the two cycles.** Direct substitution shows both displayed triples are three-cycles. By [1, Theorem B], every planar orbit reaches a compact invariant graph \(\Gamma_b\) in finite time. By [1, Proposition 41], for \(b\ge10\), every point of \(\Gamma_b\setminus\mathcal Q_b\) reaches \(\mathcal X_b\) in finite time, and the only other graph orbit is \(\mathcal Q_b\). Consequently every planar point reaches precisely one of the two cycles. Thus the complement of the finite-entry basin of \(\mathcal X_b\) is exactly
\[
E_b=\bigcup_{n\ge0}F_b^{-n}(\mathcal Q_b).
\]

**Step 2: Integer-affine itinerary obstruction.** For every nonnegative integer \(n\), \(F_b^n\) has a finite polyhedral partition into full-dimensional affine cells (plus their lower-dimensional boundaries). On every cell it has a formula
\[
F_b^n(z)=M z+u+bv,\qquad M\in\operatorname{Mat}_{2\times2}(\mathbb Z),\quad u,v\in\mathbb Z^2.
\]
Indeed each quadrant restriction is affine with integral linear coefficients and translation \((-1,b)\); compositions preserve this form. For irrational \(b\), none of the three points of \(\mathcal Q_b\) belongs to \((\mathbb Z+b\mathbb Z)^2\), since its first coordinate contains \(b\) with coefficient \(1/3\) or \(-1/3\). If \(M=0\), the entire cell is mapped to \(u+bv\), hence cannot be mapped to any point of \(\mathcal Q_b\). If \(M\ne0\), the preimage of any given point under the cell formula lies in an affine subspace of dimension at most one. For the cell boundaries, which lie in a finite union of straight lines, the same dimension bound is immediate. It follows that \(F_b^{-n}(\mathcal Q_b)\) is contained in a **finite** union of affine lines for every \(n\). Consequently \(E_b\) is contained in countably many affine lines, has planar measure zero, and has Hausdorff dimension at most one.

**Step 3: Sharp lower dimension.** Every point of the ray
\[
L_b=\left\{\left(s,s+\frac{b+1}{3}\right):s>0\right\}
\]
lies in the first quadrant and maps in one step to \(\bigl(-(b+4)/3,(2b-1)/3\bigr)\in\mathcal Q_b\). Thus \(L_b\subset E_b\), and the Hausdorff dimension of \(E_b\) is at least one. This proves the exact dimension.

**Step 4: An open dense full-measure basin core.** For each \(n\), the set of points with \(F_b^n(z)\in\mathcal X_b\) that lie in the interior of an affine cell with positive-rank linear part has planar measure zero: on such a cell the inverse image of each of the three target points is at most one-dimensional. Affine partition boundaries also have measure zero. Hence, up to a null set, every point that enters \(\mathcal X_b\) does so through a **full-dimensional cell on which \(F_b^n\) is constant** and equal to a point of \(\mathcal X_b\). The union \(\mathcal O_b\) of the interiors of all these constant-image cells, over all \(n\), is open, is contained in the finite-entry basin, and has full planar Lebesgue measure because that basin is the complement of the null set \(E_b\). Every nonempty open disk has positive area, so \(\mathcal O_b\) is dense. This finishes the proof.

## Verification
Each branch formula follows from a finite composition of four matrices with integer entries and translation \((-1,b)\), and the arithmetic obstruction concerns coefficients of \(b\), not numerical approximations. The separate standalone checker `check.py` verifies exact symbolic cycle identities, the affine ray-to-cycle identity, the four branch matrices, and sample affine-word coefficients using rational-in-\(b\) symbolic arithmetic. These finite calculations support the algebraic base cases only; the induction over all lengths and dimension statements are proved above. The main published premises were checked in [1, Theorem B and Proposition 41].

## Relationship to prior work
Cima, Gasull, Mañosa and Mañosas [1] classify the graph dynamics of this family. Their Theorem B captures every plane orbit on a graph and Proposition 41 identifies its two three-cycles when \(b\ge10\). Their Section 6 explicitly asks whether the plateau-limit behavior holds on an open dense or full-planar-measure set. The new result answers these planar basin questions for the irrational half-line \(b\ge10\) and identifies the exact exceptional Hausdorff dimension. The subsequent paper [2, Theorem 2] proves graphwise full-measure results on other parameter intervals; a one-dimensional graphwise assertion does not imply the present planar nullity because rank-zero branches can send planar open sets to points. The proof supplies an arithmetic obstruction to precisely that obstacle. Prior related classifications of local survivor areas for other parameter regimes do not imply the global result.

## Limitations
The argument excludes rational \(b\) even though the same basin conclusion may remain true there. It does not classify the precise line arrangement, the number of exceptional preimage components, or their length growth. No claim is made about parameter values below ten or about measure-theoretic rates of capture. Independent validation and comprehensive publication-priority review have not been performed.

## References
[1] A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052 (first public 2024-10-01), published *Qualitative Theory of Dynamical Systems* 24 (2025), article 70. https://arxiv.org/abs/2410.01052 ; https://doi.org/10.1007/s12346-025-01221-1 .

[2] A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Further results for a family of continuous piecewise linear planar maps*, arXiv:2503.02411 (first public 2025-03-04), Theorem 2. https://arxiv.org/abs/2503.02411 .

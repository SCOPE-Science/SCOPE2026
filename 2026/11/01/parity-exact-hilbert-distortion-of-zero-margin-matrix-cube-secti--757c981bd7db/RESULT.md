# Parity-exact Hilbert distortion of zero-margin matrix cube sections

## Finding
For all integers \(n,m\ge2\), let
\[
W_{n,m}=\left\{A\in\mathbb R^{n\times m}:\ \sum_{j=1}^{m}A_{ij}=0\ \text{for every }i,\quad\sum_{i=1}^{n}A_{ij}=0\ \text{for every }j\right\}
\]
with the entrywise maximum norm \(\|A\|_{\infty}=\max_{i,j}|A_{ij}|\). This space has real dimension \(d=(n-1)(m-1)\). Its multiplicative Banach--Mazur distance to Euclidean space is exactly
\[
\boxed{d_{\mathrm{BM}}(W_{n,m},\ell_2^d)^2=\frac{(n-1)(m-1)}{nm}\,M(n,m)},
\]
where
\[
M(n,m)=\begin{cases}
nm,&n,m\text{ even},\\
n(m-1),&n\text{ even},\ m\text{ odd},\\
m(n-1),&n\text{ odd},\ m\text{ even},\\
nm-\max\{n,m\},&n,m\text{ odd}.
\end{cases}
\]
The restricted Frobenius norm is an optimal Euclidean comparison norm. In particular, for even \(n,m\), the distance equals \(\sqrt d\), the maximal dimension-dependent upper bound, whereas each odd side produces a strict parity loss. Explicit matrices attain all extremal norm ratios.

## Assumptions and scope
All scalars and isomorphisms are real. The norm \(\|\cdot\|_\infty\) is the **entrywise** maximum norm, not the induced matrix operator norm. For any \(d\)-dimensional real normed spaces \(X,Y\), \(d_{\mathrm{BM}}(X,Y)=\inf_{T:X\to Y\ \mathrm{invertible}}\|T\|\,\|T^{-1}\|\). We require strictly \(n,m\ge2\), with no other assumption on parity or relative size. The result concerns the simultaneous zero-row-sum and zero-column-sum constraints; it is not a formula for an arbitrary linear subspace or for the transportation-cost norm on the graph with the same bipartition.

## Proof
**Step 1: symmetry determines an optimal Hilbert norm.** Consider any positive-definite quadratic form \(Q\) on \(W_{n,m}\) with distortion at most \(D\). By multiplying \(Q\) by a positive constant, assume
\[
\|A\|_\infty^2\le Q(A)\le D^2\|A\|_\infty^2\quad(A\in W_{n,m}).
\]
Independent row and column permutations preserve both the space and its maximum norm. Average \(Q\) over \(S_n\times S_m\); the resulting positive-definite quadratic form satisfies the same inequalities. Any invariant bilinear form is a linear combination of the sums of \(A_{ij}B_{k\ell}\) over pairs sharing both coordinates, sharing only the row, sharing only the column, or sharing neither. On \(W_{n,m}\), the latter three types vanish after expansion using the zero-margin constraints, leaving a constant multiple of \(\sum_{i,j}A_{ij}B_{ij}\). Thus the averaged form equals \(c\|A\|_F^2\) for some \(c>0\), and the restricted Frobenius norm is globally optimal among **all** Hilbertian comparison norms.

**Step 2: exact minimum Frobenius radius of the maximum-norm unit sphere.** The Frobenius-orthogonal projection from \(\mathbb R^{n\times m}\) onto \(W_{n,m}\) is
\[
\Pi(B)=\left(I_n-\tfrac1n\mathbf1_n\mathbf1_n^{\mathsf T}\right)B\left(I_m-\tfrac1m\mathbf1_m\mathbf1_m^{\mathsf T}\right).
\]
For each coordinate functional \(L_{ij}(A)=A_{ij}\), its squared dual Frobenius norm on the subspace equals \(\|\Pi E_{ij}\|_F^2=(1-1/n)(1-1/m)\). By Cauchy--Schwarz, with equality for the normalized matrix \(\Pi E_{ij}\),
\[
\max_{\|A\|_F=1}\|A\|_\infty^2=\frac{(n-1)(m-1)}{nm}=:\kappa_{n,m}.
\]
Equivalently \(\min_{\|A\|_\infty=1}\|A\|_F^2=1/\kappa_{n,m}\).

**Step 3: exact maximum Frobenius radius.** Let \(R^2=\max\{\|A\|_F^2:A\in W_{n,m},\ \|A\|_\infty\le1\}\). For an even length \(s\), a zero-sum vector \(x\in[-1,1]^s\) satisfies \(\sum x_i^2\le s\). For an odd length \(s\), the sharper bound \(\sum x_i^2\le s-1\) holds: the convex sum of squares attains a maximum at a vertex of the hyperplane section of the cube, where at least \(s-1\) coordinates are saturated; because \(s-1\) is even, the remaining coordinate must equal \(0\), and cancellation forces equally many positive and negative signs. Summing the corresponding row and column inequalities gives
\[
R^2\le\begin{cases}
nm,&n,m\text{ even},\\
n(m-1),&n\text{ even},\ m\text{ odd},\\
m(n-1),&n\text{ odd},\ m\text{ even},\\
\min\{n(m-1),m(n-1)\},&n,m\text{ odd}.
\end{cases}
\]
The last minimum is \(nm-\max\{n,m\}\).

Every upper bound is attained. With two even sides, use the checkerboard \(A_{ij}=(-1)^{i+j}\). With exactly one odd side, set its final row or column to zero and put a checkerboard in the remaining even-by-even rectangle. With both sides odd, by transposition suppose \(n\le m\). On the first \(n\) columns, define a circulant \(n\)-by-\(n\) matrix with entries zero on the diagonal, plus one for the next \((n-1)/2\) cyclic offsets and minus one for the remaining offsets. This has zero margins and \(n(n-1)\) nonzero entries. Since \(m-n\) is even, add columns in pairs \(v,-v\), where \(v\in\{-1,0,1\}^n\) has one zero and equally many plus and minus entries. Every new column has zero sum and every new pair preserves all row sums. The resulting matrix has \(n(n-1)+(m-n)(n-1)=m(n-1)\) nonzero entries and unit maximum norm. Therefore \(R^2=M(n,m)\) in all cases.

**Step 4: exact distance and sharpness.** The best Frobenius comparison has squared distortion
\[
\frac{\max_{\|A\|_\infty=1}\|A\|_F^2}{\min_{\|A\|_\infty=1}\|A\|_F^2}=\kappa_{n,m}M(n,m).
\]
Step 1 excludes any better Euclidean position. The matrices in Steps 2 and 3 attain the two ratios, proving the exact formula with both endpoints realized. For even \(n,m\), \(\kappa_{n,m}M(n,m)=(n-1)(m-1)=d\). In each remaining parity case \(M(n,m)<nm\), giving a strict loss from that maximal bound. \(\square\)

## Verification
Execute `python3 verification/check.py` from this package root using Python's standard library. It independently constructs every parity-family extremizer for all \(2\le n,m\le25\), checks both margin constraints, their exact square counts, and the projected coordinate squared norm as rational numbers. It also enumerates all \(3^9\) ternary matrices in the \(3\)-by-\(3\) instance to independently confirm the sharp discrete value \(6\). Expected output: `VERIFY_OK witness_and_projection_checks=4033 exhaustive_ternary_3x3_maximum=6`. These computations only corroborate the analytic all-size proof; they do not claim to enumerate all real feasible matrices.

## Relationship to prior work
Passer's finite-dimensional approximate Jordan--von Neumann theorem develops general Euclidean Banach--Mazur comparisons, without a two-margin matrix classification [1]. Hinrichs and Schneider treat equivalence of anchored and ANOVA function spaces using interpolation [2]; their functional-analytic decomposition motivates viewing the present zero-margin matrices as pure two-factor interactions but does not calculate their exact Hilbert distance. Existing published computations of the real zero-sum \(\ell_\infty^s\) hyperplane, appearing as the Lipschitz dual of a graph cycle [3], determine the one-margin factor but do not imply a complete classification for matrices constrained in **both** directions. The separately studied complete-bipartite transportation spaces have dimension \(n+m-1\), unlike the present \((n-1)(m-1)\)-dimensional cycle/interaction subspace, and carry a different norm [4]. A general result about symmetric cube sections or Banach tensor products might imply the formula in another language; this is a remaining bibliographic risk.

## Limitations
The proof uses real scalars, the unweighted entrywise maximum norm, full rectangular Cartesian grids, and both sets of unweighted zero-margin conditions. It does not classify weighted margin constraints, complex scalars, sparse bipartite cycle spaces, other matrix norms, or uniqueness of the optimal Euclidean quadratic form. Published coverage by a stronger abstract theorem remains possible. The result has received self-review only; no independent scientific audit has been performed.

## References
[1] Benjamin Passer, *An Approximate Version of the Jordan von Neumann Theorem for Finite Dimensional Real Normed Spaces*, arXiv:1305.3546, first posted 2013-05-13; Sections 1–3, especially Theorems 2.9 and 3.4.

[2] Aicke Hinrichs and Jan Schneider, *Equivalence of anchored and ANOVA spaces via interpolation*, arXiv:1503.08933, first posted 2015-03-31; introduction and interpolation comparisons.

[3] *Scalar-field parity in Euclidean distortion of cycle transportation spaces*, published open scientific result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-scalar-field-parity-in-euclidean-distortion-of-cycle-transportat--13d7bdc76366 ; Finding and Steps 1–5 of proof.

[4] *Maximal Hilbert distortion for complete-bipartite transportation spaces*, published open scientific result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-maximal-hilbert-distortion-for-complete-bipartite-transportation--203c5ca21810 ; Finding and Assumptions and scope.

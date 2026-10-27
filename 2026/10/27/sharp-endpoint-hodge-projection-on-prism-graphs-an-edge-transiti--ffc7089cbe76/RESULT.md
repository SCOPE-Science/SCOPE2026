# Sharp endpoint Hodge projection on prism graphs: an edge transition and a log-periodic defect

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\square K_2\) be the unweighted prism (circular ladder) graph, with \(3n\) undirected edges and unit edge-counting measure. Let \(P_n\) be the Euclidean orthogonal projection of real edge flows onto the subspace of vertex-potential gradients. The result gives its **sharp** operator norm on \(\ell^\infty(E(G_n))\), including the maximizing edge orbit and the full order-\(1/n\) lattice-phase correction.

Put
\[
q=2+\sqrt3,\quad r=q^{-1}=2-\sqrt3,\quad L=\log q,\quad m=\lfloor n/2\rfloor,
\qquad g_j=\frac{r^j+r^{n-j}}{2\sqrt3\,(1-r^n)}\quad(0\le j<n),\quad \Delta_n=g_0-g_m.
\]
Define
\[
H_n=1-\frac1n+\sum_{j=1}^{n-1}\max\!\left\{\frac1n,2g_j\right\}+2\Delta_n,
\qquad V_n=1+4\Delta_n.
\]
Then
\[
\boxed{\|P_n\|_{\infty\to\infty}=\max\{H_n,V_n\}},\qquad
\begin{cases}
\|P_3\|_{\infty\to\infty}=V_3=9/5>H_3=26/15,\\
\|P_4\|_{\infty\to\infty}=H_4=V_4=2,\\
\|P_n\|_{\infty\to\infty}=H_n>V_n & (n\ge5).
\end{cases}
\]
Every displayed norm is attained by a sign-valued input. In particular \(\|P_n\|_{\infty\to\infty}<3\) for every finite \(n\), but \(\lim_{n\to\infty}\|P_n\|_{\infty\to\infty}=3\).

More precisely, write \(\beta_n=\log_q(n/\sqrt3)\), \(\{x\}=x-\lfloor x\rfloor\), and the continuous period-one function \(F\) on \([0,1]\) as
\[
F(u)=2+(\sqrt3-1)q^u-2u-\frac{\log3}{L},\quad F(1)=F(0).
\]
Then the **uniform-in-phase sharp expansion** is
\[
\boxed{n\bigl(3-\|P_n\|_{\infty\to\infty}\bigr)-\frac{2\log n}{L}
=F(\{\beta_n\})+o(1).}
\]
The sequence on the left does **not** converge: its exact limsup is \(F(0)\), and its exact liminf is \(F(u_*)\), where
\[
u_* =\frac1L\log\!\left(\frac{2}{(\sqrt3-1)L}\right)\in(0,1).
\]
Numerically these limits are approximately \(1.8978462432\) and \(1.5762442666\), respectively. Thus even after removal of the leading \((\log n)/n\) defect, a nonzero periodic lattice fluctuation survives.

## Assumptions and scope
The graph is simple, with \(n\ge3\), two copies of the length-\(n\) cycle and one rung between each pair of corresponding vertices. Each of the \(3n\) edges carries one real coordinate; arbitrary orientations are harmless, because reversing an orientation changes row and column signs. The gradient space is \(\operatorname{im}B\), where \(B\) is the \((3n)\times(2n)\) signed vertex-edge incidence matrix; \(P_n=B(B^TB)^+B^T\). The norm is the induced coordinate maximum norm \(\ell^\infty\to\ell^\infty\), not the Hilbert operator norm (which equals one). A maximizer may depend on the output edge.

## Proof
**1. Exact Green function.** Let \(D\) be the forward difference incidence of the cycle, and \(L_C=D^TD=2I-S-S^{-1}\). Decompose the two rails into the symmetric and antisymmetric vertex modes. Their Laplacians are \(L_C\) and \(L_C+2I\), respectively. The inverse of the second is the circulant \(G=(g_{i-j})\); the stated geometric formula solves \((4I-S-S^{-1})g=\delta_0\), because \(r+r^{-1}=4\). Summing this equation gives \(\sum_{j=0}^{n-1}g_j=1/2\). Symmetry and the explicit geometric formula show \(g_0\ge g_1\ge\cdots\ge g_m>0\), with an equal midpoint pair when \(n\) is odd.

**2. All transfer-current entries.** On cycle-edge coordinates,
\[
D L_C^+D^T=I-J/n,\qquad D(L_C+2I)^{-1}D^T=I-2G,
\]
where \(J\) is the all-ones \(n\times n\) matrix. Accordingly, up to orientation signs, the horizontal-to-horizontal blocks of \(P_n\) are \(I-J/(2n)-G\) on the same rail and \(G-J/(2n)\) between rails. The two horizontal-to-rung blocks are opposite signed copies of \(DG\); the rung-to-rung block is \(2G\). The identity \(DG\) uses the same forward-difference orientation on both rails.

**3. Sharp row sums and orbit transition.** For a horizontal output edge, the same- and opposite-rail absolute coefficients at offset zero sum to \(1-1/n\), while at nonzero offset \(j\) they sum to \(\max\{1/n,2g_j\}\). The mixed rung coefficients contribute \(\sum_j|g_j-g_{j+1}|=2(g_0-g_m)\), proving its row sum is \(H_n\). For a rung output edge, the rung-to-rung coefficients contribute \(2\sum_jg_j=1\), and the two horizontal rails contribute \(4(g_0-g_m)\), proving \(V_n\). All horizontal edges have the same row sum by symmetry, as do all rungs. The maximum absolute row sum is the induced \(\ell^\infty\) norm; choosing the input signs to match a maximizing row gives exact attainment.

Direct substitution gives \(H_3=26/15\), \(V_3=9/5\), and \(H_4=V_4=2\). For \(n\ge5\), since \(\max\{1/n,2g_j\}\ge1/n\),
\[
H_n-V_n\ge1-\frac2n-2\Delta_n.
\]
The explicit Green formula gives \(0<\Delta_n<1/(2\sqrt3)\): for even \(n=2m\), \(\Delta_n=(1-r^m)/[2\sqrt3(1+r^m)]\); for odd \(n=2m+1\), \(\Delta_n=(1-r^m)(1-r^{m+1})/[2\sqrt3(1-r^{2m+1})]\). Thus \(H_n-V_n>1-2/n-1/\sqrt3>0\) for \(n\ge5\), establishing the sole edge-orbit transition.

**4. Exact cutoff and leading asymptotic.** Put \(a_j=2g_j\). For sufficiently large \(n\), strict monotonicity up to \(m\) provides an integer \(k_n<m\) such that \(a_j\ge1/n\) exactly for offsets of cyclic distance at most \(k_n\), excluding distance zero from the count. Rewriting every maximum as \(a_j+(1/n-a_j)_+\), using \(\sum_ja_j=1\), gives the exact positive-defect formula
\[
3-H_n=\frac{2k_n+2}{n}+2g_m+
\frac{2r^{k_n+1}(1-r^{n-2k_n-1})}{\sqrt3(1-r)(1-r^n)}.
\]
The cutoff inequality \(a_{k_n}\ge1/n>a_{k_n+1}\), together with the geometric Green formula, yields \(k_n=(\log n)/L+O(1)\); also \(ng_m\to0\). Therefore \(3-H_n=2\log n/(nL)+O(1/n)\), and the positive-defect formula proves \(H_n<3\) for large \(n\). In fact the same formula, or its direct ungrouped version, works for each smaller \(n\); it and \(V_n<1+2/\sqrt3<3\) show all finite norms are below three.

**5. Nonconstant logarithmic phase.** Set \(\beta_n=\log_q(n/\sqrt3)\), \(b_n=\lfloor\beta_n\rfloor\). For all sufficiently large \(n\), \(k_n\in\{b_n,b_n+1\}\): at distance \(b_n\) the leading term of \(na_j\) is at least one, while at distance \(b_n+2\) it is at most \(q^{-1}\) times a factor tending to one. The alternative \(k_n=b_n+1\) occurs only when \(\{\beta_n\}\to1\), because the finite-cycle image term is exponentially small for distances \(O(\log n)\). The endpoint equality \(F(0)=F(1)\) makes this exceptional rounding harmless.

Multiplying the exact defect identity by \(n\), the geometric tail contributes
\[
\frac{2nr^{k_n+1}}{\sqrt3(1-r)}+o(1)
=(\sqrt3-1)q^{\beta_n-k_n}+o(1).
\]
The integer term is \(2k_n+2\); subtracting \(2\log n/L=2\beta_n+\log3/L\) gives the stated continuous periodic function \(F\), with an \(o(1)\) error along *all* integers \(n\to\infty\).

The function \(F\) is strictly convex on \([0,1]\), its derivative is \((\sqrt3-1)Lq^u-2\), and it has the unique interior minimum at \(u_*\); the maximum on this interval is at both endpoints. For any \(u\in[0,1]\), integers closest to \(\sqrt3q^{j+u}\) have \(\{\beta_n\}\to u\) as \(j\to\infty\) (interpreting \(u=1\) periodically). Thus the limsup and liminf are attained as subsequential limits and are distinct. This completes the proof.

## Verification
The standalone `verify_prism.py` constructs exact rational graph incidence matrices and independently inverts the vertex Laplacian for every \(3\le n\le12\). It verifies orthogonal idempotence, both row orbits, the Green recurrence and mass, finite norm inequalities, and the special cases. It also performs supplementary floating-point checks of the phase formula at six larger sizes. The successful run contains 539 assertions. These finite computations are consistency tests; the proof of the all-\(n\) norm, transition and asymptotic oscillation is the analysis above. Reproduce with `python verify_prism.py` and SymPy.

## Relationship to prior work
Jiang, Lim, Yao and Ye (2008 preprint, published 2010/11) formulate least-squares gradient projection of graph edge flows. Kassel and Wu (2013) develop the transfer-current perspective. Cinkir (2016/17) supplies effective-resistance calculations for open ladders and prisms; all-pair resistance data can in principle recover transfer currents by polarization. None of these general frameworks is claimed as new, nor is the geometric-cycle Green function. The specific result here is the sharp **edge-orbit selection**, the exact endpoint amplification, and its nonconvergent order-\(1/n\) logarithmic-phase correction. The related prism-resistance paper's full text was not obtainable in this examination, so priority against any equivalent unstated consequence remains a residual risk.

## Limitations
The result concerns real, unweighted, finite prism graphs and the specific Euclidean edge-gradient projection. It does not classify weighted prisms, other graph products, arbitrary projection choices, or \(\ell^p\)-norms. The log-periodic expansion is asymptotic, not an exact finite-size identity; its exact finite precursor is the cutoff formula. The literature comparison is based on accessible primary material and recorded search results, not an independent historical-priority certification.

## References
- X. Jiang, L.-H. Lim, Y. Yao and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067 (first version 2008-11-07); *Mathematical Programming* 127 (2011), 203–244. https://doi.org/10.1007/s10107-010-0419-x
- A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946 (2013).
- Z. Cinkir, *Effective Resistances and Kirchhoff Index of Ladder Graphs*, *Journal of Mathematical Chemistry* 54 (2016), 955–966. https://doi.org/10.1007/s10910-016-0597-8
- Z. Cinkir, *Effective Resistances and Kirchhoff index of Prism Graphs*, arXiv:1704.03429 (2017).

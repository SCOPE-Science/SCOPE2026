# Quadratic page-count threshold for retaining a shortcut in optimal-resistance book networks

## Finding

For the \(m\)-page book network \(G_m=K_2\vee\overline{K_m}\), optimize every edge conductance independently to minimize the sum of pairwise electrical effective resistances under a linear expenditure constraint. When both spoke families have the same positive price \(S\) and the direct hub-to-hub edge has positive price \(R\), the global optimum deletes the direct edge exactly when

\[
R\ge R_c(m,S):=\frac{8S(m+2)}{m^3+m^2+2m+4}.
\]

Every spoke retains positive conductance. In particular, when all prices are equal, the direct edge is retained for \(m=2\), whereas it is deleted for every \(m\ge3\). The cutoff is asymptotically \(8S/m^2\), exhibiting a quadratic page-count law. Explicit conductances and the exact optimal total resistance are given below.

## Assumptions and scope

Take an integer \(m\ge2\). The vertices are two hubs \(u,v\) and \(m\) distinct page vertices \(a_1,\ldots,a_m\). The graph has the direct edge \(uv\) and, for each page, edges \(ua_i,va_i\); there are no page-to-page edges. Assign to each spoke a per-unit price \(S>0\) and to \(uv\) price \(R>0\). There is a budget \(B>0\). Any nonnegative independent edge conductances \(w_e\) satisfying \(S\sum_{e\ne uv}w_e+Rw_{uv}=B\) are allowed, not just symmetric allocations. Disconnected allocations are assigned infinite objective.

Write \(L(w)\) for the weighted combinatorial graph Laplacian, \(L(w)^\dagger\) for its Moore–Penrose pseudoinverse, and \(n=m+2\). The total effective resistance is

\[
\mathcal K(w)=\sum_{i<j}(e_i-e_j)^{\mathsf T}L(w)^\dagger(e_i-e_j)
=n\operatorname{tr}(L(w)^\dagger).
\]

Define the dimensionless constants

\[
K_m=\frac{m^2(m+1)}{2(m+2)},\qquad
k=\frac{4S}{R}-1,\qquad
R_c=\frac{4S}{K_m+1}.
\]

The optimum has the same conductance \(t_*>0\) on every one of the \(2m\) spokes and direct conductance \(z_*\ge0\). It is fully explicit:

\[
(t_*,z_*)=
\begin{cases}
\left(\dfrac{B}{2mS},0\right),&R\ge R_c,\\[2mm]
\left(\dfrac{B(1-y_*)}{2mS},\dfrac{By_*}{R}\right),&0<R<R_c,
\end{cases}
\]

where in the second case \(k>K_m>0\) and

\[
y_*=\frac{\sqrt{k}-\sqrt{K_m}}{k\sqrt{K_m}+\sqrt{k}}\in(0,1).
\]

The minimized total effective resistance is

\[
\mathcal K_*=(m+2)\frac{2S}{B}
\begin{cases}
K_m+1,&R\ge R_c,\\[1mm]
\dfrac{(\sqrt{K_m k}+1)^2}{k+1},&0<R<R_c.
\end{cases}
\]

The formulas agree continuously at equality. All assertions cover every \(m\ge2\) and all positive \(S,R,B\).

## Proof

**Unrestricted uniqueness and symmetry.** On the subspace perpendicular to the all-ones vector, write \(A(w)=L(w)|_{\mathbf1^\perp}\). On connected feasible allocations, \(A(w)\) is positive definite and the minimized objective is proportional to \(F(w)=\operatorname{tr}(A(w)^{-1})\). Given a nonzero conductance perturbation \(h\), the induced perturbation \(H=A(h)\ne0\) because the original graph is simple and each off-diagonal Laplacian entry identifies its edge weight. Along any line in the connected positive-definite domain,

\[
\frac{d^2}{ds^2}F(w+sh)\bigg|_{s=0}
=2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0.
\]

The strict sign follows by expressing the trace as \(2\operatorname{tr}(A^{-1/2}(A^{-1/2}HA^{-1/2})^2A^{-1/2})\). Thus \(F\) is strictly convex. The compact budget polytope contains connected allocations. Approaching a disconnected allocation forces a nonzero Laplacian eigenvalue to vanish, so \(F\to\infty\); hence a unique connected minimizer exists. Hub exchange and arbitrary page permutations preserve prices, constraints and the objective. Uniqueness therefore forces all \(2m\) spoke conductances to equal some \(t>0\), with \(uv\) conductance \(z\ge0\). This is a conclusion from unrestricted optimization, not a symmetry assumption.

**Spectrum and budget reduction.** In this symmetric family, the nonzero Laplacian eigenvalues are \(2t\) with multiplicity \(m-1\), \((m+2)t\) with multiplicity one, and \(mt+2z\) with multiplicity one. The first family consists of zero-sum page fluctuations, the second of a hub-common-versus-page mode, and the last of hub antisymmetry. Consequently,

\[
\operatorname{tr}(L^\dagger)=\frac{m-1}{2t}+\frac1{(m+2)t}+\frac1{mt+2z}
=\frac{m(m+1)}{2(m+2)t}+\frac1{mt+2z}.
\]

Set \(y=Rz/B\), the fraction of expenditure devoted to the hub edge. The full budget gives \(t=B(1-y)/(2mS)\) and \(0\le y<1\). Substitution yields the strictly convex one-variable objective

\[
F(y)=\frac{2S}{B}\left(\frac{K_m}{1-y}+\frac1{1+ky}\right),\qquad
k=\frac{4S}{R}-1>-1.
\]

Its denominators are positive over \(0\le y<1\). Differentiating,

\[
\frac{B}{2S}F'(y)=\frac{K_m}{(1-y)^2}-\frac{k}{(1+ky)^2},
\quad
\frac{B}{2S}F''(y)=\frac{2K_m}{(1-y)^3}+\frac{2k^2}{(1+ky)^3}>0.
\]

The derivative at the feasible boundary \(y=0\) equals \((2S/B)(K_m-k)\). Hence the unique minimum occurs at \(y=0\) exactly when \(k\le K_m\), which is \(R\ge4S/(K_m+1)\). Otherwise \(k>K_m>0\), and the unique interior stationary equation is

\[
\frac{\sqrt{K_m}}{1-y}=\frac{\sqrt{k}}{1+ky}.
\]

Solving gives the stated \(y_*\), which lies strictly between zero and one. The remaining conductance formulas follow from the budget. Substitution into \(F\) gives \(F_*=(2S/B)(\sqrt{K_m k}+1)^2/(k+1)\) in the interior, and \(F_*=(2S/B)(K_m+1)\) at the boundary. Multiplication by \(m+2\) produces the exact Kirchhoff index.

**Size and boundary consequences.** At \(R=S\), one has \(k=3\). Direct arithmetic gives \(K_2=3/2<3\) and \(K_3=18/5>3\); moreover \(K_m\) increases for \(m\ge2\). Thus the direct edge survives exactly at \(m=2\). The cutoff expression simplifies to \(R_c/S=8(m+2)/(m^3+m^2+2m+4)\sim8/m^2\). At fixed \(m,S,B\), as \(R\uparrow R_c\) from below, \(y_*\sim(R_c-R)/(2K_mR_c)\), hence \(z_*\sim B(R_c-R)/(2K_mR_c^2)\). As \(R\downarrow0\), the optimal hub conductance grows as \(B/(2\sqrt{K_m S R})\), while its budget share vanishes as \(\sqrt R/(2\sqrt{K_m S})\).

## Verification

The included `verify_book_resistance.py` is standalone Python source requiring NumPy and SciPy. Run with `python verify_book_resistance.py` in the directory containing the file. Its exact-rational Gaussian inversions compare \(\operatorname{tr}(L^\dagger)\) against the spectral formula for \(15\) cases, including a deleted direct edge. Additional runs checked \(49\) budget/spectral identities, \(49\) support-threshold decisions, \(980\) random asymmetric feasible competitors, \(15\) unrestricted numerical minimization attempts, and the all-equal-price page threshold through \(m=44\). All checks passed at the time of this package. Finite computations support but do not establish the theorem; the proof above establishes all integer page counts and positive parameter ranges.

## Relationship to prior work

Ghosh, Boyd and Saberi introduced convex total-effective-resistance design and described symmetry-based analytical solutions for trees, wheels, and barbell graphs. Their publicly accessible 2006 proceedings and 2008 full paper provide the methodological starting point; the inspected analytic examples do not give this priced book-network support cutoff. General methods for solving an SDP do not themselves imply a closed page-dependent threshold. Literature on unweighted resistance distances for graph joins supplies fixed-conductance spectral information but does not characterize independently allocated conductances under heterogeneous prices. The specific contribution here is the complete unrestricted allocation, its sharp shortcut-deletion price, and its \(m^{-2}\) scaling.

## Limitations

The two spoke classes must have a common price \(S\), while the direct-edge price may differ. The graph is undirected and simple, with no other page connections; no claim is made for unequal individual spoke prices, other objective functions such as the weighted spanning-tree determinant, or disconnected designs. Independent publication-priority verification and external mathematical audit have not been carried out. The proceedings source is dated to a July 2006 conference; the exact first online-release day was not established.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, Kyoto, July 24–28, 2006, pp. 1185–1196. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66. DOI: 10.1137/050645452. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. *Resistance distances and Kirchhoff indices in graph joins*, Journal of Physics A: Mathematical and Theoretical (2025/2026), DOI: 10.1088/1751-8121/ae2997. (Related fixed-weight graph-join comparison; full article access was limited.)

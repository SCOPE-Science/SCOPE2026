# An anomalous two-thirds power law for resistance-optimal circular ladders

## Finding

**Theorem.** Fix an integer \(n\ge3\) and a price \(t>0\). Let \(G_n=C_n\square K_2\) have two copies of an \(n\)-cycle connected by \(n\) corresponding rung edges. The \(2n\) cycle (rim) edges each have price one; the \(n\) rungs each have price \(t\). Assign conductances \(w_e\ge0\) with \(\sum_{e\in E_{\mathrm{rim}}}w_e+t\sum_{e\in E_{\mathrm{rung}}}w_e=1\), and minimize the Kirchhoff index \(K_n=\sum_{u<v}R_{\mathrm{eff}}(u,v)\), taken as infinite for disconnected networks.

The global optimizer is **unique**, positive on every edge, and constant within each edge type, with rim conductance \(a\) and rung conductance \(b\). Define
\[
 \sigma_k=4\sin^2(\pi k/n),\quad A_n=\frac{n^2-1}{12},\quad x=\frac ba.
\]
There is a unique positive solution \(x=x_n(t)\) of
\[
 t\left(A_n+\sum_{k=0}^{n-1}\frac{\sigma_k}{(\sigma_k+2x)^2}\right)
 =4\sum_{k=0}^{n-1}\frac1{(\sigma_k+2x)^2}.
\tag{1}
\]
The unique optimal weights and exact minimum are
\[
 a_n^*=\frac1{n(2+tx_n)},\quad b_n^*=\frac{x_n}{n(2+tx_n)},
\]
\[
 K_n^*(t)=2n^2(2+tx_n)\left(A_n+S_n(x_n)\right),
\quad S_n(x)=\sum_{k=0}^{n-1}\frac1{\sigma_k+2x}.
\tag{2}
\]
The sum has an exact closed form for every \(x>0\):
\[
 S_n(x)=\frac{n}{2\sqrt{x(x+2)}}\coth\!\left(\frac n2\operatorname{arcosh}(1+x)\right).
\tag{3}
\]
For every **fixed** \(t>0\), as \(n\to\infty\), putting \(c_t=(18/t^2)^{1/3}\),
\[
 n^{2/3}x_n(t)\longrightarrow c_t,\quad
 a_n^*\sim\frac1{2n},\quad b_n^*\sim\frac{c_t}{2n^{5/3}},
\tag{4}
\]
\[
 \boxed{K_n^*(t)=\frac{n^4}{3}+\frac{(18t)^{1/3}}2 n^{10/3}+o(n^{10/3}).}
\tag{5}
\]
For comparison, assigning a common conductance to **all** edges has
\(K_n^{\mathrm{uniform}}(t)\sim(2+t)n^4/6\). The difference in leading constants is genuine: the optimal rung budget share tends to zero while maintaining connectivity.

## Assumptions and scope

All statements concern simple undirected prism graphs with \(n\ge3\), real \(t>0\), unit **total priced conductance** (not unit resistance), and effective resistance in the ordinary electrical sense. Each rung and rim conductance is optimized separately before the theorem establishes symmetry. At fixed finite \(n\), the optimum has positive conductance on all \(3n\) edges. Formulas (4)–(5) take \(n\to\infty\) with \(t\) held strictly positive and constant; they do not assert uniformity when the price depends on \(n\).

## Proof

**1. Global uniqueness and symmetry, without an assumed symmetric competitor.** Let \(N=2n\) and restrict the Laplacian \(L(w)\) to the \((N-1)\)-dimensional space orthogonal to the all-ones vector. Whenever the weighted network is connected this restriction is positive definite and \(K_n(w)=N\operatorname{tr}L(w)_{\mathbf1^\perp}^{-1}\). For a positive definite symmetric matrix \(X\) and a nonzero symmetric direction \(H\),
\[
 \frac{d^2}{ds^2}\bigg|_{s=0}\operatorname{tr}(X+sH)^{-1}
 =2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0.
\]
The inequality follows by writing the trace as the trace of a congruence of \((X^{-1/2}HX^{-1/2})^2\) with a positive-definite matrix. The map from prism edge weights to Laplacian is injective: each edge's weight is the negative of its distinct off-diagonal Laplacian entry. Thus the objective is strictly convex on the connected feasible set. The priced unit-budget simplex is compact, and approaching the disconnected locus forces the smallest positive Laplacian eigenvalue to vanish and hence \(K_n\to\infty\). An optimizer therefore exists and is unique. Rotations and reflections of the cycle together with swapping the two layers preserve the objective and edge prices, and act transitively on the \(2n\) rim edges and separately on the \(n\) rungs. Uniqueness forces a common rim weight \(a\) and a common rung weight \(b\). Neither can vanish without disconnecting the graph, so \(a,b>0\).

**2. Exact spectrum and reduction.** The cycle Laplacian eigenvalues are \(\sigma_k\), \(0\le k<n\), and the two-layer mode decomposition of \(L\) gives \(a\sigma_k\) (symmetric layer mode) and \(a\sigma_k+2b\) (antisymmetric layer mode). Exactly one eigenvalue, \(a\sigma_0\), vanishes. The classical cycle sum \(\sum_{k=1}^{n-1}\sigma_k^{-1}=(n^2-1)/12=A_n\) follows, for example, by summing the cycle Green function or the trigonometric cosecant-square identity. With \(x=b/a\), the budget reads \(na(2+tx)=1\), so \(a=1/[n(2+tx)]\). Consequently
\[
 K_n(x)=2n^2(2+tx)\left(A_n+S_n(x)\right),\quad x>0.
\tag{6}
\]
Set \(\alpha=\operatorname{arcosh}(1+x)\). Since \(\sigma_k+2x=2(\cosh\alpha-\cos(2\pi k/n))\), summing the Poisson kernel identity
\[
 \frac{\sinh\alpha}{\cosh\alpha-\cos\theta}
 =1+2\sum_{j\ge1}e^{-j\alpha}\cos(j\theta)
\]
over the \(n\)-th roots of unity gives \(\sum_k(\cosh\alpha-\cos(2\pi k/n))^{-1}=n\coth(n\alpha/2)/\sinh\alpha\); this proves (3) because \(\sinh\alpha=\sqrt{x(x+2)}\).

**3. Unique positive scalar equation.** Differentiating (6), using \(S_n'(x)=-2\sum_k(\sigma_k+2x)^{-2}\), gives
\[
 \frac{K_n'(x)}{2n^2}
 =t\left(A_n+\sum_k\frac{\sigma_k}{(\sigma_k+2x)^2}\right)
 -4\sum_k\frac1{(\sigma_k+2x)^2}.
\]
Define \(U(x)=\sum_k(\sigma_k+2x)^{-2}\) and \(V(x)=\sum_k\sigma_k(\sigma_k+2x)^{-2}\). Equation (1) is equivalent to \(t=T(x):=4/(A_n/U(x)+V(x)/U(x))\). Here \(U(x)\) strictly decreases, so \(A_n/U(x)\) strictly increases. Furthermore \(V/U\), the weighted average of \(\sigma_k\) under weights \((\sigma_k+2x)^{-2}\), is nondecreasing: for \(\sigma_i>\sigma_j\), the ratio of their weights \(((\sigma_j+2x)/(\sigma_i+2x))^2\) strictly increases with \(x\), shifting relative mass upward in \(\sigma\). Thus \(T\) is strictly decreasing. As \(x\downarrow0\), the zero eigenvalue contributes \(1/(4x^2)\) to \(U\), so \(T(x)\to\infty\). As \(x\to\infty\), \(A_n/U\to\infty\), so \(T(x)\to0\). Thus exactly one stationary point exists, and because \(K_n(x)\to\infty\) at both endpoints it is the unique minimizer. This proves (1)–(3).

**4. Sharp asymptotics and control of the minimizer.** Fix \(t>0\), set \(x=c n^{-2/3}\), and hold \(c\) in any compact subinterval of \((0,\infty)\). Since \(\operatorname{arcosh}(1+x)\sim\sqrt{2x}\), the hyperbolic cotangent in (3) tends to one, uniformly on such compact \(c\)-intervals, at an exponentially small rate in \(n^{2/3}\). Therefore
\[
 S_n(c n^{-2/3})=\frac{n^{4/3}}{2\sqrt{2c}}+o(n^{4/3})
\]
uniformly, and with \(F_n(x)=(2+tx)(A_n+S_n(x))\),
\[
 \frac{F_n(c n^{-2/3})-2A_n}{n^{4/3}}
 =\frac{tc}{12}+\frac1{\sqrt{2c}}+o(1)
 =:g_t(c)+o(1).
\tag{7}
\]
To justify passing to the minimizer rather than assuming its scaling, evaluate at any fixed trial \(c>0\). This gives \(F_n(x_n)-2A_n\le C n^{4/3}\) for some fixed \(C\). The lower bound \(F_n(x_n)-2A_n\ge t x_n A_n\) shows \(n^{2/3}x_n\) is bounded above. Using the exact inequality from (3), \(S_n(x)\ge n/[2\sqrt{x(x+2)}]\), and the already established upper bound \(x_n=O(n^{-2/3})\), the lower bound \(F_n(x_n)-2A_n\ge2S_n(x_n)\) shows \(n^{2/3}x_n\) is bounded below by a positive constant. Thus scaled minimizers stay in a compact subset of \((0,\infty)\), on which (7) is uniform. The function \(g_t(c)=tc/12+(2c)^{-1/2}\) is strictly convex, and its unique minimizer satisfies \(tc^{3/2}=3\sqrt2\), i.e.
\[
 c=c_t=(18/t^2)^{1/3},\quad g_t(c_t)=tc_t/4=(18t)^{1/3}/4.
\]
Every subsequential scaled-minimizer limit must minimize \(g_t\), so \(n^{2/3}x_n\to c_t\). Substituting into \(a_n,b_n\) gives (4). Finally (2), (7), and \(2n^2\cdot2A_n=(n^4-n^2)/3\) yield (5). The uniform-edge comparison follows from \(x=1\) and \(S_n(1)=O(n)\). \(\square\)

## Verification

`artifacts/check_prism.py` is a standalone Python 3 standard-library corroboration script. Execute `python3 artifacts/check_prism.py` after extracting that embedded file to the specified relative path. It builds weighted Laplacian matrices from individual graph edges, computes inverse traces by exact rational Gauss–Jordan elimination, and independently compares the block-spectral formula. It also constructs exact stationary solutions by defining the price from a rational candidate ratio and checks strict cost optimality against rational perturbations. A separate floating-point check verifies the Chebyshev/hyperbolic sum. The observed output was:

`VERIFY_OK 80 independent exact inverse-trace identities; 200 exact optimal-root inequalities; 24 hyperbolic-sum comparisons`

These tests verify finitely many specializations only; universality, uniqueness and the asymptotic exponent are proved analytically above, not by finite enumeration. Independently, numerical scalar-root calculations for \(n=32,128,512,2048\) at \(t=1\) show \(n^{2/3}x_n\) approaching \(18^{1/3}\) and the normalized next-order Kirchhoff coefficient approaching \(18^{1/3}/2\).

## Relationship to prior work

Ghosh, Boyd and Saberi proved general convex minimization of total effective resistance and global-optimization machinery, including a barbell example (2006 conference version, 2008 journal version). The strict convexity reduction here uses that framework; general solvability alone does not supply the particular prism equation, its unique finite solution, or its anomalous \(n^{-2/3}\) weight law. Çınkır (2017, §§1–3 and Theorems 3.1–3.2) obtains resistance and Kirchhoff formulas for **unit-edge** prisms. Baigonakova and Mednykh (2019, Theorems 2–4) give exact formulas and large-size asymptotics for **unit-resistance** prisms and Möbius ladders. Azimi and Farrokhi (2023, §§1 and 4) obtain matrix inverses and Kirchhoff data for **unweighted** circular ladders. None of those inspected prism results optimizes priced edge conductances, and their fixed-weight asymptotics differ from (4)–(5). Carmona, Encinas, and Mitjana (2014) analyze weighted **linear** ladder-like chains, not the closed priced-conductance prism optimization; its accessible abstract does not settle the possibility of a related unpublished/specialized extension. No literature or database search proves absolute novelty.

## Limitations

The result is an exact theorem only for two-layer circular ladders, uniform prices **within** each of the two edge classes, and the total effective-resistance/Kirchhoff-index objective. It does not classify arbitrary heterogeneous edge prices, rectangular grids of increasing width, or price parameters that vary with network size. The finite-dimensional numerical tests are not proofs. Earlier equivalent results in less discoverable literature are a residual originality risk; a relevant 2014 full text could not be inspected despite checking an open institutional repository and publisher access, so no whole-paper noncoverage assertion is made for it. The study has no independent audit or outside verification.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006 proceedings, Kyoto, July 24–28, 2006 (conference-range date, precise first-public day not established): https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf. Extended paper: *SIAM Review* 50 (2008), 37–66; day-verified online publication February 1, 2008: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
2. Z. Çınkır, *Effective Resistances and Kirchhoff index of Prism Graphs*, arXiv:1704.03429v1 (April 11, 2017), https://arxiv.org/html/1704.03429v1.
3. G. A. Baigonakova and A. D. Mednykh, *Elementary formulas for Kirchhoff index of Möbius ladder and Prism graphs*, Siberian Electronic Mathematical Reports 16 (2019), 1654–1661, DOI:10.33048/semi.2019.16.117, https://www.mathnet.ru/eng/semr1158.
4. A. Azimi and M. Farrokhi D. G., *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497v1 (June 18, 2023), https://arxiv.org/pdf/2306.10497.
5. A. Carmona, A. M. Encinas and M. Mitjana, *Effective resistances for ladder-like chains*, International Journal of Quantum Chemistry 114 (2014), 1670–1677, DOI:10.1002/qua.24740. Full text access was unsuccessful; only the primary abstract and citation information were consulted.

# Sharp fluctuation transition in stretched-exponential weighted recursive trees

## Finding
Fix \(1/2<\beta<1\) and \(0<c<2^{\beta}\). Define deterministic weights by \(w_1=W_1=1\), \(p_j=cj^{-\beta}\), \(w_j=p_jW_{j-1}/(1-p_j)\), and \(W_j=W_{j-1}+w_j\) for integers \(j\ge2\). Each newcomer attaches independently to an earlier vertex with probability proportional to its weight. Let \(T_n\) be the total root-to-vertex distance in the resulting \(n\)-vertex tree. The cumulative weights have stretched-exponential growth:
\[
\log W_n=\frac{c}{1-\beta}n^{1-\beta}+O(1).
\]
The mean satisfies
\[
\mathbb ET_n\sim \frac{c}{(1-\beta)(2-\beta)}n^{2-\beta}.
\]
There is a **sharp fluctuation transition at \(\beta=2/3\)**:
\[
\operatorname{Var}(T_n)\sim
\begin{cases}
\displaystyle\frac{2c^3}{(1-\beta)(2-3\beta)(3-3\beta)(4-3\beta)}n^{4-3\beta},&1/2<\beta<2/3,\\[7pt]
3c^3n^2\log n,&\beta=2/3,\\[3pt]
\sigma_{\beta,c}^2n^2,&2/3<\beta<1,
\end{cases}
\]
where \(\sigma_{\beta,c}^2=\sum_{j=2}^{\infty}p_j^2v_j\in(0,\infty)\), \(v_2=0\), and \(v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j)\). Precisely when \(\beta>2/3\), the centered quantity \((T_n-\mathbb ET_n)/n\) converges almost surely and in \(L^2\) to the nondegenerate random variable \(Z=\sum_{j=2}^{\infty}p_j\xi_j\), where \(\xi_j\) is the centered conditional insertion-depth innovation. When \(1/2<\beta\le2/3\), this normalization has diverging second moment and therefore no \(L^2\) limit with finite variance. The result does **not** assert failure of weak convergence or almost-sure convergence below the threshold.

## Assumptions and scope
The vertices arrive in increasing label order, the root is label one with depth zero, and each vertex \(j\ge2\) independently selects its parent among the earlier vertices, proportional to the fixed strictly positive weights. The quantity \(p_j=w_j/W_j\) is the fraction of total weight held by the \(j\)-th vertex immediately after insertion, **not** the probability of selecting that vertex as a parent at time \(j\). The restriction \(0<c<2^\beta\) makes all \(p_j\) strictly between zero and one. The result is for a fixed pair \((\beta,c)\), without uniformity at the endpoints. All limits are as integer \(n\to\infty\).

## Proof
**1. Construction and first moment.** The displayed recurrence gives \(W_j=W_{j-1}/(1-p_j)\). Thus \(\log W_n=-\sum_{j=2}^n\log(1-p_j)=\sum_{j=2}^n p_j+O(\sum_{j\ge2}p_j^2)\). Since \(\beta>1/2\), the square sum converges; integral comparison gives the stretched-exponential formula. The standard depth identity for deterministic weighted recursive trees, \(\mathbb ET_n=\sum_{j=1}^{n-1}(n-j)p_j\) with \(p_1=1\), gives the mean by a Riemann sum.

**2. Imported exact identities and a new asymptotic lemma.** Write \(\mathcal F_j\) for all parent choices through vertex \(j\), let \(D_j\) be the depth of vertex \(j\), and put \(\xi_j=D_j-\mathbb E(D_j\mid\mathcal F_{j-1})\). Directly rederivable by conditioning on the parent choice (and explicitly established in the motivating paper), the weighted-depth martingale and total-path-length identities are
\[
M_n=\sum_{j=2}^np_j\xi_j,\qquad
T_n-\mathbb ET_n=\sum_{j=2}^n[1+(n-j)p_j]\xi_j,
\]
where the \(\xi_j\) are orthogonal martingale differences. Their variances \(v_j=\mathbb E\xi_j^2\) satisfy \(v_2=0\) and \(v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j)\). Consequently
\[
\operatorname{Var}(T_n)=\sum_{j=2}^n[1+(n-j)p_j]^2v_j.
\]
The recurrence gives \(0\le v_j\le\sum_{i=2}^{j-1}p_i=O(j^{1-\beta})\). Summing its increments yields
\[
v_n=\sum_{j=2}^{n-1}p_j-\sum_{j=2}^{n-1}p_j^2-\sum_{j=2}^{n-1}p_j^2v_j.
\]
The second sum is bounded, and the third is \(O(1+n^{\max(2-3\beta,0)}+\mathbf{1}_{\{\beta=2/3\}}\log n)\), which is \(o(n^{1-\beta})\) for every \(\beta>1/2\). Hence the key new asymptotic is
\[
v_n\sim\frac{c}{1-\beta}n^{1-\beta},\qquad p_n^2v_n\sim\frac{c^3}{1-\beta}n^{1-3\beta}.
\]

**3. Supercritical variance and sharp boundary.** The terms containing the additive \(1\) in \([1+(n-j)p_j]^2\) have total contribution bounded by \(O(n^{3-2\beta}+n^{2-\beta})\); for \(1/2<\beta\le2/3\) this is lower order than the claimed main term. If \(\beta<2/3\), the leading Riemann sum is
\[
\frac{c^3}{1-\beta}\sum_{j=2}^n(n-j)^2j^{1-3\beta}
\sim\frac{c^3}{1-\beta}n^{4-3\beta}
\int_0^1(1-t)^2t^{1-3\beta}\,dt.
\]
The integral equals \(2/[(2-3\beta)(3-3\beta)(4-3\beta)]\). At \(\beta=2/3\), the same sum is \(3c^3n^2\log n+o(n^2\log n)\): expanding \((n-j)^2\) shows that the two correction sums are only \(O(n^2)\). Both variance formulas follow.

**4. Almost-sure and mean-square convergence beyond the threshold.** For \(\beta>2/3\), the series \(\sum_jp_j^2v_j\) converges and has a positive term at \(j=3\), since \(v_3=p_2(1-p_2)>0\). Thus \(M_n\) converges almost surely and in \(L^2\) to \(Z\). Exactly,
\[
\frac{T_n-\mathbb ET_n}{n}=M_n+\frac1n\sum_{j=2}^n(1-jp_j)\xi_j.
\]
The martingale series \(\sum_{j\ge2}(1-jp_j)\xi_j/j\) converges almost surely by \(\sum_jv_j/j^2<\infty\) and \(\sum_jp_j^2v_j<\infty\). Kronecker's lemma makes the remainder converge almost surely to zero. Orthogonality bounds its \(L^2\) norm squared by \(O(n^{-\beta}+n^{2-3\beta})=o(1)\). Therefore the claimed almost-sure and \(L^2\) limit holds. The variance asymptotic follows by \(L^2\) convergence. Below or at the threshold, the variance estimates in Step 3 diverge after division by \(n^2\), excluding finite-variance \(L^2\) convergence. This completes the stated classification.

## Verification
Run `python3 verify.py` using the standard Python library. It independently enumerates every possible parent-choice configuration for five sizes (three through seven vertices) with exact rational probabilities and checks the finite-size variance identity against a separate recurrence implementation. It also computes large-size variance-ratio diagnostics for parameters on either side of the boundary and at the boundary. Such numerical comparisons are corroboration, not proof of infinite asymptotics; Steps 2–4 above establish those limits.

## Relationship to prior work
Gałązka and Wdowicka (2026), *Total Path Length in Power-Weight Recursive Trees*, arXiv:2610.00614v1, supply the exact innovation and variance identities for arbitrary deterministic weights, and the almost-sure linear-scale theorem assuming \(p_n=O(1/n)\). Their Discussion §10 explicitly asks whether that sufficient rate can be relaxed. Those exact identities are used here with attribution; the new contribution is a sharp \(2/3\) transition and full three-regime variance asymptotics for the natural stretched-exponential class \(p_n=cn^{-\beta}\), where \(p_n\) is not \(O(1/n)\). Sénizergues (2019/2021), arXiv:1904.07115, studies related weighted recursive trees principally with cumulative weights asymptotic to powers of \(n\) and profile/height observables; those conditions do not include the stretched-exponential weights above. The claim is not that exact finite-size variance formulas are new.

## Limitations
The theorem is restricted to \(1/2<\beta<1\). At and below the fluctuation threshold it establishes divergence of \(L^2\) fluctuations at the original linear normalization, not the optimal limiting **distribution** at a larger normalization. The asymptotic formulas are not uniform as \(\beta\) approaches either endpoint. Earlier general-purpose martingale or weighted-recursive-tree theorems not located by the recorded searches could potentially imply portions of the transition; independent priority assessment is outstanding.

## References
1. M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1 (first posted 2026-09-30), especially Theorem 5.2, Proposition 5.3, Theorem 6.2 and Section 10. https://arxiv.org/html/2610.00614v1
2. D. Sénizergues, *Geometry of weighted recursive and affine preferential attachment trees*, arXiv:1904.07115 (2019), published in Electronic Journal of Probability (2021), especially §1.1–1.2. https://arxiv.org/html/1904.07115v3
3. M. Pain and D. Sénizergues, *Correction terms for the height of weighted recursive trees*, arXiv:2101.01156 (2021), mentioned as related height literature; its detailed theorems were not inspected. https://arxiv.org/abs/2101.01156

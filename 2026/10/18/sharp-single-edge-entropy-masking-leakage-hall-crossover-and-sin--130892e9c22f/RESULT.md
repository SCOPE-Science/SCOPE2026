# Sharp single-edge entropy masking: leakage, Hall crossover, and Sinkhorn slowdown

## Finding
For the entropically regularized finite transportation problem with **exactly one penalized cell** and all other costs zero, both the worst-case total-variation error of replacing the costly cell by an actual forbidden edge and the worst-case local full-sweep Sinkhorn convergence factor are attained at the same balanced Hall-boundary marginals. The exact dimension-independent values, in terms of \(t=e^{-M/\varepsilon}\), are
\[
\sup\operatorname{TV}(P_t,P_0)=\frac{\sqrt t}{1+\sqrt t},\qquad
\sup\lambda_{\mathrm{Sinkhorn}}=\left(\frac{1-\sqrt t}{1+\sqrt t}\right)^2.
\]
The first supremum ranges over all strictly positive finite marginals for which forbidding the exceptional cell is feasible; the second ranges over all strictly positive finite marginals without that feasibility restriction. Both suprema are attained at \(r_1=c_1=1/2\). Thus they obey the exact identity \(\sup\lambda_{\mathrm{Sinkhorn}}=(1-2\sup\operatorname{TV})^2\). In particular, for a uniform target total-variation error \(0<\eta<1/2\), the sharp necessary and sufficient penalty is \(M\ge2\varepsilon\log((1-\eta)/\eta)\). A fixed positive Hall slack improves leakage from an \(e^{-M/(2\varepsilon)}\) law to an \(e^{-M/\varepsilon}\) law, with an explicit boundary crossover.

## Assumptions and scope
Let \(m,n\ge2\) be arbitrary integers. Let \(r=(r_1,\ldots,r_m)\), \(c=(c_1,\ldots,c_n)\) be strictly positive probability vectors, with \(p=r_1\in(0,1)\), \(q=c_1\in(0,1)\). Fix \(\varepsilon>0\), \(M\ge0\), and minimize
\[
F(P)=M P_{11}+\varepsilon\sum_{i=1}^{m}\sum_{j=1}^{n}P_{ij}(\log P_{ij}-1)
\]
over nonnegative matrices \(P\) whose row/column marginals equal \(r,c\). Interpret \(0\log0=0\). Costs of the form \(M{\bf1}_{(i,j)=(1,1)}+u_i+v_j\) give the same minimizer. Write \(t=e^{-M/\varepsilon}\) and denote the unique minimizer by \(P_t\). The hard-forbidden comparison \(P_0\) means minimizing the same entropy objective with \(P_{11}=0\), when feasible, and does not mean applying an infinite finite-precision penalty. Use \(\operatorname{TV}(P,Q)=\frac12\sum_{ij}|P_{ij}-Q_{ij}|\).

For the local rate, a full Sinkhorn iteration means row-normalizing \(K_{ij}=1\), except \(K_{11}=t\), followed by column-normalizing to the prescribed marginals. The local convergence factor is the largest modulus eigenvalue of the derivative of the log-column-scaling map after quotienting its one-dimensional common-scaling gauge. It is a *local asymptotic* rate; no claim about globally uniform number of iterations is made.

## Proof
**Step 1: exact optimizer and hard feasibility.** Strict convexity of the entropy and positive kernel \(K\) imply a unique strictly positive optimizer with \(P_{ij}=a_i K_{ij} b_j\) for positive scaling vectors. Conditional on the exceptional row or column, the other entries must factor proportionally to the prescribed residual marginals. If \(x=P_{11}\), exact row and column sums force
\[
\begin{aligned}
P_{11}&=x,&P_{1j}&=\frac{(p-x)c_j}{1-q}\quad(j>1),\\
P_{i1}&=\frac{(q-x)r_i}{1-p}\quad(i>1),&
P_{ij}&=\frac{(1-p-q+x)r_ic_j}{(1-p)(1-q)}\quad(i,j>1).
\end{aligned}
\]
Since the kernel has cross odds \(t\), eliminating scaling vectors gives \(x(1-p-q+x)=t(p-x)(q-x)\). Conversely these positive entries satisfy all KKT conditions if the odds identity holds. Setting \(d=p+q-1\), its unique root in \((\max\{0,d\},\min\{p,q\})\) is characterized by
\[
(1-t)x^2+[1-p-q+t(p+q)]x-tpq=0.
\]
For \(t=1\), this is \(x=pq\); for \(0<t<1\), the positive quadratic root is unambiguous. For a forbidden \((1,1)\), feasibility is equivalent to \(p+q\le1\); indeed the above four-block plan with \(x=0\) is nonnegative exactly in that range. The limiting \(P_0\) is its unique maximum-entropy feasible plan (the same conditional factorization is obtained by constrained entropy minimization, including the Hall equality case). Comparing the four blocks of \(P_t\) and \(P_0\), their absolute mass differences are \(x,x,x,x\), respectively. Hence
\[\operatorname{TV}(P_t,P_0)=2x.\]

**Step 2: sharp uniform leakage and a penalty budget.** For fixed \(s=p+q\), the coefficient of \(x\) in its quadratic is \(1-s+ts\), while the negative constant is \(-tpq\). The positive root is strictly increasing in \(pq\), so is maximal at \(p=q=s/2\). Along that balanced curve it increases strictly with \(s\), as follows by implicit differentiation: with \(B=1-s+ts\), the derivative of \((1-t)x^2+Bx-ts^2/4\) with respect to \(s\) is \(-(1-t)x-ts/2<0\), while its derivative with respect to \(x\) is positive. For hard feasibility \(s\le1\), the unique maximizer (when \(t<1\)) is therefore \(p=q=1/2\). At that point the odds equation is \(x^2=t(1/2-x)^2\), giving \(x=\sqrt t/[2(1+\sqrt t)]\). The claimed sharp worst-case total variation and logarithmic penalty condition follow. At \(t=1\), the same marginal pair maximizes \(pq\).

**Step 3: exact Hall-slack boundary.** If \(p+q\le1-\kappa\) for fixed \(\kappa\in(0,1)\), the same monotonicity makes the worst case \(p=q=(1-\kappa)/2\). Put \(B=\kappa+t(1-\kappa)\). Its exceptional mass is exactly
\[
 x_{\max}(\kappa,t)=\frac{t(1-\kappa)^2}{2\left[B+\sqrt{B^2+t(1-t)(1-\kappa)^2}\right]}.
\]
For fixed \(\kappa>0\), this equals \((1-\kappa)^2t/(4\kappa)+O_\kappa(t^2)\). In the joint boundary limit \(t\downarrow0\), \(\kappa/\sqrt t\to u\in[0,\infty)\), rationalization gives
\[
\frac{x_{\max}(\kappa,t)}{\sqrt t}\longrightarrow\frac{\sqrt{u^2+1}-u}{2}.
\]
At \(\kappa=0\), the unscaled mass is asymptotic to \(\sqrt t/2\), unlike the strict-slack exponential law. Thus \(\sqrt t\), not \(t\), is the sharp Hall-boundary scale.

**Step 4: exact local Sinkhorn factor.** Denote \(D_r=\operatorname{diag}(r)\), \(D_c=\operatorname{diag}(c)\). Differentiating one row and one column normalization of the logarithmic column scalings at the fixed point gives
\[
J=D_c^{-1}P_t^{\mathsf T}D_r^{-1}P_t.
\]
It has a gauge eigenvalue \(1\). Write the optimizer as \(P_t=rc^{\mathsf T}+(x-pq)ab^{\mathsf T}\), where \(a_1=b_1=1\), \(a_i=-r_i/(1-p)\) for \(i>1\), and \(b_j=-c_j/(1-q)\) for \(j>1\). The vectors \(D_r^{-1/2}a\), \(D_c^{-1/2}b\) are orthogonal to the respective marginal square-root vectors, and their squared norms are \(1/[p(1-p)]\), \(1/[q(1-q)]\). Consequently the whitened joint matrix \(D_r^{-1/2}P_tD_c^{-1/2}\) has only two nonzero singular values, \(1\) and \(|x-pq|/\sqrt{p(1-p)q(1-q)}\). The non-gauge spectrum of \(J\) is therefore \(\lambda=(x-pq)^2/[p(1-p)q(1-q)]\) and, if \(n>2\), zeros.

**Step 5: the sharp local-rate bound, with equality.** Aggregate the plan into the positive two-by-two table \(\begin{psmallmatrix}x&y\\z&w\end{psmallmatrix}\), where \(y=p-x\), \(z=q-x\), \(w=1-p-q+x\). Then \(xw=t yz\) and \(x-pq=xw-yz\). Elementary arithmetic-geometric mean gives
\[
(x+y)(z+w)\ge(\sqrt{xw}+\sqrt{yz})^2,
\qquad
(x+z)(y+w)\ge(\sqrt{xw}+\sqrt{yz})^2;
\]
the respective differences are \((\sqrt{xz}-\sqrt{yw})^2\) and \((\sqrt{xy}-\sqrt{zw})^2\). Multiplying and using the odds identity yields
\[
\lambda=\frac{(xw-yz)^2}{(x+y)(z+w)(x+z)(y+w)}
\le\left(\frac{1-\sqrt t}{1+\sqrt t}\right)^2.
\]
For \(0<t<1\), equality in both arithmetic-geometric mean inequalities requires \(x=w\), \(y=z\), equivalent to \(p=q=1/2\); the balanced plan attains it. At \(t=1\), every plan has \(\lambda=0\). Thus the same pair is the exact slowest Sinkhorn case and worst leaking soft mask. Their two formulas give the claimed identity. Finally \(1-\lambda_{\max}=4\sqrt t/(1+\sqrt t)^2\), and a full-sweep e-folding time \(1/[-\log\lambda_{\max}]\sim1/(4\sqrt t)\) for \(t\downarrow0\).

## Verification
The standalone `verify.py` performs exact rational two-by-two checks and 8,467 seeded multidimensional numerical assertions, including marginal conservation, positive entries, cross odds, the rank-two singular-value formula, independent finite-difference checks of the full-sweep Sinkhorn Jacobian, and Hall-slack and boundary-layer limits. It requires Python 3 and NumPy. These finite tests serve only as reproducibility checks; Steps 1–5 supply the arguments for every admissible dimension and parameter.

## Relationship to prior work
Corless–Quinn–Boufelja–Shorten (2024) develops structurally forbidden transport cells and constrained Sinkhorn algorithms, including feasibility issues. Baradat–Ventre (2022) examines Sinkhorn with hard supports when the constrained Schrödinger problem fails. Tang and collaborators (2024) study a broader Sinkhorn-type constrained-transport method. Weed (2018) gives general entropic linear-programming penalty approximation estimates. General local Sinkhorn Jacobian/convergence analysis, including results of Lehmann–von Renesse–Sambale–Uschmajew (2021), predates this result. The contribution assessed here is **not** the scaling equations, the two-by-two cross-ratio identity in isolation, the general Sinkhorn Jacobian, or broad entropic convergence; it is the *simultaneous sharp, dimension-free one-edge soft-mask leakage and full-sweep local-rate classification*, its exact common maximizer, uniform penalty budget, and sharp Hall-slack crossover. These comparisons do not establish publication priority against unindexed specialized matrix-scaling literature.

## Limitations
Only one penalized cell is allowed; the remaining cost must be zero up to separable row/column potentials. All marginals are strictly positive. Hard-mask comparison requires \(p+q\le1\). Sinkhorn's factor is asymptotic and local, assumes exact arithmetic and exact row/column scaling, and is not a total runtime estimate. The Hall-slack asymptotic fixes \(\kappa>0\), while its displayed crossover permits \(\kappa\to0\). No arbitrary sparse mask, general-cost transport, Sinkhorn global complexity bound, or publication-priority certification is claimed.

## References
- M. Corless, A. Quinn, S. Boufelja and R. Shorten, *Algorithms for constrained optimal transport*, arXiv:2404.00003 (first publicly posted 2024-02-16), https://arxiv.org/abs/2404.00003 .
- Y. Tang et al., *A Sinkhorn-type Algorithm for Constrained Optimal Transport*, arXiv:2403.05054 (2024), https://arxiv.org/abs/2403.05054 .
- A. Baradat and E. Ventre, *Convergence of the Sinkhorn algorithm when the Schrödinger problem has no solution*, arXiv:2207.02977 (2022), https://arxiv.org/abs/2207.02977 .
- J. Weed, *An explicit analysis of the entropic penalty in linear programming*, arXiv:1806.01879 (2018), https://arxiv.org/abs/1806.01879 .
- L. Lehmann, M. von Renesse, M. Sambale and A. Uschmajew, *A note on overrelaxation in the Sinkhorn algorithm* (2021), DOI:10.1007/s11590-021-01830-0 .
- J. Espinosa Mena, *On the Convergence of the Sinkhorn Algorithm with Sparse Cost Matrices*, arXiv:2405.20528 (2024), https://arxiv.org/abs/2405.20528 ; relevant related source, full text not verified.

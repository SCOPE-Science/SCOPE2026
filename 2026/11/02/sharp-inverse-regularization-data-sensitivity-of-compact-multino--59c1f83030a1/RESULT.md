# Sharp inverse-regularization data sensitivity of compact multinode Shepard interpolation

## Finding
For the residual-indicator, data-dependent compact multinode Shepard operator, the data-to-output Lipschitz constant at a covered nonnode point has an explicit upper bound of order \(\epsilon^{-1}\). This order is **attained** on an admissible six-node one-dimensional degree-one configuration: changing a single indicator-only observation by \(c\epsilon\) changes the numerical answer by a positive amount independent of \(\epsilon\). At the symmetric evaluation point the exact change is
\[
\widetilde K_{\epsilon}[f+c\epsilon e_{1/4}](3/2)-\widetilde K_{\epsilon}[f](3/2)
=\frac{(1+c)^t-1}{2[1+(1+c)^t]},\qquad c>0,\quad t\ge1.
\]
The one-sided data derivative there is \(t/(4\epsilon)\). This is a fixed-stencil, exact-arithmetic statement, not a claim about floating-point roundoff or the particular stencil-selection heuristic.

## Assumptions and scope
Fix dimension \(s\ge1\), polynomial degree \(d\ge0\), finitely many distinct \(\Pi_d(\mathbb R^s)\)-unisolvent stencils \(\tau_j\) covering the data nodes, and nonempty indicator sets \(\mathcal E_j\subset X\setminus\tau_j\). Assume the fixed evaluation point \(x\in\Omega\setminus X\) is covered by at least one stencil. Set \(J_x\) to the positive-support active stencils. Their geometric compact multinode Shepard weights \(\widetilde W_j(x)>0\) do not depend on the observed data. All geometry and indicator sets remain unchanged under data perturbation.

For data \(f=(f_a)_{a\in X}\), let \(P_j[f](y)=\sum_{a\in\tau_j}\ell_{j,a}(y)f_a\) be the exact local polynomial interpolant, and set
\[
I_j(f)=\frac{1}{|\mathcal E_j|}\sum_{y\in\mathcal E_j}|f_y-P_j[f](y)|,\qquad
p_j(f;x)=\frac{\widetilde W_j(x)(\epsilon+I_j(f))^{-t}}
{\sum_{k\in J_x}\widetilde W_k(x)(\epsilon+I_k(f))^{-t}},
\quad\widetilde K_\epsilon[f](x)=\sum_{j\in J_x}p_j(f;x)P_j[f](x).
\]
Here \(\epsilon>0\), \(t\ge1\), and the geometric exponent \(\mu>0\) is arbitrary. Introduce finite, computable constants
\[
L_x=\max_{j\in J_x}\sum_{a\in\tau_j}|\ell_{j,a}(x)|,\qquad
H_x=\max_{j\in J_x}\frac1{|\mathcal E_j|}
\sum_{y\in\mathcal E_j}\left(1+\sum_{a\in\tau_j}|\ell_{j,a}(y)|\right).
\]
Then for every pair of data vectors with \(\|f\|_\infty,\|g\|_\infty\le B\), where \(B\ge0\),
\[
\boxed{\ |\widetilde K_\epsilon[f](x)-\widetilde K_\epsilon[g](x)|
\le L_x\left(1+\frac{tBH_x}{\epsilon}\right)\|f-g\|_\infty.\ }
\tag{1}
\]
The exponent \(\epsilon^{-1}\) cannot be uniformly reduced in this class, even with fixed well-separated nodes, degree one, and indicator sets containing only one point.

For the explicit witness, take \(\Omega=(-1/10,31/10)\), ordered nodes
\[
X=(0,1/4,1,2,11/4,3),\quad h=1,\quad x=3/2,
\]
and degree-one stencils and indicator sets
\[
\begin{array}{c|c|c}
 j&\tau_j&\mathcal E_j\\\hline
1&\{0,1\}&\{1/4\}\\
2&\{2,3\}&\{11/4\}\\
3&\{0,1/4\}&\{1\}\\
4&\{11/4,3\}&\{2\}
\end{array}
\]
with support radii \(R_j=\operatorname{diam}(\tau_j)+h\) and geometric factor \(\prod_{a\in\tau_j}(\|x-a\|^{-1}-R_j^{-1})_+^{\mu}\), as in the source construction. The fill distance is \(1/2<1=h\); the stencils cover all nodes and all indicator sites are at distance at most \(h\) from their respective stencils. At \(x=3/2\), only stencils 1 and 2 are active and have identical geometric weight. The baseline samples are \(f=(0,0,0,1,1,1)\) in node order, i.e., two constant branches separated by a gap. Let \(f^{(\delta)}\) differ only through \(f^{(\delta)}_{1/4}=\delta\). This point belongs to the indicator set of stencil 1 but not to either active interpolation stencil.

## Proof
**Upper estimate.** Put \(\delta=\|f-g\|_\infty\) and interpolate the data along \(f^{(u)}=(1-u)f+ug\), \(0\le u\le1\). From the absolute residual definition and linearity of the interpolants, \(u\mapsto I_j(f^{(u)})\) is Lipschitz with almost-everywhere derivative of magnitude at most \(H_x\delta\). Similarly, at every \(u\),
\[
|P_j[f^{(u)}](x)|\le L_xB,\qquad
\left|\frac{d}{du}P_j[f^{(u)}](x)\right|\le L_x\delta.
\]
The logarithmic unnormalized nonlinear weight \(q_j(u)=\log\widetilde W_j(x)-t\log(\epsilon+I_j(f^{(u)}))\) has almost-everywhere derivative bounded by \(tH_x\delta/\epsilon\). Differentiate the normalized weights at those points. With \(p_j=p_j(f^{(u)};x)\), one obtains the exact identity
\[
\frac{d}{du}\widetilde K_\epsilon[f^{(u)}](x)
=\sum_jp_j\frac{dP_j}{du}
+\operatorname{Cov}_{p}(P_j,q'_j).
\]
Since \(|P_j|\le L_x B\), \(|q'_j|\le tH_x\delta/\epsilon\), both weighted standard deviations are at most those bounds; Cauchy--Schwarz therefore gives \(|\operatorname{Cov}_p(P,q')|\le L_xBtH_x\delta/\epsilon\). Integrating the almost-everywhere inequality over \(u\in[0,1]\) proves (1). There is no differentiability assumption on the original data: the finite absolute-residual functions are Lipschitz, so the chain and product rules hold almost everywhere.

**Geometry and exact lower witness.** On the stated one-dimensional domain the largest nearest-node distance is \(1/2\). The four support radii are \(2,2,5/4,5/4\). At \(x=3/2\) the last two stencils are inactive (each has an endpoint at distance \(3/2>5/4\)). The first two are active, and the product of their two unraised geometric factors equals \((1/6)(3/2)=1/4\). Hence their geometric weights are equal for every \(\mu>0\), with each unnormalized product equal to \(4^{-\mu}\). The first active local polynomial is identically zero, the second identically one. Their indicators are initially zero; after perturbation the indicators are \(\delta\) and zero, respectively. Thus for all \(\delta\ge0\)
\[
\widetilde K_\epsilon[f](3/2)=\frac12,\quad
\widetilde K_\epsilon[f^{(\delta)}](3/2)
=\frac{(\epsilon+\delta)^t}{\epsilon^t+(\epsilon+\delta)^t}.
\tag{2}
\]
Differentiating from the right at zero yields \(t/(4\epsilon)\); setting \(\delta=c\epsilon\) gives the stated nonvanishing difference. Taking \(c=1\) yields \((2^t-1)/(2(1+2^t))\) for every \(\epsilon>0\). For \(0<\delta\ll\epsilon\), the change is asymptotic to \(t\delta/(4\epsilon)\) at fixed \(\epsilon\). Because \(f^{(\delta)}\) remains in the unit data cube for small \(\delta\), the Lipschitz modulus over that cube at this evaluation point is at least \(t/(4\epsilon)\). Combined with (1), its dependence on \(\epsilon\) is \(\Theta(\epsilon^{-1})\) for fixed \(t\) and fixed geometry.

This is not an isolated-point effect: for every evaluation point in \((5/4,7/4)\), exactly the two large stencils are active, with positive geometric factors \(G_1(x),G_2(x)\). The baseline and perturbed values there are, respectively,
\[
\frac{G_2(x)}{G_1(x)+G_2(x)},\qquad
\frac{G_2(x)(1+c)^t}{G_1(x)+G_2(x)(1+c)^t},
\]
whose difference is strictly positive and independent of \(\epsilon\) for each fixed \(c>0\).

## Verification
Run the included standalone `verify.py` with Python 3 and standard library only. It explicitly reconstructs all four compact-support products, indicator residuals, and local degree-one interpolation polynomials using exact rational arithmetic. It checks 420 combinations of exact perturbation scales, exponents and geometry parameters and 1,800 seeded bounded-data comparisons against (1). It records \(L_x=H_x=2\) for the six-node witness. These finite computations are cross-checks; the statements for all positive \(\epsilon\), all \(t\ge1\), all admissible finite geometries and arbitrary bounded data follow from the proof above.

## Relationship to prior work
Dell'Accio, Di Tommaso, Larosa, Ruiz-Álvarez and Yáñez, arXiv:2610.31026v1 (2026-10-22), introduce the exact residual-indicator compact multinode scheme and analyze interpolation error, discontinuity detection, coverage and geometric stability. Their general structural and convergence results do not provide a data-to-data perturbation modulus as \(\epsilon\downarrow0\), nor the six-node exact noise transition (2). Their numerical study fixes \(\epsilon=10^{-14}\), making the perturbation scale here concrete. Levin, Ramón, Ruiz-Álvarez and Yáñez, arXiv:2412.02286v1 (2024-12-03), consider nonlinear WENO-type Shepard weights with a different degree-zero least-squares indicator; their interpolation-order and regularity analysis does not state (1) or (2) for the present degree-one residual-indicator operator. The algebra of normalized inverse-indicator weights is generally known; the claim is the quantitative sharp data-conditioning result, including an admissible finite geometry for this particular operator, not invention of that weighting principle.

## Limitations
The witness prescribes a valid fixed stencil family, not necessarily the exact stencil family selected by any particular implementation's greedy Leja heuristic. It concerns sampled-data perturbations at fixed geometry, not instability under moving nodes, finite-precision error or the accuracy of recovery of an unknown continuous target. The critical scale applies when competing active indicators both vanish while their local branch values differ; it does not assert \(\epsilon^{-1}\) amplification for every data configuration. The globally bounded-data upper constant is sufficient rather than optimized. Independent external mathematical validation and exhaustive historical priority have not been performed.

## References
1. F. Dell'Accio, F. Di Tommaso, F. Larosa, J. Ruiz-Álvarez, D. F. Yáñez, *Data-dependent Compact Multinode Shepard Method*, arXiv:2610.31026v1, first submitted 2026-10-22, https://arxiv.org/html/2610.31026v1, especially Sections 3--6.
2. D. Levin, J. M. Ramón, J. Ruiz-Álvarez, D. F. Yáñez, *Weighted Essentially Non-Oscillatory Shepard method*, arXiv:2412.02286v1, first submitted 2024-12-03, https://arxiv.org/html/2412.02286v1, especially Sections 2--3.

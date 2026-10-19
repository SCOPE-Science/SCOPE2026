# Golden-ratio noise threshold for reentrant feedback allocation on stars

## Finding

**Theorem.** Let \(m\ge 2\) be an integer and let \(G=K_{1,m}\) have unit-conductance edges. The hub receives white-noise variance \(\rho>0\), and each leaf receives independent unit-variance white noise. Choose unrestricted nonnegative node feedback gains \(g_v\) with \(\sum_v g_v=B>0\), and minimize the total stationary variance of the resulting stable linear diffusion, equivalently
\[
J(g)=\operatorname{tr}\!\left[Q\bigl(L+\operatorname{diag}(g)\bigr)^{-1}\right],
\qquad Q=\operatorname{diag}(\rho,1,\ldots,1).
\]
The minimizer exists and is globally unique for every \((m,\rho,B)\). It assigns a common strictly positive gain \(y\) to all leaves and a gain \(x\ge0\) to the hub, with \(x+my=B\) and \(x<B\).

Set
\[
\rho_*(m)=\frac{5\sqrt5-11}{2}\,m(m-1),\qquad
B_*(m)=\frac{\sqrt5-1}{2}\,m,
\]
and define
\[
R_m(B)=\frac{m(m-1)(B/m)}{(1+B/m)^2(2+B/m)}.
\]
The exact support criterion is
\[
\boxed{x=0\quad\Longleftrightarrow\quad\rho\le R_m(B).}
\]
Consequently, the complete support phase diagram is:

1. If \(0<\rho<\rho_*(m)\), the equation \(R_m(B)=\rho\) has exactly two positive solutions \(B_-(m,\rho)<B_+(m,\rho)\). The hub is unpinned exactly for \(B\in[B_-,B_+]\), and has strictly positive gain for all other positive budgets.
2. If \(\rho=\rho_*(m)\), the hub is unpinned at the *single* budget \(B=B_*(m)\), and is pinned at every other positive budget.
3. If \(\rho>\rho_*(m)\), the hub is pinned for every positive budget.

This determines the entire optimal allocation exactly. When \(\rho\le R_m(B)\), it is \(x=0\), \(y=B/m\). Otherwise, \(x\) is the unique solution in \((0,B)\) to \(\partial_x F_{m,\rho,B}(x)=0\), where the following explicit rational function is strictly convex on \([0,B]\):
\[
\begin{aligned}
y(x)&=\frac{B-x}{m},\\
D(x)&=m\,y(x)+x\bigl(1+y(x)\bigr),\\
F_{m,\rho,B}(x)&=\frac{\rho\bigl(1+y(x)\bigr)}{D(x)}
+\frac{m}{1+y(x)}+\frac{m}{D(x)\bigl(1+y(x)\bigr)}.
\end{aligned}
\]
For each fixed \(\rho>0\), the two switching budgets exist for all sufficiently large \(m\), and obey
\[
B_-(m,\rho)\sim\frac{2\rho}{m-1},\qquad
B_+(m,\rho)\sim\frac{m^2}{\sqrt\rho}
\quad(m\longrightarrow\infty).
\]

**Exact small-network example.** For the three-vertex path \(K_{1,2}\) with \(\rho=1/6\), the unpinned-hub interval is precisely
\[
\boxed{\sqrt{33}-5\ \le B\le\ 2.}
\]
The central vertex is pinned at both smaller and larger budgets. Thus reentrant deletion already occurs on three vertices when the hub noise intensity differs from that of the leaves.

## Assumptions and scope

All edges have unit weight, all gain costs are one per unit, disturbances are independent centered white noises with covariance intensities specified by \(Q\), and feedback gains are freely adjustable nonnegative real numbers summing exactly to \(B\). For the SDE
\[
\mathrm dX_t=-A(g)X_t\,\mathrm dt+Q^{1/2}\mathrm dW_t,
\qquad A(g)=L+\operatorname{diag}(g),
\]
the stationary covariance \(\Sigma\) satisfies \(A\Sigma+\Sigma A=Q\). Its trace is \(J(g)/2\); multiplying the objective by two does not change the minimizer. No diagonal-gain symmetry is imposed before optimization. The theorem requires \(m\ge2\), \(\rho>0\), and \(B>0\); zero hub-noise variance, extra edge weights, unequal leaf noise intensities, and dynamic feedback are not claimed.

## Proof

**1. Positivity and uniqueness without imposed symmetry.** Every feasible \(g\) gives a positive definite \(A(g)\). Indeed,
\[
v^\mathsf{T}A(g)v=\sum_{\{u,v\}\in E}(v_u-v_v)^2+\sum_i g_iv_i^2;
\]
if this vanishes, connectivity makes the vector constant and the positive total gain makes it zero. The feasible simplex is compact. For any nonzero diagonal perturbation \(H\),
\[
\frac{\mathrm d^2}{\mathrm dt^2}\operatorname{tr}\bigl[Q(A+tH)^{-1}\bigr]
=2\operatorname{tr}\bigl[Q(A+tH)^{-1}H(A+tH)^{-1}H(A+tH)^{-1}\bigr]>0.
\]
For the positivity, put \(K=(A+tH)^{-1/2}H(A+tH)^{-1/2}\) and \(P=(A+tH)^{-1/2}Q(A+tH)^{-1/2}\succ0\); the trace after the factor two is \(\operatorname{tr}(PK^2)>0\). Thus the objective is strictly convex, and its minimizer is unique. Permuting leaves preserves the graph, \(Q\), budget, and objective; uniqueness therefore forces all leaf gains to be equal.

**2. Exact one-variable formula.** Write the hub gain as \(x\), each leaf gain as \(y=(B-x)/m\), with \(0\le x\le B\). The matrix has block form
\[
A=\begin{pmatrix}m+x&-\mathbf1^\mathsf{T}\\-\mathbf1&(1+y)I_m\end{pmatrix}.
\]
Its Schur-complement determinant is \(D=(m+x)(1+y)-m=my+x(1+y)>0\). Block inversion gives
\[
(A^{-1})_{00}=\frac{1+y}{D},\qquad
\sum_{i=1}^m(A^{-1})_{ii}=\frac{m}{1+y}+\frac{m}{D(1+y)}.
\]
Weighting the hub diagonal by \(\rho\) proves the displayed expression for \(F_{m,\rho,B}\). Strict convexity descends to \(F\). Direct differentiation yields
\[
F'_{m,\rho,B}(B)=\frac{B+2}{B}>0,
\]
so the optimizer never has \(x=B\), and every leaf gain is positive.

**3. The exact hub support criterion.** Differentiating the same rational function at the other endpoint gives
\[
F'_{m,\rho,B}(0)=
\frac{m^3(m-1)B-\rho(B^3+4mB^2+5m^2B+2m^3)}{Bm^2(B+m)^2}.
\]
A differentiable strictly convex function on \([0,B]\) has its unique minimum at the left endpoint exactly when its right derivative there is nonnegative. Hence \(x=0\) precisely when \(\rho\le R_m(B)\). If this fails, the signs of \(F'(0)\) and \(F'(B)\) are opposite, proving existence and uniqueness of the stated interior stationary point.

**4. Sharp phase diagram and golden-ratio cusp.** With \(z=B/m>0\), write
\[
R_m(B)=m(m-1)f(z),\qquad
f(z)=\frac{z}{(z+1)^2(z+2)}.
\]
The derivative is
\[
f'(z)=\frac{2(1-z-z^2)}{(z+1)^3(z+2)^2}.
\]
Thus \(f\) increases strictly to its unique maximum at \(z_*=(\sqrt5-1)/2\), then decreases strictly. Also \(f(0+)=f(+\infty)=0\), and exact simplification gives \(f(z_*)=(5\sqrt5-11)/2\). These facts prove the three stated regimes, including endpoint equality and the tangency case.

**5. Asymptotics and example.** For fixed \(\rho\), \(\rho/[m(m-1)]\to0\), so the smaller root has \(z_-\to0\) and the larger \(z_+\to\infty\). The expansions \(f(z)\sim z/2\) at zero and \(f(z)\sim z^{-2}\) at infinity give the two switching-budget asymptotics. At \(m=2\), \(\rho=1/6\), clearing the support equation yields
\[
B^3+8B^2-28B+16=(B-2)(B^2+10B-8)=0.
\]
Its positive roots are exactly \(\sqrt{33}-5\) and \(2\), giving the claimed three-vertex example.

## Verification

The accompanying self-contained program `verify.py` checks the symbolic endpoint derivatives and golden-ratio identity, the factored exact example, reconstruction of \(\operatorname{tr}(QA^{-1})\) from independently formed full matrices, numerical minimization over the gain simplex after symmetry reduction, and many asymmetric feasible allocations. Running `python verify.py` with NumPy, SciPy, and SymPy installed produced **3,371 passed assertions**. These computations check algebra and representative cases; strict convexity and the calculus argument, not the finite tests, establish the universal theorem.

## Relationship to prior work

Lin, Fardad, and Jovanović (2013, arXiv:1302.0450) formulate stochastic consensus leader selection through an inverse-trace Laplacian objective and relax *Boolean* leader indicators while taking disturbance covariance proportional to the identity. Fitch and Leonard (2014, arXiv:1407.1569) derive fixed-gain leader-set centrality criteria, not optimal continuously divisible feedback under heterogeneous noise. Patterson and Bamieh (2010, DOI:10.1109/CDC.2010.5718151) examine noise-free leader selection; the available description does not establish this variable-gain covariance-weighted classification.

The equal-intensity star case is structurally related to previously obtained uniform-noise complete-bipartite gain allocation; **that special case and generic convexity are not asserted to be new**. The substantive additional result here is the complete two-parameter hub-noise/budget phase diagram, its universal golden-ratio cusp, the exact small-path counterexample, and the two distinct asymptotic switching scales. A specialization of general weighted A-optimal-design theory might recover these formulas; possible equivalent unindexed prior work remains an originality risk.

## Limitations

The theorem concerns continuous-time, fixed unit edges, independent noise with two intensity classes, and linear feedback gains with a single uniform linear budget. It does not establish that similar phase diagrams hold on arbitrary trees, under correlated noise, or for nonlinear control. The optimization-root specification is exact but implicit in interior phases. The polynomial and numerical checks cannot establish originality; the primary-work comparison and available published records support only a best-knowledge, non-exhaustive novelty assessment. Independent validation is not claimed.

## References

1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450, first public preprint 2013-02-03. https://arxiv.org/abs/1302.0450.
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public preprint 2014-07-07. https://arxiv.org/abs/1407.1569.
3. S. Patterson, B. Bamieh, *Leader Selection for Optimal Network Coherence*, IEEE Conference on Decision and Control, 2010, DOI:10.1109/CDC.2010.5718151.

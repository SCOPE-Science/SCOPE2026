# The sharp conditioning frontier for Armijo-before-top-one gradient compression

## Finding
Let \(\sigma\in(0,1)\), \(a>0\), and \(K\ge1\). For any real symmetric positive-definite \(2\times2\) matrix \(Q\) with spectral condition number at most \(K\), consider \(f(x)=\frac12x^\mathsf{T}Qx\), nonzero \(x\), and its gradient \(g=Qx\). First obtain the *largest continuous Armijo-acceptable step* in the full-gradient direction:
\[
\alpha_*=\frac{2(1-\sigma)\|g\|_2^2}{g^\mathsf{T}Qg},\qquad
f(x-\alpha_*g)=f(x)-\sigma\alpha_*\|g\|_2^2.
\]
Let \(i\) be any maximizer of \(|g_1|,|g_2|\), with either tie choice allowed. Then make the first, zero-feedback, top-one-compressed update \(x^+=x-a\alpha_*g_i e_i\). Define
\[
t_K=\frac{K-1}{\sqrt{2K}},\qquad
R(K)=\left(\frac{\sqrt{4+t_K^2}+t_K}{2}\right)^2.
\]
**Sharp universal characterization:** \(f(x^+)\le f(x)\) for every such \(Q,x,i\) **if and only if**
\[
\boxed{\;a(1-\sigma)R(K)\le1.\;}
\]
With strict inequality, every nonzero starting point decreases the objective strictly. If the inequality fails, some \(Q\) with condition number exactly \(K\) and an open set of gradients with a *unique* top-one coordinate make the objective increase. At equality, the nonincrease bound is sharp, attained by a rotated \(Q\) and a tied gradient.

For unscaled compression, \(a=1\), the sharp condition-number threshold is
\[
K_*(\sigma)=A+\sqrt{A^2-1},\qquad
A=1+\frac{\sigma^2}{1-\sigma}.
\]
In particular, \(\sigma=\frac12\) yields \(K_*=\frac{3+\sqrt5}{2}\). Above this value an Armijo-acceptable *full-gradient* step may raise the objective when its update is top-one compressed.

## Assumptions and scope
The line search is an idealized continuous step search that returns its **largest** acceptable step, not a capped or discretely backtracked Armijo trial. The gradient is deterministically full and exact; only its update is sparsified by the two-coordinate top-one operator, with zero accumulated error feedback. The coordinates refer to the basis in which the compressor operates, while \(Q\) may have any eigenvector orientation. The result is one-step, not an assertion about long-run convergence of compressed SGD or subsequent feedback iterates. The parameter \(K\) bounds the eigenvalue ratio of \(Q\) and is at least one.

## Proof
**Step 1 (exact one-step objective test).** Quadratic expansion shows that for every \(\alpha>0\),
\[
f(x-\alpha g)=f(x)-\alpha\|g\|_2^2+\tfrac12\alpha^2 g^\mathsf{T}Qg.
\]
Thus the set of positive full-gradient Armijo steps is \((0,\alpha_*]\), with \(\alpha_*\) as displayed. Another quadratic expansion at the compressed update gives exactly
\[
f(x^+)-f(x)=-a\alpha_*g_i^2\left[1-a(1-\sigma)\frac{Q_{ii}\|g\|_2^2}{g^\mathsf{T}Qg}\right].\tag{1}
\]
Because \(Q\) is nonsingular, every nonzero \(g\in\mathbb R^2\) is realizable by \(x=Q^{-1}g\). Top-one selection guarantees \(g_i\ne0\).

**Step 2 (sharp geometric ratio).** By coordinate interchange and sign reversal, the acute angle \(\theta\) between \(e_i\) and the line spanned by \(g\) lies in \([0,\pi/4]\). Rescale \(Q\) to eigenvalues \(1,\kappa\), where \(1\le\kappa\le K\). If its top eigenvector makes angle \(\phi\) with \(e_i\), then, putting \(b=g/\|g\|\),
\[
r(\phi,\theta)=\frac{Q_{ii}}{b^\mathsf{T}Qb}
=\frac{1+(\kappa-1)\cos^2\phi}{1+(\kappa-1)\cos^2(\phi-\theta)}.
\]
Set \(u=(\kappa+1)/2\), \(v=(\kappa-1)/2\), and write the numerator and denominator as \(u+v\cos2\phi\) and \(u+v\cos(2\phi-2\theta)\). For a candidate maximum \(r\ge1\), the inequality \(r(\phi,\theta)\le r\) for every orientation is equivalent to
\[
u(r-1)\ge v\sqrt{1+r^2-2r\cos(2\theta)}.
\]
The least such \(r\) has equality. Squaring and using \(u^2-v^2=\kappa\) yields
\[
\kappa(r-1)^2=(\kappa-1)^2r\sin^2\theta,
\quad\text{hence}\quad
\sqrt r-\frac1{\sqrt r}=\frac{(\kappa-1)\sin\theta}{\sqrt\kappa}.
\tag{2}
\]
The right-hand side strictly increases in \(\theta\in[0,\pi/4]\) for \(\kappa>1\), and nondecreases with \(\kappa\ge1\). Thus its largest value over all admissible \(Q\) and selected top-one coordinates is \(t_K\); solving (2) gives the exact factor \(R(K)\). The equality orientation exists because the cosine-wave maximum used above is attained on the compact rotation circle. The degenerate \(K=1\) case gives \(R(1)=1\) directly.

**Step 3 (necessity, equality, and tie handling).** Substitute the exact maximum \(R(K)\) into (1). It gives universal nonincrease precisely for \(a(1-\sigma)R(K)\le1\), and strict decrease for the strict inequality. At equality and \(K>1\), choose the maximizing \(\theta=\pi/4\) and the corresponding \(Q\); one tie selection attains zero objective change. For \(K=1\), equality gives zero change for all nonzero gradients. If the bound is violated and \(K>1\), the maximizing ratio exceeds \(1/[a(1-\sigma)]\). Continuity under small perturbations of the tied gradient makes the top-one selection unique while retaining strict increase. If \(K=1\), the same increase follows from (1) for every selected coordinate.

**Step 4 (golden-ratio threshold).** The equality \((1-\sigma)R(K)=1\) is equivalent, by (2), to
\[
\frac{K-1}{\sqrt{2K}}=\frac{\sigma}{\sqrt{1-\sigma}}.
\]
Consequently \(K+K^{-1}=2+2\sigma^2/(1-\sigma)\). Its unique solution \(K\ge1\) is \(K_*(\sigma)=A+\sqrt{A^2-1}\). At \(\sigma=1/2\), \(A=3/2\), which proves the asserted exact boundary.

## Verification
Run \(\texttt{python3 verify.py}\) in the provided folder. It uses only Python's standard library. It independently scans matrix orientations at gradient ties, checks the sharp condition bound for other gradient directions, compares actual quadratic objective values with the predicted safe scaling, and constructs a strict top-one counterexample with condition number three and Armijo parameter one half. The deterministic verifier reports its number of tests. Finite numerical checks supplement, rather than replace, the analytic supremum and universal quantifier proof.

## Relationship to prior work
Subramaniam, Magesh, and Veeravalli introduced scaled Armijo step searches for gradient-compressed SGD with top-\(k\) sparsification and error feedback, and derived general convergence guarantees for sufficiently small scaling parameters. Their step search is capped and backtracked; at zero initial feedback its first update has the same structural composition studied here. The present statement neither describes that full implementation's finite backtracking grid nor competes with its multi-iteration convergence guarantees. It instead computes the **exact sharp spectral-and-orientation one-step frontier** for the ideal maximal full-gradient Armijo step in dimension two. Other established sharp descent frontiers for Polyak, LARS, and Barzilai–Borwein updates concern different step constructions and do not logically imply the above compressed-Armijo factor.

## Limitations
The sharpness theorem is only two-dimensional, deterministic, quadratic, first-step, zero-feedback, and top-one, with exact arithmetic and ideal continuous Armijo maximization. Smaller accepted backtracking steps can avoid the exhibited increase, so this finding does **not** imply that all actual implementations using bounded backtracking diverge. It makes no claim about stochastic gradients, later accumulated feedback, higher-rank compression, or long-run convergence. Earlier equivalent special-case calculations remain a priority risk; no independent audit has been performed.

## References
1. A. M. Subramaniam, A. Magesh, and V. V. Veeravalli, *Adaptive Step-Size Methods for Compressed SGD*, arXiv:2207.10046v1 (first posted 2022-07-20), Sections II–IV and theoretical results in Section III. https://arxiv.org/abs/2207.10046
2. General background: J. Nocedal and S. J. Wright, *Numerical Optimization*, 2nd ed., Springer (2006), Chapter 3 (Armijo line search).

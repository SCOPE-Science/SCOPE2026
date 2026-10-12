# Boundary-only feasibility forces slack escape in exponential-slack I-LMM
## Finding
Consider the scalar inequality
\[
F(x)=x^2\le 0.
\]
Its feasible set is the singleton \(\{0\}\). Apply Algorithm I-LMM of Ren and Tang to the paper's exponential-slack equation
\[
\Phi(x,t)=x^2+e^t=0
\]
with the source-admissible parameters \(\rho,\gamma\in(0,1)\), \(\theta>0\), \(\delta\in[1,2]\), any positive summable sequence \((\zeta_k)\), initialization \(x_0=0\), and arbitrary finite \(t_0\).

Then, for every finite \(k\),
\[
x_k=0,\qquad \Phi(x_k,t_k)=e^{t_k}>0.
\]
Hence the algorithm's exact Step 1 stopping test is never satisfied. Nevertheless,
\[
t_k\longrightarrow-\infty
\qquad\text{and}\qquad
\|\Phi(x_k,t_k)\|=e^{t_k}\longrightarrow0.
\]
Thus the original variable is an exact solution throughout the run, while the auxiliary exponential slack must escape to infinity in magnitude before the transformed residual can vanish asymptotically.

## Assumptions and scope
The statement concerns the exact theoretical Algorithm I-LMM in the 2026 paper, not a tolerance-based implementation. The scalar map \(F(x)=x^2\) is continuously differentiable and satisfies the paper's base model \(F(x)\le0\). No strict feasible point exists.

Write
\[
r_k=e^{t_k}>0,
\qquad
\mu_k=\theta r_k^\delta,
\qquad
s_k=\frac{r_k^2}{r_k^2+\theta r_k^\delta}
     =\frac{r_k^{2-\delta}}{r_k^{2-\delta}+\theta}.
\]
The proof uses only the published direction equation, geometric line search, and update rule.

## Proof
At \(x_k=0\), the transformed residual and Jacobian are
\[
\Phi(0,t_k)=r_k,
\qquad
\Phi'(0,t_k)=\begin{bmatrix}0&r_k\end{bmatrix}.
\]
The scalar system in Step 2 therefore gives
\[
(r_k^2+\mu_k)h_k=-r_k,
\qquad
h_k=-\frac{r_k}{r_k^2+\mu_k}.
\]
Consequently
\[
d_k=\Phi'(0,t_k)^{\mathsf T}h_k
   =\begin{bmatrix}0\\-s_k\end{bmatrix},
\qquad 0<s_k<1.
\]
Every accepted update therefore preserves the original variable exactly and changes only the slack coordinate:
\[
x_{k+1}=0,
\qquad
t_{k+1}=t_k-\lambda_k s_k,
\]
where \(\lambda_k=\rho^{l_k}>0\). Induction yields \(x_k=0\) for all \(k\). Since every finite \(t_k\) has \(e^{t_k}>0\), Step 1 can never stop exactly.

It remains to prove \(t_k\to-\infty\). The published line-search test, specialized to this trajectory and divided by \(r_k>0\), is
\[
e^{-\lambda s_k}
\le
1+\zeta_k-\gamma\lambda^2 r_k.
\]
For \(0\le u\le1\), the elementary estimate \(e^{-u}\le1-u/2\) holds. Hence every trial \(\lambda\) satisfying
\[
\lambda s_k\le1,
\qquad
\gamma\lambda r_k\le\frac{s_k}{2}
\]
is accepted, independently of the value of \(\zeta_k>0\).

Suppose for contradiction that \((t_k)\) were bounded below. It is decreasing, so then \(r_k\) would remain in a compact interval
\[
0<r_{\min}\le r_k\le r_{\max}<\infty.
\]
The continuous function
\[
s(r)=\frac{r^{2-\delta}}{r^{2-\delta}+\theta}
\]
would then have a positive lower bound \(s_{\min}>0\). Choose
\[
\bar\lambda
=
\min\!\left\{1,\frac{s_{\min}}{2\gamma r_{\max}}\right\}>0.
\]
Every geometric trial with \(\lambda\le\bar\lambda\) is accepted. Therefore the smallest accepted backtracking index is uniformly bounded, so there is a constant \(\lambda_{\min}>0\) with \(\lambda_k\ge\lambda_{\min}\) for all \(k\). It follows that
\[
t_{k+1}
\le
t_k-\lambda_{\min}s_{\min},
\]
which contradicts the assumed lower bound. Thus \(t_k\to-\infty\), and consequently \(e^{t_k}\to0\).

Finally, because \(e^t>0\) for every finite real \(t\), a finite root of \(F(x)+e^t=0\) necessarily satisfies \(F(x)<0\). Therefore this exponential-slack equation represents strict feasibility. The boundary-only system \(x^2\le0\) has no finite transformed root.

## Verification
The algebra above reconstructs the exact source update. A finite numerical replay is included only as a consistency check; it is not used to prove the infinite statement. The proof of nontermination uses positivity of \(e^t\) at every finite \(t\), and the proof of slack escape uses a uniform line-search acceptance bound under the contrary assumption that \(t_k\) is bounded below.

The source paper's Theorem 3.1 is consistent with the result: it states that any finite accumulation point \((x^*,t^*)\) of I-LMM satisfies \(\Phi(x^*,t^*)=0\), hence \(F(x^*)<0\). The trajectory above has no finite accumulation point in the slack coordinate.

## Relationship to prior work
Ren and Tang introduce \(\Phi(x,t)=F(x)+e^t\), describe it as a route from inequalities to equations, and apply I-LMM to this transformed system. Their paper states the forward implication from a transformed root to a feasible inequality point and proves that any finite accumulation point is in fact strictly feasible. It does not state the exact boundary trajectory above, the invariant \(x_k=0\), or the conclusion \(t_k\to-\infty\) when the original feasible set has no strict point.

Earlier smoothing methods for nonlinear inequalities, such as Che's 2012 predictor-corrector method, use a boundary-preserving nonsmooth/smoothing reformulation and establish convergence to solutions of the non-strict system under their own assumptions. That literature does not imply the source-specific I-LMM recurrence or its auxiliary-slack escape.

Targeted searches for exponential-slack inequality reformulations, boundary-only feasibility, Levenberg--Marquardt nontermination, and this scalar trajectory did not locate a published statement implying the result.

## Limitations
This is a structural boundary example for the exact theoretical I-LMM. It does not claim that tolerance-based implementations fail to stop, nor that I-LMM fails on systems with a strict feasible point. It does not contradict the paper's accumulation-point theorem, because the auxiliary coordinate diverges and hence the full sequence has no finite accumulation point. The claim is restricted to the scalar boundary-only system \(F(x)=x^2\) and the paper's stated parameter ranges.

## References
1. K. Ren and J. Tang, *A computationally improved Levenberg−Marquardt method for systems of inequalities*, Journal of Industrial and Management Optimization 22 (2026), 3175--3187, DOI: 10.3934/jimo.2026116.
2. H. Che, *A smoothing and regularization predictor-corrector method for nonlinear inequalities*, Journal of Inequalities and Applications 2012, Article 214, DOI: 10.1186/1029-242X-2012-214.

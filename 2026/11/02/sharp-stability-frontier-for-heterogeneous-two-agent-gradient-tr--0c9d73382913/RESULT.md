# Sharp stability frontier for heterogeneous two-agent gradient tracking

## Finding

Consider two agents with the symmetric doubly stochastic mixing matrix
\[
W_\lambda=\frac12\begin{pmatrix}1+\lambda&1-\lambda\\1-\lambda&1+\lambda\end{pmatrix},\qquad 0<\lambda<1,
\]
and strictly convex scalar local objectives \(f_1(x)=(1+e)x^2/2\), \(f_2(x)=(1-e)x^2/2\), where \(0\le e<1\). The average local curvature is one and the curvature dispersion is \(e\). Run constant-stepsize distributed gradient tracking (DGT)
\[
x_{k+1}=W_\lambda(x_k-\beta y_k),\qquad
 y_{k+1}=W_\lambda y_k+H(x_{k+1}-x_k),\quad
 H=\operatorname{diag}(1+e,1-e),\quad y_0=Hx_0,
\]
for \(0<\beta<2\). Define
\[
 B_*(\lambda,e)=\frac{4(1+\lambda)^2}{1+6\lambda+\lambda^2+\sqrt{(1-\lambda)^4+16e^2\lambda(1+\lambda)^2}}.
\]
For every \(0<\lambda<1\) and \(0\le e<1\), **DGT converges to the common minimizer zero from every admissible initial position if and only if** \(0<\beta<B_*(\lambda,e)\). At \(\beta=B_*(\lambda,e)\), the reduced error matrix has a simple eigenvalue \(-1\), and an admissible initial position excites its nonconvergent mode. For \(B_*(\lambda,e)<\beta<2\), it has a real eigenvalue strictly below \(-1\), excited by generic admissible initial positions.

For \(e=0\), \(B_*(\lambda,0)=2\). Every strictly positive curvature contrast \(e>0\) lowers the sharp stability ceiling below two. The joint slow-mixing and small-contrast behavior is nonuniform:
\[
\lim_{\lambda\uparrow1}B_*(\lambda,e)=\frac{2}{1+e},\qquad
B_*(\lambda,e)=2-\frac{8\lambda}{(1-\lambda)^2}e^2+O_\lambda(e^4)
\quad(e\downarrow0).
\]
The complete-graph limit is \(\lim_{\lambda\downarrow0}B_*(\lambda,e)=2\).

In particular, with \(\lambda=e=1/2\), the threshold is \((17-\sqrt{73})/6\). The homogeneous-curvature iteration is stable at \(\beta=3/2\), but the heterogeneous iteration has characteristic polynomial
\[
z^3+\tfrac14z^2-\tfrac{29}{32}z+\tfrac1{32}
\]
with a real root below \(-1\).

## Assumptions and scope

All assertions are in exact arithmetic. There are exactly two agents, identical positive constant stepsizes \(\beta\), connected symmetric mixing with strictly positive second eigenvalue \(\lambda\), positive curvatures \(1\pm e\), and prescribed gradient-tracker initialization \(y_0=Hx_0\). The interval \(0<\beta<2\) is the natural constant-step search interval in the motivating work. No conclusion is asserted for other network eigenvalue signs, more agents, time-varying stepsizes, nonlinear objectives, or \(\beta\ge2\).

## Proof

**Reduced dynamics.** Let \(v=(1,1)^{\mathsf T}/\sqrt2\), \(u=(1,-1)^{\mathsf T}/\sqrt2\), and write \(x_c=v^{\mathsf T}x\), \(x_d=u^{\mathsf T}x\). Scale the tracker by \(\widetilde y=\beta y\) and write its consensus/disagreement components as \(y_c,y_d\). The nontrivial reduced state \((y_c,x_d,y_d)^{\mathsf T}\) evolves under
\[
M_{\beta,\lambda,e}=\begin{pmatrix}
1-\beta&\beta e(\lambda-1)&-\beta e\lambda\\
0&\lambda&-\lambda\\
-\beta e&\beta(\lambda-1)&(1-\beta)\lambda
\end{pmatrix}.
\]
The untouched consensus coordinate satisfies \(x_{c,k+1}=x_{c,k}-y_{c,k}\). Gradient-tracker initialization preserves \(y_{c,k}=\beta(x_{c,k}+e x_{d,k})\). Consequently convergence of the reduced state to zero implies \(x_k\to0\).

**Characteristic polynomial and the only possible crossing.** Write \(P(z)=\det(zI-M)=z^3+a z^2+b z+c\). Direct expansion gives
\[
\begin{aligned}
a&=\beta(1+\lambda)-1-2\lambda,\\
b&=\beta^2\lambda(1-e^2)-4\beta\lambda+\lambda^2+2\lambda,\\
c&=-\beta^2\lambda(1-e^2)+\beta\lambda(1+\lambda)-\lambda^2.
\end{aligned}
\]
Thus \(P(1)=\beta(1-\lambda)^2>0\) and
\[
-P(-1)=Q(\beta)=2\lambda(1-e^2)\beta^2-(1+6\lambda+\lambda^2)\beta+2(1+\lambda)^2.
\]
Define the cubic Schur crossing invariant \(S=1-b+ac-c^2\). Put \(u=e^2\). Since \(b\) and \(c\) are affine in \(u\), with \(c\)'s slope equal to \(\beta^2\lambda\), the coefficient of \(u^2\) in \(S\) is \(-\beta^4\lambda^2\); hence \(S\) is concave in \(u\in[0,1]\). Its two endpoint identities are
\[
S|_{u=0}=(1-\lambda^2+\beta\lambda)H_0,
\]
where
\[
H_0=(1-\lambda)^2+2\beta\lambda(1-\lambda)+\beta^2\lambda(1+\lambda-\beta),
\]
and
\[
S|_{u=1}=(1-\lambda)\bigl[\beta^2\lambda(1+\lambda)^2+\beta\lambda(1-\lambda)(2\lambda+3)+(1-\lambda)^2(1+\lambda)\bigr]>0.
\]
For \(0<\beta\le1+\lambda\), each term in \(H_0\) is nonnegative and the first is strictly positive. On \(1+\lambda\le\beta\le2\), \(\partial_\beta^2 H_0=2\lambda(1+\lambda-3\beta)<0\). Concavity puts the minimum at an endpoint; \(H_0(1+\lambda)>0\) and \(H_0(2)=(1-\lambda)^2>0\). Therefore \(S>0\) throughout \(0<\lambda<1\), \(0<\beta<2\), \(0\le e<1\).

If a real monic cubic has a nonreal conjugate pair on the unit circle, factor it as \((z^2-2t z+1)(z-r)\), with \(-1<t<1\). Its coefficients necessarily satisfy \(1-b+ac-c^2=0\). Thus \(S>0\) excludes *every* nonreal unit-circle crossing. Since \(P(1)>0\), the only possible unit-circle crossing as \(\beta\) varies is \(z=-1\).

**Determination of the frontier.** At \(\beta\downarrow0\) the eigenvalues tend to \(1,\lambda,\lambda\), and the simple eigenvalue near one has expansion \(1-\beta+O(\beta^2)\). Hence sufficiently small positive \(\beta\) is Schur stable. The discriminant of \(Q\) is
\[
\Delta=(1-\lambda)^4+16e^2\lambda(1+\lambda)^2.
\]
The smaller positive root of \(Q\) is precisely \(B_*(\lambda,e)\), after rationalizing the quadratic formula. For \(e>0\), \(Q(0)>0\) and \(Q(2)=-8e^2\lambda<0\), so the second root lies beyond two and \(Q\) changes from positive to negative exactly at \(B_*\) inside \((0,2)\). For \(e=0\), the smaller root is two and \(Q>0\) throughout \((0,2)\). Eigenvalues vary continuously, and the preceding unit-circle exclusion proves Schur stability precisely for \(0<\beta<B_*\). At the boundary \(P(-1)=0\); it is a simple root because a double root at \(-1\) would also force \(S=0\). Above the boundary, \(P(-1)>0\) and \(P(z)\to-\infty\) for real \(z\to-\infty\), so a real eigenvalue lies below \(-1\).

**Admissible initialization is not a loophole.** The prescribed starting states of the reduced system form the range of
\[
T=\begin{pmatrix}\beta&\beta e\\0&1\\\beta e&\beta\end{pmatrix},
\]
acting on \((x_{c,0},x_{d,0})\). If a nonzero left eigenvector were orthogonal to both columns, it would have to be proportional to \(w=(-e,-\beta(1-e^2),1)^{\mathsf T}\). Yet
\[
M^{\mathsf T}w=(-e,-\beta(1-e^2),\lambda)^{\mathsf T},
\]
which is not an eigenvector relation for \(\lambda<1\): the first two entries require eigenvalue one (at least one is nonzero), while the third requires eigenvalue \(\lambda\). Thus every eigenmode, including the critical/unstable mode, is excited by some admissible initial position, and all but a proper linear subset of initial positions excite any specified simple eigenmode. Such modes affect positions through the disagreement update or the consensus identity above.

**Limits.** The stated complete-graph and slow-mixing limits follow directly from the closed formula. For fixed \(0<\lambda<1\), a Taylor expansion of the square root at \(e=0\) gives the quadratic contrast correction.

## Verification

The standalone `verify.py` checks the characteristic determinant, endpoint values, two positive Schur-factor identities, the quadratic discriminant, physical-initialization left-eigenvector identity, and the exact rational witness. It also compares the full cubic Schur conditions to the stated threshold in 5,400 deterministic exact-rational parameter tests. The verification code is supplementary to the infinite-parameter proof; finite samples are not an exhaustive certificate of the theorem.

## Relationship to prior work

Wang, Ballotta, Carli, Iannelli, Cao and Schenato (2026) derive the DGT reduced matrix, a general sufficient convergence certificate, and exact optimum stepsizes in complete-graph or homogeneous-curvature regimes; their heterogeneous-network treatment is a sufficient bound with numerical tuning, not the exact positive-second-eigenvalue, two-agent stability frontier above. The full statement and proof of the closely related public sign-aware graph-specific result were inspected; its homogeneous-curvature hypothesis precludes an implication to a positive-contrast stability frontier. Tian, Chai and Xu (2026) study exact worst-case rates for DIGing and AugDGM across function and network classes, rather than the exact stability boundary for this fixed two-agent heterogeneous adapt-then-combine update; their accessible abstracts do not settle this claim, and the unavailable full texts remain a priority risk. Classical cubic Schur stability is used as context, not claimed as new.

## Limitations

No floating-point stability guarantee, finite-precision convergence rate, varying-stepsize result or arbitrary-network extension follows. The endpoint \(\beta=B_*\) is nonconvergent for some valid starts, rather than exponentially divergent. The 2023 integral-action interpretation and other general distributed tracking literature have not been exhaustively checked for an equivalent specialized expression; the available abstracts provide no decisive covering statement. Historical priority is therefore subject to independent literature review. No independent mathematical audit has been performed.

## References

1. Y. Wang, L. Ballotta, R. Carli, A. Iannelli, X. Cao and L. Schenato, *Adaptive Stepsizes With Certified Convergence in Distributed Gradient Tracking With Quadratic Costs*, arXiv:2608.03548v1 (2026-08-04), https://arxiv.org/abs/2608.03548.
2. *Exact sign-aware graph-specific tuning for homogeneous distributed gradient tracking*, public published-finding corpus record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-sign-aware-graph-specific-tuning-for-homogeneous-distribut--4bef30512fd6. Its full `RESULT.md` was inspected; it assumes uniform scalar curvature.
3. Q. Tian, L. Chai and J. Xu, *Exact Worst-case Convergence Rates of Distributed Gradient Tracking Methods*, arXiv:2607.23601v1 (2026-07-26), https://arxiv.org/abs/2607.23601 (abstract inspected; full text not retrieved).
4. I. Notarnicola, M. Bin, L. Marconi and G. Notarstefano, *The Gradient Tracking Is a Distributed Integral Action*, IEEE Transactions on Automatic Control 68 (2023), 7911–7918, https://doi.org/10.1109/TAC.2023.3248487 (abstract inspected; full text not confirmed).

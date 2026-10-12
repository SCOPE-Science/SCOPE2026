# Sharp dual-stepsize stability frontier for constant-parameter quadratic APAPC

## Finding

Consider the accelerated proximal alternating predictor–corrector (APAPC) update of Condat, Sadiev, and Richtárik [1], with constant averaging parameter \(a\geq1\), applied in finite dimensions to
\[
\min_{x\in\mathbb R^n}\;\frac{\mu}{2}\|x\|^2+\frac{\lambda}{2}\|Kx\|^2,
\qquad \mu>0,\quad\lambda>0,\quad K\in\mathbb R^{m\times n}.
\]
For arbitrary fixed \(\gamma,\tau>0\), every primal, dual, and auxiliary iterate converges to the unique zero saddle point for every initialization permitted by APAPC **if and only if**
\[
\boxed{\gamma\tau\|K\|_2^2<
\frac{(1+a\gamma\mu)(2+a\gamma\mu)
(2+\tau/(a\lambda))}{3+a\gamma\mu}.}
\tag{1}
\]
At equality (when \(K\ne0\)) there is a scalar singular-vector initialization with a nondecaying alternating mode. If the left side exceeds the right side, some initialized trajectory diverges exponentially. Thus the inequality is both necessary and sufficient, not merely a rate certificate.

Set
\[
B=\frac{(1+a\gamma\mu)(2+a\gamma\mu)}{3+a\gamma\mu},
\qquad L=\|K\|_2.
\]
The exact phase diagram in the dual step \(\tau\) is: when \(\gamma L^2\leq B/(a\lambda)\), **every finite** \(\tau>0\) converges; otherwise convergence holds exactly for
\[
0<\tau<\frac{2B}{\gamma L^2-B/(a\lambda)}.
\tag{2}
\]
In particular, for \(a=\gamma=\mu=\lambda=L=1\) all finite dual steps are stable, although the standard sufficient coupling bound in [1] would restrict \(\tau\leq2\). This identifies a strongly regularized regime in which no finite upper bound on the dual step is necessary for convergence of the quadratic iteration.

## Assumptions and scope

All vector spaces are finite-dimensional real Euclidean spaces. The nonsmooth/smooth splitting is precisely \(f\equiv0\), \(g(x)=\mu\|x\|^2/2\), \(h(w)=\lambda\|w\|^2/2\), with \(\mu,\lambda>0\). Its conjugate is \(h^*(v)=\|v\|^2/(2\lambda)\). Although \(f\equiv0\) has minimal gradient Lipschitz constant zero, it satisfies the source paper's formal upper-bound hypothesis with any chosen \(L_f\geq\mu\). The fixed positive primal and dual steps are \(\gamma\) and \(\tau\); the parameter is \(a_t=a\geq1\) for every iteration. Initial values satisfy the algorithm's standard \(x^0=z^0\), \(u^0=v^0\); no further restrictions are imposed. The optional averaged dual variable \(u^t\) is included in the convergence claim. When \(K=0\), the strict inequality in (1) holds automatically. No assumption of full row/column rank is needed.

The unique primal–dual saddle point is \((0,0)\); this follows from positive curvature of both the primal term and the dual conjugate. The claim concerns **iterates** of this fixed-parameter, exactly computed quadratic algorithm, not arbitrary convex functions, time-varying acceleration parameters, or objective monotonicity at each step.

## Proof

**1. Exact update.** Define \(r=(1+a\gamma\mu)^{-1}\), \(d=(1+\tau/(a\lambda))^{-1}\), both strictly between zero and one. As \(f\equiv0\), the predictor, dual proximal step, and corrector in Algorithm 1 of [1] reduce exactly to
\[
\hat z=r(z-a\gamma K^\top v),\qquad
v^+=d\big(v+(\tau/a)K\hat z\big),\qquad
z^+=r(z-a\gamma K^\top v^+).
\tag{3}
\]
The averaged outputs obey \(x^+=(1-1/a)x+z^+/a\) and, optionally, \(u^+=(1-1/a)u+v^+/a\).

**2. Singular-mode decomposition.** Orthogonal singular-vector changes of variables decouple (3). For any singular value \(s\geq0\), put \(b_s=\tau s/a\), \(c_s=a\gamma s\), and \(m_s=b_sc_s=\gamma\tau s^2\). The associated two-dimensional pair evolves under
\[
M_s=\begin{pmatrix}
r(1-dm_s r)&-r c_s d(1-m_s r)\\
d b_s r&d(1-m_s r)
\end{pmatrix}.
\tag{4}
\]
For unmatched nullspace directions the one-dimensional factors are \(r\) or \(d\), both in \((0,1)\). Therefore stability of all core iterates is equivalent to \(\rho(M_s)<1\) for every nonzero singular value.

**3. Exact Schur criterion.** The characteristic polynomial of (4) is \(\xi^2-T_s\xi+D_s\), where
\[
T_s=r+d-dm_s r(1+r),\qquad D_s=rd(1-m_s r).
\]
For a real monic quadratic, both roots have modulus strictly below one if and only if \(1-T_s+D_s>0\), \(1-D_s>0\), and \(1+T_s+D_s>0\). Direct substitution yields
\[
\begin{aligned}
1-T_s+D_s&=(1-r)(1-d)+d m_s r>0,\\
1-D_s&=1-rd+d m_s r^2>0,\\
1+T_s+D_s&=(1+r)(1+d)-d m_s r(1+2r).
\end{aligned}
\tag{5}
\]
The first two are always strictly positive for the stated assumptions, including \(m_s=0\). The third is positive precisely when
\[
m_s<\frac{(1+r)(1+d)}{dr(1+2r)}
=\frac{(1+a\gamma\mu)(2+a\gamma\mu)(2+\tau/(a\lambda))}{3+a\gamma\mu}.
\tag{6}
\]
The right-hand side is independent of \(s\). Since \(m_s=\gamma\tau s^2\) is increasing in \(s^2\), testing the largest singular value alone proves (1). Once \(z^t,v^t\to0\), the output recurrences converge to zero because \(1-1/a\in[0,1)\). Conversely, convergence of every iterate for every initialization requires every \(M_s\) to be Schur stable.

**4. Necessity and sharpness.** If equality holds for a nonzero largest singular value, then (5) gives \(1+T_s+D_s=0\), so \(\xi=-1\) is an eigenvalue. A corresponding nonzero real eigenvector provides a permitted initial \((z^0,v^0)\) with nondecaying alternation. If the inequality is violated, the real polynomial is negative at \(\xi=-1\) and positive as \(\xi\to-\infty\), so it has a root strictly below \(-1\); the associated trajectory diverges. These witnesses persist in a scalar \(1\times1\) matrix and respect \(x^0=z^0\), \(u^0=v^0\). This proves both directions of the strict condition.

**5. Unbounded-dual-step phase.** Rewriting (1) as \(\tau(\gamma L^2-B/(a\lambda))<2B\) gives the two regimes in (2), with the weak boundary \(\gamma L^2=B/(a\lambda)\) belonging to the all-finite-steps regime. No limiting value \(\tau=+\infty\) is part of the algorithm.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic to compare the independently expanded update (3), its mode matrix (4), the characteristic coefficients, all three Schur expressions (5), and the threshold in (6) across a deterministic parameter grid. It also verifies an exactly critical scalar witness \((a,\gamma,\mu,\lambda,s,\tau)=(1,1,1,1,2,6/5)\), for which \(\det(I+M_s)=0\), and verifies the claimed all-dual-step example for selected rational steps. A further independent 3,000-case floating-point eigenspectrum test was performed during derivation. The proof above, rather than finite tests, establishes the universal statement.

For an immediate reproducible check with only Python's standard library, run `python verify.py`; successful execution prints `VERIFY_OK`.

## Relationship to prior work

Condat, Sadiev, and Richtárik [1, Algorithm 1 and Theorem 3.3] introduced APAPC and supplied sufficient Lyapunov step conditions, including \(\gamma\tau\|K\|^2\leq1+a\gamma\mu\) in the corresponding constant-parameter setting. The present result fixes the exact two-curvature quadratic case and determines the **necessary-and-sufficient** boundary, which can allow arbitrarily large dual steps. It does not relax [1]'s conditions for general convex composite objectives.

The earlier PAPC/PDFP\(^{2}\)O analyses of Li and Yan [2] and Li and Yan [3] already established the sharp generic \(4/3\) coupling obstruction and the relevant two-dimensional eigenvalue mechanism when both proximal curvatures vanish. The boundary in (6) tends to that known \(4/3\) value as \(\mu\downarrow0\) and \(\lambda\uparrow\infty\) with \(a=1\). Thus the undamped endpoint and the basic spectral mechanism are credited, not claimed as new. Luke and Shefi [4] established PAPC linear convergence under supportability and rank assumptions but did not provide this exact finite-curvature, fixed-parameter stability phase diagram.

## Limitations

The statement concerns \(f\equiv0\) and strictly positive *isotropic* primal and dual quadratic curvatures. Because the smooth gradient is zero, the predictor–corrector core decouples from the Nesterov extrapolated evaluation point; the result is not a proof of acceleration when \(f\ne0\). It is a convergence threshold, not an optimal spectral rate or finite-time estimate, and says nothing about nonlinear or nonsmooth penalties, nonautonomous choices of \(a_t\), noisy proximal evaluations, infinite-dimensional operators, or all choices of initial values at the critical equality. Historical equivalent parametrizations may exist in the broad primal–dual splitting literature.

## References

[1] L. Condat, A. Sadiev, and P. Richtárik, *A Nesterov-Accelerated Primal–Dual Splitting Algorithm for Convex Nonsmooth Optimization*, arXiv:2604.09245v1, first public 2026-04-10. https://arxiv.org/html/2604.09245v1

[2] Y. Li and M. Yan, *On the improved conditions for some primal-dual algorithms*, arXiv:2201.00139v1, first public 2022-01-01. https://arxiv.org/html/2201.00139v1

[3] Z. Li and M. Yan, *New convergence analysis of a primal-dual algorithm with large stepsizes*, arXiv:1711.06785, first public 2017-11-18. https://arxiv.org/html/1711.06785v2

[4] D. R. Luke and R. Shefi, *A Globally Linearly Convergent Method for Pointwise Quadratically Supportable Convex-Concave Saddle Point Problems*, arXiv:1702.08770, first public 2017-02-28. https://arxiv.org/html/1702.08770v1

# Rank-one immunity and a sharp rank-two positivity transition in projected exponential Lyapunov integration

## Finding
Consider the one-step projected exponential Euler method of Carrel--Vandereycken [1] with exact matrix functions and best-Frobenius-rank truncation. On the stable matrix Lyapunov flow
\[
\dot X=-2aX+C,\qquad a\geq0,\quad C\succeq0,\quad X(0)=Y\succeq0,
\]
its one-step map is \(\mathcal E_{h,r}(Y)=\mathcal T_r(sY+q\mathcal P_Y C)\), where \(s=e^{-2ah}\), \(q=(1-s)/(2a)\) for \(a>0\), and \(s=1,q=h\) for \(a=0\). The rank-one map always preserves positive semidefiniteness for every \(h>0\) and every \(C\succeq0\). In contrast, every rank \(r\geq2\) with ambient dimension \(n\geq r+1\) admits a strictly positive rank-\(r\) initial covariance, a rank-one \(C\succeq0\), and a step producing a strictly negative numerical eigenvalue, although the exact covariance is positive semidefinite.

The first failure occurs for \(r=2,n=3\), and admits a complete sharp classification. Set \(Y=\operatorname{diag}(d,e,0)\), \(d,e>0\), \(C=vv^{\mathsf T}\), \(v=(1,0,1)^{\mathsf T}\), and \(t=q/s\). Define
\[
 b(t)=\frac{\sqrt{(d+t)^2+4t^2}-(d+t)}{2},\qquad
 t_*=\frac{e+\sqrt{4de+5e^2}}2.
\]
For \(0<h<h_*\), every best rank-two truncation is positive semidefinite; for \(h>h_*\), its uniquely determined matrix is indefinite, with minimum eigenvalue \(-s b(t)\). Here
\[
 h_*=\begin{cases}t_*,&a=0,\\(2a)^{-1}\log(1+2at_*),&a>0.\end{cases}
\]
At \(h=h_*\), positive-semidefinite and indefinite best-rank-two truncations both exist, so positive semidefiniteness is not guaranteed without a tie convention. For \(h>h_*\), the optimal unrestricted Frobenius rank-two truncation error is \(se\), whereas the optimal positive-semidefinite rank-at-most-two approximation error to the same intermediate matrix is \(s b(t)\). Their ratio \(b(t)/e\) is unbounded as \(e\downarrow0\) at fixed \(a,d,h>0\).

## Assumptions and scope
All matrices are real symmetric; \(h>0\), \(a\geq0\), and all operations are exact. The ambient space is \(n\times n\), and \(\mathcal M_r\) denotes matrices of rank \(r\). The orthogonal Frobenius tangent projector for a symmetric positive-semidefinite matrix of rank \(r\), with range projector \(P\), is
\[
\mathcal P_Y C=PC+CP-PCP.
\]
The operator \(\mathcal T_r\) is a best rank-at-most-\(r\) approximation in Frobenius norm obtained by truncated singular value decomposition; it need not be positive semidefinite. Uniqueness statements refer to the truncated matrix, not its singular vectors. At a tie, \(\mathcal T_r\) is set-valued. The scalar negative drift \(-aI\) on both sides of the Lyapunov operator is included for all \(a\geq0\), including arbitrarily strong damping. No inference is made about arbitrary noncommuting drift matrices, different low-rank integrators, or finite-precision rounding.

## Proof
**Step 1: Reduction of the published update.** In [1, equation (31)], take the Sylvester operator \(\mathcal L X=(-aI)X+X(-aI)=-2aX\) and constant \(\mathcal G(X)=C\). Since \(h\varphi_1(-2ah)=q\), the intermediate matrix equals
\[
W=sY+q\mathcal P_YC=s(Y+t\mathcal P_YC),\qquad t=q/s>0.
\]
For \(a>0\), \(t=(e^{2ah}-1)/(2a)\); for \(a=0\), \(t=h\). The exact solution \(X(h)=sY+qC\) is positive semidefinite because \(s,q>0\).

**Step 2: Universal rank-one safety.** Write \(Y=\sigma uu^{\mathsf T}\) with \(\sigma>0\) and \(\|u\|=1\), and set \(c=u^{\mathsf T}Cu\geq0\), \(w=(I-uu^{\mathsf T})Cu\). In an orthonormal basis beginning with \(u\) and, when nonzero, \(w/\|w\|\), the nonzero block of \(Y+t\mathcal P_Y C\) is
\[
\begin{pmatrix}\sigma+tc&t\|w\|\\t\|w\|&0\end{pmatrix}.
\]
Its two possibly nonzero eigenvalues are \(\frac12(z\pm\sqrt{z^2+4t^2\|w\|^2})\) with \(z=\sigma+tc>0\). The positive eigenvalue has strictly larger magnitude than the negative one. Hence the best rank-one SVD truncation is uniquely positive semidefinite. Multiplication by \(s>0\) does not change this conclusion.

**Step 3: Exact rank-two spectrum.** For the specified three-dimensional family, \(P=\operatorname{diag}(1,1,0)\) and
\[
R=Y+t\mathcal P_YC=\begin{pmatrix}d+t&0&t\\0&e&0\\t&0&0\end{pmatrix}.
\]
Its three eigenvalues are \(p(t)>0\), \(e>0\), and \(-b(t)<0\), with
\[
p(t)=\frac{d+t+\sqrt{(d+t)^2+4t^2}}2>b(t)>0.
\]
The SVD retains the two largest absolute eigenvalues and reconstructs their original signs. Consequently the second retained eigenvalue is \(e\) if \(e>b(t)\) and \(-b(t)\) if \(e<b(t)\). At equality, either eigenmode is a Frobenius-optimal rank-two choice.

**Step 4: Sharp threshold.** Rationalization gives \(b(t)=2t^2/[\sqrt{(d+t)^2+4t^2}+d+t]\). The equation \(b(t)=e\) is equivalent, without spurious roots for positive parameters, to \(t^2=e(d+t+e)\). Its quadratic has exactly one positive root, namely \(t_*\). Because \(t(h)\) is continuous and strictly increasing from zero to infinity, the transition in \(h\) occurs exactly at the stated \(h_*\). For \(h>h_*\), the smallest eigenvalue after truncation is \(-s b(t)\), which is strictly negative. For \(h<h_*\), the retained eigenvalues are positive. The full covariance remains \(sY+qC\succeq0\) throughout.

**Step 5: Minimality and arbitrary ranks.** In ambient dimension at most two, every proper positive rank is one, already covered by Step 2; full-rank truncation has no effect and returns \(sY+qC\succeq0\). Thus dimension three and rank two are minimal. For any \(r\geq2\) and \(n\geq r+1\), embed the three-dimensional construction with \(C=vv^{\mathsf T}\) supported on coordinates \(1,r+1\), and choose \(Y\) diagonal with positive values \(d,e,d_3,\ldots,d_r\) on coordinates \(1,2,3,\ldots,r\). Choose \(0<e<\min\{b(t),d_3,\ldots,d_r\}\), omitting the last set for \(r=2\). The intermediate spectrum consists of \(p(t),-b(t),e,d_3,\ldots,d_r\) and zeros. Truncation to rank \(r\) discards \(e\) and necessarily retains \(-b(t)\), proving the claimed failure in every admissible rank and dimension.

**Step 6: Repair cost and small-eigenvalue scaling.** For \(h>h_*\), the best unconstrained rank-two approximation drops \(se\), so its Frobenius error is \(se\). The nearest positive-semidefinite matrix of rank at most two retains the eigenmodes with eigenvalues \(sp(t)\) and \(se\) and deletes \(-sb(t)\), giving error \(sb(t)\). The ratio \(b(t)/e\) diverges as \(e\downarrow0\) with \(h,a,d\) fixed. Also \(t_*=\sqrt{de}+O(e)\), and \(h_*=t_*+O(t_*^2)=\sqrt{de}+O(e)\) for fixed \(a,d\); thus no positive step bound uniform in the smallest positive eigenvalue exists. Indeed taking \(e=o(h^2)\) as \(h\downarrow0\) yields strict negativity for all sufficiently small steps.

## Verification
The standalone `verify.py` reconstructs the precise method with the range projector, checks its eigenvalues and SVD truncations against the closed formulas for many deterministic parameter combinations, tests rank-one safety for random positive-semidefinite sources, checks embedded higher-rank witnesses, and checks the exact stable-drift example \(a=d=1\), \(e=1/10\), \(h=(\log3)/2\). For that example, \(s=1/3\), \(t=1\), and the retained negative eigenvalue is exactly \(-(\sqrt2-1)/3\), while the exact covariance is positive semidefinite. These computational tests do not replace the analytical proof.

## Relationship to prior work
Carrel and Vandereycken [1] introduce projected exponential Euler, tangent projection, and best-Frobenius-rank SVD truncation; their convergence analysis does not state a positive-semidefinite invariance theorem. The present result does not claim the method or truncation principle to be new. Kressner and collaborators [2] already show that another low-rank Lyapunov solution procedure can generate indefinite approximations and explain spectral positive-part repair; the general danger of indefiniteness and its remedy are not claimed as original here. Schmidt and collaborators [3] develop low-rank Kalman covariance filtering using square-root factors, a distinct construction that enforces positive-semidefinite covariance representation. The specific rank-one/rank-two dichotomy, exact damped-step boundary, and unrestricted-versus-PSD Frobenius cost ratio for [1, equation (31)] are the statements assessed here.

## Limitations
Only one step of the exact projected exponential Euler method with scalar dissipative drift and constant rank-one positive source is classified sharply. The dimension/rank dichotomy is universal within this flow family but does not imply all higher-rank initial states fail. Positivity can be regained by PSD-constrained truncation; that may change approximation costs and subsequent dynamics. The construction does not contradict norm-error or stiffness-robustness theorems in [1], and it does not establish long-time instability. At the exact threshold, an implementation's tie resolution matters. Independent publication-priority checking remains necessary; general indefinite low-rank Lyapunov phenomena are known [2].

## References
[1] B. Carrel and B. Vandereycken, *Projected exponential methods for stiff dynamical low-rank approximation problems*, arXiv:2312.00172 (first submitted 2023-11-30), especially equation (31), tangent projection and SVD truncation in Sections 2--3. https://arxiv.org/html/2312.00172v2

[2] D. Kressner and coauthors, *Compress-and-restart block Krylov subspace methods for Sylvester matrix equations*, Numerical Linear Algebra with Applications (2021), Section 2.3.1 on indefinite Lyapunov approximations and positive-semidefinite repair. https://doi.org/10.1002/nla.2339

[3] J. Schmidt, P. Hennig, J. Nick, and F. Tronarp, *The Rank-Reduced Kalman Filter: Approximate Dynamical-Low-Rank Filtering In High Dimensions*, arXiv:2306.07774 (2023), Sections 2--3. https://arxiv.org/abs/2306.07774

# Sharp trace-conditioned stability envelopes for orthogonal-subspace zeroth-order descent

## Finding
Consider unbiased zeroth-order descent from \(k\) Haar-orthogonal directions on a positive-definite quadratic in \(d\) variables. Its **exact mean-square stability limit** is the unique solution of a scalar equation involving the entire Hessian spectrum. Moreover, with dimension, subspace rank, smallest eigenvalue, largest eigenvalue, and Hessian trace prescribed, that critical step is strictly decreasing under spectral spreading: balanced interior eigenvalues uniquely give the **largest** admissible step, while endpoint-saturated interior eigenvalues give the **smallest**. Both bounds are attained by genuine quadratics; thus they are exact stability envelopes, not sufficient-only estimates.

More precisely, let \(d\ge2\), \(1\le k<d\), \(H=H^\mathsf T\succ0\), and order the eigenvalues \(0<\lambda_1\le\cdots\le\lambda_d=L\). Independently at each step choose a uniformly distributed rank-\(k\) orthogonal projector \(P_t\), and let
\[
S_t=\frac dkP_t,\qquad x_{t+1}=(I-\eta S_tH)x_t.
\]
Put
\[
a=\frac{d((k+1)d-2)}{k(d-1)(d+2)},\qquad
b=\frac{d(d-k)}{k(d-1)(d+2)}>0.
\]
For every deterministic \(x_0\ne0\), \(\mathbb E\|x_t\|_2^2\to0\) if and only if \(0<\eta<\eta_*(H)\), where \(\eta_*(H)\) is the unique root in \((0,2/(aL))\) of
\[
\boxed{\quad b\eta\sum_{i=1}^d\frac{\lambda_i}{2-a\eta\lambda_i}=1.\quad}
\]
At equality, the expected squared error fails to decay; above the root, it diverges from every nonzero deterministic starting vector. Furthermore, the standard isotropic-safe step \(2k/(dL)\) is strictly below \(\eta_*(H)\) for every *non-scalar* positive-definite \(H\); it equals the sharp threshold if and only if \(H=LI\). For \(k=d\), the method is ordinary gradient descent and the corresponding strict threshold is \(2/L\).

For the **sharp constrained envelope**, assume \(d\ge4\), \(0<\mu<L\), and fix the Hessian statistics \(\lambda_1=\mu\), \(\lambda_d=L\) and \(\sum_i\lambda_i=T\), with
\[
(d-1)\mu+L\le T\le\mu+(d-1)L.
\]
Write \(m=d-2\) and \(R=T-\mu-L\). Define the *balanced spectrum* \(\Lambda_{\rm bal}\) to contain \(\mu,L\), and \(m\) copies of \(R/m\). Define the *endpoint-saturated spectrum* \(\Lambda_{\rm sat}\) by writing
\[
\Delta=R-m\mu=q(L-\mu)+r,
\quad 0\le r<L-\mu,
\quad q=\left\lfloor\frac\Delta{L-\mu}\right\rfloor,
\]
with the convention that \(q=m,r=0\) is allowed. If \(q<m\), take \(q\) interior entries equal to \(L\), one entry equal to \(\mu+r\) when \(r>0\), and fill the remaining positions with \(\mu\); when \(r=0\), simply take \(q\) copies of \(L\) and \(m-q\) of \(\mu\). If \(q=m\), every interior entry is \(L\). Then all spectra satisfying the constraints obey the **attained, sharp** bounds
\[
\boxed{\quad\eta_*(\Lambda_{\rm sat})\le\eta_*(H)\le\eta_*(\Lambda_{\rm bal}).\quad}
\]
Equality on the right occurs only for the balanced interior multiset; equality on the left occurs only for the saturated interior multiset, up to permutation. At degenerate trace endpoints these multisets coincide. More generally \(\eta_*\) is strictly Schur-concave in the interior eigenvalues at fixed sum and fixed endpoints. In particular, top eigenvalue and trace alone do not fix the exact mean-square edge, even if the smallest eigenvalue is additionally known.

For \(d=4\), \(k=2\), \(\mu=1\), \(L=4\), \(T=10\), the two extremal spectra are \((1,1,4,4)\) and \((1,5/2,5/2,4)\). The saturated critical step is exactly \( (35-\sqrt{505})/40\approx0.3131948736438942\); the balanced critical step is the unique zero of \(500z^3-1280z^2+855z-162\) in \(0,9/20\), approximately \(0.3375977868030830\). Both exceed the general sufficient constant step \(2k/(dL)=1/4\), and the sharper interval distinguishes matrices with identical three elementary curvature statistics.

## Assumptions and scope
The iterates and calculations are in exact real arithmetic; the projectors are independent and Haar-uniform on the real Grassmannian. The true objective is \(f(x)=\tfrac12 x^\mathsf THx\), so a centered two-point directional difference satisfies, for every \(\delta>0\) and each unit direction \(u\),
\[
\frac{f(x+\delta u)-f(x-\delta u)}{2\delta}=u^\mathsf THx.
\]
Taking \(k\) orthonormal frame vectors and summing these directional differences with factor \(d/k\) gives exactly \(S_tHx_t\); there is no finite-difference bias on these quadratics. All spectral statements are invariant under orthogonal diagonalization. Stability means convergence of \(\mathbb E\|x_t\|_2^2\) to zero for **every** deterministic initial vector, and the theorem strengthens it to all nonzero starts simultaneously. The endpoint constraints fix actual extreme eigenvalues, not merely upper and lower bounds. The \(k=d\) limiting case has no strict spectral-spreading effect and is explicitly separate.

## Proof
**1. Exact Haar second moment.** Orthogonal invariance for a rank-\(k\) Haar projector \(P\) implies that on symmetric matrices \(X\) the linear map \(X\mapsto\mathbb E[PXP]\) has form \(cX+e\operatorname{tr}(X)I\). The projection of a fixed unit vector onto a uniformly random \(k\)-plane has squared length distributed as \(\mathrm{Beta}(k/2,(d-k)/2)\); hence
\[
\mathbb E P_{11}^2=\frac{k(k+2)}{d(d+2)},\qquad
\mathbb E P_{11}=\frac kd.
\]
Since \(P^2=P\), symmetry among offdiagonal entries gives
\[
\mathbb E P_{12}^2=\frac{k(d-k)}{d(d-1)(d+2)}.
\]
Evaluating \(X=e_1e_1^\mathsf T\) at entries \((1,1)\) and \((2,2)\), and rescaling by \(d^2/k^2\), proves for \(S=dP/k\)
\[
\boxed{\mathbb E[SXS]=aX+b\operatorname{tr}(X)I.}
\]
This identity also yields \(\mathbb ES=I\), \(a\ge1\), and \(a+db=d/k\). The beta moment and isotropic decomposition themselves are classical, and are used here as exact inputs.

**2. A closed positive second-moment recursion.** Work in an eigenbasis of \(H\), write \(y_i(t)=\mathbb E[x_i(t)^2]\), and take conditional expectations using the moment identity with \(X=Hxx^\mathsf TH\). This gives
\[
\begin{aligned}
y_i(t+1)&=(1-2\eta\lambda_i+a\eta^2\lambda_i^2)y_i(t)
+\eta^2b\sum_j\lambda_j^2y_j(t),\\
y(t+1)&=B_\eta y(t),\\
B_\eta&=\operatorname{diag}(1-2\eta\lambda_i+a\eta^2\lambda_i^2)
+\eta^2b\,\mathbf1(\lambda_1^2,\ldots,\lambda_d^2).
\end{aligned}
\]
Every entry of \(B_\eta\) is nonnegative: its diagonal summand equals \((1-\eta\lambda_i)^2+(a-1)\eta^2\lambda_i^2\ge0\). Since \(b>0\), \(B_\eta\) is strictly positive for every \(\eta>0\). Perron--Frobenius therefore implies that every nonzero nonnegative starting variance vector decays, remains nondecaying, or grows exactly according as \(\rho(B_\eta)\) is below, at, or above \(1\).

**3. Exact spectral threshold.** Write \(D_i=1-2\eta\lambda_i+a\eta^2\lambda_i^2\). When \(0<\eta<2/(aL)\), every \(D_i<1\). The determinant lemma (equivalently the positive rank-one resolvent formula) says
\[
\rho(B_\eta)<1\quad\Longleftrightarrow\quad
\eta^2b\sum_i\frac{\lambda_i^2}{1-D_i}<1.
\]
Indeed a positive rank-one perturbation of a nonnegative diagonal matrix with all entries strictly below \(1\) crosses Perron eigenvalue \(1\) precisely when its scalar secular quantity equals \(1\). Since \(1-D_i=\eta\lambda_i(2-a\eta\lambda_i)\), the scalar condition is
\[
F_H(\eta):=b\eta\sum_i\frac{\lambda_i}{2-a\eta\lambda_i}<1.
\]
The function is continuous and strictly increasing on \((0,2/(aL))\), begins at \(0\), and tends to \(+\infty\) at its right endpoint. Therefore it has exactly one root \(\eta_*(H)\). When \(\eta\ge2/(aL)\), the diagonal entry corresponding to \(L\) already has \(D_i\ge1\), and the strictly positive rank-one perturbation ensures \(\rho(B_\eta)>1\). At the unique root \(\rho=1\); the strictly positive left Perron vector proves nondecay for every nonzero variance initialization. For the standard bound \(\eta_0=2k/(dL)\), the column-sum identity \(a+db=d/k\) gives \(\mathbf1^\mathsf TB_{\eta_0}\le\mathbf1^\mathsf T\), with strict inequality in every column whose eigenvalue is smaller than \(L\). Since \(B_{\eta_0}\) is strictly positive, Perron--Frobenius makes its spectral radius strictly smaller than \(1\) when at least one such column exists, establishing \(\eta_*(H)>\eta_0\). For \(H=LI\), all column sums equal one and \(\eta_*=\eta_0\). For \(k=d\), \(b=0,a=1\) and the deterministic bound \(0<\eta<2/L\) follows directly.

**4. Sharp trace-constrained extremizers.** For fixed \(0<\eta<2/(aL)\), the summand
\[
\phi_\eta(s)=\frac{s}{2-a\eta s},\qquad
\phi_\eta''(s)=\frac{4a\eta}{(2-a\eta s)^3}>0
\]
is strictly convex on \([\mu,L]\). Fixing endpoints and trace leaves \(m=d-2\) interior numbers in \([\mu,L]\) with fixed sum \(R\). Jensen's inequality says their sum of \(\phi_\eta\) is minimized uniquely by equal entries \(R/m\). Conversely, successive transfers of mass from a smaller interior entry to a larger one (stopping at a bound) strictly increase the sum whenever entries are genuinely changed; iteration produces exactly the endpoint-saturated multiset, which therefore uniquely maximizes the sum. Equivalently, the endpoint-saturated vector majorizes every feasible interior vector, which majorizes the balanced vector. These comparisons hold at every \(\eta\) below the common pole \(2/(aL)\); the unique increasing root of \(F_H(\eta)=1\) is consequently largest for the balanced spectrum and smallest for the saturated spectrum. Strict convexity proves the stated equality characterization and strict Schur-concavity. The example follows by scalar root bisection with exact rational \(a=10/9,b=2/9\).

## Verification
A standalone standard-library Python checker accompanies the result. It checks the rational Haar moment coefficients, the rank-one secular transition against the Perron radius of the explicit positive variance matrix for randomized SPD spectra, isotropic sharpness, the fixed-trace rearrangement, and the four-dimensional numerical boundaries. It completed **2,171 tests** and reported `CHECK_OK`. The universal claims and all equality conditions follow from the preceding proofs, not these finite tests. Run `python check.py` from the extracted standalone package; no external libraries or datasets are required.

## Relationship to prior work
Song et al. (2026), *Zeroth-Order Optimization at the Edge of Stability*, analyze mean-square stability for Gaussian two-point directions and, in their Appendix B, discuss general fourth-moment operators, a uniform-spherical **single** direction, and averages of independent Gaussian directions. Their general covariance framework anticipates the importance of direction moments. It does not state the rank-\(k\) Haar-orthogonal secular equation or the fixed-trace, fixed-endpoint sharp spectral extremizers proved here.

Kozak et al. (2021), *Zeroth order optimization with orthogonal random directions*, formulate the same orthogonal-subspace iteration and give a general sufficient constant-step bound \(2k/(dL)\). That bound is attained for isotropic quadratics; it is not an exact anisotropic characterization and does not classify trace-constrained extremal spectra. Ghosh et al. (2026), *Gradient Descent with Stochastic Subspaces via Persistence of Memory*, develop broader subspace convergence estimates rather than this exact anisotropic mean-square edge. A published 2026 mathematical note, *Exact Haar moments remove sampling-dimension restrictions in sparse stochastic subspace descent*, already derives the corresponding classical Haar second moments for sparse-subspace descent, and its moment formula is expressly prior information, not claimed as a new lemma here. That note proves stationarity bounds and rank-one sharpness, not the exact all-mode secular threshold and spectral envelope.

The present mathematical contribution is therefore the sharp spectrum-level stability criterion and its nontrivial extremal consequences **for the rank-\(k\) orthogonal oracle**, not the oracle, elementary Haar moments, Perron--Frobenius, or convex majorization considered in isolation.

## Limitations
The theorem is exact only for fixed positive-definite quadratics, independent uniformly random real subspaces, symmetric two-point differences, and exact mean-square dynamics. A nonquadratic objective has finite-difference bias and changing Hessians; fixed finite \(\delta\) need not retain these thresholds. The conditioned envelope assumes prescribed \(\mu,L,T\) with positive \(\mu\) and compares the asymptotic expected squared norm, not almost-sure boundary behavior, worst single-iteration expansion, or finite-precision safety. The \(k=d\) case has no random spectral-spread dependence. The sharp scalar condition requires spectral information or bounds; it is not claimed as a practical spectrum-free step-size estimator. Historical equivalences in generalized random-projection, positive-map and numerical-linear-algebra literature cannot be ruled out definitively without further independent review.

## References
1. M. Song, L. Zhang, B. Li, N. He, M. Muehlebach, S. Oh, *Zeroth-Order Optimization at the Edge of Stability*, arXiv:2604.14669v1, 16 April 2026, Section 4 and Appendix B. https://arxiv.org/html/2604.14669v1
2. D. Kozak, C. Molinari, L. Rosasco, L. Tenorio, S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941, 2021, Section 3 and Theorem 3.1(iv). https://arxiv.org/abs/2107.03941
3. S. Ghosh, C. Z. Q. Ng, P.-L. Poirion, A. Takeda, *Gradient Descent with Stochastic Subspaces via Persistence of Memory*, arXiv:2609.18416v1, 16 September 2026, Sections 3 and C. https://arxiv.org/html/2609.18416v1
4. *Exact Haar moments remove sampling-dimension restrictions in sparse stochastic subspace descent*, public mathematical research record, 2026, `d9ecf263b248`. https://github.com/Resultary/2026/blob/main/2026/9/18/SCOPE-exact-haar-moments-sparse-ssd--d9ecf263b248/RESULT.md

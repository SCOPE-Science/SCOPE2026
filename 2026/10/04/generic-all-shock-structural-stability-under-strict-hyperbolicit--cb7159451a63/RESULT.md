# Generic all-shock structural stability under strict hyperbolicity alone
## Finding
Let \(U\subset\mathbb{R}^n\) be open and connected and let \(F\in C^2(U;\mathbb{R}^n)\) be strictly hyperbolic. Fix the wave pattern consisting of one strict Lax \(k\)-shock for each \(k=1,\ldots,n\), arranged in increasing speed order. For Lebesgue-almost every endpoint pair \((u_l,u_r)\in U^2\), every nondegenerate Rankine--Hugoniot chain with this all-shock pattern is structurally stable under sufficiently small perturbations of the endpoints and of \(F\) in the \(C^2\) topology. The perturbed chain has the same shock families, remains strictly Lax-admissible, and keeps the speed order.

Neither genuine nonlinearity nor the global regular-manifold hypothesis on the Rankine--Hugoniot map is required for this all-shock statement.

## Assumptions and scope
The system is
\[
u_t+F(u)_x=0,
\]
with \(F\in C^2(U;\mathbb{R}^n)\). Strict hyperbolicity means that the eigenvalues of \(DF(u)\) are real, simple, and ordered
\[
\lambda_1(u)<\cdots<\lambda_n(u)
\]
for every \(u\in U\).

An all-shock chain consists of states
\[
u^{(0)}=u_l,\ u^{(1)},\ldots,u^{(n-1)},\ u^{(n)}=u_r
\]
and speeds \(s_1<\cdots<s_n\), with \(u^{(k)}\neq u^{(k-1)}\), satisfying for each \(k\)
\[
F(u^{(k)})-F(u^{(k-1)})=s_k\bigl(u^{(k)}-u^{(k-1)}\bigr)
\]
and the strict Lax inequalities
\[
\lambda_{k-1}(u^{(k-1)})<s_k<\lambda_k(u^{(k-1)}),\qquad
\lambda_k(u^{(k)})<s_k<\lambda_{k+1}(u^{(k)}),
\]
with \(\lambda_0=-\infty\) and \(\lambda_{n+1}=+\infty\). The claim concerns only this classical all-shock pattern. It does not address rarefactions, contacts, composite waves, undercompressive shocks, or loss of strict hyperbolicity.

Structural stability is local: for a compact set \(K\Subset U\) containing the finitely many states, sufficiently small endpoint perturbations and sufficiently small \(C^2(K)\) perturbations of the flux admit a unique nearby all-shock chain with the same Lax inequalities and speed ordering.

## Proof
For fixed endpoints define the all-shock objective map \(\mathcal J\) by its \(k\)-th \(\mathbb{R}^n\)-valued block
\[
J_k=F(u^{(k)})-F(u^{(k-1)})-s_k\bigl(u^{(k)}-u^{(k-1)}\bigr),\qquad k=1,\ldots,n.
\]
The unknown vector is
\[
x=\bigl(u^{(1)},\ldots,u^{(n-1)},s_1,\ldots,s_n\bigr)\in\mathbb{R}^{n^2},
\]
and the endpoint parameter is \(p=(u_l,u_r)\in U^2\). A zero of \(\mathcal J\) is exactly a Rankine--Hugoniot chain.

Restrict the \((x,p)\)-domain to the open set on which all jumps are nondegenerate, all strict Lax inequalities hold, and \(s_1<\cdots<s_n\). This admissible locus is open because the ordered eigenvalues vary continuously under strict hyperbolicity.

At an admissible zero set
\[
A_k:=DF(u^{(k)})-s_kI,
\qquad
B_k:=-\bigl(DF(u^{(k-1)})-s_kI\bigr).
\]
The right-state Lax inequality places \(s_k\) strictly between consecutive eigenvalues of \(DF(u^{(k)})\), with the endpoint conventions above. Hence \(s_k\) is not an eigenvalue of \(DF(u^{(k)})\), so every \(A_k\) is invertible.

Now take the total derivative of \(\mathcal J\) with respect to the unknowns and endpoints. Select only the \(n^2\) columns belonging to
\[
u^{(1)},\ldots,u^{(n-1)},u_r.
\]
In block form this square submatrix is
\[
\begin{pmatrix}
A_1&0&\cdots&0\\
B_2&A_2&\ddots&\vdots\\
0&\ddots&\ddots&0\\
\vdots&&B_n&A_n
\end{pmatrix}.
\]
It is block lower triangular, and therefore its determinant is
\[
\prod_{k=1}^n\det A_k\neq0.
\]
Thus the full derivative \(D_{(x,p)}\mathcal J\) is surjective at every zero on the admissible locus. This argument uses neither genuine nonlinearity nor a regular-value hypothesis for non-admissible Hugoniot points.

The parameterized map is \(C^1\): with \(F\in C^2\), evaluations of \(F\) and \(DF\) are continuously differentiable in the finite-dimensional variables. The parametric transversality theorem therefore applies on the admissible open locus; its differentiability threshold is satisfied because the source and target dimensions of the restricted maps are both \(n^2\). Consequently, for Lebesgue-almost every \(p=(u_l,u_r)\), the map \(x\mapsto\mathcal J(x;p)\) is transverse to zero at every admissible zero. Since its derivative in \(x\) is square, transversality is equivalent to invertibility of \(D_x\mathcal J\).

Fix such an endpoint pair and an admissible zero. For flux perturbations, view \(\mathcal J\) as a map of \((x,u_l,u_r,F)\), with \(F\) in the Banach space \([C^2(K)]^n\). In the all-shock case this map is \(C^1\) without any rarefaction construction. Invertibility of \(D_x\mathcal J\) gives, by the Banach-space implicit function theorem, a unique nearby zero depending \(C^1\)-smoothly on the endpoints and flux. Strict hyperbolicity persists under sufficiently small \(C^2(K)\) perturbations because the eigenvalue gaps have a positive minimum on \(K\), and the strict Lax inequalities, nondegeneracy, containment in \(K\), and speed ordering are open conditions. Hence the nearby zero is the required structurally stable all-shock Riemann solution.

## Verification
The critical rank step can be checked directly from the displayed Jacobian. No numerical experiment or finite enumeration is used. The only global measure-theoretic input is parametric transversality applied after restricting to the open admissible locus. The proof does not assert existence of an all-shock solution for a given endpoint pair; it says that whenever such a solution exists for a generic pair, it is structurally stable.

The source paper explicitly records two ingredients used here: strict Lax admissibility makes the shock state blocks \(DF(u^{(k)})-s_kI\) invertible, and genuine nonlinearity is used only for rarefaction objects. Its genericity proof nevertheless invokes the global regular-manifold hypothesis because it proves transversality at every nondegenerate zero, including non-admissible zeros. Restricting the parametric-transversality argument to the physically admissible all-shock locus is the step that removes that global hypothesis.

## Relationship to prior work
Tan and Bertozzi prove generic structural stability for arbitrary mixtures of Lax shocks and rarefactions in general \(n\times n\) systems, but their theorem assumes strict hyperbolicity, genuine nonlinearity, and a global regular-manifold hypothesis for the Rankine--Hugoniot map. Their Section 3.4 notes that Lax admissibility makes the shock blocks invertible, and their conclusion states that genuine nonlinearity is used only for rarefaction objects. The present statement narrows the wave pattern to all shocks and, in exchange, removes both of those additional standing assumptions.

Schecter, Marchesin, and Plohr study structural stability under perturbations of initial data and flux for systems of two conservation laws, with a viscous-profile framework and maximal-rank conditions. That work does not give the present arbitrary-dimensional generic endpoint theorem.

Kong proves global structure stability for Lax Riemann solutions containing shocks and contact discontinuities in general \(n\times n\) quasilinear systems under generalized-Riemann initial-data perturbations of a fixed system. The available abstract does not state robustness under perturbations of the flux function and does not give an almost-every-endpoint transversality theorem. Thus it does not imply the present claim.

The earlier \(2\times2\) generic theorem of Tan and Bertozzi also assumes genuine nonlinearity and the regular-manifold condition, so it does not cover this assumption-reduced result.

## Limitations
The result is conditional on existence of a nondegenerate, strict, speed-ordered all-shock Lax chain. It gives local structural persistence, not global uniqueness among all wave patterns. It does not cover rarefaction-containing solutions, contacts, composite waves, undercompressive shocks, or characteristic degeneracy. The older Kong paper was not available as lawful full text during the comparison, so a residual originality risk remains that details beyond its abstract contain a closer flux-perturbation statement than the abstract indicates.

## References
1. H. K. Tan and A. L. Bertozzi, “Generic Structural Stability for Riemann Solutions to \(n\times n\) Systems of Hyperbolic Conservation Laws,” arXiv:2609.28714v1, 2026.
2. H. K. Tan and A. L. Bertozzi, “Generic Structural Stability for Riemann Solutions to \(2\times2\) Systems of Hyperbolic Conservation Laws,” SIAM Journal on Mathematical Analysis 58 (2026), 888–925, DOI 10.1137/25M1733586.
3. S. Schecter, D. Marchesin, and B. J. Plohr, “Structurally Stable Riemann Solutions,” Journal of Differential Equations 126 (1996), 303–354.
4. D.-X. Kong, “Global structure stability of Riemann solutions of quasilinear hyperbolic systems of conservation laws: Shocks and contact discontinuities,” Journal of Differential Equations 188 (2003), 242–271, DOI 10.1016/S0022-0396(02)00068-2.

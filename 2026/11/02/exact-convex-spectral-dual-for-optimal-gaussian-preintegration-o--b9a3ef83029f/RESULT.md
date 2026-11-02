# Exact convex-spectral dual for optimal Gaussian preintegration of affine quadratics

## Finding
Let \(X\sim N(0,I_d)\), with \(d\ge1\), let \(A\in\mathbb R^{d\times d}\) be symmetric and \(b\in\mathbb R^d\), and put \(f(X)=\tfrac12 X^\top AX+b^\top X\). For a unit vector \(v\), preintegrate exactly in its Gaussian direction: \(G_v=\mathbb E[f(X)\mid (I-vv^\top)X]\). Its variance reduction is
\[
R(v):=\operatorname{Var}(f(X))-\operatorname{Var}(G_v)
=v^\top Bv-\tfrac12(v^\top Av)^2,\qquad B=A^2+bb^\top.
\]
Define the *one-dimensional convex spectral dual* by
\[
\Phi(t)=\tfrac12t^2+\lambda_{\max}(B-tA),\qquad t\in\mathbb R.
\]
Then, for **every** such \(A,b,d\),
\[
\boxed{\quad \max_{\|v\|=1}R(v)=\min_{t\in\mathbb R}\Phi(t).\quad}
\]
The minimizing scalar \(t_*\) is unique, belongs to \([\lambda_{\min}(A),\lambda_{\max}(A)]\), and completely determines every optimal preintegration direction. Write \(E_*\) for the top eigenspace of \(B-t_*A\). A unit vector \(v\) is globally optimal **if and only if**
\[
v\in E_*\quad\text{and}\quad v^\top Av=t_*.
\]
Such vectors always exist, including when the top eigenvalue is multiple. Every unit trial vector has the exact nonnegative optimality gap
\[
\boxed{\quad R_*-R(v)=
\bigl[\lambda_{\max}(B-t_*A)-v^\top(B-t_*A)v\bigr]
+\tfrac12\bigl(v^\top Av-t_*\bigr)^2.\quad}
\]
In particular, a computed spectral upper bound for the first bracket and a Rayleigh mismatch bound give a rigorous optimality certificate.

A sharp homogeneous specialization is especially simple. If \(b=0\), and the extreme eigenvalues \(a=\lambda_{\min}(A)\), \(c=\lambda_{\max}(A)\) have opposite signs \(a<0<c\), then
\[
\boxed{\quad R_*=\tfrac12(a^2+c^2),\qquad
\min_{\|v\|=1}\operatorname{Var}(G_v)
=\tfrac12\bigl(\operatorname{tr}A^2-a^2-c^2\bigr).\quad}
\]
All optimal directions have components only in the \(a\)- and \(c\)-eigenspaces, with total squared component norms respectively \(-a/(c-a)\) and \(c/(c-a)\). This includes repeated extreme eigenvalues. In contrast, when \(A\) is positive or negative semidefinite, the maximal reduction equals \(\tfrac12\max(a^2,c^2)\), attained by a maximal-absolute-eigenvalue eigenvector (or by any vector in its possibly repeated eigenspace).

An illustrative exact counterpoint to the leading active-subspace eigenvector is \(A=\operatorname{diag}(-3,0,2)\), \(b=0\). The optimal direction \(v=(\sqrt{3/5},0,\sqrt{2/5})^\top\) makes \(G_v\) constant and gives **zero remaining variance**, whereas preintegrating the dominant \(A^2\)-eigenvector leaves variance \(2\). Both directions use the same single exact preintegration.

## Assumptions and scope
All matrices and vectors are real, \(A\) is symmetric but is not required to be positive definite or invertible, \(d\) is an arbitrary positive integer, and \(X\) has independent standard-normal components. The unit direction \(v\) is chosen deterministically before sampling. The conditional expectation is exact; only the postconditioning integration variance is optimized. Eigenvalues are counted with multiplicities; \(\lambda_{\max}\) is the largest algebraic eigenvalue. The homogeneous closed form explicitly separates the indefinite case \(a<0<c\) from the semidefinite cases. No claim is made for arbitrary nonquadratic integrands, non-Gaussian inputs, or multi-direction preintegration.

## Proof
**1. Conditional-variance identity.** Let \(P=I-vv^\top\), \(Y=PX\), and \(Z=v^\top X\). The variables \(Y\) and \(Z\sim N(0,1)\) are independent. Direct substitution yields
\[
f(Y+Zv)=\tfrac12Y^\top AY+b^\top Y+
Z(v^\top AY+v^\top b)+\tfrac12Z^2v^\top Av.
\]
The conditional expectation is \(G_v=\tfrac12Y^\top AY+b^\top Y+\tfrac12v^\top Av\). Since \(\operatorname{Var}(Z)=1\), \(\operatorname{Var}(Z^2)=2\), and \(\operatorname{Cov}(Z,Z^2)=0\), the law of total variance gives
\[
\operatorname{Var}(f)-\operatorname{Var}(G_v)
=\mathbb E(v^\top AY+v^\top b)^2+\tfrac12(v^\top Av)^2.
\]
Because \(\mathbb E[YY^\top]=P\), this equals \(v^\top A^2v-(v^\top Av)^2+(v^\top b)^2+\tfrac12(v^\top Av)^2=R(v)\). Independently, \(\operatorname{Var}(f)=\tfrac12\operatorname{tr}A^2+\|b\|^2\) and \(\operatorname{Var}(G_v)=\tfrac12\|PAP\|_F^2+\|Pb\|^2\).

**2. Global upper bound.** For each unit \(v\) and each real \(t\), completing the square gives the identity
\[
R(v)=v^\top(B-tA)v+\tfrac12t^2-\tfrac12(v^\top Av-t)^2
\le\tfrac12t^2+\lambda_{\max}(B-tA)=\Phi(t).
\]
Thus \(R_*\le\inf_t\Phi(t)\). The largest eigenvalue of an affine symmetric pencil is convex in \(t\). Consequently \(\Phi\) is one-strongly convex, is coercive, and has exactly one minimizing scalar \(t_*\).

**3. No duality gap, including repeated eigenvalues.** Let \(E_*\) be the maximal eigenspace of \(B-t_*A\). The one-sided directional derivative formula for a maximal eigenvalue (which also follows directly from its Rayleigh maximum representation) gives
\[
\partial\lambda_{\max}(B-tA)\big|_{t=t_*}
=[-\lambda_{\max}(A|_{E_*}),-\lambda_{\min}(A|_{E_*})].
\]
The optimality condition \(0\in\partial\Phi(t_*)\) therefore says that \(t_*\) lies between the smallest and largest Rayleigh quotients of \(A\) on \(E_*\). If \(E_*\) has dimension one, the unique quotient already equals \(t_*\). Otherwise continuously mixing unit eigenvectors of the compression of \(A\) onto \(E_*\) realizes every quotient in that interval, so a unit \(v_*\in E_*\) satisfies \(v_*^\top Av_*=t_*\). It attains equality in both inequalities in Step 2, proving strong duality, global attainment, and \(t_*\in[\lambda_{\min}(A),\lambda_{\max}(A)]\). Reversing the equality conditions proves the characterization of **all** maximizers.

**4. Exact gap and stability.** Subtract the Step 2 identity from \(R_*=\Phi(t_*)\) to obtain the displayed two-term deficit. Both terms are nonnegative. If the leading eigenspace \(E_*\) is separated from its orthogonal complement by a positive spectral gap \(\gamma\), the first term is at least \(\gamma\|(I-\Pi_{E_*})v\|^2\). This gives an explicit angular and Rayleigh-quotient stability certificate with no general-position assumption.

**5. Homogeneous extreme-eigenvalue classification.** For \(b=0\), expand any unit direction in an orthonormal eigenbasis of \(A\); let the weights \(p_i\ge0\) sum to one, let the corresponding eigenvalues be \(\lambda_i\in[a,c]\), and let \(m=\sum_i p_i\lambda_i\). The elementary spectral inequality \((\lambda_i-a)(c-\lambda_i)\ge0\) gives
\[
\sum_i p_i\lambda_i^2\le(a+c)m-ac.
\]
If \(a<0<c\), then \(a+c\in[a,c]\), so
\[
2R(v)\le a^2+c^2-(m-a-c)^2\le a^2+c^2.
\]
Equality requires \(p_i=0\) for every strict interior eigenvalue and \(m=a+c\); solving the two mass equations gives weights \(-a/(c-a)\) and \(c/(c-a)\), both strictly positive. More precisely, for every unit \(v\),
\[
2(R_*-R(v))=(m-a-c)^2+2\sum_i p_i(\lambda_i-a)(c-\lambda_i).
\]
When \(a\ge0\) or \(c\le0\), the same upper bound is maximized over \(m\in[a,c]\) at the endpoint with larger absolute value, giving \(R_*=(1/2)\max(a^2,c^2)\). Equality requires concentration in the corresponding extreme eigenspace; the zero matrix is the trivial all-directions case.

**6. Zero-variance example.** For \(A=\operatorname{diag}(-3,0,2)\), the optimal variance is \(\tfrac12(9+4-9-4)=0\). The stated \(v\) has \(PAP=0\), hence \(G_v\) is constant. A dominant active-subspace eigenvector is the first coordinate vector; then \(PAP=\operatorname{diag}(0,0,2)\) and \(\operatorname{Var}(G_v)=\tfrac12(2^2)=2\). These are exact finite-dimensional equalities.

## Verification
A standalone deterministic verifier (`verify.py`) accompanies this result, with dependencies listed in `requirements.txt`. It tests exact rational deficit identities across arbitrary diagonal spectra, dense symmetric matrices against competing directions, global scalar convex-dual minimization and eigenvector reconstruction with nonzero affine terms, and the exact zero-variance example. Numerical checks supplement, but do not replace, Steps 1–6. Run `python verify.py` in an environment with the listed dependencies.

## Relationship to prior work
Liu and Owen's *Pre-integration via Active Subspaces* (arXiv:2202.02682; *SIAM Journal on Numerical Analysis* 61 (2023), 495–514) develops Gaussian-direction preintegration and relates the active-subspace top eigenvector to a total-Sobol-index objective. Its Section 4 and Proposition 4.2 supply the affine-quadratic reduction criterion used here; **that identity is acknowledged prior work, not a novel contribution**. The new contribution is the universally exact global optimization of that criterion by a one-dimensional strongly convex eigenvalue problem, complete treatment of multiple leading eigenvalues, nonnegative global certificates, and the sharp indefinite-spectrum closed form. Liu's *Conditional Quasi-Monte Carlo with Constrained Active Subspaces* (arXiv:2212.13232) treats feasible direction selection under tractability constraints rather than this exact unconstrained quadratic maximization. Classical variational eigenvalue and convex-subgradient arguments provide the proof tools but are not themselves new.

## Limitations
This is a mathematical specialization for a Gaussian affine-quadratic family with exact conditional integration. It does not imply the same optimality for nonlinear payoffs, noisy conditional integrals, arbitrary transformed distributions, or every practical randomized quasi-Monte Carlo criterion. Optimizing variance alone need not optimize higher-order regularity. The spectral dual is a one-dimensional convex optimization problem rather than an elementary closed form for arbitrary nonzero \(b\); repeated leading eigenvalues require constructing a vector in their top eigenspace with the prescribed Rayleigh quotient. The result has not undergone independent scientific audit. Related general results on hidden convexity and joint numerical ranges may yield alternative formulations; exhaustive priority across those literatures is not certified.

## References
1. S. Liu and A. B. Owen, *Pre-integration via Active Subspaces*, arXiv:2202.02682 (first publicly posted 2022-02-06); *SIAM Journal on Numerical Analysis* 61 (2023), 495–514. https://arxiv.org/abs/2202.02682 ; https://doi.org/10.1137/22M1479129.
2. S. Liu, *Conditional Quasi-Monte Carlo with Constrained Active Subspaces*, arXiv:2212.13232 (first publicly posted 2022-12-26). https://arxiv.org/abs/2212.13232.
3. C.-K. Li and Y.-T. Poon, *Convexity of the Joint Numerical Range*, *SIAM Journal on Matrix Analysis and Applications*, https://doi.org/10.1137/S0895479898343516. Cited as background for spectral convexity, not as evidence of a new theorem.

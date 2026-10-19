# A sharp perfect-conditioning sign alias in Ritz-polynomial inverse-square-root preconditioning

## Finding

A degree-one polynomial interpolating the positive inverse square root at two spectral nodes can make a symmetric positive-definite matrix **exactly identity-preconditioned** while producing the wrong principal inverse-square-root action. The phenomenon admits a complete three-point spectral classification and a sharp transition when the interpolation nodes are obtained from a full-support two-step Lanczos pilot.

For distinct \(0<u<v\), let
\[
\alpha=u^2,\quad \beta=v^2,\quad \gamma=(u+v)^2,
\qquad q(z)=\frac{u^2+uv+v^2-z}{uv(u+v)}.
\]
Then \(q\) interpolates \(z^{-1/2}\) at \(\alpha,\beta\), but
\[
q(\gamma)=-\gamma^{-1/2},\qquad
zq(z)^2-1=\frac{(z-\alpha)(z-\beta)(z-\gamma)}{\alpha\beta\gamma}.
\]
Consequently, for \(A=\operatorname{diag}(\alpha,\beta,\gamma)\), the preconditioned matrix \(B=Aq(A)^2\) is exactly \(I_3\), yet one left-preconditioned Arnoldi step returns \(q(A)b\), not the principal action \(A^{-1/2}b\). Its relative error attains \(2\), at \(b=e_3\), despite a zero preconditioned Krylov residual.

**Rigidity and sharp dimensionless frontier.** If a real affine \(q\) interpolates \(z^{-1/2}\) at two distinct SPD eigenvalues \(\alpha<\beta\), a third distinct positive eigenvalue \(\gamma\) produces \(Aq(A)^2=I\) if and only if \(\gamma=(\sqrt\alpha+\sqrt\beta)^2\). Thus the sign-alias family has \(\kappa_2(A)>4\), and every value strictly above \(4\) occurs. Within this interpolation-anchored, exactly identity-preconditioned class, dimension three and the strict conditioning threshold \(4\) are sharp. No claim of such a frontier is made for arbitrary polynomials or approximate preconditioning.

**Full-support Ritz pilot.** Set \(A=\operatorname{diag}(1,4,9)\) and use two exact Lanczos steps with pilot \(g_t=(1,1,\sqrt t)^{\mathsf T}\), \(t>0\). Let \(q_t\) be the affine interpolant to \(z^{-1/2}\) at its two positive Ritz values. There is an explicit unique transition
\[
t_c=\frac{180\sqrt{582}-3537}{26117}=0.0308397484187822\ldots
\]
such that \(q_t(9)<0\) exactly when \(0<t<t_c\), with \(q_{t_c}(9)=0\) and \(q_t(9)>0\) for \(t>t_c\). For every \(0<t<t_c\), a one-step left-preconditioned Arnoldi evaluation with \(b=e_3\) returns exactly \(-e_3/3\) instead of \(+e_3/3\). Nevertheless \(B_t=Aq_t(A)^2\) obeys
\[
\kappa_2(B_t)=1+\frac{4000}{27}t+O(t^2)\quad(t\downarrow0).
\]
Thus even a pilot that samples every eigendirection can yield an arbitrarily well-conditioned preconditioned operator and a **200% relative error**. At the precise sign-repair threshold \(t_c\), the preconditioner becomes singular.

## Assumptions and scope

All calculations use exact real arithmetic. The matrices are symmetric positive definite; \(q\) is the real degree-one Lagrange interpolant to the positive branch \(z^{-1/2}\) at two distinct positive nodes. In the full-support construction, the polynomial is formed using a separate, explicitly specified two-step Lanczos pilot; applying the polynomial to a different right-hand side is permitted. The left method forms \(c=q(A)b\), constructs a Krylov basis for \(B=Aq(A)^2\), and evaluates the principal inverse square root of the small projected matrix. A nonzero component of \(c\) is required for initialization. The assertion at \(t=t_c\) concerns polynomial singularity, not a defined Arnoldi output for \(b=e_3\).

## Proof

**1. Spectral identity and rigidity.** The unique line through \((u^2,1/u)\) and \((v^2,1/v)\) is the displayed \(q\). Direct substitution gives its three values \(1/u,1/v,-1/(u+v)\). The polynomial \(zq(z)^2-1\) has degree three, leading coefficient \(1/[u^2v^2(u+v)^2]\), and precisely the three displayed roots. This proves the factored identity. Conversely, once the two positive interpolation anchors are prescribed, the two corresponding eigenvalues of \(Aq(A)^2\) equal \(1\); if this SPD preconditioned matrix has condition number one, it must equal \(I\). Every additional eigenvalue must therefore be a root of the cubic, and the only possible distinct third eigenvalue is \((u+v)^2\). The original condition number is \(((u+v)/u)^2>4\), and choosing \(u=1\), \(v=\sqrt K-1>1\) realizes each \(K>4\).

**2. Principal-branch error.** Because \(B=I\), every nonzero preconditioned Krylov space is one-dimensional, with projected matrix \([1]\); the left Arnoldi formula gives \(q(A)b\) exactly in one step. In an eigenbasis,
\[
q(A)=\operatorname{diag}(1/u,1/v,-1/(u+v)),\quad
A^{-1/2}=\operatorname{diag}(1/u,1/v,1/(u+v)).
\]
Their difference is \(-2e_3e_3^{\mathsf T}/(u+v)\). Hence the relative error is
\[
\frac{2|b_3|/(u+v)}{\sqrt{|b_1|^2/u^2+|b_2|^2/v^2+|b_3|^2/(u+v)^2}},
\]
whose sharp maximum over nonzero \(b\) is \(2\). Both the preconditioned residual and the projected function error vanish: the error lies in selecting the spectral sign branch rather than approximating the action of \(B^{-1/2}\).

**3. Exact two-step Ritz nodes.** For \(A=\operatorname{diag}(1,4,9)\), \(g_t=(1,1,\sqrt t)^{\mathsf T}\), let \(M_j=1+4^j+t9^j\) for \(0\le j\le3\). The characteristic polynomial of the two-node Lanczos compression is \(z^2-s_1(t)z+s_0(t)\), with
\[
\Delta=M_0M_2-M_1^2=9+89t,\quad
s_1=\frac{M_0M_3-M_1M_2}{\Delta}=\frac{45+965t}{9+89t},\quad
s_0=\frac{M_1M_3-M_2^2}{\Delta}=\frac{36+1476t}{9+89t}.
\]
These identities follow by imposing weighted orthogonality of the monic quadratic to \(1\) and \(z\), so they describe the actual two-step Lanczos nodes, not guessed eigenvalue samples. The two Ritz nodes are positive and distinct for every \(t>0\). Writing them \(\theta_1<\theta_2\), the interpolation formula gives
\[
q_t(z)=\frac{s_1(t)+\sqrt{s_0(t)}-z}{\sqrt{s_0(t)}(\sqrt{\theta_1}+\sqrt{\theta_2})}.
\]
Thus \(q_t(9)<0\) exactly when \(9-s_1(t)>\sqrt{s_0(t)}\). The left-hand side decreases strictly from \(4\), whereas \(\sqrt{s_0(t)}\) increases strictly from \(2\). Squaring at their unique crossing yields
\[
(9-s_1)^2-s_0=-\frac{4(26117t^2+7074t-243)}{(9+89t)^2},
\]
whose unique positive crossing is the stated \(t_c\); there is no extraneous squared root since \(9-s_1(t_c)>0\). At the crossing, \(q_t(9)=0\) and \(B_t\) is singular. For smaller positive \(t\), \(q_t(1),q_t(4)>0\), \(q_t(9)<0\), and \(B_t\) is positive definite.

**4. Exact one-step error and near-isometry.** With \(b=e_3\), \(c=q_t(9)e_3\) and \(Be_3=9q_t(9)^2e_3\). The one-dimensional Arnoldi compression is \([9q_t(9)^2]\), and the formula therefore returns \(\operatorname{sign}(q_t(9))e_3/3\) with an exact zero Krylov residual. This proves the two branches. As \(t\downarrow0\), the Ritz nodes tend to \(1,4\), hence \(B_t\to I_3\). Differentiating the two moment ratios and the interpolating polynomial shows that the three preconditioned eigenvalue derivatives at \(t=0\), in the order \(1,4,9\), are \(-400/27\), \(400/27\), and \(-400/3\). The second is the largest and the third the smallest, so their quotient gives the displayed sharp condition-number expansion.

## Verification

The accompanying `verify.py` uses symbolic factorization and rational identities to check the three-root formula, Lanczos moment coefficients, transition polynomial, and first derivatives. Independent dense two-step Lanczos calculations numerically evaluate the full-support pilots and replay the one-step preconditioned extraction. It reports `VERIFICATION_OK` with 169 checks. Run with Python 3 and the packages declared in `requirements.txt`. The proof, not the finite test grid, establishes the universal assertions and the unique transition.

## Relationship to prior work

Frommer, Ramirez-Hidalgo, Schweitzer and Tsolakis (2024) introduce polynomial inverse-square-root Krylov preconditioning, allow Ritz-based polynomial construction, and explicitly warn that a polynomial with an incorrect branch may produce an inverse square root other than the principal one. Their branch warning and the underlying Arnoldi algorithm are prior results, not contributions claimed here. The additional statements proved above are the exact three-point identity and its converse, the sharp threshold \(\kappa_2(A)>4\) within that identity-preconditioned class, and the full-support Lanczos pilot's explicit branch-transition law and near-identity asymptotic. Higham's treatment of matrix functions provides the broader principal-root and matrix-sign background.

## Limitations

This is an exact-arithmetic obstruction for a deliberately underresolved **two-node** Ritz interpolant and the corresponding SPD three-mode family. It does not say that a polynomial approximating the positive inverse square root uniformly on the *entire* spectrum has this defect: a strong uniform error/positivity guarantee rules it out. It does not establish a generic failure rate under random pilots, or a bound for arbitrary degrees or nonnormal matrices. The branch error can be detected by inspecting the sign of \(q\) on the spectrum; an eigenvalue-only condition number of \(Aq(A)^2\) cannot detect it. No independent mathematical audit has been performed.

## References

1. A. Frommer, G. Ramirez-Hidalgo, M. Schweitzer, and M. Tsolakis, *Polynomial Preconditioning for the Action of the Matrix Square Root and Inverse Square Root*, arXiv:2401.06684v1, first public 2024-01-12, especially Sections 3, 5, and 6. https://arxiv.org/html/2401.06684v1
2. N. J. Higham, *Functions of Matrices: Theory and Computation*, SIAM, 2008, especially Chapters 1 and 6. https://doi.org/10.1137/1.9780898717778

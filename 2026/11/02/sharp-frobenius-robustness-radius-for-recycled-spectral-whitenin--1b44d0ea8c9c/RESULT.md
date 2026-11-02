# Sharp Frobenius robustness radius for recycled spectral whitening

## Finding
Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, \(n\ge2\), with increasing eigenvalues \(0<\lambda_1\le\lambda_2\le\cdots\le\lambda_n\). Fix \(K>1\). Set \(U=\sqrt{\lambda_1}A^{-1/2}\), the exact full spectral-whitening preconditioner scaled to the smallest eigenvalue. For \(t\ge0\) and a real symmetric perturbation \(E\) with \(\|E\|_F\le1\), define
\[
B(t,E)=\lambda_1^{-1}U(A+tE)U=I+tA^{-1/2}EA^{-1/2}.
\]
Then the largest perturbation radius for which **every** such \(E\) yields a positive-definite \(B(t,E)\) satisfying \(\kappa_2(B(t,E))\le K\) is exactly
\[
\boxed{t_*(A,K)=\frac{K-1}{\sqrt{K^2/\lambda_1^2+1/\lambda_2^2}}.}
\]
All perturbations are safe for \(0\le t\le t_*\), including the endpoint. At the endpoint a commuting, rank-two perturbation with Frobenius norm one attains condition number exactly \(K\). For **every** \(t>t_*\), some admissible perturbation produces a positive-definite \(B(t,E)\) with condition number strictly greater than \(K\) (and, at sufficiently large radii, positive definiteness itself can fail). The result holds without a simple-eigenvalue hypothesis.

## Assumptions and scope
The norm \(\|E\|_F\) is the Frobenius norm of the perturbation to the **unpreconditioned** matrix. The spectral condition number \(\kappa_2\) means the ratio of largest to smallest eigenvalue of a symmetric positive-definite matrix, not the condition number of an eigendecomposition. The preconditioner is fixed from the reference \(A\), reused for each \(A+tE\), and uses exact real symmetric functional calculus. We allow \(\lambda_1=\lambda_2\), with any orthonormal pair in the corresponding eigenspace. There are no assertions about an approximate, rank-limited or adaptively updated preconditioner, finite-precision arithmetic, or convergence rates for particular right-hand sides.

## Proof
Put \(H=A^{-1}\), with decreasing eigenvalues \(h_1=1/\lambda_1\ge h_2=1/\lambda_2\ge\cdots>0\). Since \(\|E\|_2\le\|E\|_F\le1\), Weyl's inequality gives \(A+tE\succ0\) whenever \(t<\lambda_1\). Observe that \(t_*<\lambda_1\), because \(K-1<K\) and \(\sqrt{K^2h_1^2+h_2^2}>Kh_1\).

For every positive-definite symmetric \(B\), the inequality \(\kappa_2(B)\le K\) is equivalent to
\[
v^{\mathsf T}Bv-Ku^{\mathsf T}Bu\le0
\quad\text{for all orthonormal }u,v\in\mathbb R^n.
\]
Indeed the inequality follows from the minimum and maximum eigenvalues, and the reverse implication follows by choosing orthogonal extreme eigenvectors (or any orthonormal pair when all eigenvalues coincide). With \(B=B(t,E)\), its left side is
\[
1-K+t\left\langle E,H^{1/2}(vv^{\mathsf T}-Kuu^{\mathsf T})H^{1/2}\right\rangle_F.
\]
By Frobenius duality, the exact maximum over all symmetric \(\|E\|_F\le1\) is
\[
1-K+t\,\|H^{1/2}(vv^{\mathsf T}-Kuu^{\mathsf T})H^{1/2}\|_F.
\]
Write \(a=u^{\mathsf T}Hu\), \(d=v^{\mathsf T}Hv\), \(b=u^{\mathsf T}Hv\). Expanding the squared norm gives
\[
F(u,v)^2=K^2a^2+d^2-2Kb^2.
\]
Let \(\eta_1\ge\eta_2>0\) be the two eigenvalues of the compression of \(H\) to the plane spanned by \(u,v\), and let \(x\in[0,1]\) be the squared cosine of the angle between \(u\) and a top eigenvector of that compression. Writing \(\Delta=\eta_1-\eta_2\), we have
\[
a=\eta_2+\Delta x,\qquad d=\eta_1-\Delta x,\qquad b^2=\Delta^2x(1-x).
\]
Thus \(F^2\) is a convex quadratic in \(x\), with coefficient \((K+1)^2\Delta^2\ge0\). It is maximized at an endpoint. The larger endpoint value is \(K^2\eta_1^2+\eta_2^2\), since \(K>1\) and \(\eta_1\ge\eta_2\). By the min-max principle for two-dimensional compressions, \(\eta_1\le h_1\) and \(\eta_2\le h_2\). Therefore
\[
\max_{u\perp v,\ \|u\|=\|v\|=1}F(u,v)
=\sqrt{K^2h_1^2+h_2^2}=:L.
\]
Equality holds when \(u=w_1\) and \(v=w_2\) are orthonormal eigenvectors for \(h_1,h_2\). The exact worst difference over all perturbations and orthonormal pairs is consequently \(1-K+tL\). Hence for \(0\le t\le(K-1)/L\), it is nonpositive; together with positivity this proves uniform \(\kappa_2\le K\).

To prove attainment, choose such \(w_1,w_2\) and set
\[
E_*=-\frac{Kh_1}{L}w_1w_1^{\mathsf T}+\frac{h_2}{L}w_2w_2^{\mathsf T}.
\]
This perturbation is symmetric, commutes with \(A\), has rank two and satisfies \(\|E_*\|_F^2=(K^2h_1^2+h_2^2)/L^2=1\). At \(t=t_*\), the eigenvalues in these directions are \(\mu_-=1-t_*Kh_1^2/L\) and \(\mu_+=1+t_*h_2^2/L\), with all other eigenvalues equal to one. Since \(0<\mu_-<1<\mu_+\) and
\[
\mu_+-K\mu_- = 1-K+t_*L=0,
\]
we have \(\kappa_2(B(t_*,E_*))=K\). If \(t>t_*\), choose \(t_0\) strictly between \(t_*\) and \(\min\{t,\lambda_1\}\), sufficiently close to \(t_*\) that \(B(t_0,E_*)\succ0\). Its condition number exceeds \(K\) by the same strict eigenvalue inequality. With \(E=(t_0/t)E_*\), the perturbation remains Frobenius-admissible and \(B(t,E)=B(t_0,E_*)\), proving failure of uniform conditioning at **every** larger radius. At \(t\ge\lambda_1\), the admissible perturbation \(E=-(\lambda_1/t)w_1w_1^{\mathsf T}\) also makes \(B(t,E)\) singular. This completes the proof.

## Verification
Run `python check_whitening.py` with Python 3 and NumPy. The supplied self-contained script checks the exact two-dimensional rational example, constructs the attaining perturbation for seeded random orthogonally rotated SPD matrices in dimensions two through eight, includes repeated smallest eigenvalues, tests random symmetric perturbations on the critical boundary, and finds violations just beyond it. On the recorded run, all **8,472 checks passed**. The infinite-dimensional-family theorem is established by the preceding proof, not by the finite numerical checks.

For example, when \(A=\operatorname{diag}(1,2)\) and \(K=2\), the exact radius is \(t_*=2/\sqrt{17}\). An extremizing \(E_*\) is \(\operatorname{diag}(-4/\sqrt{17},1/\sqrt{17})\), for which the two eigenvalues of \(B(t_*,E_*)\) are \(9/17\) and \(18/17\). The older crude spectral-norm estimate would certify only \(t\le1/3\), strictly smaller than \(2/\sqrt{17}\).

## Relationship to prior work
Diouane, Gürol, Mouhtal and Orban study reuse of selected spectral information for \(A+tE\), comparing PCG and deflated CG using first-order expansions and fixed perturbation directions. Their October 2026 manuscript expressly singles out varying perturbation directions and repeated eigenvalues as extensions. The present theorem treats a different, narrower observable: an exact *finite-radius worst-case spectral condition-number cap*, for the full-whitening limiting member of the spectral-preconditioner family. It neither proves nor substitutes for their CG-error comparison. Their March 2026 precursor optimizes the location of a spectral cluster for a finite iteration budget and does not supply a uniform Frobenius perturbation radius.

Giraud and Gratton analyze first-order eigenpair-error sensitivity of spectral preconditioners. Their Section 3.3 studies derivative-level condition numbers of individual perturbed eigenvalues; this does not imply a non-asymptotic, all-directions, sharp \(\kappa_2\) threshold. Rump analyzes structured condition numbers and distances to singularity, which concern a different failure event from exceeding a prescribed finite condition-number cap. The proof above is elementary and self-contained, and no claim is made that its spectral min-max or Frobenius-duality ingredients are new.

## Limitations
The result is an exact benchmark for full spectral whitening, not a low-memory algorithm or a practical condition estimator. It assumes real symmetric matrices, a Frobenius ball around the **unpreconditioned** system, perfect reference eigeninformation, and a fixed two-norm condition-number target. It does not bound condition numbers for partial deflation, restricted sparsity patterns, nonnormal systems or approximate eigenvectors. Prior-art coverage by other matrix perturbation or optimal-conditioning theorems cannot be ruled out completely; no independent mathematical review has been performed.

## References
1. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *Deflation-Based Spectral Preconditioning for the Conjugate Gradient Method on Perturbed Systems*, arXiv:2610.28808v1, first submitted 2026-10-20. https://arxiv.org/abs/2610.28808
2. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget*, arXiv:2603.28969v1, first submitted 2026-03-30. https://arxiv.org/abs/2603.28969
3. L. Giraud, S. Gratton, *On the Sensitivity of Some Spectral Preconditioners*, SIAM J. Matrix Anal. Appl. 27 (2006), 1089–1105; DOI:10.1137/040617546. Author-posted manuscript consulted.
4. S. M. Rump, *Structured Perturbations Part I: Normwise Distances*, SIAM J. Matrix Anal. Appl. 25 (2003), 1–30; DOI:10.1137/S0895479802405732. Abstract consulted.

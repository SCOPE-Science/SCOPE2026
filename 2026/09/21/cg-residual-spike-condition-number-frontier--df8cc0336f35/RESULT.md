# Sharp condition-number frontier for CG residual spikes

## Result

Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, with
\[
\mu=\lambda_{\min}(A)>0,\qquad L=\lambda_{\max}(A),\qquad \kappa=L/\mu.
\]
Run standard conjugate gradients in exact arithmetic on \(Ax=b\):
\[
r_0=b-Ax_0,\quad p_0=r_0,
\]
\[
\alpha_k=\frac{r_k^Tr_k}{p_k^TAp_k},\qquad
r_{k+1}=r_k-\alpha_kAp_k,
\]
\[
\beta_k=\frac{r_{k+1}^Tr_{k+1}}{r_k^Tr_k},\qquad
p_{k+1}=r_{k+1}+\beta_kp_k.
\]
For every nonterminal iteration,
\[
\boxed{
\frac{\|r_{k+1}\|_2}{\|r_k\|_2}
\le \frac{L-\mu}{2\sqrt{L\mu}}
=\frac{\kappa-1}{2\sqrt\kappa}
}
\]
and equivalently
\[
\boxed{
\beta_k\le \frac{(\kappa-1)^2}{4\kappa}.
}
\]
The constant is globally sharp for every \(\kappa\ge1\), already at the first iteration of a two-dimensional system.

Consequently, Euclidean CG residuals are guaranteed to be nonincreasing at every step for every SPD system of condition number at most \(\kappa\) if and only if
\[
\boxed{\kappa\le 3+2\sqrt2\approx5.82842712474619.}
\]
For every larger condition number there is a two-dimensional SPD system whose first CG step increases the Euclidean residual norm.

## Proof

### 1. Lanczos/CG factorization

Normalize the nonzero CG residuals, with alternating signs if necessary, to obtain the Lanczos basis. On the active Krylov subspace the resulting symmetric tridiagonal Lanczos matrix \(T\) is an orthogonal compression of \(A\). Hence
\[
\mu I\preceq T\preceq LI.
\]
The standard CG--Lanczos relation gives the factorization
\[
T=\mathcal L D\mathcal L^T,
\]
where \(\mathcal L\) is unit lower bidiagonal and, with the indexing above,
\[
D_{k+1,k+1}=\frac1{\alpha_k},\qquad
\mathcal L_{k+2,k+1}=\sqrt{\beta_k}.
\]
This is the usual \(LDL^T\) representation of the Lanczos tridiagonal in terms of CG coefficients.

### 2. A trailing Schur complement preserves the spectral interval

After eliminating the first \(k\) pivots of \(T\), let \(S_k\) be the remaining trailing Schur complement. Since
\[
L^{-1}I\preceq T^{-1}\preceq \mu^{-1}I
\]
and \(S_k^{-1}\) is the corresponding principal block of \(T^{-1}\), Cauchy interlacing gives
\[
\mu I\preceq S_k\preceq LI.
\]
The leading \(2\times2\) block of \(S_k\) has the form
\[
B_k=\begin{pmatrix}a&c\\c&d\end{pmatrix},
\qquad
 a=\frac1{\alpha_k},\qquad
 c=\frac{\sqrt{\beta_k}}{\alpha_k}.
\]
Thus
\[
\sqrt{\beta_k}=\frac{|c|}{a}.
\]
Moreover \(\mu I\preceq B_k\preceq LI\).

### 3. Sharp two-by-two lemma

For any real symmetric
\[
B=\begin{pmatrix}a&c\\c&d\end{pmatrix}
\]
satisfying \(\mu I\preceq B\preceq LI\), positivity of \(B-\mu I\) and \(LI-B\) gives
\[
c^2\le(a-\mu)(d-\mu),\qquad
c^2\le(L-a)(L-d).
\]
For fixed \(a\), the largest feasible \(|c|\) occurs when these two upper bounds are equal, i.e. when \(d=L+\mu-a\). Therefore
\[
c^2\le(a-\mu)(L-a).
\]
Hence
\[
\frac{c^2}{a^2}
\le \max_{a\in[\mu,L]}
\frac{(a-\mu)(L-a)}{a^2}
=\frac{(L-\mu)^2}{4L\mu},
\]
with the maximum at
\[
a=\frac{2L\mu}{L+\mu}.
\]
Applying this lemma to \(B_k\) proves
\[
\sqrt{\beta_k}\le\frac{L-\mu}{2\sqrt{L\mu}}.
\]
If CG has already terminated, then \(r_{k+1}=0\) and the assertion is trivial.

## Sharpness

Take
\[
A=\operatorname{diag}(\mu,L),\qquad
r_0=
\begin{pmatrix}
\sqrt{L/(L+\mu)}\\[2mm]
\sqrt{\mu/(L+\mu)}
\end{pmatrix}.
\]
Then \(\|r_0\|_2=1\) and the first CG step is the steepest-descent step with
\[
\alpha_0=\frac{L+\mu}{2L\mu}.
\]
A direct calculation gives
\[
\frac{\|r_1\|_2}{\|r_0\|_2}
=\frac{L-\mu}{2\sqrt{L\mu}}.
\]
Thus the all-step bound cannot be improved as a function of the global spectral condition number alone.

The universal residual-monotonicity threshold follows from
\[
\frac{\kappa-1}{2\sqrt\kappa}\le1
\iff \kappa\le3+2\sqrt2.
\]

## Conditioning certificate from an observed exact-arithmetic spike

If an exact CG step has observed ratio
\[
q=\frac{\|r_{k+1}\|_2}{\|r_k\|_2},
\]
then the sharp inequality implies
\[
\boxed{
\kappa(A)\ge\left(q+\sqrt{1+q^2}\right)^2.
}
\]
In particular, any exact-arithmetic spike \(q>1\) certifies
\(\kappa(A)>3+2\sqrt2\). This is a one-sided conditioning certificate; no analogous finite-precision claim is made here.

## Fixed SPD preconditioning

For a fixed SPD preconditioner \(M\), symmetric PCG is CG applied to
\[
\widetilde A=M^{-1/2}AM^{-1/2}.
\]
Since the transformed residual is \(\widetilde r_k=M^{-1/2}r_k\), the same result gives
\[
\boxed{
\frac{\|r_{k+1}\|_{M^{-1}}}{\|r_k\|_{M^{-1}}}
\le
\frac{\widetilde\kappa-1}{2\sqrt{\widetilde\kappa}},
\qquad
\widetilde\kappa=\kappa_2(M^{-1/2}AM^{-1/2}).
}
\]
This statement concerns the \(M^{-1}\)-norm of the residual. It does not assert the same bound for the ordinary Euclidean norm of PCG residuals.

## Relation to prior literature

Hestenes and Stiefel already observed that, without spectral restrictions, CG residual lengths can follow essentially arbitrary positive behavior. Bouyouli, Meurant, Smoch, and Sadok (2009, Theorem 3.3 in the openly available technical-report version) proved the all-step condition-number bound
\[
\frac{\|r_k\|_2}{\|r_{k-1}\|_2}\le\frac{\kappa(A)-1}{2}.
\]
The result above sharpens that all-step bound by a factor \(\sqrt\kappa\), and the two-dimensional construction proves the improved constant is best possible.

Meurant's 2020 prescribed-convergence analysis shows, in the two-dimensional case, a feasibility discriminant for simultaneously prescribing residual norms and eigenvalues. Rewritten in terms of the first residual ratio, that condition contains the same sharp two-eigenvalue first-step frontier. Thus the first-step constant itself is not claimed as new. To the best of our knowledge, the new content is that the same sharp constant governs **every** CG iteration for arbitrary dimension at fixed global condition number, together with the resulting exact universal monotonicity threshold and the fixed-preconditioner \(M^{-1}\)-residual consequence.

A 2024 survey by Carson, Liesen, and Strakoš emphasizes that CG residual behavior is nonlinear and can oscillate; the exact all-step frontier above was not located there or in the other checked sources.

### Sources

- M. R. Hestenes and E. Stiefel, *Methods of conjugate gradients for solving linear systems*, J. Res. Natl. Bur. Stand. 49 (1952), 409--436. https://doi.org/10.6028/jres.049.044
- R. Bouyouli, G. Meurant, L. Smoch, and H. Sadok, *New results on the convergence of the conjugate gradient method*, Numer. Linear Algebra Appl. 16 (2009), 223--236. https://doi.org/10.1002/nla.618 ; open technical report: https://www-lmpa.univ-littoral.fr/publications/articles/lmpa336.pdf
- G. Meurant, *On prescribing the convergence behavior of the conjugate gradient algorithm*, Numer. Algorithms 84 (2020), 1353--1380. https://doi.org/10.1007/s11075-019-00851-2
- E. Carson, J. Liesen, and Z. Strakoš, *Towards understanding CG and GMRES through examples*, Linear Algebra Appl. 692 (2024), 241--291. https://doi.org/10.1016/j.laa.2024.04.003

## Limitations

The theorem is an exact-arithmetic statement for standard CG on a real finite-dimensional SPD matrix. It uses the actual spectral condition number of \(A\); replacing the extreme eigenvalues by looser enclosing bounds remains valid but can be conservative. No floating-point residual-gap statement is implied. The PCG extension requires a fixed SPD preconditioner and applies to the \(M^{-1}\)-norm of the residual, not automatically to its Euclidean norm. Sharpness is global and already occurs at the first step; no claim is made that equality can be forced at every prescribed later iteration. Older monographs on Lanczos/CG and Gaussian-elimination multiplier bounds were not all accessible theorem by theorem, so historical-equivalence risk remains.

Same-model review: passed. Independent audit: not yet performed.

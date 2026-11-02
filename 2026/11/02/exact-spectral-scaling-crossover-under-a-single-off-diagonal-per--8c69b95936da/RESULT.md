# Exact spectral-scaling crossover under a single off-diagonal perturbation

## Finding

Let \(a>b>c>0\) and consider the reference symmetric positive-definite matrix \(A=\operatorname{diag}(a,b,c)\). Retain its first eigenvector as a one-dimensional recycled spectral subspace. Perturb the system by
\[
 A(t)=A+tE,\qquad E=(e_1e_2^{\mathsf T}+e_2e_1^{\mathsf T})/\sqrt2,\qquad 0<t<\sqrt{2ab}.
\]
Thus \(\|E\|_{\mathrm F}=1\), and the perturbed system remains positive definite. For the symmetric scaled spectral preconditioner
\[
 U_\theta=\operatorname{diag}(\sqrt{\theta/a},1,1),\qquad B_\theta(t)=U_\theta A(t)U_\theta,\qquad\theta>0,
\]
write \(d=t/\sqrt{2a}\), \(\Delta=b-c\), and \(d_c=\Delta/\sqrt b\). The unique minimizer of the spectral condition number \(\kappa_2(B_\theta(t))\) over every \(\theta>0\) is
\[
 \boxed{\theta_*(t)=\begin{cases}
 c\Delta/(\Delta-d^2),&0<d\le d_c,\\
 b,&d_c\le d<\sqrt b.
 \end{cases}}
\]
The formulas agree at \(d=d_c\). The **exact** optimal condition number is
\[
 \boxed{\inf_{\theta>0}\kappa_2(B_\theta(t))=
 \begin{cases}b/c+d^2/(\Delta-d^2),&0<d\le d_c,\\
 (\sqrt b+d)/(\sqrt b-d),&d_c\le d<\sqrt b.
 \end{cases}}
\]
At \(t=0\), in contrast, every \(\theta\in[c,b]\) is optimal, so the positive-perturbation uniqueness assertion intentionally excludes \(t=0\).

The small-perturbation optimum has the singular boundary-layer expansion
\[
 \theta_*(t)-c=\frac{ct^2}{2a(b-c)}+O(t^4)\qquad(t\downarrow0).
\]
Consequently the condition-number-optimal scale approaches the untouched eigenvalue \(c\) at order \(t^2\). At and beyond the explicit crossover \(t_c=\sqrt{2a}(b-c)/\sqrt b\), it equals the other untouched eigenvalue \(b\) exactly. This is an exact global optimization law, not an eigenvalue perturbation estimate.

## Assumptions and scope

The matrices are real and symmetric, \(a>b>c>0\), and \(0<t<\sqrt{2ab}\). A selected reference eigenpair \((a,e_1)\) is recycled **without updating its eigenvector** when the target matrix becomes \(A(t)\). The object optimized is the spectral ratio \(\lambda_{\max}(B_\theta(t))/\lambda_{\min}(B_\theta(t))\), not a finite-iteration PCG error, a choice of deflation subspace, or a uniform bound across all perturbation directions.

## Proof

**1. Reduction and positive definiteness.** Write \(d=t/\sqrt{2a}\), so \(0<d<\sqrt b\). Then
\[
 B_\theta(t)=\begin{pmatrix}
 \theta&d\sqrt\theta&0\\
 d\sqrt\theta&b&0\\
 0&0&c
 \end{pmatrix}.
\]
The upper block has determinant \(\theta(b-d^2)>0\) and trace \(\theta+b>0\). Its two eigenvalues are
\[
 L_\pm(\theta)=\frac{\theta+b\pm\sqrt{(\theta-b)^2+4d^2\theta}}2.
\]
In particular, \(L_+>b>c\). It follows exactly that
\[
 \kappa_2(B_\theta(t))=\frac{L_+(\theta)}{\min\{c,L_-(\theta)\}}.
\]

**2. The coupled-block optimum.** The ratio \(R(\theta)=L_+(\theta)/L_-(\theta)\) is a strictly increasing function of
\[
 H(\theta)=\frac{L_+(\theta)+L_-(\theta)}{\sqrt{L_+(\theta)L_-(\theta)}}
 =\frac{\theta+b}{\sqrt{\theta(b-d^2)}}.
\]
Indeed, \(H=\sqrt R+1/\sqrt R\), which is strictly increasing for \(R>1\); the coupling \(d>0\) guarantees \(R>1\). By the arithmetic--geometric mean inequality, \(\sqrt\theta+b/\sqrt\theta\) has its unique minimum at \(\theta=b\). Thus \(R\) strictly decreases for \(0<\theta<b\) and strictly increases for \(\theta>b\).

**3. Crossing of the untouched mode.** The lower block eigenvalue \(L_-(\theta)\) is strictly increasing in \(\theta\). For instance differentiating its explicit formula, the desired derivative inequality reduces to
\[
 ((\theta-b)^2+4d^2\theta)-(\theta-b+2d^2)^2=4d^2(b-d^2)>0.
\]
Furthermore \(L_-(0+)=0\) and \(L_-(\infty)=b-d^2\). Whenever \(d^2<b-c\), its unique crossing of \(c\) occurs at
\[
 (\theta-c)(b-c)=d^2\theta,
 \qquad \theta_0=\frac{c(b-c)}{b-c-d^2}.
\]
The condition \(\theta_0\le b\) is equivalent to
\[
 d^2\le\frac{(b-c)^2}{b},\quad\text{i.e. }d\le d_c.
\]
The same comparison can be performed directly at \(\theta=b\), where \(L_-(b)=b-d\sqrt b\). Thus \(L_-(b)\ge c\) precisely when \(d\le d_c\), including the case where \(L_-\) never crosses \(c\).

**4. Global minimization.** If \(d\le d_c\), then \(\theta_0\le b\). Before \(\theta_0\), the condition number equals \(R(\theta)\), which is strictly decreasing on \((0,\theta_0)\). After \(\theta_0\), its denominator is the fixed \(c\), and \(L_+(\theta)\) is strictly increasing, so the condition number increases. The unique minimizer is \(\theta_0\). There \(L_-=c\), and therefore \(L_+=\theta_0+b-c\), giving
\[
 \kappa_*=\frac{\theta_0+b-c}{c}=\frac bc+\frac{d^2}{b-c-d^2}.
\]
If \(d>d_c\), then \(L_-(b)<c\). For \(\theta\le b\), \(L_-<c\) and the condition number equals strictly decreasing \(R(\theta)\). For \(\theta\ge b\), if \(L_-<c\) it equals increasing \(R(\theta)\), whereas if \(L_-\ge c\) it equals increasing \(L_+(\theta)/c\). Therefore its unique minimizer is \(\theta=b\), where \(L_\pm=b\pm d\sqrt b\), yielding \(\kappa_*=(\sqrt b+d)/(\sqrt b-d)\). At the common boundary \(d=d_c\), both formulas yield \(\theta_*=b\), with \(L_-(b)=c\). All assertions follow.

**5. Small-perturbation scale.** In the first branch,
\[
 \theta_*(t)-c=\frac{cd^2}{b-c-d^2}
 =\frac{ct^2}{2a(b-c)}+O(t^4),
\]
which proves the boundary-layer statement and also identifies exactly why a fixed nonzero separation from the untouched eigenvalues is not uniform along the optimizer as \(t\) tends to zero.

## Verification

Run `python3 verify.py` using only the Python standard library. It checks the defining eigenvalue identities and crossing relation with exact fractions, exact branch values at representative rational coupling parameters, and independent numerical comparisons across log-spaced scales and a parameter grid. These computations check the implementation and algebra; the continuum global-optimality and uniqueness assertions rely on the proof above, not finite sampling.

For a transparent example, take \((a,b,c)=(9,4,1)\). At \(d=1\) (equivalently \(t=3\sqrt2\)), the unique optimum is \(\theta_*=3/2\) with \(\kappa_*=9/2\). At \(d=3/2\) the optimum is \(\theta_*=4\) and \(\kappa_*=7\). At \(d=8/5\), the optimum remains \(\theta_*=4\) and \(\kappa_*=9\). All three perturbed matrices are positive definite.

## Relationship to prior work

Diouane, Gürol, Mouhtal, and Orban (2026, arXiv:2610.28808, Section 3.3) study precisely this form of recycled symmetric spectral scaling for perturbed SPD systems, but use eigenpair asymptotics uniform only over scaling parameters separated from untouched reference eigenvalues by a fixed positive gap. The present statement is an exact condition-number optimizer for a specified three-mode perturbation and describes both the \(O(t^2)\) approach to an excluded eigenvalue and a finite-perturbation branch where the optimizer exactly equals another excluded eigenvalue. Their energy-norm comparison bound and this spectral-condition-number objective are distinct.

The 2026 predecessor arXiv:2603.28969 and 2024 precursor arXiv:2410.02204 address selection of cluster placement for finite-iteration PCG energy error, not this closed-form exact optimum across an off-diagonal perturbation. Giraud and Gratton (2006) analyze the *sensitivity* of spectral preconditioners to approximate eigen-information using first-order formulas; a related but different perturbation setting and outcome. Qu et al. (2022) provide general diagonal-preconditioning optimization algorithms, whose abstract capability includes computational approaches to such restricted instances, but not the present explicit collision threshold. No claim is made to invent spectral preconditioning, matrix scaling, quadratic eigenvalue formulas, or the condition-number objective itself.

## Limitations

This is a complete result only for a three-mode symmetric real SPD model with exactly one off-diagonal coupling and one recycled eigenvector. It optimizes a worst-case CG spectral proxy, not actual finite-iteration error for a specified right-hand side. It cannot be extrapolated to arbitrary perturbation directions, several recycled eigenvectors, nonnormal problems, or stochastic approximation. The historical comparison remains non-exhaustive; a specialized older arrowhead-matrix scaling calculation could imply the result even if not found in the inspected sources. There has been no independent mathematical audit.

## References

1. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *Deflation-Based Spectral Preconditioning for the Conjugate Gradient Method on Perturbed Systems* (2026), arXiv:2610.28808v1, https://arxiv.org/html/2610.28808v1 .
2. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget* (2026), arXiv:2603.28969, https://arxiv.org/abs/2603.28969 .
3. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *An Efficient Scaled Spectral Preconditioner for Sequences of Symmetric Positive Definite Linear Systems* (2024), arXiv:2410.02204, https://arxiv.org/abs/2410.02204 .
4. L. Giraud, S. Gratton, *On the Sensitivity of Some Spectral Preconditioners*, SIAM J. Matrix Anal. Appl. 27 (2006), 1089–1105, https://doi.org/10.1137/040617546 .
5. Z. Qu, W. Gao, O. Hinder, Y. Ye, Z. Zhou, *Optimal Diagonal Preconditioning* (2022), arXiv:2209.00809, https://arxiv.org/abs/2209.00809 .

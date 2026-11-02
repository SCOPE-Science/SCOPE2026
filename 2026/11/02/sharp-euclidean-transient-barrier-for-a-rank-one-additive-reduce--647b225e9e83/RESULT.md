# Sharp Euclidean transient barrier for a rank-one additive reduced-basis preconditioner

## Finding

Let \(A\in\mathbb R^{2\times2}\) be symmetric positive definite (SPD), let \(p\) be any Euclidean unit vector, and consider the Type-II additive reduced-basis inverse action
\[
 B_\alpha=p(p^{\mathsf T}Ap)^{-1}p^{\mathsf T}+\alpha(I-pp^{\mathsf T}),\qquad \alpha>0.
\]
The Richardson error propagator is \(T_\alpha=I-B_\alpha A\). Write \(\kappa=\lambda_{\max}(A)/\lambda_{\min}(A)\).

**Exact minimax theorem.** For every fixed \(\kappa\ge1\), including matrices and coarse lines in every orientation,
\[
 \boxed{\sup_{A\succ0:\,\kappa_2(A)=\kappa}\ \sup_{\|p\|_2=1}\ \inf_{\alpha>0}\|T_\alpha\|_2
 =\frac{\kappa-1}{2\sqrt\kappa}.}
\]
Thus the worst-case **optimally tuned** one-step Euclidean error amplification is below one exactly for \(\kappa<3+2\sqrt2\), equal to one at equality, and above one thereafter. It grows as \(\sqrt\kappa/2\) for large \(\kappa\). This is a one-step, worst-orientation statement; it is not an obstruction to asymptotic convergence.

**Exact individual-system safety interval.** Choose a unit vector \(q\perp p\) and put
\[
 a=p^{\mathsf T}Ap>0,\quad b=q^{\mathsf T}Aq>0,\quad h=p^{\mathsf T}Aq,
 \quad r=\frac{|h|}{a},\quad s=\frac{|h|}{b},\quad y=\alpha b.
\]
SPD implies \(rs=h^2/(ab)<1\). A strict Euclidean contraction \(\|T_\alpha\|_2<1\) is possible for some \(\alpha>0\) **if and only if** \(r<1\). For \(r<1\) its **entire** admissible range is
\[
 \boxed{\frac{1-\sqrt{(1-r^2)(1-r^2s^2)}}{1+(1-r^2)s^2}
 <\alpha b<
 \frac{1+\sqrt{(1-r^2)(1-r^2s^2)}}{1+(1-r^2)s^2}.}
\]
When \(h=0\), this reduces to \(0<\alpha b<2\). When \(r\ge1\), no positive \(\alpha\) makes the error operator a strict Euclidean contraction.

For \(A=\operatorname{diag}(\varepsilon,1)\) and \(p=(\cos\theta,\sin\theta)^{\mathsf T}\), where \(0<\varepsilon<1\) and \(0\le\theta\le\pi/2\), put \(t=\tan\theta\) for interior angles. The forbidden coarse directions are precisely
\[
 t^2-(1-\varepsilon)t+\varepsilon\le0.
\]
They exist if and only if \(\varepsilon\le3-2\sqrt2\); for strict inequality they form the closed interval between
\[
 t_\pm=\frac{1-\varepsilon\pm\sqrt{1-6\varepsilon+\varepsilon^2}}2.
\]
At equality there is one forbidden direction, \(t=\sqrt2-1\). At the eigenvector endpoints \(\theta=0,\pi/2\), contractivity is available.

## Assumptions and scope

The matrix is real, SPD and exactly two dimensional, \(\alpha\) is a positive scalar, \(p\) is orthonormalized, the reduced stiffness \(p^{\mathsf T}Ap\) is inverted exactly, and all norms are Euclidean operator norms. There is one exact Galerkin coarse direction and one scalar-corrected complementary direction. This is precisely the inverse action associated with the Type-II additive reduced-basis construction, when restricted to a fixed two-dimensional SPD system. The minimax order matters: the complementary coefficient can be optimized **after** knowing \(A,p\).

The theorem concerns \(T_\alpha=I-B_\alpha A\), corresponding to an undamped Richardson outer iteration. It does not concern the norm of the symmetrically preconditioned system, PCG convergence factors, or arbitrary higher-dimensional coarse complements.

## Proof

**1. Exact error matrix.** In the orthonormal basis \((p,q)\), the stiffness and inverse action are
\[
 A=\begin{pmatrix}a&h\\h&b\end{pmatrix},\qquad
 B_\alpha=\begin{pmatrix}1/a&0\\0&\alpha\end{pmatrix}.
\]
Consequently
\[
 T_\alpha=\begin{pmatrix}0&-h/a\\-\alpha h&1-\alpha b\end{pmatrix}.
\]
Changing the sign of \(q\) changes the signs of the off-diagonal entries without changing the operator norm. We may therefore express the norm through \(r,s\ge0\) and \(y=\alpha b>0\).

**2. The exact strict-contraction window.** Direct calculation yields
\[
 \det(I-T_\alpha^{\mathsf T}T_\alpha)
 =(1-r^2)(1-s^2y^2)-(1-y)^2
 =-r^2+2y-[1+(1-r^2)s^2]y^2.
\]
If \(r\ge1\), applying \(T_\alpha\) to the complementary basis vector gives
\(\|T_\alpha q\|_2\ge r\ge1\), so strict contraction is impossible.

Now suppose \(r<1\). By Sylvester's criterion, \(I-T_\alpha^{\mathsf T}T_\alpha\succ0\) if and only if its upper-left entry \(1-s^2y^2\) and its determinant are both positive. Positivity of the determinant already implies \(1-s^2y^2>0\), because \(1-r^2>0\) and \((1-y)^2\ge0\). Thus strict contraction is **equivalent** to positivity of the displayed concave quadratic. Its leading coefficient is negative and its discriminant is
\[
 4\bigl[1-r^2\{1+(1-r^2)s^2\}\bigr]
 =4(1-r^2)(1-r^2s^2)>0,
\]
where \(rs<1\) follows from SPD. Its two roots are exactly the stated endpoints; they are nonnegative and the interval between them is nonempty. This proves the pointwise characterization, including all strict boundary distinctions.

**3. Universal minimax upper bound.** Choosing \(\alpha=1/b\), which is always allowed, produces
\[
 T_{1/b}=\begin{pmatrix}0&-h/a\\-h/b&0\end{pmatrix},\qquad
 \|T_{1/b}\|_2=\max\{|h|/a,|h|/b\}.
\]
If the eigenvalues of \(A\) are \(\mu\le L\), rotate its eigenbasis by an angle \(\theta\). For \(t=|\tan\theta|\), the first ratio is
\[
 \frac{|h|}{a}=\frac{(L-\mu)t}{\mu+Lt^2}.
\]
The arithmetic-geometric mean inequality \(\mu+Lt^2\ge2\sqrt{\mu L}\,t\) gives
\[
 \frac{|h|}{a}\le\frac{L-\mu}{2\sqrt{\mu L}}.
\]
Interchanging \(p\) and \(q\) proves the identical bound for \(|h|/b\). Therefore, for every \(A,p\),
\[
 \inf_{\alpha>0}\|T_\alpha\|_2
 \le\|T_{1/b}\|_2
 \le\frac{\kappa-1}{2\sqrt\kappa}.
\]

**4. Sharp lower bound despite optimizing \(\alpha\).** Fix any \(\kappa>1\). Set \(\mu=1/\kappa\), \(L=1\), \(A=\operatorname{diag}(\mu,1)\), and choose a unit coarse vector with \(\tan\theta=\sqrt\mu\). The equality case of the preceding inequality yields
\[
 r=\frac{|h|}{a}=\frac{1-\mu}{2\sqrt\mu}
 =\frac{\kappa-1}{2\sqrt\kappa}.
\]
For **every** \(\alpha>0\), the norm of \(T_\alpha q\) is at least \(r\), hence \(\inf_\alpha\|T_\alpha\|_2\ge r\). Together with the universal upper bound, this proves exact minimax equality. For \(\kappa=1\), choosing \(\alpha=1/b\) makes \(B_\alpha=A^{-1}\) and the minimax value is zero. Solving \((\kappa-1)/(2\sqrt\kappa)=1\) yields the unique allowed threshold \(\kappa=3+2\sqrt2\).

**5. Principal-angle boundary and the spectral/Euclidean distinction.** With \(\mu=\varepsilon\), \(L=1\), and \(t=\tan\theta\), one has
\[
 r=\frac{(1-\varepsilon)t}{\varepsilon+t^2}.
\]
Thus \(r\ge1\) is exactly the stated quadratic inequality. Its discriminant is \(1-6\varepsilon+\varepsilon^2\), giving the angle cases and endpoints.

Finally \(B_\alpha\succ0\) for every \(\alpha>0\), so \(B_\alpha A\) is similar to the SPD matrix \(B_\alpha^{1/2}AB_\alpha^{1/2}\). Its two positive eigenvalues approach \(1\) and \(0\) as \(\alpha\downarrow0\). Thus for sufficiently small positive \(\alpha\), both lie in \((0,2)\), and \(\rho(T_\alpha)<1\). Hence the impossibility of Euclidean one-step contraction does **not** imply nonconvergence of the stationary iteration. This completes the proof.

## Verification

`verify_typeii.py` independently reconstructs the exact matrices and determinant polynomial; checks the discriminant and angle identities symbolically; performs 25,904 generic matrix-norm comparisons over rational coefficients; checks 48 exact sharp minimax families; and reconstructs the following exact rational example. The script reports success under Python 3 with SymPy and NumPy. The symbolic and finite checks corroborate the displayed proof and are not used as a substitute for it.

For \(A=\operatorname{diag}(1/16,1)\) and \(p=(4,1)^{\mathsf T}/\sqrt{17}\), choose \(q=(-1,4)^{\mathsf T}/\sqrt{17}\). Then
\[
 a=\frac2{17},\quad b=\frac{257}{272},\quad h=\frac{15}{68},\quad
 \frac{h}{a}=\frac{15}{8},\quad\frac{h}{b}=\frac{60}{257}.
\]
For every \(\alpha>0\), \(\|T_\alpha\|_2\ge15/8\). At \(\alpha=272/257=1/b\), equality holds. Thus optimal tuning still permits \(87.5\%\) one-step Euclidean amplification. Small positive \(\alpha\) nevertheless gives spectral convergence.

## Relationship to prior work

Fan, Hu and Zhang (2026, §3.1, equations (7)–(8), and §3.4) introduce the additive reduced-basis complement correction and investigate nonsingularity and error estimates for stationary Richardson updates. The present theorem addresses a distinct quantitative question: sharp Euclidean **one-step** safety, pointwise correction windows, and worst-case **optimally tuned** amplification. Those formulas do not appear in the inspected portions of the motivating manuscript.

The published result *Sharp Euclidean damping frontier for weighted Jacobi on \(2\times2\) SPD systems* develops the analogous Euclidean-norm issue for a **common scalar relaxation** \(\omega D^{-1}\). In particular, it already establishes the \(3+2\sqrt2\) universal standard-Jacobi threshold and the condition \(|h|\le\min\{a,b\}\) for the undamped Jacobi step. The threshold's numerical coincidence is therefore **not claimed as independently new**. The contribution here is the minimax equality with an **optimizable complementary scalar while the Galerkin coarse coordinate stays exact**, together with its exact pointwise \(\alpha\)-interval. The published common-damping conclusions alone do not give these optimized one-coordinate statements.

Demmel (2023) analyzes block-Jacobi scaling in relation to spectral condition numbers; that target differs from the Euclidean norm of this nonnormal Richardson propagator. Xu and Zhang (2020/2022) study two-grid convergence in energy norm, also a different metric and iteration. Classical theory of diagonal or block-diagonal relaxation could contain equivalent two-dimensional formulas, so exhaustive priority is not asserted.

## Limitations

Only a fixed real SPD two-dimensional linear system, a single orthonormal Galerkin coarse vector, positive scalar complementary correction and an undamped outer Richardson step are treated. The minimax is over all coarse-vector orientations and all SPD matrices with a fixed condition number. The theorem does not claim that the worst-case orientation is typical in reduced-basis training, that Euclidean one-step growth harms Krylov convergence, or that the scalar choice \(1/b\) is optimal at every individual orientation. For general dimensions or nonsymmetric/indefinite systems, the displayed sharp formula is not proved. The scientific review is not independent validation.

## References

1. X. Fan, Q. Hu and S. Zhang, *Additive reduced basis preconditioners for large-scale parametrized PDEs*, arXiv:2609.11097, first submitted 10 September 2026, especially §§3.1–3.4. https://arxiv.org/abs/2609.11097
2. *Sharp Euclidean damping frontier for weighted Jacobi on \(2\times2\) SPD systems*, published-finding corpus (2026), https://github.com/Resultary/2026/blob/main/2026/9/20/SCOPE-weighted-jacobi-euclidean-damping-frontier--457b47fc383f/RESULT.md
3. J. Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, SIAM J. Matrix Anal. Appl. 44 (2023), 408–413. https://doi.org/10.1137/22M1504901
4. X. Xu and C.-S. Zhang, *A new analytical framework for the convergence of inexact two-grid methods*, arXiv:2007.12754, first submitted 24 July 2020. https://arxiv.org/abs/2007.12754

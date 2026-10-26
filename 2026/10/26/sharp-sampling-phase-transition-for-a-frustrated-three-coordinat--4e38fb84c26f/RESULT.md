# Sharp sampling phase transition for a frustrated three-coordinate quadratic

## Finding

Let \(0<r<1\) and \(0<c<\sqrt r\). For the three-coordinate quadratic with Hessian
\[
C=\begin{pmatrix}1&r&c\\r&1&c\\c&c&1\end{pmatrix},
\]
there is a **sharp transition in the optimal fixed independent coordinate-sampling law**, although all three coordinate curvatures are equal. Write
\[
c_*(r)=\frac{\sqrt{(1-r)^2+16r}-(1-r)}{4}.
\]
The exact maximum sharp worst-case expected one-step energy decrement and one attaining sampling law \(p=(u_*,u_*,1-2u_*)\) are
\[
\boxed{u_*=
\begin{cases}
\dfrac{r-c^2}{r(3-r)-2c^2},&0<c\le c_*(r),\\[4pt]
\dfrac{1+c}{3+r+4c},&c_*(r)\le c<\sqrt r,
\end{cases}}
\]
and
\[
\boxed{\gamma_*=\max_{p\in\Delta_3}\gamma(p)=
\begin{cases}
\dfrac{(1-r)(r-c^2)}{r(3-r)-2c^2},&0<c\le c_*(r),\\[4pt]
\dfrac{1+r-2c^2}{3+r+4c},&c_*(r)\le c<\sqrt r.
\end{cases}}
\]
At the transition the formulas coincide. Strictly below the transition, the antisymmetric coordinate mode and the slow symmetric mode tie. Strictly above, the slow symmetric mode alone controls the minimum. This transition occurs in the smallest cyclic (three-variable) class whose inverse correlations cannot all be made nonnegative by changing variable signs.

## Assumptions and scope

Minimize \(f(x)=\tfrac12x^{\mathsf T}Cx\). At each step independently sample \(i\in\{1,2,3\}\) with fixed probabilities \(p_i\ge0\), \(\sum_i p_i=1\), then perform the *exact* coordinate update \(x^+=x-(Cx)_i e_i\). All diagonal entries of \(C\) equal \(1\). The parameter restrictions imply \(C\succ0\): the antisymmetric eigenvalue is \(1-r>0\), and the determinant of the remaining symmetric block is \(1+r-2c^2>1-r>0\). The error is measured by the objective gap, equivalently the squared \(C\)-energy.

For any probability vector, define \(P=\operatorname{Diag}(p)\) and
\[
\gamma(p)=\lambda_{\min}(P^{1/2}CP^{1/2}).
\]
The claimed optimum is the largest possible *sharp uniform conditional one-step* energy decrement; it does not optimize all asymptotic, sample-cost, tail-probability, or adaptive-sampling criteria.

## Proof

**1. Exact expected contraction.** The update decreases \(f\) by \(\frac12(Cx)_i^2\). Thus
\[
\mathbb E[f(x^+)\mid x]=f(x)-\tfrac12 x^{\mathsf T}CPCx.
\]
For \(x\ne0\), the ratio of the last decrement to \(f(x)\) is a Rayleigh quotient of \(C^{1/2}PC^{1/2}\), whose eigenvalues are those of \(P^{1/2}CP^{1/2}\). Hence the smallest eigenvalue is the exact worst-case decrement, attained by some nonzero initial state.

**2. Global reduction to symmetric sampling.** The map \(p\mapsto\gamma(p)=\lambda_{\min}(C^{1/2}PC^{1/2})\) is concave because its matrix argument is affine in \(p\). Swapping the first two coordinates preserves \(C\) and \(\gamma\). Averaging any \(p\) with its swap cannot lower \(\gamma\). Therefore the maximum over the full (possibly asymmetric) simplex is attained by a vector \(p=(u,u,v)\), \(v=1-2u\), \(0\le u\le\frac12\). This proves global optimality of a symmetric optimizer without asserting uniqueness of every optimizer.

**3. Competing spectral branches.** The antisymmetric vector \((1,-1,0)\) has eigenvalue \(a u\), where \(a=1-r\). The symmetric two-dimensional subspace has matrix
\[
B(u)=\begin{pmatrix}(1+r)u&c\sqrt{2uv}\\c\sqrt{2uv}&v\end{pmatrix},
\qquad v=1-2u.
\]
Write \(b=1+r\), and let \(\ell(u)\) be the smaller eigenvalue of \(B(u)\). Then
\[
\gamma(u)=\min\{a u,\ell(u)\},\quad
\ell(u)=\tfrac12\bigl(bu+v-\sqrt{(bu-v)^2+8c^2uv}\bigr).
\]
Both endpoints \(u=0\) and \(u=\frac12\) give \(\ell=0\). For \(0<u<\frac12\), \(\ell(u)>0\).

**4. Unique maximum of the symmetric-mode eigenvalue.** The smaller eigenvalue \(\ell(u)\) is concave in \(u\): its spectrum equals that of a constant positive-definite congruence of the affine diagonal matrix \(\operatorname{Diag}(u,1-2u)\). It is *strictly* concave for \(c>0\). Indeed, the radical discriminant is the square root of a quadratic \(Au^2+Bu+1\), with \(4A-B^2=32c^2(1+r-2c^2)>0\); the radical therefore has strictly positive second derivative. The equations
\[
(bu-q)(1-2u-q)-2c^2u(1-2u)=0,\qquad \partial_u[(bu-q)(1-2u-q)-2c^2u(1-2u)]=0
\]
are solved at
\[
u_s=\frac{1+c}{3+r+4c},\qquad q_s=\frac{1+r-2c^2}{3+r+4c}.
\]
Substitution verifies the eigenvalue equation; \(0<u_s<\frac12\), and the smaller eigenvalue is \(q_s\), since the trace of \(B(u_s)\) minus \(2q_s\) equals \(c>0\). Strict concavity then makes \(u_s\) the unique maximizer of \(\ell\) on \([0,\frac12]\).

**5. Eigenmode crossing.** For \(u>0\), compare \(\ell(u)\) with \(a u\). The characteristic determinant of \(B(u)-a uI\) equals
\[
2u\bigl[(r-c^2)(1-2u)-r(1-r)u\bigr].
\]
The other eigenvalue of \(B(u)\) is strictly greater than \(a u\): the upper-left diagonal entry is \(bu>au\), and the eigenvalues strictly straddle that diagonal entry because \(c>0\) and \(u,v>0\). Consequently \(\ell(u)\ge au\) exactly for \(u\le u_b\), where
\[
u_b=\frac{r-c^2}{r(3-r)-2c^2}\in(0,\tfrac12).
\]
Thus \(\gamma(u)=a u\) for \(u\le u_b\), whereas \(\gamma(u)=\ell(u)\) for \(u\ge u_b\). If \(u_s\le u_b\), \(\ell\) is already decreasing after crossing and the unique symmetric maximizer is \(u_b\). If \(u_s\ge u_b\), \(\ell\) continues to increase until \(u_s\), the unique symmetric maximizer.

**6. Exact transition and optimal values.** The sign of \(q_s-a u_s\) is the opposite of the sign of
\[
F(r,c)=2c^2+(1-r)c-2r.
\]
Since \(F(r,0)<0\), \(F(r,\sqrt r)>0\), and \(\partial_c F>0\), it has exactly one zero in \((0,\sqrt r)\), equal to \(c_*(r)\). At \(c=c_*(r)\), \(u_s=u_b\). For smaller \(c\), \(u_s<u_b\), giving \(u_*=u_b\) and \(\gamma_*=a u_b\); for larger \(c\), \(u_s>u_b\), giving \(u_*=u_s\) and \(\gamma_*=q_s\). At the boundary the two expressions agree. Combining with step 2 proves the unrestricted global formulas.

**7. Frustration rather than inverse positivity.** Cramer's rule gives off-diagonal entries of \(C^{-1}\) proportional to \(c^2-r<0\), \(c(r-1)<0\), and \(c(r-1)<0\), respectively; its determinant is positive. The product of their signs is negative and is invariant under any diagonal sign conjugation. Therefore no simultaneous sign change places this family inside the inverse-positive hypothesis used by the known closed-form sampling theorem.

## Verification

The standalone script `artifacts/frustrated_sampling_verification.py` uses SymPy for exact polynomial identities and exact characteristic spectra in three rational examples. It independently optimizes 90 random parameter pairs at five simplex starting points each using SciPy and checks the predicted analytic optimum. The recorded output is `artifacts/verification.txt`. The deterministic random seed is `78239`. The finite computational checks are auxiliary; the proof above covers *all* real parameters in the stated open domain.

## Relationship to prior work

Richtárik and Takáč (arXiv:1310.3438v1, 13 October 2013), especially Section 4, optimize nonuniform sampling using an expected separable-overapproximation convergence *bound*; they do not give the exact minimax one-step spectral optimum here. Gower and Richtárik (arXiv:1506.03296v1, 10 June 2015), Section 5.1 in the publicly available full version, formulate general optimal randomized-linear-solver sampling as a semidefinite program. Their generic SDP covers the present optimization problem implicitly, but does not itself state these two closed-form parameter regimes, the transition, or the mode-multiplicity mechanism.

Pukelsheim and Torsney (Annals of Statistics 19, 1991, 1614–1625), Sections 2–5, develop general optimal-design weight characterizations for independent support points. The corresponding saturated E-optimal design perspective is another formulation of the optimization, but the inspected full paper gives no frustrated inverse-sign triangle specialization or stated transition. An earlier closed-form theorem for entrywise inverse-positive quadratic Hessians also gives exact iid sampling, but its inverse-sign hypothesis decisively fails for this family, including after coordinate sign changes. This distinction is on assumptions and implications, not merely terminology.

## Limitations

A symmetric optimal sampling law is established; the theorem does **not** claim that all optimal laws are symmetric. The result is for one-step conditional expected \(C\)-energy contraction with fixed iid exact-coordinate minimization. It is not a guarantee of best wall-clock time, per-epoch rate, adaptive policy, or optimality for arbitrary nonsymmetric matrices. General semidefinite design methods already cover the underlying *optimization formulation*; the contribution claimed here is the explicit sharp solution and structural phase transition for this motivated non-inverse-positive family. Unlocated specialized E-optimal design or diagonal-scaling formulae remain an originality risk. No independent mathematical audit has been performed.

## References

1. P. Richtárik and M. Takáč, *On Optimal Probabilities in Stochastic Coordinate Descent Methods*, arXiv:1310.3438v1 (13 October 2013), https://arxiv.org/abs/1310.3438.
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296v1 (10 June 2015), https://arxiv.org/abs/1506.03296.
3. F. Pukelsheim and B. Torsney, *Optimal weights for experimental designs on linearly independent support points*, Ann. Statist. 19(3), 1614–1625 (1991), doi:10.1214/aos/1176348265.
4. P. Richtárik and M. Takáč, *On optimal probabilities in stochastic coordinate descent methods*, Optimization Letters 10, 1233–1243 (2016), doi:10.1007/s11590-015-0916-1.
5. The publicly indexed result *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* (2026), https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995.

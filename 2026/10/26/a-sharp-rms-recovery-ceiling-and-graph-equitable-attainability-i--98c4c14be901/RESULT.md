# A sharp RMS recovery ceiling and graph-equitable attainability in dispersive logistic populations

## Finding

For a connected undirected weighted graph with Laplacian \(L\), consider identical quadratic self-limitation and heterogeneous positive intrinsic growth rates:
\[
\dot x_i=r_i x_i-x_i^2-d(Lx)_i,\qquad r_i>0,\quad d\ge0.
\]
There is a unique strictly positive equilibrium \(x(d)\). Write \(J(d)=\operatorname{diag}(r_i-2x_i(d))-dL\), and define its **local asymptotic recovery exponent** \(\alpha(d)=-\lambda_{\max}(J(d))\). Let
\[
m=\frac1n\sum_{i=1}^n r_i,\qquad q=\left(\frac1n\sum_{i=1}^n r_i^2\right)^{1/2}.
\]
For every network and dispersal strength,
\[
\boxed{0<\alpha(d)\le q.}
\]
The bound is achieved **if and only if**
\[
\boxed{r_i^2-q^2=2d(Lr)_i\quad\text{for all }i,}
\]
in which case the equilibrium is \(x_i(d)=(r_i+q)/2\) and the complete Jacobian is \(J(d)=-qI-dL\). When the growth rates are nonconstant, at most one finite dispersal strength attains this ceiling. The unconstrained supremum is also strictly below \(q\) whenever the displayed equations have no nonnegative solution \(d\).

For the **complete mean-field mixing** normalization \(L=I-\mathbf{1}\mathbf{1}^{\mathsf T}/n\), the classification is exact:

1. If all rates equal \(a\), then \(\alpha(d)=a=q\) for every \(d\ge0\).
2. If the rates take exactly two values \(a\ne b\), then the unique rate-optimal dispersal strength is
   \[
   \boxed{d_*=(a+b)/2,\qquad \alpha(d_*)=q.}
   \]
3. If the rates take at least three distinct values, then \(\max_{d\ge0}\alpha(d)<q\).

More generally, on **any** connected weighted graph with exactly two intrinsic rates \(a\ne b\), the ceiling is attainable if and only if the centered growth-rate vector is an eigenvector of the graph Laplacian,
\[
L(r-m\mathbf{1})=\lambda(r-m\mathbf{1}),\qquad\lambda>0.
\]
The unique optimizer achieving the ceiling is then \(d_*=(a+b)/(2\lambda)\). Equivalently, within each growth-rate class, the total weighted degree to the opposite class must be the same for every vertex. This is an equitable two-class coupling condition.

As an exact three-patch illustration, take complete mean-field mixing with growth rates \((1,1,4)\). The unique optimizer is \(d_*=5/2\), where
\[
 x_* =\frac12(1+\sqrt6,\ 1+\sqrt6,\ 4+\sqrt6),\qquad \alpha(d_*)=\sqrt6.
\]
The endpoints are \(\alpha(0)=1\) and \(\lim_{d\to\infty}\alpha(d)=2\), both strictly below \(\sqrt6\). Thus sufficiently strong mixing is not the fastest way to recover locally from small population perturbations.

## Assumptions and scope

The graph is finite, connected, undirected, with symmetric nonnegative edge weights, at least two vertices, and \(L\mathbf{1}=0\). The self-limitation coefficient is the same positive constant at all sites and has been scaled to one by population normalization. All intrinsic growth rates are positive. The parameter \(d\) uniformly scales the fixed weighted Laplacian. At \(d=0\), all patches are isolated but their positive product equilibrium is unambiguous.

The term *recovery exponent* means the slowest real exponential rate of the **linearization at the positive equilibrium**; it is not the growth exponent at the extinction state, the transient speed from an arbitrarily distant initial condition, a stochastic resilience probability, or an ecological carrying-capacity objective. Symmetry of \(J\) makes this rate the negative largest real eigenvalue with no nonnormal qualification.

## Proof

**1. Existence and uniqueness.** The vector field is the gradient of
\[
\Phi(x)=\sum_i\left(\frac{r_i x_i^2}{2}-\frac{x_i^3}{3}\right)-\frac d2\sum_{\{i,j\}}w_{ij}(x_i-x_j)^2.
\]
On the nonnegative orthant, this potential is coercive and has a global maximizer. Since \(\Phi(t\mathbf{1})>0=\Phi(0)\) for sufficiently small \(t>0\), a maximizing vector is nonzero. If \(d>0\), any zero component adjacent to a positive component has strictly positive one-sided derivative \(d\sum_jw_{ij}x_j\), impossible at a maximum; connectivity therefore forces every component positive. At \(d=0\), the coordinatewise maxima occur at \(x_i=r_i>0\). Thus a positive equilibrium exists for every \(d\ge0\).

For uniqueness, suppose \(x,y>0\) are equilibria and \(t=\max_i x_i/y_i>1\), with equality \(x_k=ty_k\) for some \(k\). Since \(x_j\le ty_j\), at coordinate \(k\) the vector field obeys
\[
0=F_k(x)\le tF_k(y)-t(t-1)y_k^2<0,
\]
a contradiction. Hence \(x\le y\); interchanging \(x,y\) gives equality.

**2. Strict local stability.** Set \(v_i=x_i z_i\). Using the equilibrium equations to eliminate \(r_i\), the following **exact identity** holds for every real perturbation \(v\):
\[
 v^{\mathsf T}Jv=-\sum_i x_i v_i^2-d\sum_{\{i,j\}}w_{ij}x_i x_j(z_i-z_j)^2.
\]
Every \(x_i\) is strictly positive, so \(J\) is negative definite and \(\alpha(d)>0\).

**3. The universal bound and its equality case.** Summing the equilibrium equations cancels dispersal:
\[
\sum_i(x_i-r_i/2)^2=\frac14\sum_i r_i^2=\frac{nq^2}{4}.
\]
Cauchy--Schwarz implies
\[
\frac1n\sum_i x_i\le\frac{m+q}{2}.
\]
Equality holds exactly when \(x_i-r_i/2=q/2\) for every \(i\). The Rayleigh quotient of the unit constant vector in the symmetric Jacobian yields
\[
\lambda_{\max}(J)\ge m-\frac2n\sum_i x_i,
\qquad \alpha(d)\le\frac2n\sum_i x_i-m\le q.
\]
At equality in the last inequality, \(x=(r+q\mathbf{1})/2\) and hence \(J=-qI-dL\); the constant vector is its leading eigenvector, proving sufficiency. Substitution into the equilibrium equation gives
\[
\frac{r_i^2-q^2}{4}=\frac d2(Lr)_i,
\]
which is the displayed necessary-and-sufficient algebraic attainability criterion. For nonconstant \(r\), connectedness implies \(Lr\ne0\), so there is at most one such \(d\).

**4. Why unattainability is a strict optimization gap.** The positive equilibrium lies in the box \([\min_i r_i,\max_i r_i]^n\): evaluate the equilibrium equation at a minimizing and maximizing component. For \(d\to\infty\), the bounded reaction term gives \(Lx(d)=O(d^{-1})\). Because the graph is connected, its spectral gap implies that \(x(d)\) approaches a constant vector; the summed equilibrium equation forces that constant to be \(m\) (positive because the minimum rate is positive). Thus
\[
 \lim_{d\to\infty}x(d)=m\mathbf{1},
 \qquad\lim_{d\to\infty}\alpha(d)=m.
\]
For the spectral limit, the Rayleigh maximum of \(\operatorname{diag}(r_i-2x_i(d))-dL\) separates the constant direction from the negative diverging transverse modes; its slow eigenvalue converges to the constant-direction average \(m-2m=-m\). Smooth dependence of the equilibrium and \(\alpha(d)\) on every finite \(d\) follows from the strictly negative definite Jacobian and the implicit-function theorem. If the rates are nonconstant, \(m<q\), while \(\alpha(0)=\min_i r_i<q\). Therefore continuity on the compactified half-line makes the supremum a finite attained maximum; without an equality solution it is strictly smaller than \(q\).

**5. Exactly two rate classes.** If \(r_i\in\{a,b\}\), then the two-point identity
\[
 r_i^2-q^2=(a+b)(r_i-m)
\]
follows by writing the mean-square and mean of the two classes. Consequently the equality equation becomes
\[
2dL(r-m\mathbf{1})=(a+b)(r-m\mathbf{1}).
\]
For heterogeneous rates, this is equivalent to the stated positive-eigenvalue condition with \(d=(a+b)/(2\lambda)\). The component formula for \(Lr\) shows this is equivalent to constant cross-class weighted degrees within each class; symmetry of edge weights supplies the required consistency of the two constants. On the complete mean-field graph, \(L(r-m\mathbf{1})=r-m\mathbf{1}\), hence \(\lambda=1\). This proves the unique maximizer for exactly two rates.

For three or more different rates under complete mean-field mixing, the equality equation reduces to
\[
 r_i^2-2dr_i+(2dm-q^2)=0
\]
for every distinct rate \(r_i\). A nonzero monic quadratic cannot have three distinct real roots. Strictness follows from step 4. Constant growth rates give \(x=r\mathbf{1}\) and \(J=-rI-dL\), proving the remaining case. \(\square\)

## Verification

The standalone script `verify.py` executes exact rational tests of the equilibrium and complete-mean-field attainability formulas, exact rational checks of the two-class eigenvector criterion for a noncomplete weighted graph, and numerical tests of the global ceiling, local spectral rates, and unattainability gap for positive three-class instances. Run `python verify.py` with Python 3 and NumPy/SciPy installed. The analytical argument above, not finite tests, proves the quantified statements.

For the three-patch example, substituting \(q=\sqrt6\), \(r=(1,1,4)\) and \(d=5/2\) gives \(F(x_*)=0\) by the exact algebraic criterion, and \(J=-\sqrt6I-(5/2)L\). Its eigenvalues are \(-\sqrt6\) and \(-\sqrt6-5/2\) (twice), certifying the asserted rate without numerical approximation.

## Relationship to prior work

Jorba-Cuscó, Oliva-Zúniga, Sardanyés and Pérez-Palau study two coupled logistic patches, their global phase portrait, stochastic robustness, and diffusion **optimizing equilibrium biomass** (Theorem 4.4). Their two-patch results supply the motivating model, and the identity obtained by summing the equilibrium equations is already part of their optimization treatment. When their two patches have identical quadratic limitation, their biomass-optimal diffusion coincides with the special two-patch instance of the value above; that coincidence is **not** presented as a new optimization of biomass. Their stated objective and their results do not give a universal upper bound on the equilibrium Jacobian recovery exponent, a graph-spectral equality criterion, or the three-rate obstruction.

Earlier studies by Arditi, Lobry and Sari, and Arditi, Bersier and Rohr consider carrying capacity and mixing in logistic metapopulations, not the graph-spectral recovery-rate characterization established here. The 2015 Arditi--Lobry--Sari full text could not be inspected, so its relation beyond the available abstract remains a publication-priority risk. General results about graph logistic dynamics and spectral perturbations may provide alternate routes to portions of the conclusion; no claim of literature-exhaustive novelty is made.

## Limitations

The bound is tied to identical quadratic self-limitation, symmetric conservative dispersal, positive growth rates, and the largest eigenvalue of the positive-equilibrium Jacobian. It does not automatically apply to different self-limitation coefficients, directed migration, negative intrinsic rates, stochastic persistence, nonlinear far-from-equilibrium return times, or maximizing equilibrium biomass. Numerical checks use finitely many systems only. Independent validation has not been performed.

## References

- M. Jorba-Cuscó, R. I. Oliva-Zúniga, J. Sardanyés, and D. Pérez-Palau, *Dispersal-enhanced resilience in two-patch metapopulations: origin's instability type matters*, arXiv:2308.01364, version 1 publicly posted 2023-08-02; published as *Optimal dispersal and diffusion-enhanced robustness in two-patch metapopulations: origin's saddle-source nature matters*, *Theory in Biosciences* **143** (2024), 79–95, https://doi.org/10.1007/s12064-023-00411-2 ; https://arxiv.org/abs/2308.01364 .
- R. Arditi, F. Bersier, and R. Rohr, *The perfect mixing paradox and the logistic equation: Verhulst vs. Lotka*, *Ecosphere* **7** (2016), https://doi.org/10.1002/ecs2.1521 .
- R. Arditi, C. Lobry, and T. Sari, *Is dispersal always beneficial to carrying capacity? New insights from the multi-patch logistic equation*, *Theoretical Population Biology* (2015), https://doi.org/10.1016/j.tpb.2015.10.001 .

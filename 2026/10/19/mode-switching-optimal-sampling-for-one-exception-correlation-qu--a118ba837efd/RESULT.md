# Mode-switching optimal sampling for one-exception correlation quadratics

## Finding

There is an exact two-phase law for the best fixed independent coordinate-selection probabilities in exact randomized coordinate descent, even when **all coordinate Lipschitz constants are equal**. Let an integer \(m\ge2\) and real parameters \(0<\rho<1\), \(0<s<\sqrt\rho\) be given. On \(m+1\) coordinates define the symmetric matrix \(C\) by
\[
C_{ii}=1,\quad C_{1j}=C_{j1}=s\ (j>1),\quad
C_{ij}=\rho\ (i\ne j,\ i,j>1).
\]
Put
\[
\alpha=1+(m-1)\rho,\qquad \beta=1-\rho,\qquad
s_c=\frac{\sqrt{\beta^2+4m^2\rho}-\beta}{2m}.
\]
Then \(0<s_c<\sqrt\rho\), \(C\) is positive definite, and the **unique** probability vector attaining the best worst-case expected one-step reduction of \(C\)-energy assigns probability \(q\) to coordinate \(1\) and a common probability \(v\) to each other coordinate, where
\[
(q,v,\mu_*)=
\begin{cases}
\left(\dfrac{\beta\rho}{D},\dfrac{\rho-s^2}{D},\dfrac{\beta(\rho-s^2)}{D}\right),
&0<s\le s_c,\\[3mm]
\left(\dfrac{\alpha+ms}{E},\dfrac{1+s}{E},\dfrac{\alpha-ms^2}{E}\right),
&s_c\le s<\sqrt\rho,
\end{cases}
\]
with \(D=m(\rho-s^2)+\beta\rho\) and \(E=m+\alpha+2ms\). At \(s=s_c\), the two formulae agree. The exact optimal worst-case conditional contraction factor is \(1-\mu_*\). Below the threshold both a transverse eigenmode and a coupled eigenmode limit the optimal rate; above it only the coupled eigenmode is active. This is an exact result for the **one-step expected energy** criterion and makes no claim about finite-horizon optimality or wall-clock performance.

## Assumptions and scope

For \(b\in\mathbb R^{m+1}\) define \(f(x)=\tfrac12x^TCx-b^Tx\), with minimizer \(x_*=C^{-1}b\). Given fixed probabilities \(p_i\ge0\), \(\sum_i p_i=1\), choose one coordinate independently at each step and minimize \(f\) exactly along it:
\[
x^+=x-(Cx-b)_i e_i.
\]
All diagonal entries of \(C\) are one, so the coordinatewise Lipschitz constants are identical. Write \(\|e\|_C^2=e^TCe\) and define
\[
\mu(p)=\inf_{e\ne0}\frac{\|e\|_C^2-\mathbb E[\|e^+\|_C^2\mid e]}{\|e\|_C^2}.
\]
The theorem maximizes \(\mu(p)\) over **all** coordinate distributions, without a prior symmetry restriction. The range \(0<s<\sqrt\rho\) also keeps the inverse outside the entrywise-positive class, including after diagonal sign switching.

## Proof

**1. Exact contraction and strict definiteness.** For any error \(e=x-x_*\), a coordinate update satisfies
\[
\|e\|_C^2-\|e^+\|_C^2=(e_i^TCe)^2.
\]
Consequently, with \(P=\operatorname{diag}(p)\),
\[
\mu(p)=\lambda_{\min}(C^{1/2}PC^{1/2})
=\lambda_{\min}(P^{1/2}CP^{1/2}).
\]
On the transverse subspace among coordinates \(2,\ldots,m+1\), \(C\) has eigenvalue \(\beta>0\). On the remaining two-dimensional subspace its matrix is \(\left(\begin{smallmatrix}1&s\sqrt m\\s\sqrt m&\alpha\end{smallmatrix}\right)\), whose determinant \(\alpha-ms^2=\beta+m(\rho-s^2)>0\). Thus \(C\succ0\). The displayed eigenvalue also proves the sharpness of the conditional worst-case contraction for each \(p\).

**2. A symmetric optimizer exists.** The map \(p\mapsto\lambda_{\min}(C^{1/2}PC^{1/2})\) is concave because the matrix inside is affine in \(p\). Averaging any probability vector under permutations of coordinates \(2,\ldots,m+1\) cannot decrease \(\mu\). Therefore some maximizer has \(p=(q,v,\ldots,v)\), with \(q+mv=1\). A boundary distribution has \(\mu=0\), whereas every positive distribution has \(\mu>0\); hence a maximizer is interior.

**3. Spectrum and unique best symmetric probability.** Parametrize the symmetric interior by \(r=q/v>0\), so \(q=r/(m+r)\) and \(v=1/(m+r)\). The transverse eigenvalue is \(\beta/(m+r)\). The other two eigenvalues are those of
\[
\frac1{m+r}\begin{pmatrix}r&s\sqrt{mr}\\s\sqrt{mr}&\alpha\end{pmatrix}.
\]
Let \(\ell(r)\) be the lower eigenvalue of the unscaled two-by-two matrix, and put \(\delta=\alpha-ms^2>\beta\). The characteristic equation gives
\[
(r-\ell)(\alpha-\ell)=ms^2r,
\qquad
r=\frac{\ell(\alpha-\ell)}{\delta-\ell}.
\]
The latter expression is strictly increasing for \(0<\ell<\delta\), since its derivative has positive numerator \((\ell-\delta)^2+\delta ms^2\). Thus \(\ell\) increases strictly from zero to \(\delta\). The rate to maximize is
\[
\mu(r)=\frac{\min\{\beta,\ell(r)\}}{m+r}.
\]
The coupled branch \(\ell(r)/(m+r)\) has a **unique** maximum at
\[
r_{\rm peak}=\frac{\alpha+ms}{1+s},\qquad
\ell(r_{\rm peak})=\frac{\delta}{1+s}.
\]
Indeed, substituting \(r=\ell(\alpha-\ell)/(\delta-\ell)\) and differentiating produces a numerator proportional to \((\delta-(1+s)\ell)(\delta-(1-s)\ell)\); only the first root lies in \((0,\delta)\). The transverse and coupled branches cross uniquely at
\[
r_{\rm cross}=\frac{\beta\rho}{\rho-s^2}.
\]
For smaller \(r\) the coupled branch limits the rate; for larger \(r\) the transverse branch decreases strictly. Hence the unique symmetric maximum occurs at \(r_*=\min\{r_{\rm peak},r_{\rm cross}\}\). The condition \(r_{\rm cross}\le r_{\rm peak}\) simplifies to
\[
ms^2+\beta s-m\rho\le0,
\]
whose unique positive root is \(s_c\). Substituting the two possible ratios into \(q=r/(m+r)\), \(v=1/(m+r)\), and \(\mu(r)\) yields exactly the formulas in the finding. The root is strictly between zero and \(\sqrt\rho\), proving both regimes are nonempty.

**4. Uniqueness without an assumed symmetric candidate.** Let \(p_*=(q_*,v_*,\ldots,v_*)\) be the unique symmetric optimizer. Choose a unit eigenvector \(z\) of \(C^{1/2}P_*C^{1/2}\) for its lower **coupled** eigenvalue (at the crossing, select this vector within the tied minimal eigenspace). Put \(y=C^{1/2}z\). The entries of \(y\) on coordinates \(2,\ldots,m+1\) all coincide. Both this common entry and the first entry are nonzero: from the eigen-equation \(CP_*y=\mu_*y\), a zero in either class forces a zero in the other because \(s,q_*,v_*>0\), contradicting \(y\ne0\).

Now suppose any unrestricted probability vector \(p\) is optimal. Its permutation average is symmetric and optimal, hence equals \(p_*\). In particular, \(p_1=q_*\) and \(\sum_{i>1}p_i=mv_*\). Because \(y\) is constant on the ordinary class, its Rayleigh quotient obeys
\[
z^TC^{1/2}PC^{1/2}z=\sum_i p_i y_i^2
=\sum_i p_{*,i}y_i^2=\mu_*.
\]
As \(\mu(p)=\mu_*\), equality in the minimum-eigenvalue Rayleigh bound makes \(z\) an eigenvector of \(C^{1/2}PC^{1/2}\). Subtracting the eigen-equation for \(p_*\) and using invertibility of \(C^{1/2}\) gives \((p_i-p_{*,i})y_i=0\) for all \(i\). Since every \(y_i\ne0\), we obtain \(p=p_*\), proving **global uniqueness**.

**5. Boundary relative to inverse-positive sampling.** Direct block inversion gives, for two distinct ordinary indices,
\[
(C^{-1})_{ij}=\frac1m\left(\frac1\delta-\frac1\beta\right)<0,
\qquad
(C^{-1})_{1i}=-\frac{s}{\delta}<0.
\]
Thus any triple consisting of the exceptional coordinate and two ordinary coordinates has a **negative product of its three inverse off-diagonal entries**. Diagonal sign switching preserves this product, so no such switching makes \(C^{-1}\) entrywise nonnegative. This precisely excludes the sign-switch versions of the existing inverse-positive closed formula.

## Verification

Run `python3 VERIFY.py` using the Python standard library. The program tests the two spectral formulas in both regimes and at the boundary, checks thousands of unrestricted probability competitors and local perturbations, verifies the exact coordinate-energy identity with rational arithmetic, and checks the negative inverse-sign triangle. Its output is `PASS: 3727 rational and finite numerical assertions`. These finite calculations test algebra and examples only; the universal statements are proved in the preceding steps.

## Relationship to prior work

Coordinate-wise randomized optimization and nonuniform sampling were analyzed in Nesterov's foundational work and in Richtárik–Takáč's optimal probability bounds; Gower–Richtárik provide a general randomized linear-solver framework. Their general contraction or optimization principles do not, by themselves, state this one-exception correlation family's exact two-phase rates and globally unique probabilities. The related published inverse-positive result establishes a closed form when the inverse matrix is entrywise nonnegative; Step 5 proves its hypothesis cannot be met here, even after signed coordinate changes. Saturated E-optimal design theory of Pukelsheim–Torsney supplies a general optimal-design interpretation, but a direct explicit equivalence to these two formulas has not been identified in the inspected material.

## Limitations

This is a sharp **one-step conditional expected-energy** result for a specific positively correlated, structured family and exact, independently sampled, single-coordinate minimizations. It does not cover other correlation patterns, minibatches, accelerated methods, adaptive sampling, or actual computational cost. General E-optimal design literature is a genuine residual originality risk; the 1991 full text was not successfully retrieved for comprehensive exclusion. An implicit or unindexed specialization may exist. No independent validation has been performed.

## References

- Y. Nesterov, *Efficiency of Coordinate Descent Methods on Huge-Scale Optimization Problems*, SIAM J. Optim. 22 (2012), 341–362, doi:10.1137/100802001, published online 24 April 2012.
- P. Richtárik and M. Takáč, *On Optimal Probabilities in Stochastic Coordinate Descent Methods*, arXiv:1310.3438v1 (13 October 2013); Optimization Letters 10 (2016), 1233–1243, doi:10.1007/s11590-015-0916-1. Full open-access HTML sections 1–4 consulted.
- R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM J. Matrix Anal. Appl. 36 (2015), 1660–1690, doi:10.1137/15M1025487.
- F. Pukelsheim and B. Torsney, *Optimal Weights for Experimental Designs on Linearly Independent Support Points*, Ann. Statist. 19 (1991), 1614–1625, doi:10.1214/aos/1176348265.
- *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995 (public result text inspected).

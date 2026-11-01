# A universal supercritical oscillatory bifurcation in a circulating logistic triad

## Finding
For the clipped, cyclically interacting three-logistic-map family defined below, every positive circulation strength produces a loss of homogeneous-fixed-point stability **before** the uncoupled logistic-map flip. Apart from two specified low-order resonances, this loss is a supercritical Neimark–Sacker bifurcation with an attracting invariant closed curve. The exact critical growth rate and the first Lyapunov coefficient in the Fourier-amplitude normalization are
\[
r_{\mathrm c}(c)=1+\frac{2}{1+3c^2},\qquad
\ell_1(c)=-\frac{(3+3c^2)^3}{(1+3c^2)^2}<0.
\]
The strict sign is valid for **every** positive nonresonant circulation strength; its rational expression has no sign-changing parameter window. This supplies a finite, exactly solvable oscillatory-instability mechanism, rather than a large-network or random-matrix approximation.

## Assumptions and scope
Fix \(c>0\), \(r>1\), and indices \(j\in\mathbb Z/3\mathbb Z\). Define \(H(v)=\min\{1,\max\{0,v\}\}\) and the self-map of \([0,1]^3\)
\[
F_{r,c}(x)_j=H\!\left(r x_j\left[1-x_j+c(x_{j+1}-x_{j-1})\right]\right).
\]
The homogeneous interior fixed point is \(x_*=(q,q,q)\), with \(q=1-r^{-1}\). The clipping is inactive in a neighborhood of \(x_*\), so the local map is analytic. Write \(\kappa=\sqrt3 c\), \(t=r-1\), and \(\omega=e^{2\pi i/3}\). Set \(r_{\mathrm c}=1+2/(1+\kappa^2)\). For the invariant-circle conclusion assume additionally \(c\notin\{1/3,1/\sqrt3\}\); these exclusions remove the one-to-three and one-to-four linear resonances, and do **not** assert what happens at those parameters.

Local attraction means attraction of all sufficiently close points in the full three-dimensional state space. No global basin statement is made. The first Lyapunov coefficient refers to the complex Fourier coordinate \(Z=\frac13\sum_{j=0}^2(x_j-q)\omega^{-j}\) after a near-identity transformation with unit derivative, not to Euclidean radius in the original \(x\)-coordinates.

## Proof
**1. Exact spectral boundary.** At \(x_*\), the derivative has the diagonal entry \(2-r=1-t\), the cyclic forward entry \(ct\), and the cyclic backward entry \(-ct\). The three Fourier modes diagonalize it, yielding
\[
\lambda_0=1-t,\qquad
\lambda_{\pm}=1-t\pm i\kappa t.
\]
Consequently \(|\lambda_{\pm}|^2=(1-t)^2+\kappa^2t^2\), and \(|\lambda_{\pm}|<1\) exactly when \(0<t<2/(1+\kappa^2)\). On this interval \(|\lambda_0|<1\) as well. At \(t_{\mathrm c}=2/(1+\kappa^2)\), \(\lambda_0=(\kappa^2-1)/(\kappa^2+1)\in(-1,1)\), and \(\lambda_+\lambda_-=1\). For \(\mu=r-r_{\mathrm c}\), differentiating the modulus gives \(\left.\partial_r|\lambda_+|\right|_{r_{\mathrm c}}=1\), so the crossing is outward and transverse. Since \(r_{\mathrm c}<3\) for every \(c>0\), this oscillatory loss precedes the scalar logistic flip at \(r=3\).

**2. Exact polynomial Fourier equations.** Write, uniquely near the fixed point,
\[
x_j=q+U+Z\omega^j+\overline Z\,\omega^{-j},\qquad U\in\mathbb R,\quad Z\in\mathbb C.
\]
Direct substitution, with no discarded terms, gives the exact quadratic equations
\[
\begin{aligned}
U'&=(1-t)U-rU^2-2r|Z|^2,\\
Z'&=(1-t+i\kappa t)Z+r(-2+i\kappa)UZ-r(1+i\kappa)\overline Z^{\,2}.
\end{aligned}
\]
At \(r=r_{\mathrm c}\), let \(\lambda=1-t_{\mathrm c}+i\kappa t_{\mathrm c}=(\kappa+i)/(\kappa-i)\). A smooth local center manifold has the quadratic graph \(U=h|Z|^2+O(|Z|^3)\), where invariance and \(|\lambda|=1\) imply
\[
h=-\frac{2r_{\mathrm c}}{t_{\mathrm c}}.
\]
In the restricted complex equation, the quadratic and cubic coefficients relevant to the cubic resonant normal form are
\[
\beta=-r_{\mathrm c}(1+i\kappa),\qquad
\gamma=-\frac{2r_{\mathrm c}^2}{t_{\mathrm c}}(-2+i\kappa),
\]
so \(Z'=\lambda Z+\beta\overline Z^{\,2}+\gamma Z|Z|^2+O(|Z|^4)\).

**3. Cubic normal form and sign.** The unit-circle eigenvalue has no resonances of orders one or two for \(c>0\). Its only order-three resonance occurs at \(\kappa^2=1/3\), and its only order-four resonance occurs at \(\kappa^2=1\). Outside these two cases, eliminate the quadratic term by the near-identity coordinate change \(Z=W+p\overline W^{\,2}+O(|W|^3)\), with
\[
p=\frac{\beta}{\overline\lambda^{\,2}-\lambda}
=\frac{(1+\kappa^2)(3+\kappa^2)}{2(3\kappa^2-1)}.
\]
The resonant cubic coefficient is \(A=\gamma+2\beta\overline p\), and exact simplification gives
\[
\operatorname{Re}(\overline\lambda A)
=-\frac{(\kappa^2+3)^3}{(\kappa^2+1)^2}.
\]
In the radial normal form, \(R'=\bigl(1+\mu+O(\mu^2)\bigr)R+\ell_1 R^3+O(\mu R^2+R^4)\), where \(R=|W|\). The coefficient is strictly negative, without any sign exception in the stated domain.

**4. Attracting invariant circle.** The classical nonresonant Neimark–Sacker theorem applies to the two-dimensional center reduction: its critical pair crosses outward at nonzero speed, the nonresonance hypotheses hold, and \(\ell_1<0\). Thus, for each fixed permitted \(c\), there is \(\delta(c)>0\) such that, whenever \(0<r-r_{\mathrm c}<\delta(c)\), an attracting invariant Jordan curve bifurcates from \(x_*\). The remaining real multiplier stays uniformly within the unit circle in this sufficiently small parameter neighborhood, so the curve attracts transversely in the full three-dimensional system. Its leading Fourier radius satisfies
\[
|W|=\sqrt{\frac{(r-r_{\mathrm c})(1+\kappa^2)^2}{(\kappa^2+3)^3}}+O(r-r_{\mathrm c}).
\]
As the fixed point is interior, the curve lies in \((0,1)^3\) sufficiently close to onset and clipping does not affect the bifurcation.

For instance, \(c=1\) yields \(r_{\mathrm c}=3/2\), the noncritical multiplier \(1/2\), \(\lambda_+=e^{i\pi/3}\), and \(\ell_1=-27/2\), hence leading Fourier radius \(\sqrt{2(r-3/2)/27}\).

## Verification
The standalone `verify.py` uses SymPy to simplify the symbolic Fourier normal-form identity and the rational first Lyapunov coefficient. It independently compares the exact complex polynomial coordinates against 500 random evaluations of the original three-coordinate quadratic map, checks 300 numerical strict spectral-crossing cases, and compares two near-critical attracting trajectories with the predicted Fourier radius. All checks passed in the recorded execution. These finite tests are corroboration; the existence and universal sign claims follow from the analytic derivation and the standard bifurcation theorem.

Run with `python verify.py` in an environment with Python 3.10 or newer and SymPy installed. The check code computes only this model and has no external data inputs.

## Relationship to prior work
Baron and Galla, *The disordered logistic map* (2026), introduce a logistic-map interaction framework and investigate the oscillatory instability of high-dimensional randomly coupled populations. The present system is a deliberately balanced, deterministic, antisymmetric three-site specialization. No general random-matrix theorem is claimed here, and an explicit three-site normal-form coefficient is not a consequence of a large-system instability criterion.

Mareno and English (2020) establish flip and Neimark–Sacker bifurcations for a **two-variable, symmetrically coupled** logistic-map system; their formulas concern a different map and do not yield the circulation-strength identity above. Dementyeva, Kuznetsov, Savin and Sedova (2014) examine a three-site **additively and unidirectionally coupled** quadratic system of the form \(x_{n+1}=1-\lambda x_n^2+\varepsilon(x_n-y_n)\), rather than the present multiplicatively interacting logistic population map. The structural difference is important: neither calculation can be substituted for the present exact cubic coefficient. The standard Neimark–Sacker theorem is used as a known tool, not claimed as a new result.

## Limitations
The dynamics and attraction results are local, not global. The attracting circle conclusion excludes the one-to-three and one-to-four resonances \(c=1/3\) and \(c=1/\sqrt3\); linear stability boundaries still hold there. The analysis is for exactly three identically growing sites with balanced antisymmetric circulation, not arbitrary heterogeneous/random coupling matrices or other network sizes. The explicit normal-form amplitude is normalization-dependent; its sign and bifurcation type are not. Historical priority is provisional against specialized cyclic competitive-map literature, despite the inspected relevant articles.

## References
1. J. W. Baron and T. Galla, *The disordered logistic map*, arXiv:2609.24402 (first publicly submitted 2026-09-21), https://arxiv.org/abs/2609.24402.
2. A. Mareno and L. Q. English, *Flip and Neimark–Sacker Bifurcations in a Coupled Logistic Map System*, Discrete Dynamics in Nature and Society 2020, Article 4103606, https://doi.org/10.1155/2020/4103606.
3. I. S. Dementyeva, A. P. Kuznetsov, A. V. Savin and Y. V. Sedova, *Quasiperiodic dynamics of three coupled logistic maps*, Russian Journal of Nonlinear Dynamics 10 (2014), 139–148, https://doi.org/10.20537/nd1402001.
4. A. Kuznetsov, *Neimark–Sacker bifurcation*, Scholarpedia 3(5):1845 (2008), https://www.scholarpedia.org/article/Neimark-Sacker_bifurcation.

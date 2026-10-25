# A sharp circle-to-threefold-oval crossover for nearly maximal random inscribed triangles

## Finding
For \(0\le\eta<1/10\), consider the smooth convex body with polar radius
\[
r_\eta(\theta)=1+\eta\cos(3\theta),\qquad 0\le\theta<2\pi.
\]
Choose three points independently from its boundary by **uniform arclength**, and write \(T_\eta\) for their Euclidean triangle area. Put
\[
M_\eta=\frac{3\sqrt3}{4}(1+\eta)^2,\qquad
L_\eta=\int_0^{2\pi}\sqrt{r_\eta(\theta)^2+r_\eta'(\theta)^2}\,d\theta.
\]
Then \(M_\eta\) is the exact maximal possible triangle area. For every fixed \(0<\eta<1/10\),
\[
\Pr\{T_\eta>M_\eta-\varepsilon\}
\sim C_\eta\varepsilon^{3/2},
\quad
C_\eta=\frac{8\pi}{a_\eta\sqrt{b_\eta}}\left(\frac{1+\eta}{L_\eta}\right)^3,
\]
where
\[
a_\eta=\frac{3\sqrt3}{8}(1+\eta)(1+7\eta),\qquad
b_\eta=\frac{9\sqrt3}{4}\eta(1+\eta).
\]
There is also a **joint small-deformation/short-deficit law**: for every sequence \(\eta_\varepsilon\in[0,1/10)\) with \(\eta_\varepsilon/\varepsilon\to\lambda\in[0,\infty)\),
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr\{T_{\eta_\varepsilon}>M_{\eta_\varepsilon}-\varepsilon\}}{\varepsilon}
=\frac4{3\pi}F\!\left(\frac{3\sqrt3}{2}\lambda\right),
\]
with the *explicit* transition function
\[
F(s)=\begin{cases}
1-s,&0\le s\le\frac12,\\[3pt]
\displaystyle\frac{(1-s)\arccos(1-1/s)+s\sqrt{2/s-1/s^2}}{\pi},&s>\frac12.
\end{cases}
\]
At \(\eta=0\), this gives the known circular coefficient \(4/(3\pi)\). For any fixed \(\eta>0\), however small, the exponent is \(3/2\), not \(1\). The crossover profile changes formula sharply at \(\lambda=1/(3\sqrt3)\), where the contributing rotational phases cease to include the entire circle. More precisely, as \(s\downarrow1/2\) from above,
\[
F(s)=1-s+\frac{8\sqrt2}{3\pi}(s-1/2)^{3/2}+O((s-1/2)^{5/2}),
\]
so the profile is continuously differentiable but has a divergent second derivative at the phase cutoff. Both asymptotic regimes match:
\[
\lim_{s\to\infty}\sqrt{s}F(s)=\frac{2\sqrt2}{3\pi},\qquad
\lim_{\eta\downarrow0}\sqrt\eta\,C_\eta=\frac{16}{9\,3^{3/4}\pi^2}.
\]

## Assumptions and scope
The probability space consists of **exactly three** independent points sampled uniformly with respect to arclength on the boundary of a fixed polar threefold oval, except in the explicitly stated joint limit in which its shape parameter varies with the area threshold. The model is geometric probability for planar convex bodies, not a statement about a large random sample's maximum. All areas are ordinary unoriented Euclidean areas and all parameters are dimensionless. The strictly positive deformation \(\eta\) is less than \(1/10\); the undeformed circle is included in the joint scaling law. All asymptotics have \(\varepsilon\downarrow0\).

The radial curve is strictly convex: with \(c=\cos3\theta\), the numerator of its curvature is
\[
r_\eta^2+2(r_\eta')^2-r_\eta r_\eta''
=(1+\eta c)(1+10\eta c)+18\eta^2(1-c^2)>0.
\]
Its angular sampling density is \(g_\eta(\theta)=\sqrt{r_\eta(\theta)^2+r_\eta'(\theta)^2}/L_\eta\).

## Proof
**Global optimum and localization.** The body lies in the closed disk of radius \(R=1+\eta\). Every triangle contained in that disk has area at most \(3\sqrt3 R^2/4\), with equality precisely for a triangle joining three equally spaced points on the disk's boundary. For \(\eta>0\), the oval meets this circle at exactly the three angles \(0,2\pi/3,4\pi/3\), so there are exactly six labeled maximizing triples; for \(\eta=0\), all rotated equilateral triples maximize.

**Quadratic loss for fixed deformation.** Near the ordered triple of maxima, write the three angles as \(\theta_j=2\pi(j-1)/3+x_j\). The exact signed-area formula in a neighborhood is
\[
T_\eta=\frac12\sum_{j=1}^3r_\eta(\theta_j)r_\eta(\theta_{j+1})
\sin(\theta_{j+1}-\theta_j),\qquad\theta_4=\theta_1+2\pi.
\]
Taylor expansion gives
\[
M_\eta-T_\eta=
\frac{\sqrt3R^2}{8}\sum_{j=1}^3(x_{j+1}-x_j)^2
+\frac{9\sqrt3\eta R}{4}\sum_{j=1}^3x_j^2+O_\eta(\|x\|^3),
\]
where \(x_4=x_1\). In the orthonormal decomposition \(x=m(1,1,1)/\sqrt3+u\) with \(\sum_j u_j=0\), this is
\[
M_\eta-T_\eta=a_\eta\|u\|^2+b_\eta m^2+O_\eta(\|x\|^3).
\]
Both coefficients are strictly positive for \(\eta>0\). Rescaling the ellipsoidal neighborhood by \(\sqrt\varepsilon\), dominated convergence gives its angular-coordinate volume \(\frac{4\pi}{3}\varepsilon^{3/2}/(a_\eta\sqrt{b_\eta})+o(\varepsilon^{3/2})\). At each of the six maxima, the product of the three angular sampling densities is \((R/L_\eta)^3\). Summing these six disjoint contributions proves the fixed-deformation formula.

**Joint crossover.** Assume \(\eta_\varepsilon/\varepsilon\to\lambda<\infty\). The radius function differs uniformly from the unit circle by \(O(\varepsilon)\). Thus any triangle with deficit at most \(\varepsilon\) has angle triple within \(O(\sqrt\varepsilon)\) of the union of the two one-dimensional manifolds of labeled equilateral-circle configurations. On either manifold use coordinates
\[
(\theta_1,\theta_2,\theta_3)
=\phi(1,1,1)+(0,2\pi/3,4\pi/3)+u,
\quad u_1+u_2+u_3=0,
\]
with the other manifold reversing the order of the two nonbase vertices. Equip the two-dimensional \(u\)-plane with orthonormal coordinates. The Jacobian from \((\phi,u)\) to the triple of angles is \(\sqrt3\). Uniformly in the near-maximal region,
\[
M_{\eta_\varepsilon}-T_{\eta_\varepsilon}
=\frac{3\sqrt3}{2}\eta_\varepsilon(1-\cos3\phi)
+\frac{3\sqrt3}{8}\|u\|^2+o(\varepsilon).
\]
The sampling density product converges uniformly to \((2\pi)^{-3}\). For a given phase \(\phi\), the limiting admissible \(u\)-disk has area
\[
\frac{8\pi}{3\sqrt3}
\left[\varepsilon-\frac{3\sqrt3}{2}\eta_\varepsilon(1-\cos3\phi)\right]_+.
\]
Integration over \(0\le\phi<2\pi\), including both labeled orientation components and the Jacobian, gives
\[
\Pr\{T_{\eta_\varepsilon}>M_{\eta_\varepsilon}-\varepsilon\}
=\frac{4\varepsilon}{3\pi}\left[\frac1{2\pi}\int_0^{2\pi}
\Bigl(1-s_\varepsilon(1-\cos3\phi)\Bigr)_+d\phi\right]+o(\varepsilon),
\quad s_\varepsilon=\frac{3\sqrt3\eta_\varepsilon}{2\varepsilon}.
\]
The bracket converges to \(F(s)\). If \(s\le1/2\), the positive part never truncates the phase integral and \(F(s)=1-s\). If \(s>1/2\), the allowed phases satisfy \(|\phi|<\arccos(1-1/s)\) after folding by threefold periodicity, giving the stated arccosine expression. Writing \(s=1/2+t\) with \(t>0\), the removed negative phase region has width \(2\sqrt{8t}+O(t^{3/2})\) and negative integrand \(2t-\phi^2/4+O(t\phi^2+\phi^4)\); integration yields the stated \(t^{3/2}\) cusp with coefficient \(8\sqrt2/(3\pi)\). This proves the joint law, including its critical support transition. Finally the large-\(s\) expansion and the small-\(\eta\) expansion of \(L_\eta\) prove the displayed matched limits.

## Verification
The companion script `verify_trilobe.py` uses independent finite-difference Hessians, direct vertex-coordinate area calculations, spherical-ball importance sampling in the positive-definite quadratic neighborhood, and low-discrepancy integration of the angular crossover. Run using Python 3 with NumPy and SciPy installed:

```bash
python verify_trilobe.py
```

For \(\eta=0.01,0.05,0.09\), the numerical Hessian eigenvalues agree with \(b_\eta,a_\eta,a_\eta\). Fixed-deformation area-tail ratios approach one at deficits \(10^{-3}\) and \(2\times10^{-4}\). The computed joint-crossover probabilities agree with the limiting law at phase parameters \(0,1/4,1/2,3/4,2,5\). These are finite numerical checks; the global and asymptotic statements rely on the analytical argument above.

## Relationship to prior work
Koroleva and Nikitin, arXiv:1301.1360 (first posted 7 January 2013), state in Lemma B the *circular* three-point upper-area coefficient \(4/(3\pi)\), used here as a known consistency check. Their polygon results use a fixed circular circumference and do not provide a deformation-dependent distribution or joint shape/threshold crossover. The later general theorem of Nikitin and Simarova, arXiv:2010.04460, addresses rotation-invariant fixed kernels on a circle (assumption A1, Section 3) and samples with prescribed circle densities. The present triangle-area kernel is not rotation invariant when \(\eta>0\), and the joint limit changes the kernel together with its threshold; its explicit transition profile does not follow from the cited fixed-kernel theorem. The ordinary fixed-positive-\(\eta\) Gaussian-volume calculation is not claimed as a new method; the contribution is its exact geometric constant **and the uniform two-scale interpolation across a symmetry-breaking degeneracy**.

## Limitations
The formulas are confined to this threefold radial family, to independent *arclength-uniform boundary points*, and to rare events near the absolute maximum of triangle area. There is no assertion about general convex ovals, full triangle-area distributions, rates uniform for unbounded \(\eta/\varepsilon\), or large-sample extreme-value limits. The proof is mathematical but has not undergone independent external validation; the originality assessment is based on the cited and accessible literature and may not establish definitive historical priority.

## References
1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360, first posted 2013-01-07. https://arxiv.org/abs/1301.1360
2. Ya. Yu. Nikitin and E. N. Simarova, *Generalized Limit Theorems for U-max Statistics*, arXiv:2010.04460, first posted 2020-10-09. https://arxiv.org/abs/2010.04460
3. W. Lao and M. Mayer, *U-max-statistics*, Journal of Multivariate Analysis 99 (2008), 2039–2052, DOI 10.1016/j.jmva.2008.02.001 (foundational context, not used for the new calculation).

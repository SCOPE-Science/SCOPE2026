# Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks

## Finding

Let \(b>1\) and let \(c_1,\ldots,c_m\) be points on the unit circle in the Euclidean plane, where \(m\ge2\), with repetitions allowed. Let \(K_m=\bigcap_{j=1}^m\overline B(c_j,b)\). Starting from the labeled center \(c_1\) and proceeding counterclockwise, let \(\Delta_1,\ldots,\Delta_m\ge0\) be the consecutive angular gaps between centers (ties may be ordered arbitrarily), so that \(\sum_j\Delta_j=2\pi\). Set
\[
\rho_b(t)=-\cos t+\sqrt{b^2-\sin^2t},\qquad
F_b(s)=\int_0^{s/2}\rho_b(t)^2\,dt.
\]
The **exact circular-gap identity**, for every allowed configuration, is
\[
\operatorname{Area}(K_m)=\sum_{j=1}^m F_b(\Delta_j).
\]
The function \(F_b\) is strictly convex on \([0,2\pi]\). Consequently, the intersection area has the sharp lower bound
\[
\operatorname{Area}(K_m)\ge mF_b(2\pi/m),
\]
with equality exactly when the centers form a regular \(m\)-gon, up to a common rotation and relabeling. For completeness, the maximum over arbitrary positions is \(\pi b^2\), attained exactly when every center coincides.

Now choose the \(m\) center angles independently and uniformly from \([0,2\pi)\), and write \(A_m=\operatorname{Area}(K_m)\). The **exact finite-sample expectation** is
\[
\mathbb E A_m=m\int_0^\pi\rho_b(t)^2(1-t/\pi)^{m-1}\,dt.
\]
With \(a=b-1\) and \(\alpha=a^2/b\), as the number of centers tends to infinity,
\[
\mathbb E A_m-\pi a^2=\frac{2\alpha\pi^3}{(m+1)(m+2)}+O_b(m^{-4}),
\qquad
mF_b(2\pi/m)-\pi a^2=\frac{\alpha\pi^3}{3m^2}+O_b(m^{-4}).
\]
Thus the ratio of the random expected area excess to the best deterministic excess tends to **six**. Moreover,
\[
\boxed{\lim_{m\to\infty}m^5\operatorname{Var}(A_m)=40\alpha^2\pi^6},
\qquad
\boxed{m^{5/2}(A_m-\mathbb E A_m)
\ \xrightarrow{\mathrm d}\ \mathcal N(0,40\alpha^2\pi^6)}.
\]
These are distributional and variance limits for population sampling, not confidence bounds for finite observed samples.

## Assumptions and scope

The centers lie **on the unit circumference**, not uniformly in the interior of the disk. Every intersected disk has fixed radius \(b>1\); this ensures that the intersection contains \(\overline B(0,b-1)\) and is star-shaped about the origin. For nonrepeated deterministic centers, the gaps are strictly positive; repeated centers yield zero gaps and do not change the assertions. Random centers are independent with continuous uniform angular law, so repetitions have probability zero. All areas are ordinary two-dimensional Lebesgue areas. Error constants in \(O_b(\cdot)\) may depend on fixed \(b\), and all limits keep \(b\) fixed.

The circle-centered disk family approximates \(\overline B(0,b-1)\) from the outside: intersecting \(\overline B(c,b)\) over all \(c\) on the unit circle gives exactly \(\overline B(0,b-1)\). The theorem therefore compares optimal deterministic sampling and random sampling of boundary-constrained disk centers, and quantifies intrinsic area fluctuations of the resulting disc-polygons.

## Proof

**1. Radial formula and circular gaps.** For a ray of argument \(\theta\), the positive intersection radius of the disk with center at argument \(\phi\) is
\[
r_{b,\phi}(\theta)=\cos(\theta-\phi)+\sqrt{b^2-\sin^2(\theta-\phi)}.
\]
Let \(t\in[0,\pi]\) be the shorter angular distance between \(\theta\) and the *antipodal* center angle \(\phi+\pi\). Then \(r_{b,\phi}(\theta)=\rho_b(t)\), and
\[
\rho_b'(t)=\sin t\left(1-\frac{\cos t}{\sqrt{b^2-\sin^2t}}\right)>0
\quad(0<t<\pi),
\]
since \(b>1\) makes \(\sqrt{b^2-\sin^2t}>|\cos t|\). The radial function of the intersection is therefore \(\rho_b\) of the distance to the nearest antipodal center. A circular Voronoi cell belonging to one antipodal center extends halfway into each of its two adjacent gaps. Using the polar area formula, its contribution is a half-integral of \(\rho_b^2\) over each half-gap. Summing these pieces gives exactly \(\sum_jF_b(\Delta_j)\).

**2. Sharp deterministic extremum.** Differentiating the gap score yields \(F_b'(s)=\rho_b(s/2)^2/2\) and
\[
F_b''(s)=\tfrac12\rho_b(s/2)\rho_b'(s/2)>0
\qquad(0<s<2\pi).
\]
Continuity at endpoints gives strict convexity on the closed gap interval. Jensen's inequality with \(\sum_j\Delta_j=2\pi\) proves the sharp minimum, and its equality case forces all gaps to be \(2\pi/m\). Because any two distinct, equally sized disks have a strictly smaller intersection area than either full disk, \(\operatorname{Area}(K_m)=\pi b^2\) is possible only when all centers coincide.

**3. Exact expectation.** For independent uniform center angles, the nearest antipodal-center angular distance \(T\in[0,\pi]\) from a fixed ray has survival probability \(\mathbb P(T>t)=(1-t/\pi)^m\), hence density \((m/\pi)(1-t/\pi)^{m-1}\). The polar formula and rotational invariance now give the exact one-dimensional expectation integral in the finding.

**4. Uniform local expansion and gap moments.** A Taylor expansion at zero gives
\[
\rho_b(t)^2=a^2+\alpha t^2+O_b(t^4),\qquad
F_b(s)=\frac{a^2s}{2}+\frac{\alpha s^3}{24}+O_b(s^5).
\]
The remainder bound is uniform for \(0\le s\le2\pi\): the quotient of the Taylor remainder by \(s^5\) extends continuously at zero, and the interval is compact. Let \(S_p=\sum_j\Delta_j^p\). Since the angles are sampled independently and uniformly, conditioning on the first sampled angle and measuring the remaining angles relative to it shows that the **counterclockwise gaps anchored at the first sample** satisfy
\[
(\Delta_1,\ldots,\Delta_m)\ \overset{\mathrm d}=\
2\pi\frac{(E_1,\ldots,E_m)}{E_1+\cdots+E_m},
\]
where the \(E_i\) are independent exponential random variables of mean one. Thus \((\Delta_j/(2\pi))\) has the Dirichlet distribution with all concentration parameters equal to one. Its exact moments imply
\[
\mathbb E S_3=\frac{48\pi^3}{(m+1)(m+2)},\qquad
\mathbb E S_5=O(m^{-4}),
\]
and hence the expected-area asymptotic with remainder \(O_b(m^{-4})\). Applying the same expansion with \(\Delta_j=2\pi/m\) gives the regular configuration asymptotic and the factor-six ratio.

**5. Variance and Gaussian law.** Write \(R_m=A_m-\pi a^2-(\alpha/24)S_3\). By the uniform remainder bound, \(|R_m|\le C_bS_5\). The Dirichlet mixed moments give
\[
\mathbb E S_5^2=(2\pi)^{10}
\frac{m\,10!+m(m-1)(5!)^2}{m(m+1)\cdots(m+9)}
=O(m^{-8}),
\]
so \(\mathbb E R_m^2=O_b(m^{-8})\). For \(G_m=S_3/(2\pi)^3\), exact Dirichlet moments yield
\[
\operatorname{Var}(G_m)
=\frac{72(m-1)(5m+11)}{(m+1)^2(m+2)^2(m+3)(m+4)(m+5)}
\sim\frac{360}{m^5}.
\]
Cauchy–Schwarz shows \(R_m\) has negligible variance and covariance on the \(m^{-5}\) scale. Therefore
\[
m^5\operatorname{Var}(A_m)
\to \left(\frac{\alpha}{24}\right)^2(2\pi)^6\cdot360
=40\alpha^2\pi^6.
\]
For the distributional limit, let \(\overline E_m=m^{-1}\sum_iE_i\) and \(\overline{E^3}_m=m^{-1}\sum_iE_i^3\). The spacing representation becomes
\[
\frac{\alpha}{24}S_3
=\frac{\alpha\pi^3}{3m^2}
\frac{\overline{E^3}_m}{\overline E_m^3}.
\]
The bivariate central limit theorem and the delta method at \((6,1)\) produce the influence variable \(E_i^3-18E_i+12\), of mean zero and variance \(360\) (using exponential moments \(\mathbb E E_i^k=k!\)). Thus the cubic-gap term, centered, converges under multiplication by \(m^{5/2}\) to a centered normal with variance \(40\alpha^2\pi^6\). Since \(m^5\mathbb E R_m^2\to0\), the remainder disappears in \(L^2\) at this normalization, completing the central limit theorem with centering by the exact \(\mathbb E A_m\).

## Verification

The supplied `verify.py` uses only the Python standard library. Run `python verify.py` alongside this document. It separately computes each disk's positive radial root, integrates its pointwise minimum over orientation, and compares it with the angular-gap formula for 60 deterministic and seeded-random configurations across four radii and five sample sizes. It also checks the Jensen extremum, exact Dirichlet third-power moment identities, the delta-method variance \(360\), and approach to the factor-six efficiency ratio. In the performed execution it reported `VERIFY_OK independent_polar_cases=60 other_checks=16 max_area_error=2.65e-08`. The analytical argument, not the finite numerical tests, proves the results for all admissible radii and integers.

## Relationship to prior work

Paouris and Pivovarov study intersections of congruent balls with i.i.d. centers sampled from **bounded continuous densities in ambient space**, proving stochastic intrinsic-volume comparison inequalities. A singular uniform law on a fixed circumference is not covered by those density hypotheses, and their results do not state the exact circular-gap formula, finite-sample expectation, or limiting variance constant here.

Fejes Tóth and Fodor develop Dowker-type extremal principles and symmetric optimizers for disc-polygons containing a fixed hyperconvex disc. Their Theorems 1–2 are relevant to the deterministic optimizer; **existence of a rotationally symmetric optimal disc-polygon is not claimed as new in isolation**. The additional strict gap-Jensen equality condition, exact random mean, factor-six sampling loss, and sharp Gaussian/variance law are not statements of those inspected theorems.

Fodor and Vígh study random disc-polygons from i.i.d. points uniform in the *interior of the hyperconvex dual* or the original smooth body, with different area-deficit orders. Fodor and Papvári study another interior-sampling spindle-hull model. Neither interior-sampling result directly implies the boundary-angle law above. Classical exponential representations of uniform circular spacings supply the probabilistic input but do not independently identify this disk-intersection score and constants. Possible earlier equivalent boundary-sampling calculations remain a historical originality risk.

## Limitations

The geometry and the constants require the centers to lie on one fixed Euclidean circle and all disk radii to agree. The assumption \(b>1\) is essential for a strictly positive radial function and the proof's monotonicity inequality; no claim is made for \(b\le1\), higher dimensions, arbitrary boundary curves, or nonuniform sampling. The central limit theorem is asymptotic; no Berry–Esseen rate is established. The statement does not assert exhaustive historical novelty, and the general exponential-spacing central limit mechanism is standard.

## References

1. G. Paouris and P. Pivovarov, *Random ball-polyhedra and inequalities for intrinsic volumes*, arXiv:1510.07292, first posted 25 October 2015. https://arxiv.org/abs/1510.07292
2. G. Fejes Tóth and F. Fodor, *Dowker-type theorems for hyperconvex discs*, Periodica Mathematica Hungarica 70 (2015), 131–144. https://doi.org/10.1007/s10998-014-0071-y ; lawful full text: https://real.mtak.hu/33619/
3. F. Fodor and V. Vígh, *Variance estimates for random disc-polygons in smooth convex discs*, arXiv:1802.02808. https://arxiv.org/abs/1802.02808
4. F. Fodor and D. I. Papvári, *A central limit theorem for random disc-polygons in smooth convex discs*, arXiv:2310.18143. https://arxiv.org/abs/2310.18143
5. R. Pyke, *Spacings*, Journal of the Royal Statistical Society, Series B 27 (1965), 395–449. The uniform circular-spacing representation is used as a standard probabilistic fact.

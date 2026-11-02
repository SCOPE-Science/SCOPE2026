# Spectral topology and radial invisibility for two-scale atomic Hausdorff operators

## Finding
Fix \(\beta\geq0\), \(a\geq0\), \(b,c>0\) and distinct \(h,k>0\). On the upper half-plane Hardy space when \(\beta=0\), or weighted Hilbert Bergman space when \(\beta>0\), define the normalized dilation \(U_s f(z)=s^{-(\beta+1)/2}f(z/s)\) and
\[
T_{h,k}=aI+bU_{e^h}+cU_{e^k}.
\]
This is a positive three-atom Hausdorff operator. Let \(d=|b-c|\), \(R=b+c\), and \(m_{h,k}(\xi)=a+b e^{ih\xi}+c e^{ik\xi}\).

**(1) Spectrum and fine spectrum.** The operator is normal, has no eigenvalues, and has equal ordinary, approximate-point and Fredholm essential spectra. If \(h/k\notin\mathbb Q\), this common spectrum is the full closed annulus
\[
\{z\in\mathbb C:d\leq|z-a|\leq R\}.
\]
If \(h/k=q/p\) in lowest positive terms, where \(p\ne q\), it is instead the zero-area analytic curve
\[
\Gamma_{q,p}=\{a+b e^{iq\theta}+c e^{ip\theta}:\theta\in[0,2\pi]\}.
\]

**(2) Exact radial blindness.** For every continuous \(F\) on a disk containing the spectrum, the long-window Mellin-symbol mean
\[
\nu_{h,k}(F)=\lim_{L\to\infty}\frac1{2L}\int_{-L}^{L}F(m_{h,k}(\xi))\,d\xi
\]
exists and defines a probability measure. Although \(\nu_{h,k}\) has two-dimensional annular support in the irrational case and is carried by a zero-area curve in the rational case, its radial pushforward about \(a\) is **identical for every pair** \(h\ne k\):
\[
\nu_{h,k}\{|z-a|\leq r\}=\begin{cases}
0,&r<d,\\
\dfrac2\pi\arcsin\sqrt{\dfrac{r^2-d^2}{4bc}},&d\leq r\leq R,\\
1,&r>R.
\end{cases}
\]
For \(d<r<R\), the radial density is
\[
\frac{2r}{\pi\sqrt{(R^2-r^2)(r^2-d^2)}}.
\]
In the irrational case only, \(\nu_{h,k}\) is absolutely continuous with planar density
\[
\frac1{\pi^2\sqrt{(R^2-|z-a|^2)(|z-a|^2-d^2)}}
\]
on the open annulus and zero outside it. These formulas include the central-point limit when \(b=c\).

**(3) Exact arithmetic threshold of mixed-moment distinguishability.** For \(h/k=q/p\) coprime and unequal, let \(\nu_{\mathrm{irr}}\) denote the two-torus (irrational-ratio) value law at the same \(a,b,c\). For all nonnegative integers \(u,v\) with \(u+v<p+q\),
\[
\int(z-a)^u(\overline z-a)^v\,d\nu_{h,k}(z)
=\int(z-a)^u(\overline z-a)^v\,d\nu_{\mathrm{irr}}(z).
\]
The degree \(p+q\) is optimal: its moment indexed by \((u,v)=(p,q)\) has the exact positive defect
\[
\int(z-a)^p(\overline z-a)^q\,d\nu_{h,k}
-\int(z-a)^p(\overline z-a)^q\,d\nu_{\mathrm{irr}}=b^pc^q.
\]

**(4) Quantitative spectral filling by rational curves.** With Euclidean Hausdorff distance,
\[
d_{\mathrm H}\left(\Gamma_{q,p},\{z:d\leq|z-a|\leq R\}\right)
\leq\frac{\pi\sqrt{b^2+c^2}}{\sqrt{p^2+q^2}}.
\]
Thus rational spectra of arbitrarily high coprime degrees remain zero-area while converging quantitatively to the entire annulus, and their long-window laws converge weakly to the planar law (indeed their mixed moments agree through all degrees below \(p+q\)).

## Assumptions and scope
Let \(\mathbb U=\{z:\operatorname{Im}z>0\}\). For \(\beta>0\), the Bergman norm is \(\|f\|_{\beta}^{2}=\int_{\mathbb U}|f(x+iy)|^2y^{\beta-1}\,dx\,dy\); for \(\beta=0\), it is the usual Hardy norm \(\|f\|_0^2=\sup_{y>0}\int_{\mathbb R}|f(x+iy)|^2\,dx\). The spaces consist of holomorphic functions. The coefficient \(a\) is real and nonnegative and \(b,c\) are strictly positive, so the corresponding atomic measure is positive. All \(h,k\) are positive and distinct. The symbol-value mean above is a frequency-averaged distribution, **not** a normalized trace on the infinite-dimensional Hilbert space. The essential spectrum uses the Fredholm definition; equality to the full spectrum is asserted for these multiplication models only.

## Proof
**Unitary Mellin model.** By the Paley–Wiener–Plancherel representation, each of the spaces is (up to an irrelevant fixed normalizing constant) unitarily parametrized by \(g\in L^2((0,\infty),t^{-\beta}\,dt)\) via \(f(z)=\int_0^\infty e^{izt}g(t)\,dt\). Indeed Plancherel in the horizontal coordinate and integration in \(y\) give the factor \(\int_0^\infty e^{-2yt}y^{\beta-1}\,dy=\Gamma(\beta)/(2t)^\beta\) when \(\beta>0\); the boundary Hardy case is standard Plancherel. Changing integration variables shows that \(U_s\) corresponds to \(g(t)\mapsto s^{(1-\beta)/2}g(st)\). The logarithmic substitution \(x=\log t\) and unitary weight \(g(t)\mapsto e^{(1-\beta)x/2}g(e^x)\) conjugate it to translation \(H(x)\mapsto H(x+\log s)\) on \(L^2(\mathbb R)\). Fourier transformation therefore conjugates \(T_{h,k}\) to multiplication by \(m_{h,k}(\xi)\) (up to changing \(\xi\) to \(-\xi\), which does not affect any conclusion). This also proves that its measure realization is \(\mu=a\delta_1+b e^{(1-\beta)h/2}\delta_{e^h}+c e^{(1-\beta)k/2}\delta_{e^k}\) under the convention \((\mathcal H_\mu f)(z)=\int f(z/t)\,d\mu(t)/t\).

**Spectral topology and type.** For a bounded multiplication operator on \(L^2(\mathbb R)\), the spectrum is the essential range of its symbol. Here the continuous almost-periodic symbol has essential range equal to the closure of its ordinary range, since every open neighborhood of a value has a positive-measure preimage. In the irrational case the two-torus orbit \((e^{ih\xi},e^{ik\xi})\) is dense by Kronecker's theorem, hence the closure of \(m_{h,k}(\mathbb R)\) is the image of the two-torus under \((u,v)\mapsto a+bu+cv\), precisely the annulus \(d\leq|z-a|\leq R\). In the rational case choose coprime \(p,q>0\) with \(h/k=q/p\). The orbit is exactly \((e^{iq\theta},e^{ip\theta})\), giving \(\Gamma_{q,p}\); a continuously differentiable periodic plane curve has zero two-dimensional Lebesgue measure. The symbol is real analytic and nonconstant, so the inverse image of any fixed complex value is discrete and has Lebesgue measure zero; hence there is no point spectrum. On nonatomic \(L^2\), every value in the essential range gives an infinite-dimensional approximate null sequence and the corresponding multiplication operator is not Fredholm. Outside the range the inverse multiplier is bounded; thus ordinary, approximate-point and Fredholm essential spectra coincide.

**Radial law and planar density.** Irrational Kronecker equidistribution gives the pushforward of Haar measure on \(\mathbb T^2\); rational periodicity gives the pushforward of uniform \(\theta\). In either case the phase difference \(\Delta=(h-k)\xi\) is uniformly distributed modulo \(2\pi\), and
\[
|m_{h,k}(\xi)-a|^2=b^2+c^2+2bc\cos\Delta.
\]
Elementary integration of this cosine law yields the claimed cumulative and differentiated radial formulas, valid also when \(d=0\). In the irrational case common rotation of the two torus angles makes the sum rotationally invariant about \(a\); divide the radial density by the circle area factor \(2\pi r\) to obtain the planar density. The measure charges no boundary circles, so these densities describe the full measure.

**Moment threshold.** In the irrational case, the mean of each Laurent monomial \(U^jV^\ell\) on \(\mathbb T^2\) is zero unless \((j,\ell)=(0,0)\). In the rational case with \(U=e^{iq\theta}\), \(V=e^{ip\theta}\), it is nonzero precisely when \(qj+p\ell=0\). Since \(p,q\) are coprime, a nontrivial solution has the form \((j,\ell)=t(p,-q)\) and hence \(|j|+|\ell|\geq p+q\). Any Laurent monomial in the expansion of \((bU+cV)^u(bU^{-1}+cV^{-1})^v\) has \(|j|+|\ell|\leq u+v\); thus all moments below total degree \(p+q\) agree. At \((u,v)=(p,q)\), the only nontrivial resonant monomial possible is obtained by taking all \(p\) positive factors from \(bU\) and all \(q\) conjugate factors from \(cV^{-1}\), and its coefficient is exactly \(b^pc^q\). No opposite resonance can occur because the total positive and negative factor budgets are unequal. The nonresonant constant terms cancel in the comparison, proving optimality.

**Quantitative Hausdorff approximation.** On the flat two-torus of angular coordinates \((\theta,\varphi)\), the rational orbit equals the connected subgroup \(p\theta-q\varphi=0\pmod{2\pi}\). The nearest representative of this codimension-one subgroup is within Euclidean angular distance \(\pi/\sqrt{p^2+q^2}\), because consecutive parallel lifts of the subgroup have that perpendicular half-spacing. The map \((\theta,\varphi)\mapsto a+b e^{i\theta}+c e^{i\varphi}\) is \(\sqrt{b^2+c^2}\)-Lipschitz by Cauchy–Schwarz. Thus every point of the full annulus, represented by some torus angle pair, lies within the stated distance of an image point on the rational subgroup. The opposite directed distance is zero because every rational curve point already belongs to the annulus. Finally, polynomial moments are dense among continuous functions on the compact annulus, so the unbounded-degree moment match implies weak convergence along any sequence of coprime \(p,q\) with \(p+q\to\infty\).

## Verification
The standalone `verify.py` computes the relevant Laurent constant coefficients using exact integer combinatorics for all unequal coprime \(1\leq p,q\leq8\), the coefficient pairs \((b,c)=(1,2),(2,3)\), and all mixed moments below total degree \(p+q\). It checks the first positive defect \(b^pc^q\) separately. It also compares the radial cumulative formula against deterministic angular midpoint quadrature at twelve interior radii, including \(b=c\). Its successful output is `EXACT_MOMENT_TESTS_PASSED 4048` and `TOTAL_CHECKS_PASSED 4060`. These finite tests support arithmetic coefficients and normalization; the all-parameter and infinite-dimensional assertions are proved above.

## Relationship to prior work
Bellavita and Stylogiannis (arXiv:2603.08449v1, 2026) establish spectral transforms for Hausdorff operators on half-plane Hardy and Bergman spaces, and their Section 6 discusses discrete measures and convolution spectra. This supplies the motivating spectral framework and the general transform principle. The present result does not claim that transform principle as new: its contribution is the explicit rational-versus-irrational topological dichotomy **jointly with** the common radial distribution, sharp mixed-moment detection degree, and quantitative filling bound for normalized two-scale atomic operators. Hung and Ky (arXiv:2505.04043, 2025) study boundedness in related spaces. Abadias and Oliva-Maza (JFA 2024) study generalized Hausdorff spectral sets on disk-holomorphic spaces, not the same fixed upper-half-plane Hilbert-space realization. General Fourier and Kronecker orthogonality are used as known principles. The published three-frequency even-moment resonance result concerning trigonometric trinomials is mathematically related but treats reconstruction of three-point supports and unimodular phases rather than this operator spectral/radial dichotomy.

## Limitations
No new theorem about arbitrary Hausdorff measures or the \(L^p\) spectrum for \(p\ne2\) is claimed. The geometric classification is based on the established multiplier transform; the specific novel candidate is its combined arithmetic/measure-theoretic refinement for two normalized atoms beyond the identity. The quantity \(\nu_{h,k}\) is an explicitly defined Bohr-frequency law, not an operator trace measure. The Hausdorff estimate is an upper bound, not an asserted optimal constant. An earlier equivalent package of spectral-value and arithmetic distribution results could exist under almost-periodic or finite-Fourier terminology. The accessible 2024 general spectral-set paper was available by abstract but not fully inspectable during this comparison, so its potential implication coverage remains a specific publication-priority risk. Independent mathematical review is outstanding.

## References
1. Carlo Bellavita and Georgios Stylogiannis, *Spectrum of Hausdorff operators on weighted Bergman and Hardy spaces of the upper half-plane*, arXiv:2603.08449v1, first public 2026-03-09, primary MSC 47B91, https://arxiv.org/html/2603.08449v1.
2. Ha Duy Hung and Luong Dang Ky, *Hausdorff operators on weighted Bergman and Hardy spaces*, arXiv:2505.04043v1, first public 2025-05-07, https://arxiv.org/abs/2505.04043.
3. Luciano Abadias and Jesús Oliva-Maza, *Spectral sets of generalized Hausdorff matrices on spaces of holomorphic functions on the disk*, Journal of Functional Analysis 286 (2024), 110298, https://doi.org/10.1016/j.jfa.2023.110298.
4. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79.

# Axis-coalescence crossover for long invariant chords of high-dimensional ellipsoids

## Finding
For an ellipsoid in dimension \(d\ge4\), a line sampled by Euclidean-motion-invariant Crofton measure, conditional on hitting the ellipsoid, has a long-chord probability whose power exponent changes when the multiplicity of the longest semiaxis changes. The complete transition on the natural semiaxis-splitting scale is a beta integral, with an explicit leading constant.

Fix an integer \(d\ge4\), an integer \(1\le r\le d-1\), a length \(a>0\), and fixed shorter semiaxes \(b_{r+2},\ldots,b_d\in(0,a)\) (the list may be empty). Let \(\lambda\ge0\) and, for \(0<\varepsilon<1\), define the ellipsoid \(E_{\varepsilon,\lambda}\subset\mathbb R^d\) with semiaxes
\[
\underbrace{a,\ldots,a}_{r\text{ times}},\quad
\frac{a}{\sqrt{1+\lambda\varepsilon}},\quad
b_{r+2},\ldots,b_d.
\]
Write \(L_{\varepsilon,\lambda}\) for the chord length of an invariantly sampled **unoriented affine line conditioned to intersect** this ellipsoid. Put
\[
k=r+1,\quad m=d-k,\quad p=\frac{d-1}{2},\quad
\beta=p+\frac m2=d-\frac{r+2}{2},\quad
\gamma_j=\frac{a^2}{b_j^2}-1>0\quad(j>k).
\]
Let \(U\) be uniform on \(S^{d-1}\), and set
\[
H_0=\mathbb E\sqrt{1+\sum_{j=k+1}^{d}\gamma_jU_j^2},\qquad
C_{d,r}=\frac{2^\beta\Gamma(d/2)\Gamma((d+1)/2)}
{\Gamma((r+1)/2)\Gamma(\beta+1)H_0\prod_{j=k+1}^{d}\sqrt{\gamma_j}}.
\]
Empty products equal one. Define
\[
\mathcal F_{d,r}(\lambda)=\frac1{B(1/2,r/2)}
\int_0^1 t^{-1/2}(1-t)^{r/2-1}
\bigl(1-\lambda t/2\bigr)_+^{\beta}\,dt,
\]
where \(x_+=\max(x,0)\). Then, **for every fixed \(\lambda\ge0\)**,
\[
\boxed{\lim_{\varepsilon\downarrow0}
\varepsilon^{-\beta}\mathbb P\bigl(L_{\varepsilon,\lambda}>2a(1-\varepsilon)\bigr)
=C_{d,r}\,\mathcal F_{d,r}(\lambda).}
\]
Convergence is locally uniform in \(\lambda\in[0,\infty)\). The profile is positive, continuous and strictly decreasing on \([0,\infty)\), has \(\mathcal F_{d,r}(0)=1\), and satisfies
\[
\boxed{\mathcal F_{d,r}(\lambda)\sim
\sqrt{\frac2\lambda}\,
\frac{B(1/2,\beta+1)}{B(1/2,r/2)}
\qquad(\lambda\to\infty).}
\]
The large-parameter coefficient agrees exactly with the fixed-ellipsoid tail constant when the formerly coalescing axis is instead separated by a fixed positive squared-inverse-axis gap; its exponent is then \(\beta+1/2\). Thus the profile resolves the singular transition between the \(r+1\)-fold and \(r\)-fold maximum-axis classes.

For reference, the underlying fixed-shape endpoint law, obtained by the same proof, is the following: if a \(d\)-ellipsoid has precisely \(s\in\{1,\ldots,d\}\) longest semiaxes equal to \(a\), with \(\eta_j=(a/b_j)^2-1\) for its remaining axes, and \(H=\mathbb E\sqrt{1+\sum\eta_jU_j^2}\), then its invariant chord length \(L\) obeys
\[
\mathbb P(L>2a(1-\varepsilon))\sim
\frac{2^{d-(s+1)/2}\Gamma(d/2)\Gamma((d+1)/2)}
{\Gamma(s/2)\Gamma(d-(s-1)/2)\,H\prod\sqrt{\eta_j}}
\varepsilon^{d-(s+1)/2}.
\]
For \(s=d\) the products are empty, \(H=1\), and this reduces to the exact spherical endpoint exponent. The crossover, rather than this elementary sphere specialization or previously known low-dimensional distributions, is the central contribution.

## Assumptions and scope
All ellipsoids are full-dimensional Euclidean ellipsoids. The moving semiaxis \(a/\sqrt{1+\lambda\varepsilon}\) approaches the tied maximum on the same \(\varepsilon\) scale as the relative chord-length deficit. The other shorter axes remain strictly below \(a\). Probabilities always use the Euclidean-motion-invariant measure on affine lines, **conditioned on intersection**; uniformly sampling a direction followed by an independently chosen chord is a different experiment. No Gaussian-point, two-point, or fixed-central-line sampling is used.

The asymptotic statement fixes \(d,r,a,b_j,\lambda\) before letting \(\varepsilon\downarrow0\). Local uniformity permits \(\lambda\) to vary within a fixed compact interval. No uniform simultaneous regime with \(\lambda\to\infty\) is claimed.

## Proof
**1. The exact Crofton law.** Write \(E=A B_d\), where \(A\) is a positive diagonal matrix. Parameterize an unoriented affine line by its unit direction \(u\) (modulo sign) and offset \(y\in u^\perp\). Invariant line measure is, up to an irrelevant multiplicative constant, spherical direction measure times \((d-1)\)-dimensional offset Lebesgue measure. Thus directions of lines meeting \(E\) have density proportional to the brightness
\[
\operatorname{vol}_{d-1}(E\mid u^\perp)
=\kappa_{d-1}(\det A)\sqrt{u^TA^{-2}u}.
\]
The identity follows, for example, by taking the Gram determinant of the restriction of \(A\) to an orthonormal basis of \(u^\perp\), or by the Schur-complement determinant identity. Conditional on \(u\), the offset is uniform in the projected ellipsoid. After a linear change of offset variables, its coordinates are uniform on the unit \((d-1)\)-ball, say \(W\). Completing the square in the quadratic line-intersection equation gives exactly
\[
L=\frac{2\sqrt{1-\|W\|^2}}{\sqrt{u^TA^{-2}u}}.
\]
Consequently \(\mathbb P(\|W\|^2<z)=z^p\) for \(0\le z\le1\), where \(p=(d-1)/2\).

For the displayed ellipsoid, write
\[
Q_\varepsilon(u)=a^2 u^TA^{-2}u
=1+\lambda\varepsilon u_k^2+\sum_{j>k}\gamma_j u_j^2,
\qquad H_\varepsilon=\mathbb E\sqrt{Q_\varepsilon(U)}.
\]
The preceding identities give the **exact** survival formula for any \(t>0\):
\[
\mathbb P(L_{\varepsilon,\lambda}>t)=
\frac{\mathbb E\left[\sqrt{Q_\varepsilon(U)}
\left(1-\frac{t^2}{4a^2}Q_\varepsilon(U)\right)_+^p\right]}{H_\varepsilon}.
\tag{1}
\]
This identity includes the Crofton direction bias, whose omission would change the leading constant.

**2. Split the almost-maximum eigenspace.** Let \(z=(U_{k+1},\ldots,U_d)\in\mathbb R^m\). For \(m>0\), its density on \(\|z\|<1\) is
\[
f(z)=\frac{\Gamma(d/2)}{\pi^{m/2}\Gamma(k/2)}
(1-\|z\|^2)^{k/2-1}.
\]
Conditionally on \(z\), the remaining \(k\) coordinates are uniform on the sphere of radius \(\sqrt{1-\|z\|^2}\). In particular,
\[
U_k^2=(1-\|z\|^2)T,\qquad
T\sim\operatorname{Beta}(1/2,r/2),
\]
with \(T\) independent of \(z\). For \(m=0\), the same statement holds with \(z=0\), density integration replaced by evaluation at zero, and the empty-product convention.

**3. Scaling of the rare region.** Set \(t=2a(1-\varepsilon)\), \(\delta=2\varepsilon-\varepsilon^2\), and
\[
X=\lambda\varepsilon(1-\|z\|^2)T+\sum_{j>k}\gamma_jz_j^2.
\]
Equation (1) reduces exactly to
\[
\frac1{H_\varepsilon}\mathbb E\left[
\sqrt{1+X}\bigl(\delta-(1-\varepsilon)^2X\bigr)_+^p\right].
\tag{2}
\]
The integrand vanishes unless \(\sum\gamma_jz_j^2\le\delta/(1-\varepsilon)^2\). For \(m>0\), set
\[
z_j=\frac{\sqrt\delta}{1-\varepsilon}\frac{v_j}{\sqrt{\gamma_j}}
\qquad(j>k).
\]
The integration domain is confined to \(\|v\|\le1\). On this domain \(z\to0\), the density tends uniformly to \(\Gamma(d/2)/(\pi^{m/2}\Gamma(k/2))\), the brightness factor tends uniformly to one, \(H_\varepsilon\to H_0\), and the normalized positive part tends to
\[
\bigl(1-\|v\|^2-(\lambda/2)T\bigr)_+^p.
\]
These convergences are uniform when \(\lambda\) lies in any fixed compact interval. All integrands are bounded by an integrable constant on a unit ball times the fixed beta law. Dominated convergence is therefore applicable, including the \(m=0\) case.

For each \(T=t_0\in[0,1]\), the elementary beta-ball integral gives
\[
\int_{\mathbb R^m}
\bigl(1-\|v\|^2-(\lambda/2)t_0\bigr)_+^p\,dv
=\frac{\pi^{m/2}\Gamma(p+1)}{\Gamma(p+m/2+1)}
\bigl(1-(\lambda/2)t_0\bigr)_+^{p+m/2}.
\]
For \(m=0\), this equality means evaluation on the zero-dimensional space. Multiplying the Jacobian, density at zero, and the factor \(\delta^{p+m/2}\sim(2\varepsilon)^\beta\) proves the claimed \(C_{d,r}\mathcal F_{d,r}(\lambda)\), including locally uniform convergence.

**4. The crossover boundary.** Since \(T\) is beta distributed, the integral defining \(\mathcal F\) is continuous, positive and strictly decreasing; dominated convergence gives its value at zero. As \(\lambda\to\infty\), put \(t=(2/\lambda)s\) in that beta integral. The factor \((1-t)^{r/2-1}\to1\) on \(0\le s\le1\), giving
\[
\mathcal F_{d,r}(\lambda)
\sim\sqrt{2/\lambda}\frac{B(1/2,\beta+1)}{B(1/2,r/2)}.
\]
Using \(B(x,y)=\Gamma(x)\Gamma(y)/\Gamma(x+y)\), multiplication by \(C_{d,r}\) simplifies exactly to the coefficient of a fixed-gap \(r\)-fold largest-axis ellipsoid after the formal substitution \(\lambda=\gamma_k/\varepsilon\). This identifies the neighboring power exponents, but is **not** a claim of an unproved joint uniform limit.

**5. Fixed-shape check.** Repeat Step 3 with the actual (fixed) largest-axis multiplicity \(s\), with no varying \(\lambda\)-term. The same beta-ball volume calculation gives the stated \(d-(s+1)/2\) exponent and coefficient. In the fully spherical case the exact law is \(\mathbb P(L>2a(1-\varepsilon))=(2\varepsilon-\varepsilon^2)^p\), agreeing with the formula. This completes the proof.

## Verification
The accompanying `checker.py` uses direct ellipsoid-line quadratic intersection calculations, independently evaluates one-dimensional spheroid integrals, samples limiting beta-ball measures to test general unequal-axis endpoint coefficients, and numerically evaluates the coalescence profile at nonzero \(\lambda\). No Monte Carlo sample is used to justify a limit; the proof above is analytic. Run in a Python environment with NumPy and SciPy using `python checker.py`. Every numerical threshold in the checker is stated there and concerns reproducible finite tests.

## Relationship to prior work
Heinrich (2014) gives **all** chord-power integrals of arbitrary ellipsoids via a spherical integral, and therefore in principle determines their chord-length distributions by their moments. That background is credited and the all-moments formula is not claimed here. The present result evaluates a distinct, nonuniform **joint rare-chord/axis-coalescence limit** and its beta crossover: a moment formula at any fixed shape does not itself state this two-scale asymptotic or its matching coefficient. Hug and Schneider (first public preprint November 26, 2019) study invariant measures of lines and pairs of lines intersecting convex bodies, not the length law of the rarest ellipsoid chords. Kellerer (1984) explicitly studies ellipse and three-dimensional spheroid chord distributions, which are excluded from the dimension-\(d\ge4\) main claim. Van der Jagt, Jongbloed and Vittorietti (2023) prove regularity and propose density approximations for random **hyperplane section volumes**; these are not affine-line chord lengths for \(d\ge4\).

## Limitations
Historical priority is provisional: older stereological and ellipsoid-chord literature could contain an equivalent nonuniform axis-degeneracy asymptotic under different notation. The cited 1977 Suwa paper was inspectable only through an abstract; it concerns random test-line populations of three-dimensional ellipsoids. The theorem assumes positive axes, Euclidean line invariance and a fixed finite dimension. Its asymptotics are locally uniform in finite crossover parameters, **not** in the unbounded-parameter regime. All numerical tests are finite and are not independent certification. The result says nothing about random lines obtained from interior-point pairs or uniform-central-direction sampling.

## References
- D. Hug and R. Schneider, *Integral geometry of pairs of hyperplanes or lines*, first posted arXiv:1911.11659v1 on 2019-11-26; *Archiv der Mathematik* **115** (2020), 339–351. https://arxiv.org/abs/1911.11659
- L. Heinrich, *Lower and Upper Bounds for Chord Power Integrals of Ellipsoids*, *Applied Mathematical Sciences* **8** (2014), 8257–8269, DOI:10.12988/ams.2014.411913. https://www.m-hikari.com/ams/ams-2014/ams-165-168-2014/heinrichAMS165-168-2014.pdf
- A. M. Kellerer, *Chord-length distributions and related quantities for spheroids*, *Radiation Research* **98** (1984), 425–437. https://epub.ub.uni-muenchen.de/8751/1/8751.pdf
- T. van der Jagt, G. Jongbloed and M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, *Image Analysis & Stereology* **42** (2023), 171–184, first public arXiv:2305.02864v1 (2023-05-04). https://arxiv.org/abs/2305.02864
- N. Suwa, *Estimation of the distribution of ellipsoids with random test lines*, *Tohoku Journal of Experimental Medicine* **121** (1977), 365–370. DOI:10.1620/tjem.121.365 (abstract reviewed only).

# Sharp logarithmic endpoint approach of spherical Fourier extension stability in three dimensions

## Finding

Consider the Fourier extension operator on the unit two-sphere with **unnormalized surface measure** \(\sigma\),
\[\widehat{f\sigma}(x)=\int_{\mathbb S^2}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega).\]
For \(3<q<\infty\) use the mixed norm
\[\|F\|_{q,2}=\left(\int_0^\infty\left(\int_{\mathbb S^2}|F(r\theta)|^2\,d\sigma(\theta)\right)^{q/2}r^2\,dr\right)^{1/q};\]
for \(q=\infty\), replace the radial integral by the essential supremum. Let \(P_0\) be the orthogonal projection onto constants. Define \(C_{3,q}\) to be the optimal extension operator norm, and \(\Gamma_{3,q}\) to be the **largest** nonnegative number such that for every \(f\in L^2(\mathbb S^2)\),
\[C_{3,q}^2\|f\|_2^2-\|\widehat{f\sigma}\|_{q,2}^2\ge\Gamma_{3,q}\|f-P_0f\|_2^2.\]

Define \(r_*\) as the unique solution in \((\pi/2,\pi)\) of
\[(r_*^2-2)\sin r_*+2r_*\cos r_*=0,\]
and set
\[v_*:=\frac{\sin r_*-r_*\cos r_*}{r_*^2},\qquad\kappa:=1-\frac2{r_*^2},\qquad C_0:=\frac{6^{3/2}\sqrt\pi}4,\qquad C_1:=r_*^2\sqrt{\frac{2\pi}{\kappa}}.\]
Then as real \(q\to\infty\), the exact sharp stability coefficient satisfies
\[\boxed{\Gamma_{3,q}=16\pi^2\left[1-v_*^2+\frac{(-3+v_*^2)\log q+2\log C_0-2v_*^2\log C_1}{q}+O\!\left(\frac{(\log q)^2}{q^2}\right)\right].}\]
In particular the sharp endpoint coefficient and **sharp logarithmic convergence rate** are
\[\boxed{\Gamma_{3,\infty}=16\pi^2(1-v_*^2),\qquad \lim_{q\to\infty}\frac{q}{\log q}(\Gamma_{3,\infty}-\Gamma_{3,q})=16\pi^2(3-v_*^2)>0.}\]
Numerically, \(r_*\approx2.0815759778181\), \(v_*\approx0.4361818172715\), \(\Gamma_{3,\infty}\approx127.8698717362\), and the coefficient of \((\log q)/q\) in the gap is approximately \(443.6972125711\). The associated sharp **squared extension norm** also satisfies
\[C_{3,q}^2=16\pi^2\left[1+\frac{-3\log q+2\log C_0}{q}+O\!\left(\frac{(\log q)^2}{q^2}\right)\right].\]
This last formula is a companion consequence of the same two-mode analysis, not a separate independent claim.

## Assumptions and scope

All constants use the Fourier transform without \((2\pi)\)-normalizing factors, the actual area measure on \(\mathbb S^2\), radial measure \(r^2\,dr\), and angular \(L^2(d\sigma)\). The result holds for fixed spatial dimension three as the real exponent \(q>3\) tends to infinity. Its exact sharp-coefficient identification uses the finite-exponent modal-ordering theorem and endpoint theorem of Xu [1]; the asymptotic expansion, global profile maximum, Laplace coefficients and logarithmic rate are established below. We do not infer the statement for the unmixed \(L^q(\mathbb R^3)\) norm.

## Proof

**1. Reduce the optimal coefficient to two Bessel moments.** For \(\nu=1/2\), put
\[I_k(q)=\int_0^\infty|r^{-1/2}J_{k+1/2}(r)|^q r^2\,dr.\]
Xu's strict modal ordering and sharp-deficit theorem [1, Theorems 1.2–1.4, Sections 4–5] give for every \(q>3\),
\[C_{3,q}^2=(2\pi)^3I_0(q)^{2/q},\qquad\Gamma_{3,q}=(2\pi)^3\{I_0(q)^{2/q}-I_1(q)^{2/q}\}.\]
The first harmonic realizes equality in the relevant spectral deficit, so there is no loss in passing from the full function space to these two moments. At \(q=\infty\), the same endpoint theorem replaces the two \(L^q\) norms by their suprema. This step is a cited published premise rather than a numerical assumption.

**2. Locate the two absolute maxima exactly.** The elementary half-integer identities are
\[r^{-1/2}J_{1/2}(r)=c\,s(r),\qquad r^{-1/2}J_{3/2}(r)=c\,v(r),\qquad c=\sqrt{\frac2\pi},\]
where \(s(r)=\sin r/r\), \(s(0)=1\), and \(v(r)=(\sin r-r\cos r)/r^2=-s'(r)\), \(v(0)=0\). The unique absolute maximum of \(|s|\) on \([0,\infty)\) occurs at the endpoint \(r=0\), with value one, because \(|\sin r|<r\) for \(r>0\).

Set \(N(r)=(r^2-2)\sin r+2r\cos r\). Direct differentiation gives
\[v'(r)=\frac{N(r)}{r^3},\qquad N'(r)=r^2\cos r.\]
Since \(N(0)=0\), \(N\) increases on \((0,\pi/2)\), then decreases on \((\pi/2,\pi)\), and \(N(\pi)=-2\pi\), its unique positive zero before \(\pi\) lies in \((\pi/2,\pi)\). It is \(r_*\). In fact \(v\) is positive on \((0,\pi]\): \(g(r)=\sin r-r\cos r\) has \(g'(r)=r\sin r>0\) there and \(g(0)=0\). For \(\pi\le r\le4\), \(\cos r<-1/2\) because \(4<4\pi/3\), so \(g(r)>r/2-1>0\). Also \(N'<0\) throughout \((r_*,4)\), since \(4<3\pi/2\). Thus \(v\) increases up to \(r_*\) and decreases, while staying positive, through \(r=4\). For all \(r\ge4\),
\[|v(r)|\le r^{-1}+r^{-2}\le5/16<1/\pi=v(\pi)<v(r_*).\]
This proves that \(r_*\) is the **unique global maximum of \(|v|\)**. From the spherical-Bessel equation,
\[v''(r)+\frac2r v'(r)+\left(1-\frac2{r^2}\right)v(r)=0,\]
so at the peak \(v''(r_*)=-\kappa v_*\) with \(\kappa=1-2/r_*^2>0\). Consequently
\[\log|v(r)|=\log v_*-\frac\kappa2(r-r_*)^2+O((r-r_*)^3).\]

**3. Compute the weighted Laplace integrals.** At the endpoint maximum,
\[\log s(r)=-r^2/6+O(r^4)\qquad(r\downarrow0).\]
The change of variable \(r=u/\sqrt q\) and Gaussian integration give
\[I_0(q)=c^q q^{-3/2}\left(\int_0^\infty u^2e^{-u^2/6}\,du\right)(1+O(q^{-1}))=c^q C_0q^{-3/2}(1+O(q^{-1})).\]
At the unique interior peak of the first nonconstant mode, ordinary one-dimensional Laplace asymptotics give
\[I_1(q)=(cv_*)^q r_*^2\sqrt{\frac{2\pi}{\kappa q}}\,(1+O(q^{-1}))=(cv_*)^q C_1q^{-1/2}(1+O(q^{-1})).\]
Both error estimates are valid for real \(q\to\infty\). To justify localization globally, choose a fixed compact neighborhood of each maximizing point. Strict uniqueness yields a strictly smaller amplitude on the rest of a fixed finite interval. At large radius \(|s(r)|\le r^{-1}\) and \(|v(r)|\le r^{-1}+r^{-2}\), and the \(r^2\,dr\) tail is exponentially negligible for large \(q\). Analytic Taylor expansions at the two nondegenerate peaks give relative remainder \(O(q^{-1})\), including at the endpoint by the substitution \(r=u/\sqrt q\). Thus no unexamined secondary oscillatory maximum contributes at the stated order.

**4. Recover the sharp gap and its sign.** Taking \(2/q\)-powers, using \(\log(1+O(q^{-1}))=O(q^{-1})\),
\[I_0(q)^{2/q}=c^2\left[1+\frac{-3\log q+2\log C_0}{q}+O\!\left(\frac{(\log q)^2}{q^2}\right)\right],\]
\[I_1(q)^{2/q}=c^2v_*^2\left[1+\frac{-\log q+2\log C_1}{q}+O\!\left(\frac{(\log q)^2}{q^2}\right)\right].\]
Substitution into the exact sharp coefficient and \((2\pi)^3c^2=16\pi^2\) gives the boxed two-term expansion. The endpoint supreme norms are \(c\) and \(cv_*\), giving \(\Gamma_{3,\infty}\) exactly. The leading logarithmic loss is \(16\pi^2(3-v_*^2)(\log q)/q\), strictly positive since \(0<v_*<1\). This completes the proof.

## Verification

Run `python3 verify_spherical_gap.py` with standard Python; SciPy, if installed, additionally tests finite-exponent quadrature. The reported numerical endpoint is \(127.8698717362\) and the logarithmic loss coefficient is \(443.6972125711\). The checker tests normalizations, algebraic critical-point identities, and numerical consistency at finite exponents. The proof of all-\(q\) sharpness and the asymptotic remainder is the written analytic argument plus the identified published modal theorem, not the checker.

## Relationship to prior work

Carneiro, Oliveira e Silva and Sousa [2] derived the weighted Bessel reduction and endpoint extremal ordering; Ciccone and Sousa [3] studied additional harmonic-mode hierarchies and maximizing ranges. Xu [1] identified the exact optimal **finite**-exponent and endpoint stability coefficients in terms of the top two Bessel moments. The present claim concerns their hitherto unquantified **asymptotic transition**, including the exact positive logarithmic approach coefficient and the entire order-\(q^{-1}\) term. It uses the source's sharpness theorem; the finite-exponent formula and degree-one extremizer are not claimed as new. The mechanism is that the constant spherical mode concentrates at the radial endpoint with volume factor \(q^{-3/2}\), whereas the first mode concentrates at an interior radial point with factor \(q^{-1/2}\). This geometric mismatch creates the precise logarithmic rate.

## Limitations

The asymptotic is for dimension three, the radial--angular mixed norm and the indicated Fourier/surface normalizations. It is not a finite-\(q\) closed formula and gives no threshold or remainder uniform in spatial dimension. The argument relies on the strict modal ordering [1] rather than reproving it. Although a targeted comparison of relevant accessible literature found no equivalent sharp endpoint-rate statement, generic Laplace methods are classical and an implicit historical treatment cannot be excluded. No independent mathematical audit has been performed.

## References

[1] Zewei Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648 (first posted 2026-10-14), Theorems 1.2--1.4, Sections 4--5. https://arxiv.org/abs/2610.19648

[2] Emanuel Carneiro, Diogo Oliveira e Silva and Mateus Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365 (first posted 2017-10-28), Advances in Mathematics 341 (2019), 583--608, Sections 1--2 and 4. https://arxiv.org/abs/1710.10365

[3] Valentina Ciccone and Mateus Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, Journal of Fourier Analysis and Applications 31 (2025), article 70; DOI: 10.1007/s00041-025-10201-7, especially Section 2. https://doi.org/10.1007/s00041-025-10201-7

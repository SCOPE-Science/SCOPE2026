# Exact Fourier nodal-ring folds and pairwise threshold reversals for a Gaussian–circle mixture

## Finding
Let \(\sigma\) be normalized arclength probability on the unit circle of \(\mathbb R^2\), and \(\gamma_a\) the centered Gaussian probability with covariance \(2aI_2\), for \(a>0\). For \(0<t<1\), set \(\mu_{a,t}=(1-t)\gamma_a+t\sigma\). Use \(\widehat\mu(\xi)=\int e^{-2\pi i\xi\cdot x}\,d\mu(x)\) and angular Fourier radius \(r=2\pi|\xi|\). Then
\[
\widehat\mu_{a,t}(\xi)=(1-t)e^{-ar^2}+tJ_0(r).
\]
Write the positive zeros of \(J_0\) as \(j_{0,m}\), increasing in \(m\ge1\). Define \(I_k=(j_{0,2k-1},j_{0,2k})\), where \(J_0<0\), and \(G_a(r)=e^{ar^2}J_0(r)\). Each \(I_k\) contains a unique point \(\rho_k(a)\) at which \(G_a\) attains its strict nondegenerate minimum. It is characterized by
\[
J_1(\rho_k)=2a\rho_kJ_0(\rho_k),\qquad \Lambda_k(a)=-e^{a\rho_k^2}J_0(\rho_k)>0.
\]
Let \(\lambda=(1-t)/t\). The **entire real Fourier zero set** is a union of concentric circles, with the following complete multiplicity rule in every negative Bessel lobe:

* For \(\lambda<\Lambda_k(a)\), there are exactly two distinct radial zeros in \(I_k\), both simple in the radial variable.
* For \(\lambda=\Lambda_k(a)\), there is exactly one radial zero, at \(r=\rho_k(a)\), of exact radial Taylor order two.
* For \(\lambda>\Lambda_k(a)\), there is no radial zero in \(I_k\).

There are no other real zeros or zeros of higher radial order. For each fixed \(a>0\), \(\Lambda_k(a)\to\infty\), so **every** nontrivial circle component \(t>0\) produces infinitely many zero circles. If \(N_{a,t}(R)\) counts *distinct positive radial zeros* \(r\le R\), then
\[
N_{a,t}(R)=\frac R\pi+O_{a,t}(1)\quad(R\to\infty).
\]

The fold thresholds have a nontrivial *ordering-reversal law*: for every pair \(1\le k<\ell\) there exists exactly one \(a_{k\ell}>0\) such that
\[
\Lambda_\ell(a)<\Lambda_k(a)\ (0<a<a_{k\ell}),\quad
\Lambda_\ell(a_{k\ell})=\Lambda_k(a_{k\ell}),\quad
\Lambda_\ell(a)>\Lambda_k(a)\ (a>a_{k\ell}).
\]
Two different lobes can therefore undergo simultaneous folds at isolated Gaussian variances, but each individual fold remains nondegenerate. For fixed \(a>0\), writing \(s_k=j_{0,2k}\), the sharp large-index laws are
\[
\rho_k(a)=s_k-\frac1{2as_k}+O_a(s_k^{-3}),\quad
\Lambda_k(a)\sim\frac{e^{as_k^2-1}}{a\sqrt{2\pi}\,s_k^{3/2}},\quad
\frac1{1+\Lambda_k(a)}\sim ae\sqrt{2\pi}\,s_k^{3/2}e^{-as_k^2}.
\]
Finally, the first positive radial zero \(r_*(a,t)\) for \(t\downarrow0\) satisfies
\[
r_*(a,t)\sim\sqrt{\frac{\log(1/t)}a}.
\]

## Assumptions and scope
Here \(a\) is a strictly positive Gaussian variance parameter, \(t\) is a strictly interior mixture mass, \(J_0,J_1\) are real Bessel functions of the first kind, and each radial root is counted without its continuous angular multiplicity. The circle radius in the Fourier variable \(\xi\) equals \(r/(2\pi)\). The theorem concerns **real Fourier frequencies only**, not complex zeros of the entire characteristic function. A double radial root yields a geometrically smooth zero circle whose radial normal derivative vanishes; this is not a nodal-curve crossing.

## Proof
**1. Exact transform.** The Gaussian density corresponding to covariance \(2aI_2\) has characteristic function \(\exp(-a|\zeta|^2)\) in angular frequency \(\zeta\). Integrating \(e^{-ir\cos\theta}\) against normalized circle arclength gives \(J_0(r)\). Substituting \(\zeta=2\pi\xi\) proves the stated mixture formula. Multiplication by the everywhere-positive quantity \(e^{ar^2}/t\) reduces zeros, with all Taylor orders unchanged, to
\[
\lambda+G_a(r)=0,\qquad \lambda=(1-t)/t>0.
\]
Since \(G_a(r)\ge0\) outside the negative lobes, no other roots are possible. At \(r=0\) the Fourier transform equals one. At any Bessel zero, the Gaussian term is strictly positive, so no Fourier zero lies on a lobe boundary.

**2. Uniqueness and curvature of every lobe minimum.** In \(I_k\) define \(u_a(r)=\log(-G_a(r))=ar^2+\log(-J_0(r))\). Because the positive Bessel zeros are simple, \(u_a\to-\infty\) at both lobe endpoints, hence it has an interior maximum. Its stationary points obey
\[
0=u'_a(r)=2ar+\frac{J'_0(r)}{J_0(r)}
\quad\Longleftrightarrow\quad J_1(r)=2arJ_0(r).
\]
Using Bessel's differential equation \(J''_0+J'_0/r+J_0=0\), substitution at any stationary point gives the **exact** second derivative
\[
u_a''(r)=4a-1-4a^2r^2
=-(2ar-1/r)^2-1+1/r^2<0,
\]
since \(r>j_{0,1}>1\). Thus **every** stationary point is a strict local maximum. There cannot be two: between two strict local maxima a differentiable function has a stationary local minimum, contradicting the strict-negative-second-derivative identity. Therefore the maximum is unique. It is nondegenerate, so \(G_a\) has exactly one nondegenerate minimum. Comparison with its zero values at the two endpoints yields precisely the zero-count and multiplicity trichotomy. At a threshold, \(G_a''(\rho_k)=G_a(\rho_k)u_a''(\rho_k)>0\). More precisely, for \(\delta=\Lambda_k-\lambda\downarrow0\), the two radii satisfy
\[
r_{k,\pm}=\rho_k\pm\sqrt{2\delta/G_a''(\rho_k)}+O_{a,k}(\delta).
\]

**3. Pairwise ordering reversal.** At \(a=0\), the lobe maxima of \(-J_0\) are strictly decreasing in \(k\). Indeed \(E(r)=J_0(r)^2+J'_0(r)^2\) obeys
\[
E'(r)=2J'_0(r)[J_0(r)+J_0''(r)]=-\frac{2J'_0(r)^2}{r}\le0.
\]
The inequality is strict upon integration over any nonempty interval because \(J'_0\) is not identically zero. At the sole extrema of \(-J_0\) in consecutive negative lobes, \(J'_0=0\), so \(\Lambda_\ell(0)<\Lambda_k(0)\) whenever \(\ell>k\). The implicit-function theorem applies to every nondegenerate minimum; differentiating at that critical point by the envelope theorem gives
\[
\frac{d}{da}\log\Lambda_k(a)=\rho_k(a)^2.
\]
Since the lobes are ordered and disjoint, \(\rho_\ell(a)>\rho_k(a)\); thus \(a\mapsto\log(\Lambda_\ell(a)/\Lambda_k(a))\) is strictly increasing. For any fixed \(x\in I_\ell\) with \(x>j_{0,2k}\), one has \(\Lambda_\ell(a)\ge e^{ax^2}|J_0(x)|\), while \(\Lambda_k(a)\le e^{a j_{0,2k}^2}\) because \(|J_0|\le1\). The ratio tends to infinity as \(a\to\infty\). Continuity and strict monotonicity give exactly one crossover for every pair.

**4. Sharp high-lobe fold asymptotics.** Put \(s=s_k=j_{0,2k}\), the right endpoint of the negative lobe, and \(\delta=s-\rho_k\). For each fixed \(a>0\), the exponential weight forces \(\rho_k\) toward \(s_k\) as \(k\to\infty\): the familiar uniform large-argument Bessel cosine asymptotic bounds \(|J_0(r)|\) polynomially, while \(e^{ar^2}\) favors larger \(r\); comparison against points a fixed small distance from the endpoint gives \(\delta\to0\). The zero and derivative asymptotics yield
\[
J_0(s-\delta)=-J_0'(s)\delta\bigl(1+O_a(s^{-2})\bigr),\quad
J_0'(s)=\sqrt{\frac2{\pi s}}\bigl(1+O(s^{-1})\bigr),
\]
with positive derivative at the right endpoint. More accurately, the Bessel equation at a zero, together with the critical equation \(J'_0(\rho)/J_0(\rho)=-2a\rho\), gives
\[
\delta=\frac1{2as}+O_a(s^{-3}).
\]
Consequently \(a\rho_k^2=as_k^2-1+O_a(s_k^{-2})\). Substitution in \(\Lambda_k=e^{a\rho_k^2}|J_0(\rho_k)|\) proves the announced exact leading constant and the reciprocal critical-mixture-mass asymptotic. In particular \(\Lambda_k\to\infty\), establishing infinitely many circles for each \(t>0\).

**5. Zero counting and first-root escape.** Standard Bessel zero asymptotics give \(j_{0,m}=(m-1/4)\pi+O(m^{-1})\). Beyond a threshold depending on \(a,t\), every negative lobe contributes exactly two simple roots; therefore \(N_{a,t}(R)=R/\pi+O_{a,t}(1)\). If \(r\) is a zero, then \(\lambda=e^{ar^2}|J_0(r)|\le e^{ar^2}\), so \(r\ge\sqrt{\log\lambda/a}\). Conversely, choose a negative Bessel antinode at distance \(O(1)\) to the right of \(\sqrt{(1+\varepsilon)\log\lambda/a}\). The Bessel asymptotic ensures its amplitude is at least a constant times \(r^{-1/2}\), hence \(e^{ar^2}|J_0(r)|>\lambda\) for all sufficiently large \(\lambda\), while at adjacent lobe boundaries \(G_a=0\). Thus a root occurs by that radius, up to an additive constant. Taking \(\lambda=(1-t)/t\to\infty\), then \(\varepsilon\downarrow0\), proves the first-root equivalent.

## Verification
The standalone `verify_circle.py` evaluates the defining Bessel quantities with SciPy, checks one nondegenerate fold in each of 45 sampled lobes, demonstrates root pairs on each side of a fold, and locates three pairwise threshold reversals. The executable's output is embedded as `verification_output.txt`. These are finite numerical crosschecks; **all infinite and asymptotic assertions are proved analytically above**, conditional only on the cited standard Bessel zero/asymptotic facts. Sample pairwise Gaussian-variance crossings are \(a_{1,2}\approx0.005325096171630\), \(a_{1,3}\approx0.002781989290075\), and \(a_{2,3}\approx0.001425119997171\); decimal approximations are not part of the exact existence/uniqueness proof.

## Relationship to prior work
The exact characteristic-function formulas for the uniform circle, Gaussian, and related radial distributions are classical. González Vieli (2011, first published online December 8, 2011) studies when spherical restriction of the Fourier transform determines a measure supported on a sphere. Yin and Dong (2021 preprint; inspected revised full text) derive Bessel characteristic-function representations for elliptical families and several location/scale mixtures. Neither inspected text gives the above Gaussian–surface-circle *convex mixture* zero-circle fold census, pairwise fold threshold-order reversal, or sharp outer-lobe exponential fold asymptotic. The Bessel-zero facts and large-radius expansions in NIST DLMF supply standard premises, not the mixed-measure phase diagram. The possibility of an older equivalent result in unindexed diffraction, statistics, or radial positive-definiteness literature remains a genuine priority risk.

## Limitations
The theorem is restricted to the precise planar mixture of one centered isotropic Gaussian and unit-circle arclength; it does not classify arbitrary radial mixtures, higher-dimensional spherical mixtures, complex-frequency zeros, or eigenfunctions associated with the circles. The simultaneous-crossing statement is **pairwise**; no exclusion of three or more coincident thresholds at special parameter values is claimed. The Gaussian variance parameter \(a\) is fixed in the sharp \(k\to\infty\) asymptotics, so no unproved uniform-in-\(a\) extension is asserted. Priority is assessed against accessible primary sources and research records, not independently certified.

## References
1. F. J. González Vieli, "A uniqueness result for the Fourier transform of measures on the sphere", *Bull. Aust. Math. Soc.* 86 (2012), 78–82; published online 2011-12-08; doi:10.1017/S0004972711002942. Primary MSC 42B10.
2. C. Yin and H. Dong, "The Bessel function expression of characteristic function", arXiv:2112.06472 (first publicly posted 2021; revised full text inspected, 2023).
3. NIST Digital Library of Mathematical Functions, §10.21 (Bessel zeros and separation), https://dlmf.nist.gov/10.21.
4. NIST Digital Library of Mathematical Functions, §10.17 (large-argument Bessel expansions), https://dlmf.nist.gov/10.17.

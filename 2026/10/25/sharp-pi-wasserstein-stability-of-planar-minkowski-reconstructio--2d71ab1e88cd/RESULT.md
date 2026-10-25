# Sharp \(\pi\) Wasserstein stability of planar Minkowski reconstruction

## Finding
Let \(\mu,\nu\) be balanced Borel probability measures on the unit circle, neither supported by a single antipodal pair. Their Steiner-centered planar Minkowski bodies \(K_\mu,K_\nu\) are defined by \(S_{K_\mu}=2\pi\mu\) and \(S_{K_\nu}=2\pi\nu\); each has perimeter \(2\pi\). Write \(W_1\) for Wasserstein transport using **geodesic arc-length distance** on the circle. Then the optimal universal constant in
\[
d_H(K_\mu,K_\nu)\le C W_1(\mu,\nu)
\]
is exactly \(C=\pi\). Furthermore the same best constant \(\pi\) holds if the measures are restricted to **strictly positive smooth probability densities**, corresponding to smooth strictly convex bodies with positive curvature radius.

More explicitly, for every \(0<\varepsilon<\pi/2\) put \(c=\cos\varepsilon\), let \(\delta_\theta\) be the point mass at angle \(\theta\), and define the balanced probability measures
\[
\mu_\varepsilon=\frac{\delta_{\varepsilon}+\delta_{-\varepsilon}}{2(1+c)}+\frac{c}{1+c}\delta_\pi,
\qquad \nu=\frac12(\delta_0+\delta_\pi).
\]
Although \(\nu\) is degenerate, the pairs \(\mu_{\varepsilon,a}=(1-a)\mu_\varepsilon+a\sigma\), \(\nu_a=(1-a)\nu+a\sigma\), where \(0<a<1\) and \(\sigma\) is uniform circle probability, are admissible. In direction \(0\), the magnitude of their support-function difference is
\[
(1-a)\frac{(\pi-\varepsilon)\sin\varepsilon}{1+\cos\varepsilon},
\]
and their geodesic Wasserstein distance is
\[
(1-a)\left[\frac{\varepsilon}{2}+\frac{1-\cos\varepsilon}{2(1+\cos\varepsilon)}(\pi-\varepsilon)\right].
\]
Their quotient tends to \(\pi\). Circular convolution with a positive smooth approximate identity gives the claimed smooth positive-density sharpness.

## Assumptions and scope
The circle has circumference \(2\pi\). A probability measure \(\lambda\) is balanced when \(\int_{S^1}u\,d\lambda(u)=0\); it is nondegenerate when its support is not contained in an antipodal pair. The Minkowski surface-area measure is normalized as \(S_{K_\lambda}=2\pi\lambda\), and the Steiner point is the origin. The Hausdorff distance between two convex bodies equals the uniform distance between their support functions. \(W_1\) uses geodesic rather than chordal distance. No quantitative separation from antipodal concentration is assumed.

## Proof
**1. Universal upper bound.** In Section 6.1, An [1] proves that the Steiner-centered inverse \(D^2+1\) on the circle has the even Green kernel
\[
G(t)=-\frac{\cos t}{4\pi}+\left(\frac12-\frac{|t|}{2\pi}\right)\sin|t|,\qquad -\pi\le t\le\pi,
\]
extended periodically, with geodesic Lipschitz seminorm \(1/2\). For balanced measures the first-harmonic correction vanishes, giving
\[
h_{K_\mu}(\theta)-h_{K_\nu}(\theta)=2\pi\int_{S^1}G(\theta-\phi)\,d(\mu-\nu)(\phi).
\]
Kantorovich--Rubinstein duality then gives \(\|h_{K_\mu}-h_{K_\nu}\|_\infty\le 2\pi(1/2)W_1=\pi W_1\). This step is a cited published theorem; the new result establishes that its constant cannot improve.

**2. Balanced near-antipodal family.** Let \(c=\cos\varepsilon\) and \(b=(1-c)/(2(1+c))\). The total mass of \(\mu_\varepsilon\) is one, while its first moment along the horizontal axis is \(c/(1+c)-c/(1+c)=0\); its vertical moment vanishes by reflection. The measure \(\nu\) is balanced as well. Their signed difference is
\[
\mu_\varepsilon-\nu=\frac{\delta_{\varepsilon}+\delta_{-\varepsilon}}{2(1+c)}-\frac12\delta_0-b\delta_\pi.
\]
For any fixed \(a\in(0,1)\), adding \(a\sigma\) to each measure makes both nondegenerate, with unchanged balance. By Kantorovich--Rubinstein duality and linearity of the signed difference, \(W_1(\mu_{\varepsilon,a},\nu_a)=(1-a)W_1(\mu_\varepsilon,\nu)\), even though the latter \(\nu\) is degenerate.

**3. Exact transport cost.** In transporting \(\mu_\varepsilon\) to \(\nu\), retain their common mass at \(\pi\), send total mass \(1/2\) from \(\pm\varepsilon\) to \(0\), and send the remaining mass \(b\) from \(\pm\varepsilon\) to \(\pi\). This has cost
\[
L_\varepsilon=\frac{\varepsilon}{2}+b(\pi-\varepsilon).
\]
It is optimal: on the four-point set prescribe \(f(0)=0\), \(f(\varepsilon)=f(-\varepsilon)=\varepsilon\), \(f(\pi)=2\varepsilon-\pi\). These values are geodesically 1-Lipschitz for \(0<\varepsilon<\pi/2\), so they extend to a globally 1-Lipschitz circle function. Its integral against \(\mu_\varepsilon-\nu\) equals \(L_\varepsilon\), certifying the lower bound by transport duality. Therefore \(W_1=L_\varepsilon\).

**4. Exact support gap.** Evaluate the displayed Green formula at \(\theta=0\). Since \(G(0)=-1/(4\pi)\), \(G(\pi)=1/(4\pi)\), and
\[
G(\varepsilon)=-\frac{c}{4\pi}+\frac{\pi-\varepsilon}{2\pi}\sin\varepsilon,
\]
the cosine contributions cancel, leaving
\[
2\pi\int G(-\phi)\,d(\mu_\varepsilon-\nu)(\phi)
=\frac{(\pi-\varepsilon)\sin\varepsilon}{1+c}=:H_\varepsilon>0.
\]
The corresponding Hausdorff distance for the admissible smoothed-by-uniform pairs is at least \((1-a)H_\varepsilon\). As \(\varepsilon\downarrow0\),
\[
H_\varepsilon=\frac\pi2\varepsilon+O(\varepsilon^2),\qquad
L_\varepsilon=\frac12\varepsilon+O(\varepsilon^2),
\]
so \(\liminf d_H(K_{\mu_{\varepsilon,a}},K_{\nu_a})/W_1(\mu_{\varepsilon,a},\nu_a)\ge\pi\). The universal upper bound forces equality of the optimal constant with \(\pi\).

**5. Strictly positive smooth densities.** Fix \(0<a<1\). Convolve both \(\mu_{\varepsilon,a}\) and \(\nu_a\) angularly with a strictly positive even smooth probability approximate identity (for example, the circular heat kernel as its time decreases to zero). Convolution preserves total mass and vanishing first moment, and the uniform component guarantees densities at least \(a/(2\pi)>0\). The reconstructed support functions are smooth and their curvature-radius functions \(h+h''\) are strictly positive, hence the corresponding bodies are smooth and strictly convex. For each fixed \(\varepsilon>0\), the convolved measures converge in geodesic \(W_1\) to the original pair; the Green-kernel support functions converge uniformly because \(G\) is continuous. Choose convolution time tending to zero sufficiently rapidly with \(\varepsilon\). Their reconstruction-to-transport ratio still tends to \(\pi\). This completes the proof.

## Verification
The standalone finite checks in `verify.py` evaluate the Green kernel and transport costs for several small angles, check probability and first-moment identities, test a geodesic 1-Lipschitz transport potential, and compare the derived exact support gap with its kernel evaluation. The calculations converge to the sharp coefficient but the infinite theorem follows from the preceding analytic argument and cited upper bound.

## Relationship to prior work
An [1, Proposition 6.1] proves the upper bound with coefficient \(\pi\) and [1, Proposition 6.3] proves only that the **exponent** of \(W_1\) is optimal, using a Fourier-mode pair with ratio \(\pi/3\). Immediately after Proposition 6.3, [1] states that its optimal Lipschitz constant is not determined. The present construction proves optimality of the *numerical coefficient* and shows that the restriction to positive smooth densities does not reduce it.

Böröczky, Machado and Ramos [2] study quantitative Minkowski reconstruction using dual-convex discrepancy, an optimized translation, and dispersion conditions. Those results neither give this sharp universal circle-geodesic coefficient nor imply the fixed-Steiner-normalization near-antipodal extremizing construction. Classical Minkowski existence and uniqueness [3] are used only for defining the reconstructed bodies, not for the new sharpness argument.

## Limitations
This is a planar result with perimeter \(2\pi\), Steiner centering, and **geodesic** transport cost. Other center conventions, chordal transport, ambient dimensions at least three, or bounds under fixed nondegeneracy parameters are not covered. The supremal constant is shown to be approached; attainment by a distinct admissible pair is not claimed.

## References
[1] C. An, *Gauss--Chebyshev Quadrature, S1-Designs, and the Planar Minkowski Inverse Problem: A One-Dimensional Model for Design-Induced Convex Geometry*, arXiv:2610.11814, first version 8 October 2026, especially §§6.1, 6.3. https://arxiv.org/abs/2610.11814

[2] K. Böröczky, J. M. Machado and J. P. G. Ramos, *Quantitative Stability for Minkowski's problem*, arXiv:2603.17726, first version 18 March 2026, especially §1 and §3. https://arxiv.org/abs/2603.17726

[3] R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, second expanded edition, Cambridge University Press, 2014, cited for the classical planar Minkowski existence theorem.

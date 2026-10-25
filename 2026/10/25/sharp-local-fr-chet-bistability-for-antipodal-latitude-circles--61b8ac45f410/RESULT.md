# Sharp local Fréchet bistability for antipodal latitude circles

## Finding

On the unit round two-sphere, fix \(0<h<1\), and give equal probability to the two circles of latitude with Cartesian heights \(h\) and \(-h\), each uniformly by arclength. Let \(F_h(x)\) be the mean squared intrinsic spherical distance from \(x\) to this measure. Define \(h_{\rm ax}\) as the unique root in \((0,1)\) of
\[
\frac{h\arcsin h}{\sqrt{1-h^2}}=1.
\]
Then the two poles are strict isolated local minima of \(F_h\) for \(0<h<h_{\rm ax}\), and are strict local maxima when \(h_{\rm ax}<h<1\). The equator is a transversely strict local-minimum circle (a Morse–Bott minimum manifold) for \(e^{-1}<h<1\); for \(0<h<e^{-1}\) it has negative normal second variation and therefore is not a local-minimum manifold. No classification is asserted at either zero-Hessian boundary.

In particular the poles and the equator coexist as **distinct locally minimizing components** throughout the exact nonempty interval
\[
e^{-1}<h<h_{\rm ax},\qquad h_{\rm ax}=0.75806016669947\ldots.
\]
Their energies are explicitly
\[
F_h(\pm e_3)=\frac{\pi^2}{4}+\arcsin^2h,\qquad
F_h(x)=\frac{\pi^2}{4}+\frac12\operatorname{Li}_2(1-h^2)
\quad (x_3=0),
\]
where \(\operatorname{Li}_2(z)=\sum_{j\ge1}z^j/j^2\) for \(0\le z<1\). Within the coexistence interval, these two *particular local-minimum components* have equal energy at a unique height \(h_*=0.59251250331177\ldots\), characterized by
\[
\frac12\operatorname{Li}_2(1-h_*^2)=\arcsin^2h_*.
\]
The pole energy is smaller for \(h<h_*\) and the equator energy is smaller for \(h>h_*\). This is a comparison of those stationary families only; it does **not** assert that they exhaust all global minima.

## Assumptions and scope

The domain is the standard unit \(S^2\subset\mathbb R^3\) with great-circle metric \(d(x,v)=\arccos(x\cdot v)\in[0,\pi]\). The measure \(\mu_h\) is the average of the arclength-uniform probabilities on the horizontal circles \(v_3=\pm h\); both have positive radius \(r=\sqrt{1-h^2}\). Define \(F_h(x)=\int d(x,v)^2\,d\mu_h(v)\). All local extrema are in the spherical Riemannian topology. “Strict” at a pole means positive/negative definite spherical Hessian; “transversely strict” at the equator refers only to the normal direction to its rotational orbit. The endpoints \(h=0,1\) are excluded. The result does not quantify sample Fréchet means or identify all critical latitudes.

## Proof

**Reduction to a one-dimensional symmetric potential.** Parametrize one circle by \(v_\phi=(r\cos\phi,r\sin\phi,h)\). The other is its antipodal image, after shifting \(\phi\) by \(\pi\). The identity
\[
\frac{\arccos(q)^2+\arccos(-q)^2}{2}=\frac{\pi^2}{4}+\arcsin^2q
\]
shows, writing \(t=x_3\in[-1,1]\) and rotating around the vertical axis, that
\[
F_h(t)=\frac{\pi^2}{4}+
\frac1{2\pi}\int_0^{2\pi}
 f\!\left(ht+r\sqrt{1-t^2}\cos\phi\right)\,d\phi,
\qquad f(q)=\arcsin^2q.
\tag{1}
\]
For every \(0<h<1\), the integrand is smooth in a neighborhood of \(t=0\) and in the appropriate geodesic coordinate near either pole, because the dot products stay away from \(\pm1\). Thus the Taylor expansions below are legitimate. Symmetry makes the first derivatives vanish.

**Equatorial value.** The elementary analytic expansion
\[
f(z)=\frac12\sum_{j=1}^\infty
\frac{4^j z^{2j}}{j^2\binom{2j}{j}},\qquad |z|<1,
\tag{2}
\]
can be verified by differentiating twice and checking \(f(0)=f'(0)=0\). Since the circular average of \(\cos^{2j}\phi\) is \(\binom{2j}{j}/4^j\), the function
\[
G(r)=\frac1{2\pi}\int_0^{2\pi}f(r\cos\phi)\,d\phi
=\frac12\operatorname{Li}_2(r^2).
\tag{3}
\]
In particular \(F_h(0)=\pi^2/4+G(r)\), while \(F_h(1)=\pi^2/4+f(h)\).

**Exact equatorial normal Hessian.** Expand equation (1) for small axial coordinate \(t\). The coefficient of \(t^2\) is
\[
C_{\rm eq}(h)=\frac{h^2}{2}
\langle f''(r\cos\phi)\rangle
-\frac r2\langle \cos\phi\,f'(r\cos\phi)\rangle,
\tag{4}
\]
where brackets denote circular average. Periodic integration by parts of \(\sin\phi f'(r\cos\phi)\) gives
\[
\langle f''(r\cos\phi)\rangle=G''(r)+\frac{G'(r)}r.
\tag{5}
\]
From (3), \(G'(r)=-\log(1-r^2)/r\), and
\(G''(r)=2/(1-r^2)+\log(1-r^2)/r^2\). Inserting these into (4), using \(h^2=1-r^2\), yields the **exact** expansion
\[
F_h(t)=F_h(0)+(1+\log h)t^2+O_h(t^4).
\tag{6}
\]
As the energy is constant in longitude, this proves the transverse positive-Hessian criterion \(h>e^{-1}\) and the negative-Hessian criterion \(h<e^{-1}\).

**Exact polar Hessian.** For a geodesic angle \(\theta\) from the north pole, equation (1) has argument
\(h\cos\theta+r\sin\theta\cos\phi\). Taylor expansion and circular averaging give
\[
F_h(\cos\theta)=F_h(1)+
\left(\frac{r^2}{4}f''(h)-\frac h2f'(h)\right)\theta^2+O_h(\theta^4).
\tag{7}
\]
Using \(f'(h)=2\arcsin(h)/r\) and
\(f''(h)=2/r^2+2h\arcsin(h)/r^3\), (7) becomes
\[
F_h(\cos\theta)=F_h(1)+
\frac12\left(1-\frac{h\arcsin h}{\sqrt{1-h^2}}\right)\theta^2+O_h(\theta^4).
\tag{8}
\]
The function \(h\arcsin(h)/\sqrt{1-h^2}\) increases strictly from zero to infinity on \((0,1)\), proving that \(h_{\rm ax}\) exists uniquely and giving both polar classifications. Antipodal symmetry gives the south-pole classification.

**A unique crossover strictly inside the coexistence interval.** Set
\[
\Delta(h)=F_h(0)-F_h(1)
=\frac12\operatorname{Li}_2(1-h^2)-\arcsin^2h.
\]
Direct differentiation yields
\[
\Delta'(h)=\frac{2h\log h}{1-h^2}
-\frac{2\arcsin h}{\sqrt{1-h^2}}<0.
\tag{9}
\]
For \(h=2/5\), the bound \(\operatorname{Li}_2(z)>z\), together with \(\arcsin(2/5)<\pi/6\), implies \(\Delta(2/5)>0\). For \(h=7/10\), \(\operatorname{Li}_2(z)\le-\log(1-z)\), while \(\arcsin h\ge h\), gives \(\Delta(7/10)<0\). Moreover \(e^{-1}<2/5\), and \(h_{\rm ax}>7/10\), since \(\arcsin(7/10)<\pi/4\) and hence \((7/10)\arcsin(7/10)/\sqrt{51/100}<1\). Therefore the unique zero of \(\Delta\) lies in \((2/5,7/10)\subset(e^{-1},h_{\rm ax})\). Monotonicity proves the sign comparison. Continuity plus the simultaneous local-minimum conditions also implies an energy barrier on any meridian connecting these components (an intervening stationary level at or above the larger local-minimum energy). This completes the stated local theorem.

## Verification

The accompanying `verify.py` uses only the Python standard library. Running `python3 verify.py` checks the exact equatorial dilogarithm identity against a periodic 16,384-node quadrature, checks the pole identity, compares both Taylor coefficients against finite differences for eleven heights, and checks the transition and crossover brackets. The observed output is `PASS 48 numerical comparisons and transition checks` with thresholds \(0.367879441171442\), \(0.758060166699473\), and \(0.592512503311775\). These are diagnostics, not a substitute for equations (1)–(9), which establish the continuum theorem.

## Relationship to prior work

Hotz–Huckemann study intrinsic Fréchet means on the **one-dimensional circle**, including the effects of antipodal mass and local nonuniqueness; those results do not classify latitude-ring measures on the ambient two-sphere. Afsari–Tron–Vidal establish convergence conditions for Riemannian center-of-mass algorithms, notably under geodesic-ball concentration hypotheses, rather than these broad antipodal supports. Tran develops general derivative tensors for **absolutely continuous** rotationally symmetric measures on spheres, and studies a two-region diffuse example; the present measure is concentrated on two curves. The elementary curvature mechanism is related, but the inspected results do not state the exact \(e^{-1}\) equatorial threshold, the second polar threshold, or the dilogarithmic energy crossover for the specified singular family. Related general results may facilitate independent rederivation; no priority beyond the documented comparisons is claimed.

## Limitations

This is a local-stability and two-orbit energy-comparison theorem, **not** a classification of global Fréchet means or all stationary latitudes. The two zero-Hessian boundary heights are not classified by quartic terms. The measure is singular with respect to spherical area. The result gives no finite-sample inference theorem. Historical-priority verification outside the inspected primary literature and published record search remains open.

## References

1. Thomas Hotz and Stephan Huckemann, *Intrinsic Means on the Circle: Uniqueness, Locus and Asymptotics*, arXiv:1108.2141 (first public version 2011-08-10), https://arxiv.org/abs/1108.2141 .
2. Bijan Afsari, Roberto Tron, and René Vidal, *On The Convergence of Gradient Descent for Finding the Riemannian Center of Mass*, arXiv:1201.0925 (first public version 2011-12-30), https://arxiv.org/abs/1201.0925 .
3. Do Tran, *Behavior of Fréchet mean and Central Limit Theorems on spheres*, arXiv:1911.01985 (first public version 2019-11-05), https://arxiv.org/abs/1911.01985 .

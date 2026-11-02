# Two even chord moments identify spherical lunes, with sharp square-root angle stability

## Finding
Let \(0<\theta\le\pi\) and \(R>0\). On the sphere of radius \(R\), take the spherical lune whose longitudes lie in an interval of width \(\theta\), bounded by two semicircles meeting at antipodal poles. Choose \(X,Y\) independently according to normalized surface area on that lune, and put \(D=\|X-Y\|_2\), \(\mu=\mathbb E[D^2]\), \(\nu=\mathbb E[D^4]\), and \(\kappa=\nu/\mu^2\).

With \(x=\theta/2\), \(v=\sin x/x\), and \(p=\pi^2/16\), define \(h=pv^2\). Then
\[
\mu=2R^2(1-h),\qquad
\nu=4R^4\left(\frac43-2h+\frac29v^2\cos^2x\right),
\]
so that
\[
\boxed{\kappa(x)=\frac{\tfrac43-2pv^2+\tfrac29v^2\cos^2x}{(1-pv^2)^2}.}
\]
The function \(\kappa(x)\) is strictly decreasing on \(0<x\le\pi/2\). Consequently the **complete feasible region** is
\[
\mu>0,\qquad \frac{40}{27}\mu^2\le\nu<K_*\mu^2,
\quad K_*:=\frac{14/9-\pi^2/8}{(1-\pi^2/16)^2}.
\]
Each feasible pair determines exactly one spherical lune up to Euclidean isometry: solve the displayed strictly monotone scalar equation for \(x\), then set
\[
\theta=2x,\qquad R=\sqrt{\frac{\mu}{2(1-p(\sin x/x)^2)}}.
\]
The lower moment-ratio endpoint is attained uniquely by hemispheres (\(\theta=\pi\)); the upper endpoint is not attained by a positive-area lune.

For any two such lunes, their angles satisfy a global inverse Hölder bound
\[
|\theta_1-\theta_2|\le C|\kappa_1-\kappa_2|^{1/2}
\]
with a finite absolute constant \(C\); **no exponent greater than \(1/2\)** works uniformly, even for positive opening angles. At a fixed radius the entire chord-distance distribution is strictly stochastically increasing with the opening angle, although the scale-free fourth-moment ratio decreases.

## Assumptions and scope
The samples are independently uniform by **spherical surface area**, not uniformly chosen directions in polar angle or isotropic random-line chords. The distance is the **ambient Euclidean chord length**, not intrinsic geodesic distance. Spherical lunes are restricted to geodesically convex opening angles \(0<\theta\le\pi\). The sphere radius is unknown and strictly positive. The limiting zero-area case \(\theta=0\) is excluded.

## Proof
Choose the longitude centered at zero and write a unit direction as \(U=(\sqrt{1-Z^2}\cos\Phi,\sqrt{1-Z^2}\sin\Phi,Z)\), where \(Z\) is uniform on \([-1,1]\), \(\Phi\) is uniform on \([-x,x]\), and they are independent. Using \(\mathbb E\sqrt{1-Z^2}=\pi/4\), the mean vector is
\[
\mathbb E U=(\tfrac\pi4 v,0,0),\qquad \|\mathbb E U\|^2=h.
\]
The second-moment matrix is diagonal, with diagonal entries
\[
\frac13(1+v\cos x),\quad\frac13(1-v\cos x),\quad\frac13.
\]
For independent \(U,V\), \(D^2=2R^2(1-U\cdot V)\), \(\mathbb E[U\cdot V]=h\), and \(\mathbb E[(U\cdot V)^2]=\operatorname{tr}((\mathbb E UU^{\mathsf T})^2)=1/3+2v^2\cos^2x/9\). This establishes both moments.

To prove the needed global strict monotonicity, put \(s=\sin x\), \(c=\cos x\) and
\[
H(x)=(s-xc)\big(3px^2-9p^2s^2+x^2c^2+pc^2s^2\big)+xc s^2(x^2-ps^2).
\]
Direct differentiation gives
\[
\boxed{\kappa'(x)=-\frac{4sH(x)}{9x^5(1-p(s/x)^2)^3}.}
\]
All denominator factors are positive. The strict inequality \(H(x)>0\) over the entire interval follows from a **rational polynomial certificate**, rather than numerical sampling: take the degree-15 sine and degree-14 cosine Taylor polynomials \(S_{15},C_{14}\), and \(p_0=6168503/10000000\). Form \(P(t)=H_{S_{15},C_{14},p_0}(\sqrt t)/t^{5/2}\), which is an exact rational polynomial of degree 35. On \(t\in[0,(11/7)^2]\), express \(P\) in the degree-35 Bernstein basis. Every one of its 36 exact rational coefficients is **greater than \(1/10\)**. The embedded verifier constructs and checks those coefficients using rational arithmetic.

For completeness, the Taylor remainders on \(0\le x\le 11/7\) are bounded by \(x^{17}/17!\) and \(x^{16}/16!\); Machin's arctangent identity with alternating rational series proves \(|p-p_0|<10^{-7}\). On the explicit ranges \(|s|\le2x\), \(|c|\le2\), \(|s-xc|\le x^3\), \(0\le p\le1\), direct differentiation of the displayed polynomial gives \(|H_s|\le500x^2\), \(|H_c|\le200x^3\), and \(|H_p|\le123x^5\). Therefore for \(0<x\le\pi/2<11/7\),
\[
\left|\frac{H(x)}{x^5}-P(x^2)\right|
\le (11/7)^{14}\left(\frac{500}{17!}+\frac{200}{16!}\right)+\frac{123}{10^7}<\frac1{10000}.
\]
Thus \(H(x)/x^5>1/10-1/10000>0\), proving strict monotonicity without a floating-point sign assumption.

As \(x\downarrow0\), \(v\to1\) and \(\kappa\to K_*\); at \(x=\pi/2\), \(v=2/\pi\), \(h=1/4\), \(c=0\), giving \(\kappa=40/27\). Continuity and strict monotonicity give the feasible interval and its inverse formula. Positive \(\mu\) fixes the radius uniquely. One moment cannot determine both unknown parameters, since for any angle the radius may be adjusted to produce that mean square.

For stability, the small-angle expansion reads
\[
K_*-\kappa(x)=\frac{2(4+p-9p^2)}{27(1-p)^3}x^2+O(x^4),
\]
whose coefficient is strictly positive. Also \(-\kappa'(x)/x\) extends continuously to a positive value at \(x=0\) and stays positive on the compact interval \([0,\pi/2]\). Hence its minimum \(c_0>0\) exists and
\[
\kappa(x_1)-\kappa(x_2)\ge \frac{c_0}{2}(x_2^2-x_1^2)
\ge\frac{c_0}{2}(x_2-x_1)^2
\]
for \(0<x_1<x_2\le\pi/2\). One may take \(C=2\sqrt{2/c_0}\). Comparing \(x\) with \(2x\) as \(x\downarrow0\) proves that an exponent greater than \(1/2\) is impossible.

Finally, on one probability space use independent uniform \(Z_1,Z_2\in[-1,1]\) and uniform \(T_1,T_2\in[-1/2,1/2]\) for every \(\theta\). The longitude difference is \(\theta(T_1-T_2)\), of absolute value at most \(\pi\). Therefore \(\cos(\theta(T_1-T_2))\) strictly decreases in \(\theta\) almost surely for \(\theta\in(0,\pi]\), and so the corresponding \(D^2\) strictly increases. This proves the stochastic ordering.

## Verification
Run `python verify.py` with `sympy` and `numpy`. The deterministic script verifies the 36 exact Bernstein coefficients, the Machin-series rational bound for \(\pi\), the explicit total Taylor-error bound, two independent small-angle symbolic identities, and six fourth-dimensional quadratures of the moment formulas. A successful run prints `VERIFY_OK`; no finite grid is used to prove the continuum inequality.

## Relationship to prior work
Tu and Fischbach (2002) give forward distance-density machinery for spherical **volume** samples, including radially varying densities, not an inverse theorem for surface-area lunes. Gille (2005) studies isotropically sampled hemisphere chords, a different sampling law. Moseeva, Tarasov and Zaporozhets (2020) express spherical **geodesic-distance** laws of spherical convex bodies generated by line-free cones in terms of random geodesic chords, and explicitly calculate spherical-cap laws. Their formal pointed-cone assumption excludes a whole lune containing antipodal poles. Besau and collaborators (2023) study random spherical convex hull facet counts on a fixed right-angle wedge. These are important related forward constructions but do not state the displayed scale-free lune moment monotonicity or its inverse classification. The hemispherical endpoint is also covered by a separate spherical-cap moment formula; it is not claimed as a new endpoint calculation. Historical originality is provisional rather than certified.

## Limitations
The conclusion excludes lunes with opening angle greater than \(\pi\), nonuniform surface samples, and geodesic instead of Euclidean distances. The inverse bound is deterministic for exact moments; no finite-sample or noise-propagation theorem is asserted for radius. The interval certificate uses rational symbolic computation and explicitly stated inequalities, not an independent formal proof system. A previously unindexed equivalent result may exist.

## References
- S.-J. Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046v1 (first public 2002-01-22), https://arxiv.org/html/math-ph/0201046v1.
- W. Gille, *Chord Length Distributions of the Hemisphere*, Journal of Mathematics and Statistics 1 (2005), 24–28, first published 2005-03-31, https://doi.org/10.3844/jmssp.2005.24.28.
- T. Moseeva, A. Tarasov and D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297v1 (2020-07-14), https://arxiv.org/html/2007.07297v1.
- F. Besau et al., *Spherical convex hull of random points on a wedge*, Mathematische Annalen (first published 2023-08-25), https://doi.org/10.1007/s00208-023-02704-9.

# Exact Crofton component law and sharp centering for spherical latitude zones

## Finding
Let \(S^2=\{x\in\mathbb R^3:\|x\|=1\}\), fix an axis \(e\), and let
\[
Z_{a,b}=\{x\in S^2:-a\le x\cdot e\le b\},\qquad 0\le a,b\le1,\quad a+b>0.
\]
Choose a Euclidean affine plane from the rigid-motion-invariant measure conditioned to meet the unit ball: its unit normal is uniform on \(S^2\), and its signed offset from the origin is independent and uniform on \([-1,1]\). Write \(N\in\{0,1,2\}\) for the number of connected components of its intersection with \(Z_{a,b}\); tangencies are ignored as a null event. Set \(f(t)=\arccos t\), \(g(t)=\sqrt{1-t^2}\), and \(H(t)=f(t)g(t)\).

The **complete component-count distribution** is
\[
\begin{aligned}
\Pr(N=0)&=1-\frac{a+b}{2}-\frac{H(a)+H(b)}4,\\
\Pr(N=2)&=\frac{f(a)g(b)+f(b)g(a)}4,\\
\Pr(N=1)&=\frac{a+b}{2}+\frac{(f(a)-f(b))(g(a)-g(b))}4.
\end{aligned}
\]
In particular, the spherical surface-area fraction of the zone is \(h=(a+b)/2\), and
\[
\Pr(N=1)\ge h,
\]
with equality **if and only if** \(a=b\). For the centered zone, therefore, the probability of obtaining exactly one connected component equals the zone's area fraction, regardless of its width.

At a fixed area fraction \(h\in(0,1)\), moving the zone monotonically away from the equator strictly **increases** \(\Pr(N=0)\) and \(\Pr(N=1)\), and strictly **decreases** \(\Pr(N=2)\). The centered zone uniquely maximizes two-component sections and uniquely minimizes both zero- and one-component sections:
\[
\max_{a+b=2h}\Pr(N=2)=\frac12\arccos(h)\sqrt{1-h^2}.
\]
Its exact sharp minimum is
\[
\min_{a+b=2h}\Pr(N=2)=
\begin{cases}
\dfrac{(\pi/2)\sqrt{1-4h^2}+\arccos(2h)}4,&0<h\le1/2,\\
0,&1/2\le h<1.
\end{cases}
\]
The minimizing zones are exactly those at maximal allowable displacement, up to reflection. Consequently the minimum is strictly positive when \(h<1/2\) and is exactly zero when \(h\ge1/2\). The one-sided boundary onset is sharp:
\[
\min_{a+b=2h}\Pr(N=2)
=\frac{\pi+2}{4}\sqrt{\frac12-h}
+O\bigl((\tfrac12-h)^{3/2}\bigr),\quad h\uparrow\tfrac12.
\]

## Assumptions and scope
Planes are sampled by the **affine kinematic measure**, not by choosing three random surface points or by Haar-uniform planes through the sphere's center. The normalization is conditional on meeting the unit ball, so signed offset is uniform on \([-1,1]\). The object being sectioned is the spherical **surface** zone, not the solid-ball slab. A plane's intersection with the whole sphere is one circle almost surely. Removing the parts above \(b\) and below \(-a\) leaves zero, one, or two connected circular arcs (a complete circle counts as one component). The formulas remain valid at \(a=0\), \(b=0\), \(a=1\), or \(b=1\), provided \(a+b>0\). Every probability statement is up to null tangency cases.

## Proof
**1. Plane-circle geometry.** For a unit normal \(n\) and offset \(s\in(-1,1)\), the section circle has center \(sn\) and radius \(\sqrt{1-s^2}\). Its axial coordinate ranges from \(c-A\) to \(c+A\), where
\[
c=sn\cdot e,\qquad A=\sqrt{1-s^2}\sqrt{1-(n\cdot e)^2}.
\]
Its intersection with the zone is empty precisely when \(c-A>b\) or \(c+A<-a\), and has two components precisely when \(c-A<-a\) **and** \(c+A>b\). Every remaining generic configuration has exactly one component. This also proves that \(N\in\{0,1,2\}\).

**2. Trigonometric sampling coordinates.** The signed offset \(s\) and axial normal coordinate \(u=n\cdot e\) are independent uniform random variables on \([-1,1]\). Put \(|u|=\sin U\) and \(|s|=\sin V\), where \(U,V\in[0,\pi/2]\). Conditional on either sign of \(us\), \((U,V)\) has density \(\cos U\cos V\). If \(us>0\),
\[
c-A=-\cos(U+V),\qquad c+A=\cos(U-V).
\]
For \(us<0\) the extrema are instead \(-\cos(U-V)\) and \(\cos(U+V)\).

**3. Two-component integral.** Define \(\alpha=f(a)\), \(\beta=f(b)\). For \(T,t\in[0,\pi/2]\), let \(J(T,t)\) be the integral of \(\cos U\cos V\) over
\[
U,V\ge0,\quad U+V<T,\quad |U-V|<t.
\]
The substitution \(p=U+V\), \(q=U-V\) has Jacobian \(1/2\), and \(\cos U\cos V=(\cos p+\cos q)/2\). Direct integration gives
\[
J(T,t)=
\begin{cases}
T\sin T/2,&T\le t,\\
\bigl[t\sin T+(T-t)\sin t\bigr]/2,&T\ge t.
\end{cases}
\]
For \(us>0\), two components require \(U+V<\alpha\) and \(|U-V|<\beta\); for \(us<0\), interchange \(\alpha,\beta\). The signs occur equally often, so
\[
\Pr(N=2)=\tfrac12\bigl[J(\alpha,\beta)+J(\beta,\alpha)\bigr]
=\tfrac14(\alpha\sin\beta+\beta\sin\alpha).
\]
This is the displayed formula because \(\sin(f(t))=g(t)\).

**4. Empty-section integral.** In the \(us>0\) sign sector, the circle lies entirely above the northern cut precisely when \(U+V>\pi-\beta\); the opposite sign sector gives the analogous southern condition with \(\alpha\). A second elementary integral is
\[
\int_{U+V>\pi-\theta}\cos U\cos V\,dU\,dV
=1-\cos\theta-\frac{\theta\sin\theta}{2},
\quad 0\le\theta\le\pi/2,
\]
where the integration is over \([0,\pi/2]^2\). Summing the disjoint north/south events with their sign weights \(1/2\) yields
\[
\Pr(N=0)=1-\frac{a+b}{2}-\frac{H(a)+H(b)}4.
\]
The remaining probability is \(\Pr(N=1)=1-\Pr(N=0)-\Pr(N=2)\). Factoring the resulting cross term gives the third displayed identity.

**5. Strict fixed-area ordering and rigidity.** The functions \(f,g\) are strictly decreasing on \([0,1]\). Hence
\[
\Pr(N=1)-h=\tfrac14(f(a)-f(b))(g(a)-g(b))\ge0,
\]
and equality holds exactly at \(a=b\). Furthermore \(H\) is strictly concave on \((0,1)\), since
\[
H''(t)=\frac{t\sqrt{1-t^2}-\arccos t}{(1-t^2)^{3/2}}<0.
\]
The inequality follows by writing \(t=\cos\theta\) and observing \(\theta>\sin\theta\ge\cos\theta\sin\theta\). Consequently \(\Pr(N=0)\) grows strictly with displacement \(|a-b|\) at fixed \(a+b\).

For the remaining two-component probability, let \(S(a,b)=4\Pr(N=2)\). When \(0\le a<b<1\), direct differentiation gives
\[
(\partial_a-\partial_b)S
=\frac{b^2-a^2+bH(a)-aH(b)}{g(a)g(b)}>0.
\]
Both terms in the numerator are positive because \(H\) is positive and strictly decreasing. Thus decreasing \(a\) and increasing \(b\) at a fixed sum decreases \(\Pr(N=2)\) strictly. Continuity extends the comparison to the endpoints. The largest allowed displacement is \(\min(h,1-h)\); evaluating the probabilities at \((a,b)=(h,h)\), and at \((0,2h)\) when \(h\le1/2\) or \((2h-1,1)\) when \(h\ge1/2\), proves the sharp endpoint formulas, uniqueness up to reflection, and the half-area threshold.

Finally, with \(\varepsilon=1-2h\downarrow0\), one has \(\arccos(1-\varepsilon)=\sqrt{2\varepsilon}+O(\varepsilon^{3/2})\) and \(\sqrt{1-(1-\varepsilon)^2}=\sqrt{2\varepsilon}+O(\varepsilon^{3/2})\). Substitution proves the stated square-root onset.

## Verification
The standalone program `spherical_zone_components_check.py` uses only the Python standard library. Invoke it with `python3 spherical_zone_components_check.py`. It independently classifies circle-section components from raw plane normals and signed offsets, compares numerical midpoint quadrature and independent Monte Carlo with the closed formulas, checks the fixed-area order and rigid centered identity, and examines the square-root onset. These finite checks corroborate but do not replace the analytic proof above.

## Relationship to prior work
Moseeva, Tarasov, and Zaporozhets (2020, arXiv:2007.07297, especially Section 2 and Theorem 2.1) study lengths of **great-circle** sections of **spherically convex** bodies and distances between points. Their framework does not directly apply to a potentially nonconvex latitude zone sectioned by **affine** random planes, nor does their theorem determine the present component-count distribution. Coleman (1992) studies a different stereological problem: circular disk and annular **plane profiles of radial spherical shells**, with distributions of shell radii and inverse sampling. Coleman (1989) tabulates random plane-section **disk-radius** distributions of a sphere; the visible abstract does not establish the latitude-zone topology results here. Invariant plane-measure normalization is classical and not claimed as new.

## Limitations
The statement concerns a unit sphere in three-dimensional Euclidean space, latitude zones bounded by at most two parallel planes, and the specified affine-invariant plane law conditional on hitting the unit ball. Other random-plane conventions, nonparallel zone boundaries, higher-dimensional section connectivity, and the geometry of individual arcs are not classified. The exact formulas are fully proved, but historical priority is provisional: a full comparison with Coleman's 1989 paper was not possible from publicly available material, and similar results might exist under different stereological terminology.

## References
1. T. Moseeva, A. Tarasov, D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297, first posted 14 July 2020. https://arxiv.org/abs/2007.07297
2. R. Coleman, *The stereology of spherical shells*, Acta Stereologica 11 (1992), 137–142. https://ias-iss.org/acta/ActaStereologica_pdf/AS_1887.pdf
3. R. Coleman, *Random sections of a sphere*, Canadian Journal of Statistics 17 (1989), 27–39, DOI:10.2307/3314760. https://doi.org/10.2307/3314760

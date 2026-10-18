# Quartic stabilization of the rectangle obstruction at the dual Brunn–Minkowski endpoint

## Finding

Let
\[
R_t=[-1-t,1+t]\times[-1+t,1-t],\qquad |t|<1.
\]
For the dual quermassintegrals in the convention of Li, Wan and Zhang,
\[
\widetilde V_q(K)=\frac1n\int_{S^{n-1}}\rho_K(u)^q\,du
=\frac qn\int_K|x|^{q-n}\,dx,
\]
the critical planar exponent is \(Q=4\). There is an **exact identity**
\[
\boxed{\widetilde V_4(R_t)=\frac{16}{3}(1-t^4).}
\]
Since \(R_{-t}\) is a quarter-turn of \(R_t\) and \((R_t+R_{-t})/2=R_0\), the normalized endpoint Brunn–Minkowski deficit of this pair is
\[
\boxed{1-\Bigl(\frac{\widetilde V_4(R_t)}{\widetilde V_4(R_0)}\Bigr)^{1/4}
=1-(1-t^4)^{1/4}=\frac14t^4+O(t^8).}
\]
Thus the planar rectangle perturbation is quartically stabilizing, not merely second-order neutral, at the threshold where its second variation changes sign.

For every fixed integer \(n\ge2\), put \(d=n-2\), \(q=n+2\), and
\[
K_{t,\varepsilon}=R_t\times[-\varepsilon,\varepsilon]^d
\]
(with the product interpreted as \(R_t\) when \(d=0\)). Then for every \(|t|<1\) and every \(\varepsilon>0\),
\[
\boxed{\frac{\widetilde V_{n+2}(K_{t,\varepsilon})}
{\widetilde V_{n+2}(K_{0,\varepsilon})}
=\frac{1-t^4+\frac d2\varepsilon^2(1-t^2)}{1+\frac d2\varepsilon^2}.}
\]
In particular,
\[
\lim_{\varepsilon\downarrow0}\left[1-
\left(\frac{\widetilde V_{n+2}(K_{t,\varepsilon})}{\widetilde V_{n+2}(K_{0,\varepsilon})}\right)^{1/(n+2)}\right]
=1-(1-t^4)^{1/(n+2)}
=\frac{t^4}{n+2}+O(t^8)\quad(t\to0).
\]
The last expansion is for the **limiting** deficit, not generally for fixed positive \(\varepsilon\) when \(n>2\).

## Assumptions and scope

The rectangles and boxes are origin-symmetric convex bodies with nonempty interior. The planar identity holds throughout \(|t|<1\). The all-dimensional ratio is exact at exponent \(q=n+2\); its quartic limiting behavior is taken after the thickness limit \(\varepsilon\downarrow0\). No universal stability modulus is asserted for arbitrary convex bodies, nor is the quartic term asserted to lead for fixed positive transverse thickness.

The published rectangle second variation shows quadratic stability for \(2<Q<4\) and quadratic instability for \(Q>4\). The novel assessed question is the first surviving order at the degenerate endpoint \(Q=4\), for this canonical family.

## Proof

**Planar computation.** Write \(a=1+t\), \(b=1-t\). Direct integration over the centered rectangle gives
\[
\int_{R_t}(x^2+y^2)\,dx\,dy
=\frac43ab(a^2+b^2).
\]
Because \(ab=1-t^2\) and \(a^2+b^2=2(1+t^2)\), the integral equals \(\frac83(1-t^4)\). In dimension two at \(q=4\), the defining moment identity yields
\[
\widetilde V_4(R_t)=2\int_{R_t}(x^2+y^2)\,dx\,dy
=\frac{16}{3}(1-t^4).
\]
Rotation invariance gives \(\widetilde V_4(R_t)=\widetilde V_4(R_{-t})\), and the Minkowski midpoint is \(R_0\). Dividing the two values and expanding \((1-t^4)^{1/4}\) proves the exact deficit and its coefficient.

**All-dimensional computation.** At \(q=n+2\) the definition gives
\[
\widetilde V_{n+2}(K)=\frac{n+2}{n}\int_K|x|^2\,dx.
\]
Decompose \(x=(y,z)\in\mathbb R^2\times\mathbb R^d\), use \(|x|^2=|y|^2+|z|^2\), and integrate the cube coordinates. Since
\[
|R_t|=4(1-t^2),\quad
\int_{R_t}|y|^2\,dy=\frac83(1-t^4),\quad
\int_{[-\varepsilon,\varepsilon]^d}|z|^2\,dz=(2\varepsilon)^d\frac{d\varepsilon^2}{3},
\]
we obtain the **exact** expression
\[
\widetilde V_{n+2}(K_{t,\varepsilon})
=\frac{n+2}{n}(2\varepsilon)^d
\left[\frac83(1-t^4)+\frac{4d}{3}\varepsilon^2(1-t^2)\right].
\]
Its ratio with the value at \(t=0\) is the displayed finite-thickness formula. Passing to \(\varepsilon\downarrow0\) and taking the continuous positive \((n+2)\)-nd root gives the claimed limiting profile. The final small-\(t\) expansion follows from the binomial series.

**Consistency with the published dimensional reduction.** Li–Wan–Zhang's formula for \(Q=q-n+2\) is
\[
\widetilde V_q(K_{t,\varepsilon})
=\frac{2q}{nQ}(2\varepsilon)^{n-2}\widetilde V_Q(R_t)
+o(\varepsilon^{n-2}),
\]
not a prefactor containing \(2^q\). At \(q=n+2\), \(Q=4\), it agrees with the exact integral just computed. Thus the limiting ratio also follows from their formula; however, the direct exact calculation does not depend on invoking that asymptotic.

**Neighboring exponents.** The source's §4.1 defines
\[
P(Q)=(Q-2)\frac{\int_0^1(1-s^2)(1+s^2)^{(Q-4)/2}\,ds}{\int_0^1(1+s^2)^{(Q-2)/2}\,ds}
\]
and derives the rectangle second-variation coefficient proportional to \(P(Q)-1\). It establishes \(P(4)=1\), with negative sign when \(2<Q<4\) and positive sign when \(Q>4\). This locates the exact quartic identity precisely at the change of sign; it does not by itself imply the quartic coefficient.

## Verification

The exact rectangle inertia identity, factorization, finite-thickness moment decomposition, and Taylor coefficients are elementary symbolic identities valid for the stated full parameter intervals. A standalone exact rational script in the unchanged source package independently checks the planar polynomial identity, ratio and leading coefficient; finite spot checks do not replace the exact proof. The present corrected text also verifies the all-dimensional limiting statement directly without relying on a finite experiment. The corrected constant in the dimensional-reduction quotation is the one printed in the cited paper.

## Relationship to prior work

H. Li, Y. Wan and Y. Zhang, *On the Brunn–Minkowski inequality for q-th dual quermassintegrals with q>n* (arXiv:2608.03949v1, §4 and Theorem 1.5), establish the symmetric threshold and the rectangle second-variation mechanism. The article's §4.2–4.3 supplies the reduction from exponent \(q\) in dimension \(n\) to \(Q=q-n+2\) in the plane. It does not state the exact critical endpoint rectangle profile or its first nonzero quartic term. Hadwiger's established moment-of-inertia inequality proves the endpoint Brunn–Minkowski inequality for all origin-symmetric bodies, but gives neither this particular endpoint deficit nor the exact finite-thickness ratio. The preceding integral calculation supplies the local order and rate of stabilization in the already motivated counterexample family.

## Limitations and residual priority risk

No new global Brunn–Minkowski inequality is proved. The analysis concerns the particular rectangle mechanism, and the critical quartic behavior above dimension two emerges only after the thin-box limit. The finite-thickness correction generally adds a positive quadratic deficit when \(d>0\). A preexisting unpublished calculation of the elementary critical rectangle integral cannot be excluded. The final finding does not claim external certification, author independence, or a publication outcome.

## References

1. H. Li, Y. Wan, Y. Zhang, *On the Brunn–Minkowski inequality for q-th dual quermassintegrals with q>n*, arXiv:2608.03949v1, 2026.
2. H. Hadwiger, *Vorlesungen über Inhalt, Oberfläche und Isoperimetrie*, Springer, 1957.

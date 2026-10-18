# Universal quarter-period area contraction and exact rotational profiles of regular Reuleaux odd-gons

## Finding
Fix an odd integer \(n\geq3\) and width \(w>0\). Let \(\mathcal C_{n,w}\) be the planar convex bodies of constant width \(w\) invariant under the origin-centered rotation through \(2\pi/n\). Write \(B_w\) for the disk of radius \(w/2\), \(\mathcal R_\theta\) for rotation through \(\theta\), and
\[
M_\theta(K)=\tfrac12(K+\mathcal R_\theta K),\qquad
D(K)=\operatorname{Area}(B_w)-\operatorname{Area}(K).
\]

**Universal contraction-angle classification.** For \(0\leq\theta\leq\pi/n\), a scalar \(q\) satisfying \(D(M_\theta(K))=qD(K)\) for **every** \(K\in\mathcal C_{n,w}\) exists precisely at the three angles
\[
\boxed{\theta=0,\quad\theta=\frac\pi{2n},\quad\theta=\frac\pi n},
\qquad
\boxed{q=1,\quad q=\tfrac12,\quad q=0},
\]
respectively. In particular, a deterministic rotation by the quarter-period \(\pi/(2n)\), followed by Minkowski averaging, halves the area deficit for *all* such bodies; a rotation by the half-period \(\pi/n\) yields the disk itself.

**Area profile of the canonical minimizers.** Let \(R_n(w)\) be the centered regular Reuleaux \(n\)-gon of width \(w\), and set \(\delta=\pi/n\). Its entire rotational Minkowski-midpoint area profile is
\[
\boxed{
\operatorname{Area}(M_\theta(R_n(w)))
=\frac{nw^2}{4}\left(2\delta-\tan\frac\delta2-\theta-
\frac{\sin(\delta/2-\theta)}{\cos(\delta/2)}\right),
\qquad 0\leq\theta\leq\delta.}
\]
It is strictly increasing on \((0,\delta)\), and obeys the complementary-angle identity
\[
\boxed{\operatorname{Area}(M_\theta(R_n))+
\operatorname{Area}(M_{\delta-\theta}(R_n))
=\operatorname{Area}(R_n)+\operatorname{Area}(B_w).}
\]
Its endpoint areas are \(\operatorname{Area}(R_n)=nw^2(\delta-\tan(\delta/2))/2\) and \(\operatorname{Area}(B_w)=\pi w^2/4\).

As \(n\to\infty\) through odd integers, **uniformly** for \(0\leq t\leq1\),
\[
\boxed{
D(M_{t\pi/n}(R_n(w)))
=\frac{\pi^3w^2}{48n^2}(1-t)^2(1+2t)
+O\!\left(\frac{w^2}{n^4}\right).}
\]
The \(n=3\) instance of the explicit area profile is already known; the new general formula is asserted for every odd \(n\geq5\), together with the all-body universal-angle classification and the all-odd-order uniform asymptotic law.

## Assumptions and scope
A convex body is compact with nonempty interior. Constant width \(w\) means its Euclidean support function \(h_K(\varphi)\) satisfies \(h_K(\varphi)+h_K(\varphi+\pi)=w\) for every angle. Rotation symmetry acts about the origin. Minkowski addition is ordinary vector addition of convex sets; \(\operatorname{Area}\) is planar Lebesgue area. The class permits nonsmooth bodies and smooth bodies with positive curvature. The universal contraction factor is required to be independent of the chosen body, while it may depend on \(n\) and \(\theta\).

The regular Reuleaux \(n\)-gon is formed by replacing the sides of the regular generating \(n\)-gon of circumradius \(R=w/(2\cos(\pi/(2n)))\) with the appropriate circular arcs of radius \(w\). It is the known minimum-area member of \(\mathcal C_{n,w}\); that minimization theorem is not proved or claimed anew here. The interval \(0\leq\theta\leq\pi/n\) is a symmetry half-period for the area of rotational averages.

## Proof
**1. Spectral contraction and its complete rigidity.** The constant-width and \(2\pi/n\)-periodic conditions force the Fourier frequencies of the support function to be odd multiples of \(n\), so for real coefficients
\[
h_K(\varphi)=\frac w2+
\sum_{j\geq0}\bigl(a_j\cos((2j+1)n\varphi)+b_j\sin((2j+1)n\varphi)\bigr).
\]
The classical planar support-area identity, valid for all convex supports by approximation in \(W^{1,2}\), yields
\[
D(K)=\frac\pi2\sum_{j\geq0}
\bigl((2j+1)^2n^2-1\bigr)(a_j^2+b_j^2).
\]
Averaging a frequency \(k\) with its rotated copy multiplies its squared amplitude by \(\cos^2(k\theta/2)\). Consequently,
\[
\tag{1}
D(M_\theta(K))=\frac\pi2\sum_{j\geq0}
\bigl((2j+1)^2n^2-1\bigr)(a_j^2+b_j^2)
\cos^2\!\left(\frac{(2j+1)n\theta}{2}\right).
\]
All summands are nonnegative and the sums converge for every convex support. In particular, at \(\theta=\pi/(2n)\) each cosine square equals \(1/2\), and at \(\theta=\pi/n\) each vanishes; at \(\theta=0\) each equals one.

To prove no other angle has a universal multiplier, note that for any admissible odd multiple \(k=(2j+1)n\) the smooth support \(h(\varphi)=w/2+\epsilon\cos(k\varphi)\) gives a strictly convex constant-width member of the class whenever \(0<|\epsilon|<w/[2(k^2-1)]\). Thus a universal factor must equal \(\cos^2(n\theta/2)\) and \(\cos^2(3n\theta/2)\) simultaneously. Put \(x=n\theta/2\in[0,\pi/2]\). Their difference is \(\sin(4x)\sin(2x)\), whose only zeros in this interval are \(0,\pi/4,\pi/2\). The three exhibited angles are therefore exhaustive. Independently, at \(\theta=\pi/n\) the oddness of \(n\) gives \(\mathcal R_{\pi/n}K=-K\) by the \(2\pi/n\) symmetry, and constant width implies \((K+(-K))/2=B_w\).

**2. Curvature blocks and exact mixed area for regular Reuleaux bodies.** Set \(\delta=\pi/n\) and \(R=w/(2\cos(\delta/2))\). By rotating the angular origin, the Reuleaux support \(h\) has period \(2\delta\), and within the representative interval \(-\delta/2\leq x<3\delta/2\),
\[
h(x)=
\begin{cases}
w-R\cos x,&-\delta/2\leq x\leq\delta/2,\\
R\cos(x-\delta),&\delta/2\leq x<3\delta/2.
\end{cases}
\]
Its radius-of-curvature density \(h+h''\) equals \(w\) on the first interval and zero on the second (almost everywhere). The pieces join with matching function and first-derivative values, so there are no singular curvature atoms. The mixed area \(V(K,L)\), defined by \(\operatorname{Area}(K+L)=\operatorname{Area}(K)+2V(K,L)+\operatorname{Area}(L)\), has support representation
\[
V(K,L)=\tfrac12\int_0^{2\pi}h_L(\varphi)(h_K+h_K'')(\varphi)\,d\varphi.
\]
For \(0\leq\theta\leq\delta\), insert the curvature blocks, split the integration at \(x=\theta-\delta/2\), and integrate the elementary cosines:
\[
\begin{split}
V(R_n,\mathcal R_\theta R_n)
&=\frac{nw}{2}\left[\int_{-\delta/2}^{\theta-\delta/2}
R\cos(x-\theta+\delta)\,dx
+\int_{\theta-\delta/2}^{\delta/2}
\bigl(w-R\cos(x-\theta)\bigr)\,dx\right]\\
&=\frac{nw}{2}\left[w(\delta-\theta)-2R\sin(\delta/2-\theta)\right].
\end{split}
\]
At \(\theta=0\) this equals \(\operatorname{Area}(R_n)\). Because area is quadratic under Minkowski addition, the area of the midpoint is one-half of \(\operatorname{Area}(R_n)+V(R_n,\mathcal R_\theta R_n)\). Simplification gives the asserted closed profile.

**3. Monotonicity, complementary angles, and asymptotics.** Differentiating the exact profile yields
\[
\frac{d}{d\theta}\operatorname{Area}(M_\theta(R_n))
=\frac{nw^2}{4}\left[-1+
\frac{\cos(\delta/2-\theta)}{\cos(\delta/2)}\right].
\]
For \(0<\theta<\delta\), the numerator is strictly larger than the denominator; hence the derivative is positive. Replacing \(\theta\) by \(\delta-\theta\) negates the sine term in the profile, giving the complementary-angle identity. Finally, set \(\theta=t\delta\) and Taylor-expand \(\tan(\delta/2)\) and \(\sin((1/2-t)\delta)/\cos(\delta/2)\). The constant and linear powers of \(\delta\) cancel in the disk-area deficit. The cubic coefficient is exactly \((1-t)^2(1+2t)/12\), and the remainder is \(O(\delta^5)\) uniformly for \(t\in[0,1]\). Multiplication by \(nw^2/4\) proves the displayed \(O(w^2/n^4)\) asymptotic.

The strict area monotonicity is **specific** to the Reuleaux minimizers, not a property of arbitrary \(\mathcal C_{n,w}\). For example, the strictly convex body with support \(h=w/2+\epsilon\cos(3n\varphi)\) has \(D(M_\theta(K))=D(K)\cos^2(3n\theta/2)\), which is nonmonotone on the same interval. This confirms that the explicit Reuleaux profile is genuinely additional to the universal-angle identity.

## Verification
Run `python3 verify.py` from a directory containing the bundled standalone checker (Python standard library only). The checker reconstructs each Reuleaux support and curvature block, performs numerical integration of the mixed-area identity independently of the closed formula for multiple odd orders and angles, checks endpoints and complement relations, compares the Fourier area identity for strictly convex two-mode supports to direct support/curvature integration, checks the exact three universal multipliers, and tests the uniform large-order limit at several sample parameters. Its finite tests are regression evidence; the proof above establishes the statements for all allowed bodies, dimensions, and real angles.

## Relationship to prior work
Falcó and Myroshnychenko (2026) classify the minimizing constant-width bodies subject to \(C_n\) and \(D_n\) symmetry and derive the bang-bang curvature structure. Their published theorem provides the regular Reuleaux minimizers and their individual areas, not the angular mixed-area profile, its strict monotonicity, the uniform scaling profile, or the all-body universal contraction-angle classification proved here.

Bogosel (2023) studies the mixed area of a Reuleaux polygon with its opposite. It supplies the known half-period endpoint \(\mathcal R_{\pi/n}R_n=-R_n\), but not the nontrivial intermediate-angle formula. A previously published calculation gives the exact rotational midpoint area profile for **the Reuleaux triangle \(n=3\)**, including its endpoint complement law; that case is expressly not claimed as new. Its proof gives no all-odd-order formula or quarter-period classification across all bodies.

Sun and Sun (2026) investigate repeated fixed-rotation Minkowski averaging, limit bodies and convergence rates. The accessible abstract does not state a one-step exact area profile or the universal-angle classification for constant-width \(C_n\)-invariant bodies; the complete article could not be inspected, so possible stronger relevant coverage remains a priority risk. A separate result on random reflected Minkowski symmetrizations gives stochastic area-deficit moments, not the deterministic cyclic-rotation formulas here. The present proof uses classical support-Fourier identities, whose general validity is prior mathematics; the new claims are their precise all-body angle classification and the explicit regular-Reuleaux profiles beyond the previously published triangular case.

## Limitations
The universal classification fixes an odd cyclic symmetry order and the Minkowski averaging weight \(1/2\); it does not describe arbitrary weighted or reflected symmetrizations. The area-profile formula requires regular Reuleaux odd-gons, and its monotonicity does not hold for all cyclic constant-width bodies. The leading asymptotic is uniform in the normalized angle for fixed width, but does not concern variable-width regimes. The all-body proof uses the established planar support-area formula, not an independently new isoperimetric principle. Exact historical priority cannot be fully guaranteed, especially because the full text of Sun and Sun's relevant fixed-rotation paper was inaccessible.

## References
1. J. Falcó and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width*, arXiv:2608.05125v1, publicly submitted 2026-08-05, primary MSC2020 52A10 and 52A40. https://arxiv.org/abs/2608.05125.
2. B. Bogosel, *Mixed volumes and the Blaschke–Lebesgue theorem*, arXiv:2311.14618v1, publicly submitted 2023-11-24, especially Section 2.2. https://arxiv.org/abs/2311.14618.
3. *Exact rotational Minkowski-average area profile of the Reuleaux triangle*, mathematical result publicly available 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rotational-minkowski-average-area-profile-of-the-reuleaux--53c190e0340e.
4. Y. Sun and B. Sun, *Fixed-Rotation Minkowski Averaging: Classification and Sharp Rates*, *Bulletin of the Australian Mathematical Society* **114** (2026), 170–181, published online 2026-01-29, DOI:10.1017/S0004972725100816.
5. *Exact covariance and typical-rate gap for random planar Minkowski symmetrization*, mathematical result publicly available 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-covariance-and-typical-rate-gap-for-random-planar-minkowsk--3fd879e2fc01.

# Sharp pentagonal-section probability and aspect-ratio rigidity for right rectangular pyramids

## Finding
Let \(a,b,h>0\), and let \(P\) be the right rectangular pyramid with base vertices \((\pm a,\pm b,0)\) and apex \((0,0,h)\). Choose an unoriented plane through the **volume centroid** of \(P\) with its normal uniformly distributed over the sphere, and let \(N\) be the number of sides of the polygonal section. Put \(c=h/4\), \(L=\sqrt{a^2+b^2}\), and \(S=\sqrt{a^2+b^2+c^2}\). Then \(N\in\{4,5\}\) almost surely, and its complete law is
\[
\boxed{\Pr(N=5)=p(a,b,c)=\frac4\pi\left[\arcsin\frac aS+\arcsin\frac bS-\arcsin\frac LS\right],\qquad \Pr(N=4)=1-p(a,b,c).}
\]
For **every** fixed positive base half-length pair \(a,b\), the probability has exactly one maximizing height. The corresponding value \(c_*\) is characterized as the unique positive solution of
\[
\boxed{\sqrt{a^2+b^2}=c_*\left(\frac{a}{\sqrt{b^2+c_*^2}}+\frac{b}{\sqrt{a^2+c_*^2}}\right).}
\]
Over **all** positive \(a,b,h\), the sharp universal bound is
\[
\boxed{\Pr(N=5)\le p_*:=\frac{6}{\pi}\arccos\frac13-2=0.3509593121836439\ldots.}
\]
Equality holds if and only if \(a=b=h/4\), up to common positive scaling (equivalently the base is square and the apex height is four times its half-side length). In particular, for fixed base diagonal and apex height, the square base uniquely maximizes the probability.

The optimizer has a positive-definite, **explicit sharp quadratic stability law**. With any fixed \(L>0\), set
\[
 a=L\cos(\pi/4+\eta),\quad b=L\sin(\pi/4+\eta),\quad c=\frac{L}{\sqrt2}(1+\xi),
\]
for sufficiently small \(\eta,\xi\). Then
\[
\boxed{p_*-p(a,b,c)=\frac{\sqrt2}{\pi}\eta^2+\frac{\sqrt2}{3\pi}\xi^2+O((|\eta|+|\xi|)^3).}
\]
The *numerical value* of the square-case constant is known from a dual random-shadow problem; the contribution claimed here is the full nonsquare **centroidal-section law**, its sharp universal shape-and-height rigidity, and its two-mode stability.

## Assumptions and scope
The pyramid is a nondegenerate Euclidean convex hull, with four genuine base edges and one apex. Its volume centroid is \((0,0,h/4)\), so after centering it has base vertices \((\pm a,\pm b,-c)\) and apex \((0,0,3c)\). The sampled planes pass through this fixed centroid; they are **not** invariant affine planes with random offsets. The normal is Haar-uniform in orientation; identifying opposite normals gives the same plane. Generic means excluding the surface-measure-zero set of planes passing through vertices or containing edges. The stability expansion holds with \(L\) fixed and both perturbations small enough that \(a,b,c>0\). No claim is made for other pyramid bases or for noncentroidal offsets.

## Proof
**1. Exhaustive section-type classification.** Choose the sign of the normal \(u=(u_x,u_y,u_z)\) so that \(u_z>0\). The apex scalar product is \(3cu_z>0\), while the four base scalar products are \(\pm au_x\pm bu_y-cu_z\). Every opposite pair of base corners has sum \(-2cu_z<0\), hence at most two base corners can have positive scalar product; if there are two, they are adjacent. The pyramid has four cyclic base edges and four apex-to-base edges. A generic plane intersects an edge exactly when its endpoint scalar products have opposite signs. With zero positive base corners, there are four intersected apex edges; with two adjacent positives, there are two intersected base edges and two intersected apex edges; both cases give quadrilaterals. With exactly one positive base corner, two base edges and three apex edges are intersected, giving a pentagon. Thus \(N\in\{4,5\}\) and the pentagon event is
\[
 |a|u_x|-b|u_y||<cu_z<a|u_x|+b|u_y|.
\]
No other generic sign configurations are possible.

**2. Exact spherical integral.** On the upper hemisphere, independently of the signs of \(u_x,u_y\), use \(|u_x|=\sin\theta\cos\phi\), \(|u_y|=\sin\theta\sin\phi\), \(u_z=\cos\theta\), where \(0<\theta,\phi<\pi/2\). Put \(F=a\cos\phi+b\sin\phi\) and \(G=a\cos\phi-b\sin\phi\). The event is equivalent to
\[
 \arctan(c/F)<\theta<\arctan(c/|G|).
\]
Accounting for four sign quadrants and the upper-hemisphere area \(2\pi\) yields
\[
 p(a,b,c)=\frac2\pi\int_0^{\pi/2}\left(\frac F{\sqrt{c^2+F^2}}-\frac{|G|}{\sqrt{c^2+G^2}}\right)d\phi.
\]
Write \(a=L\cos\alpha\), \(b=L\sin\alpha\), with \(\alpha\in(0,\pi/2)\), so \(F=L\cos(\phi-\alpha)\) and \(G=L\cos(\phi+\alpha)\). For \(S^2=L^2+c^2\), a primitive on intervals of fixed cosine sign is \(\arcsin(L\sin t/S)\), since
\[
 \frac{d}{dt}\arcsin\frac{L\sin t}{S}=\frac{L\cos t}{\sqrt{c^2+L^2\cos^2t}}.
\]
Integrating \(F\) and splitting the absolute value of \(G\) at \(\phi=\pi/2-\alpha\) gives, respectively,
\[
 I_F=\arcsin\frac aS+\arcsin\frac bS,\qquad
 I_{|G|}=2\arcsin\frac LS-\arcsin\frac aS-\arcsin\frac bS.
\]
Substitution proves the exact formula without numerical integration.

**3. Unique height optimum.** Direct differentiation, valid for every \(c>0\), gives
\[
 \frac{\partial p}{\partial c}=\frac{4}{\pi(L^2+c^2)}\left[L-c\left(\frac a{\sqrt{b^2+c^2}}+\frac b{\sqrt{a^2+c^2}}\right)\right].
\]
The subtracted function is strictly increasing on \((0,\infty)\), since its derivative is
\[
 \frac{ab^2}{(b^2+c^2)^{3/2}}+\frac{ba^2}{(a^2+c^2)^{3/2}}>0.
\]
It increases from zero to \(a+b>L\). Hence the derivative of \(p\) changes sign exactly once, positive to negative. Since the exact law tends to zero at both endpoints \(c\downarrow0\) and \(c\to\infty\), this is the unique global height maximum.

**4. Sharp shape bound and equality.** Fix \(L,c>0\) and parametrize \(a=L\cos\alpha\), \(b=L\sin\alpha\) for \(0<\alpha<\pi/2\). The only \(\alpha\)-dependent part of the law is \(T=\arcsin(a/S)+\arcsin(b/S)\), and
\[
 \frac{\partial T}{\partial\alpha}=\frac a{\sqrt{c^2+a^2}}-\frac b{\sqrt{c^2+b^2}}.
\]
Because \(t/\sqrt{c^2+t^2}\) increases strictly for \(t>0\), the derivative is strictly positive for \(\alpha<\pi/4\) and strictly negative for \(\alpha>\pi/4\). Thus exactly the square \(a=b\) maximizes the pentagon probability for each fixed \(L,c\). Put \(a=b=s\) in the height equation from step 3. Its unique positive solution is \(c=s\). The maximum is therefore attained precisely at \(a=b=c>0\), and evaluation at \(a=b=c=1\) gives
\[
 p_*=\frac4\pi\left(2\arcsin\frac1{\sqrt3}-\arcsin\sqrt{\frac23}\right)
 =\frac6\pi\arccos\frac13-2.
\]
Strictness in both stages proves the global equality characterization.

**5. Local stability and boundary regimes.** Fix \(L\) and use the dimensionless variables in the statement. The first derivatives vanish at \((\eta,\xi)=(0,0)\); differentiating the explicit analytic formula gives
\[
 \partial_{\eta\eta}p=-\frac{2\sqrt2}{\pi},\qquad
 \partial_{\xi\xi}p=-\frac{2\sqrt2}{3\pi},\qquad
 \partial_{\eta\xi}p=0
\]
at that point. Taylor's theorem proves the displayed stability expansion with the full cubic remainder. The exact law also gives the sharp endpoint expansions, for fixed \(a,b>0\):
\[
 p(a,b,c)=\frac{4c}{\pi L}+O(c^2)\quad(c\downarrow0),\qquad
 p(a,b,c)=\frac{4(a+b-L)}{\pi c}+O(c^{-3})\quad(c\to\infty).
\]
These confirm both degenerating ends are strictly below the unique optimum.

## Verification
Run the complete standalone `verify.py` using Python 3. It independently evaluates the one-dimensional spherical integral with composite Simpson quadrature; constructs the five signed vertex projections and counts sign-changing edges for Gaussian-uniform directions; compares the analytic height derivative with centered finite differences; checks strict balancing and the universal bound over seeded positive triples; and checks both Hessian coefficients and the vanishing mixed curvature. A saved local execution returned `ALL_CHECKS_PASSED`. The analytical proof, rather than sampled directions or floating-point quadrature, establishes the universal assertions.

## Relationship to prior work
Brandenburg, De Loera and Meroni (arXiv:2304.14239v1, first public 2023-04-27) analyze chamber structures, edge-intersection signatures and optimization of affine and central polytope slices. These results motivate a metric-probability question, but their inspected theorem and experimental sections do not give this right-rectangular-pyramid law or a universal optimum over its aspect ratios. Black and Criado (arXiv:2406.06936v1, 2024-06-11) develop estimates for expected random shadow complexity of fixed polytopes, not this exact centroidal-section classification. Feldman and Klain (arXiv:0809.3459v1, 2008-09-19) give general inner-angle formulas for projected face counts, which do not by themselves establish the explicit present law or rigidity.

The closest directly indexed result is *Exact five-vertex shadow law and unique height optimum for right rectangular pyramids* (published mathematical finding, 2026-10-11). The square specialization here is **already covered** by the known shadow law after polar duality: the polar of a centered right **square** pyramid is again a right square pyramid, and the common value \(p_*\) is not new. For a nonsquare rectangular base, however, the polar has a **rhombic**, not rectangular, base. Haar measure is not preserved by the nonorthogonal affine map that turns this rhombus into a rectangle. Consequently, the previous right-rectangular-shadow law does not imply the general nonsquare centroidal-section formula, the universal bound across the three section parameters, or its sharp two-dimensional stability Hessian. These are the precise contributions assessed here; there is no novelty claim for polar duality, solid-angle integration, or the square-case constant.

## Limitations
Only right pyramids with rectangular bases, exact centroidal planes and Haar-uniform orientations are treated. Generic sections are four- or five-sided; exceptional vertex- or edge-containing planes have probability zero. The local stability law is not a global quadratic inequality. The bound does not extend here to arbitrary nonrectangular pyramid bases or randomly offset affine planes. Prior-literature inspection is substantial but not exhaustive: older specialized solid-angle formulas and unindexed results might contain equivalent statements. Independent mathematical review remains unperformed.

## References
1. M.-C. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1 (2023-04-27), https://arxiv.org/abs/2304.14239 .
2. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1 (2024-06-11), https://arxiv.org/abs/2406.06936 .
3. D. V. Feldman and D. A. Klain, *Angles as Probabilities*, arXiv:0809.3459v1 (2008-09-19), https://arxiv.org/abs/0809.3459 .
4. *Exact five-vertex shadow law and unique height optimum for right rectangular pyramids*, published geometric finding (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-five-vertex-shadow-law-and-unique-height-optimum-for-right--2273575e8a0a .

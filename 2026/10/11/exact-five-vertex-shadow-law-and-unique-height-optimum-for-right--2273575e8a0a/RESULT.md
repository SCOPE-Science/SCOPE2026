# Exact five-vertex shadow law and unique height optimum for right rectangular pyramids

## Finding
For all positive real numbers \(a,b,h\), consider the right rectangular pyramid
\[
K(a,b,h)=\operatorname{conv}\{(\pm a,\pm b,0),(0,0,h)\}\subset\mathbb R^3.
\]
Let \(N\) be the number of vertices in the orthogonal projection of \(K(a,b,h)\) onto a uniformly distributed, unoriented two-dimensional Euclidean plane. Then \(N\in\{4,5\}\) almost surely and
\[
\Pr(N=5)=p(a,b,h)=\frac2\pi\left[\arctan\frac ah+\arctan\frac bh-2\arcsin\frac{ab}{\sqrt{(a^2+h^2)(b^2+h^2)}}\right]. \tag{1}
\]
For every fixed \(a,b>0\), this probability has one and only one maximizing height \(h_*>0\). With \(s=a^2+b^2\), \(c=ab\), the square \(t_*=h_*^2\) is the unique positive solution of
\[
2ab(2t+s)=(a+b)(t+c)\sqrt{t+s}. \tag{2}
\]
For every fixed base area \(4ab\) and fixed height \(h>0\), \(p(a,b,h)\) increases *strictly* with the unordered base aspect ratio \(\max(a,b)/\min(a,b)\). Thus the square base uniquely minimizes this probability among equal-area right rectangular pyramids at fixed height. Moreover, setting \(r=a/b\ge1\), the optimum over height tends to one in the thin-base limit, with the sharp expansion
\[
1-\max_{h>0}p(a,b,h)\sim\frac4{\pi\sqrt r}\qquad (r\to\infty). \tag{3}
\]

## Assumptions and scope
All distances are ordinary Euclidean distances. Each \(a,b\) is a positive **half**-side length, and \(h\) is the perpendicular height above the rectangle center. The random unoriented plane has the rotation-invariant Haar distribution on the Grassmannian of two-planes in \(\mathbb R^3\). Vertices are distinct planar convex-hull extreme points, not face multiplicities. The measure-zero directions whose normal is horizontal or produce collinear projected triples do not affect the stated probabilities. Equation (2) characterizes the unique positive root without selecting extraneous roots introduced by squaring.

## Proof
**1. Projective reduction and the exact event.** Write the plane normal \(u=(u_x,u_y,u_z)\) with \(u_z\ne0\). Orthogonal projection, restricted to the horizontal base plane, is a linear isomorphism onto the target plane. Under the inverse isomorphism, the projected apex is the planar point \(q=(-h u_x/u_z,-h u_y/u_z)\), while the base projects back to \(R=[-a,a]\times[-b,b]\). Consequently, the projected polygon is affinely equivalent to \(\operatorname{conv}(R\cup\{q\})\). An exterior point produces five vertices precisely if it sees one and only one side of \(R\). This is the disjoint union, except for boundaries, of
\[
\{|q_x|>a,\ |q_y|<b\}\ \cup\ \{|q_x|<a,\ |q_y|>b\}. \tag{4}
\]
If \(q\) is inside the rectangle, or in one of the four corner regions, there are four projected vertices; these exhaust the possibilities almost surely.

**2. Integrating the random direction.** A uniformly distributed spherical normal gives \(q\) the isotropic planar Cauchy density
\[
f(q_x,q_y)=\frac{h}{2\pi(h^2+q_x^2+q_y^2)^{3/2}}. \tag{5}
\]
For the first pair of strips, direct integration (first in \(q_y\), then in \(q_x\)) gives
\[
\Pr(|q_x|>a,|q_y|<b)
=\frac2\pi\left[\arctan\frac bh-\arcsin\frac{ab}{\sqrt{(a^2+h^2)(b^2+h^2)}}\right]. \tag{6}
\]
Adding its counterpart with \(a,b\) swapped gives (1). For example, formula (6) follows from
\[
\int_{-b}^{b}\frac{h\,dy}{2\pi(h^2+x^2+y^2)^{3/2}}=\frac{hb}{\pi(h^2+x^2)\sqrt{h^2+x^2+b^2}}.
\]

**3. Rigidity of optimal height.** Put \(t=h^2\), \(s=a^2+b^2\), \(c=ab\), and set
\[
F(t)=\frac{2c(2t+s)}{(t+c)\sqrt{t+s}}.
\]
Differentiating (1) and collecting over a positive denominator shows that the sign of \(\partial p/\partial h\) equals the sign of \(F(t)-(a+b)\). Explicitly, before extracting this sign,
\[
\frac{\pi}{2}\frac{\partial p}{\partial h}
=\frac{2ab/\sqrt{t+s}-a}{t+a^2}+\frac{2ab/\sqrt{t+s}-b}{t+b^2}. \tag{7}
\]
Furthermore,
\[
F'(t)=-\frac{c\,[2t^2+(3s-2c)t+s(2s-3c)]}{(t+c)^2(t+s)^{3/2}}<0,
\]
since \(s\ge2c>0\). Now \(F(0)=2\sqrt s>a+b\), while \(F(t)\to0\). Hence the derivative changes from positive to negative exactly once, proving the unique global maximum (2). The endpoint probabilities approach zero as \(h\to0^+\) and as \(h\to\infty\).

**4. Anisotropy monotonicity.** Scale all lengths by \(\sqrt{ab}\), so \(c=1\); write \(t=h^2/(ab)\) and \(s=(a^2+b^2)/(ab)\ge2\). The arctangent sum in (1) is the argument in \((0,\pi)\) of \((t-1)+i\sqrt{t(s+2)}\). Differentiating this argument and the arcsine term yields the exact identity
\[
\frac{\partial p}{\partial s}=\frac{\sqrt t}{\pi(t^2+ts+1)}\left[\frac{t-1}{\sqrt{s+2}}+\frac2{\sqrt{t+s}}\right]>0. \tag{8}
\]
For \(t\ge1\) positivity is immediate; for \(0<t<1\), use \(2/\sqrt{s+t}>2/\sqrt{s+2}>(1-t)/\sqrt{s+2}\). Since \(s=r+1/r\) strictly increases with \(r\ge1\) away from one, the square base is the unique minimizer up to swapping sides.

**5. Sharp thin-base law.** Set \(b=1\), \(a=r\to\infty\) by similarity, and write \(t_*=r v_r\). Equation (2), after division by its leading power in \(r\), reads
\[
\frac{2(1+2v_r/r+1/r^2)}{\sqrt{1+v_r/r+1/r^2}}=(1+1/r)(v_r+1).
\]
The strictly decreasing-root characterization implies \(v_r\to1\) (bracket the unique root between any fixed values on either side of one). Thus \(h_*/\sqrt r\to1\). Expanding the four arctangent and arcsine terms in (1) at \(h=h_*\), with \(h_*/\sqrt r\to1\), gives
\[
1-p(r,1,h_*)=\frac2\pi\left(\frac{h_*}{r}+\frac1{h_*}\right)+o(r^{-1/2})=\frac4{\pi\sqrt r}+o(r^{-1/2}).
\]
This proves (3).

## Verification
The attached standalone `verify.py` computes both the closed law and an independent projected-polygon hull count for specified parameter triples; checks the exact derivative and anisotropy identities numerically against centered differences; isolates the unique height root by bisection and verifies the strict one-sided sign change; and checks the thin-base coefficient. Run with `python3 verify.py`; it requires only Python's standard library. The finite direction samples diagnose implementation, whereas the infinite-dimensional quantifiers above follow from the analytic steps. For the square base, \(h_*=\sqrt2a\) and \(p_5=(2/\pi)(3\operatorname{arcsec}3-\pi)\approx0.3509593\); this specialization is a known regular-octahedron shadow probability, not a novelty claim.

## Relationship to prior work
Finch's 2012 treatment and Böröczky–Henk's earlier analysis discuss random planar shadows of regular polytopes, including existing exact regular-octahedron probabilities; Black–Criado (2024) gives general shadow-complexity estimates. Their inspected texts do not provide the present non-square rectangular-pyramid law, its unique maximizing-height equation, or strict fixed-area anisotropy monotonicity. The coincident square-base/regular-octahedron value is explicitly prior knowledge. The novel content, subject to independent historical verification, is the full anisotropic right rectangular-pyramid family and its sharp coupled optimization and degeneration behavior. General intrinsic-angle formulas may recover pieces after specialization; no assertion that the methods themselves are new is made.

## Limitations
The calculation requires the apex to be directly above the rectangle center, Euclidean orthogonal projection and uniform plane orientation; it does not cover oblique apexes, nonrectangular bases, other dimensions, or nonuniform viewing directions. The proof is analytic, but the originality conclusion depends on the surveyed indexed and inspected literature and does not exclude unindexed earlier derivations. No independent audit or external confirmation is claimed.

## References
1. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (2012-03-12), https://arxiv.org/html/1203.2464v1 .
2. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, preprint SC 97-21 (May 1997), https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf .
3. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1 (2024-06-11), https://arxiv.org/abs/2406.06936 .

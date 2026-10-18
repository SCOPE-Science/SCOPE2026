# Sharp oblique orientation transition for the minimum shadow perimeter of a circular bicone

## Finding
Let \(K_{r,h}\subset\mathbb R^3\) be the solid symmetric circular bicone
\[
K_{r,h}=\left\{(x,y,z):\frac{\sqrt{x^2+y^2}}r+\frac{|z|}h\le1\right\},\qquad r,h>0.
\]
For a unit vector \(u\), write \(P(u)\) for the Euclidean perimeter of the orthogonal projection of \(K_{r,h}\) onto \(u^\perp\). Put \(t=h/r\). There is a unique \(t_0>0\) satisfying
\[
\boxed{\sqrt{1+t_0^2}=\operatorname{arsinh}(1/t_0)},\qquad t_0=0.6627434193491816\ldots.
\]
If \(0<t\le t_0\), the only minimizing *unoriented* projection planes are those containing the bicone axis, and
\[
\boxed{\min_u P(u)=4r\sqrt{1+t^2}.}
\]
If \(t>t_0\), every minimizing viewing normal makes the same unique acute **oblique** angle \(\alpha_*(t)\in(0,\pi/2)\) with the axis, up to reflection across the equator and axial rotation. Writing \(L=\sqrt{1+t^2}\) and \(s_*=\sin\alpha_*\), the unique number \(x_*=Ls_*\in(1,L)\) is the root of the strictly increasing equation
\[
\boxed{t\sqrt{x^2-1}=\frac1L\int_0^1
 \frac{z^2\,dz}{\sqrt{1-z^2/L^2}\sqrt{x^2-z^2}}.}
\]
The exact minimizing perimeter is given in the proof by an incomplete elliptic integral. The transition has the sharp orientation law
\[
\boxed{\frac\pi2-\alpha_*(t)=2\sqrt{\frac{t_0}{1+t_0^2}}\sqrt{t-t_0}
 +O((t-t_0)^{3/2})}\qquad (t\downarrow t_0).
\]
For tall bicones, \(\alpha_*(t)=t^{-1}-\frac13t^{-3}+O(t^{-5})\) and \(\min_u P(u)=2\pi r-\frac{\pi r}{2t^2}+O(rt^{-4})\). Thus the direction minimizing the silhouette perimeter changes from a side-on view to a genuinely tilted view even though the body retains the same rotational symmetry.

## Assumptions and scope
All measurements are Euclidean. The parameter \(r\) is the equatorial disk radius and \(h\) is *half* the tip-to-tip height. A viewing direction is an unoriented normal \(\{u,-u\}\) to a projection plane; distinct directions related by rotation around the bicone axis are geometrically equivalent. Projection perimeter is the intrinsic one-dimensional boundary measure in the projected plane, not a three-dimensional section perimeter, shadow area, mean width of the solid, or surface area of the solid. Angles are radians. The formulas include every \(r,h>0\), with equality cases stated above.

For \(0\le\alpha\le\pi/2\), let \(s=\sin\alpha\) and \(L=\sqrt{1+t^2}\). Define the incomplete elliptic integral of the second kind by
\[
E(\beta\mid m)=\int_0^\beta\sqrt{1-m\sin^2 v}\,dv.
\]
The complete directional shadow-perimeter formula is
\[
\boxed{\frac{P(\alpha)}{4r}=
\begin{cases}
 E(\pi/2\mid s^2),&0\le s\le1/L,\\
 ts\sin\theta_0+E(\pi/2-\theta_0\mid s^2),&1/L<s\le1,
\end{cases}}
\quad\theta_0=\arccos\frac1{Ls}\quad(s>1/L).
\]
For \(t>t_0\), evaluating this expression at \(s=s_*\) gives the exact global minimum; no unlisted closed form for \(s_*\) is asserted.

## Proof
**Support-function reduction.** The bicone is the convex hull of its equatorial radius-\(r\) disk and the two points \(\pm he_3\). Its support function is therefore
\[
h_K(v)=\max\{r\sqrt{v_1^2+v_2^2},h|v_3|\}.
\]
Take \(u=(\sin\alpha,0,\cos\alpha)\) and the orthonormal basis \((\cos\alpha,0,-\sin\alpha),(0,1,0)\) of \(u^\perp\). Cauchy's planar support-function perimeter formula and fourfold symmetry yield
\[
\frac{P(\alpha)}{4r}=\int_0^{\pi/2}
\max\{\sqrt{1-s^2\cos^2\theta},ts\cos\theta\}\,d\theta.\tag{1}
\]
The second term exceeds the first precisely where \(Ls\cos\theta>1\). This gives the displayed two-branch elliptic profile. In the first branch, differentiating under the integral shows strict decrease in \(s\in(0,1/L]\):
\[
\frac1{4r}\frac{dP}{ds}=-s\int_0^{\pi/2}
\frac{\cos^2\theta}{\sqrt{1-s^2\cos^2\theta}}\,d\theta<0.
\]

**Single-crossing derivative.** In the second branch let \(\theta_0=\arccos(1/(Ls))\). Differentiating equation (1), the moving-boundary terms cancel because both support-function terms agree at the crossing. Hence
\[
F_t(s):=\frac1{4r}\frac{dP}{ds}
=t\sin\theta_0-s\int_{\theta_0}^{\pi/2}
\frac{\cos^2\theta}{\sqrt{1-s^2\cos^2\theta}}\,d\theta.
\]
Set \(x=Ls\) and make the substitution \(z=x\cos\theta\). This gives the exact identity
\[
xF_t(s)=G_t(x),\quad
G_t(x)=t\sqrt{x^2-1}-\frac1L\int_0^1
\frac{z^2\,dz}{\sqrt{1-z^2/L^2}\sqrt{x^2-z^2}}.
\tag{2}
\]
For each fixed \(t>0\), \(G_t\) is continuous at \(x=1\), with \(G_t(1)<0\). It is strictly increasing for \(1<x\le L\): its first term increases and its positive integrand strictly decreases in \(x\). In particular,
\[
G_t'(x)=\frac{tx}{\sqrt{x^2-1}}+
\frac{x}{L}\int_0^1\frac{z^2\,dz}
{\sqrt{1-z^2/L^2}(x^2-z^2)^{3/2}}>0
\qquad(1<x\le L).
\]
Consequently, the perimeter either decreases throughout the second branch or decreases and then increases exactly once.

**Threshold and equality cases.** At \(s=1\), direct elementary integration gives
\[
F_t(1)=\sqrt{1+t^2}-\operatorname{arsinh}(1/t)=:H(t).
\]
Here \(H'(t)=\sqrt{1+t^2}/t>0\), with \(H(t)\to-\infty\) as \(t\downarrow0\) and \(H(t)\to\infty\) as \(t\to\infty\). Thus \(H\) has exactly one root \(t_0\). If \(t\le t_0\), then \(G_t(x)<0\) for \(1\le x<L\), proving the side-on direction is uniquely minimizing modulo axial symmetry. At \(s=1\), the planar shadow is the rhombus with vertices \((\pm h,0),(0,\pm r)\), and its perimeter is \(4\sqrt{h^2+r^2}\). If \(t>t_0\), then \(G_t(1)<0<G_t(L)\); strict monotonicity gives exactly one root \(x_*\), at which the derivative changes sign from negative to positive. This is the unique oblique minimum, completing the full-domain and equality classification.

**Sharp approach to the transition.** Differentiating \(F_t(s)\) at \(s=1\), with \(\theta_0=\arctan t\), and using elementary antiderivatives of \(\csc\theta\) and \(\csc^3\theta\) gives
\[
\partial_sF_t(1)=\tfrac12\left(\frac{\sqrt{1+t^2}}{t^2}
 +\operatorname{arsinh}(1/t)\right)>0.
\]
At \(t=t_0\), this equals \(L_0^3/(2t_0^2)\), while \(\partial_tF_t(1)=H'(t)=L_0/t_0\). The implicit-function theorem therefore yields
\[
s_*(t)=1-\frac{2t_0}{1+t_0^2}(t-t_0)+O((t-t_0)^2).
\]
The elementary expansion of \(\arcsin\) at one proves the stated square-root angle law.

**Tall-cone limit.** In (2), the root satisfies \(x_*\to1\) as \(t\to\infty\), and dominated convergence after \(z=\sin v\) gives \(\int_0^1 z^2/\sqrt{1-z^2}\,dz=\pi/4\). Thus \(x_*=1+\pi^2/(32t^4)+o(t^{-4})\). Expanding \(\arcsin(x_*/\sqrt{1+t^2})\) yields \(\alpha_*=t^{-1}-t^{-3}/3+O(t^{-5})\). The active support-function interval has length \(O(t^{-2})\); comparing it with the ellipse profile shows that its correction to the minimum is \(O(rt^{-6})\). Expanding the complete elliptic integral at \(s=1/L\) therefore gives \(P_{\min}=2\pi r-\pi r/(2t^2)+O(rt^{-4})\).

## Verification
The companion `check_projection_perimeter.py` reproduces the threshold, compares the closed directional formula with direct support-function quadrature, reconstructs projected convex hulls from independently sampled disk images and apices, compares analytical minimizers with numerical scalar optimization, and tests both asymptotic regimes. Run `python check_projection_perimeter.py` with NumPy and SciPy installed. The exact global classification rests on equation (2) and strict monotonicity, not on finite sampling or numerical optimization.

## Relationship to prior work
Finch's *Oblique Circular Cones and Cylinders* (arXiv:1212.5946, first public 24 December 2012) analyzes surface area and mean width of solid circular cones and cylinders, including oblique-cone cut ratios. It supplies a motivating convex-hull/elliptic-integral context but concerns three-dimensional intrinsic volumes and bisected cone ratios, not the minimum **planar projection perimeter** of the symmetric two-apex bicone. Finch's *Convex Hull of Two Orthogonal Disks* (arXiv:1211.4514) is also about intrinsic volumes of convex hulls, with different generating sets. General Cauchy support integration and the perimeter formula for a projected disk are classical ingredients, not claimed as new. The contribution asserted here is the exact change of the minimizing viewing orientation, uniqueness, implicit root and square-root transition. Accessible mathematical-record searches did not find the same theorem; this is not definitive proof of historical priority.

## Limitations
Only Euclidean planar orthogonal-shadow perimeter is optimized. The bicone must be symmetric, with congruent coaxial upper and lower circular cones. The result does not classify projected areas, noncentral sections, asymmetric cones, or general bodies of revolution. The minimizing angle for \(t>t_0\) is specified by a rigorous integral root rather than an elementary closed expression. Finite computer checks are corroborative, and historical priority has not been independently certified.

## References
- S. R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946 (first posted 24 December 2012), https://arxiv.org/abs/1212.5946.
- S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514 (first posted 19 November 2012), https://arxiv.org/abs/1211.4514.
- Classical Cauchy support-function formula for the perimeter of a planar convex body (used as a standard identity, not as an original result).

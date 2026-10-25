# The curvature-gradient term in polygonal boundary-chord statistics

## Finding

Let \(\gamma:\mathbb R/L\mathbb Z\to\mathbb R^2\) be a positively oriented, embedded, closed \(\mathrm C^8\) curve, parametrized by arclength, with length \(L>0\) and everywhere-positive curvature \(\kappa(s)>0\). For each integer \(m\ge3\), join successive points \(\gamma(jL/m)\) to form the inscribed convex polygon \(P_m\). Write \(p_m\) for its perimeter. Choose \(X_m,Y_m\) independently and uniformly by arclength on \(\partial P_m\), and denote their Euclidean separation by \(D_m\) and their shorter along-boundary separation by \(B_m\). Define the dimensionless observable
\[
\Lambda_m=p_m^2\lim_{r\downarrow0}\frac{\Pr(D_m\le r)-\Pr(B_m\le r)}{r^2}.
\]
(The radius limit is taken **first**, separately for each polygon.) The limit exists. The new two-term continuum law is
\[
\boxed{\displaystyle
m\Lambda_m=\frac L6\int_0^L\kappa^2\,ds+
\frac{L^3}{m^2}\left[\frac7{360}\int_0^L\kappa^4\,ds-\frac1{36}\int_0^L(\kappa')^2\,ds\right]+O_{\gamma}(m^{-4}).}
\tag{1}
\]
In particular, the first correction combines a positive quartic curvature term and a **negative curvature-gradient energy**, not merely a function of the distribution of curvature values.

This distinction is witnessed by two explicit strictly convex smooth ovals with identical arclength distributions of curvature. For integer \(p\ge2\), let their support functions, in outward-normal angle \(\theta\), be
\[
h_p(\theta)=1+\frac{\cos(p\theta)}{2(1-p^2)},\qquad
\rho_p(\theta)=h_p+h_p''=1+\tfrac12\cos(p\theta)>0.
\]
They all have perimeter \(2\pi\), and each \(\int f(\kappa)\,ds\) agrees for every continuous function \(f\) for which the integral is defined. Nevertheless, the second coefficient in (1) equals
\[
\boxed{\displaystyle
\lim_{m\to\infty}m^2\left(m\Lambda_m-\frac{4\pi^2}{3\sqrt3}\right)
=\frac{4\sqrt3\,\pi^4}{3645}(378-85p^2).}
\tag{2}
\]
It is strictly **positive for \(p=2\)** and strictly **negative for \(p=3\)**. Thus the correction detects geometric oscillation frequency even though all one-point curvature statistics, including every curvature moment, are identical.

## Assumptions and scope

The curve is parametrized once around by positively oriented Euclidean arclength. Its curvature is strictly positive, so its sufficiently fine successive inscribed polygons have genuine, positive exterior turns. Derivatives \(\kappa'\) and \(\kappa''\) are arclength derivatives. The order \(\mathrm C^8\) is a convenient sufficient regularity for the uniform remainders and periodic quadrature estimates; optimal regularity is not asserted. Probability samples are taken **on each polygon**, not on the limiting smooth curve or in its interior. The lengths used to place the vertices are smooth-curve arclength increments \(L/m\), rather than equal polygon edge lengths. All constants hidden in \(O_{\gamma}\) may depend on the fixed curve. Neither convergence uniform over classes of curves nor interchangeability of the limits \(r\downarrow0\) and \(m\to\infty\) is claimed.

## Proof

**1. The established local boundary-corner identity, reconstructed.** For any strictly convex polygon of perimeter \(p\), let its exterior turning angles be \(\beta_j\in(0,\pi)\). Fix a sufficiently small radius \(r\), less than the nonadjacent-side separation and relevant positive edge-length scales. Two points on the same edge contribute equally to the Euclidean-close and boundary-close events. The only extra Euclidean-close pairs lie on two edges incident at a common vertex. If their distances from that vertex are \(u,v\ge0\), their shorter boundary distance is locally \(u+v\). Their Euclidean difference vector is obtained from \((u,v)\) by a linear map with Jacobian \(\sin\beta_j\), taking the positive quadrant to a sector of angle \(\beta_j\). Consequently, the parameter-pair area where Euclidean separation is at most \(r\) equals \(\beta_jr^2/(2\sin\beta_j)\), whereas the corresponding boundary-distance triangle has area \(r^2/2\). Counting both orders of the independently sampled pair and dividing by \(p^2\) yields the exact previously known formula
\[
\Pr(D\le r)-\Pr(B\le r)
=\frac{r^2}{p^2}\sum_j\left(\frac{\beta_j}{\sin\beta_j}-1\right).
\tag{3}
\]
Thus \(\Lambda_m=\sum_j H(\beta_{j,m})\), where \(H(z)=z/\sin z-1\). Equation (3), including its polygonal-angle consequences, is **prior work**; the novelty claim concerns the second-order continuum expansion (1) and the frequency distinction (2).

**2. Turning angles of equal-arclength inscribed polygons.** Put \(\delta=L/m\), let \(T(s)=\gamma'(s)=e^{i\phi(s)}\) be the unit complex tangent, and let \(\phi'=\kappa\). Consider the chord centered at \(c\) with arclength span \(\delta\):
\[
W(c,\delta)=\gamma(c+\delta/2)-\gamma(c-\delta/2)
=\delta\left[T(c)+\frac{\delta^2}{24}T''(c)+O_{\mathrm C^1}(\delta^4)\right].
\]
Here the remainder and its derivative in \(c\) are bounded uniformly along the closed curve. Since \(\operatorname{Im}(T''/T)=\kappa'\), the chord's direction angle is
\[
\arg W(c,\delta)=\phi(c)+\frac{\delta^2}{24}\kappa'(c)+O_{\mathrm C^1}(\delta^4).
\]
The outgoing and incoming chords at vertex \(s_j=j\delta\) are centered at \(s_j+\delta/2\) and \(s_j-\delta/2\), respectively. Taylor subtraction therefore yields, uniformly in \(j\),
\[
\boxed{\displaystyle
\beta_{j,m}=\delta\kappa(s_j)+\frac{\delta^3}{12}\kappa''(s_j)+O_{\gamma}(\delta^5).}
\tag{4}
\]
Strict convexity guarantees that the differences of chord-direction angles are the genuine positive exterior turns when \(m\) is sufficiently large.

**3. Expansion and periodic summation.** The even analytic function \(H\) satisfies
\[
H(z)=\frac{z^2}{6}+\frac{7z^4}{360}+O(z^6),\qquad z\to0.
\]
Inserting (4), uniformly in the vertices, gives
\[
H(\beta_{j,m})=\frac{\delta^2}{6}\kappa(s_j)^2
+\delta^4\left(\frac{\kappa(s_j)\kappa''(s_j)}{36}
+\frac{7\kappa(s_j)^4}{360}\right)+O_{\gamma}(\delta^6).
\]
For a periodic \(\mathrm C^4\) function \(g\), the periodic trapezoidal rule satisfies \(\delta\sum_{j=0}^{m-1}g(j\delta)=\int_0^L g(s)\,ds+O_g(\delta^4)\). For the second integrand, the weaker \(O(\delta^2)\) quadrature bound suffices. Multiply the sum of the preceding vertex expansions by \(m=L/\delta\), apply these bounds, and integrate by parts around the closed curve:
\[
\int_0^L\kappa\kappa''\,ds=-\int_0^L(\kappa')^2\,ds.
\]
Since \(\delta=L/m\), this proves (1) with the stated \(O_{\gamma}(m^{-4})\) remainder.

**4. Identical curvature histograms but opposite second corrections.** For the displayed support functions, \(\rho_p=h_p+h_p''=1+\frac12\cos(p\theta)\) is their positive radius of curvature and \(ds=\rho_p\,d\theta\), \(\kappa=1/\rho_p\). The parametrized curve is \(\gamma_p(\theta)=h_p(\theta)(\cos\theta,\sin\theta)+h_p'(\theta)(-\sin\theta,\cos\theta)\). It is closed and strictly convex because \(\rho_p>0\). Its length is \(\int_0^{2\pi}\rho_p\,d\theta=2\pi\). For any integrable observable \(f\),
\[
\int f(\kappa)\,ds=\int_0^{2\pi} f\left(\frac1{1+\frac12\cos(p\theta)}\right)
\left(1+\frac12\cos(p\theta)\right)d\theta,
\]
which is independent of the integer \(p\), by periodic substitution. In contrast,
\[
\int(\kappa')^2\,ds
=\int_0^{2\pi}\frac{(\rho_p'(\theta))^2}{\rho_p(\theta)^5}\,d\theta
=p^2\int_0^{2\pi}\frac{\frac14\sin^2u}{(1+\frac12\cos u)^5}\,du.
\]
Elementary periodic integration (e.g. differentiating the integral of \((1+e\cos\theta)^{-3}\) in \(e\)) gives
\[
\int\kappa^2 ds=\frac{4\pi}{\sqrt3},\quad
\int\kappa^4 ds=\frac{8\sqrt3\pi}{3},\quad
\int(\kappa')^2 ds=p^2\frac{34\sqrt3\pi}{81}.
\]
Substitution of these expressions and \(L=2\pi\) into (1) proves (2). The sign changes because \(378-85(2)^2=38>0\), whereas \(378-85(3)^2=-387<0\).

## Verification

The included standard-library Python program `verify.py` constructs the equal-arclength inscribed polygons directly from the two support functions by solving \(s=\theta+\sin(p\theta)/(2p)\), calculates each vertex's exterior turning angle from successive edges, and computes \(\Lambda_m\). For \(p=2,3\), each of the five sample sizes \(m=64,128,256,512,1024\) shows convergent second-coefficient estimates toward the distinct exact values from (2), with terminal absolute errors below \(0.03\). It independently checks two periodic integrals appearing in the proof and the unit-circle special case, where \(m\Lambda_m=m^2[(2\pi/m)/\sin(2\pi/m)-1]\). Running `python3 verify.py` produces `VERIFY_OK`. These tests check numerical normalization, signs, and representative cases, but do not replace the uniform Taylor proof or certify bibliographic uniqueness.

## Relationship to prior work

The exact short-radius polygonal identity (3) and its angular rigidity are established earlier and are used here only as an ingredient. Classical random-chord treatments for regular polygons, such as Bäsel [1], concern invariant-random lines or area-uniform random points rather than the successive equal-arclength polygon sampling limit. Iglesias and Bruckstein [2] investigate convergence of polygonal curvature energies toward elastica; the available abstract states convergence results but does not state the specific turning functional, the explicit \(m^{-2}\) correction, or its curvature-histogram counterexample. Scholtes, Schumacher, and Wardetzky [3] develop variational convergence for discrete bending energy, rather than the displayed boundary-distance observable. An inspected published polygonal short-pair formula for area-uniform interior points [4] is a different probability law and does not imply (1). The additional information established here is the exact second-order continuum term, its sign-sensitive \((\kappa')^2\) contribution, and the equal-histogram frequency separation.

## Limitations

Only simple closed positively curved \(\mathrm C^8\) planar curves, with equally spaced arclength vertices, are proved to satisfy the stated error estimate. No finite-\(m\) monotonicity, statistical inference rate, joint radius/mesh asymptotic, or optimal regularity is claimed. The local polygonal identity is not new. A plausible earlier specialist paper on discrete polygonal curvature functionals [2] could be inspected only through its abstract because full text was unavailable; equivalent earlier second-order formulas remain a bibliographic risk. Independent scholarly validation has not been performed.

## References

1. Uwe Bäsel, *Random chords and point distances in regular polygons*, first public arXiv preprint 12 April 2012, https://arxiv.org/abs/1204.2707.
2. José A. Iglesias and Alfred M. Bruckstein, *On the Gamma-convergence of some polygonal curvature functionals*, first published online 6 June 2014, https://doi.org/10.1080/00036811.2014.910302.
3. Sebastian Scholtes, Henrik Schumacher, and Max Wardetzky, *Variational Convergence of Discrete Elasticae*, first public preprint 8 January 2019, https://arxiv.org/abs/1901.02228.
4. *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, published mathematical record `24e8bcd8655b` (interior-area sampling).
5. *An exact polygonal shortcut law and sharp angular stability*, prior mathematical record `b7f8e5bf-9498-4bcc-843d-f79a05558fbe` (the local boundary-corner identity).

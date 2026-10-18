# An interior logarithmic caustic in random brightness of the cubic threefold-projection body

## Finding
Let \(K_\varepsilon\subset\mathbb R^3\) be the constant-width convex body with support function
\[
h_\varepsilon(u)=1+\varepsilon u_1u_2u_3,\qquad u\in S^2,
\]
where \(0<|\varepsilon|\le3\sqrt6/8\). For a Haar-uniform unit vector \(N\), write \(B_\varepsilon(N)=\operatorname{area}_2(K_\varepsilon\mid N^\perp)\), and normalize its random brightness deficit by
\[
Y=\frac{4(\pi-B_\varepsilon(N))}{\pi\varepsilon^2}.
\]
Then \(Y\) has a parameter-independent, absolutely continuous law supported on \([0,8/27]\). Put
\[
L(s)=s(1-s),\qquad U(s)=\frac{(1-s)(1+s)^2}{4}.
\]
At every \(0<y<8/27\), except \(y=1/4\), its density is the convergent improper integral
\[
\boxed{f_Y(y)=\frac1{2\pi}\int_{\substack{0<s<1\\L(s)<y<U(s)}}
\frac{ds}{\sqrt{s}\sqrt{y-L(s)}\sqrt{U(s)-y}}.}
\]
Its sole interior density singularity occurs at \(y=1/4\), with the **exact logarithmic coefficient**
\[
\boxed{f_Y(1/4+\eta)=\frac6\pi\log\frac1{|\eta|}+O(1)\qquad(\eta\to0,\ \eta\ne0).}
\]
The two endpoint tails have different finite, nonzero slopes:
\[
\boxed{\mathbb P(Y\le y)=\frac32y+o(y)\quad(y\downarrow0),\qquad
\mathbb P(Y\ge8/27-\delta)=\frac92\delta+o(\delta)\quad(\delta\downarrow0).}
\]
Moreover,
\[
\boxed{\mathbb EY=\frac4{21},\qquad
\operatorname{Var}(Y)=\frac{400}{63063}.}
\]
For \(\varepsilon\ne0\), the internal singularity of the ordinary brightness density is at the area \(\pi(1-\varepsilon^2/16)\). It is not an atom: the law is absolutely continuous. In contrast, the separately studied axial cubic threefold-projection body has a random-brightness density singular only at its endpoints.

## Assumptions and scope
All areas are Euclidean orthogonal-projection areas in three dimensions; Haar measure on \(S^2\) is a probability measure. The specified parameter interval is the previously established sharp support-function interval for this particular cubic. The endpoint is allowed, although a principal curvature radius can vanish there. The normalization of \(Y\) excludes \(\varepsilon=0\), at which the body is the Euclidean unit ball and brightness is constant. Opposite unit normals define the same projection plane; this does not change the distribution.

## Proof
**1. Brightness reduction.** The existing exact directional-brightness identity for this body, also recovered directly from its circle harmonics, is
\[
B_\varepsilon(n)=\pi-\frac{\pi\varepsilon^2}{4}
\prod_{i=1}^3(1-n_i^2).
\]
To see its normalization, write a great circle perpendicular to \(n\) as \(u(\theta)=e_1\cos\theta+e_2\sin\theta\) with \(e_1,e_2\) orthonormal, and put \(z=e_1-i e_2\). The cubic restricted to this circle has only first and third harmonics; its third-harmonic amplitude squared is \(|z_1z_2z_3|^2/16=\prod_i(1-n_i^2)/16\). Removing the translation-producing first harmonic and integrating \(\tfrac12\int_0^{2\pi}(p^2-(p')^2)d\theta\) yields the displayed area. Consequently
\[
Y=\prod_{i=1}^3(1-X_i),\qquad X_i=N_i^2.
\]
Independent standard Gaussian coordinates divided by their Euclidean norm show that \((X_1,X_2,X_3)\) has the Dirichlet distribution with parameters \((1/2,1/2,1/2)\), with density \((2\pi\sqrt{x_1x_2x_3})^{-1}\) on \(x_i>0\), \(\sum_i x_i=1\). The arithmetic-geometric mean inequality gives the exact range \([0,8/27]\), whose upper endpoint is attained only at \(x_i=1/3\); its zeros are the three simplex vertices.

**2. Exact one-dimensional law.** Set \(S=X_1\). Then \(S\) has density \((2\sqrt{s})^{-1}\) on \((0,1)\). Independently conditional on \(S=s\), the ratio \(T=X_2/(1-s)\) has density \(1/(\pi\sqrt{t(1-t)})\) on \((0,1)\). A direct substitution gives
\[
Y=L(s)+(1-s)^3T(1-T)
=L(s)+[U(s)-L(s)]\,4T(1-T).
\]
Since \(4T(1-T)\) is again \(\operatorname{Beta}(1/2,1/2)\), the conditional law of \(Y\) is arcsine on \([L(s),U(s)]\). Integrating its conditional density against \((2\sqrt{s})^{-1}\) proves the displayed formula. Each conditional distribution is nonatomic, so the mixture is absolutely continuous. The only interior critical value is \(1/4\): on the simplex the gradient of \(Y\) vanishes only at \((1/3,1/3,1/3)\), its global maximum, whereas the three edges have respective maxima \(1/4\) at their midpoints. Standard local changes of variables therefore give a smooth density away from this value and the endpoints.

**3. Exact interior logarithmic coefficient.** Use coordinates in a neighborhood of the midpoint of the face \(X_1=0\):
\[
X_1=s,\quad X_2=(1-s)/2+t,\quad X_3=(1-s)/2-t.
\]
This parametrization has unit Jacobian in the simplex coordinates \((X_1,X_2)\). The Dirichlet probability density and the polynomial level function are exactly
\[
\frac{1}{2\pi\sqrt{s}\sqrt{(1-s)^2/4-t^2}}\,ds\,dt,
\qquad
Y=\frac14+\frac s4-\frac{s^2+s^3}{4}-t^2+st^2.
\]
Thus the measure equals \((\pi\sqrt s)^{-1}(1+O(s+t^2))\,ds\,dt\). The smooth, locally invertible normal coordinate
\[
q=s\left(\frac14-\frac s4-\frac{s^2}{4}+t^2\right)
\]
is positive for \(s>0\) sufficiently small, has derivative \(\partial_s q(0,0)=1/4\), and gives the **exact** normal form \(Y-1/4=q-t^2\). Its transformed measure is
\[
\frac2{\pi\sqrt q}\bigl(1+O(q+t^2)\bigr)\,dq\,dt.
\]
The leading contribution to the density at \(1/4+\eta\) is therefore
\[
\frac2\pi\int_{\substack{|t|<c\\t^2+\eta>0}}
\frac{dt}{\sqrt{t^2+\eta}}
=\frac2\pi\log\frac1{|\eta|}+O(1).
\]
For \(\eta>0\), this is obtained from an inverse hyperbolic sine; for \(\eta<0\), from an inverse hyperbolic cosine with \(|t|>\sqrt{-\eta}\). The smooth-error term and chart boundaries contribute \(O(1)\), including the small shift of the transformed chart boundaries. By permutation symmetry there are precisely three such boundary midpoints, each with this same coefficient. On the complement of their neighborhoods the level map is regular at \(1/4\), and the remaining integrable simplex-edge weights contribute boundedly to the pushforward density. The three coefficients add to \(6/\pi\), proving the two-sided logarithmic law.

**4. Endpoint tails.** At a simplex vertex, say \(X_1=1\), let \(R=1-X_1\). It has \(\operatorname{Beta}(1,1/2)\) density \((2\sqrt{1-r})^{-1}\), hence \(\mathbb P(R\le r)=r/2+O(r^2)\). Since \(Y=R+O(R^2)\) uniformly over the conditional split of \(R\) between \(X_2,X_3\), that vertex contributes \(y/2+o(y)\) to \(\mathbb P(Y\le y)\). The three vertices exhaust the zero set and have disjoint neighborhoods, giving \(3y/2+o(y)\).

For the upper endpoint, write \(X_1=1/3+u\), \(X_2=1/3+v\), \(X_3=1/3-u-v\). The **exact** expansion is
\[
Y=\frac8{27}-\frac23(u^2+uv+v^2)+uv(u+v).
\]
The simplex-coordinate density at the center is \(3\sqrt3/(2\pi)\). The ellipse \((2/3)(u^2+uv+v^2)<\delta\) has area \(\pi\sqrt3\,\delta\), so the upper tail is \((9/2)\delta+o(\delta)\). There are no other maximizers.

**5. Moments.** The identity \(Y=X_1X_2+X_1X_3+X_2X_3-X_1X_2X_3\) and the Dirichlet moment formula
\[
\mathbb E\prod_{i=1}^3 X_i^{a_i}=
\frac{\prod_{i=1}^3(1/2)_{a_i}}{(3/2)_{a_1+a_2+a_3}}
\]
for nonnegative integers \(a_i\) give \(\mathbb EY=4/21\) and \(\mathbb EY^2=128/3003\). Subtracting the square of the mean yields \(\operatorname{Var}(Y)=400/63063\). Thus \(\mathbb EB_\varepsilon=\pi(1-\varepsilon^2/21)\) and \(\operatorname{Var}(B_\varepsilon)=25\pi^2\varepsilon^4/63063\).

## Verification
Run `python3 verify.py` using the standalone standard-library checker included here. It independently evaluates the Dirichlet moments by rational arithmetic, confirms both exact local Taylor polynomials, verifies the normal-coordinate identity and its Jacobian at the caustic, and compares the first two moments against deterministic-seed Gaussian-direction simulation. The density integral was independently evaluated numerically on both sides of \(1/4\); its increment for each factor-of-ten approach is consistent with the predicted \((6/\pi)\log10\) growth. Numerical data are not substituted for the analytic normal-form and endpoint proofs.

## Relationship to prior work
Myroshnychenko, Ryabogin and Saroglou (2026, Proposition 5.1 and Theorem 5.4) introduce the cubic constant-width exception and its threefold symmetric projections. The published *Exact brightness profile of the cubic threefold-projection exception* supplies the all-direction product formula used in Step 1, but does not state the Haar pushforward law or analyze its interior singularity. The published *Sharp convexity threshold for the cubic constant-width support family* supplies the exact admissible parameter interval but no random-direction distribution. The published *Exact projection-body volume and random-brightness law for axial cubic bodies* concerns the inequivalent zonal harmonic with an elementary density possessing only endpoint singularities; it does not imply the non-axial logarithmic caustic. Abas (2026) develops distributions for polyhedral brightness and width and supplies related general integral-geometric context, but its publicly inspected abstract does not settle this smooth cubic case. The new content is the exact conditional-arcsine mixture and especially its nontrivial two-sided interior logarithmic coefficient and endpoint slopes.

## Limitations
This is a distribution theorem for one specific non-axial degree-three support harmonic, not a classification of all threefold-projection bodies. It does not imply a general density law for arbitrary constant-width bodies, and it does not prove that random-brightness data uniquely identify this body among all convex bodies. The previously published directionwise brightness identity is an explicit premise and not a new claim here. The full 92-page Abas manuscript was not materially inspected; an unindexed equivalent calculation under probabilistic terminology remains a priority risk. None of the simulation or finite symbolic checks proves the analytic asymptotics by itself.

## References
1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1 (first public 2026-09-23), https://arxiv.org/abs/2609.27192.
2. *Exact brightness profile of the cubic threefold-projection exception* (2026), publicly available mathematical finding.
3. *Sharp convexity threshold for the cubic constant-width support family* (2026), publicly available mathematical finding.
4. *Exact projection-body volume and random-brightness law for axial cubic bodies* (2026), publicly available mathematical finding.
5. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1 (first public 2026-08-10), https://arxiv.org/abs/2609.26202.
6. R. Schneider and W. Weil, *Stochastic and Integral Geometry*, Springer, 2008, for spherical Haar and Dirichlet distributions.

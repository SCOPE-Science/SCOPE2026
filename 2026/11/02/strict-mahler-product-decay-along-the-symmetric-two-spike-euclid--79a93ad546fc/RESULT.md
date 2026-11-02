# Strict Mahler-product decay along the symmetric two-spike Euclidean-ball family

## Finding

For an integer \(d\ge2\) and \(a\ge1\), consider the centrally symmetric convex body
\[
K_{d,a}=\operatorname{conv}\!\bigl(B_2^d\cup\{-ae_1,ae_1\}\bigr)\subset\mathbb R^d.
\]
Write \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), \(t=1/a\), and
\[
I_d(t)=\int_0^t(1-s^2)^{(d-1)/2}\,ds.
\]
Its Mahler (polar-volume) product has the exact formula
\[
\mathcal P_d(a)=\operatorname{vol}_d(K_{d,a})\operatorname{vol}_d(K_{d,a}^{\circ})
=4\kappa_{d-1}^{2} I_d(t)\left[I_d(t)+\frac{(1-t^2)^{(d+1)/2}}{dt}\right].
\]
**The function \(a\mapsto\mathcal P_d(a)\) is strictly decreasing on \([1,\infty)\)**. In particular, every finite \(a>1\) satisfies the sharp inequalities
\[
\boxed{\frac{4\kappa_{d-1}^{2}}{d}<\mathcal P_d(a)<\kappa_d^{2}}.
\]
The upper value is attained only at the ball \(a=1\); the lower value is not attained for finite \(a\), and arises in the rescaled double-cone limit. Quantitatively,
\[
\mathcal P_d(a)=\frac{4\kappa_{d-1}^{2}}{d}
\left[1+\frac{d-1}{3a^2}+O_d(a^{-4})\right]\quad(a\to\infty).
\]
In dimension three, the entire profile is the exact quartic
\[
\boxed{\mathcal P_3(a)=\frac{4\pi^2}{9}\left(3+\frac2{a^2}-\frac1{a^4}\right).}
\]
For every odd dimension \(d=2m+1\ge3\), the product is a polynomial in \(a^{-2}\) with rational coefficients multiplied by \(4\kappa_{2m}^2\); an explicit polynomial is given below.

## Assumptions and scope

\(B_2^d\) is the closed Euclidean unit ball, \(e_1\) its first coordinate unit vector, and \(K^\circ=\{y:\langle x,y\rangle\le1\ \forall x\in K\}\) is the polar with respect to the origin. The body \(K_{d,a}\) has nonempty interior for every \(d\ge2\), \(a\ge1\). By symmetry, the origin is its Santaló point, so the displayed product is also its Santaló volume product. All limits and strict inequalities refer to fixed integer dimension \(d\ge2\).

## Proof

**1. Polarity and cross-sections.** Since taking polars reverses convex hulls and unions, direct evaluation of the support constraints gives
\[
K_{d,a}^{\circ}=B_2^d\cap\{y:|y_1|\le1/a\}.
\]
Writing \(z=|y_1|\), the polar sections are \((d-1)\)-balls of radius \(\sqrt{1-z^2}\), hence
\[
\operatorname{vol}_d(K_{d,a}^\circ)=2\kappa_{d-1}I_d(t).
\]
For \(a>1\), the line segment from the axial vertex \((a,0)\) tangent to the meridional unit disk touches that circle at axial coordinate \(t=1/a\). Consequently the radial extent of the primal body at height \(z=|x_1|\) is exactly
\[
r(z)=\begin{cases}
\sqrt{1-z^2},&0\le z\le t,\\
(1-tz)/\sqrt{1-t^2},&t\le z\le1/t.
\end{cases}
\]
These sections are centered Euclidean \((d-1)\)-balls, not merely upper bounds: rotational symmetry and convexity of the hull give the full sections. Integration yields
\[
\begin{aligned}
\operatorname{vol}_d(K_{d,a})
&=2\kappa_{d-1}\left[I_d(t)+\int_t^{1/t}
\left(\frac{1-tz}{\sqrt{1-t^2}}\right)^{d-1}\,dz\right]\\
&=2\kappa_{d-1}\left[I_d(t)+\frac{(1-t^2)^{(d+1)/2}}{dt}\right].
\end{aligned}
\]
Multiplication proves the displayed exact formula for \(a>1\). Its continuous extension to \(a=1\) gives the unit ball.

**2. Strict monotonicity.** Put \(f(s)=(1-s^2)^{(d-1)/2}\), \(I=I_d(t)\), \(J(t)=\int_0^t s^2 f(s)\,ds\), and \(H=(1-t^2)^{(d+1)/2}/(dt)\). For \(0<t<1\), direct differentiation gives
\[
I'=f,\qquad H'=-f\left(1+\frac1{dt^2}\right),\qquad
\frac{d}{dt}\frac{\mathcal P_d(1/t)}{4\kappa_{d-1}^2}
=f\left[I+H-\frac{I}{dt^2}\right].
\]
A second direct derivative, with the equality at \(t=0\), gives the exact integration identity
\[
I-t(1-t^2)f(t)=(d+2)J(t).
\]
Since \(H=(1-t^2)f(t)/(dt)\), the bracket above equals
\[
S(t)=I-\frac{d+2}{dt^2}J(t).
\]
The function \(s^2\) is strictly increasing and \(f(s)\) is strictly decreasing on \((0,t)\) for every \(d\ge2\); the strict reversed Chebyshev integral inequality therefore yields
\[
J(t)<\frac{t^2}{3}I(t),\qquad
S(t)>\frac{2(d-1)}{3d}I(t)>0.
\]
Thus \(d\mathcal P_d(1/t)/dt>0\) for \(0<t<1\), and \(\mathcal P_d(a)\) strictly decreases with \(a>1\). Continuity gives strict comparison with \(a=1\) as well.

**3. Endpoints and rate.** As \(t\downarrow0\), Taylor expansion gives
\[
I=t-\frac{d-1}{6}t^3+O_d(t^5),\qquad
H=\frac{1}{dt}-\frac{d+1}{2d}t+O_d(t^3),
\]
and hence \(I(I+H)=1/d+(d-1)t^2/(3d)+O_d(t^4)\). At \(t=1\), \(H=0\) and \(2\kappa_{d-1}I_d(1)=\kappa_d\). The two strict bounds and the asymptotic expansion follow.

**4. Special dimensions.** When \(d=3\), \(I_3=t-t^3/3\) and \(H_3=(1-t^2)^2/(3t)\). Their product simplifies exactly to \((3+2t^2-t^4)/9\). More generally, if \(d=2m+1\), put \(s=t^2\) and
\[
Q_m(s)=\sum_{j=0}^m\frac{(-1)^j\binom mj}{2j+1}s^j.
\]
Then \(I_d(t)=tQ_m(s)\) and
\[
\frac{\mathcal P_d(a)}{4\kappa_{2m}^2}
=Q_m(s)\left[sQ_m(s)+\frac{(1-s)^{m+1}}{2m+1}\right],\quad s=a^{-2}.
\]
This is a polynomial with rational coefficients for every odd dimension.

## Verification

A standalone standard-library program `verify.py` independently integrates the piecewise meridional sections by Simpson quadrature, compares them with the closed product formula, checks strict monotonicity for dimensions \(2,3,4,5,8\), verifies the three-dimensional polynomial and a rational derivative identity, and tests the large-spike asymptotic. Its reported finite tests corroborate but do not prove the universal theorem. The complete proof is the cross-section identity and strict Chebyshev argument above.

## Relationship to prior work

The polar-volume product is classical. Meyer and Reisner (2006) developed a general convexity theorem for reciprocal polar volume in shadow systems. That result concerns \(1/\operatorname{vol}(K_t^\circ)\), not the sign of the derivative of the **product** \(\operatorname{vol}(K_t)\operatorname{vol}(K_t^\circ)\) for the specific smooth-core, two-spike family here; no implication establishing the stated formula or strict monotonicity was identified in the accessible text. Hu Yan (2012), Theorems 1–2 and Section 4, studied generalized cylinders and bodies of revolution with power-law meridional profiles \(|z|^p+r^p\le1\); the present family instead has a spherical central band and linear conical tails. Its double-cone endpoint overlaps the established bicone/cylinder volume product, but not the intermediate exact strict law. Lin and Leng (2014) give a general three-dimensional minimum bound among centrally symmetric bodies of revolution, which does not provide this all-dimensional strict one-parameter profile. These are statement/implication comparisons, not priority certification.

## Limitations

The argument requires two **equal antipodal** added vertices and a Euclidean ball; it asserts nothing about asymmetric spikes, ellipsoids under different spike directions, or general shadow systems. The finite asymptotic lower limit is not achieved for any finite spike length. An earlier, unindexed computation of this particular one-parameter product may exist; the accessible 2006 and 2014 abstract-level source material does not rule that out. No independent external validation has been performed.

## References

1. M. Meyer and S. Reisner, *Shadow systems and volume of polar convex bodies*, preprint arXiv:math/0606305 (first posted 2006-06-13), subsequently *Mathematika* 53 (2006), 129–148. https://arxiv.org/abs/math/0606305
2. H. Yan, research article on Mahler volume of bodies of revolution in \(\mathbb R^3\), *Journal of Inequalities and Applications* 2012, article 3, published 2012-01-09. https://doi.org/10.1186/1029-242X-2012-3
3. Y. Lin and G. Leng, *Origin-Symmetric Bodies of Revolution with Minimal Mahler Volume in \(\mathbb R^3\)—a new proof*, arXiv:1403.0322 (first posted 2014-03-03). https://arxiv.org/abs/1403.0322

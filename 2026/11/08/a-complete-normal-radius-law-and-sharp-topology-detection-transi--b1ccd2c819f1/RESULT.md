# A complete normal-radius law and sharp topology-detection transition for flat Möbius bands

## Finding

An area-uniform point on a flat Möbius band has an exact, explicitly piecewise distribution of its largest **boundary-free injective exponential disk**. That one-dimensional law has a sharp information transition: it cannot distinguish a Möbius strip from an untwisted cylinder when the half-width is at most half the horizontal period, but it reconstructs both shape parameters **and** distinguishes their topology once the half-width passes that threshold. A new square-root singularity and an eventual atom distinguish the nonorientable case. The maximal disk radius exhibits three exact regimes, including a topology-driven advantage of as much as a factor of two over the matched cylinder.

## Assumptions and scope

Fix \(a,b>0\). Write \(S=\mathbb R\times[-b,b]\) with Euclidean metric. The flat Möbius band \(M_{a,b}\) is the quotient by the glide reflection \(g(x,y)=(x+a,-y)\); the flat cylinder \(C_{a,b}\) is the quotient by \(h(x,y)=(x+a,y)\). Both have area \(2ab\). Let \(P\) be uniformly distributed by normalized two-dimensional area; boundary points have probability zero.

For every interior \(p\), \(R(p)\) is the supremum of those \(r>0\) for which the geodesic exponential map restricted to the open Euclidean disk \(B_r(0)\subset T_p\) is defined entirely before the surface boundary and is injective. In a flat quotient this map is a local isometry and its image is an embedded flat normal disk. **Do not confuse** this invariant with the strong-convexity radius or require that ambient distances between all points in the disk equal their planar distances.

Let \(S_M(r)=\Pr\{R_M\ge r\}\) and \(S_C(r)=\Pr\{R_C\ge r\}\). Write \((x)_+=\max\{x,0\}\). For every \(r\ge0\),

\[
S_C(r)=\begin{cases}(1-r/b)_+,&0\le r\le a/2,\\0,&r>a/2,\end{cases}
\qquad
S_M(r)=\begin{cases}(1-r/b)_+,&0\le r\le a/2,\\(b-r-\sqrt{r^2-a^2/4})_+/b,&a/2<r\le a,\\0,&r>a.\end{cases}
\]

At a jump, the \(\ge\) convention specifies the value at the atom. Both laws have support in \([0,\infty)\). For \(b>a/2\), the Möbius CDF just above \(a/2\) satisfies
\[
\Pr\{R_M\le a/2+\varepsilon\}
=\frac{a}{2b}+\frac{\sqrt a}{b}\sqrt\varepsilon+O_{a,b}(\varepsilon),
\quad\varepsilon\downarrow0.
\]
The cylinder instead has an atom \(\Pr\{R_C=a/2\}=1-a/(2b)\). The Möbius law has no atom at \(a/2\). For \(b>(1+\sqrt3/2)a\), it has an atom of size \((b-a-\sqrt3a/2)/b\) at \(a\); there is no such atom below or at that threshold.

The maximal radius over centers in \(M_{a,b}\) is
\[
R_M^{\max}=\begin{cases}
b,&b\le a/2,\\
\frac b2+\frac{a^2}{8b},&a/2<b<(1+\sqrt3/2)a,\\
a,&b\ge(1+\sqrt3/2)a.
\end{cases}
\]
The maximizing centers have \(|y|=0\) in the first regime, \(|y|=b/2-a^2/(8b)\) in the middle regime, and \(\sqrt3a/2\le|y|\le b-a\) in the last regime (including the threshold singleton). For the matched cylinder, \(R_C^{\max}=\min(b,a/2)\).

Within the disjoint union of these two-parameter families, the distribution is uniform on \([0,b]\) **if and only if** \(b\le a/2\), and in this narrow regime all \(a\ge2b\) and either topology have the same law. Otherwise the infinitesimal CDF slope at zero is \(1/b\), while the first interior cusp (Möbius) or jump (cylinder) is at \(a/2\), so the law recovers \(a,b\) and the class. For fixed \(a,b\), \(R_M\) first-order stochastically dominates \(R_C\); their distributions are unequal exactly when \(b>a/2\).

## Proof

**1. The injectivity bottlenecks.** In the universal strip a lift of a center has coordinates \((x,y)\). Its open planar radius-\(r\) disk lies inside the strip exactly when \(r\le b-|y|\). It projects injectively to the quotient precisely when it is disjoint from all its nontrivial deck translates. An isometric deck transformation takes the disk to the equal-radius disk centered at the transformed lift, so two such disks are disjoint for all nontrivial deck transformations exactly when \(2r\) is at most the distance to the nearest distinct deck image. This criterion is both necessary and sufficient; there is no conjugate-point obstruction in the flat strip.

For the cylinder, nonzero images lie at \((x+ka,y)\) and the nearest distance is \(a\). For the Möbius band, \(g^k(x,y)=(x+ka,(-1)^k y)\). Even nonzero \(k\) give minimal distance \(2a\), while odd \(k\) give minimal distance \(\sqrt{a^2+4y^2}\). Consequently, for every interior center,
\[
R_C(x,y)=\min\{b-|y|,a/2\},\qquad
R_M(x,y)=\min\{b-|y|,a,\tfrac12\sqrt{a^2+4y^2}\}.
\]
The \(a\) term from the twice-around translation is essential in the thick regime.

**2. Exact distribution.** In the fundamental rectangle \(x\in[0,a)\), \(y\in[-b,b]\), normalized area makes \(|y|\) uniform on \([0,b]\). Thus for \(0\le r\le a/2\), \(R_M\ge r\) exactly when \(|y|\le b-r\); this is also the cylinder condition. For \(a/2<r\le a\), the Möbius inequality additionally requires \(|y|\ge\sqrt{r^2-a^2/4}\). Its feasible interval is
\[
\sqrt{r^2-a^2/4}\le|y|\le b-r,
\]
whose normalized length is the second line of \(S_M\). At \(r>a\), the even deck translation precludes injectivity. For the cylinder, \(r>a/2\) is impossible. This proves both exact laws including the correct endpoint conventions.

**3. The two singularities.** For \(b>a/2\), put \(r=a/2+\varepsilon\). The square root in the CDF is
\[
\sqrt{r^2-a^2/4}=\sqrt{a\varepsilon+\varepsilon^2}=\sqrt a\,\sqrt\varepsilon+O_a(\varepsilon^{3/2}).
\]
The feasibility interval remains nonempty for sufficiently small positive \(\varepsilon\); the displayed cusp follows. Unlike the continuous Möbius cusp, the cylinder has a positive-measure plateau \(R_C=a/2\) on \(|y|\le b-a/2\). The Möbius event \(R_M=a\) is equivalent to \(\sqrt3a/2\le|y|\le b-a\), yielding precisely the stated atom and its sharp threshold.

**4. Sharp maximization.** For nonnegative \(y\), the function \(b-y\) decreases, \(\sqrt{a^2+4y^2}/2\) increases, and the even-deck ceiling equals \(a\). If \(b\le a/2\), the maximum is \(b\) at \(y=0\). If \(b>a/2\), the two variable barriers meet uniquely at
\[
y_*=\frac b2-\frac{a^2}{8b},\qquad r_*=b-y_*=\frac b2+\frac{a^2}{8b}.
\]
The intersection is active exactly when \(r_*\le a\), equivalently \(b\le(1+\sqrt3/2)a\) in the current \(b>a/2\) regime. Beyond that threshold, the constant ceiling \(a\) is reached on \(\sqrt3a/2\le y\le b-a\). This proves all maximizer cases.

**5. Inverse classification and stochastic comparison.** When \(b\le a/2\), the pointwise radius is simply \(b-|y|\) in both models, hence its distribution is uniform on \([0,b]\) and conceals the period and topology. For \(b>a/2\), \(b\) is determined by the small-radius CDF slope \(1/b\), and \(a/2\) by the first nonanalytic point (a square-root cusp for the Möbius case; a jump for the cylinder). These singularities cannot agree, and therefore every nonuniform law uniquely determines both parameters and the model class. Finally, the pointwise comparison
\[
\min\{b-|y|,a,\sqrt{a^2+4y^2}/2\}\ge\min\{b-|y|,a/2\}
\]
proves first-order stochastic dominance. If \(b>a/2\), an open positive-measure interval of \(y>0\) has strict inequality, while if \(b\le a/2\) there is equality for every \(y\).

## Verification

The standalone pure-Python program `verify.py` checks the pointwise formula against a fresh enumeration of all deck transformations with \(|k|\le12\), which is exhaustive for the two deck-image minima by the parity argument above. It also checks the analytical survival distribution against deterministic quadrature over \(10{,}000\) center ordinates for multiple values of \(a,b,r\), checks endpoint and threshold regimes, and checks the exact maximum against an independent grid optimization. Successful execution prints `FLAT_QUOTIENT_LOCAL_NORMAL_RADIUS_OK 72`. Numerical grids corroborate but are not substitutes for the analytic proof. Run `python3 verify.py`; no third-party dependencies are required.

## Relationship to prior work

Croke and Herreros (2011 preprint) prove lens-data rigidity for flat cylinders and Möbius bands; their §3 argument uses the orientation double cover. Their theorems do **not** provide the uniform-area pushforward of the normal injectivity radius, the square-root versus atom transition, or reconstruction from this one-dimensional statistic. Dibble (2014 preprint; 2010 MSC primary 53C20) studies general injectivity and convexity radii and explicitly distinguishes the two notions. The present exact quotient-image computation is compatible with such general facts, but does not claim the standard exponential-map definition or shortest-loop criterion as new. The relevant published geometry does not imply this **single-statistic** reconstruction from lens rigidity alone without the explicit law and inverse argument.

## Limitations

This is a result for rectangular **intrinsic** flat metrics and normalized area sampling, not the geometry of a physically embedded paper strip in three-dimensional space. It does not imply that each normal disk is strongly convex in the ambient shortest-path metric. A general flat Möbius metric with nongeodesic boundary is outside scope. The inverse is only within the specified cylinder/Möbius families; an arbitrary surface need not be determined by its radius distribution. Historical-priority searches do not exclude unindexed older equivalent results. Independent audit has not been performed.

## References

- C. B. Croke and P. Herreros, *Lens rigidity with trapped geodesics in two dimensions*, arXiv:1108.4938, first public version 24 August 2011; later Asian Journal of Mathematics 20 (2016), 47–58. https://arxiv.org/abs/1108.4938
- J. Dibble, *The convexity radius of a Riemannian manifold*, arXiv:1412.0341, initial public version 1 December 2014, primary 2010 MSC 53C20. https://arxiv.org/abs/1412.0341

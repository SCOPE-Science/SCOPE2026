# Exact logarithmic section-length law for the orthogonal spherical lune

## Finding

Let \(S^2\) be the unit sphere with its intrinsic curvature-one geodesic metric. Define the **orthogonal spherical lune**
\[
W=\{(x,y,z)\in S^2:x\ge 0,\ y\ge 0\}.
\]
Take a Haar-uniform unoriented great circle \(G\), and write \(L\) for the geodesic length of the arc \(G\cap W\). Then \(0<L<\pi\) almost surely and its complete distribution function is
\[
\boxed{\mathbb P(L\le t)=\frac{t+\cot t\log|\cos t|}{\pi}},\quad 0<t<\pi,\quad t\ne\frac\pi2.
\]
The continuous extension at \(t=\pi/2\) is \(1/2\); outside \((0,\pi)\) the CDF is respectively zero or one. The probability density on \((0,\pi)\setminus\{\pi/2\}\) is
\[
\boxed{f_L(t)=\frac{-\log|\cos t|}{\pi\sin^2 t}}.
\]
The density is symmetric about \(\pi/2\), strictly increases up to that point and strictly decreases afterward. It has endpoint limits \(1/(2\pi)\), an integrable logarithmic divergence at \(\pi/2\), and no point mass. In particular \(\mathbb E L=\pi/2\), and both the mean and the unique median are \(\pi/2\). More precisely, as \(\varepsilon\downarrow0\),
\[
\mathbb P\!\left(\left|L-\frac\pi2\right|<\varepsilon\right)
=\frac{2\varepsilon}{\pi}(1-\log\varepsilon)+O(\varepsilon^3|\log\varepsilon|).
\]

## Assumptions and scope

The orientation is chosen by Haar measure on the space of unoriented two-dimensional linear subspaces of \(\mathbb R^3\): equivalently, take a unit normal uniformly on \(S^2\) and identify antipodal normals. The lune is the intersection of two perpendicular closed hemispheres; it has area \(\pi\), boundary length \(2\pi\), and contains two antipodal poles. Every great circle meets it. For almost every orientation this intersection is a single nondegenerate arc. No conditioning on a cut or reweighting by the arc length occurs. Spherical arclength, not Euclidean straight-chord length, is measured. All exceptional normals used in the proof form a spherical-area-null set.

## Proof

**1. Endpoints and angular length.** Write the uniform normal as \(N=(a,b,c)\). For \(c\ne0\), let \(s=\operatorname{sgn}(c)\). The unique endpoint on the boundary meridian \(y=0\) with \(x\ge0\) is
\[
P=\frac{(sc,0,-sa)}{\sqrt{a^2+c^2}},
\]
and that on \(x=0\) with \(y\ge0\) is
\[
Q=\frac{(0,sc,-sb)}{\sqrt{b^2+c^2}}.
\]
The restrictions \(x\ge0\) and \(y\ge0\) cut the great circle into the single arc between these endpoints: each is a semicircular restriction, their intersection is connected, and the midpoint of the shorter endpoint arc has positive first and second coordinates. Thus the intrinsic arc length lies in \((0,\pi)\), and
\[
\cos L=P\cdot Q
=\frac{ab}{\sqrt{a^2+c^2}\sqrt{b^2+c^2}}.
\tag{1}
\]
This holds even when \(ab<0\), which is the regime of longer-than-right-angle sections.

**2. Haar measure.** Rotational invariance implies that \(U=|a|\) is uniform on \((0,1)\), its sign \(S=\operatorname{sgn}(a)\) is symmetric and independent of \(U\), and \(T=\operatorname{arg}(b+ic)\) is uniform on \([0,2\pi)\), independent of both. Substituting \(b=\sqrt{1-a^2}\cos T\) and \(c=\sqrt{1-a^2}\sin T\) into (1) yields
\[
\cos L=\frac{S U\cos T}{\sqrt{U^2+(1-U^2)\sin^2T}}.
\tag{2}
\]
Fix \(u\in(0,1)\) and \(0<t<\pi/2\). The event \(L<t\) means that \(S\cos T>0\) and
\[
\sin^2 T<\frac{u^2\sin^2t}{\cos^2t+u^2\sin^2t}.
\]
For each sign of \(S\), the appropriate angular interval has measure twice the arcsine of the square-root threshold. Averaging the uniform \(T\) and sign \(S\), and using \(\arcsin( u\sin t/\sqrt{\cos^2t+u^2\sin^2t})=\arctan(u\tan t)\), gives
\[
\mathbb P(L<t\mid U=u)=\frac1\pi\arctan(u\tan t).
\tag{3}
\]
Integrating \(u\) from zero to one and evaluating an elementary antiderivative,
\[
\mathbb P(L<t)=\frac1\pi\int_0^1\arctan(u\tan t)\,du
=\frac1\pi\bigl(t+\cot t\log\cos t\bigr),\quad 0<t<\pi/2.
\tag{4}
\]
**3. Reflection and analytic consequences.** The measure-preserving transformation \((a,b,c)\mapsto(-a,b,c)\) negates the right side of (1), so \(L\) and \(\pi-L\) have identical laws. Therefore \(F_L(t)=1-F_L(\pi-t)\), extending (4) to the claimed absolute-cosine formula on \((\pi/2,\pi)\). Taking limits establishes continuity at the midpoint and the endpoints. Differentiation gives the displayed density. Using \(z=\sin^2t\), it can be written
\[
f_L(t)=\frac{-\log(1-z)}{2\pi z},\quad 0<z<1.
\]
The series \(-\log(1-z)/z=\sum_{j\ge0}z^j/(j+1)\) proves strict monotonicity in \(z\), hence the stated unimodality and endpoint limits. The logarithmic singularity is integrable, and expansion of (4) at \(\pi/2-\varepsilon\) gives the narrow central-band formula. Reflection symmetry supplies \(\mathbb E L=\pi/2\) and the median.

## Verification

Run the standalone standard-library checker `verify_chord.py` with `python3 verify_chord.py`. It independently samples 240,000 uniformly distributed normal directions, reconstructs each section length from its endpoints, and for 120 further normals compares that value against angular clipping on the great circle using 8,192 evenly spaced test angles. It also quadratures the independent one-dimensional integral in (4), checks derivative and reflection identities, and tests the midpoint logarithmic asymptotic. The checked output is `ALL_RIGHT_LUNE_SECTION_LAW_CHECKS_PASSED`. The exact proof, not numerical sampling, justifies the infinite collection of thresholds.

## Relationship to prior work

Moseeva, Tarasov and Zaporozhets [1] study distributions of geodesic chords of spherical convex bodies and calculate the spherical-cap case. Their explicitly defined spherical bodies are generated by line-free cones, whereas this lune contains an antipodal pair, and their paper does not evaluate the right-lune section-length law. Besau and coauthors [2] introduce and analyze the orthogonal spherical-wedge model. Their Section 4 obtains a geometric description of a normal-plane section as another wedge (especially Lemma 4.1), but investigates random-polytope facet asymptotics, not the Haar pushforward CDF and its logarithmic density. Gille's papers [3,4] concern Euclidean three-dimensional solid hemisphere and wedge chord models, not the intrinsic one-dimensional arc cut from this spherical lune. The substantive evaluated statement here is the complete exact distribution under a specified random-great-circle measure; generic section parameterizations or unrelated chord samplings do not themselves state this distribution.

## Limitations

This is a right-angle lune on the unit two-sphere, with planes through the sphere center and Haar-uniform orientations. It does not determine the law for other lune opening angles, offset planar cuts, random endpoint-pair distances, or a length-biased sampling of planes. Historical priority remains subject to further literature comparison. Independent mathematical audit has not been performed.

## References

1. T. Moseeva, A. Tarasov, D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297 (first posted 2020-07-14), https://arxiv.org/html/2007.07297v1 .
2. F. Besau, A. Gusakova, M. Reitzner, C. Schütt, C. Thäle, E. Werner, *Spherical convex hull of random points on a wedge*, arXiv:2203.07916 (first posted 2022-03-15), https://arxiv.org/abs/2203.07916 .
3. W. Gille, *Chord Length Distributions of the Hemisphere*, *Journal of Mathematics and Statistics* 1 (2005), 24–28; DOI:10.3844/jmssp.2005.24.28 .
4. W. Gille, *Analysis of the Chord Length Distribution Along an Edge: The Wedge Case and the Quadratic Rod Case*, *Journal of Mathematics and Statistics* 1 (2005), 106–112; DOI:10.3844/jmssp.2005.106.112 .

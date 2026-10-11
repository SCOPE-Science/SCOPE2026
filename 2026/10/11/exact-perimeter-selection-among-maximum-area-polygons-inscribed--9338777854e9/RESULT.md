# Exact perimeter selection among maximum-area polygons inscribed in ellipses

## Finding

For every noncircular ellipse with semiaxes \(a>b>0\) and every integer \(n\ge3\), the maximum-area inscribed \(n\)-gons form a rotating affine-regular family. Their *Euclidean perimeter*, which is not affine invariant, has an exactly classifiable orientation dependence: there is a unique maximum phase and a unique minimum phase modulo the perimeter's fundamental period, and no other stationary phases.

Put \(q=n/\gcd(n,2)\), \(d=n/q\), \(\alpha=(a^2+b^2)/2\), \(\beta=(a^2-b^2)/2\), \(\phi=\theta+\pi/n-\pi/2\), and \(c=(-1)^q\cos(2q\phi)\). Here \(\theta\) is the angular parameter of the first vertex on the unit circle before the affine map. If \(P_n(\theta)\) is the Euclidean perimeter, then \(P_n(\theta)=F_{a,b,n}(c)\), where \(F_{a,b,n}\) is **strictly decreasing and strictly concave** on \([-1,1]\). In particular the maximum phases are exactly
\[
\cos(2q\phi)=(-1)^{q+1},
\]
and the minimum phases exactly \(\cos(2q\phi)=(-1)^q\). Thus the maximizing phases have \(\cos(2q\phi)=1\) when \(q\) is odd and \(\cos(2q\phi)=-1\) when \(q\) is even.

The theorem also gives *sharp global angular stability*. For \(z(s)=(s+\alpha)/\beta\), the degree-\(q\) Chebyshev polynomial \(T_q\), and \(w=2d\sin(\pi/n)\), define
\[
G(c)=\frac{w}{\pi\beta}\int_0^\infty
\frac{s^{1/2}T_q'(z(s))}{(T_q(z(s))-c)(T_q(z(s))+1)}\,ds.
\]
Both \(G(-1)>0\) and \(G(1)>G(-1)\) are finite. For any maximizing phase \(\theta_*\) and all \(\theta\),
\[
2G(-1)\sin^2(q(\theta-\theta_*))
\le P_n(\theta_*)-P_n(\theta)
\le2G(1)\sin^2(q(\theta-\theta_*)).
\]
Both constants are globally best possible. The lower coefficient is the limit of the deficit divided by \(\sin^2(q(\theta-\theta_*))\) as \(\theta\to\theta_*\) and the upper one is attained at every minimizing phase. The maximum and minimum orientations are therefore nondegenerate.

## Assumptions and scope

The ellipse is \(E=\{(a\cos t,b\sin t):t\in[0,2\pi)\}\), with \(a>b>0\); the polygons are non-self-intersecting convex \(n\)-gons inscribed in its boundary. The \(n\) vertices of every maximum-area polygon, cyclically ordered, are
\[
V_j(\theta)=(a\cos(\theta+2\pi j/n),b\sin(\theta+2\pi j/n)),\quad j=0,\ldots,n-1.
\]
The common maximum area is \(ab(n/2)\sin(2\pi/n)\). This family is the entire area-maximizer set, including all rotations. We compare only their *ordinary Euclidean* perimeters, not affine perimeters and not the perimeters of arbitrary inscribed polygons. As \(\theta\) varies, the perimeter has fundamental period \(\pi/q\); orientations differing by that period give the same value. The circular case \(a=b\) is excluded, because then the perimeter is constant in \(\theta\).

## Proof

**1. Complete area-maximizer family.** Inverse-affinely map the ellipse onto the unit circle. Area scales by \(ab\). For cyclic circle vertices with consecutive positive gaps \(\Delta_j\) summing to \(2\pi\), twice their polygonal area is \(\sum_j\sin\Delta_j\). At a global maximum, moving any one vertex along the arc between its two neighbors preserves a convex inscribed polygon and changes only two consecutive gaps. If their sum is \(\delta\in(0,2\pi)\), the variable contribution is \(2\sin(\delta/2)\cos(t-\delta/2)\), uniquely maximized at the arc midpoint \(t=\delta/2\). Hence every consecutive pair of gaps is equal, so all are \(2\pi/n\). Conversely the regular polygon exists and thus gives the global maximum. This proves the claimed area and the complete one-parameter family.

**2. Exact side-length reduction.** Elementary chord subtraction gives
\[
\lVert V_{j+1}(\theta)-V_j(\theta)\rVert
=2\sin(\pi/n)\sqrt{\alpha+\beta\cos(2\phi+4\pi j/n)}.
\]
Because the arguments modulo \(2\pi\) form a cyclic grid of size \(q=n/\gcd(n,2)\), each repeated \(d\) times,
\[
P_n(\theta)=w\sum_{j=0}^{q-1}\sqrt{\alpha+\beta\cos(2\phi+2\pi j/q)},\qquad w=2d\sin(\pi/n).
\]
This also shows that the phase period is at most \(\pi/q\); strict monotonicity below shows it is exactly that value.

**3. Chebyshev resolvent and sign.** For every positive \(x\),
\[
\sqrt{x}=\frac1\pi\int_0^\infty\frac{x}{x+s}\frac{ds}{\sqrt{s}}.
\]
The Chebyshev polynomial \(T_q\) obeys the product identity
\[
\prod_{j=0}^{q-1}\left(z+\cos(\psi+2\pi j/q)\right)
=2^{1-q}\left(T_q(z)-(-1)^q\cos(q\psi)\right).
\]
For justification, both sides are monic polynomials in \(z\), and the zeros of the right side are precisely the \(q\) values \(-\cos(\psi+2\pi j/q)\), with multiplicity; continuity covers repeated zeros. Logarithmic differentiation gives
\[
\sum_{j=0}^{q-1}\frac1{z+\cos(\psi+2\pi j/q)}
=\frac{T_q'(z)}{T_q(z)-(-1)^q\cos(q\psi)}.
\]
Here \(z=(s+\alpha)/\beta>1\), since \(\alpha-\beta=b^2>0\). Using \(x/(x+s)=1-s/(x+s)\) and the preceding logarithmic derivative yields
\[
F_{a,b,n}(c)=\frac{w}{\pi}\int_0^\infty s^{-1/2}
\left[q-\frac{s}{\beta}\frac{T_q'(z(s))}{T_q(z(s))-c}\right]ds.
\]
The integrand as a whole, rather than its separated terms, is integrable. Differentiation with respect to \(c\) is justified uniformly on \([-1,1]\): at infinity, the derivative integrand is \(O(s^{-q-1/2})\), while at zero it is \(O(s^{1/2})\). Therefore
\[
F_{a,b,n}'(c)=-\frac{w}{\pi\beta}\int_0^\infty
\frac{s^{1/2}T_q'(z(s))}{(T_q(z(s))-c)^2}\,ds<0,
\]
and
\[
F_{a,b,n}''(c)=-\frac{2w}{\pi\beta}\int_0^\infty
\frac{s^{1/2}T_q'(z(s))}{(T_q(z(s))-c)^3}\,ds<0.
\]
Indeed \(T_q(z)>1\) and \(T_q'(z)>0\) for \(z>1\), as follows from \(T_q(z)=\cosh(q\operatorname{arcosh}z)\). All derivative integrals are finite. Strict descent and concavity follow; since \(c\) is a cosine, only its endpoints are stationary phases, and these are the asserted alternating maxima and minima.

**4. Sharp stability.** Subtract the resolvent expressions at \(c=-1\) and a general \(c\). This gives the *exact* factorization
\[
F_{a,b,n}(-1)-F_{a,b,n}(c)=(1+c)G(c),
\]
with \(G\) as above. All its integrands are positive and \(G'(c)>0\) by differentiation. Thus \(G(-1)\le G(c)\le G(1)\). For a maximizing \(\theta_*\), the phase relation becomes \(c(\theta)=-\cos(2q(\theta-\theta_*))\) and hence \(1+c(\theta)=2\sin^2(q(\theta-\theta_*))\). Inserting this identity gives the two-sided bound. Its lower coefficient is best by the continuous limit at a maximum; its upper coefficient is attained at \(c=1\), exactly a minimum. Since \(G(-1)>0\), all maximizing phases have a strict quadratic deficit. An analogous second-derivative argument treats minima. This completes all claims.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. Run `python3 verify.py` in the directory containing this document. It performs 6,732 deterministic finite tests: direct Euclidean vertex-edge perimeters against the grouped expression, phase monotonicity, finite-difference comparisons with the independent Chebyshev-resolvent integral, and the Chebyshev product/logarithmic-derivative identities. The output is `VERIFY_OK 6732`. These finite checks do not replace the proof for arbitrary real semiaxes and all polygon orders.

## Relationship to prior work

Craizer, Teixeira and da Silva [1] study affine geometry of equal-area polygons and establish an *affine* isoperimetric inequality for affine-regular polygons. Their Section 6 defines affine perimeter through a discrete affine normalization, not ordinary Euclidean edge lengths. The strict Euclidean-perimeter phase ordering and sharp orientation constants here are different statements, not corollaries of the cited affine inequality.

Gronchi and Longinetti [2] study area-drop functionals whose maximizers are affinely regular polygons; that affine-invariant optimization differs from maximizing Euclidean perimeter *within the already area-maximizing inscribed family*. Only the publicly accessible abstract was materially examined for [2]; its full text was unavailable. Fisher and Jamison [3] address characterizations of affinely regular polygons; only bibliographic and abstract-level evidence was available. The explicit ellipse example [4] confirms the continuum of equally area-maximizing orientations but does not compare their perimeters. The broader arbitrary-inscribed-polygon perimeter problem discussed in [5] has a different feasible set.

## Limitations

The theorem does not characterize perimeter maximizers among *all* inscribed \(n\)-gons, only among those maximizing area; it does not address ellipses of zero minor semiaxis or three-dimensional ellipsoids. Earlier equivalent trigonometric-sum inequalities or treatments of affine-regular polygon perimeters may exist and were not exhaustively ruled out; in particular the inaccessible full texts of [2] and [3] remain historical overlap risks. The included numerical checks are finite diagnostics, not a replacement for the exact Chebyshev argument.

## References

[1] M. Craizer, R. C. Teixeira, M. A. H. B. da Silva, *Affine Properties of Convex Equal-Area Polygons*, arXiv:1103.2722, first posted 2011-03-14; *Discrete & Computational Geometry* 48 (2012), 580–595, DOI:10.1007/s00454-012-9448-y.

[2] P. Gronchi, M. Longinetti, *Affinely Regular Polygons as Extremals of Area Functionals*, *Discrete & Computational Geometry* 39 (2008), 273–297, DOI:10.1007/s00454-007-9010-5, published online 2007-09-11.

[3] J. C. Fisher, R. E. Jamison, *Properties of Affinely Regular Polygons*, *Geometriae Dedicata* 69 (1998), 241–259, DOI:10.1023/A:1004903818702.

[4] P. Pamfilos, *Maximal Polygon in Ellipse*, geometry problem and construction, https://users.math.uoc.gr/~pamfilos/eGallery/problems/MaximalRegInEllipse.html (date not established).

[5] R. Nandakumar, *Inscribed n-gons of maximum perimeter for an ellipse*, MathOverflow, 2021-10-27, https://mathoverflow.net/questions/407192/inscribed-n-gons-of-maximum-perimeter-for-an-ellipse.

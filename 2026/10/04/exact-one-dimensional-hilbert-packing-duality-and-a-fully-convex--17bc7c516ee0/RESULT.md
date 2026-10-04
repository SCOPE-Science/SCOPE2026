# Exact one-dimensional Hilbert packing duality and a fully convexified diagonal bound
## Finding

Let \(K=[a,b]\) and \(G=[c,d]\) satisfy \(a<c<0<d<b\). Define
\[
D_H(G,K)
=\frac12\log\!\left(\frac{(d-a)(b-c)}{(c-a)(b-d)}\right).
\]
For every \(\alpha>0\),
\[
M_H(G,K;\alpha)
=\widehat M_H(G,K;\alpha)
=M_H(K^\circ,G^\circ;\alpha)
=\widehat M_H(K^\circ,G^\circ;\alpha)
=\left\lfloor\frac{D_H(G,K)}{\alpha}\right\rfloor+1.
\]
Moreover, for every \(\eta>0\),
\[
\widehat M_{\mathrm{diag},H}(K^\circ,G^\circ;\eta)
\le
\widehat M_H(K^\circ,G^\circ;\eta/4)^2.
\]
This gives an affirmative one-dimensional instance of the fully convexified diagonal-product problem of Arya and Mount with \(C=1\) and \(c=1/4\). The constant \(C=1\) is optimal for this choice of \(c\).

## Assumptions and scope

All intervals are subsets of \(\mathbb R\), \(0\in\operatorname{int}G\), and \(G\subset\operatorname{int}K\). The Hilbert metric is normalized as in Arya--Mount: one half of the logarithmic cross ratio. The result concerns one-dimensional Hilbert geometries only; it does not resolve their Problem 5.1 in dimensions at least two.

For an interval \(I=[u,v]\) with \(u<0<v\), polarity is
\[
I^\circ=[1/u,1/v].
\]
Hence \(K^\circ=[1/a,1/b]\subset\operatorname{int}[1/c,1/d]=\operatorname{int}G^\circ\).

## Proof

Define the increasing Hilbert coordinate
\[
\psi_K(x)=\frac12\log\!\left(\frac{x-a}{b-x}\right),
\qquad a<x<b.
\]
For \(x,y\in(a,b)\), direct evaluation of the cross ratio gives
\[
d_K^H(x,y)=\left|\psi_K(x)-\psi_K(y)\right|.
\]
Thus \(G=[c,d]\) is isometric to the Euclidean interval
\[
[\psi_K(c),\psi_K(d)]
\]
of length \(D_H(G,K)\).

Consider a Hilbert-convexified \(\alpha\)-separated sequence \(x_1,\ldots,x_N\) in \(G\). After \(j-1\) terms, their ordinary convex hull is the interval
\[
[\min_{i<j}x_i,\max_{i<j}x_i].
\]
Because \(\psi_K\) is increasing, its image is exactly the interval between the corresponding extreme \(\psi_K\)-coordinates. If \(x_j\) has Hilbert distance at least \(\alpha\) from that hull, its \(\psi_K\)-coordinate lies outside the previous coordinate interval and enlarges its length by at least \(\alpha\). Therefore every term after the first consumes at least \(\alpha\) of the available span:
\[
(N-1)\alpha\le D_H(G,K).
\]
Hence
\[
\widehat M_H(G,K;\alpha)\le
\left\lfloor\frac{D_H(G,K)}{\alpha}\right\rfloor+1.
\]
Conversely, if
\[
m=\left\lfloor\frac{D_H(G,K)}{\alpha}\right\rfloor,
\]
choose \(m+1\) points whose \(\psi_K\)-coordinates are
\[
\psi_K(c),\ \psi_K(c)+\alpha,\ \ldots,\ \psi_K(c)+m\alpha.
\]
They occur monotonically in \(G\), and each new point is exactly \(\alpha\) from the preceding convex hull except possibly for unused terminal span. Hence the upper bound is attained. The same coordinate interval argument gives the identical formula for ordinary packing, so
\[
M_H(G,K;\alpha)=\widehat M_H(G,K;\alpha).
\]

It remains to compare the reversed polar pair. The Hilbert diameter of \(K^\circ\) inside \(G^\circ\) is
\[
\frac12\log\!\left(
\frac{(1/b-1/c)(1/d-1/a)}
{(1/a-1/c)(1/d-1/b)}
\right).
\]
Multiplying numerator and denominator by \(abcd>0\) reduces the cross-ratio quotient exactly to
\[
\frac{(b-c)(d-a)}{(c-a)(b-d)},
\]
which is the quotient defining \(D_H(G,K)\). Therefore
\[
D_H(K^\circ,G^\circ)=D_H(G,K),
\]
and the exact packing formula applies to both sides at the same separation parameter.

Finally, Arya and Mount prove the mixed diagonal estimate
\[
\widehat M_{\mathrm{diag},H}(K^\circ,G^\circ;\eta)
\le
M_H(K^\circ,G^\circ;\eta/4)\,
\widehat M_H(K^\circ,G^\circ;\eta/2).
\]
In one dimension the first factor equals its convexified counterpart by the formula just proved. Monotonicity in the separation parameter then yields
\[
\widehat M_{\mathrm{diag},H}(K^\circ,G^\circ;\eta)
\le
\widehat M_H(K^\circ,G^\circ;\eta/4)^2.
\]
Thus Problem 5.1 holds in one dimension with \(C=1\) and \(c=1/4\). Since every diagonal packing number and every ordinary or convexified packing number is at least \(1\), taking \(\eta\) larger than the relevant compact Hilbert diameters makes both sides equal to \(1\), so no multiplicative constant below \(1\) can work at this scale.

## Verification

The proof is analytic and covers every admissible nested interval and every positive separation parameter. The accompanying `verify.py` checks the cross-ratio polarity identity exactly on several rational interval instances and checks the Hilbert-coordinate distance identity numerically on fixed samples. Those computations are sanity checks only; they are not substitutes for the quantified proof.

The source date is the arXiv version-one submission timestamp, 2026-08-06 02:25:49 UTC. A compiled bibliographic record lists MSC classifications in the order 52A40, 51F99, 52A20; the finding is assigned to 52A40.

## Relationship to prior work

Arya and Mount define ordinary Hilbert packing, Hilbert-convexified packing, and diagonal convexified packing, prove the mixed diagonal product estimate used above, and pose as Problem 5.1 whether a fully convexified diagonal bound exists with absolute constants. Their paper does not isolate the one-dimensional case or state the exact interval packing and reversed-polar identities above.

Artstein, Milman, Szarek, and Tomczak-Jaegermann introduced convexified packing in the normed-space entropy-duality setting and proved a polarity theorem for that notion. Their result motivates the modern Hilbert-geometric program but does not imply this exact interval Hilbert formula: the Hilbert metric is projective and non-translation-invariant before one-dimensional straightening.

A claim-focused search found no source stating the same exact four-way packing identity together with the one-dimensional resolution of the diagonal-product problem.

## Limitations

The substantive limitation is dimension: the argument uses the total order of an interval, which makes every preceding convex hull another interval and forces each convexified point to extend one endpoint. In higher dimension a new point can avoid a convex hull without increasing a single scalar span, and synchronized diagonal convexification remains the difficulty identified by Arya and Mount.

The cross-ratio coordinate itself is classical. The claimed contribution is the exact packing collapse, the same-scale reversed-polar identity, and the resulting fully convexified diagonal bound in the one-dimensional model case. No claim of higher-dimensional extension is made.

## References

1. S. Arya and D. M. Mount, “Duality Bounds for Convexified Packing in Hilbert Geometry,” arXiv:2608.05533v2, 2026. Version one submitted 2026-08-06 02:25:49 UTC.
2. S. Artstein, V. Milman, S. J. Szarek, and N. Tomczak-Jaegermann, “On convexified packing and entropy duality,” Geometric and Functional Analysis 14 (2004), 1134–1141, DOI 10.1007/s00039-004-0486-3.

# An explicit two-integer nonconstructible cyclic \(771\)-gon
## Finding
Consider a convex cyclic \(771\)-gon whose side sequence consists of \(769\) copies of \(768\), followed by two copies of \(769\). This polygon exists and is not constructible from those side lengths with straightedge and compass.

More precisely, if \(r\) is the circumradius and \(t=(2r)^{-2}\), define
\[
P(t)=768\,U_{768}\!\left(\sqrt{1-768^2t}\right),
\qquad
Q(t)=P(t)^2-4\cdot769^2\left(1-769^2t\right),
\]
where \(U_{768}\) is the Chebyshev polynomial of the second kind. Then the geometric value of \(t\) is a root of \(Q\), and every irreducible factor of \(Q\) over \(\mathbb Q\) has degree divisible by \(384\). Hence the minimal polynomial of this \(t\) has degree \(384\) or \(768\), so \(t\) is not constructible.

## Assumptions and scope
The polygon is convex and cyclic, with side multiset consisting exactly of \(769\) sides of length \(768\) and two sides of length \(769\). The statement concerns classical straightedge-and-compass constructibility from these given integer lengths. It is an explicit certificate for one order, \(771\); it is not a new general nonconstructibility theorem for all cyclic polygons.

## Proof
Let \(u=(2r)^{-1}\). Write \(\alpha\) for the half central angle subtended by a side of length \(768\), and \(\beta\) for the half central angle subtended by a side of length \(769\). Thus
\[
\sin\alpha=768u,\qquad \sin\beta=769u,
\]
and convexity gives
\[
769\alpha+2\beta=\pi.
\]
Existence follows directly: as \(u\) increases continuously from \(0\) to \(1/769\), the left side increases continuously from \(0\) to a value strictly larger than \(\pi\), so there is a unique solution with \(0<u<1/769\).

Put \(t=u^2\). Since \(769\alpha=\pi-2\beta\),
\[
\sin(769\alpha)=\sin(2\beta)=2\cdot769u\sqrt{1-769^2u^2}.
\]
Using \(\sin(769\alpha)=\sin\alpha\,U_{768}(\cos\alpha)\) and \(\cos\alpha=\sqrt{1-768^2t}\), division by \(u>0\) gives
\[
P(t)=2\cdot769\sqrt{1-769^2t},
\]
so \(Q(t)=0\).

Set \(p=769\) and \(m=384\). Because \(p\) is prime,
\[
U_{p-1}(x)\equiv (x^2-1)^m\pmod p.
\]
One direct verification uses
\[
U_{p-1}\!\left(\frac{z+z^{-1}}2\right)=\frac{z^p-z^{-p}}{z-z^{-1}}
\]
and the characteristic-\(p\) identity \((z+z^{-1})^p=z^p+z^{-p}\), which yields the displayed polynomial congruence. After substituting \(x^2=1-768^2t\), Fermat's congruence and \(768\not\equiv0\pmod p\) yield
\[
P(t)\equiv768\,t^m\pmod p.
\]
Also \(P(0)=768p\). Therefore every coefficient of \(P\) below degree \(m\) is divisible by \(p\), while its leading coefficient is not. For \(Q=P^2-4p^2+4p^4t\), the constant term is
\[
p^2(768^2-4),
\]
which has exact \(p\)-adic valuation \(2\), because \(768^2-4\equiv-3\pmod{769}\). Coefficients of degrees \(1,\ldots,383\) have valuation at least \(2\), coefficients of degrees \(384,\ldots,767\) have valuation at least \(1\), and the leading coefficient has valuation \(0\). Hence the lower \(769\)-adic Newton polygon of \(Q\) is exactly the single segment from \((0,2)\) to \((768,0)\), of reduced slope \(-1/384\).

For a polynomial over \(\mathbb Q_p\) with one Newton-polygon slope \(-a/e\) in lowest terms, every irreducible factor has degree divisible by \(e\): each root has \(p\)-adic valuation \(a/e\), so the ramification index of any local field containing that root is divisible by \(e\), and hence so is the local extension degree. Thus every irreducible factor of \(Q\) over \(\mathbb Q_p\), and therefore every irreducible factor over \(\mathbb Q\), has degree divisible by \(384\). Since \(\deg Q=768\), the minimal polynomial of the geometric root \(t\) has degree \(384\) or \(768\), neither a power of \(2\). Therefore \(t\) is not constructible. If the polygon were constructible, its vertices would determine the circumcenter and circumradius by straightedge and compass, so \(t=(2r)^{-2}\) would be constructible, a contradiction.

## Verification
The bundled `verify.py` reconstructs \(P\) and \(Q\) by integer polynomial arithmetic, checks \(\deg P=384\) and \(\deg Q=768\), verifies the coefficient divisibilities that determine the Newton polygon, checks that the constant term has exact \(769\)-adic valuation \(2\), and confirms primality of \(769\). It prints `VERIFY_OK` on success. The universal nonconstructibility conclusion comes from the analytic and \(p\)-adic proof above, not from finite numerical testing.

## Relationship to prior work
The first public version of Czédli and Kunos (arXiv:1307.5484v1, 2013) conjectured nonconstructibility for odd orders and explicitly displayed \(n=771\) as the first constructible-regular order beyond their verified range; their table left the \(771\) column unresolved and stated that it was beyond the capacity of their personal computers. Their later paper (arXiv:1307.5484v2; *Acta Sci. Math.* 81 (2015), 643–683) proved the stronger existential theorem that every odd \(n\ge8\) has some nonconstructible cyclic \(n\)-gon with at most two integer side lengths, using a limit theorem and Hilbert irreducibility. That later theorem therefore already settles existence at \(n=771\); the contribution here is narrower and different: it gives the concrete consecutive pair \(768,769\), the exact multiplicities \(769+2\), and a short elementary local-field certificate for this explicit polygon. Targeted searches located no prior statement of this specific example or certificate.

## Limitations
This does not improve the 2015 general theorem and does not claim that \(768\) and \(769\) are minimal, unique, or optimal side lengths. It also does not classify which two-length \(771\)-gons are constructible. The originality claim is limited to this explicit witness and its Newton-polygon proof; unindexed or differently phrased prior examples remain a residual risk.

## References
1. G. Czédli and Á. Kunos, *On the geometric constructibility of cyclic polygons with even number of vertices*, arXiv:1307.5484v1, first publicly posted 2013-07-21.
2. G. Czédli and Á. Kunos, *Geometric constructibility of cyclic polygons and a limit theorem*, arXiv:1307.5484v2; *Acta Sci. Math. (Szeged)* 81 (2015), 643–683, doi:10.14232/actasm-015-259-3.

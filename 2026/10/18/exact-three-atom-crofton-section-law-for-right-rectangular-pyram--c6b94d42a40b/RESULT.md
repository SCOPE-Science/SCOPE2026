# Exact three-atom Crofton section law for right rectangular pyramids

## Finding
Let \(a,b,h>0\) and let \(P\) be the right rectangular pyramid with base vertices \((\pm a,\pm b,0)\) and apex \((0,0,h)\). Choose a random unoriented affine plane from the invariant measure on planes conditioned on meeting \(P\) in a two-dimensional polygon. If \(N\) is the number of section sides, then precisely \(N=3,4,5\) occur, each with strictly positive probability.

Define
\[
S=\sqrt{a^2+b^2},\quad D=\sqrt{a^2+b^2+h^2},\quad
J=\frac12\left[D\arctan\frac{hD}{ab}-a\arctan\frac hb-b\arctan\frac ha\right],\quad
Z=\pi(a+b)+2J.
\]
The exact complete polygon-type law is
\[
\boxed{\Pr(N=3)=\frac{\pi(2a+2b-D-S)+4J}{Z}},\qquad
\boxed{\Pr(N=4)=\frac{\pi(2S-a-b)+2J}{Z}},\qquad
\boxed{\Pr(N=5)=\frac{\pi(D-S)-4J}{Z}}.
\]
In particular
\[
\boxed{\mathbb E N=\frac{2\pi(a+b+D)}{Z}}.
\]
The law is invariant under simultaneously scaling \(a,b,h\) and symmetric under interchanging \(a,b\). It is genuinely a two-shape-parameter law.

## Assumptions and scope
The space of oriented affine planes is parameterized by \((u,t)\in S^2\times\mathbb R\), where the plane is \(H(u,t)=\{x:u\cdot x=t\}\). The measure \(d\sigma(u)\,dt\), with \(\sigma\) ordinary sphere area and a harmless factor of two for unoriented planes, is translation and rotation invariant. Conditional on intersection with \(P\), its orientation density is proportional to the directional width \(w_P(u)\), and its offset is uniform between the minimum and maximum support heights. This is **not** the law obtained by first choosing a uniform orientation and then sampling one intersecting offset. Degenerate contacts and planes through vertices or edges have zero probability.

The pyramid has four base edges and four apex edges. Its five facet planes bound a generic section, so the section has at least three and at most five sides. These are the only three possible values, not merely an upper bound.

## Proof
**1. Width normalization.** Write \(u=(x,y,z)\), \(A=a|x|+b|y|\) and \(B=h|z|\). The four base support heights are \(\pm ax\pm by\), and the apex height is \(hz\). By symmetry across \(z=0\), the average width over the two possible signs of \(z\) is \(2A+(B-A)_+\). Consequently
\[
W:=\int_{S^2}w_P(u)\,d\sigma(u)
=4\pi(a+b)+8J=4Z,
\]
where \((s)_+=\max(s,0)\) and
\[
J=\int_{S^2\cap\{x,y,z>0\}}(hz-ax-by)_+\,d\sigma(u).
\]
Indeed \(\int_{S^2}|u_i|\,d\sigma=2\pi\) for each coordinate. With \(x=\cos\vartheta\cos\varphi\), \(y=\cos\vartheta\sin\varphi\), \(z=\sin\vartheta\), the positive-octant integral reduces to
\[
J=\frac12\int_0^{\pi/2}\left[h-v(\varphi)\arctan\frac{h}{v(\varphi)}\right]d\varphi,\qquad
v(\varphi)=a\cos\varphi+b\sin\varphi.
\]
The elevation identity is \(\int_0^{\pi/2}(h\sin\vartheta-v\cos\vartheta)_+\cos\vartheta\,d\vartheta=[h-v\arctan(h/v)]/2\).

To evaluate the remaining integral, integration by parts gives
\[
2J=hD^2\int_0^{\pi/2}\frac{d\varphi}{h^2+(a\cos\varphi+b\sin\varphi)^2}
-a\arctan\frac hb-b\arctan\frac ha.
\]
The substitution \(s=\tan\varphi\) yields
\[
\int_0^{\pi/2}\frac{d\varphi}{h^2+(a\cos\varphi+b\sin\varphi)^2}
=\int_0^\infty\frac{ds}{(h^2+b^2)s^2+2abs+(h^2+a^2)}
=\frac{1}{hD}\arctan\frac{hD}{ab}.
\]
This proves the stated expression for \(J\) and the normalization \(W=4Z\).

**2. All pentagonal sections.** A plane cuts a polyhedron edge precisely when its endpoint support heights straddle the plane offset. For a pyramid, five cut edges occur if and only if the plane separates the apex and exactly one base corner from the other three base corners (or reverses both sides). For a direction in the positive octant the upper base support height is \(ax+by\), the runner-up base height is \(|ax-by|\), and the apex support height is \(hz\). The interval of offsets yielding five crossing edges therefore has length
\[
\ell_5(u)=\left[\min(hz,ax+by)-|ax-by|\right]_+
=(hz-|ax-by|)_+-(hz-ax-by)_+.
\]
The lower-apex configuration and coordinate-sign symmetries give a total five-section plane measure
\[
M_5=8(J_--J),\qquad
J_-:=\int_{S^2\cap\{x,y,z>0\}}(hz-|ax-by|)_+\,d\sigma(u).
\]
Let \(S=\sqrt{a^2+b^2}\), and write \(a=S\cos\alpha,b=S\sin\alpha\). Applying the same elevation integral to \(J_-\), and pairing \(|a\cos\varphi-b\sin\varphi|\) with \(a\cos\varphi+b\sin\varphi\), one obtains
\[
J_-+J=2\int_0^{\pi/2}\frac12\left[h-S\cos\varphi\arctan\frac{h}{S\cos\varphi}\right]d\varphi
=\frac\pi2(D-S).
\]
The first equality follows by changing the integration variable in the two cosine phases and reflecting about a coordinate axis. The second is an elementary one-variable integration by parts, or the preceding formula with one base half-length tending to zero. Thus
\[
\Pr(N=5)=\frac{M_5}{W}=\frac{\pi(D-S)-4J}{Z}.
\]

**3. Expected side count.** For any edge of length \(L\), its crossing-offset interval has length \(L|u\cdot e|\), where \(e\) is its unit direction. Integrating over \(S^2\) gives \(2\pi L\). The four base edges have total length \(4(a+b)\), and the four apex edges each have length \(D\). It follows exactly that
\[
\int_{S^2}\int_\mathbb R N(u,t)\,\mathbf1_{H(u,t)\cap P\ne\varnothing}\,dt\,d\sigma(u)
=8\pi(a+b+D),
\]
whence \(\mathbb E N=2\pi(a+b+D)/Z\). Since \(p_3+p_4+p_5=1\) and \(3p_3+4p_4+5p_5=\mathbb E N\), substitution yields the formulas for \(p_3,p_4\).

**4. Strict positivity and boundary.** A plane clipping a base corner cuts exactly three incident edges; a near-horizontal plane just below the apex cuts four apex edges; and directions with \(ax\) and \(by\) nearly equal and \(hz\) between the two top base heights give five crossing edges. Each configuration persists under small perturbations of direction and offset, proving \(p_3,p_4,p_5>0\) for all \(a,b,h>0\). All calculations disregard only zero-measure exceptional planes.

## Verification
The accompanying standalone file `verify_rect_pyramid.py` uses only the Python standard library. It independently integrates the positive-octant support gaps by high-resolution midpoint quadrature and compares them against both exact arctangent identities. It also samples independent uniformly distributed sphere directions, offsets uniformly across the occupied width, and uses the width as an importance weight so the sampling matches the motion-invariant plane measure. In 11 shapes, including unequal rectangle aspect ratios and both short and tall pyramids, it performed 825,000 direction-offset samples and obtained a maximum absolute frequency discrepancy less than 0.00441. The analytic integral comparisons had absolute discrepancies below \(2\times10^{-8}\). The numerical checks are corroborations, not substitutes for the integral proof.

## Relationship to prior work
Classical stereology studies polygonal side-count frequencies of random sections of polyhedra, especially the integral-geometric formulation in Voss (1982). A directly related methodological paper by Socha (1988) computes **section-angle distributions**, not the complete three-class law for rectangular pyramids; the accessible paper's full text was inspected. Feldman and Klain (2008) relate **random orthogonal projections** of tetrahedra to solid-angle probabilities, which is a different experiment. A separate result treats all-vertex **orthogonal shadows** of right rectangular pyramids; those shadow probabilities do not determine Crofton section probabilities. No inspected accessible source states the explicit full two-parameter formulas proved here.

## Limitations
Definitive historical priority is unresolved. In particular, Voss (1982) explicitly discusses exact side-count frequency formulas for unspecified families of simple polyhedra. Its full text and tables could not be obtained, and it is **not claimed** that they lack a square-pyramid or rectangular-pyramid formula. A historical-priority overlap remains possible. The formulas here concern right pyramids centered over a rectangular base, not general oblique pyramids. They use affine-plane-invariant sampling conditional on intersection, not central sections or equally weighted intersecting orientations. Independent mathematical validation has not been performed.

## References
1. K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy **128** (1982), 111–120. DOI: 10.1111/j.1365-2818.1982.tb00443.x. Publisher abstract inspected; full text inaccessible.
2. P. Socha, *Random Plane Section of a Polyhedron*, Acta Stereologica **7** (1988), 41–46. Accessible full text: https://www.ias-iss.org/acta/ActaStereologica_pdf/Vol.1.2.5.7.8/VOL%207/NO%201/AS_7_n1_41_SOC.pdf.
3. D. V. Feldman and D. A. Klain, *Angles as probabilities*, preprint arXiv:0809.3459, first posted 19 September 2008. https://arxiv.org/abs/0809.3459.

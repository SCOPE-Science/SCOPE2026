# Arithmetic resonance in the excluded area of two rotated regular polygons

## Finding
For every pair of integers \(n,m\ge3\), and arbitrary circumradii \(R,S>0\), let \(P_{n,R}\) be the regular polygon with vertices \(R(\cos(2\pi j/n),\sin(2\pi j/n))\); define \(P_{m,S}\) analogously. For a real orientation \(\theta\), study the area
\[
A(\theta)=\operatorname{Area}\bigl(P_{n,R}+\operatorname{Rot}_{\theta}P_{m,S}\bigr).
\]
Write
\[
 g=\gcd(n,m),\qquad q=n/g,\qquad \alpha=\frac{\pi g}{nm},
\quad \theta_* = \frac{\pi}{n}-\begin{cases}\alpha,&q\text{ even},\\0,&q\text{ odd},\end{cases}
\]
\[
 d(\theta)=\operatorname{dist}\bigl(\theta,\theta_*+2\alpha\mathbb Z\bigr)\in[0,\alpha],\qquad
 C=\frac{RSg\sin(\pi/n)\sin(\pi/m)}{\sin\alpha},
\]
\[
 A_0=\frac{nR^2}{2}\sin\frac{2\pi}{n}+\frac{mS^2}{2}\sin\frac{2\pi}{m}.
\]
Then **the complete angular area profile** is
\[
\boxed{A(\theta)=A_0+2C\cos d(\theta).} \tag{1}
\]
Its smallest period is \(2\alpha=2\pi/\operatorname{lcm}(n,m)\); every maximum is attained at \(\theta=\theta_*+2\alpha k\), and every minimum at \(\theta=\theta_*+(2k+1)\alpha\), where \(k\in\mathbb Z\). The range and peak-to-trough amplitude are
\[
\boxed{A_{\min}=A_0+2C\cos\alpha,\qquad A_{\max}=A_0+2C,
\qquad A_{\max}-A_{\min}=2C(1-\cos\alpha).} \tag{2}
\]
These formulas include both equal and unequal polygon orders, with no parity restriction.

For a uniform random relative orientation \(\Theta\in[0,2\pi)\), the random variable \(A(\Theta)\) has **exactly the distribution**
\[
\boxed{A(\Theta)\ \overset{\mathrm d}=\ A_0+2C\cos U,\qquad U\sim\operatorname{Unif}[0,\alpha].} \tag{3}
\]
Its cumulative distribution function is zero below \(A_{\min}\), one above \(A_{\max}\), and, for \(A_{\min}\le a\le A_{\max}\),
\[
\boxed{\Pr\{A(\Theta)\le a\}=1-\frac1\alpha\arccos\frac{a-A_0}{2C}.} \tag{4}
\]
It has no atoms; on the open support its density is
\[
\boxed{f(a)=\frac1{\alpha\sqrt{4C^2-(a-A_0)^2}}.} \tag{5}
\]
In terms of the perimeters \(p_n=2nR\sin(\pi/n)\) and \(p_m=2mS\sin(\pi/m)\), its first two moments are
\[
\boxed{\mathbb EA(\Theta)=A_0+\frac{p_np_m}{2\pi},\quad
\operatorname{Var}A(\Theta)=4C^2\left(\frac12+\frac{\sin(2\alpha)}{4\alpha}-\frac{\sin^2\alpha}{\alpha^2}\right).} \tag{6}
\]
For fixed positive \(R,S\) and arbitrary integer sequences \(n,m\to\infty\), writing \(g=\gcd(n,m)\) at each step gives the sharp arithmetic resonance
\[
\boxed{\operatorname{Var}A(\Theta)\sim\frac{4\pi^6R^2S^2}{45}\frac{g^4}{n^4m^4}.} \tag{7}
\]
In particular, same-order pairs \((n,m)=(k,k)\) have fluctuations of variance order \(k^{-4}\), whereas consecutive-order pairs \((k,k+1)\) have variance order \(k^{-8}\).

## Assumptions and scope
The polygons are compact, nondegenerate, and Euclidean regular, centered at the origin, with a common specified initial vertex direction. Minkowski addition means \(X+Y=\{x+y:x\in X,y\in Y\}\), and angles are in radians. The scale parameters \(R,S\) are strictly positive. In the random law, only the *relative orientation* is uniformly distributed; there is no randomness in shape or size. All claims hold for \(n,m\ge3\), not for line segments. For excluded area of impenetrable particles, the physical quantity \(\operatorname{Area}(P_{n,R}-\operatorname{Rot}_{\theta}P_{m,S})\) is the same formula after shifting \(\theta\) by \(\pi\); a uniform angle makes this shift immaterial to the law.

## Proof
**1. Mixed-area reduction.** For planar convex polygons \(K,L\), the mixed-area identity is
\[
\operatorname{Area}(K+L)=\operatorname{Area}(K)+\operatorname{Area}(L)+2V(K,L),\qquad
V(K,L)=\frac12\sum_{e\subset\partial K}\ell(e)\,h_L(\nu_e), \tag{8}
\]
where \(\ell(e)\) is edge length, \(\nu_e\) its unit outward normal and \(h_L(u)=\max_{x\in L}x\cdot u\) the support function. Formula (8) follows by differentiating the planar Steiner polynomial \(\operatorname{Area}(K+tL)\) at \(t=0\), where moving each supporting edge by \(t h_L(\nu_e)\) contributes \(\ell(e)h_L(\nu_e)\) to the derivative; vertex corrections are quadratic. Alternatively it is the standard first-variation definition of planar mixed area. This identity remains valid if edge directions coincide, by continuity.

The \(n\) edges of \(P_{n,R}\) each have length \(2R\sin(\pi/n)\) and outward-normal angles \(\pi/n+2\pi j/n\). The support function of the other, rotated, regular polygon is
\[
 h_{\operatorname{Rot}_\theta P_{m,S}}(\phi)
 =S\cos\bigl(\operatorname{dist}(\phi-\theta,(2\pi/m)\mathbb Z)\bigr), \tag{9}
\]
where the circular distance is in \([0,\pi/m]\). Therefore
\[
V=RS\sin(\pi/n)\sum_{j=0}^{n-1}
\cos\operatorname{dist}\!\left(\frac\pi n+\frac{2\pi j}{n}-\theta,\frac{2\pi}{m}\mathbb Z\right). \tag{10}
\]
**2. Collapse of all normal angles.** In the circle of circumference \(2\pi/m\), the \(n\) edge normals in (10) form \(g\) copies of a grid of \(q=n/g\) equally spaced residues. Adjacent grid residues differ by \(2\pi/(mq)=2\alpha\). To see the multiplicity, multiplication by \(m\) turns the residues into the cyclic subgroup of order \(n/\gcd(n,m)=q\).

An interval of angles whose center is a grid point when \(q\) is odd, or whose center is the midpoint of two grid points when \(q\) is even, contains signed representative angles at
\[
 \left\{-\frac{q-1}{2}(2\alpha),-\frac{q-3}{2}(2\alpha),\ldots,
  \frac{q-1}{2}(2\alpha)\right\} \tag{11}
\]
(with integer or half-integer multiples of \(2\alpha\), according to the parity). If the grid is shifted by \(t\in[-\alpha,\alpha]\) relative to this centered position, all representatives stay within \([-\pi/m,\pi/m]\); at the endpoints one representative may lie on the boundary, where the two nearest-vertex choices have equal cosine. Thus the whole sum in (10) becomes
\[
 g\sum_{r=0}^{q-1}\cos\bigl(t+(r-(q-1)/2)2\alpha\bigr)
 =g\frac{\sin(q\alpha)}{\sin\alpha}\cos t
 =g\frac{\sin(\pi/m)}{\sin\alpha}\cos t. \tag{12}
\]
Here the Dirichlet identity follows by summing a finite geometric progression of complex exponentials. The centered grid phase occurs when \(\theta\equiv \pi/n\pmod{2\alpha}\) if \(q\) is odd, and when \(\theta\equiv\pi/n-\alpha\pmod{2\alpha}\) if \(q\) is even. This is precisely \(\theta_*\) from above. Taking \(t\) to be the signed displacement to the closest centered phase proves \(V=C\cos d(\theta)\) and hence (1).

Because \(0<\alpha\le\pi/3\), the cosine decreases strictly on \([0,\alpha]\). Thus (2), all maximizing and minimizing orientations, and the *smallest* angular period follow; indeed the function has one strict maximum per interval of length \(2\alpha\).

**3. Exact probability law and moments.** Uniform orientation on \([0,2\pi)\) induces uniform phase on the period interval, because \(\operatorname{lcm}(n,m)=\pi/\alpha\) is an integer. Folding the phase at its midpoint gives \(d(\Theta)\sim\operatorname{Unif}[0,\alpha]\). Monotonicity of cosine proves (3)–(5). Integrating \(\cos U\) and \(\cos^2U\) gives
\[
\mathbb E\cos U=\frac{\sin\alpha}{\alpha},\qquad
\mathbb E\cos^2 U=\frac12+\frac{\sin(2\alpha)}{4\alpha}. \tag{13}
\]
The mean mixed term is \(2C\sin\alpha/\alpha=2nmRS\sin(\pi/n)\sin(\pi/m)/\pi=p_np_m/(2\pi)\), proving (6) without any stochastic approximation.

**4. Sharp asymptotic.** As \(n,m\to\infty\), \(\alpha\le\pi/\max(n,m)\to0\) and
\[
 C=\pi RS(1+o(1)). \tag{14}
\]
For \(U=\alpha T\), with \(T\sim\operatorname{Unif}[0,1]\), the uniform Taylor estimate \(\cos(\alpha T)=1-\alpha^2T^2/2+O(\alpha^4)\) yields
\[
\operatorname{Var}(\cos U)=\frac{\alpha^4}{4}\operatorname{Var}(T^2)+O(\alpha^6)
=\frac{\alpha^4}{45}+O(\alpha^6), \tag{15}
\]
since \(\operatorname{Var}(T^2)=1/5-1/9=4/45\). Multiplying by \(4C^2\), then substituting \(\alpha=\pi g/(nm)\), proves (7). In the two comparison sequences \((k,k)\) and \((k,k+1)\), respectively \(g=k\) and \(g=1\), proving the stated difference of four powers.

## Verification
The accompanying standalone `verify.py` constructs vertex lists of both polygons, sums **all** pairs of vertices, and independently computes the convex hull area using the Qhull library rather than using support functions or the mixed-area derivation. It checks \(3\le n,m\le20\), twelve deterministic pseudorandom angles and radius pairs per order pair, a total of 3,888 independent convex-hull comparisons, with maximal observed relative error under \(8\times10^{-16}\). It also checks peak and trough orientations, a uniform-angle midpoint quadrature for the first two moments, and reproduces selected published fixed-orientation numerical excluded-area values to their stated precision. Reproduce with Python 3, NumPy and SciPy using `python verify.py`.

This finite regression check does not constitute a proof for unbounded polygon orders or all real angles. The proof of the latter is the exact finite trigonometric reduction (8)–(12); the probability statement follows from elementary measure transport.

## Relationship to prior work
Baram, Fogel, Hemmer, Halperin and Morr (2015), arXiv:1502.06195, develop algorithms for exact polygon Minkowski sums; their full manuscript describes sorted-edge merging for convex inputs but no arithmetic-resonance angular law or random-orientation distribution. Geigenfeind and de las Heras (2019), arXiv:1902.05961, study orientation-dependent excluded areas. Their full text explicitly compares analytic expressions for congruent equilateral triangles and squares and numerical profiles for regular pentagons and hexagons; those cases are **prior coverage**, not separately claimed as new here. The complete all-pairs formula and \(\gcd(n,m)\)-controlled random law are not given in the inspected paper.

Moud (2026), arXiv:2606.21812, evaluates fixed-orientation excluded areas for equal-area regular polygons and tabulates many pairs of orders; its full text gives exact self-pair parity formulas. Those fixed-angle values and parity identities are covered prior results; the present claim is the full two-order **orientation-dependent** profile, its law and precise arithmetic variance rate. A representative published mixed-pair table value is reproduced by the formula. The listed published geometric results on harmonic–arithmetic regular-polygon symmetrization, translative convex-hull ratios, repeated random rotations and intersections, and rotational Minkowski averages of Reuleaux triangles concern different objects or operations; their full-result statements do not imply (1)–(7).

## Limitations
No assertion of a novel convex-polygon Minkowski-sum algorithm, a novel mixed-area identity, or novel low-order triangle/square fixed-orientation formulas is made. The distribution assumes Haar-uniform *relative* rotation; orientation bias changes the law. The result is for two regular Euclidean polygons, not general equiangular or irregular polygons, and it does not solve particle-packing or many-body phase behavior. A prior equivalent all-pairs expression in older integral-geometry, hard-particle virial-coefficient, or computational-geometry literature cannot be ruled out without independent historical-priority assessment. Independent audit has not been performed.

## References
1. A. Baram, E. Fogel, M. Hemmer, D. Halperin, S. Morr, *Exact Minkowski Sums of Polygons With Holes*, arXiv:1502.06195v1, publicly submitted 2015-02-22. https://arxiv.org/abs/1502.06195
2. T. Geigenfeind, D. de las Heras, *The excluded area of two-dimensional hard particles*, arXiv:1902.05961v1, publicly submitted 2019-02-15. https://arxiv.org/html/1902.05961v1
3. A. Abbasi Moud, *Saturation Coverage in Binary Mixtures of Oriented Regular Polygons via Random Sequential Adsorption*, arXiv:2606.21812v1, publicly submitted 2026-06-20. https://arxiv.org/abs/2606.21812
4. *Exact translative convex-hull profile of every regular polygon*, published-finding corpus record 2026/10/11/SCOPE-exact-translative-convex-hull-profile-of-every-regular-polygon--79b005afe9c0.
5. *Exact rotational Minkowski-average area profile of the Reuleaux triangle*, published-finding corpus record 2026/10/11/SCOPE-exact-rotational-minkowski-average-area-profile-of-the-reuleaux--53c190e0340e.

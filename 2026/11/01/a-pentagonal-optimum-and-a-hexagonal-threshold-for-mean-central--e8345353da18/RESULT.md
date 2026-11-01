# A pentagonal optimum and a hexagonal threshold for mean central sections of regular prisms

## Finding

Let \(n\ge5\) be an integer, and let \(h>0\). Form the right regular \(n\)-gonal prism
\[
P_{n,h}=\operatorname{conv}\left\{\left(\cos\frac{2\pi j}{n},\sin\frac{2\pi j}{n},\pm h\right):0\le j<n\right\}\subset\mathbb R^3.
\]
Choose a unit normal \(U\) uniformly on the sphere and let \(N_{n,h}\) be the number of vertices of the central polygon \(P_{n,h}\cap U^\perp\). The value is unambiguous almost surely.

**Theorem (exact expectation and sharp phase transition).** For every integer \(n\ge5\) and \(h>0\),
\[
\boxed{\mathbb E N_{n,h}=\frac{2n}{\pi}\left[\arctan h+2\arcsin\!\left(\frac{\sin(\pi/n)}{\sqrt{1+h^2}}\right)\right].}
\tag{1}
\]
The function \(h\mapsto\mathbb E N_{n,h}\) has the following complete extremal classification.

* For \(n=5\), it has **exactly one global maximum** at
  \[
  \boxed{h_*=\frac{3+\sqrt5}{4},\qquad \mathbb E N_{5,h_*}=\frac{10}{\pi}\left[\arctan\frac{3+\sqrt5}{4}+2\arcsin\sqrt{\frac{3-\sqrt5}{6}}\right]=5.246274819729384\ldots.}
  \tag{2}
  \]
  It increases strictly below \(h_*\) and decreases strictly above \(h_*\).
* For every \(n\ge6\), the expectation increases **strictly** for all finite \(h>0\), from an unattained limiting value \(4\) to an unattained limiting supremum \(n\).
* The borderline case \(n=6\) has a different large-height approach rate from all \(n\ge7\):
  \[
  \boxed{6-\mathbb E N_{6,h}=\frac{3}{2\pi h^3}+O(h^{-5})\quad(h\to\infty),}
  \tag{3}
  \]
  whereas for every fixed integer \(n\ge7\),
  \[
  \boxed{n-\mathbb E N_{n,h}=\frac{2n}{\pi}\left(1-2\sin\frac\pi n\right)\frac1h+O_n(h^{-3})\quad(h\to\infty).}
  \tag{4}
  \]
The unique finite maximizer at five sides and the cancellation of the linear approach term at six sides are the two geometric regimes of this theorem.

## Assumptions and scope

The base vertices lie on the unit circle in the horizontal plane, so the base circumradius is one and the **total height is \(2h\)**. The symbol \(h\) always denotes half-height divided by base circumradius, not side-edge length or total height. The chosen plane passes through the centroid of the prism, and its unoriented normal is rotation-invariant (Haar measure). This is **not** a law of randomly translated planes or affine stereological sampling.

For a generic plane, the intersection is a two-dimensional convex polygon, and each section vertex is the transverse intersection with an original prism edge. The exceptional directions for which the plane contains a prism vertex or an original edge have spherical area zero. The theorem concerns the **expected** section vertex count, not the distribution of the complete section combinatorial type or its metric shape. The index restriction \(n\ge5\) is part of the assertion; no novelty is claimed for triangular-prism or rectangular-box cases.

## Proof

**1. Edge crossing and spherical angular probability.** Let \(a,b\in\mathbb R^3\setminus\{0\}\) be the endpoints of a polytope edge, and let \(\theta=\arccos\bigl(\langle a,b\rangle/(\|a\|\|b\|)\bigr)\in[0,\pi]\). Apart from a measure-zero set of normals, the plane \(U^\perp\) intersects the relative interior of this edge if and only if \((U\cdot a)(U\cdot b)<0\). Orthogonal projection of the isotropic direction \(U\) onto \(\operatorname{span}\{a,b\}\) has uniformly distributed direction. In the resulting circle, the two sign-disagreement arcs have combined angular length \(2\theta\); therefore
\[
\mathbb P\bigl((U\cdot a)(U\cdot b)<0\bigr)=\frac\theta\pi. \tag{5}
\]
A generic central section vertex lies on one and only one edge of \(P_{n,h}\), and each such transverse crossed edge produces a section vertex. Hence, by linearity of expectation, \(\mathbb E N_{n,h}\) is the sum of (5) over all \(3n\) edges of the prism; no independence of crossing events is required.

**2. The two edge orbits.** Write \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\). For each of the \(n\) vertical edges, the endpoints are \((v_j,h)\) and \((v_j,-h)\), with angle
\[
\theta_{\rm vert}=2\arctan h. \tag{6}
\]
For each of the \(2n\) edges in the top and bottom regular polygons, the endpoint vectors have common squared norm \(1+h^2\) and mutual dot product \(h^2+\cos(2\pi/n)\). Thus
\[
\theta_{\rm rim}=2\arcsin\left(\frac{\sin(\pi/n)}{\sqrt{1+h^2}}\right). \tag{7}
\]
The arcsine lies in its principal interval since \(h>0\). Summing \(n\theta_{\rm vert}/\pi+2n\theta_{\rm rim}/\pi\) proves (1). Continuity and \(\arcsin\sin(\pi/n)=\pi/n\) give \(\lim_{h\downarrow0}\mathbb E N_{n,h}=4\); the opposite limit is \(n\).

**3. Exact derivative and the five-versus-six threshold.** Put \(s=\sin(\pi/n)\) and \(c=\cos(\pi/n)>0\). Differentiating (1) gives
\[
\frac{d}{dh}\mathbb E N_{n,h}=\frac{2n}{\pi(1+h^2)}\left(1-\frac{2sh}{\sqrt{h^2+c^2}}\right).\tag{8}
\]
The function \(q(h)=h/\sqrt{h^2+c^2}\) is strictly increasing from zero toward one on \((0,\infty)\). For \(n\ge6\), \(2s\le1\) and \(q(h)<1\), so the factor in parentheses is strictly positive for every finite \(h\). This proves the stated monotonicity and strict upper bound \(\mathbb E N_{n,h}<n\).

For \(n=5\), \(2s>1\). Since \(q\) is strictly increasing, (8) vanishes exactly once, at
\[
h=\frac{c}{\sqrt{4s^2-1}}.
\]
The derivative is positive before and negative after this unique point, making it the unique global maximum. Using \(s^2=(5-\sqrt5)/8\) and \(c^2=(3+\sqrt5)/8\) gives \(h_*=(3+\sqrt5)/4\). Also
\[
\frac{s}{\sqrt{1+h_*^2}}=\sqrt{\frac{4s^2-1}{3}}=\sqrt{\frac{3-\sqrt5}{6}},
\]
which proves (2), including the exact expression for its attained maximum.

**4. Sharp large-height asymptotics.** As \(h\to\infty\), for fixed \(s\),
\[
\arctan h=\frac\pi2-\frac1h+\frac1{3h^3}+O(h^{-5}),\qquad
\arcsin\frac{s}{\sqrt{1+h^2}}=\frac{s}{h}+\frac{s^3/6-s/2}{h^3}+O(h^{-5}).
\]
Consequently
\[
\mathbb E N_{n,h}=n+\frac{2n}{\pi}\left[\frac{2s-1}{h}+\frac{1/3+s^3/3-s}{h^3}+O_n(h^{-5})\right].\tag{9}
\]
For \(n=6\), \(s=1/2\), so the coefficient of \(h^{-1}\) vanishes and the coefficient of \(h^{-3}\) inside the brackets is exactly \(-1/8\). Equation (3) follows. For \(n\ge7\), \(2s-1<0\), giving (4). All \(O\)-constants are for the indicated fixed integer \(n\). \(\square\)

## Verification

Run the self-contained Python 3 standard-library file `verify_prism_sections.py` from the same directory. It independently constructs the original edges and sums their actual three-dimensional endpoint angles, rather than using the trigonometric simplification in (1); it checks the unique pentagonal stationary point and derivative signs, the other dimensions' positive derivative signs, and the high-height asymptotic constants. An independently implemented random-plane edge-crossing counter checks (1) using \(260{,}000\) reproducible Gaussian normal directions. On execution it printed:

```
VERIFY_OK formula_direct_angles=42 derivative_and_asymptotic_checks=294 monte_carlo_normals=260000 max_absolute_sampling_error=0.016526
golden_ratio_half_height=1.309016994374947, pentagon_peak=5.246274819729384, n6_asymptotic_coefficient=0.477464829275686
```

The analytic proof above covers **all** integers \(n\ge5\) and all real \(h>0\). The finite checker does not certify the infinite quantifiers and should not be interpreted as independent mathematical validation.

## Relationship to prior work

Birkemeyer, Brose, Brandenburg and Prün [1] study combinatorial slice types, including a general proposition (their Proposition 3.6) reducing slices of a prism to slabs of the base. That structural statement does **not** assign Haar probabilities to sections or optimize an expected section complexity over height. The present theorem supplies the new probability-weighted integral evaluation and finds a sharp transition between the five- and six-sided regular bases.

For comparison, the published work *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes* [2] gives the two-point polygon-type law for **rectangular boxes** (the regular four-gon prism is the cube/box subfamily). It does not cover the non-centrally-symmetric regular pentagonal prism or any regular \(n\)-gonal prism with \(n\ge5\). The published work *Exact mean-square width of every uniform regular prism* [3] computes a second moment of support-function width, not the section vertex count. These two publicly accessible full texts were compared for mathematical implication, not merely their titles.

The classical stereological paper of Voss [4] treats polygon frequencies from randomly placed planes through crystalline aggregates, and Ohser–Mücklich [5] treat section statistics of a spatial ensemble of regular prisms. Those are generally **affine/offset section sampling** models rather than the Haar distribution of **central planes** here. Only accessible bibliographic material/abstracts for these two older works could be checked; their full mathematical scope remains a residual historical-priority risk. An existing general edge-angle identity could also be specialized to derive (1) without having previously recorded the five/six phase transition. Consequently the present originality claim is for the complete sharp height-extremum classification and its asymptotic transition, not for the elementary angular crossing lemma (5).

## Limitations

This theorem concerns only the *expected number of vertices* of sections through the **center** of a right regular prism, for \(n\ge5\). It does not give full probability distributions for possible polygon types, section areas, affine-offset section frequencies, or nonregular/oblique prisms. The formula is in the explicit half-height-to-circumradius normalization and is not a general affine-invariant assertion. The primary combinatorial slicing literature supplies context but not a claimed novelty guarantee; inaccessible older stereological literature can contain equivalent formulas. The proof is self-contained modulo elementary rotational symmetry, and the numerical experiments only test selected cases. Independent mathematical audit has not been performed.

## References

[1] A. Birkemeyer, A. E. Brose, M.-C. Brandenburg and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195v1 (first public 2026-09-14), especially Proposition 3.6, https://arxiv.org/abs/2609.16195.

[2] *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, publicly available complete mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.

[3] *Exact mean-square width of every uniform regular prism*, publicly available complete mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-mean-square-width-of-every-uniform-regular-prism--eb371b3be549.

[4] K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy 128 (1982), 111–120, https://doi.org/10.1111/j.1365-2818.1982.tb00443.x.

[5] J. Ohser and F. Mücklich, *Stereology for some classes of polyhedrons*, Advances in Applied Probability 27 (1995), 384–396, https://doi.org/10.2307/1427832.

# Exact uniform-edge chord law and quadratic mesh energy of random spherical polytopes

## Finding

Let \(n\ge4\) points be sampled independently and uniformly by spherical area on the Euclidean unit sphere \(S^2\), and let \(P_n\) be their Euclidean convex hull. Its boundary is almost surely simplicial with \(2n-4\) triangular facets and \(3n-6\) unoriented edges. After constructing \(P_n\), choose an edge *uniformly by count*, rather than proportionally to its length. Write \(L_n\) for the Euclidean chord length of that edge.

There are independent random variables \(B_n\sim\operatorname{Beta}(n-1,2)\) and \(U\), the latter supported on \((0,2)\), such that

\[
L_n\overset{d}=2\sqrt{B_n(1-B_n)}\,U,
\qquad
f_U(u)=\frac{2u^2}{3\pi\sqrt{4-u^2}}+\frac{u\bigl(\pi-2\arcsin(u/2)\bigr)}{3\pi}\quad(0<u<2).
\]

The law is exact for every integer \(n\ge4\), rather than just an asymptotic limit. In particular,

\[
\mathbb E[L_n^2]=\frac{20(n-1)}{(n+1)(n+2)},\qquad
\boxed{\mathbb E\biggl[\sum_{e\in E(P_n)}|e|^2\biggr]=\frac{60(n-1)(n-2)}{(n+1)(n+2)}.}
\]

The known expected Euclidean surface area of the same hull is \(4\pi(n-1)(n-2)/((n+1)(n+2))\) [1]. Thus the *ratio of expected values*, not the expectation of a per-realization ratio, is the universal constant

\[
\boxed{\frac{\mathbb E\bigl[\sum_e |e|^2\bigr]}{\mathbb E[\operatorname{Area}(\partial P_n)]}=\frac{15}{\pi}.}
\]

For a precise mesh-quality benchmark, every Euclidean triangular facet \(F\) obeys \(\sum_{e\subset F}|e|^2\ge4\sqrt3\operatorname{Area}(F)\), with equality for an equilateral triangle. Double-counting the edges gives the deterministic inequality \(\sum_e|e|^2\ge2\sqrt3\operatorname{Area}(\partial P_n)\). The ratio of the two expectations above, relative to this sharp local triangular benchmark, is exactly \(5\sqrt3/(2\pi)\), independently of the number of vertices.

The product law determines every nonnegative real moment:

\[
\mathbb E[L_n^q]=2^q\frac{\mathrm B(n-1+q/2,\,2+q/2)}{\mathrm B(n-1,2)}\int_0^2u^q f_U(u)\,du,\quad q\ge0.
\]

Finally, with \(G\sim\Gamma(2,1)\) independent of \(U\),

\[
\sqrt n\,L_n\ \Longrightarrow\ 2\sqrt G\,U\qquad(n\to\infty).
\]

## Assumptions and scope

All points are independent and area-uniform on \(S^2\), and all measurements use ambient Euclidean distances, not spherical geodesic distances. The sampled edge is uniform *conditional on the realized polytope*. Almost sure general position makes the face counts deterministic. The beta distribution uses shape parameters and has density \(n(n-1)b^{n-2}(1-b)\) on \((0,1)\). The gamma law has shape two and rate one. The theorem concerns integer \(n\ge4\); boundary degeneracies have zero probability.

## Proof

**1. From edges to facets.** Draw a uniform facet \(F\) of \(P_n\), then a uniform one of its three edges. Every edge belongs to exactly two facets, so every edge is chosen with probability \(2/[3(2n-4)]=1/(3n-6)\). Thus the edge-law calculation may be performed on one labeled side of a uniformly chosen triangular facet.

**2. Radial factor.** The spherical Blaschke–Petkantschin decomposition in [1, Section 4 and Equations (9)–(10), (42)–(44)] assigns the intensity of facets an area-weighted angular factor times a radial factor. If \(t\in(0,1)\) is the squared radius of the circle containing a facet, the radial intensity, up to its normalizing constant, is

\[
\frac{t\,dt}{\sqrt{1-t}}\left[\left(\frac{1+\sqrt{1-t}}2\right)^{n-3}+\left(\frac{1-\sqrt{1-t}}2\right)^{n-3}\right].
\]

Both terms count the mutually exclusive possibilities that the larger or smaller spherical circumcap contains no other sample point. On each branch substitute \(t=4b(1-b)\) and \(b=(1\pm\sqrt{1-t})/2\). The branches cover \((0,1/2)\) and \((1/2,1)\), respectively. Since \(|dt|/\sqrt{1-t}=4|db|\), the full radial measure is exactly proportional to \(16b^{n-2}(1-b)\,db\). Its integral is \(16\mathrm B(n-1,2)=16/[n(n-1)]\), so \(B_n\sim\operatorname{Beta}(n-1,2)\) and the planar circumcircle radius is \(2\sqrt{B_n(1-B_n)}\).

**3. Explicit angular factor.** By the same decomposition, the three angular positions of vertices on the unit circumcircle have density proportional to the Euclidean area of their triangle; this distribution is independent of \(B_n\). Rotate the first vertex to angle zero, and let the other two have angles \(\alpha,\beta\in(0,2\pi)\). The chord between the first two has length \(u=2\sin(\alpha/2)\), and the area is

\[
A(\alpha,\beta)=\frac{u}{2}\left|\cos(\beta-\alpha/2)-\cos(\alpha/2)\right|.
\]

Direct integration over \(\beta\) yields

\[
I(\alpha)=\int_0^{2\pi} A(\alpha,\beta)\,d\beta
=4\sin^2(\alpha/2)+(\pi-\alpha)\sin\alpha,
\quad \int_0^{2\pi}I(\alpha)\,d\alpha=6\pi.
\]

Hence the density of \(\alpha\) is \(I(\alpha)/(6\pi)\). The transformation \(u=2\sin(\alpha/2)\) is two-to-one away from the endpoints, with branches \(\alpha=2\arcsin(u/2)\) and \(2\pi-2\arcsin(u/2)\), and Jacobian magnitude \(2/\sqrt{4-u^2}\). Summing both contributions gives the asserted \(f_U\). It is nonnegative, integrates to one, has a finite limit at zero, and an integrable square-root singularity at two. Multiplying the independent radial and angular factors proves the full finite-sample law.

**4. Moments and mesh energy.** Using the integral for \(I(\alpha)\), one obtains \(\mathbb E[U]=128/(27\pi)\), \(\mathbb E[U^2]=5/2\), and \(\mathbb E[U^4]=70/9\). For example, \(u^2=2(1-\cos\alpha)\) and

\[
\int_0^{2\pi}u^4\,d\alpha=12\pi,\quad
\int_0^{2\pi}u^2(\pi-\alpha)\sin\alpha\,d\alpha=3\pi,
\]

so \(\mathbb E U^2=(12\pi+3\pi)/(6\pi)=5/2\). Also \(\mathbb E[4B_n(1-B_n)]=8(n-1)/((n+1)(n+2))\). The product gives \(\mathbb E L_n^2=20(n-1)/((n+1)(n+2))\). Since each polytope has \(3n-6\) edges, linearity of expectation yields the squared-edge sum. Dividing by the known expected area from [1, Equation (2)] gives \(15/\pi\). The local triangular benchmark follows from the Euclidean identity \(a^2+b^2+c^2\ge4\sqrt3\,A\), with equality precisely for equilateral triangles, and the fact that each edge belongs to two facets.

**5. Limiting law.** Set \(Y_n=n(1-B_n)\). Its exact density is \((n-1)y(1-y/n)^{n-2}/n\) for \(0<y<n\), which converges to \(ye^{-y}\), the \(\Gamma(2,1)\) density. Its limiting distribution is therefore \(G\). Independence of \(B_n\) and \(U\), the identity \(\sqrt n L_n=2\sqrt{Y_n(1-Y_n/n)}\,U\), and Slutsky's theorem give the claimed weak limit.

## Verification

A standalone checker `verify_random_edge_law.py` performs independent numerical quadrature of the angular density and its first, second and fourth moments. It verifies that for \(n=4\) the derived CDF reduces at five test points to the directly known uniform-pair chord law \(\Pr(L_4\le t)=t^2/4\). It separately reconstructs exact edge sets of the convex hulls of random points for four sample sizes and checks the predicted squared-edge sum and CDF. Running it with the dependencies in `requirements.txt` produced `ALL_SHAPE_DENSITY_CDF_AND_HULL_CHECKS_PASSED`.

The infinite-family result is established by the analysis above, **not** by the sampled convex hulls or any finite set of numerical tests.

## Relationship to prior work

Akopyan, Edelsbrunner and Nikitenko [1] provide the spherical Blaschke–Petkantschin decomposition, independence of facet shape and radius, the expected surface area, and a closed expected *total first-power* edge-length formula. Their complete primary manuscript was inspected, including Sections 4 and 6. These ingredients are fully credited. They do not give an evaluated normalized-chord density, the complete finite-sample uniform-edge length law, or the exact squared-edge-energy / expected-area invariant. The new statement is not inferred from a first moment alone; it requires the angular-law calculation and the second moment. Bonnet and O'Reilly [2] study the distribution of typical facet *height* and face counts, including asymptotics, but do not evaluate the angular factor required for uniform-edge lengths. Muche's Poisson–Voronoi typical-edge distribution [3] concerns edges of Voronoi cells, rather than the dual Delaunay/spherical convex-hull edges sampled here. Priority against all earlier or differently indexed literature remains provisional.

## Limitations

The theorem covers the unit two-sphere, independent uniform sampling, Euclidean chords, and edges sampled uniformly by count. It makes no claim about a length-weighted edge, about the variance of the *total* quadratic energy, nonuniform sampling, fixed-degree conditioning, or higher-dimensional polytopes. The limiting assertion is weak convergence, not a claimed quantitative rate or total-variation estimate. The independence of facet shape and radius is inherited from prior work; the evaluated angular density and metric consequences are the new portion. No independent mathematical audit has been performed.

## References

[1] Arseniy Akopyan, Herbert Edelsbrunner, Anton Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere*, arXiv:2007.07783v1, first public July 15, 2020; subsequent journal article, DOI 10.1080/10586458.2021.1980459. https://arxiv.org/abs/2007.07783

[2] Gilles Bonnet, Eliza O'Reilly, *Facets of spherical random polytopes*, Mathematische Nachrichten (2022), DOI 10.1002/mana.202000314. https://onlinelibrary.wiley.com/doi/full/10.1002/mana.202000314

[3] Lutz Muche, *The Poisson Voronoi Tessellation II. Edge Length Distribution Functions*, Mathematische Nachrichten 178 (1996), pp. 271–283, DOI 10.1002/mana.19961780113. (Only the bibliographic record and abstract were available in this comparison.)

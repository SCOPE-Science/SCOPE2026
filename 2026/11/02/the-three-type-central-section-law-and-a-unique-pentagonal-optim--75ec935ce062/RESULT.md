# The three-type central-section law and a unique pentagonal optimum for triangular prisms

## Finding

For every real \(h>0\), let \(P_h\subset\mathbb R^3\) be the right triangular prism with six vertices
\[
 v_j^{\pm}=(\cos(2\pi j/3),\sin(2\pi j/3),\pm h),\qquad j=0,1,2.
\]
Choose a plane through the origin by taking its unoriented normal uniformly from the sphere. Let \(N_h\) be the number of vertices of its nondegenerate polygonal section with \(P_h\). The exceptional normals for which the plane hits a prism vertex have probability zero. Almost surely \(N_h\in\{3,4,5\}\).

Set \(s=\sqrt{1+h^2}\) and define
\[
 A(h)=\arcsin\frac{1}{2s},\qquad
 B(h)=\arcsin\frac{\sqrt3}{2s},\qquad
 C(h)=\arcsin\frac{1}{s},
\]
where inverse sines take values in \([0,\pi/2]\). Then the complete distribution is
\[
 \begin{aligned}
 \Pr(N_h=3)&=1-\frac6\pi A(h),\\
 \Pr(N_h=4)&=\frac6\pi\bigl(2A(h)-2B(h)+C(h)\bigr),\\
 \Pr(N_h=5)&=\frac6\pi\bigl(2B(h)-A(h)-C(h)\bigr).
 \end{aligned}
\]
The pentagonal-section probability has a **unique global maximum** over all \(h>0\), at the unique positive solution \(h_*\) of
\[
 \frac{2\sqrt3 h_*}{\sqrt{4h_*^2+1}}-\frac{h_*}{\sqrt{4h_*^2+3}}=1.
\]
Numerically \(h_*=0.53146955106361159\ldots\) and
\[
 \max_{h>0}\Pr(N_h=5)=0.38515580567417676\ldots.
\]
Equivalently, because the base edge has length \(\sqrt3\) and the prism height is \(2h\), the maximizing height-to-base-edge ratio is \(2h_*/\sqrt3=0.6136881767453314\ldots\), **not** the equilateral-edged ratio \(1\).

The sharp thin- and long-prism limits are
\[
 \begin{aligned}
 \Pr(N_h=3)&=\frac{\sqrt3}{\pi}h^2+O(h^4),\\
 \Pr(N_h=5)&=\frac6\pi h-\frac{5\sqrt3}{\pi}h^2+O(h^3)
 \end{aligned}\qquad(h\downarrow0),
\]
and
\[
 \begin{aligned}
 \Pr(N_h=3)&=1-\frac3{\pi h}+O(h^{-3}),\\
 \Pr(N_h=4)&=\frac{12-6\sqrt3}{\pi h}+O(h^{-3}),\\
 \Pr(N_h=5)&=\frac{6\sqrt3-9}{\pi h}+O(h^{-3})
 \end{aligned}\qquad(h\to\infty).
\]

## Assumptions and scope

The prism is convex, right, equilateral-based, with circumradius one and arbitrary positive half-height \(h\). The cutting plane passes **through the geometric center**, without any random translation. Its unoriented normal is Haar-uniform. This is not the stereological distribution obtained by choosing an unrestricted translation-invariant random affine plane conditioned to hit the prism. The finite exceptional set of great-circle arcs where the plane contains a prism vertex is omitted (spherical measure zero). The formula gives all possible generic section side counts, not their metric areas or perimeters.

## Proof

**1. Reduction to signs and nine edges.** With normal \(u=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)\), identify \(u\) and \(-u\), and use the prism's reflection in its midplane to take \(0\le\theta\le\pi/2\). Put
\[
 c_j=\cos(\phi-2\pi j/3),\qquad t=h\cot\theta\ge0.
\]
For \(0<\theta<\pi/2\), the signs of the six plane functionals at the vertices are those of \(c_j+t\) on the upper triangle and \(c_j-t\) on the lower triangle. A generic plane meets each prism edge exactly when its endpoint signs differ. Distinct crossed edges give distinct polygon vertices by strict convexity of the section; there are three edges in each base and three vertical edges.

**2. Fundamental azimuthal sector and full enumeration.** Rotation and reflection symmetry of the equilateral base, together with reversing the horizontal normal (which preserves the section type after vertical reflection), reduces the uniformly distributed azimuth to \(0<\phi<\pi/6\), with density \(6/\pi\). Set
\[
 a=\cos(\phi+\pi/3),\quad b=\cos(\phi-\pi/3),\quad c=\cos\phi=a+b.
\]
Throughout this open sector \(0<a<b<c\), and the three horizontal vertex projections are \((c,-a,-b)\). The four disjoint intervals in the scalar \(t\) give the following crossing counts:

| Interval for \(t\) | Upper-base edge crossings | Lower-base edge crossings | Vertical edge crossings | Total \(N_h\) |
| --- | ---: | ---: | ---: | ---: |
| \(0<t<a\) | 2 | 2 | 0 | 4 |
| \(a<t<b\) | 2 | 2 | 1 | 5 |
| \(b<t<c\) | 0 | 2 | 2 | 4 |
| \(t>c\) | 0 | 0 | 3 | 3 |

This is exhaustive because the nine-edge graph contains all edges, and the equality thresholds have measure zero.

**3. Haar normalization and exact integration.** For the uniform unoriented plane normal, \(z=|\cos\theta|\) is uniform on \([0,1]\) and independent of \(\phi\). For every \(x>0\),
\[
 \Pr(t>x)=1-\frac{x}{\sqrt{h^2+x^2}}.
\]
Consequently,
\[
 \begin{aligned}
 \Pr(N_h=3)&=\frac6\pi\int_0^{\pi/6}
 \left(1-\frac{\cos\phi}{\sqrt{h^2+\cos^2\phi}}\right)\,d\phi,\\
 \Pr(N_h=5)&=\frac6\pi\int_0^{\pi/6}
 \left(\frac{b}{\sqrt{h^2+b^2}}-\frac{a}{\sqrt{h^2+a^2}}\right)\,d\phi.
 \end{aligned}
\]
The identity
\[
 \int\frac{\cos x\,dx}{\sqrt{h^2+\cos^2x}}=
 \arcsin\frac{\sin x}{\sqrt{1+h^2}}+\text{constant}
\]
produces the stated formulas for \(\Pr(N_h=3)\) and \(\Pr(N_h=5)\). Subtracting them from one gives \(\Pr(N_h=4)\). The integral representations separately establish nonnegativity; the probabilities sum to one.

**4. The unique optimum.** Differentiation gives
\[
 \frac{d}{dh}\Pr(N_h=5)=
 \frac6{\pi(1+h^2)}\left(1+\frac{h}{\sqrt{4h^2+3}}
 -\frac{2\sqrt3h}{\sqrt{4h^2+1}}\right).
\]
Define \(q(h)=2\sqrt3h/\sqrt{4h^2+1}-h/\sqrt{4h^2+3}\). Then
\[
 q'(h)=\frac{2\sqrt3}{(4h^2+1)^{3/2}}
 -\frac3{(4h^2+3)^{3/2}}>0
\]
for every \(h\ge0\), because \(2\sqrt3>3\) and the first denominator is smaller than the second. Also \(q(0)=0\), while \(\lim_{h\to\infty}q(h)=\sqrt3-1/2>1\). Thus there is exactly one solution \(q(h)=1\), with the derivative positive below it and negative above it. This proves strict global maximality, not merely local stationarity.

**5. Endpoint asymptotics.** Taylor expansion of the explicit inverse-sine formulas yields the thin limits. In particular \(C(h)=\pi/2-\arctan h\) for \(h>0\), explaining the linear pentagonal probability, whereas \(A(h)=\pi/6-h^2/(2\sqrt3)+O(h^4)\) and \(B(h)=\pi/3-\sqrt3h^2/2+O(h^4)\). At infinity, \(\arcsin(x)=x+O(x^3)\) and \(s=h+O(h^{-1})\), giving the three long-prism coefficients.

## Verification

The accompanying standalone `verify_prism.py` numerically integrates neither the exact formula nor its proof. Instead, it enumerates all nine original prism edges for a deterministic, equal-area spherical grid of normals and directly counts sign-changing edges. Across six positive half-heights it compares the independent counts to the three formula values; the maximum grid discrepancy was under \(0.000551\). It also checks the stated stationary root and thin-limit coefficients. Run with `python verify_prism.py` (Python 3 standard library only). This finite grid is corroboration and **not** an exhaustive proof for arbitrary directions; the exhaustive edge-sign argument above supplies that proof.

## Relationship to prior work

Stereological work on section-polygon frequencies predates this calculation. In particular, Voss (1982) gives an integral-geometric method and analytical frequencies for unspecified families of polyhedra, and Ohser–Mücklich (1995) consider randomly oriented regular-prism populations for reconstructing stereological size/shape distributions. Their setting principally allows random plane offsets; the present theorem fixes the cutting plane at the center and optimizes the pentagon probability as the prism aspect ratio varies. The complete text of Voss (1982) was unavailable for inspection, so whether it includes an intermediate equivalent fixed-center formula cannot be excluded. This is an explicit historical-priority risk, not a proof of novelty.

Hibi–Li (2014) classify vertex-preserving separating hyperplanes for cube-related and poset polytopes. Their definition concerns hyperplanes that do not create new edge-intersection vertices, unlike the generic sections computed here. Existing exact central-section laws for rectangular boxes and for right regular pentagonal prisms concern different face graphs and do not imply the triangular-prism three-type law or its optimum merely by substituting dimensions. No theorem asserting an unrestricted maximum over all prisms is claimed.

## Limitations

Only right prisms over equilateral triangles are covered. Results may change for oblique prisms, scalene base triangles, noncentral or non-Haar planes, or alternative section-sampling conventions. The historical-priority check for Voss's complete 1982 text remains unresolved. The program does not give machine-certified infinite proof and independent scientific audit has not been performed.

## References

- K. Voss, “Frequencies of n-polygons in planar sections of polyhedrons,” *Journal of Microscopy* **128** (1982), 111–120, DOI: 10.1111/j.1365-2818.1982.tb00443.x (abstract accessible; full text not inspected).
- J. Ohser and F. Mücklich, “Stereology for some classes of polyhedrons,” *Advances in Applied Probability* **27** (1995), 384–396, DOI: 10.2307/1427832 (abstract examined).
- T. Hibi and N. Li, “Cutting convex polytopes by hyperplanes,” arXiv:1402.3805, initially submitted 2014-02-16 (accessible HTML full text examined).

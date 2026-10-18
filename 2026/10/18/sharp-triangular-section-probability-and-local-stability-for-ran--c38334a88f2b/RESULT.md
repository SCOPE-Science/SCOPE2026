# Sharp triangular-section probability and local stability for random affine cuts of rectangular boxes

## Finding

For positive \(a,b,c\), let \(B(a,b,c)=[-a,a]\times[-b,b]\times[-c,c]\). A random affine plane is sampled using translation- and rotation-invariant plane measure, conditioned on meeting \(B(a,b,c)\). The probability \(P_3(a,b,c)\) that the section has exactly three vertices is

\[
P_3(a,b,c)=\frac{4}{a+b+c}\,\mathbb E\min\{a|U_1|,b|U_2|,c|U_3|\},
\qquad U\sim\operatorname{Unif}(S^2).
\]

For fixed positive sum of the half-side lengths, \(P_3\) is **strictly Schur-concave**: every nontrivial transfer making two unequal half-side lengths closer strictly increases the probability. Consequently the cube is the unique maximum up to common scale, and

\[
0<P_3(a,b,c)\le P_*:=2-\frac{4\sqrt2}{\pi}\arctan\sqrt2
=0.2798257232129537\ldots.
\]

The sharp range among genuine boxes is \((0,P_*]\); its zero infimum is approached by flattening any one side. There is also an exact local stability coefficient. For every fixed \(h\in\mathbb R^3\) with \(h_1+h_2+h_3=0\), and all sufficiently small \(\varepsilon\) for which the half-side lengths are positive,

\[
P_*-P_3(1+\varepsilon h_1,1+\varepsilon h_2,1+\varepsilon h_3)
= C\varepsilon^2\sum_{i=1}^3h_i^2+o_h(\varepsilon^2),
\]
\[
C=\frac{\arctan\sqrt2}{\pi\sqrt2}-\frac{1}{3\pi}
=0.1089184892037839\ldots>0.
\]

The constant is the exact isotropic Hessian coefficient at the cube, in the coordinates of fixed-sum half-side lengths.

## Assumptions and scope

An unoriented plane is the equivalence class of \((u,t)\in S^2\times\mathbb R\) under \((u,t)\sim(-u,-t)\), with equation \(u\cdot x=t\). The invariant measure is induced by surface measure \(d\sigma(u)\) times Lebesgue measure \(dt\), restricted and normalized to planes meeting \(B(a,b,c)\). In particular, conditional orientation is **not** uniformly distributed: directions are weighted by the width \(2(a|u_1|+b|u_2|+c|u_3|)\). Degenerate planes containing vertices or edges have measure zero.

Only three-dimensional rectangular boxes with positive side lengths and this precise affine-plane probability measure are covered. Schur comparison concerns the normalized vector \((a,b,c)/(a+b+c)\), not comparison at fixed volume or diagonal.

## Proof

**1. Width-weighted probability identity.** For fixed \(u\), the extremal support levels of the eight vertices are \(\pm s\), with \(s=a|u_1|+b|u_2|+c|u_3|\). The two extremal vertices are unique away from a null set of normals. The second level below the maximum is \(s-2m\), where \(m=\min\{a|u_1|,b|u_2|,c|u_3|\}\). Thus a plane gives a triangular section precisely when its offset lies in the two end intervals of total length \(4m\). All hitting offsets occupy length \(2s\). Since \(\mathbb E|U_i|=1/2\), integration over normals gives total hitting-plane measure proportional to \(a+b+c\), proving the stated identity. The identification can also be checked directly by observing that exactly the three edges incident to the extremal vertex are cut in either end interval.

**2. Shape rigidity and the full range.** Put \(F(a,b,c)=\mathbb E\min\{a|U_1|,b|U_2|,c|U_3|\}\). For each fixed normal the integrand is the minimum of three linear forms in the half-side lengths, hence concave. Uniform spherical measure makes \(F\) symmetric and homogeneous. Moreover averaging any unequal pair strictly increases \(F\). Indeed, if \(a>b\), compare \((a,b,c)\) with \((b,a,c)\). On a positive-measure open neighborhood where \(|U_1|\approx|U_2|\) and \(c|U_3|>\max\{a,b\}\max\{|U_1|,|U_2|\}\), the two endpoint minima select different coordinates, while the minimum at a nontrivial convex mixture is strictly larger than the mixture of those endpoint minima. Such neighborhoods exist by taking \(|U_1|,|U_2|\) sufficiently small. The same argument, with the crossing ratio adjusted, holds for every nontrivial pairwise balancing transfer. Therefore \(F\), and \(P_3=4F/(a+b+c)\) at fixed sum, is strictly Schur-concave. Averaging all permutations proves uniqueness of \(a=b=c\). The probability is positive on the positive cone and tends to zero as any one half-side length tends to zero with the other two fixed; continuity yields the claimed exact range.

**3. Exact cube value.** On the positive octant, symmetry partitions the sphere into six regions congruent to \(D=\{u_1\ge u_2\ge u_3\ge0\}\). Including signs yields \(48\) congruent sectors. On \(D\), the minimum coordinate is \(u_3\). Its spherical triangle has vertices \(v_1=(1,0,0)\), \(v_2=(1,1,0)/\sqrt2\), and \(v_3=(1,1,1)/\sqrt3\). For any oriented spherical patch \(D\), the spherical vector-area identity is

\[
\int_Du\,d\sigma(u)=\frac12\sum_{\text{oriented great-circle edges }(v,w)}
\frac{\arccos(v\cdot w)}{\|v\times w\|}(v\times w).
\]

For the indicated triangle, the third component is \(\pi/8-\phi/(2\sqrt2)\), where \(\phi=\arctan\sqrt2=\arccos(1/\sqrt3)\). Hence \(F(1,1,1)=48(\pi/8-\phi/(2\sqrt2))/(4\pi)\); multiplying by \(4/3\) gives \(P_*=2-4\sqrt2\phi/\pi\).

**4. Exact second variation.** For fixed \(h=(h_1,h_2,h_3)\), write \(F_h(\varepsilon)=F(1+\varepsilon h_1,1+\varepsilon h_2,1+\varepsilon h_3)\). Differentiating the piecewise-linear minimum under the sphere integral, its first derivative has no boundary term (the branches agree on ties). The second derivative receives negative contributions only from two-way ties \(|u_i|=|u_j|<|u_k|\). In distribution/coarea notation,

\[
F_h''(0)=-\sum_{i<j}(h_i-h_j)^2
\mathbb E\bigl[|U_i|^2\,\delta(|U_i|-|U_j|)\,\mathbf1_{\{|U_i|<|U_k|\}}\bigr].
\]

The triple-tie set consists of finitely many points; its \(O(\varepsilon^2)\) neighborhoods contribute \(O(\varepsilon^3)\) to the minimum integral and do not alter the second-order term. On each of the eight signed tie arcs, parameterize \((|u_i|,|u_j|,|u_k|)=(\sin\theta/\sqrt2,\sin\theta/\sqrt2,\cos\theta)\), with \(0\le\theta\le\phi\). The spherical gradient of \(|u_i|-|u_j|\) has length \(\sqrt2\) on the arc, and the spherical arclength element is \(d\theta\). Consequently each coefficient equals

\[
J=\frac{2}{\pi\sqrt2}\int_0^\phi\frac{\sin^2\theta}{2}\,d\theta
=\frac{\phi}{2\pi\sqrt2}-\frac{1}{6\pi}.
\]

Since \(\sum h_i=0\), the identity \(\sum_{i<j}(h_i-h_j)^2=3\sum_i h_i^2\) yields \(F_h''(0)=-3J\sum_i h_i^2\). Its linear term vanishes by permutation symmetry. Because \(a+b+c=3\) along this perturbation, multiplying the Taylor expansion by \(4/3\) gives the claimed coefficient \(C=2J\). The same coarea argument justifies twice differentiability at the balanced box and the little-oh remainder for each fixed \(h\).

## Verification

The accompanying standalone Python checker constructs a deterministic low-discrepancy grid of \(2^{18}\) spherical directions, evaluates the exact conditional-probability integral for the cube and asymmetric boxes, and compares two perturbative difference quotients with \(C\). The checker reports the stated constants. These finite calculations are corroboration only; Steps 1–4 prove the continuum theorem.

As a separate internal normalization check, each of the four box edges parallel to coordinate \(i\) meets a plane over an offset interval of length \(2a_i|u_i|\). Summing over all twelve edges and dividing by total hitting-plane measure gives the known exact expected section-vertex count \(\mathbb E N=4\), independent of box aspect ratio. This identity is not claimed as new.

## Relationship to prior work

Bray (2009), Chapter 10, treats motion-invariant random plane sections and obtains the regular **cube's** polygon-type probabilities. The symmetric cube endpoint is accordingly background, not an independent novelty claim here. The new theorem concerns **all** positive rectangular boxes, strict majorization with a unique extremal aspect ratio, and the exact second-variation coefficient. Birkemeyer–Brose–Brandenburg–Prün (2026), on combinatorial slicing hierarchies, and Brandenburg–Curtis–Giardino–Meroni–Padrol (2026), on cube-slice reconstruction, address which section combinatorics determine polytope properties, not this shape-optimized affine-plane probability. Other calculations of hexagonal **central** box sections use a different orientation law and conditioning, so neither their extremal values nor their implications cover this statement.

## Limitations

The exact probability formula remains a two-dimensional spherical expectation for a general box; no elementary closed form at arbitrary aspect ratios is asserted. The quadratic expansion is for fixed shape-perturbation vectors with zero sum and does not provide a universal, aspect-ratio-independent global quadratic remainder. The theorem does not address arbitrary affine images with sheared faces, random central sections, or offset laws different from invariant plane measure. Possible earlier equivalents under stereological terminology remain a bibliographic risk. A very closely related 2026 cube-slice reconstruction manuscript was available by abstract but not in full text for comparison.

## References

1. Brian Michael Bray, *Invariant measures on multifids of convex polytopes*, University of Wollongong doctoral thesis (2009), Chapter 10, pp. 109–118. Open-access text: https://scispace.com/pdf/invariant-measures-on-multifids-of-convex-polytopes-2szr2numek.pdf
2. Anna Birkemeyer, Anouk E. Brose, Marie-Charlotte Brandenburg, Niklas Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (first public September 14, 2026). https://arxiv.org/abs/2609.16195
3. Marie-Charlotte Brandenburg, Juliana Curtis, Chiara Giardino, Chiara Meroni, Arnau Padrol, *Reconstruction of slices of cubes*, arXiv:2610.09939 (first public October 7, 2026). https://arxiv.org/abs/2610.09939
4. Marie-Charlotte Brandenburg, Jesús A. De Loera, Chiara Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239 (2023). https://arxiv.org/abs/2304.14239

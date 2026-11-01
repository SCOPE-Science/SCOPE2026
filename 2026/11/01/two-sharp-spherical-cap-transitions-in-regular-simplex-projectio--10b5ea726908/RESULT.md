# Two sharp spherical-cap transitions in regular-simplex projection widths

## Finding

Let \(d\ge3\) be an integer. For the Euclidean regular \(d\)-simplex of unit edge length, let \(W\) be the length of its one-dimensional orthogonal projection in a direction uniformly distributed on \(S^{d-1}\). Define \(H_d(t)=\mathbb P(W\ge t)\), and set
\[
 a=\frac{\sqrt3}{2},\qquad b=\sqrt{\frac23},\qquad N=d(d+1),\qquad P=d(d+1)(d-1).
\]
Write \(I_z(p,q)=B_z(p,q)/B(p,q)\) for the regularized incomplete beta function. Put
\[
 C_d(t)=\frac12 I_{1-t^2}\!\left(\frac{d-1}{2},\frac12\right).
\]
For \(b\le t\le a\), define the nonnegative spherical-lens integral
\[
 L_d(t)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}
 \int_{t/a}^1(1-s^2)^{(d-3)/2}
 I_{\min\{1,\,4(as-t)^2/(1-s^2)\}}\!\left(\frac12,\frac{d-2}{2}\right)\,ds,
\]
with the endpoint at \(s=1\) interpreted by continuity. Then the **exact high-width law** is
\[
 \boxed{H_d(t)=\begin{cases}
 N C_d(t),&a\le t\le1,\\
 N C_d(t)-P L_d(t),&b\le t\le a.
 \end{cases}}
\]
In particular, a unit-edge regular tetrahedron has the exactly linear upper tail \(H_3(t)=6(1-t)\) on \(\sqrt3/2\le t\le1\).

The first overlap of the spherical caps occurs at \(t=a\); the first positive-measure triple overlap occurs immediately below \(t=b\). Both thresholds are exact and dimension-independent. Let \(\kappa_j=\pi^{j/2}/\Gamma(j/2+1)\) be the unit \(j\)-ball volume, and let
\[
 B_d=\frac{8\kappa_{d-2}}{d^2\kappa_d}\left(\frac4{\sqrt3}\right)^{(d-2)/2}.
\]
The sharp first-overlap asymptotic is
\[
 \boxed{H_d(a-\varepsilon)-N C_d(a-\varepsilon)
 =-P B_d\varepsilon^{d/2}+o_d(\varepsilon^{d/2})}\qquad(\varepsilon\downarrow0).
\]
The negative nonzero coefficient characterizes the first failure of the disjoint-cap formula.

## Assumptions and scope

The simplex is full-dimensional in its \(d\)-dimensional affine span, its edge length is exactly one, and directions follow normalized rotation-invariant surface measure. The variable \(t\) measures *projection length*, not the length of a random section, nor a planar-shadow area. All assertions concern fixed integer \(d\ge3\). The survival function is exact throughout \([b,1]\) but is not asserted to have this expression below \(b\), where triple intersections require further terms.

Let \(n=d+1\) and embed the simplex, after translation, as the convex hull of \((e_i-\mathbf1/n)/\sqrt2\) in the sum-zero hyperplane of \(\mathbb R^n\). A unit vector in this hyperplane represents a direction; directed edge normals are
\[
 r_{ij}=\frac{e_i-e_j}{\sqrt2},\qquad 1\le i\ne j\le n.
\]
Each directed root has Euclidean norm one, and the width is \(W(U)=\max_{i\ne j}\langle U,r_{ij}\rangle\).

## Proof

**1. Cap-union representation and its first contact.** Since the maximum and minimum of a linear functional on a simplex occur at vertices, \(W(U)=\max_{i\ne j}\langle U,r_{ij}\rangle\). Thus \(\{W\ge t\}\) is the union of \(N=n(n-1)\) spherical caps \(\{U:\langle U,r_{ij}\rangle\ge t\}\). Each cap has normalized measure \(C_d(t)\), as follows by integrating the density of a coordinate of a uniform point on \(S^{d-1}\).

For distinct directed roots \(r_{ij}\ne r_{kl}\), direct multiplication yields
\[
 \langle r_{ij},r_{kl}\rangle
 =\frac{\delta_{ik}-\delta_{il}-\delta_{jk}+\delta_{jl}}2
 \in\left\{-1,-\frac12,0,\frac12\right\}.
\]
The largest value is \(1/2\), attained exactly when the directed edges have the same initial vertex or the same terminal vertex. Two caps of angular radius \(\arccos t\) can overlap only when their centers' angular distance is at most twice that radius. The first possible overlap is consequently at \(t=\cos(\pi/6)=a\), and all caps are pairwise disjoint up to null boundaries for \(t\ge a\). This proves the first branch.

**2. Pair count and first triple threshold.** Each directed root has exactly \(2(n-2)\) distinct roots with inner product \(1/2\), hence the number of unordered such pairs is \(N(n-2)=P\). For \(t\ge b\), any simultaneously active pair \(v,w\) must have \(\langle v,w\rangle\ge 2t^2-1>0\). Indeed \(\langle U,v+w\rangle\ge2t\) and \(\|v+w\|^2=2+2\langle v,w\rangle\). Since the permitted distinct-root inner products have no value strictly between zero and one-half, an overlapping pair must have inner product \(1/2\). The same argument at \(t=b\) gives \(2b^2-1=1/3>0\), so the conclusion also holds at that endpoint.

Three distinct roots that are pairwise at inner product \(1/2\) all share one initial vertex or all share one terminal vertex: the directed-edge incidence formula above proves this by fixing the first root and checking the two allowed adjacency classes. For such a triple \(v_1,v_2,v_3\),
\[
 \left\|\sum_{j=1}^3v_j\right\|^2=6,
 \qquad 3t\le\left\langle U,\sum_{j=1}^3v_j\right\rangle\le\sqrt6.
\]
Thus triple intersection is impossible for \(t>b\), and at \(t=b\) is contained in the single direction parallel to the sum, a set of spherical measure zero. Conversely, when \(n\ge4\), three directed roots with common initial vertex exist. Their equal projection at the sum direction is exactly \(b\); a neighborhood of that direction lies in all three caps for every \(t<b\) close enough to \(b\). Hence the triple-overlap threshold is sharp, and inclusion–exclusion is exact through pairs on the entire interval \(b\le t\le a\).

**3. Explicit lens integral.** Take two roots \(v,w\) with \(\langle v,w\rangle=1/2\). Set
\[
 m=\frac{v+w}{\sqrt3},\qquad h=v-w;
 \quad v=a m+\frac12h,\quad w=a m-\frac12h.
\]
Here \(m,h\) are orthonormal. Conditioned on \(s=\langle U,m\rangle\), the point \(U\) has residual length \(\sqrt{1-s^2}\) uniformly distributed on the orthogonal \((d-2)\)-sphere, and
\[
 \min(\langle U,v\rangle,\langle U,w\rangle)
 =as-\frac12\sqrt{1-s^2}\,|Z|,
\]
where \(Z\) is one coordinate of a uniform unit point on \(S^{d-2}\). The density of \(s\) is \(\Gamma(d/2)(1-s^2)^{(d-3)/2}/(\sqrt\pi\Gamma((d-1)/2))\), and \(\mathbb P(|Z|\le z)=I_{z^2}(1/2,(d-2)/2)\) for \(0\le z\le1\). Both cap conditions are equivalent to \(s\ge t/a\) and \(|Z|\le2(as-t)/\sqrt{1-s^2}\). Integrating proves the stated exact expression for \(L_d(t)\). Multiplying by the counted pair number \(P\) completes the piecewise formula.

**4. Sharp cap-contact expansion.** Let \(t=a-\varepsilon\) and use orthonormal coordinates near the common cap-tangency direction \(m\):
\[
 U=\sqrt{1-p^2-\|z\|^2}\,m+p h+z,
 \qquad z\perp m,h.
\]
The lens inequality is exactly
\[
 a\sqrt{1-p^2-\|z\|^2}-\frac{|p|}{2}\ge a-\varepsilon.
\]
It forces \(|p|\le2\varepsilon\) and \(p^2+\|z\|^2\le 2\varepsilon/a\), so the entire lens lies in this chart for small \(\varepsilon\). Rescale \(p=\varepsilon x\), \(z=\sqrt\varepsilon\,y\). Its defining inequality converges to \(|x|/2+(a/2)\|y\|^2\le1\). The spherical area Jacobian is \((1-p^2-\|z\|^2)^{-1/2}\), tending uniformly to one on the rescaled bounded domain. Dominated convergence gives the normalized spherical lens measure
\[
 L_d(a-\varepsilon)\sim
 \frac{\varepsilon^{d/2}}{d\kappa_d}\int_{-2}^2
 \kappa_{d-2}\left(\frac2a\left(1-\frac{|x|}{2}\right)\right)^{(d-2)/2}\,dx.
\]
The integral is \((8/d)\kappa_{d-2}(2/a)^{(d-2)/2}\). Since \(2/a=4/\sqrt3\), this equals \(B_d\varepsilon^{d/2}\) after division by \(d\kappa_d\). The exact two-cap formula therefore has the claimed nonzero leading correction. Finally, \(C_3(t)=(1-t)/2\) gives the tetrahedral linear tail.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. It enumerates the directed-root Gram matrix for several dimensions, verifies all pair counts and the absence of triple intersections before the sharp threshold, and compares the exact one-dimensional lens integral to the independently derived local cap-contact coefficient. The checker reports `ALL_CHECKS_PASSED` when its finite cross-checks succeed. These finite checks are supportive, not substitutes for the argument above, which covers every integer \(d\ge3\).

## Relationship to prior work

Har-Peled and Robson (2023) classify minimum widths and minimizing directions of regular simplices, rather than their random-direction high-width distributions. Finch (2011) calculates first and second random widths for a regular tetrahedron and states that its density was not known in that work. Kabluchko, Litvak, and Zaporozhets (2015) give all higher width moments through a Gaussian-range representation, which determines the compactly supported law *implicitly*, but their formulas do not evaluate the explicit edge-root cap union or the two adjacent exact high-tail regimes and first-overlap coefficient.

The published cube width result `SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2` uses orthant-diagonal cap truncation; cube and simplex difference-body normal configurations are distinct, and its formula has no implication giving the simplex edge-root cap intersection counts. The published result `SCOPE-exact-third-order-union-formula-at-the-first-multiple-overlap-th--e4ea7f0caeb7` treats caps centered at *vertices of a regular simplex*, whose pairwise inner products are negative, rather than caps centered at the directed differences of simplex vertices. Neither published statement supplies the present two-regime upper tail.

## Limitations

The law is only asserted in the upper range \(b\le t\le1\) and does not determine the full width distribution. Below the second threshold, triple and higher cap intersections need additional analysis. The first-order coefficient gives a fixed-dimensional asymptotic and no dimension-uniform error bound is claimed. Implicit determination of the distribution by previously known complete moments is acknowledged. Absolute historical priority for an equivalent cap-union evaluation is not certified; independent external mathematical audit has not been performed.

## References

1. S. Har-Peled and E. W. Robson, *On the Width of the Regular n-Simplex*, arXiv:2301.02616 (first public January 6, 2023), https://arxiv.org/abs/2301.02616.
2. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (first public November 2015), https://arxiv.org/abs/1511.08479.
3. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671 (first public October 2011), https://arxiv.org/abs/1110.0671.
4. *Exact directional width law of the cube and its first spherical-cap transition*, indexed result `2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2`.
5. *Exact third-order union formula at the first multiple-overlap threshold for simplex-centred spherical caps*, indexed result `2026/10/4/SCOPE-exact-third-order-union-formula-at-the-first-multiple-overlap-th--e4ea7f0caeb7`.

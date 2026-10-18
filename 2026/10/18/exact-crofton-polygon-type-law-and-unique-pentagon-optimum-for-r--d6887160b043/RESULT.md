# Exact Crofton polygon-type law and unique pentagon optimum for right equilateral triangular prisms

## Finding
Let \(K_{s,h}\subset\mathbb R^3\) be a right prism with equilateral triangular bases of side length \(s>0\) and perpendicular separation \(h>0\). Select an unoriented affine hyperplane using Euclidean-motion-invariant measure, conditioned on intersecting the interior of \(K_{s,h}\), and write \(N\) for the number of vertices of the resulting polygon. Put \(x=h/s\), \(r(x)=\sqrt{1+x^2}\), and
\[
B(x)=\frac\pi2-2\arctan\left(\frac{x}{\sqrt3\,r(x)}\right),\qquad
\Psi(x)=\frac\pi2-\arctan\left(\frac{2x}{\sqrt3}\right)+\frac{\pi x}{6}-r(x)B(x).
\]
Then \(N\in\{3,4,5\}\) almost surely and the **complete** probability law is
\[
\begin{aligned}
p_5(x):=\Pr(N=5)&=\frac{12\Psi(x)}{\pi(3+2x)},\\
p_3(x):=\Pr(N=3)&=\frac{2x}{3+2x}+p_5(x),\\
p_4(x):=\Pr(N=4)&=\frac{3}{3+2x}-2p_5(x).
\end{aligned}
\]
The pentagon probability is strictly increasing and then strictly decreasing on \((0,\infty)\). Its unique global maximizer is the unique positive root \(x_*\) of
\[
(3+2x)\left(\frac\pi6-\frac{xB(x)}{r(x)}\right)=2\Psi(x).
\]
Numerically, \(x_*=0.47287604788115\ldots\) and \(p_5(x_*)=0.11265019621095\ldots\). These decimals approximate an analytically characterized unique optimum, not an independently certified interval solution.

## Assumptions and scope
The prism can be placed with base vertices \(v_j=(s/\sqrt3)(\cos(2\pi j/3),\sin(2\pi j/3))\), \(j=0,1,2\), and spatial vertices \((v_j,\pm h/2)\). Orientations have normals \(u\) distributed over \(S^2\), and offsets \(t\) have the invariant element \(d\sigma(u)\,dt\), restricted to \(\min_{y\in K_{s,h}}u\cdot y<t<\max_{y\in K_{s,h}}u\cdot y\). Thus the *conditional* orientation density is proportional to the directional width; taking a uniform orientation followed by a uniform intersecting offset without this width bias would be a different experiment. Normalization of \(d\sigma\) is immaterial. Generic cuts avoid vertices and edges with probability one.

## Proof
**1. Allowed polygon types and mean.** A generic plane meets at most one segment of the section from each of the prism's five facets, so \(3\le N\le5\). A section vertex is a crossed prism edge. With six base edges of length \(s\) and three lateral edges of length \(h\), the invariant integral of the number of crossed edges, averaged over unit normals, equals \((6s+3h)/2\), since \(\mathbb E_u|u\cdot e|=|e|/2\). The mean width is \(\overline w=3s/4+h/2\): the planar equilateral triangle contributes \((\pi/4)(3s/\pi)=3s/4\), and the height segment contributes \(h/2\). Hence
\[
\mathbb E N=\frac{12s+6h}{3s+2h}=\frac{12+6x}{3+2x}.
\]

**2. Exact pentagon offset interval.** Fix a normal, let \(z=|u_3|\), and order the three projected triangular-base levels as \(\alpha\le\beta\le\gamma\). The two triangular end facets are both cut precisely for offsets in \([\alpha+hz/2,\gamma-hz/2]\). All three rectangular lateral facets are cut precisely for offsets in \([\beta-hz/2,\beta+hz/2]\). Consequently the interval of pentagonal offsets has length
\[
L_5(u)=\left[\min\{\beta-\alpha,hz\}+\min\{\gamma-\beta,hz\}-hz\right]_+.
\]
For a horizontal unit normal of azimuth \(\phi\), let its consecutive ordered triangular projections have gaps \(a,b\ge0\). For a general normal with vertical coordinate \(z\), the gaps are \(\sqrt{1-z^2}\,a\) and \(\sqrt{1-z^2}\,b\). Write \(F_h(v)=v\arctan(h/v)\) for \(v>0\), with \(F_h(0)=0\). The positive-part decomposition of \(L_5\) and the elementary integral
\[
\int_0^1\left(hz-v\sqrt{1-z^2}\right)_+\,dz
=\frac h2-\frac{F_h(v)}2
\]
give, for each azimuth,
\[
\int_0^1 L_5(\phi,z)\,dz=\frac12\left(F_h(a)+F_h(b)-F_h(a+b)\right).
\]

**3. Angular integration.** By the dihedral symmetry, the full azimuth integral is twelve copies of the interval \(0\le\theta\le\pi/6\), where
\[
a=s\sin\theta,\qquad b=s\sin(\pi/3-\theta),\qquad a+b=s\sin(\pi/3+\theta).
\]
The mean pentagon offset length is therefore
\[
\overline L_5=\frac3\pi\int_0^{\pi/6}
\left[F_h(s\sin\theta)+F_h(s\sin(\pi/3-\theta))
-F_h(s\sin(\pi/3+\theta))\right]d\theta.
\]
Combining the first two intervals and subtracting the third makes the bracket integral equal to \(s\Psi(h/s)\). This follows either by direct differentiation in \(h\) with zero initial value, or by integrating \(s\sin y\arctan(h/(s\sin y))\) on \([0,\pi/3]\) minus its integral on \([\pi/3,\pi/2]\). Thus \(p_5=\overline L_5/\overline w=12\Psi(x)/(\pi(3+2x))\). The mean identity and \(p_3+p_4+p_5=1\), \(3p_3+4p_4+5p_5=\mathbb EN\), yield the displayed \(p_3,p_4\).

**4. The unique sharp optimum.** Differentiating the explicit expression (for \(x>0\)) gives
\[
\Psi'(x)=\frac\pi6-\frac{xB(x)}{r(x)},\qquad
\Psi''(x)=\frac{T(x)-B(x)}{r(x)^3},\qquad
T(x)=\frac{2\sqrt3\,x r(x)}{3+4x^2}.
\]
Here \(B'(x)=-2\sqrt3/[r(x)(3+4x^2)]<0\) and
\[
T'(x)=\frac{2\sqrt3(2x^2+3)}{r(x)(4x^2+3)^2}>0.
\]
Since \(T(0)=0<B(0)=\pi/2\) while \(T(\infty)=\sqrt3/2>B(\infty)=\pi/6\), \(\Psi''\) changes from negative to positive **exactly once**. Put \(D(x)=(3+2x)\Psi'(x)-2\Psi(x)\). Then \(D'=(3+2x)\Psi''\), \(D(0)=\pi/2>0\), and
\[
\Psi(x)\sim\frac{\sqrt3/4-\pi/12}{x},\qquad
D(x)\sim-\frac{4(\sqrt3/4-\pi/12)}x<0
\quad(x\to\infty).
\]
Hence \(D\) decreases and then increases toward zero from below: it has exactly one positive root. Since \(p_5'(x)\) has the sign of \(D(x)\), this root is the unique global maximum. The limits \(p_5(x)\to0\) both as \(x\downarrow0\) and \(x\to\infty\) are also immediate.

## Verification
The included `check_prism.py` (Python 3 standard library only) independently integrates the intersection of five face-offset intervals on a two-dimensional orientation grid at six positive height-to-side ratios, counts crossed edges of the actual three-dimensional prism at three further ratios using a seeded width-weighted random-plane experiment, and checks analytic derivatives, positivity, probability normalization, and the optimizer bracket. All its assertions passed. Numerical integration/simulation corroborates the analytical proof; it is **not** the argument for infinitely many heights or for uniqueness.

## Relationship to prior work
The 2026 combinatorial-slicing work of Birkemeyer, Brose, Brandenburg, and Prün studies which combinatorial information about sections determines a polytope, and contrasts central versus affine sections. It motivates asking for the entire probability law when affine hyperplanes carry invariant measure. Its accessible abstract does not state the present prism probability law, but the full manuscript was not accessible for inspection, so historical priority is not fully resolved. Brandenburg, De Loera, and Meroni's earlier work gives arrangement-based algorithms for optimizing polytope slices, not this explicit Crofton distribution or the unique height optimum in its accessible abstract. The geometric and measure-theoretic model here is different from central-section or random-planar-shadow statistics, even when those use other five-facet or five-vertex polyhedra.

## Limitations
This theorem applies to **right equilateral triangular prisms** and width-biased affine-hyperplane sampling in three dimensions. It does not cover arbitrary triangular prisms, uniformly oriented central cuts, random planar shadows, or higher-dimensional prism products. Numerical values quoted above are approximations. Search and accessible-source inspection do not establish absolute novelty; older integral-geometry tables and the inaccessible full text of a closely related recent paper remain bibliographic risks.

## References
1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, first publicly posted 2026-09-14.
2. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, *Mathematics of Computation* 94 (2025), 1003–1042; preprint arXiv:2304.14239, first posted 2023-04-27.

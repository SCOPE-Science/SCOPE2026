# Complete random-shadow law and a unique seven-vertex optimum for pentagonal bipyramids

## Finding

For each \(h>0\), let \(P_h\) be the convex hull in \(\mathbb R^3\) of the five points \((\cos(2\pi j/5),\sin(2\pi j/5),0)\), \(0\le j<5\), and the two apices \((0,0,\pm h)\). Let \(U\) be a Haar-uniform random unit vector; write \(N_h\) for the number of vertices of the orthogonal projection of \(P_h\) onto \(U^\perp\). The following formulas give its complete law for **every real \(h>0\)**.

Define
\[
r=\cos(\pi/5),\qquad \lambda=\frac{h}{\sqrt{h^2+r^2}},\qquad
S_k=\arcsin\!\left(\lambda\sin\frac{k\pi}{10}\right)\quad(0\le k\le5),
\qquad J_k=S_k-S_{k-1}\quad(1\le k\le5).
\]
Then, with probability one, \(N_h\in\{4,5,6,7\}\), and
\[
\begin{aligned}
\Pr(N_h=4)&=\frac{10}{\pi}J_5,\\
\Pr(N_h=5)&=1-\frac{10}{\pi}(J_1-J_4+J_5),\\
\Pr(N_h=6)&=\frac{10}{\pi}(J_1-J_2+J_3-J_4),\\
\Pr(N_h=7)&=\frac{10}{\pi}(J_2-J_3).
\end{aligned}
\]
Every one of these four probabilities is strictly positive for each finite positive \(h\). In particular, the probability that **all seven vertices appear in the shadow** is uniquely maximized at \(h=h_*\), where
\[
h_*=\frac{r\lambda_*}{\sqrt{1-\lambda_*^2}}
\]
and \(\lambda_*\in(0,1)\) is the unique root of
\[
\frac{2\sin(\pi/5)}{\sqrt{1-\lambda^2\sin^2(\pi/5)}}
=\frac{\sin(\pi/10)}{\sqrt{1-\lambda^2\sin^2(\pi/10)}}
+\frac{\sin(3\pi/10)}{\sqrt{1-\lambda^2\sin^2(3\pi/10)}}.
\]
Numerically, \(\lambda_*=0.6712912804\ldots\), \(h_*=0.7327181756\ldots\), and the maximal probability is \(0.08958840734\ldots\). The equilateral-faced Johnson pentagonal bipyramid has \(h=(\sqrt5-1)/2\), at which the seven-vertex probability is \(0.08797483032\ldots\).

## Assumptions and scope

The basal pentagon has circumradius one and the apices lie symmetrically on its perpendicular axis. Viewing directions are uniform on the sphere, and a shadow means an **orthogonal**, not perspective, planar projection. Statements about the number of distinct shadow vertices hold outside a measure-zero set of nongeneric directions. The parameter \(h\) ranges over all finite positive real numbers, and the limiting flat or infinitely tall shapes are not included in the quantifiers.

## Proof

**1. Affine reduction to a planar hull.** For any direction \(u=(u_x,u_y,u_z)\) with \(u_z\ne0\), parallel projection along \(u\) from three-space to the basal plane is an invertible affine image of the orthogonal shadow. It fixes the basal pentagon and maps the two apices to the opposite planar points \(\pm t(\cos\phi,\sin\phi)\), where \(t=h\sqrt{u_x^2+u_y^2}/|u_z|\); the sign labels are immaterial. Thus it preserves the polygon vertex count. We may take \(|u_z|\) uniformly distributed on \([0,1]\) and \(\phi\) uniform on \([0,2\pi)\), independently.

**2. Visible-edge chains.** The pentagon's five outward unit edge normals have arguments \(2\pi j/5\) after one fixed rotation, and all supporting edges are at signed distance \(r\) from the origin. Let \(k_+\) be the number of supporting inequalities violated by \(+t(\cos\phi,\sin\phi)\), and \(k_-\) the number violated by its negative. Each nonempty set of violated edges is a consecutive chain on the cyclic pentagon, while the two chains are disjoint. Adding an external point whose visible chain has \(k>0\) edges replaces the chain by two edges, adds the external point as one vertex, and deletes precisely \(k-1\) polygon vertices. The two antipodal visible chains cannot interfere beyond their retained common endpoints; they are disjoint as edge sets, and the two external points are separated by the pentagon's interior. Therefore the final number is exactly
\[
N_h=5+g(k_+)+g(k_-),\qquad g(0)=0,\quad g(k)=2-k\ (k\ge1).
\]
An edge with normal angle \(\beta\) is counted by \(k_+\) exactly if \(t\cos(\phi-\beta)>r\), and by \(k_-\) exactly if \(-t\cos(\phi-\beta)>r\). A single edge cannot be counted by both chains.

**3. The five ordered events.** Fivefold rotations, reflection, and exchange of the two apices reduce the azimuth integral to \(0<\phi<\pi/10\), with density \(10/\pi\). In this fundamental interval, the five absolute cosines for normals at \(0,\pm2\pi/5,\pm4\pi/5\) are strictly ordered as
\[
\cos\phi> -\cos(\phi+4\pi/5)>-\cos(\phi-4\pi/5)
>\cos(\phi-2\pi/5)>\cos(\phi+2\pi/5)>0.
\]
The corresponding edge violations occur in that order as \(t\) increases. Their signs are \(+,-,-,+,+\), so the successive values of \(N_h\) are
\[
5,\quad6,\quad7,\quad6,\quad5,\quad4.
\]
All equalities of the thresholds have probability zero. This also establishes the claimed support and the possibility of all four counts.

**4. Exact spherical integration.** For \(c>0\), the probability at fixed azimuth of violating an edge having absolute cosine \(c\) is
\[
G(c)=\Pr(t\ge r/c)=\frac{hc}{\sqrt{r^2+h^2c^2}}.
\]
An antiderivative of \(G(\cos x)\) on positive-cosine intervals is
\[
F(x)=\arcsin\!\left(\frac{h\sin x}{\sqrt{h^2+r^2}}\right).
\]
Integrating the five ordered event tails over \((0,\pi/10)\) gives, respectively, \(J_1,J_2,J_3,J_4,J_5\); the trigonometric complement identities telescope exactly to the stated \(S_k\). On that interval, the four required probabilities at fixed azimuth are \(G_5\), \(1-G_1+G_4-G_5\), \(G_1-G_2+G_3-G_4\), and \(G_2-G_3\), where subscripts refer to ordered thresholds. Integration proves all four formulas. Strict positivity follows from nonempty open threshold intervals for each polygon type.

**5. Unique optimal height.** Since \(\lambda\) increases strictly with \(h\), maximizing the seven-vertex probability is equivalent to maximizing
\[
\Psi(\lambda)=2\arcsin(b\lambda)-\arcsin(a\lambda)-\arcsin(c\lambda),
\quad a=\sin(\pi/10)<b=\sin(\pi/5)<c=\sin(3\pi/10).
\]
Put \(g_\lambda(x)=x/\sqrt{1-\lambda^2x^2}\). Its derivative in \(x\) is \((1-\lambda^2x^2)^{-3/2}\), and
\[
\Psi'(\lambda)=\int_a^b g_\lambda'(x)\,dx-\int_b^c g_\lambda'(x)\,dx.
\]
For \(0\le\lambda_1<\lambda_2<1\), the ratio \(g'_{\lambda_2}(x)/g'_{\lambda_1}(x)\) is strictly increasing in \(x>0\). Hence the ratio of the integral on \([b,c]\) to that on \([a,b]\) is strictly increasing in \(\lambda\). At \(\lambda=0\), the first integral exceeds the second, because \(2b>a+c\); this reduces by exact trigonometry to \(5>2\sqrt5\). At \(\lambda=1\), the inequality is reversed, since \(\tan(3\pi/10)+\tan(\pi/10)>2\tan(\pi/5)\); equivalently \(\cos^2(\pi/5)-\sin(\pi/5)\cos(\pi/10)=(3-\sqrt5)/8>0\). Thus \(\Psi'\) changes sign exactly once, from positive to negative. The root is the unique global maximum and defines \(\lambda_*\) and \(h_*\) unambiguously.

## Verification

Run `python3 check_pentagonal_bipyramid.py` with Python 3 and its standard library. The checker computes six all-height probability vectors, reconstructs \(240000\) independent random **orthographic** projected convex hulls, compares their vertex counts with the visible-edge criterion, and checks their empirical frequencies against the analytical probabilities. It also numerically isolates the unique stationary point and tests the derivative on both sides. These are reproducibility checks, not a substitute for the five-step proof above.

## Relationship to prior work

McGuire (2004) derived the general expected silhouette edge count from exterior dihedral angles; its first moment does not determine a four-point probability law or an optimizing aspect ratio. Glisse and Lazard (2007) established upper bounds on mean silhouettes of surface-approximating polyhedra. Black and Criado (2024) derived general expected random-shadow bounds for fixed polytopes. None of the inspected results states the complete four-atom random shadow law and sharp seven-vertex height optimum for pentagonal bipyramids. Close results for pyramids over rectangles and octahedral bipyramids concern different base polygons and do not imply this pentagonal claim. The available comparison does not certify historical priority.

## Limitations

The theorem concerns symmetric axial pentagonal bipyramids, not arbitrary seven-vertex polyhedra or asymmetric apices. It gives the side-count distribution, not the joint law with shadow area, perimeter, or metric shape. Nongeneric viewing directions have zero spherical measure and are not individually classified. Historical uniqueness of the result has not been independently established.

## References

1. Morgan McGuire, *Observations on Silhouette Sizes*, Journal of Graphics Tools **9** (2004), 1–12. DOI: 10.1080/10867651.2004.10487594.
2. Marc Glisse and Sylvain Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087, first posted 14 February 2007; later published in Discrete & Computational Geometry **40** (2008), 241–257.
3. Alexander E. Black and Francisco Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936 (11 June 2024).
4. *The Pentagonal Bipyramid* (Johnson solid J13), https://eusebeia.qfbox.info/4d/J13 (geometric background, not a source for the probability law).

# A unique maximal-section optimizer for every even regular polygonal prism

## Finding
Let \(n\ge6\) be even and let \(Q_n\subset\mathbb R^2\) be a regular \(n\)-gon with circumradius \(1\), centered at the origin. For \(h>0\), set
\[
P_{n,h}=Q_n\times[-h,h]\subset\mathbb R^3.
\]
Choose an unoriented central plane with Haar-uniform unit normal \(U\in S^2\), and let \(N_{n,h}\) be the number of sides of the section \(P_{n,h}\cap U^\perp\). Except on a sphere-null set of directions, every section has at most \(n+2\) sides. Write \(p_n(h)=\Pr\{N_{n,h}=n+2\}\). Then, for every even \(n\ge6\) and every \(h>0\),
\[
\boxed{p_n(h)=\frac n\pi\left[2\arcsin\left(\frac{\sin(\pi/n)}{\sqrt{1+h^2}}\right)-\arcsin\left(\frac{\sin(2\pi/n)}{\sqrt{1+h^2}}\right)\right].}
\]
This probability has a unique global maximum on \((0,\infty)\), attained at the exact half-height
\[
\boxed{h_n=\sqrt{3\cos^2(\pi/n)-1}.}
\]
Writing \(p_n^*=p_n(h_n)\), the optimal and edge-uniform prism probabilities obey the two different sharp limits
\[
\boxed{\lim_{n\to\infty\atop n\,\mathrm{even}}n^2p_n^*=\frac{2\pi^2}{3\sqrt3},\qquad
\lim_{n\to\infty\atop n\,\mathrm{even}}n^4p_n(\sin(\pi/n))=\pi^4.}
\]
Consequently \(p_n^*/p_n(\sin(\pi/n))\sim\frac{2}{3\sqrt3\pi^2}n^2\). The optimal full height is larger than the base edge length whenever \(n\ge6\), and its ratio to that edge length grows like \(\sqrt2\,n/\pi\). For a hexagonal base,
\[
\boxed{h_6=\frac{\sqrt5}{2},\qquad p_6^*=\frac6\pi\left[2\arcsin\frac13-\arcsin\frac1{\sqrt3}\right]=0.1226017195408906\ldots.}
\]

## Assumptions and scope
The base circumradius is fixed at \(1\), so \(2h\) is the full vertical height. The base edge length is \(2\sin(\pi/n)\); thus the conventional edge-uniform regular prism is represented by \(h=\sin(\pi/n)\). The normal has rotation-invariant spherical probability, not motion-invariant sampling of translated affine planes. The plane passes through the origin, the prism's center. The finitely many vertex-incidence great circles of exceptional directions have probability zero; no statement about degenerate sections on those circles is needed. All polygons and sections are Euclidean.

## Proof
**1. Maximum possible side count.** A generic planar section of any convex polyhedron has at most one section edge in each facet. The prism has \(n\) lateral facets and two caps, so its section has at most \(n+2\) sides. Each generic section vertex lies in the relative interior of an edge of the three-dimensional prism. It is therefore legitimate to count intersected prism edges by checking whether the linear functional defining the plane has strictly opposite signs at their endpoints.

**2. Exact event.** Write a generic unit normal as \(u=(\rho\cos\phi,\rho\sin\phi,z)\), with \(\rho=\sqrt{1-z^2}>0\). The \(n\) base vertex values of its horizontal component are \(\rho\cos(\phi-2\pi j/n)\). Put \(\lambda=h|z|/\rho\). By the prism's dihedral symmetry we may restrict \(\phi\) to \(0<\theta<\beta=\pi/n\). Because \(n\) is even, the base projection values form \(n/2\) antipodal pairs. Their largest and second-largest distinct absolute values are precisely
\[
t_1=\cos\theta,\qquad t_2=\cos(2\beta-\theta).
\]
For \(\lambda<t_1\), the central plane meets both cap interiors: exactly two edges of each base polygon cross it. Every antipodal pair of vertical edges contributes two section vertices if and only if its projected absolute value is less than \(\lambda\). Thus, if \(k\) of the \(n/2\) pairs satisfy this inequality, the section has \(4+2k\) vertices. For \(\lambda>t_1\) no cap edge is cut and all \(n\) vertical edges are cut, yielding exactly \(n\) vertices. It follows that the maximal section has \(n+2\) vertices if and only if
\[
\boxed{\cos(2\beta-\theta)<\frac{h|z|}{\sqrt{1-z^2}}<\cos\theta.}
\]
This is a necessary and sufficient event statement for all generic directions, not a finite-sampling observation.

**3. Integrating random orientations.** Under spherical Haar measure, \(\phi\) is uniform on \([0,2\pi)\), independent of \(|z|\), which is uniform on \([0,1]\). For \(t>0\),
\[
\Pr\left\{\frac{h|z|}{\sqrt{1-z^2}}<t\right\}=\frac{t}{\sqrt{h^2+t^2}}.
\]
There are \(2n\) congruent azimuth sectors of length \(\beta\), and hence
\[
p_n(h)=\frac n\pi\int_0^\beta\left[\frac{\cos\theta}{\sqrt{h^2+\cos^2\theta}}-\frac{\cos(2\beta-\theta)}{\sqrt{h^2+\cos^2(2\beta-\theta)}}\right]d\theta.
\]
The antiderivative on the relevant acute-angle range is
\[
F_h(t)=\arcsin\left(\frac{\sin t}{\sqrt{1+h^2}}\right),\qquad F_h'(t)=\frac{\cos t}{\sqrt{h^2+\cos^2t}}.
\]
The two terms integrate to \(2F_h(\beta)-F_h(2\beta)\), proving the exact arcsine law. Its integrand is strictly positive for almost every \(\theta\in(0,\beta)\), so the maximal-side event has positive probability at every positive height.

**4. Unique maximizing height.** Set \(s=\sin\beta\), \(c=\cos\beta\), and \(H=\sqrt{1+h^2}\). Direct differentiation gives
\[
\frac{dp_n}{dH}=\frac{2ns}{\pi H}\left[\frac c{\sqrt{H^2-4s^2c^2}}-\frac1{\sqrt{H^2-s^2}}\right].
\]
Every denominator and outer factor is positive for \(H>1\). Comparing squares shows that the expression in brackets is positive, zero, or negative exactly as \(3c^2-H^2\) is positive, zero, or negative. Indeed, the comparison reduces to
\[
c^2(H^2-s^2)\gtrless H^2-4s^2c^2
\quad\Longleftrightarrow\quad s^2(3c^2-H^2)\gtrless0.
\]
For even \(n\ge6\), \(3c^2\ge9/4>1\). Consequently exactly one critical point lies in \(H>1\), it is a strict maximum, the probability increases strictly before it and decreases strictly after it, and it is the unique global maximizer. Solving \(H^2=3c^2\) yields the claimed \(h_n\). In particular \(h_n^2-\sin^2\beta=2-4\sin^2\beta>0\) for \(n\ge6\), proving that the best prism is taller than an edge-uniform one.

**5. Two different high-side-count scales.** At the optimum \(H=\sqrt3\cos\beta\), Taylor expansion at \(\beta=0\) gives
\[
2\arcsin\left(\frac{\tan\beta}{\sqrt3}\right)-\arcsin\left(\frac{2\sin\beta}{\sqrt3}\right)
=\frac{2\beta^3}{3\sqrt3}+O(\beta^5).
\]
At the edge-uniform height \(h=\sin\beta\), expansion gives
\[
2\arcsin\left(\frac{\sin\beta}{\sqrt{1+\sin^2\beta}}\right)-\arcsin\left(\frac{\sin2\beta}{\sqrt{1+\sin^2\beta}}\right)
=\beta^5+O(\beta^7).
\]
Multiplication by \(n/\pi=1/\beta\) proves the two sharp limits and their ratio. Finally \(h_n\to\sqrt2\) and \(\sin\beta\sim\beta=\pi/n\), proving the optimal aspect-ratio statement.

## Verification
The standalone file `VERIFY.py` reconstructs the section vertex count independently from the sign changes on all \(3n\) edges of each prism. It compares this exact combinatorial test with the angular threshold event on 210,000 sampled unit normals, checks the arcsine expression against direct angular quadrature, verifies the optimized hexagonal benchmark, and checks the distinct quadratic and quartic asymptotic constants at increasing even values of \(n\). All checks passed in the prepared package. These finite tests corroborate, but do not establish, the universal identities; the five analytical proof steps above cover all permitted parameters.

## Relationship to prior work
Kovič (2013) classifies the centrally symmetric regular-faced polyhedra and explicitly includes the family of even regular prisms. The material examined concerns central symmetry and the associated projective maps, not random-section probabilities or optimal aspect ratios. The classical probability that a Haar-random central section of a cube is hexagonal is \(1-6\arcsin(1/3)/\pi\), recorded in OEIS A349605 and treated geometrically by Zhang (2020). The present formula reduces to that benchmark when \(n=4\) and \(h=1/\sqrt2\), but the theorem explicitly claims only the previously noncovered infinite family \(n\ge6\). An indexed existing result on rectangular-box sections likewise covers square-prism instances but does not imply a result for polygonal prisms with more than four base sides. By planar polarity, this central-section side-count law also describes the side counts of orthographic projections of the polar regular bipyramids; known four-vertex-base octahedral cases and isolated odd-base bipyramids do not imply the general even-base law. No priority claim is made beyond the available comparisons.

## Limitations
Only central Haar-uniform planes and even regular bases with at least six sides are covered. The theorem does not determine the full distribution of other section side counts, affine-plane sections at random offsets, nonregular or odd-sided bases, or arbitrary nonprismatic bodies. The historical-literature check includes a fully accessible text transcription of Kovič's article and indexed statements of related exact cubic results; not every potentially relevant work could be inspected in full. Independent mathematical validation has not been performed.

## References
- J. Kovič, *Centrally symmetric convex polyhedra with regular polygonal faces*, Mathematical Communications **18** (2013), 429–440. Journal record: https://www.mathos.unios.hr/mc/index.php/mc/article/view/177 ; archive: https://hrcak.srce.hr/110844 .
- Y. Zhang, *A purely 3-D geometrical solution to Mathematics Magazine Problem 2065*, arXiv:2010.12349 (2020), https://arxiv.org/abs/2010.12349 . (Cubic specialization only.)
- OEIS A349605, cube central-section hexagon probability, https://oeis.org/A349605 . (Cubic specialization only.)

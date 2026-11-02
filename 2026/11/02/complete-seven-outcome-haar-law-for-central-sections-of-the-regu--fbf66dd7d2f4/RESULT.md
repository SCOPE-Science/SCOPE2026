# Complete seven-outcome Haar law for central sections of the regular snub cube

## Finding

Let \(P\) be a regular snub cube centered at the origin and \(U\) be uniform on the unit sphere. For generic \(U\), let \(N(U)\) be the number of sides of the planar polygon \(P\cap U^\perp\). Then \(N\) takes **exactly** the seven values \(12,13,14,15,16,17,18\), each with positive probability. The exact distribution is given below; in particular, central sections with odd numbers of sides have positive probability.

Let \(t\in(0,1)\) be the unique root of \(t^3+t^2+t-1=0\), and put \(D=3+2t+2t^2\). For nonnegative integers \(a,b,c\) occurring in the display, write
\[
\Theta_{abc}=\arccos\!\left(\frac{a+bt+ct^2}{D}\right),\qquad A_j=4\pi\Pr(N=j).
\]
The complete exact probability law is
\[
\begin{aligned}
A_{12}&=12\pi-24\Theta_{122}-24\Theta_{223},\\
A_{13}&=48\Theta_{122}-48\Theta_{001}+48\Theta_{223},\\
A_{14}&=24\pi-24\Theta_{122}+48\Theta_{320}+48\Theta_{120}-48\Theta_{100}
 -24\Theta_{300}-24\Theta_{201}-96\Theta_{221}+48\Theta_{001}-24\Theta_{223},\\
A_{15}&=-144\pi+144\Theta_{221}+96\Theta_{100}+48\Theta_{300}
 +96\Theta_{201}+48\Theta_{001},\\
A_{16}&=72\pi-24\Theta_{100}-24\Theta_{300}-120\Theta_{201}
 -24\Theta_{241}-48\Theta_{001}+48\Theta_{221},\\
A_{17}&=-48\Theta_{100}+48\Theta_{241}+48\Theta_{201},\\
A_{18}&=-8\pi+24\Theta_{100}-24\Theta_{241}.
\end{aligned}
\]
Every angle argument belongs to \((0,1)\). The probabilities in increasing side-count order are approximately
\[
(0.102566341672,\ 0.036362455531,\ 0.341876773357,\ 0.274364999327,\ 0.220448968733,\ 0.007700607541,\ 0.016679853838).
\]
There are exactly \(482\) open spherical chambers in the central normal arrangement. Their counts by side number \(12,\ldots,18\) are \((6,48,108,192,72,48,8)\); chamber counts themselves are **not** the probabilities. Additionally the mean has the one-angle expression
\[
\mathbb E[N]=\frac{60}{\pi}\arccos\left(\frac{2+2t+t^2}{3+2t+2t^2}\right)
 =14.5635890358919\ldots .
\]

## Assumptions and scope

The chosen handedness of the regular snub cube does not matter because reflection preserves both the distribution of unoriented plane normals and section sidedness. The plane passes through the circumcenter. Generic means \(\langle U,v\rangle\ne0\) for every polyhedron vertex \(v\). The excluded normals form a finite union of great circles, of spherical probability zero. Each section has nonempty interior as a planar convex polygon.

We use the coordinate realization consisting of all even permutations of \((\pm1,\pm t,\pm t^{-1})\) with an even number of positive entries together with all odd permutations with an odd number of positive entries. Coordinate parity here is defined by inversion parity of the permutation. Since \(t^{-1}=1+t+t^2\), all coordinates lie in the cubic field \(\mathbb Q(t)\); uniform scaling does not affect the claimed law.

## Proof

**1. Exact face and edge structure.** Work in \(\mathbb Z[t]/(t^3+t^2+t-1)\). Form the 24 stated points. For each of the \(\binom{24}{3}=2024\) vertex triples, compute the cross product of two differences and test all 24 signed distances. Collect the supporting planes and their zero sets. The exhaustive exact tests yield \(32\) triangular facets and \(6\) square facets. Intersections of two facets in exactly two vertices yield \(60\) distinct edges; every vertex has degree five. All 24 vertices have squared radius \(D=3+2t+2t^2\); all edge endpoint dot products are \(2+2t+t^2\). These are exact finite identities certified by the accompanying reproducible checker, not floating-point hull calculations.

**2. Chord-count reduction.** For generic \(u\) the polygon's vertices are exactly the points where the plane \(u^\perp\) meets the relative interiors of polyhedral edges. Thus
\[
N(u)=\#\{\{i,j\}\in E:\langle u,v_i\rangle\langle u,v_j\rangle<0\},
\]
where \(E\) is the certified set of 60 edges. Its value is constant in each chamber of the \(24\) great circles \(\langle u,v_i\rangle=0\).

**3. Exhaustive spherical chambers.** Every arrangement vertex is an antipodal direction parallel to \(v_i\times v_j\) for some distinct pair. Evaluating the exact cubic-field signs shows that \(204\) unordered circle pairs have no additional coincident circle at their intersection, and the other \(72\) unordered pairs form \(12\) four-circle concurrence axes (\(6\) pairs per axis). Hence there are \(204+12=216\) distinct intersection axes, or \(432\) points on the sphere. The arrangement has \(912\) edges and therefore \(482\) faces by Euler's formula.

More constructively, at each intersection direction \(c\), enumerate the rays \(\pm(c\times v_k)\) over the incident circles. The exact oriented cross-product signs give all adjacent ray pairs. The sign vector in the intervening open angular wedge is determined by \(\operatorname{sign}\langle c,v_h\rangle\) for nonincident circles and \(\operatorname{sign}\langle r_a+r_b,v_h\rangle\) for incident circles. This enumerates every chamber because a spherical chamber is an intersection of open hemispheres, hence a convex spherical polygon with at least one arrangement vertex. Deduplication gives the chamber counts
\[
\begin{array}{c|rrrrrrr}
\text{sides}&12&13&14&15&16&17&18\\\hline
\text{chambers}&6&48&108&192&72&48&8.
\end{array}
\]
No other sidedness is possible. Every listed chamber is nonempty and open, so each has strictly positive spherical area.

**4. Exact area of every outcome.** At a normal-arrangement vertex, let two consecutive directed tangent rays be \(r_a=s_a(c\times v_i)\) and \(r_b=s_b(c\times v_j)\), with \(s_a,s_b\in\{\pm1\}\). The angle of their local chamber wedge obeys
\[
\cos\alpha=\frac{s_as_b\langle v_i,v_j\rangle}{D}.
\]
This follows because \(c\) is perpendicular to both incident vertex vectors, and the squared length of each vertex vector is \(D\). All ray adjacencies are verified by exact orientation determinants, independently of the floating-point sorting used only to propose their order.

There are \(1824\) corner incidences, broken down by outcome \(12,\ldots,18\) as \((48,144,480,624,336,144,48)\). Each chamber is a geodesically convex spherical polygon, so Girard's formula gives its area as the sum of interior angles minus \((m-2)\pi\), with \(m\) its number of arrangement vertices. Grouping all wedge angles by their exact dot products in \(\mathbb Q(t)\) and applying this formula produces the seven expressions \(A_j\) stated in the Finding. Division by the sphere's area \(4\pi\) gives their probabilities. This also proves that the displayed probabilities sum to one: the chambers partition the sphere up to great-circle boundaries.

**5. Independent first-moment identity.** Since every edge subtends the same angle \(\vartheta=\arccos((2+2t+t^2)/D)\) at the origin, a uniformly random central plane separates its two endpoints with probability \(\vartheta/\pi\). This is the ratio of the corresponding spherical lune area to \(4\pi\). Summing the 60 edge-crossing indicators yields the exact mean formula. Directly weighting the seven angle formulas by their side numbers agrees with it.

**Exactness of the finite computations.** The checker represents every field element as an integer triple \((a,b,c)\) for \(a+bt+ct^2\), reducing products by \(t^3=1-t-t^2\) and \(t^4=-1+2t\). The unique root is isolated by rational bounds
\[
\frac{543689012692076361570855971801}{10^{30}}
<t<\frac{543689012692076361570855971802}{10^{30}}.
\]
The cubic's derivative is strictly positive on this interval. Each nonzero sign is certified by comparing the rational evaluation at the lower bound with a derivative-times-interval-width bound; exact zero is detected by the zero triple. The program exhausts every triple of 24 vertices, every pair of 24 great-circle normals, and every adjacent local sector. These finite loops cover all the cases specified in the proof.

## Verification

Run `python3 verify_snub_sections.py` using the Python standard library. It checks the rational root isolator, all supporting-facet inequalities, the 60-edge reconstruction, the 24-circle arrangement, the 482 chamber sign patterns, each local wedge's exact adjacency, the seven spherical-area formulas, and the normalization and mean identities. It additionally draws 150,000 independent Gaussian directions as a non-proof numerical diagnostic. The exact categorical probabilities and the independent Monte Carlo estimates agree within the stated diagnostic tolerance; neither the theorem nor its exact probability law depends on simulation.

## Relationship to prior work

Berlow, Brandenburg, Meroni, and Shankar (2021) prove general finite chamber stability for central polyhedral sections (their Lemma 2.4), and provide concrete cube and icosahedron examples. Brandenburg, De Loera, and Meroni (2023) develop general slicing-chamber decompositions and algorithms, including experiments on Platonic solids and other named polytopes. Neither inspected source supplies the regular snub cube's seven-outcome Haar distribution or its exact spherical area coefficients. The Sage polytope library provides the exact snub-cube construction and standard face-vector facts but not these probabilities. The present claim specializes the general chamber principle to this chiral Archimedean solid and evaluates the resulting spherical geometry; the general existence of a finite decomposition alone does not imply the stated seven numerical probabilities without this exact computation.

## Limitations

The theorem concerns unoriented central planes and generic sections of a regular snub cube. No claim is made about off-center sections, exceptional planes containing vertices, area/perimeter distributions of sections, or arbitrary nonregular chiral polyhedra. Full historical priority cannot be guaranteed from available searchable sources, particularly older descriptive tables of Archimedean-solid sections. The exact finite certificate is computer-assisted, and independent human proof review has not been performed.

## References

1. K. Berlow, M.-C. Brandenburg, C. Meroni, I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996 (initial public posting 2021-10-12), especially Lemma 2.4 and the central-section examples. https://arxiv.org/abs/2110.05996
2. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239 (initial public posting 2023-04-27), especially Theorem 1.1, Section 2 and the computational examples of Section 5. https://arxiv.org/abs/2304.14239
3. SageMath, *Polytope Library*, entry `snub_cube(exact=True)`, for the standard algebraic coordinate realization and classical face vector. https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/library.html

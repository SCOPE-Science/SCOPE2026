# The full inradius law and two contrasting tails of random cyclic triangles

## Finding

Let \(P_1,P_2,P_3\) be independent points uniform by arclength on the unit circle, and let \(R\) be the inradius of their triangle. This result gives its exact distribution, not just its previously published first two moments. For \(0<t<1/2\), define

\[
 a_\pm(t)=\arcsin\left(\frac{1\pm\sqrt{1-2t}}2\right).
\]

Then

\[
\boxed{\Pr(R>t)=\frac8{\pi^2}\int_{a_-(t)}^{a_+(t)}
 \arccos\!\left(\sin x+\frac{t}{2\sin x}\right)\,dx.}
\]

The distribution is continuous and strictly increasing on its exact support \([0,1/2]\); outside the support the survival function is \(1\) for \(t\le0\) and \(0\) for \(t\ge1/2\). Its contrasting sharp endpoint laws are

\[
\boxed{\Pr(R\le t)\sim\frac6{\pi^2}t\log\frac1t\quad(t\downarrow0),}
\qquad
\boxed{\Pr(R>\tfrac12-\varepsilon)\sim\frac8{\pi\sqrt3}\varepsilon
\quad(\varepsilon\downarrow0).}
\]

The small-radius logarithm records triangles approaching degeneracy near the three simplex vertices. The linear upper tail records an isolated, nondegenerate quadratic maximum at the equilateral triangle.

## Assumptions and scope

The three points are **independent** and each is uniform with respect to **normalized arclength on the circumference**, not uniform in the disk. The circumradius of every nondegenerate sampled triangle is one. Coincident points have probability zero. The inradius is the ordinary radius of the largest inscribed disk. Throughout, logarithms are natural. The formulas specify one fixed sampling law; no assertion is made for random side lengths conditional on perimeter, disk-interior sampling, or arclength-nonuniform boundary laws.

## Proof

**1. Exact underlying measure.** Order the three sampled circular angles and form their consecutive circular gaps \(G_1,G_2,G_3\), including the wraparound gap. Their normalized lengths are Dirichlet \((1,1,1)\), equivalently uniform on \(G_i>0\) with \(G_1+G_2+G_3=2\pi\). The interior angles of the inscribed triangle are \(G_1/2,G_2/2,G_3/2\) up to permutation. Hence their half-angles \(X,Y,Z\) are uniform on

\[
 \mathcal T=\{(x,y,z):x,y,z>0,\ x+y+z=\pi/2\},
\]

with two-dimensional coordinate density \(8/\pi^2\) in \(dx\,dy\), taking \(z=\pi/2-x-y\). This follows equally by dividing each uniform circular gap by four. The total area of the projected simplex is \(\pi^2/8\), confirming normalization.

**2. Incircle geometry.** For a triangle of circumradius one, the standard half-angle identity gives

\[
 R=4\sin X\sin Y\sin Z.
\]

To see this directly, write the inradius as area divided by semiperimeter and apply the sine law plus half-angle product identities. The arithmetic–geometric mean inequality applied to \(\sin X,\sin Y,\sin Z\), or concavity of \(\log\sin\), shows that \(R\le1/2\), with equality only when all three half-angles equal \(\pi/6\). Values approach zero along every boundary edge of \(\mathcal T\), establishing the support endpoints.

**3. One-dimensional exact law.** Fix \(X=x\) and parametrize

\[
 Y=\frac{\pi/2-x}{2}+v,\qquad Z=\frac{\pi/2-x}{2}-v,
 \qquad |v|<\frac{\pi/2-x}{2}.
\]

The Jacobian is one. The product-to-sum identity yields

\[
 R=2\sin x\,[\cos(2v)-\sin x].
\]

Thus \(R>t\) if and only if

\[
\cos(2v)>\sin x+\frac{t}{2\sin x}.
\]

For \(t>0\), the admissible interval in \(v\) has length

\[
\arccos\left(\sin x+\frac{t}{2\sin x}\right)
\]

whenever the arccosine argument is strictly below one, and length zero otherwise. There is no clipping by the simplex boundary: since \(t>0\), its admissible half-width is strictly less than \((\pi/2-x)/2\), the half-width at \(t=0\). Writing \(s=\sin x\), the strict condition is \(2s(1-s)>t\), i.e. \((1-\sqrt{1-2t})/2<s<(1+\sqrt{1-2t})/2\). Integrating the admissible \(v\)-length against the density \(8/\pi^2\) proves the survival formula. It is strictly decreasing, since the preimage of every nonempty interior inradius interval has positive simplex area. Its endpoints satisfy \(\Pr(R>0)=1\) and \(\Pr(R>1/2)=0\).

**4. Thin-incircle asymptotic.** Fix \(0<\delta<\pi/12\), and examine a \(\delta\)-square around the simplex corner \(X=Y=0\). There \(Z=\pi/2-X-Y\) and

\[
R=4XY\,[1+O(\delta^2)]
\]

uniformly, since \(\sin X/X=1+O(\delta^2)\), likewise for \(Y\), and \(\sin Z=\cos(X+Y)=1+O(\delta^2)\). For fixed \(\delta\) and \(c\downarrow0\), the elementary hyperbolic sublevel area is

\[
\operatorname{area}\{0<x,y<\delta:xy\le c\}
=c\left[1+\log\left(\frac{\delta^2}{c}\right)\right]
\qquad(0<c<\delta^2).
\]

Therefore each corner contributes \((t/4)\log(1/t)\) in leading order as \(\delta\downarrow0\). Outside the three disjoint corner squares, at most one of the three half-angles can be small. On each remaining edge segment the other two sine factors are bounded away from zero by a constant depending on \(\delta\), so a sublevel strip has area \(O_\delta(t)\). Applying the same estimate in all three corners, multiplying by the constant simplex density \(8/\pi^2\), taking \(t\downarrow0\) first and \(\delta\downarrow0\) second, gives the coefficient \(3\cdot(1/4)\cdot(8/\pi^2)=6/\pi^2\). The multiplicative \(1+O(\delta^2)\) sandwiches have the same limit after \(\delta\downarrow0\). This is a two-parameter rigorous leading-order argument, not an assumption that a numerical logarithmic fit proves a tail.

**5. Equilateral upper tail.** In local coordinates \(u=X-\pi/6\), \(v=Y-\pi/6\), the dependent angle is \(Z=\pi/6-u-v\). Taylor expansion at the unique maximum gives

\[
R=\frac12-2(u^2+uv+v^2)+O((|u|+|v|)^3).
\]

The positive-definite quadratic form \(Q(u,v)=u^2+uv+v^2\) has determinant \(3/4\). Hence the ellipse \(2Q<\varepsilon\) has coordinate area \(\pi\varepsilon/\sqrt3\). Since the density is \(8/\pi^2\), and since the maximum is isolated in the compact closure of the simplex, the cubic remainder does not affect the limiting area ratio. This proves \(\Pr(R>1/2-\varepsilon)\sim 8\varepsilon/(\pi\sqrt3)\).

## Verification

Run `python inradius_law_check.py` with Python 3, NumPy, SciPy and mpmath. The independent checker compares explicit Cartesian triangle-area/perimeter inradii to the half-angle representation for 360,000 samples, checks five interior cumulative probabilities against unconstrained circular sampling, and numerically integrates the exact survival function to recover published mean and second moment. High-precision computations additionally check convergence toward the two endpoint constants. The observed checks completed as reported in `VERIFICATION.md`; Monte Carlo and finitely many quadrature evaluations are supporting checks, **not proofs of the asymptotic limits**. The proofs are the exact simplex calculation and the two local area estimates above.

For context, the earlier known moments are

\[
 \mathbb E[R]=\frac{12}{\pi^2}-1,\qquad
 \mathbb E[R^2]=\frac52-\frac{24}{\pi^2},\qquad
 \operatorname{Var}(R)=\frac32-\frac{144}{\pi^4}.
\]

These identities are reported as *previously known* and provide cross-checks; they are not part of the claimed original contribution.

## Relationship to prior work

Finch [1] specifies the same independent-uniform unit-circle triangle model and develops angle/side statistics without this inradius survival law. Madras and KC [2] study triangles chosen from regular polygon vertices and their limiting circle statistics, chiefly perimeter and area. Kórus [3] addresses **exactly this inradius sampling law** at the level of its expectation and variance, making it the closest substantive source: its complete four-page article does not establish the distribution function or the two sharp endpoint probabilities above. Labelle [4] studies a substantially different random-triangle law, uniform side-length triples at **fixed perimeter**, rather than independent vertices at **fixed circumradius**; thus even his complete inradius distribution under that other model cannot imply this one without a nontrivial change of measure absent from that work. Rao [5] treats Dirichlet circular spacings, a known input rather than new probability theory. The deterministic identity \(OI^2=1-2R\) in a unit-circumradius triangle shows that the law is equivalently a distribution for the incenter-to-circumcenter distance, but the cited sources do not provide either complete law. Checks for synonymous radius/distance descriptions and previous research records found no equivalent full distribution; this is a best-evidence novelty judgment, not an assertion of absolute historical priority.

## Limitations

The derivation is specific to independent points uniform on a unit circle; fixed-perimeter triangle models, disk-interior samples and nonuniform circular samples have different joint shape measures. The one-dimensional integral is an exact quadrature, **not** a claimed elementary closed-form cumulative distribution. The endpoint statements provide leading equivalent terms, not a proved full asymptotic expansion or uniform bounds over different sampling laws. Historical-priority search is finite, and further uncatalogued treatments of this classical model may exist. Independent mathematical validation has not been performed.

## References

[1] Steven R. Finch, *Random Cyclic Quadrilaterals*, arXiv:1610.00510, first posted 3 October 2016; particularly its introductory and retrospective discussion of uniform cyclic triangles. https://arxiv.org/abs/1610.00510

[2] A. Madras and S. KC, *Randomly Generated Triangles whose Vertices are Vertices of Regular Polygons*, Rose-Hulman Undergraduate Mathematics Journal **7** (2006), no. 2, article 12. https://scholar.rose-hulman.edu/rhumj/vol7/iss2/12/

[3] Péter Kórus, *Average Values of Triangles*, Fundamental Journal of Mathematics and Applications **3** (2020), 57–60, DOI:10.33401/fujma.692916. https://publicatio.bibl.u-szeged.hu/37060/1/2020.fujma.AverageValuesofTriangles.pdf

[4] Gilbert Labelle, *Probability distributions arising from isoperimetric random triangles*, Maple Transactions **3** (2023), no. 4, article 17136, DOI:10.5206/mt.v3i4.17136. https://mapletransactions.org/index.php/maple/article/download/17136/13056/44750

[5] J. S. Rao, *Some Tests Based on Arc-Lengths for the Circle*, Sankhyā B **38** (1976), 329–338, on uniform circular arc spacings. https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/1976_ArcLengthsCircle-Sankhya.pdf

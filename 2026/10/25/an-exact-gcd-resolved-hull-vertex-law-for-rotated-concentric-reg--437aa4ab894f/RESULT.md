# An exact gcd-resolved hull-vertex law for rotated concentric regular polygons

## Finding
For every pair of integers \(n\ge m\ge3\), an outer regular \(n\)-gon of circumradius \(1\), and an independently rotated concentric regular \(m\)-gon of radius \(0<\rho<1\), the total number \(V\) of vertices of their **convex hull** has an exact distribution supported on at most two adjacent values in an arithmetic progression. The law, its orientation-independent radii, and an arithmetic near-circle scaling limit are completely determined below.

Put \(a=\pi/n\), \(g=\gcd(n,m)\), and \(k=m/g\). Define
\[
 q=\begin{cases}
 0,&\rho\le\cos a,\\
 \arccos(\cos a/\rho)/a,&\cos a<\rho<1,
 \end{cases}\qquad t=kq,\quad j=\lfloor t\rfloor,\quad f=t-j.
\]
If the inner polygon's orientation is uniform on a full rotation, then, up to a probability-zero set of alignments,
\[
 \boxed{\mathbb P(V=n+gj)=1-f,\qquad \mathbb P(V=n+g(j+1))=f.}
\]
The second displayed mass is zero when \(f=0\); no vertices beyond \(n+m\) arise. Consequently
\[
 \boxed{\mathbb EV=n+mq,\qquad \operatorname{Var}(V)=g^2f(1-f).}
\]
All radii giving a deterministic vertex count are classified. The entire interval \(0<\rho\le\cos a\) gives \(V=n\). For each integer \(1\le j<k\), the distinct radius
\[
 \boxed{\rho_j=\frac{\cos a}{\cos(ja/k)}}
\]
gives \(V=n+gj\) for almost every rotation, and every radius strictly between these marked points and \(1\) that is not marked gives a genuinely two-valued law. The boundary \(\rho=1\), excluded by the hypotheses, gives \(n+m\) vertices for almost every rotation.

There is a sharp arithmetic limit near coincident circumcircles. Fix \(m\ge3\) and \(\lambda>0\). For integers \(n\to\infty\), \(n\ge m\), choose \(\rho_n=1-\lambda(\pi/n)^2\), retaining only indices with \(\rho_n\in(0,1)\). Along any subsequence with fixed \(g=\gcd(n,m)\), the excess \(V-n\) converges in distribution to the two-point law above with \(q\) replaced by
\[
 \boxed{q_\infty=\sqrt{(1-2\lambda)_+}}.
\]
In particular, for \(m=6\), \(\lambda=3/8\), the limiting excess is identically \(3\) along \(\gcd(n,6)=1\), but is \(0\) or \(6\), each with probability \(1/2\), along \(6\mid n\). Thus different arithmetical subsequences retain different nontrivial fluctuation laws even though their two circumcircles converge to the same limiting circle.

## Assumptions and scope
The two polygons are **planar**, closed, convex, regular and centered at the origin. The outer vertices are \(e^{2\pi i\ell/n}\), \(0\le\ell<n\); the inner vertices are \(\rho e^{i(\Theta+2\pi i/m)}\), \(0\le i<m\), where \(\Theta\) is uniform modulo \(2\pi\). All vertex counts refer to extreme points of the **joint convex hull**, not the union or intersection, and a zero-measure collinearity/tangency orientation is immaterial to the probability law. The restriction \(n\ge m\) is essential to the supporting-normal sufficiency step below. The dimensionless radial parameter satisfies \(0<\rho<1\), and \(n,m\) are otherwise arbitrary integers subject to the stated bounds.

## Proof
**1. Every outer vertex remains exposed.** For any outer vertex \(u\) with \(\|u\|=1\), the linear functional \(x\mapsto u\cdot x\) takes value \(1\) at \(u\), strictly less than \(1\) at the remaining outer vertices, and at most \(\rho<1\) on the entire inner polygon. Hence all \(n\) outer vertices are distinct extreme points of the joint hull.

**2. An exact criterion for an inner vertex to survive.** The outward facet normals of the outer regular \(n\)-gon have angles \((2\ell+1)a\) modulo \(2\pi\), and every corresponding support line has distance \(\cos a\) from the origin. Consider an inner vertex of argument \(\theta\). Let \(\delta\in[-a,a]\) be the signed angular distance between \(\theta\) and its nearest outer facet normal. Such a normal is unique except at finitely many angular ties. At that normal \(u\), the value of the inner vertex is \(\rho\cos\delta\), while the outer polygon support is exactly \(\cos a\).

If \(\rho\cos\delta\le\cos a\), then the inner vertex satisfies **all** outer facet inequalities: the nearest facet normal gives the largest dot product among the outer facet normals, so no other inequality is violated. The inner vertex therefore lies in the outer polygon and cannot be an extreme vertex of the enlarged hull, apart from an irrelevant boundary alignment.

Conversely, if \(\rho\cos\delta>\cos a\), then this inner vertex is exposed by the normal \(u\). Indeed, its angular separation from \(u\) is \(|\delta|<a=\pi/n\le\pi/m\). Among the \(m\) equally spaced inner vertices, it uniquely has the greatest dot product with \(u\), apart from a tie at the endpoint; moreover its dot product exceeds the entire outer polygon's support. Thus it is a strict exposed vertex of the joint hull. This proves the necessary and sufficient survival criterion
\[
 \rho\cos\delta>\cos a.
\]
If \(\rho\le\cos a\), no inner vertex survives. Otherwise define \(b=\arccos(\cos a/\rho)\); since \(\rho<1\) we have \(0<b<a\). The criterion becomes \(|\delta|<b\), an angular arc of length \(2b\) in each fundamental period of length \(2a\).

**3. Reduction to a rotated equally spaced lattice.** Reduce all \(m\) inner arguments modulo the facet-normal period \(2a=2\pi/n\). The increment \(2\pi/m\) modulo \(2\pi/n\) has order \(k=m/g\), with \(g=\gcd(n,m)\). The resulting multiset therefore consists of \(k\) equally spaced phases on this period, each repeated exactly \(g\) times. Because \(\Theta\) is uniform, the common phase offset is uniform in that period.

For a circle of circumference \(L\), the number of points of a uniformly shifted lattice of \(k\) equispaced sites falling in a fixed open arc of length \(qL\), \(0\le q<1\), equals \(\lfloor kq\rfloor\) or \(\lceil kq\rceil\), outside a finite set of offsets. Integrating indicator functions over the offset shows the expected number equals \(kq\); the only possible two integer counts must therefore have probabilities \(1-\{kq\}\) and \(\{kq\}\). Here the survival arc length fraction is \(q=b/a\). Multiplying the lattice count by the multiplicity \(g\), and adding the \(n\) always-exposed outer vertices, gives exactly the stated two-atom distribution, its expectation and its variance. This argument also covers \(k=1\) and \(q=0\).

**4. All orientation-independent radii.** The function \(q(\rho)\) is strictly increasing from \(0\) to \(1\) as \(\rho\) ranges over \((\cos a,1)\). The variance vanishes exactly when \(\{kq\}=0\), i.e. \(q=j/k\) for some \(1\le j<k\), and on the initial interval \(q=0\). Solving \(\arccos(\cos a/\rho)=ja/k\) gives the claimed \(\rho_j\). The upper endpoint \(q=1\) corresponds only to \(\rho=1\), outside the open radius interval. All remaining admissible radii have positive variance, so there are no further deterministic cases.

**5. Arithmetic near-circle limit.** With \(a_n=\pi/n\) and \(\rho_n=1-\lambda a_n^2\), elementary Taylor expansion gives
\[
 \frac{\cos a_n}{\rho_n}=1-(1/2-\lambda)a_n^2+O_\lambda(a_n^4).
\]
For \(0<\lambda<1/2\), the small-angle inverse cosine satisfies \(\arccos(1-z)=\sqrt{2z}\,[1+O(z)]\) and therefore \(q_n\to\sqrt{1-2\lambda}\). If \(\lambda>1/2\), then \(\rho_n<\cos a_n\) eventually, hence \(q_n=0\). At \(\lambda=1/2\), the same comparison gives \(q_n\to0\). Thus in all cases \(q_n\to\sqrt{(1-2\lambda)_+}\).

For fixed \(g\), the two-atom measure from Step 3 depends continuously on \(q\), including at integer values of \((m/g)q\) where one mass vanishes and the adjacent support shifts. Therefore the asserted subsequential distribution follows. With \(m=6\), \(\lambda=3/8\), the limit is \(q_\infty=1/2\); choosing \(g=1\) gives \(k=6\) and deterministic excess \(3\), whereas \(g=6\) gives \(k=1\) and Bernoulli excess \(0\) or \(6\), each of probability \(1/2\). This completes the proof.

## Verification
The standalone standard-library script `verification/check_hull.py` constructs independent convex hulls by a planar monotone-chain algorithm and compares the counts to the angular criterion and the exact two-point support over 15,000 seeded configurations. It additionally checks 4,290 exact deterministic-threshold samples, 19,200 phase-grid cases approximating the two probabilities, and near-circle sequences with different greatest-common-divisor classes. The supplied script was executed successfully with its final line `ALL_PLANAR_ROTATION_HULL_CHECKS_OK`. These finite checks corroborate the formulas but are not the justification for the all-parameter law; Steps 1–5 provide that argument.

## Relationship to prior work
Classical results on random convex-hull complexity, such as Har-Peled (2011), concern **independent sampled points** and expected asymptotic face counts, not the single globally rotated, rigid equispaced configurations here. Kiss and Vidnyánszky (2014) study areas and perimeter-to-area ratios of **unions** of congruent concentric rotated regular polygons; their equal-spacing radial geometry is related to our facet-normal reduction, but they do not establish a convex-hull vertex-count law for two different orders and circumradii. The O'Rourke–Zaimi 2015 discussion counts sides of the **intersection** of regular polygons with the same circumradius, and observes a greatest-common-divisor pattern. By polarity, its equal-circumradius setting does not directly cover the present unequal-radius convex hull family; neither the exact random two-atom distribution, the full deterministic-radius profile, nor its arithmetic critical scaling follows from its reported result. The lattice-in-arc floor/ceiling principle used here is classical and is not claimed as a newly invented lemma.

## Limitations
The theorem is restricted to two concentric regular polygons with the outer polygon having at least as many vertices as the inner one, a strictly smaller inner radius, and a uniform random relative rotation. It does not claim distributions for translations, off-center configurations, three or more independently rotated layers, or the unrestricted order \(n<m\). No full-text inspection was obtained for Har-Peled's early technical report, although its available abstract explicitly concerns independent sampling rather than the correlated rotation setting. Unindexed historical treatments of rotated concentric polygons may remain, and no independent mathematical audit has been performed.

## References
1. Sariel Har-Peled, “On the Expected Complexity of Random Convex Hulls,” arXiv:1111.5340v1, publicly posted 2011-11-22, https://arxiv.org/abs/1111.5340.
2. Viktor Kiss and Zoltán Vidnyánszky, “Unions of regular polygons with large perimeter-to-area ratio,” arXiv:1402.5452v1, publicly posted 2014-02-21, https://arxiv.org/abs/1402.5452 and full text https://arxiv.org/html/1402.5452v2.
3. Joseph O'Rourke and Gjergji Zaimi, “Intersection of rotating regular polygons,” MathOverflow, 2015-10-17, https://mathoverflow.net/questions/221120/intersection-of-rotating-regular-polygons.

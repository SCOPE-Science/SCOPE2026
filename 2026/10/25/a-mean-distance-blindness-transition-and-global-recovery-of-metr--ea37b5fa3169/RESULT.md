# A mean-distance blindness transition and global recovery of metric dumbbells

## Finding
Let \(G(a,b,c)\) be the compact length-metric graph made of two circular loops of lengths \(a,b>0\), joined at distinguished vertices by one bridge of length \(c>0\). Sample \(X,Y\) independently from normalized arclength on the entire graph, and write \(D=d_G(X,Y)\). Then the **global distribution of \(D\) determines \(\{a,b\}\) and \(c\)**, including equal loops and all positive bridge lengths.

In fact, the distribution is needed only to extract the total length \(L\), its support endpoint \(M\), and its first two moments \(\mu_1=\mathbb E D\) and \(\mu_2=\mathbb E D^2\). Define \(s=a+b\) and \(p=ab\). The geometric measurements recover
\[
L=\lim_{r\downarrow0}\frac{2r}{\Pr(D\le r)},\qquad
M=\sup\operatorname{supp}D=c+\frac{s}{2},\qquad
c=2M-L,\quad s=L-c.
\]
The first moment obeys
\[
L^2\mu_1=\underbrace{\frac{s^3}{4}+\frac{cs^2}{2}+c^2s+\frac{c^3}{3}}_{B_1(s,c)}
+\left(c-\frac{s}{4}\right)p. \tag{1}
\]
Thus, for \(c\ne s/4\), the product \(p\) is recovered by dividing \(L^2\mu_1-B_1(s,c)\) by \(c-s/4\). At the **sharp blindness ratio** \(c=s/4\), every choice of two positive loop lengths with the same sum has the same total length, diameter, and mean pair distance, regardless of their asymmetry. But then
\[
L^2\mu_2=B_2(s,c)+\frac{s^2p}{48}+\frac{p^2}{12},\qquad
B_2(s,c)=\frac{s^4}{12}+\frac{cs^3}{6}+\frac{c^2s^2}{2}+\frac{2sc^3}{3}+\frac{c^4}{6}. \tag{2}
\]
The right side is strictly increasing in \(p\in(0,s^2/4]\), so the second moment uniquely determines \(p\). In either regime, the unordered loop lengths are the roots of \(u^2-su+p=0\).

For fixed \(s,c\), equation (1) also gives a sharp shape-order reversal: balancing the loop lengths strictly **minimizes** average distance when \(c<s/4\), strictly **maximizes** it when \(c>s/4\), and has no effect on the average when \(c=s/4\).

## Assumptions and scope
All three edge lengths are finite and strictly positive. Each loop is a metric circle attached to exactly one endpoint of the bridge; there are no other edges or identifications. The graph is endowed with intrinsic shortest-path distance and normalized one-dimensional Hausdorff (arclength) measure, not with Euclidean embedding distance. Isometry may exchange the two loops. The endpoints and attachment vertices have zero sampling mass. No genericity, unequal-loop, or nonresonance hypothesis is imposed.

The statement is an **intra-family** injectivity theorem: it does not assert that the distance distribution identifies an arbitrary unknown metric graph's topology. All formulas are valid at coincident loop lengths, while positivity excludes contracted loops or bridge.

## Proof
**1. Pair-distance law.** Conditional on sampling a point on the first loop, its shortest arclength to the bridge attachment is uniform on \([0,a/2]\), since each interior distance from the attachment corresponds to two loop positions. The corresponding variable for the other loop is uniform on \([0,b/2]\). For two points on the same loop, their shortest circular separation is likewise uniform on the respective half-circumference. A point uniformly sampled on the bridge has distance to its first endpoint uniform on \([0,c]\).

Write \(\mathbf1_{[0,u]}\) for an interval indicator, and \(*\) for convolution of integrable functions on the real line. The density of \(D\), up to values at finitely many discontinuities, is **exactly**
\[
\begin{aligned}
L^2 f_D(t)={}&2a\,\mathbf1_{(0,a/2)}(t)+2b\,\mathbf1_{(0,b/2)}(t)
+2(c-t)\mathbf1_{(0,c)}(t)\\
&+4(\mathbf1_{[0,a/2]}*\mathbf1_{[0,c]})(t)
+4(\mathbf1_{[0,b/2]}*\mathbf1_{[0,c]})(t)\\
&+8(\mathbf1_{[0,a/2]}*\mathbf1_{[0,b/2]})(t-c),\qquad t>0.
\end{aligned} \tag{3}
\]
Indeed, the first two terms integrate over ordered pairs from the same loop, the third over ordered bridge pairs; the two coefficients \(4\) account for both orientations of a loop/bridge pair and two positions at a fixed attachment distance, and the coefficient \(8\) accounts for both orientations of a cross-loop pair and two positions on each loop. Integrating (3) gives \(1\), since the unnormalized masses are \(a^2+b^2+c^2+2ac+2bc+2ab=L^2\).

Every convolution in (3) vanishes at \(t=0\), while the other contributions tend to \(2a+2b+2c\); therefore \(f_D(0+)=2/L\). Since \(\Pr(D=0)=0\), the small-radius limit displayed in the finding follows. Any two points on opposite loops are separated by their distances to the two attachment vertices plus the full bridge. The maximum distance is consequently \(M=c+a/2+b/2\), attained between the two antipodal loop points. All other endpoint combinations are shorter because both loops have positive length. Continuity gives the support endpoint.

**2. Moment calculation.** Partition ordered pairs by the edges containing the two sampled points. In the following table, masses are *unnormalized* arclength-product masses, and the last two columns are the conditional expectations of \(D\) and \(D^2\). The notation \(AA,BB,CC\) denotes the two individual loops and the bridge, while \(AB\) or \(AC\) includes both orderings.

| Pair class | Mass | Conditional \(\mathbb E D\) | Conditional \(\mathbb E D^2\) |
|---|---:|---:|---:|
| \(AA\) | \(a^2\) | \(a/4\) | \(a^2/12\) |
| \(BB\) | \(b^2\) | \(b/4\) | \(b^2/12\) |
| \(CC\) | \(c^2\) | \(c/3\) | \(c^2/6\) |
| \(AC\) | \(2ac\) | \(a/4+c/2\) | \(a^2/12+ac/4+c^2/3\) |
| \(BC\) | \(2bc\) | \(b/4+c/2\) | \(b^2/12+bc/4+c^2/3\) |
| \(AB\) | \(2ab\) | \(c+(a+b)/4\) | \(c^2+c(a+b)/2+(a^2+b^2)/12+ab/8\) |

For instance, in class \(AB\), \(D=c+U+V\), where \(U,V\) are independent uniforms on \([0,a/2]\) and \([0,b/2]\). The other mixed rows follow from the same calculation; for class \(CC\), the absolute difference of two independent \(\mathrm{Unif}[0,c]\) variables has first two moments \(c/3\) and \(c^2/6\). Multiplying each row by its mass, summing, and using
\[
a^2+b^2=s^2-2p,\qquad a^3+b^3=s^3-3sp,\qquad a^4+b^4=s^4-4s^2p+2p^2
\]
proves (1) and the general identity
\[
L^2\mu_2=B_2(s,c)+p\left(-\frac{s^2}{6}+\frac{cs}{2}+c^2\right)+\frac{p^2}{12}. \tag{4}
\]
Putting \(c=s/4\) in (4) gives (2).

**3. Inverse and sharpness.** From the distribution, recover \(L,M\), hence \(c,s\). For \(c\ne s/4\), equation (1) recovers \(p\). For \(c=s/4\), differentiate the right side of (2) with respect to \(p\): \(s^2/48+p/6>0\) on the exact admissible range \(0<p\le s^2/4\). Therefore the measured second moment identifies a unique \(p\) also at resonance (equivalently, letting \(Q=L^2\mu_2-B_2(s,c)\), the positive root is \(p=(-s^2+\sqrt{s^4+768Q})/8\)). The quadratic \(u^2-su+p\) then recovers \(\{a,b\}\) with multiplicity, proving global injectivity.

For a concrete nonidentifiability witness using mean alone, \(G(1,3,1)\) and \(G(2,2,1)\) are nonisometric; both have \(L=5\), \(M=3\), and \(\mu_1=17/15\), while their second moments are respectively \(107/60\) and \(91/50\). More generally, at fixed \(s\) and \(c=s/4\), every choice of \(p\in(0,s^2/4]\) is realizable, giving a continuum of indistinguishable mean-distance measurements. Finally \(p\) is greatest at the balanced split, so the sign of \(c-s/4\) in (1) proves the asserted sharp shape-order reversal. \(\square\)

## Verification
The standalone standard-library program `checker.py` performs four independent kinds of finite validation: exact rational comparisons of category-integral and symmetric-moment formulas for 80 positive triples; exact integration of the full piecewise-linear density for its zeroth, first, and second moments for those same triples; 25 resonance identities and three exact explicit ambiguity identities; and four deterministic midpoint-grid comparisons computed directly from shortest paths along the three edges. Run it with `python3 checker.py`.

Its current output reports all checks passing. The finite grid and rational tests are supporting diagnostics, not proofs for infinitely many positive real parameters. The proof above is analytic and applies on the full claimed domain.

## Relationship to prior work
Network-distance summaries and distance-based spatial statistics are established topics; Lamb (2015) studies the network \(K\)-function and its dependence on network structure. Mémoli and Needham (arXiv:1810.09646; journal version 2022) formalize inverse problems from global and local metric-measure distance distributions; their metric-graph section includes a drawn dumbbell and a plotted example of its histogram (Figure 11), as well as local-shape injectivity theorems. That plotted example and their local distribution results do not themselves give the parameter-uniform global inverse formula (1)–(4), nor the mean-blind resonance. Baptista, Kennedy and Mugnolo (2024) introduce and optimize average distance for compact metric graphs, proving broad bounds and results for flowers and other graph classes. Their general bounds do not imply the exact switch of mean-distance shape order at \(c=s/4\), nor the sharp need for the second moment precisely there.

Earlier distance-distribution work on metric stars, theta graphs, or roses concerns different shortest-path combinatorics: the present graph has two cycles separated by a positive cut edge, rather than three parallel paths or loops attached at a single common junction. No implication from those reconstruction statements to (1)–(4) is assumed.

## Limitations
Only the specified dumbbell family is characterized; no recognition theorem among arbitrary graph topologies is claimed. A **known** total length and support endpoint are used as extra observables, not inferred from the mean and variance alone. The limiting cases \(a=0\), \(b=0\), or \(c=0\) are excluded, and no stability estimate uniform as edges collapse is given. The reconstruction depends on exact distributional observables; statistical estimation from finite noisy samples is outside the theorem. Bibliographic priority is qualified because unindexed treatments of the same three-edge metric graph may exist. Independent review has not been performed.

## References
1. D. S. Lamb, *The network K-function in context: examining the effects of network structure on the network K-function*, Transactions in GIS **20** (2016), 448–460; first online 27 July 2015. DOI: 10.1111/tgis.12157.
2. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first submitted 23 October 2018); Studies in Applied Mathematics **149** (2022), 943–1001. DOI: 10.1111/sapm.12526. In particular, Section 4 and Figure 11.
3. L. N. Baptista, J. B. Kennedy, D. Mugnolo, *Mean Distance on Metric Graphs*, Journal of Geometric Analysis **34** (2024), article 137. DOI: 10.1007/s12220-024-01574-0. In particular, Definition 2.1, Theorem 3.2 and the examples in Section 4.

# Exact third-moment reconstruction and two-moment camouflage for two-loop metric bouquets

## Finding

Let \(G(a,b)\) be the compact intrinsic metric graph obtained by identifying one point of a circle of circumference \(a>0\) with one point of a second circle of circumference \(b>0\). Sample \(X,Y\) independently from normalized arclength on the whole graph and put \(D=d_G(X,Y)\). No total-length measurement is assumed. Write
\[
\mu=\mathbb E[D],\qquad \nu=\mathbb E[D^2],\qquad \omega=\mathbb E[D^3].
\]
**Inverse and feasibility theorem.** The set of all possible first-three-moment triples is exactly
\[
\boxed{\mu>0,\qquad \nu=\frac43\mu^2,\qquad 2\mu^3<\omega\le\frac{56}{27}\mu^3.}
\]
For every such triple, define
\[
\boxed{c=\bigl[32(\omega-2\mu^3)\bigr]^{1/3},\qquad L=4\mu+c.}
\]
Then \(L=a+b\) and \(c=ab/(a+b)\). Consequently the unordered pair of circle lengths is **uniquely** reconstructed as
\[
\boxed{\{a,b\}=\left\{\frac{L-\sqrt{L(L-4c)}}2,\frac{L+\sqrt{L(L-4c)}}2\right\}.}
\]
The upper endpoint \(\omega=56\mu^3/27\) occurs exactly for equal circles; the lower endpoint is excluded and approached as one circle collapses. For every \(\mu>0\), infinitely many pairwise nonisometric positive two-loop bouquets have the same first *two* distance moments. In fact each shares these two moments with a single metric circle of circumference \(4\mu\); the third moment distinguishes the two-loop graph by a strict positive excess.

There is also an exact inverse-stability statement. For any two positive two-loop bouquets, with \(\Delta=\omega-2\mu^3\),
\[
\boxed{|c_1-c_2|\le\bigl(32|\Delta_1-\Delta_2|\bigr)^{1/3},\qquad
|L_1-L_2|\le 4|\mu_1-\mu_2|+\bigl(32|\Delta_1-\Delta_2|\bigr)^{1/3}.}
\]
The exponent \(1/3\) is globally optimal for recovery of \(c\) and \(L\) from this contrast, even restricted to graphs with \(\mu=1\) and both circle lengths positive.

## Assumptions and scope

The graph has exactly two genuine circles, glued at exactly one common articulation point, with intrinsic shortest-path distance, and has no other edges. Distances between points on the same circle are the shorter circular arc, not their distance in any planar embedding. The random points are independent and uniform with respect to **total** arclength. All formulas concern population moments, not sample estimators. Loop names have no geometric meaning: the recovered object is the unordered length multiset. Comparison with a single circle concerns the first two numerical moments only, not equality of the entire distance distributions.

## Proof

**1. Direct conditional distance laws.** Put \(L=a+b\). The probability of both points falling on the circle of length \(a\) is \(a^2/L^2\); similarly for the circle of length \(b\). Conditional on both being on a circle of circumference \(h\), the intrinsic distance is uniform on \([0,h/2]\). Its \(r\)-th moment is \(h^r/[2^r(r+1)]\).

The probability that the two points fall on different circles is \(2ab/L^2\). Each path from one circle to the other passes through the unique common vertex. The respective distances to that vertex are independent uniforms \(U\sim\mathrm{Unif}[0,a/2]\) and \(V\sim\mathrm{Unif}[0,b/2]\), hence the conditional distance is \(U+V\). Thus, for every integer \(r\ge1\),
\[
\mathbb E[D^r]=\frac{a^{r+2}+b^{r+2}}{2^r(r+1)L^2}
+\frac{2ab}{L^2 2^r}\sum_{j=0}^r\binom rj\frac{a^j b^{r-j}}{(j+1)(r-j+1)}.
\]
This expression is proved here only to establish the inverse theorem; arbitrary-order *forward* network moment formulas are known in the literature.

**2. Exact low moments and cubic separation.** Define \(c=ab/L\), so \(0<c\le L/4\), with equality exactly when \(a=b\). Substitution of \(r=1,2,3\), followed by elementary expansion, gives
\[
\boxed{\mu=\frac{L-c}{4},\qquad \nu=\frac{(L-c)^2}{12},\qquad
\omega=\frac{(L-c)^3+c^3}{32}.}
\]
In particular
\[
\nu=\frac43\mu^2,\qquad
\boxed{\omega-2\mu^3=\frac1{32}\left(\frac{ab}{a+b}\right)^3>0.}
\]
All identities are valid for arbitrary positive real circumferences.

**3. Complete feasibility and inversion.** For a measured \(\mu>0\), the first formula forces \(L=4\mu+c\). The positive numbers \(a,b\) must be roots of \(z^2-Lz+Lc=0\). They exist and are positive exactly when \(L\ge4c\) and \(c>0\), equivalently \(0<c\le4\mu/3\). The discriminant formula in the finding then reconstructs their unordered pair. Conversely, for every \(\mu>0\) and \(0<c\le4\mu/3\), these roots are positive, and their intrinsic-distance moments equal the displayed formulas. Cubing \(c\) yields precisely \(2\mu^3<\omega\le2\mu^3+(4\mu/3)^3/32=56\mu^3/27\), proving necessity and sufficiency, including both endpoint assertions.

**4. First-two-moment camouflage and minimal cutoff.** A metric circle of circumference \(s\) has uniformly distributed intrinsic distance on \([0,s/2]\) between two independent uniform points. Consequently its first three moments are \(s/4,s^2/12,s^3/32\). Taking \(s=4\mu\) matches the bouquet's \(\mu\) and \(\nu=4\mu^2/3\), but yields third moment \(2\mu^3\), which is strictly smaller than the bouquet value. Holding \(\mu\) fixed and varying \(c\) throughout \((0,4\mu/3]\) gives infinitely many nonisometric bouquets with the same two moments. Thus no scheme using only the first two raw moments reconstructs the positive two-loop geometry, whereas the first and third already do.

**5. Sharp inverse modulus.** For nonnegative \(u,v\), \(|u^{1/3}-v^{1/3}|\le |u-v|^{1/3}\). Applying this to \(32\Delta_1,32\Delta_2\) proves the stated bound on \(c\), and \(L=4\mu+c\) gives the bound on \(L\). To prove exponent optimality without using degenerate graphs, fix \(\mu=1\) and choose \(c_1=\varepsilon\), \(c_2=2\varepsilon\), where \(0<\varepsilon<2/3\). Step 3 realizes both with positive circles. Then \(|L_2-L_1|=\varepsilon\), \(|c_2-c_1|=\varepsilon\), while \(|\Delta_2-\Delta_1|=7\varepsilon^3/32\). No exponent strictly greater than \(1/3\) can yield a uniform Hölder estimate for either \(L\) or \(c\) from \(\Delta\) on this fixed-mean family.

## Verification

A self-contained standard-library program `verify_figure8.py` reconstructs the first three moments from conditional uniform laws using exact rational arithmetic, checks all three low-moment identities and exact inverse constraints, independently integrates the raw shortest-path distance over all pairs of circle coordinates, and samples the graph using a fixed pseudorandom seed. Executing `python verify_figure8.py` produced `VERIFY_OK 54 exact rational equalities/inequalities, 12 independently integrated or sampled tests`. Exact checks concern multiple rational length pairs; the universal proof is the displayed algebra and argument, not the finite tests.

## Relationship to prior work

Aanjaneya, Chazal, Chen, Glisse, Guibas and Morozov (2011/2012) reconstruct metric graphs from approximate metric data; Dey, Shi and Wang (first arXiv version 2015-03-25) compare metric graphs through persistence distortion. Their observables contain more geometric information than three **unlabelled random-pair moments**, so their reconstruction assertions do not imply the minimal-moment theorem here. Doyle and Graver (1982) study continuous mean distances of shapes; their full original article was not available for complete comparison. Wei, Walteros and Batta (2019/2020) derive arbitrary forward moments and density formulas for specified networks; the known forward machinery is not presented as novel. Garijo, Márquez and Silveira (2023, especially §4, Proposition 4.2) compute continuous means of weighted cactus graphs, which includes forward means for two-loop bouquets.

Independent earlier calculations for general metric flowers already give the first two moments in a stronger multi-loop setting and specialize to the identity \(\nu=4\mu^2/3\) for two petals. That identity, and its elementary circle comparison, are therefore not asserted as historically new. The retained mathematical claim is the **joint complete inverse classification from the third moment**, the exact feasible moment surface, the sharp minimal consecutive-moment order, and the optimal contrast-based inverse modulus. These inverse assertions are not contained in the compared forward-moment statements. Historical priority is provisional pending broader human review; search absence is not a proof of novelty.

## Limitations

The theorem assumes the two-loop model or a comparison class consisting of one circle and exactly two joined circles. It does not identify arbitrary metric graphs, arbitrary metric flower petal counts, embedded Euclidean curves, or graph topology outside this class. The sharp \(1/3\) stability concerns \(c\) and total length \(L\), not a sharp uniform modulus for each individually ordered loop length near the equal-loop discriminant. Statistical estimation under finite samples is not treated. The general forward moment formulas, including the specialized first and second moments, are established prior work and not novel claims.

## References

1. T. K. Dey, D. Shi, and Y. Wang, *Comparing Graphs via Persistence Distortion*, arXiv:1503.07414, first posted 2015-03-25, https://arxiv.org/abs/1503.07414.
2. N. Wei, J. L. Walteros, and R. Batta, *On the distance between random events on a network*, Networks **75** (2020), 203–231, first online 2019-11-27, https://doi.org/10.1002/net.21919.
3. D. Garijo, A. Márquez, and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, Results in Mathematics **78** (2023), article 139, https://doi.org/10.1007/s00025-023-01902-w.
4. M. Aanjaneya et al., *Metric Graph Reconstruction from Noisy Data*, International Journal of Computational Geometry & Applications **22** (2012), 305–325, https://doi.org/10.1142/S0218195912600072.
5. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory **6** (1982), 453–471, https://doi.org/10.1002/jgt.3190060410.

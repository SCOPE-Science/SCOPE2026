# Distance histograms globally reconstruct every positive three-path theta graph

## Finding

Consider a compact length-metric theta graph made by joining the two endpoints of three disjoint intervals of strictly positive lengths \(a\le b\le c\). Choose points independently from normalized arclength measure, and let \(D_{\mathrm{rand}}\) be their shortest-path distance. **Its complete one-dimensional probability law uniquely determines the unordered triple \(\{a,b,c\}\), including every coincident-length case.**

In fact, only the small-distance density, the upper endpoint of the support, and the onset of a simple near-diameter tail law are needed. Write \(L=a+b+c\), \(d_*=(b+c)/2\), and
\[
 U(\varepsilon)=L^2\Pr\bigl(D_{\mathrm{rand}}>d_*-\varepsilon\bigr).
\]
The first two measurements recover
\[
 L=\lim_{r\downarrow0}\frac{2r}{\Pr(D_{\mathrm{rand}}\le r)},\qquad
 a=L-2d_*.
\]
If \(a<b\), with \(h=(b-a)/2>0\), the *exact* terminal law is
\[
 U(\varepsilon)=4\varepsilon(a+\varepsilon)\qquad (0<\varepsilon\le h),
\]
and immediately after \(h\), writing \(\varepsilon=h+\delta\),
\[
 U(h+\delta)-4(h+\delta)(a+h+\delta)
 =\begin{cases}
 2(a+c)\delta+O(\delta^2),&b<c,\\
 4(a+c)\delta+O(\delta^2),&b=c,
 \end{cases}\qquad\delta\downarrow0.
\]
Therefore the largest initial interval of exact agreement determines \(h\), hence \(b=a+2h\) and \(c=L-a-b\).

If \(a=b\), its different leading tail coefficient detects that exceptional case:
\[
 \lim_{\varepsilon\downarrow0}\frac{U(\varepsilon)}{\varepsilon}
 =\begin{cases}
 2c+6a,&a=b<c,\\
 12a,&a=b=c.
 \end{cases}
\]
These coefficients strictly exceed \(4a\), the corresponding limit when \(a<b\). Once \(a=b\) is known, \(c=L-2a\). Thus ties and all positive real edge lengths are covered.

## Assumptions and scope

A theta graph here is the intrinsic path-metric realization of three intervals \([0,a]\), \([0,b]\), \([0,c]\), identifying their three left endpoints to one vertex and their three right endpoints to another; interiors remain disjoint. All lengths are positive finite real numbers, without any genericity assumption. The measure is length divided by total length, not counting vertices separately. The two sample points are independent. The probability law includes its normalization and absolute length scale. The theorem concerns precisely this topological class, not arbitrary metric graphs or graphs with pendant edges.

## Proof

**1. Length and diameter.** For sufficiently small \(r>0\), the metric ball of radius \(r\) centered at a point outside the \(r\)-neighborhood of either vertex lies in one interval and has length \(2r\). The exceptional center set has length \(O(r)\), and every ball has length \(O(r)\); consequently
\[
 \Pr(D_{\mathrm{rand}}\le r)=\frac{2r}{L}+O(r^2).
\]
For two points on distinct arms of lengths \(u,v\), the two paths via the common vertices have lengths whose sum is \(u+v\), so their minimum is at most \((u+v)/2\). For two points on the same arm of length \(u\), their direct separation \(t\) competes with the route through the shortest other arm of length \(w\), giving \(\min\{t,u+w-t\}\le(u+w)/2\). Both bounds are at most \((b+c)/2\). The midpoints of the arms of lengths \(b,c\) have distance exactly \((b+c)/2\): each one-vertex route has that length, while the two-vertex routes using the remaining arm have an additional cost \(a>0\). By continuity and full support of normalized arclength, the support endpoint is \(d_*=(b+c)/2\).

**2. Exact two-arm geometry.** Give the arms of lengths \(b,c\) coordinates \(x,y\) measured from the same common vertex. For \(p=x+y-(b+c)/2\) and \(q=x-y-(b-c)/2\), all four simple path lengths are
\[
 d_*+p,\quad d_*-p,\quad d_*+a+q,\quad d_*+a-q.
\]
Thus their shortest distance exceeds \(d_*-\varepsilon\) exactly when
\[
 |p|<\varepsilon,\quad |q|<a+\varepsilon,
 \quad |p+q|<b,\quad |p-q|<c,
\]
where the last two inequalities merely impose the coordinate domain; equality boundaries have zero area. The Jacobian from \((p,q)\) to \((x,y)\) is \(1/2\). If \(0<\varepsilon\le h=(b-a)/2\), the last two constraints are automatically satisfied in the first rectangle, because \(|p\pm q|\le a+2\varepsilon\le b\le c\). Therefore the ordered two-arm product-area of near-diametral pairs is exactly \(2\varepsilon(a+\varepsilon)\). Both orders of the arms contribute \(4\varepsilon(a+\varepsilon)\).

**3. All other arm pairs.** For an arm of length \(u\), let \(w\) be the shortest of the other two arm lengths. Two points on that same arm, at separation \(t\), have distance \(\min\{t,u+w-t\}\), so its maximal possible value is \((u+w)/2\). For points on distinct arms of lengths \(u,v\), their distance is at most \((u+v)/2\). If \(a<b\), every pair other than one from arm \(b\) and one from arm \(c\) has maximum at most \(d_*-h=(a+c)/2\). Combining this with step 2 establishes the exact terminal formula through \(h\).

**4. Sharp onset when \(a<b\).** Put \(r_0=(a+c)/2=d_*-h\) and \(r=r_0-\delta\). For a pair on arm \(c\), its distance exceeds \(r\) precisely when its coordinate separation \(t\) satisfies \(r<t<a+c-r\). Using the ordered separation area element \(2(c-t)\,dt\) gives the exact new term
\[
 2\int_{r}^{a+c-r}(c-t)\,dt=2(c-a)\delta,
\]
for sufficiently small \(\delta>0\), because \(c>a\). For one point on arm \(a\) and one on arm \(c\), the paths through either vertex give a near-maximum strip of width \(2\delta\), whose other-arm shortcut constraints are inactive in its interior since \(b>a\). Its ordered product-area is \(2a\delta+O(\delta^2)\), hence the two orders contribute \(4a\delta+O(\delta^2)\). At \(\varepsilon=h+\delta\), the b–c rectangle from step 2 is clipped at corners by its arm-coordinate constraints. These clipped triangles have total area \(O(\delta^2)\) because the constraints first touch at isolated corners; therefore its deviation from \(4\varepsilon(a+\varepsilon)\) is \(O(\delta^2)\). If \(b<c\) no other type is near its maximum; the total new first-order coefficient is \(2(c-a)+4a=2(a+c)>0\). If \(b=c\), there is a second identical longest arm, so these newly entering same-arm and short-long contributions occur twice. The coefficient doubles. These positive coefficients prove both that the exact initial formula holds through \(h\) and that it cannot extend beyond \(h\).

**5. Tied shortest arms.** If \(a=b<c\), the pairs of different arms with lengths \((a,c)\) occur in two unordered ways. Each contributes \(4a\varepsilon+O(\varepsilon^2)\) after counting both orders, and pairs on the long arm contribute \(2(c-a)\varepsilon+O(\varepsilon^2)\). Their sum is \((2c+6a)\varepsilon+O(\varepsilon^2)\). If all three arms have common length \(a\), all three unordered distinct-arm pairs contribute \(4a\varepsilon+O(\varepsilon^2)\) and same-arm pairs contribute only \(O(\varepsilon^2)\); the total is \(12a\varepsilon+O(\varepsilon^2)\). Both limits exceed \(4a\), as claimed.

**6. Reconstruction.** Read \(L\) and \(d_*\) from step 1 and set \(a=L-2d_*\). Read the terminal slope of \(U\). A slope greater than \(4a\) means \(a=b\), in which case \(c=L-2a\). A slope equal to \(4a\) means \(a<b\); read the endpoint \(h\) of the initial polynomial agreement to obtain \(b=a+2h\), then \(c=L-a-b\). The multiset is therefore uniquely recovered and the graph is determined up to isometry. \(\square\)

## Verification

The accompanying standard-library Python script `verify_theta_reconstruction.py` performs independent rational planar-polygon clipping for each pair of different arms and exact one-dimensional integration for each same-arm pair. It checks 961 rational identities or inequality/coefficient comparisons across 182 strictly increasing unequal-shortest-arm configurations, including \(b=c\), plus tied-shortest-arm configurations. It also compares four distribution-tail values to independent seeded shortest-path sampling with 110,000 pairs each. All tests passed. Computation corroborates the stated finite cases; the analytic proof, not the finite testing, establishes the theorem for all positive real lengths.

## Relationship to prior work

Aanjaneya–Chazal–Chen–Glisse–Guibas–Morozov (2011) reconstruct metric graphs from metric data under noise assumptions; Lecci–Rinaldo–Wasserman (2013) analyze topology reconstruction from sampled embedded filamentary data. Their observations contain substantially more information than an unmarked distribution of one random pairwise distance. Mémoli–Needham (2018 preprint, 2022 article) investigate distance-distribution inverse problems and announce local injectivity for metric graphs. Local injectivity does not imply global injectivity on the entire noncompact three-parameter theta family, especially at equality loci. The present derivation supplies an explicit global inversion in this family, including all ties. General formulas for random-point distances on known networks, such as those of Wei–Walteros–Batta (2019), calculate the forward distribution without by themselves proving injectivity. The precise global theta-graph assertion was not established by the accessible literature examined; full-text comparison with Mémoli–Needham remains an originality limitation.

## Limitations

Only theta graphs with exactly three positive arms are covered. A distance histogram does not, in general, reconstruct an arbitrary metric space or metric graph. The formula uses a full mathematical probability law, not finite empirical data: locating the first tail-law breakpoint is not asserted to be statistically stable under finite sampling. The main inverse-geometry comparison paper's full text was inaccessible during literature review, and no independent specialist audit has been performed.

## References

- Aanjaneya, M., Chazal, F., Chen, D., Glisse, M., Guibas, L. J., and Morozov, D., *Metric graph reconstruction from noisy data*, Proceedings of SoCG, 2011, 37–46. https://doi.org/10.1145/1998196.1998203
- Lecci, F., Rinaldo, A., and Wasserman, L., *Statistical Analysis of Metric Graph Reconstruction*, first public arXiv version 2013-05-06. https://arxiv.org/abs/1305.1212
- Mémoli, F., and Needham, T., *Distance distributions and inverse problems for metric measure spaces*, preprint first made public 2018-10-23; Studies in Applied Mathematics 149 (2022), 943–1001. https://arxiv.org/abs/1810.09646 ; https://doi.org/10.1111/sapm.12526
- Wei, N., Walteros, J. L., and Batta, R., *On the distance between random events on a network*, first published 2019-11-27; Networks 75 (2020), 203–231. https://doi.org/10.1002/net.21919

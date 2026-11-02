# Full intrinsic pair-distance law on a finite circular cylinder

## Finding

Let \(S_{R,h}\) be the **lateral surface only** of a right circular cylinder of radius \(R>0\) and height \(h>0\), including its two boundary circles but **not** its end disks. Equip it with its intrinsic shortest-path metric, and let \(P,Q\) be independent surface-area-uniform points. Put \(a=\pi R\), let \(D=d_{S_{R,h}}(P,Q)\), and let \(F(r)=\mathbb P(D\le r)\).

The support of \(D\) is exactly \([0,L]\), where \(L=\sqrt{a^2+h^2}\). For \(0<r<L\), define
\[
 X=\min\{a,r\},\qquad B=\min\{a,\sqrt{\max\{r^2-h^2,0\}}\},
\]
and, for \(0\le z\le r\),
\[
 I_r(z)=\frac12\left[z\sqrt{r^2-z^2}+r^2\arcsin(z/r)\right].
\]
Then the complete elementary CDF is
\[
\boxed{F(r)=\frac{2}{ah^2}\left[\frac{h^2B}{2}
+h\big(I_r(X)-I_r(B)\big)
-\frac12\left(r^2(X-B)-\frac{X^3-B^3}{3}\right)\right].}
\]
For \(r\le0\) set \(F(r)=0\), and for \(r\ge L\) set \(F(r)=1\). Away from the two interior threshold radii \(a\) and \(h\), the density is
\[
\boxed{F'(r)=\frac{2r}{ah^2}\left[h\left(\arcsin\frac Xr-\arcsin\frac Br\right)-(X-B)\right].}
\]
The elementary initial branch is
\[
\boxed{F(r)=\frac{\pi r^2}{2ah}-\frac{2r^3}{3ah^2}
\quad(0\le r\le\min\{a,h\}).}
\]

The full law displays two geometrically different internal singularities. If \(a\ne h\), it is \(C^1\) but not \(C^2\) at \(r=a\), and \(C^2\) but not \(C^3\) at \(r=h\). More precisely, when \(a<h\), with
\(P_0(r)=\pi r^2/(2ah)-2r^3/(3ah^2)\),
\[
 F(a+\delta)-P_0(a+\delta)
 \sim -\frac{4\sqrt2}{3h\sqrt a}\,\delta^{3/2}
 \qquad(\delta\downarrow0).
\]
When \(h<a\),
\[
 F(h+\delta)-P_0(h+\delta)
 \sim \frac{8\sqrt2}{15a h^{3/2}}\,\delta^{5/2}
 \qquad(\delta\downarrow0).
\]
For the other orderings, the **same local singular coefficients** hold after subtracting the real-analytic continuation of the branch with only the *other* cutoff already enforced. If \(a=h\), both cutoffs coincide and the \(3/2\)-order cusp dominates. At the farthest possible separation, one has the sharp cubic tail
\[
\boxed{1-F(L-\varepsilon)\sim
\frac{L^3}{3a^2h^4}\,\varepsilon^3\qquad(\varepsilon\downarrow0).}
\]

All even moments are explicit: for every integer \(k\ge0\),
\[
\boxed{\mathbb E[D^{2k}]=\sum_{j=0}^k\binom kj
\frac{a^{2j}}{2j+1}
\frac{2h^{2k-2j}}{(2k-2j+1)(2k-2j+2)}.}
\]
In particular,
\[
\mathbb E[D^2]=\frac{a^2}{3}+\frac{h^2}{6},\qquad
\mathbb E[D^4]=\frac{a^4}{5}+\frac{a^2h^2}{9}+\frac{h^4}{15}.
\]
The distribution determines the cylinder's dimensions uniquely. Indeed, letting \(m_2=\mathbb E[D^2]\) and \(L\) be the right-hand endpoint of its support,
\[
\boxed{a=\sqrt{6m_2-L^2},\qquad h=\sqrt{2L^2-6m_2},\qquad R=a/\pi.}
\]

## Assumptions and scope

Both geometric parameters are arbitrary positive real numbers. The points are independent and uniform with respect to normalized two-dimensional area on the **lateral** cylindrical surface. Distances are intrinsic to that surface: neither travel through the solid cylinder nor travel across either end disk is allowed. The boundary circles have zero sampling mass but are retained in the path metric. The theorem is not a claim about extrinsic Euclidean chord distances or about a capped solid cylinder.

## Proof

**1. Covering-space reduction.** Unroll the lateral surface as the flat quotient \((\mathbb R/(2a\mathbb Z))\times[0,h]\) with product Euclidean metric. Every lifted straight segment joining the chosen angular lifts remains inside the axial strip because both endpoint heights belong to \([0,h]\). The shortest geodesic therefore chooses the closest angular lift. If \(\Theta_P,\Theta_Q\) are independent uniform representatives in \([0,2a)\), the shortest wrapped angular separation
\[
 X_0=\min\big\{|\Theta_P-\Theta_Q|,\;2a-|\Theta_P-\Theta_Q|\big\}
\]
is uniform on \([0,a]\). The two heights are independent uniform points of \([0,h]\), so their nonnegative difference \(Y\) has density \(2(h-y)/h^2\) on \([0,h]\). The variables \(X_0,Y\) are independent, and for every sampled pair
\[
 D^2=X_0^2+Y^2.
\]
This is an exact intrinsic formula, not an approximation by an unfolding.

**2. Integration and closed form.** Conditioning on \(X_0=x\) and writing
\(u(x)=\min\{h,\sqrt{\max\{r^2-x^2,0\}}\}\),
\[
 F(r)=\frac{2}{ah^2}\int_0^{\min\{a,r\}}
\left(h u(x)-\frac{u(x)^2}{2}\right)dx.
\]
For \(0<r<L\), the integrand saturates at \(u=h\) exactly for \(0\le x\le B\); it has \(u=\sqrt{r^2-x^2}\) on \([B,X]\). Splitting the integral at \(B\), using
\(\int\sqrt{r^2-x^2}\,dx=I_r(x)\) and
\(\int(r^2-x^2)dx=r^2x-x^3/3\), produces the displayed CDF. Direct differentiation gives the density; moving endpoints contribute nothing because the integrands match at each switch. For \(r\le\min\{a,h\}\), the bounds reduce to \(B=0,X=r\), giving the displayed cubic polynomial in \(r\). At \(r=L\), all possible values of \(X_0,Y\) are included, so \(F=1\).

**3. Nonanalytic thresholds.** At \(r=a\), enforcing the finite angular width removes, relative to a smooth local continuation without this angular bound, the integral over \(x\in[a,a+\delta]\). The non-saturated integrand is
\(h\sqrt{(a+\delta)^2-x^2}+O((a+\delta)^2-x^2)\). Therefore the probability correction is
\[
-\frac{2}{ah^2}h\int_a^{a+\delta}
\sqrt{2a(a+\delta-x)}\,dx
\sim-\frac{4\sqrt2}{3h\sqrt a}\delta^{3/2}.
\]
At \(r=h\), enforcing the axial cap *adds* relative to a smooth continuation without that cap
\[
\frac1{ah^2}\int_0^{\sqrt{r^2-h^2}}
\big(\sqrt{r^2-x^2}-h\big)^2dx.
\]
Set \(r=h+\delta\) and \(x=\sqrt{2h\delta}\,t\). The leading integral is
\[
\frac{\sqrt{2h}}{ah^2}\delta^{5/2}
\int_0^1(1-t^2)^2dt
=\frac{8\sqrt2}{15a h^{3/2}}\delta^{5/2}.
\]
When the thresholds differ, the other cutoff contributes a real-analytic local background, so the coefficients and differentiability orders are unchanged. When they coincide, the \(3/2\) singularity is leading. The formula has no other interior singularities because its defining endpoints are real analytic away from \(0,a,h,L\).

**4. Upper tail.** Near maximum distance \(L\), write \(X_0=a-s\), \(Y=h-t\) with small \(s,t\ge0\). Then \(D\ge L-\varepsilon\) is equivalent, up to lower-order boundary curvature, to \(as+ht\le L\varepsilon\). The joint density is exactly \(2t/(ah^2)\). Integrating over the triangular region gives
\[
\frac{2}{ah^2}\int_{as+ht\le L\varepsilon}t\,ds\,dt
=\frac{L^3}{3a^2h^4}\varepsilon^3.
\]
A uniform rescaling of the shrinking triangular region and dominated convergence justify the asymptotic, with lower-order boundary corrections negligible.

**5. Moments and inverse statement.** Independence, the uniform moment identity
\(\mathbb E[X_0^{2j}]=a^{2j}/(2j+1)\), and the triangular moment identity
\(\mathbb E[Y^{2q}]=2h^{2q}/((2q+1)(2q+2))\)
give all even moments by the binomial formula. Since the right endpoint is \(L^2=a^2+h^2\), solving the linear system with
\(6\mathbb E[D^2]=2a^2+h^2\) yields the stated inverse formulas. The strict positivity of \(a,h\) removes all sign ambiguities.

## Verification

The standalone `verify.py` requires only Python 3's standard library. It independently integrates the conditional CDF by composite midpoint quadrature, simulates pairs directly on the angular-height coordinates, checks moment and inverse identities, and numerically tests the two fractional threshold powers and the cubic endpoint tail. The executed script passed 336 deterministic CDF quadrature comparisons across seven aspect ratios and 350,000 random pairs; the largest CDF-quadrature discrepancy was \(2.31\times10^{-6}\). Finite tests are not proofs of the continuum formulas; those follow from the exact integrations above.

## Relationship to prior work

Chen and Chen (2010) give covering-coordinate and numerical shortest-path methods for periodic parametric surfaces, including one-periodic surfaces, but not probability laws for random point-pair distances. Sheng (1985) and Marsaglia, Narasimhan, and Zaman (1990) derive powerful formulas for Euclidean distances between points in planar regions and rectangles. Their stated domains are planar Euclidean distances, not distances on the angularly identified strip. The present statement uses the wrap-around minimum and a separate axial boundary, producing two different singularities and an exact inverse metric-measure relation. The established literature offers methodological context, but the uniqueness of the present result in all historical sources is not independently certified.

## Limitations

This theorem concerns lateral surfaces only, not cylindrical solids or their complete closed boundaries. The elementary law uses zero curvature in the intrinsic geometry and does not extend verbatim to warped surfaces of revolution. The singularity statements concern the CDF as a function of radius and require the stated positive geometric dimensions. Historical priority remains subject to independent review; the most pertinent older papers on random distances in rectangles were compared through published abstracts and metadata because their complete texts were not accessible during this work.

## References

1. W.-H. Chen and S.-G. Chen, *Computation of the shortest path between two curves on a parametric surface by geodesic-like method*, arXiv:1011.5320, first arXiv posting 2010-11-24. https://arxiv.org/abs/1011.5320
2. T. K. Sheng, *The distance between two random points in plane regions*, Advances in Applied Probability **17** (1985), 748–773, DOI:10.2307/1427086. https://doi.org/10.2307/1427086
3. G. Marsaglia, B. Narasimhan, and A. Zaman, *The distance between random points in rectangles*, Communications in Statistics—Theory and Methods **19** (1990), 4199–4212, DOI:10.1080/03610929008830437. https://doi.org/10.1080/03610929008830437

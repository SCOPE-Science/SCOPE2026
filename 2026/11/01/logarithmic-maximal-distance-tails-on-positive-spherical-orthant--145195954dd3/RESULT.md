# Logarithmic maximal-distance tails on positive spherical orthants

## Finding

For every integer \(d\ge 2\), let
\[
\Omega_d=\{u\in\mathbb R^d:\|u\|_2=1,\ u_i\ge0\text{ for all }i\}
\]
carry normalized spherical \((d-1)\)-area, and sample \(U,V\) independently from it. Write \(\Theta=\arccos\langle U,V\rangle\) for the intrinsic spherical distance. Then the diameter of \(\Omega_d\) is \(\pi/2\), and its near-diameter tail obeys the exact asymptotic
\[
\boxed{\displaystyle
\lim_{\varepsilon\downarrow0}
\frac{\Pr\{\Theta>\pi/2-\varepsilon\}}
{\varepsilon^d[\log(1/\varepsilon)]^{d-2}}
=\frac{2^{2d-2}\Gamma(d/2)^2}{\pi^d(d-2)!}.}
\]
The logarithmic factor is absent in dimension two and occurs with exact power \(d-2\) for every dimension at least three. In particular the leading constants in dimensions two and three both equal \(4/\pi^2\), while dimension four has leading constant \(32/\pi^4\).

## Assumptions and scope

The dimension \(d\) is a fixed integer at least two; the limit is \(\varepsilon\downarrow0\), with no uniformity in \(d\) asserted. Sampling is by induced spherical area, not by the Lebesgue distribution in the solid orthant and not by the entire-sphere measure. The sphere has radius one. The positive orthant is geodesically convex: for \(u,v\in\Omega_d\), the shorter great-circle segment is a positive linear combination of \(u,v\), so \(\Theta\) is indeed the intrinsic length distance. Because all coordinates are nonnegative, \(0\le\Theta\le\pi/2\); distinct coordinate-axis vertices attain the upper bound.

## Proof

**1. Exact area and chart partition.** The unnormalized area of \(\Omega_d\) is
\[
\omega_d=\frac{1}{2^d}\frac{2\pi^{d/2}}{\Gamma(d/2)}
=\frac{2^{1-d}\pi^{d/2}}{\Gamma(d/2)}.
\]
Up to area-zero ties, split \(\Omega_d\) into \(d\) charts according to the index of the largest coordinate. In chart \(i\), use the \(d-1\) ratios \(r_k=u_k/u_i\), \(k\ne i\), with \(r_k\in[0,1]\) and \(u=(e_i+\sum_{k\ne i}r_ke_k)/\sqrt{1+\sum r_k^2}\). The exact spherical area element is
\[
(1+\sum_{k\ne i}r_k^2)^{-d/2}\prod_{k\ne i}dr_k.
\]
For a second point in chart \(j\), use \(s_k=v_k/v_j\) and the analogous area element.

**2. Only disjoint coordinate-axis charts contribute.** If \(i=j\), then \(u_i,v_i\ge1/\sqrt d\), so \(\langle u,v\rangle\ge1/d\). Such charts have no contribution for sufficiently small thresholds. For \(i\ne j\), define \(a=r_j\), \(c=s_i\), and for each of the \(m=d-2\) remaining indices define \(b_l=r_l\), \(q_l=s_l\). The exact inner product is
\[
\langle u,v\rangle=
\frac{a+c+\sum_{l=1}^m b_lq_l}
{\sqrt{(1+a^2+\sum b_l^2)(1+c^2+\sum q_l^2)}}.
\]
There are exactly \(d(d-1)\) ordered pairs of distinct-axis charts, each contributing the same unnormalized measure \(I_d(t)\) to the event \(\langle U,V\rangle<t\). Thus
\[
\Pr\{\langle U,V\rangle<t\}
=\frac{d(d-1)}{\omega_d^2}I_d(t)
\qquad(0<t<1/d).
\]

**3. Localization without losing the logarithmic coefficient.** Fix \(0<\eta<1\). Because the denominator of the displayed inner product is at most \(d\), the event implies
\[
a+c+\sum b_lq_l<dt.
\]
For sufficiently small \(t\), the variables \(a,c\) are automatically below \(\eta\). If some \(b_l\ge\eta\), then \(q_l\le dt/b_l\), which has integral measure at most \(dt\log(1/\eta)\) over \(b_l\in[\eta,1]\); the same bound holds with \(b_l,q_l\) interchanged. Every unrestricted pair obeying \(bq\le dt\) has measure at most \(dt(1+\log(1/(dt)))\), while \((a,c)\) have area at most \((dt)^2\). Therefore, for \(m\ge1\), the part of \(I_d(t)\) outside the small box where all \(a,c,b_l,q_l\le\eta\) is
\[
O_{d,\eta}\bigl(t^d[\log(1/t)]^{m-1}\bigr),
\]
which is smaller than the claimed main order. For \(m=0\), the outside region is empty for small \(t\).

Inside the small box, both exact area densities lie between \((1+(d-1)\eta^2)^{-d}\) and one, and the denominator of the inner product lies between one and \(1+(d-1)\eta^2\). Hence the contribution \(I_{d,\eta}(t)\) satisfies
\[
(1+(d-1)\eta^2)^{-d}J_{m,\eta}(t)
\le I_{d,\eta}(t)
\le J_{m,\eta}\bigl((1+(d-1)\eta^2)t\bigr),
\]
where
\[
J_{m,\eta}(t)=\int_{[0,\eta]^{2m+2}}
\mathbf1\{a+c+\sum_{l=1}^m b_lq_l<t\}
\,da\,dc\,\prod_{l=1}^m db_l\,dq_l.
\]

**4. Exact local product integral.** For two variables uniform in \([0,\eta]\), the (unnormalized) product \(w=bq\) has density \(\log(\eta^2/w)\) on \((0,\eta^2)\). For \(0<t<\min(\eta,\eta^2)\), integration over \(a,c\), followed by \(w_l=tz_l\), gives
\[
J_{m,\eta}(t)=\frac{t^{m+2}}2
\int_{z_l\ge0,\ \sum z_l<1}
(1-\sum z_l)^2
\prod_{l=1}^m\bigl[\log(\eta^2/t)+\log(1/z_l)\bigr]dz.
\]
(The empty product and the zero-dimensional integral equal one when \(m=0\).) All coefficients of this polynomial in \(\log(\eta^2/t)\) are finite, since each \(\log(1/z_l)\) is integrable on the simplex. The leading coefficient comes from the standard beta-simplex integral,
\[
\frac12\int_{\sum z_l<1}(1-\sum z_l)^2\,dz
=\frac{1}{(m+2)!}=\frac1{d!}.
\]
Consequently, for fixed \(\eta\),
\[
J_{m,\eta}(t)\sim\frac{t^d[\log(1/t)]^{d-2}}{d!}.
\]
The bounds in step 3, together with the negligible exterior, show that the liminf and limsup of \(I_d(t)/(t^d\log(1/t)^{d-2})\) lie between \((1+(d-1)\eta^2)^{-d}/d!\) and \((1+(d-1)\eta^2)^d/d!\). Letting \(\eta\downarrow0\) proves
\[
I_d(t)\sim \frac{t^d[\log(1/t)]^{d-2}}{d!}.
\]

**5. Normalize and convert distance.** Multiplication by \(d(d-1)/\omega_d^2\) yields
\[
\Pr\{\langle U,V\rangle<t\}
\sim\frac{t^d[\log(1/t)]^{d-2}}{(d-2)!\,\omega_d^2}.
\]
Since \(\{\Theta>\pi/2-\varepsilon\}\) is exactly \(\{\langle U,V\rangle<\sin\varepsilon\}\), and \(\sin\varepsilon/\varepsilon\to1\), the asserted formula follows.

## Verification

The standalone file `check_orthant.py` recomputes the normalized positive-orthant area, the beta-simplex coefficient, and the exact dimension-two tail. It also independently checks the \(m=1\) product-log integral
\[
\frac12\int_0^t(t-w)^2\log(\eta^2/w)\,dw
=t^3\left[\frac16\log(\eta^2/t)+\frac{11}{36}\right]
\]
and uses a deterministic Sobol quadrature of a full three-dimensional projective chart, splitting the integration into a logarithmic and a linear region and retaining the exact area-density and inner-product factors. The computed ratio to its theoretical leading coefficient approaches one as the cutoff decreases. These calculations check the normalization and local mechanism; the proof above, not the quadrature, proves the all-dimensional limit. Reproduce using `python check_orthant.py` with Python, NumPy, SciPy, and SymPy.

## Relationship to prior work

Cai, Fan, and Jiang study pair angles of points uniform on the **entire** sphere, including their sample-extreme-angle laws. On the full sphere, their fixed-dimensional pair-angle density is proportional to \((\sin\theta)^{d-2}\), which has nonzero density at \(\pi/2\); conditioning both points on one positive orthant changes that endpoint into the maximum and produces a different, logarithmic tail. Their full-sphere formula does not imply the orthant tail through a constant probability factor because the orthant conditioning is correlated with the angle.

Sidiropoulos gives an exact distribution for chord lengths and inner products of full-sphere uniform points (arXiv:1411.5639, Sections II–IV). That law likewise does not cover the pair of orthant-uniform points, nor its joint corner-product localization. Laarhoven studies hypercube hashing collision probabilities, which are exactly conditional same-orthant probabilities at a prescribed spherical angle; his Theorem 1 and Appendix A establish a large-dimension exponential rate for fixed angles below \(\pi/2\), including the rate base \(1/\pi\) as the angle approaches \(\pi/2\). This is the closest rigorous conditional-angle result, but its order of limits is \(d\to\infty\) at fixed angle: it neither gives a fixed-\(d\) near-endpoint probability nor supplies the \(\varepsilon^d[\log(1/\varepsilon)]^{d-2}\) coefficient. The two limits cannot be interchanged without a separate uniform theorem. A later discussion by Cook describes sampling positive-orthant random directions and their typical inner products but does not give this near-maximum-distance asymptotic. These are comparisons of mathematical statements, not priority certificates.

## Limitations

The result concerns a fixed dimension and a coordinate-orthant spherical simplex. It does not provide the complete angle CDF, a uniform-in-dimension error term, a second-order asymptotic, or analogous constants for arbitrary spherical simplices. No claim of globally certified novelty is made. A general theorem about semialgebraic endpoint asymptotics might imply the existence of a power-log expansion, but the exact dimension-dependent leading coefficient and this explicit elementary derivation are separately established here.

## References

1. T. T. Cai, J. Fan, T. Jiang, *Distributions of Angles in Random Packing on Spheres*, arXiv:1306.0256, first posted 2013-06-02; Journal of Machine Learning Research 14 (2013), 1837–1864. https://arxiv.org/abs/1306.0256
2. P. Sidiropoulos, *N-sphere chord length distribution*, arXiv:1411.5639, first posted 2014-11-20. https://arxiv.org/html/1411.5639v1
3. T. Laarhoven, *Hypercube LSH for approximate near neighbors*, arXiv:1702.05760v1, first posted 2017-02-19, especially Theorem 1 and Appendix A. https://arxiv.org/abs/1702.05760
4. J. D. Cook, *Random points in a high-dimensional orthant*, 2023-08-09. https://www.johndcook.com/blog/2023/08/09/random-points-hypersphere-orthant/

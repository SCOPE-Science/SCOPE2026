# A Dirichlet–uniform shape law for nearly maximal random triangles in a square

## Finding

Let three points be independently sampled from normalized planar area on the unit square \(Q=[0,1]^2\), and let \(A\) be the area of their triangle. The largest possible area is \(1/2\). Write \(h=2\varepsilon\) and condition on \(A>1/2-\varepsilon\). Then
\[
\Pr(A>1/2-\varepsilon)\sim \frac{32}{5}\varepsilon^5\log(1/\varepsilon).
\]
**The scalar upper-tail law is included only as normalization; an exact distribution of this area was previously published.** The finding is the conditional *shape* law below.

With conditional probability tending to one, the three points approach three distinct corners, leaving one of the four corners unoccupied. Every choice of the three occupied corners, with every assignment of the sampled-point labels, has limiting conditional probability \(1/24\). For any such ordered corner configuration, apply its fixed square symmetry to write the vertices as
\[
X=(a,b),\qquad Y=(1-c,d),\qquad Z=(e,1-f),
\]
where all six defect coordinates tend to zero conditionally. Define
\[
T_h=\left(\frac a h,\frac b h,\frac c h,\frac f h,\frac{de}h,\frac{h-a-b-c-f-de}h\right),
\qquad U_h=\frac{\log e}{\log h}.
\]
The sixth entry of \(T_h\) can be slightly negative for finite \(h\); this does not affect weak convergence. Conditionally on the corner configuration and on \(A>1/2-\varepsilon\), the joint law converges to
\[
(T_h,U_h)\ \Longrightarrow\
\bigl(\operatorname{Dirichlet}(1,1,1,1,1,1),\operatorname{Uniform}(0,1)\bigr),
\]
**with independence of the two limits.** In particular, the two cross-corner defects share the area-deficit scale through their product while having complementary, asymptotically uniformly random logarithmic exponents: \(e=h^{U_h}\) and \(d=h^{1-U_h+o_{\Pr}(1)}\). The same statement holds, in affine side coordinates, for any nondegenerate parallelogram.

## Assumptions and scope

The sample comprises exactly three independent Lebesgue-uniform interior points. The conditioning threshold satisfies \(\varepsilon\downarrow0\), with \(0<h=2\varepsilon<1\). A corner configuration means three labeled points assigned to distinct square vertices, leaving the remaining corner unused. The symmetry transporting each such configuration to the displayed chart is fixed once and for all. The conditional variables may be assigned arbitrary values outside their chart; the probability of that event tends to zero. All limits are weak convergence of finite-dimensional distributions; the logarithmic exponents are well-defined almost surely.

## Proof

**1. Maximum-area configurations.** For a triangle in the unit square, its area is at most one half. Equality is attained by taking a complete side of the square as a triangle base and choosing the third vertex anywhere on the opposite side. Conversely, multilinearity of the oriented determinant in the three point locations shows that any maximizing triangle has such a base: an interior coordinate at which a nonconstant affine function achieves its maximum must lie at an endpoint; any coordinate that can vary through an interval at a maximum requires the opposite edge to be parallel to that coordinate axis and to have maximal length one. Thus the entire equality set comprises the four side-base families (including their endpoints) and all point permutations.

**2. Exact local area deficit.** In the displayed corner chart, the positive doubled area equals
\[
(1-c-a)(1-f-b)-(d-b)(e-a),
\]
and therefore the deficit from one is exactly
\[
H=a+b+c+f+de-ad-af-bc-be-cf.
\]
Write \(L=a+b+c+f\) and \(v=de\). Within the chart where all six coordinates are at most \(\eta<1/10\), the error satisfies
\[
0\le L+v-H\le 2\eta L.
\]
In particular, \(L+v<h\) implies the actual event \(H<h\), and \(H<h\) implies \((1-2\eta)L+v<h\).

**3. Exact logarithmic volume of the model neighborhood.** For \(0<h<\eta^2\), the integral of the model event in the six-dimensional chart is
\[
J_\eta(h)=\int_{[0,\eta]^2}\frac{(h-de)_+^4}{4!}\,de\,dd
=\frac{h^5}{120}\left(\log\frac{\eta^2}{h}+\sum_{j=1}^5\frac1j\right).
\]
Here the upper limits on the four linear coordinates are automatically inactive for sufficiently small \(h\), and the product \(v=de\) has differential density \(\log(\eta^2/v)\,dv\) for \(0<v<\eta^2\). The final identity uses \(\int_0^1(1-w)^4dw=1/5\) and \(\int_0^1(1-w)^4(-\log w)dw=(\sum_{j=1}^5 j^{-1})/5\).

For fixed \(\eta\), the sandwich in step 2 bounds each corner contribution between \(J_\eta(h)\) and \((1-2\eta)^{-4}J_\eta(h)\). Sending \(\eta\) to zero gives coefficient \(1/120\) of \(h^5\log(1/h)\) per labeled three-corner configuration. The complement of fixed corner neighborhoods is concentrated near the compact portions of the four maximizing side-base families with the third point bounded away from both opposite corners. There the five active, transverse defect coordinates have coefficients uniformly bounded below, so its probability is \(O_\eta(h^5)\). Hence the total leading tail is \(24h^5\log(1/h)/120\), which is the stated formula after \(h=2\varepsilon\). The twenty-four configurations have equal limiting weights by the square symmetries and permutations.

**4. Conditional rescaling and log-uniformity.** For the model event, put \(a=hy_1\), \(b=hy_2\), \(c=hy_3\), \(f=hy_4\), and \(v=de=hy_5\). On the five-dimensional simplex \(y_j\ge0\), \(\sum_{j=1}^5y_j<1\), the Jacobian for the four linear coordinates and \(v\) is \(h^5\). Substituting \(e=h^u\), \(d=hy_5/e\) gives \(de\,dd=h\lvert\log h\rvert\,dy_5\,du\). For every fixed \(0<\zeta<1/2\), the range \(\zeta\le u\le1-\zeta\) forces both \(d\) and \(e\) to zero uniformly for \(y_5\le1\), and the cross terms in step 2 are \(o(h)\) there. On that range, the transformed volume density tends to a constant times \(dy_1\cdots dy_5\,du\) over the simplex, with \(u\) uniform and independent. The portions \(u<\zeta\) and \(u>1-\zeta\) have relative mass at most \(2\zeta+o(1)\); letting \(\zeta\downarrow0\) yields the product weak limit. Uniform Lebesgue measure on the five-dimensional simplex with the slack coordinate adjoined is precisely \(\operatorname{Dirichlet}(1,1,1,1,1,1)\). Since \(y_5\) has a positive limit almost surely, \(d=hy_5/e\) gives the complementary-exponent assertion. Affine maps preserve normalized area probabilities and the six square side coordinates, proving the parallelogram extension.

## Verification

The standalone standard-library script `verify.py` checks the exact quadratic determinant expansion against direct coordinates for 20,000 independent input tuples; verifies the product-singularity beta integrals by exact fractions and independently by quadrature; and checks direct reconstructed square triangles and Dirichlet/log-uniform moment identities on two distinct deficit scales. Run `python3 verify.py` alongside this document. The printed finite checks corroborate algebra and scaling but cannot establish a limit law by simulation alone. The proof above supplies the infinite argument.

## Relationship to prior work

The full marginal distribution of triangle area for three uniform points in a square was determined previously, including by Philip [1] and Trott [2]; in particular its \(h^5\log(1/h)/5\) upper tail is **not claimed as new**. Their area distribution is a one-dimensional pushforward and does not specify the limiting joint corner labels, four normalized coordinate defects, product defect, or independent logarithmic split. Jiang, Li and Vitányi [3] investigate the minimum-area extreme over many random square points, a different regime from the maximum-area conditional local geometry. Koroleva and Nikitin [4] study extremal perimeters and areas for samples on the circumference, rather than area-uniform points in a square. No inspected source states or implies the six-coordinate Dirichlet–uniform law without an additional analysis of the conditional geometry.

## Limitations

The limit is for a fixed sample of three points, conditioning on area tending to the maximum; it is not a large-sample extreme-value law. The model-tail coefficient is classical, not original. Joint weak convergence does not assert finite-threshold independence, and no convergence rate is proved. Only parallelograms inherit the result directly by affine invariance. The cited exact square-area distribution does not by itself prove the conditional location law; historical priority of the joint limit is provisional.

## References

[1] J. Philip, *The Area of a Random Triangle in a Square*, complete derivation and equations (15)–(18), https://www.geogebra.org/resource/h5arghmz/5OHVLMQbc1i1rsoE/material-h5arghmz.pdf. References therein cite an earlier 2004 treatment of the distribution.

[2] M. Trott, *The Area of a Random Triangle in a Square*, in *The Mathematica GuideBook for Symbolics*, Springer (2006), pp. 298–311.

[3] T. Jiang, M. Li, and P. Vitányi, *The Average-Case Area of Heilbronn-Type Triangles*, arXiv:math/9902043, first posted 1999-02-05, https://arxiv.org/abs/math/9902043.

[4] E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360, first posted 2013-01-07, https://arxiv.org/abs/1301.1360.

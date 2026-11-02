# Sharp normalized fourth-moment bounds for chords of rectangular-box surfaces

## Finding
For arbitrary \(a,b,c>0\), let \(\Sigma=\partial([-a,a]\times[-b,b]\times[-c,c])\subset\mathbb R^3\). Choose \(X,Y\) independently from normalized two-dimensional surface area on \(\Sigma\), and let \(D=\|X-Y\|_2\), the ambient Euclidean distance. Then
\[
\boxed{\frac{512}{375}\leq\frac{\mathbb E[D^4]}{(\mathbb E[D^2])^2}<\frac{12}{5}.}
\]
The lower equality holds **if and only if** \(a=b=c\). The upper constant is the **unattained sharp supremum**, approached by the boxes \((a,b,c)=(t,1,1)\) as \(t\to\infty\). Every number in the stated half-open interval is realized by at least one strictly positive box. Equivalently, the squared coefficient of variation of squared chord length has the exact range
\[
\boxed{\frac{137}{375}\leq\frac{\operatorname{Var}(D^2)}{(\mathbb E[D^2])^2}<\frac75,}
\]
with its unique shape minimizer the cube (up to uniform scaling).

## Assumptions and scope
The box is full-dimensional, with three strictly positive **half-edge lengths** \(a,b,c\). The six faces, including their relative area weights, jointly carry the probability measure; edges and corners have measure zero. Sampling is not from the interior, from one predetermined face, or from random invariant lines. The distance is straight-line ambient Euclidean distance, not a shortest path constrained to the surface. No total surface area or volume is fixed: the statistic is similarity invariant.

## Proof
**1. Exact moment reduction.** Put \(H=ab+bc+ca\), \(B=abc\), \(T=a+b+c\), and \(A_j=a^j+b^j+c^j\) for \(j=2,3,4\). A random point lies on one of the two faces perpendicular to coordinate \(i\) with total probability \(p_i=B/(a_i H)\), where \((a_1,a_2,a_3)=(a,b,c)\). Conditional on that choice, the distinguished coordinate is equally likely to be \(\pm a_i\), while the other two coordinates are independent uniform variables on their respective intervals.

For \(i\ne j\), direct conditioning gives
\[
\mathbb E X_i^2=\frac{a_i^2(1+2p_i)}3,\qquad
\mathbb E X_i^4=\frac{a_i^4(1+4p_i)}5,\qquad
\mathbb E X_i^2X_j^2=\frac{a_i^2a_j^2(1+2p_i+2p_j)}9.
\]
Since the distribution is centrally symmetric with diagonal covariance, setting \(M=\mathbb E\|X\|^2\) and \(V_i=\mathbb E X_i^2\), independence yields
\[
\mathbb E D^2=2M,\qquad
\mathbb E D^4=2\mathbb E\|X\|^4+2M^2+4\sum_{i=1}^3V_i^2.
\]
The mixed odd terms vanish by the symmetry of \(X\) and \(Y\). Define homogeneous degree-four and degree-eight polynomials
\[
Q=A_2H+2BT,
\]
\[
W=5A_2^2H^2+14A_4H^2+56A_3BH+20A_2TBH+40A_2B^2.
\]
Substitution and simplification now give the **exact identities**
\[
\mathbb E D^2=\frac{2Q}{3H},\qquad
\mathbb E D^4=\frac{2(5Q^2+W)}{45H^2},\qquad
K:=\frac{\mathbb E D^4}{(\mathbb E D^2)^2}=\frac{5Q^2+W}{10Q^2}.
\]
Here \(H,Q>0\), so all denominators are legitimate.

**2. Universal strict upper bound.** For any exponent triple \((r,s,t)\), let \(m_{rst}(a,b,c)\) be the sum of the **distinct** monomials obtained by permuting \(a^rb^sc^t\). Exact expansion proves
\[
\frac{19Q^2-W}{4}=7m_{440}+28m_{431}+51m_{422}+80m_{332}>0.
\]
Thus \(K<12/5\) for all positive half-edge lengths.

**3. Sharp lower bound and rigidity.** By permutation symmetry take \(a\ge b\ge c>0\), and write \(a=w+v+u\), \(b=w+v\), \(c=w\), with \(u,v\ge0\), \(w>0\). Define
\[
N=\frac{75W-649Q^2}{4}=\sum_{j=0}^{6}w^j P_j(u,v),
\]
where the exact coefficient polynomials, listed in descending \(j\), are
\[
\begin{aligned}
P_6={}&13280(u^2+uv+v^2),\\
P_5={}&30(u+2v)(966u^2+845uv+845v^2),\\
P_4={}&22159u^4+116768u^3v+193227u^2v^2+152918uv^3+76459v^4,\\
P_3={}&2(u+2v)(3492u^4+23905u^3v+38268u^2v^2+28726uv^3+14363v^4),\\
P_2={}&776u^6+12804u^5v+58893u^4v^2+114356u^3v^3+112623u^2v^4+66534uv^5+22178v^6,\\
P_1={}&8v(u+v)(u+2v)(97u^4+582u^3v+833u^2v^2+502uv^3+251v^4),\\
P_0={}&v^2(u+v)^2(194u^4+776u^3v+1027u^2v^2+502uv^3+251v^4).
\end{aligned}
\]
Every displayed coefficient is strictly positive, so \(N\ge0\); the term \(w^6P_6\) shows that equality is possible **only** at \(u=v=0\). Conversely, substituting \(a=b=c\) gives \(K=512/375\). The identity
\[
K-\frac{512}{375}=\frac{2N}{375Q^2}
\]
proves the lower bound and its complete equality characterization. Both polynomial identities in steps 2 and 3 are identities over the integers; the accompanying standalone exact-arithmetic script regenerates and checks all coefficients independently of numerical sampling.

**4. Attainability and sharpness.** Set \(a=t\), \(b=c=1\), for \(t\ge1\). The preceding formulas give \(Q=2t^3+O(t^2)\) and \(W=76t^6+O(t^5)\), hence \(K\to(5\cdot4+76)/(10\cdot4)=12/5\). The continuous map \(t\mapsto K(t,1,1)\) begins at \(512/375\); by the intermediate value theorem it takes every value between that minimum and its unattained limiting supremum. Thus the stated region is complete.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It checks the two polynomial inequalities by **exact rational/integer polynomial arithmetic** (15 positive monomials in the upper certificate; 39 positive monomials in the ordered-variable lower certificate), directly recomputes the two moments by summing over all 36 ordered pairs of box faces at five independent rational half-edge triples, checks the cube endpoint and thin-rod leading terms, and performs 240,000 seeded independent point-pair simulations on three boxes as supplementary numerical diagnostics. The observed execution result was: `VERIFY_OK upper_monomials=15 lower_ordered_monomials=39 exact_face_pair_cases=5 seeded_pairs=240000`. The infinite statement follows from the displayed polynomial identities, positivity, and limiting argument, **not** from finite sampling.

## Relationship to prior work
The 1999 article by Mathai, Moschopoulos and Pederzoli gives distance distributions/moments for a cube and for certain fixed face-pair models. The accessible publisher abstract concerns fixed cube configurations, not optimization over all positive cuboid aspect ratios. Consequently, even an exact fixed-cube moment is not the sharp all-shape interval or its rigidity assertion. The complete 1999 paper was not accessible for a section-by-section comparison, so historical priority remains provisional. Tong, Ahmadi and Pan (first posted November 29, 2013) develop polygon-interior point-distance distributions and a chord-length transformation; the accessible problem statement and methods use area-uniform interior points of planar polygons, not surface-area-uniform points of three-dimensional rectangular boxes. Known general forward integral methods do not by themselves assert the displayed sharp constants or equality conditions. The particular statistic can also be read as squared-distance dispersion \(K-1\); searches considered this equivalent formulation and box/surface/face-pair aliases.

## Limitations
The theorem gives no reconstruction of arbitrary side lengths from the ratio \(K\), no finite-sample confidence bounds, and no assertion about nonorthogonal parallelepipeds, higher-dimensional boxes, interior sampling, intrinsic surface geodesics, or random-line chords. Historical originality remains best-knowledge provisional, particularly because the full 1999 primary article was inaccessible. No external independent validation has been performed.

## References
1. A. M. Mathai, P. Moschopoulos, and G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81. Publisher record: https://rivista-statistica.unibo.it/article/view/1104 (publication year verified; precise earliest public day not verified).
2. F. Tong, M. Ahmadi, and J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498, first posted 2013-11-29, https://arxiv.org/abs/1312.2498.
3. E. W. Weisstein, *Cube Line Picking—Face and Face*, MathWorld, https://mathworld.wolfram.com/CubeLinePickingFaceandFace.html (background reference to fixed-cube face-pair calculations; undated).

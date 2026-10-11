# Exact quantitative illumination of the polars of type-\(D\) root polytopes

## Finding
For every integer \(d\ge3\), let
\[
Q_d=\{x\in\mathbb R^d: |x_i|+|x_j|\le2\text{ for all }1\le i<j\le d\}.
\]
For an origin-symmetric convex body \(K\), let \(\|z\|_K=\inf\{t>0:z\in tK\}\). Its **quantitative illumination parameter** is
\[
\operatorname{ill}(K)=\inf\left\{\sum_{p\in S}\|p\|_K:\ S\subset\mathbb R^d\setminus K\text{ finite and illuminates every boundary point of }K\right\}.
\]
Here a point source \(p\) illuminates a boundary point \(v\) when the ray starting at \(p\), passing through \(v\), and continuing past \(v\) meets the interior of \(K\).

**Theorem.** For every integer \(d\ge3\),
\[
\boxed{\operatorname{ill}(Q_d)=2^d+2d.}
\]
In fact any exterior source illuminating exactly \(k\ge1\) vertices of \(Q_d\) has \(\|p\|_{Q_d}>k\). In dimension three \(Q_3\) is the rhombic dodecahedron, so \(\operatorname{ill}(Q_3)=14\). Consequently the supremum of this quantitative parameter over origin-symmetric three-dimensional convex bodies is at least \(14\), exceeding the bound \(12\) proposed in the conjecture recorded by Bezdek and Khan [3, Conjecture 4.2]. The assertion is about the **quantitative illumination parameter**, not the ordinary illumination number.

## Assumptions and scope
The dimension is any integer \(d\ge3\). All illumination inequalities are strict; sources are finite in number and lie outside the body. The value is an infimum and need not be attained. The result also holds for any invertible linear image of \(Q_d\), by covariance of the illumination condition and Minkowski gauge. The body is a scaled polar of the root polytope \(\operatorname{conv}\{\pm e_i\pm e_j:i<j\}\); polarity alone supplies no identity between the illumination parameters of dual bodies.

## Proof
**1. Geometry and gauge.** Set \(V_A=\{\pm2e_i:1\le i\le d\}\), and \(V_C=\{(\epsilon_1,\ldots,\epsilon_d):\epsilon_i\in\{-1,1\}\}\). We claim \(Q_d=\operatorname{conv}(V_A\cup V_C)\). Every displayed point satisfies the pair constraints. Conversely, given \(x\in Q_d\), put \(a=\max_i|x_i|\). If \(a\le1\), then \(x\) lies in the cube \([-1,1]^d=\operatorname{conv}(V_C)\). If \(1<a<2\), choose \(i\) with \(|x_i|=a\) and \(\sigma=\operatorname{sgn}(x_i)\). The pair constraints give \(|x_j|\le2-a\) for \(j\ne i\). Hence
\[
x=(a-1)(2\sigma e_i)+(2-a)y,\qquad y_i=\sigma,\quad y_j=x_j/(2-a)\ (j\ne i),
\]
with \(y\in[-1,1]^d\). When \(a=2\), one has \(x=2\sigma e_i\). This proves the hull identity. All listed points are exposed vertices: the axis points uniquely maximize their signed coordinate, while the signed corner is the unique solution of its simultaneously tight equations \(\epsilon_i x_i+\epsilon_j x_j=2\) for all pairs (uniqueness uses \(d\ge3\)). Thus there are exactly \(N=2d+2^d\) vertices. The gauge is
\[
\|p\|_{Q_d}=\frac12\max_{i<j}(|p_i|+|p_j|),
\]
namely half the sum of the two largest coordinate magnitudes.

**2. Exact source criterion.** The body is described by linear facets \(\sigma x_i+\tau x_j\le2\), with \(i<j\), \(\sigma,\tau\in\{-1,1\}\). An exterior point \(p\) illuminates a vertex \(v\) exactly when \(n\cdot p>2\) for every facet normal \(n\) that is active at \(v\). To see this, the continuation after \(v\) has the form \(v+t(v-p)\) for \(t>0\). On an active facet its defining functional is \(2+t(2-n\cdot p)\), which enters the strict feasible side for sufficiently small \(t>0\) precisely when \(n\cdot p>2\). Inactive inequalities remain strict by continuity.

For an axis vertex \(2s e_i\), where \(s=\pm1\), the criterion becomes
\[
 s p_i>2+\max_{j\ne i}|p_j|.\tag{A}
\]
For a corner \(v=(s_1,\dots,s_d)\in V_C\), the criterion becomes
\[
 s_i p_i+s_j p_j>2\qquad (i<j).\tag{C}
\]

**3. Sources illuminating multiple vertices.** Condition (A) forbids one source from illuminating two different axis vertices: each would require its chosen signed coordinate to be larger than \(2\) plus the absolute value of the other chosen coordinate. Condition (C) forbids illumination of corners differing in two or more signs: choose two differing coordinates and add the two opposite inequalities, giving \(0>4\). A family of three distinct sign vectors necessarily contains a pair differing in at least two coordinates. Therefore a source illuminates at most one axis vertex and at most two corners, hence at most three vertices overall.

If a source illuminates **two corners**, they differ in exactly one coordinate, say \(j\). For each of the \(d-1\ge2\) common coordinates \(i\ne j\), applying (C) to the two corners yields
\[
 s_i p_i>2+|p_j|.
\]
Thus two absolute coordinates exceed \(2\), so \(\|p\|_{Q_d}>2\).

If a source illuminates an **axis vertex and a corner**, denote the axis index by \(i\), \(a=|p_i|\), and \(b=\max_{j\ne i}|p_j|\). Condition (A) gives \(a>2+b\). Since \(d\ge3\), (C) for two indices other than \(i\) gives \(2b>2\), hence \(b>1\). It follows that
\[
\|p\|_{Q_d}\ge(a+b)/2>1+b>2.
\]

Finally, if a source illuminates **one axis and two corners**, the corners differ in one index \(j\). The axis index \(i\) cannot equal \(j\), for the two corners then require every other coordinate magnitude to exceed \(2+|p_j|\), contradicting (A) at index \(j\). Since \(i\ne j\) and \(d\ge3\), choose a common corner coordinate \(k\notin\{i,j\}\). The two-corner inequality gives \(|p_k|>2+|p_j|\ge2\). Set \(a=|p_i|\), \(b=\max_{t\ne i}|p_t|\). Now \(b>2\), \(a>2+b\), and therefore
\[
\|p\|_{Q_d}\ge(a+b)/2>1+b>3.
\]
A source illuminating exactly one vertex has \(\|p\|_{Q_d}>1\) because it is outside \(Q_d\). Together these cases prove \(\|p\|_{Q_d}>k\) for every source illuminating \(k\ge1\) vertices.

**4. Lower and upper bounds.** If finitely many sources \(p_1,\ldots,p_m\) illuminate every vertex and \(k_r\) is the number illuminated by source \(p_r\), then
\[
\sum_{r=1}^m\|p_r\|_{Q_d}\ge\sum_{r:k_r>0}\|p_r\|_{Q_d}>\sum_{r:k_r>0}k_r\ge N.
\]
Conversely, for every vertex \(v\) take the source \(p_v=(1+\varepsilon)v\), with \(\varepsilon>0\). It illuminates \(v\) because each active supporting functional becomes strictly larger than \(2\). Illuminating all vertices illuminates every boundary point of a polytope: each proper face has a vertex, and a source illuminating such a vertex crosses strictly every facet containing that face, hence also illuminates its relative interior (or one can refine this face argument through the minimal face containing the point). The total gauge cost is \(N(1+\varepsilon)\). Letting \(\varepsilon\downarrow0\) gives \(\operatorname{ill}(Q_d)\le N\), matching the lower bound.

## Verification
The analytic proof is independent of computation. A standalone standard-library verifier `verify.py` checks the explicit facet incidences, the radial illuminators and the strict local cost bound against \(8452\) integer sources over dimensions \(3\) through \(6\), using exact integer and rational arithmetic. Run with `python3 verify.py` from the directory containing that file; expected prefix: `VERIFY_OK 8452`. These finite checks are diagnostic only and do not establish the result for all sources or dimensions.

## Relationship to prior work
Kiss and de Wet [1] introduce and study the same quantitative illumination parameter and determine exact values for selected symmetric Platonic solids, with bounds for Archimedean solids; the rhombic dodecahedron is not among their treated solids. Bezdek and Litvak [2] define a related vertex index with \(\operatorname{vein}(K)\le\operatorname{ill}(K)\), which does not determine the latter. Bezdek and Khan [3, Section 4.1] record as a conjecture the upper bound \(12\) for all centrally symmetric three-dimensional bodies; the present exact value \(14\) provides a counterexample. The ordinary illumination number is a different invariant: the existence of a six-direction illumination of the rhombic dodecahedron does not imply a gauge-cost bound of six.

## Limitations
The exact formula is proved only for the displayed pair-constraint family and its linear images. The result does not determine a sharp *upper* bound for arbitrary origin-symmetric bodies, nor does it solve the classical illumination-number conjecture. The strict source inequalities do not imply that the infimum cost is attained, and the proof uses sources approaching the boundary. Historical priority beyond the fully inspected works remains uncertain, particularly for alternate descriptions of type-\(D\) duals and earlier illumination variants. Independent review or audit has not been performed.

## References
[1] G. Kiss and P. O. de Wet, "Notes on the illumination parameters of convex bodies," *Contributions to Discrete Mathematics* 7(1) (2012), 58–67. DOI: 10.55016/ojs/cdm.v7i1.62108. Public article 2012-04-23; accessible full text: https://cdm.ucalgary.ca/article/download/62108/46729/177610.

[2] K. Bezdek and A. E. Litvak, "On the vertex index of convex bodies," arXiv:1110.4334 (first submitted 2011-10-19), especially Section 3. https://arxiv.org/pdf/1110.4334.

[3] K. Bezdek and M. A. Khan, "The geometry of homothetic covering and illumination," arXiv:1602.06040 (first submitted 2016-02-19), Section 4.1, Conjecture 4.2. https://arxiv.org/pdf/1602.06040.

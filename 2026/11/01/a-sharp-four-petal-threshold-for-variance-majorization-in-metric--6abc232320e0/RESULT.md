# A sharp four-petal threshold for variance majorization in metric flower graphs

## Finding

Let \(m\ge2\) be an integer. Let \(F\) be the compact metric flower obtained by identifying one point from each of \(m\) circles of positive lengths \(\ell_1,\ldots,\ell_m\), with intrinsic shortest-path distance and total arclength \(T=\sum_i\ell_i>0\). Choose \(X,Y\) independently from normalized arclength, and write \(D=d_F(X,Y)\), \(p_i=\ell_i/T\), and \(S_k=\sum_{i=1}^{m}p_i^k\).

Then the **exact two-moment laws** are
\[
\frac{\mathbb E D}{T}=\frac{2S_2-S_3}{4},\qquad
\frac{\mathbb E D^2}{T^2}=\frac{S_3}{6}+\frac{S_2^2}{8}-\frac{5S_4}{24},
\]
\[
\frac{\operatorname{Var}(D)}{T^2}=
\frac{S_3}{6}+\frac{S_2^2}{8}-\frac{5S_4}{24}
-\frac{(2S_2-S_3)^2}{16}.
\]

At fixed \(m\) and \(T\), the raw second moment is **strictly Schur-convex** in the length vector for every \(m\ge2\). In contrast, the variance is strictly Schur-convex **exactly for \(m=2,3\)**. For every \(m\ge4\) it is neither Schur-convex nor Schur-concave. These are assertions on the open simplex \(p_i>0\), \(\sum_i p_i=1\); a majorization inequality is strict unless two vectors are permutations.

The transition has an explicit positive-length four-petal witness. Put
\[
p=(49/100,49/100,1/100,1/100),\quad
q=(49/100,49/100,3/200,1/200).
\]
Then \(q\) majorizes \(p\), yet
\[
\frac{\operatorname{Var}_{q}(D)-\operatorname{Var}_{p}(D)}{T^2}
=-\frac{515428427}{192000000000000}<0,
\]
while the mean and raw second moment *increase*, respectively, by
\[
\frac{197}{8000000}\quad\text{and}\quad\frac{119977}{19200000000}.
\]
Thus balancing lengths can increase centered travel-distance dispersion even while lowering both raw moments. The failure first becomes possible with four petals.

## Assumptions and scope

Every petal is a full circle meeting all other petals only at one identified junction; its length is strictly positive. Distance is shortest-path arclength, not the Euclidean chord distance of an embedding. Both sample points are independent, and both include petal interiors according to normalized arclength. The ratios above are scale invariant; the two raw normalized moments and normalized variance use powers \(T\) and \(T^2\) as displayed. Majorization compares vectors of equal length \(m\) and equal sum \(1\), including all coordinate permutations. When \(m=1\) there is no nontrivial balancing order, so the classification begins at \(m=2\).

## Proof

**Conditional distances.** Conditional on both points lying on petal \(i\), their circular shortest distance is uniform on \([0,\ell_i/2]\). Its first and second moments are \(\ell_i/4\) and \(\ell_i^2/12\). If the two points belong to distinct petals \(i\ne j\), the shortest route passes through the common junction. The distance to the junction from a uniform point of petal \(i\) is uniform on \([0,\ell_i/2]\); these independent distances add. Their sum has conditional first moment \((\ell_i+\ell_j)/4\) and second moment \((\ell_i^2+\ell_j^2)/12+\ell_i\ell_j/8\). Weighting the conditional cases by \(p_i p_j\) and summing over ordered pairs yields the two displayed polynomial formulas. In particular, the mean agrees with the established formula for flower graphs in Baptista–Kennedy–Mugnolo, Equation (4.3); the second moment and the variance classification are the assertions investigated here.

**Strict Schur-convexity of the raw second moment.** For its normalized polynomial \(M_2\), let \(a=p_i\), \(b=p_j\), \(s=a+b\le1\), and \(S_2=\sum_kp_k^2\). Direct differentiation along the sum-preserving pair-transfer direction gives
\[
\frac{\partial_i M_2-\partial_j M_2}{a-b}
=Q_2:=\frac{S_2}{2}+\frac{s}{2}-\frac56(a^2+ab+b^2).
\]
Since \(S_2\ge a^2+b^2=s^2-2ab\) and \(ab\le s^2/4\),
\[
Q_2\ge\frac{s}{2}-\frac{s^2}{3}-\frac{ab}{6}
\ge\frac{s(4-3s)}8>0
\quad(0<s\le1).
\]
By the pairwise differential criterion for Schur-convexity on the positive simplex, \(M_2\) is strictly Schur-convex.

**Variance and the three-petal boundary.** Write \(M_1=(2S_2-S_3)/4\) and \(V=M_2-M_1^2\). Differentiation gives
\[
\frac{\partial_i V-\partial_j V}{a-b}
=Q_V:=-\frac56(a^2+ab+b^2)
+\left(\frac12+\frac32M_1\right)(a+b)+\frac{S_2}{2}-2M_1.
\]
For three petals, set \(s=a+b\), \(t=ab\), and the remaining length \(c=1-s\). Algebra reduces this expression to
\[
24Q_V=9s^3+27s^2t-17s^2-72st+9s+44t.
\]
Here \(0<s\le1\) and \(0\le t\le s^2/4\). The last polynomial is affine in \(t\), so its minimum on the admissible interval occurs at an endpoint. At \(t=0\),
\[
Q_V=\frac{s(9s^2-17s+9)}{24}>0,
\]
because \(9s^2-17s+9=9(s-17/18)^2+35/36\). At \(t=s^2/4\),
\[
Q_V=\frac{s(9s^3-12s^2-8s+12)}{32}>0.
\]
Indeed, the cubic in parentheses equals \(1\) at \(s=1\), and its negative derivative is
\[
8+24s-27s^2=8(1-s)^2+40s(1-s)+5s^2>0
\quad(0\le s\le1).
\]
Thus the variance is strictly Schur-convex for three petals. The two-petal case is the face \(c=0\), \(s=1\), where \(Q_V=(1-ab)/24>0\), so it too is strictly Schur-convex.

**Failure with at least four petals.** At the boundary vector \((1/2,1/2,0,0,\ldots,0)\), take \(i,j\) to be two zero-length coordinates in the polynomial extension. Here \(S_2=1/2\), \(S_3=1/4\), \(M_1=3/16\), and hence \(Q_V=S_2/2-2M_1=-1/8\). By continuity the coefficient remains negative at some strictly positive vector with two small petals. A sufficiently small transfer between those petals, away from equality, then decreases \(V\) as the vector becomes more unequal. For four petals the fully explicit rational witness in the Finding section certifies this effect without relying on a limiting vector; for more petals, assign arbitrarily small positive lengths to the additional petals and use continuity. Thus \(V\) is not Schur-convex for any \(m\ge4\).

Conversely, at the equilateral vector \(p_i=1/m\) the same coefficient equals
\[
Q_V=\frac{2m^2-2m-3}{4m^3}>0\qquad(m\ge2).
\]
A small positive pairwise imbalance therefore increases variance. In particular, \(V\) cannot be Schur-concave when \(m\ge4\). These two signs establish the claimed sharp classification. \(\square\)

## Verification

The accompanying `verify.py` uses only the Python standard library. It independently reconstructs both raw moments from the conditional within-petal and cross-petal laws and matches them to the closed formulas on 21,844 exact-rational length vectors of sizes \(1\) through \(7\). It checks the three-petal differential identity at a full \(5\times5\) rational interpolation grid: after substitution of the third coordinate, both sides are polynomials of degree at most \(4\) in each free variable, so agreement on this grid proves that polynomial identity. Exact fractions also check the four-petal majorization witness, the signs of the two raw-moment differences and variance difference, and the equal-petal differential coefficients. The positivity arguments for the full open simplex are the analytic inequalities in the proof, not consequences of finite sampling. Run `python3 verify.py`.

## Relationship to prior work

Doyle and Graver introduced mean-distance calculations for graph-shaped domains in 1982. Garijo–Márquez–Silveira subsequently developed algorithms for continuous mean distance on weighted graphs. Baptista–Kennedy–Mugnolo explicitly analyzed flower graphs, giving the first-moment formula and the unique equal-length mean minimizer. Their Equation (4.3) is **prior work**, not claimed here as new. The present result evaluates the second raw moment and gives the sharp majorization boundary for centered variance; knowing the first moment alone does not imply this boundary. The reviewed relevant sections of the two modern open-access papers contain no corresponding variance theorem. The original longer Doyle–Graver article could not be examined in full; the older summary and later historical account describe mean-distance calculations rather than the variance threshold. This leaves a genuine historical-priority uncertainty.

## Limitations

The sharp classification applies only to metric flowers, with the number of petals fixed and all petal lengths positive. It is not a theorem about arbitrary graphs, star trees, Euclidean embeddings, or alternative sampling measures. For \(m\ge4\), failure of Schur-convexity does **not** identify the global minimum or maximum variance; no such optimization is asserted. The counterexample and strict Schur inequalities concern normalized measurements, so the comparison presupposes equal total length. The prior-art search cannot certify worldwide uniqueness, especially for older inaccessible texts. Independent mathematical review has not been performed.

## References

1. J. K. Doyle and J. E. Graver, *A Summary of Results on Mean Distance in Shapes*, Environment and Planning B: Planning and Design 9 (1982), 177–179, DOI: 10.1068/b090177. The publisher's issue page records first public appearance as 1982-06-01.
2. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471, DOI: 10.1002/jgt.3190060410.
3. D. Garijo, A. Márquez, and R. I. Silveira, *Continuous mean distance of a weighted graph*, arXiv:2103.11676 (first posted 2021-03-22); Results in Mathematics 78 (2023), 139.
4. L. N. Baptista, J. B. Kennedy, and D. Mugnolo, *Mean Distance on Metric Graphs*, arXiv:2312.04952 (first posted 2023-12-08), Journal of Geometric Analysis 34 (2024), 137; especially Example 4.3, Lemma 4.4, and Equation (4.3).

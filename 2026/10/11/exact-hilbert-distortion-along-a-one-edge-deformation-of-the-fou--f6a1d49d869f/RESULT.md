# Exact Hilbert distortion along a one-edge deformation of the four-point equilateral metric

## Finding

For each real \(0<t\leq2\), let \(M_t=\{1,2,3,4\}\) carry the metric
\[
d_t(1,2)=t,\qquad d_t(i,j)=1\quad\text{for the other five unordered pairs}.
\]
Let \(\mathcal F(M_t)\) be the real three-dimensional Lipschitz-free (Arens–Eells, or transportation-cost) space. Its **multiplicative Banach–Mazur distance to three-dimensional Euclidean space** has the exact formula
\[
\boxed{
d_{\mathrm{BM}}\bigl(\mathcal F(M_t),\ell_2^3\bigr)^2
=\begin{cases}
\displaystyle\frac{7-2t-t^2}{3-t^2},&0<t\leq1,\\[5pt]
\displaystyle 1+\frac{4}{(t+1)(3-t)},&1\leq t\leq2.
\end{cases}}
\]
This distance is strictly decreasing on \((0,1)\), strictly increasing on \((1,2]\), and minimized **uniquely** at the equilateral metric \(t=1\), where it equals \(\sqrt2\). The distance at the collinear triangle endpoint \(t=2\) is \(\sqrt{7/3}\); its limit as \(t\downarrow0\) is the same number. The formula includes all admissible metric parameters, including the endpoint with a tight triangle inequality.

## Assumptions and scope

All spaces and linear maps are real. For finite \(M\), the free space \(\mathcal F(M)\) is the span of point evaluation differences with its transportation-cost norm. Its dual is the Lipschitz space of real functions on \(M\) modulo constants, with norm \(\operatorname{Lip}(f)=\max_{i<j}|f_i-f_j|/d_t(i,j)\). Distances between finite-dimensional spaces are multiplicative: \(d_{\mathrm{BM}}(X,Y)=\inf_T\|T\|\,\|T^{-1}\|\). This distance is unchanged on passing to duals when the comparison space is Euclidean.

The triangle inequality for the specified six distances holds exactly when \(0<t\leq2\). No assertion is made for the degenerate pseudometric at \(t=0\), complex scalars, or arbitrary deformations of several edges.

## Proof

**1. Dual-coordinate norm.** Work in the three-dimensional space of real functions modulo constants. Introduce the invertible coordinates
\[
X=f_1-f_2,\qquad Y=f_3-f_4,\qquad
Z=\tfrac12(f_1+f_2-f_3-f_4).
\]
The four cross-pair differences are \(Z+(X-Y)/2\), \(Z+(X+Y)/2\), \(Z-(X+Y)/2\), and \(Z-(X-Y)/2\). Hence, exactly,
\[
N_t(X,Y,Z)=\operatorname{Lip}(f)
=\max\left\{\frac{|X|}{t},\ |Y|,\ |Z|+\frac{|X|+|Y|}{2}\right\}.
\]
Consequently its unit ball \(B_t\) is
\[
B_t=\left\{(X,Y,Z): |X|\leq t,\ |Y|\leq1,\ |X|+|Y|+2|Z|\leq2\right\}.
\]
These definitions remain valid at \(t=2\).

**2. Symmetry reduction.** Let \(q(x)=x^\top Hx\) be any positive definite quadratic form. Its Euclidean distortion relative to \(N_t\), squared, is
\[
D_t(q)^2=\left(\max_{N_t(x)\leq1}q(x)\right)
\left(\max_{q(x)\leq1}N_t(x)^2\right).
\]
Choose the positive constants \(m,M\) so that \(mN_t(x)^2\leq q(x)\leq MN_t(x)^2\) for every \(x\); then the squared distortion is \(M/m\). The norm is invariant under the eight independent sign changes of \((X,Y,Z)\). Averaging \(q\) over these changes preserves both quadratic inequalities and produces a diagonal positive definite form with no greater ratio \(M/m\). Therefore an optimum exists among
\[
q(X,Y,Z)=aX^2+bY^2+cZ^2,\qquad a,b,c>0.
\]
Put \(P=\max_{B_t}q\) and \(Q=\max_{q\leq1}N_t^2\). The elementary dual norm of each of the linear forms defining \(N_t\) yields the **exact identity**
\[
Q=\max\left\{\frac1{t^2a},\ \frac1b,\ \frac1{4a}+\frac1{4b}+\frac1c\right\}.
\]
The square of the optimal Banach–Mazur distance is \(\inf_{a,b,c>0}PQ\).

**3. Unit-ball vertices.** Since the quadratic form is convex, \(P\) is attained at a vertex of the compact polytope \(B_t\). By sign symmetry it suffices to list vertices of the first-octant truncation \(0\leq X\leq t\), \(0\leq Y\leq1\), \(X+Y+2Z\leq2\). At \(0<t\leq1\) this gives
\[
P=\max\left\{c,\ b+\frac c4,\ t^2a+\frac{(2-t)^2c}{4},\ t^2a+b+\frac{(1-t)^2c}{4}\right\}.
\]
At \(1\leq t\leq2\) it gives
\[
P=\max\left\{c,\ b+\frac c4,\ t^2a+\frac{(2-t)^2c}{4},\ a+b,\ t^2a+(2-t)^2b\right\}.
\]
At \(t=1\), both descriptions agree, possibly with redundant terms.

**4. The shorter-edge regime.** Suppose \(0<t\leq1\). Scale \(q\) to \(Q=1\). The three constraints in the formula for \(Q\) force
\[
a\geq t^{-2},\qquad b\geq1,\qquad
c\geq\frac{4}{4-a^{-1}-b^{-1}}.
\]
Write \(A=t^2a\geq1\), \(B=b\geq1\). The last displayed vertex value for \(P\) is at least
\[
H_t(A,B)=A+B+\frac{(1-t)^2}{4-t^2/A-1/B}.
\]
The denominator is at least \(3-t^2\geq2\), and direct differentiation gives
\[
\frac{\partial H_t}{\partial A}=1-\frac{(1-t)^2t^2}{A^2(4-t^2/A-1/B)^2}>0,\quad
\frac{\partial H_t}{\partial B}=1-\frac{(1-t)^2}{B^2(4-t^2/A-1/B)^2}>0.
\]
Thus \(P\geq H_t(1,1)=2+(1-t)^2/(3-t^2)\), which is the first claimed branch. To attain it choose
\[
(a,b,c)=\left(t^{-2},1,\frac4{3-t^2}\right).
\]
These coefficients give \(Q=1\). The four displayed values contributing to \(P\) are all at most the last one: the differences from the last are respectively \((1-t)(t+3)/(3-t^2)\), \((3-2t)/(3-t^2)\), and \(t(2-t)/(3-t^2)\), all nonnegative. Hence the bound is sharp.

**5. The longer-edge regime.** Suppose \(1<t\leq2\). Scale the form to \(P=1\). The vertex inequalities force \(c\leq1\) and
\[
a+b\leq1,\qquad t^2a+(2-t)^2b\leq1.
\]
Therefore
\[
Q\geq1+\frac1{4a}+\frac1{4b}.
\]
The strictly convex function \(g(a,b)=(4a)^{-1}+(4b)^{-1}\) attains its minimum on the positive feasible region at
\[
(a_*,b_*)=\left(\frac{3-t}{4},\frac{t+1}{4}\right).
\]
For completeness, both linear constraints are equalities there, and the negative gradient of \(g\) is a nonnegative linear combination of their outward normals. Explicitly, if
\[
\lambda_2=\frac{(4a_*^2)^{-1}-(4b_*^2)^{-1}}{t^2-(2-t)^2},\quad
\lambda_1=\frac{t^2(4b_*^2)^{-1}-(2-t)^2(4a_*^2)^{-1}}{t^2-(2-t)^2},
\]
then \(\lambda_1,\lambda_2\geq0\). Indeed, \(a_*\leq b_*\) and \(t(3-t)\geq(2-t)(t+1)\) for \(t\geq1\). Hence the supporting-hyperplane inequality for convex \(g\) certifies the global minimum, giving
\[
Q\geq1+\frac1{3-t}+\frac1{t+1}=1+\frac4{(t+1)(3-t)}.
\]
Equality is attained by \(a=a_*\), \(b=b_*\), \(c=1\). In the vertex expression for \(P\), the entries \(c\), \(a+b\), and \(t^2a+(2-t)^2b\) equal \(1\); the other two are \((t+2)/4\leq1\) and \(1-t(2-t)^2/4\leq1\). Thus \(P=1\). The third entry of \(Q\) is the claimed sharp value. The first two equal \(4/(t^2(3-t))\) and \(4/(t+1)\), both at most \(2\), because \(t^2(3-t)\) is increasing from \(2\) on \([1,2]\). The third is at least \(2\), since \((t+1)(3-t)\leq4\). Thus equality holds.

At \(t=1\), the shorter-edge proof already gives the common value \(2\). Alternatively, \(P\leq1\) gives \(a+b\leq1\), and \((4a)^{-1}+(4b)^{-1}\geq1\), so \(Q\geq2\); the same coefficients attain equality.

**6. Passing to the free space and the minimum.** Euclidean Banach–Mazur distance is invariant under duality in finite dimensions, so the value calculated for \(\operatorname{Lip}(M_t)=\mathcal F(M_t)^*\) is the desired distance for the free space. Differentiating the two squared-distance branches gives respectively
\[
-\frac{2(t-1)(t-3)}{(3-t^2)^2}\quad\text{and}\quad
\frac{8(t-1)}{((t+1)(3-t))^2}.
\]
These are strictly negative for \(0<t<1\) and positive for \(1<t\leq2\), proving the unique minimum and endpoint claims.

## Verification

The standalone Python 3 standard-library script `verify_k4.py` reconstructs the vertices from the six first-octant linear inequalities by rational determinant calculation. For each of 48 rational parameters \(t=k/24\), \(1\leq k\leq48\), it checks both optimized quadratic forms against the exact vertex and dual-linear-functional formulas. It additionally checks 2,304 independent random rational diagonal forms against the asserted optimum, with exact fractions. Run `python verify_k4.py`; the expected final line is `K4_ONE_EDGE_EXACT_OK 2304 ellipsoid tests; 48 rational parameters`. These are reproducibility and arithmetic checks; the proof of every real parameter and every (including nondiagonal) ellipsoid is the analytic argument above, not a finite test.

## Relationship to prior work

Godard [1] introduced and characterized the relevant free-space/metric-tree framework, including a four-point characterization of spaces embedding isometrically in \(L_1\). His result concerns isometric \(L_1\) representation, not the best linear distortion of a three-dimensional free space to a Hilbert space. Here the three sums of opposite-pair distances are \(t+1\), \(2\), and \(2\); the four-point tree criterion therefore holds exactly for \(t\leq1\). Thus the sharp Hilbert-distortion branch boundary agrees with a structural transition in the established tree-metric classification, although the tree criterion alone gives no quantitative Euclidean constant. Alexander–Fradelizi–García-Lirola–Zvavitch [2] studied finite free-space polytopes, isometric classes, volume products, and the full equilateral complete-graph metric; their volume-product and polytope statements do not imply the present sharp Hilbertian ellipsoid formula. Dilworth–Kutzarova–Ostrovskii [3] obtain general finite-metric free-space structural and \(\ell_1\) estimates, rather than this sharp \(\ell_2^3\) deformation profile. Ostrovska–Ostrovskii [4] study isometric structure and graph transport representations, not the Banach–Mazur metric to Euclidean space. Identical results under another polytope or root-system normalization have not been ruled out absolutely.

## Limitations

The theorem is restricted to **real** Lipschitz-free spaces over this six-distance four-point family. The nonmetric limit \(t=0\) is not part of the theorem. The proof does not classify all optimal Euclidean ellipsoids, quantify near-extremizers, or compute Banach–Mazur distances to non-Hilbert comparison spaces. The bibliographic comparison does not constitute an exhaustive search of inaccessible or unindexed historical publications.

## References

[1] A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178v1 (first posted 21 April 2009), https://arxiv.org/abs/0904.3178.

[2] M. Alexander, M. Fradelizi, L. C. García-Lirola, and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (2019), https://arxiv.org/abs/1911.10642.

[3] S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (2018), https://arxiv.org/abs/1807.03814.

[4] S. Ostrovska and M. I. Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689 (2021), https://arxiv.org/abs/2112.02689.

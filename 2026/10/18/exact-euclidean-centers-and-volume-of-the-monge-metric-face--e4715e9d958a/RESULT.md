# Exact Euclidean centers and volume of the Monge metric face

## Finding

For every integer \(n\geq 3\), let \(V_a\), \(1\leq a<n\), be the symmetric \(n\times n\) matrix with zero diagonal and
\[
(V_a)_{ij}=\frac{\mathbf 1_{\min(i,j)\leq a<\max(i,j)}}{2a(n-a)}.
\]
The simplex \(\mathcal F_n=\operatorname{conv}\{V_1,\ldots,V_{n-1}\}\) is the **metric face** of the normalized hollow symmetric Monge polytope. Equip its affine hull with the Frobenius Euclidean metric \(\|A\|_F^2=\sum_{i,j} A_{ij}^2\).

Write \(w_a=a(n-a)\) and \(W=\sum_{a=1}^{n-1}w_a=n(n^2-1)/6\). The unique intrinsic incenter is
\[
 I_n=\sum_{a=1}^{n-1}\frac{w_a}{W}V_a,
 \qquad (I_n)_{ij}=\frac{3|i-j|}{n(n^2-1)},
\]
with squared inradius
\[
 \boxed{r_n^2=\frac{9}{(n^2-1)\bigl(n(n^2-1)-6\bigr)}}.
\]
Thus the incenter is precisely the normalized distance matrix of equally spaced points on a line.

The unique minimum-enclosing Euclidean ball of \(\mathcal F_n\) has every vertex on its sphere. Its center is
\[
 O_n=\frac{n-1}{2n}(V_1+V_{n-1})+\frac1n I_n,
\]
and its squared radius is
\[
 \boxed{R_n^2=\frac{(n-2)(n^2+2n+3)}{4n^2(n^2-1)}}.
\]
The exact intrinsic \((n-2)\)-dimensional volume is
\[
 \boxed{\operatorname{vol}_{n-2}(\mathcal F_n)^2=
 \frac{n^{n-2}(n^2-1)}{3\,2^{n-2}((n-1)!)^4((n-2)!)^2}}.
\]
In particular, \(r_n\sim 3n^{-5/2}\), \(R_n\sim (2\sqrt n)^{-1}\), and the radius ratio diverges quadratically: \(R_n/r_n\sim n^2/6\). The two centers coincide for \(n=3\), but differ for every \(n\geq4\).

## Assumptions and scope

The parent hollow symmetric Monge polytope comprises nonnegative symmetric zero-diagonal matrices of entry sum one satisfying \(c_{ij}+c_{k\ell}\leq c_{i\ell}+c_{kj}\) whenever \(i<k\) and \(j<\ell\). Its metric face is the convex hull of the normalized consecutive cuts \(V_a\), as characterized in Erickson--Kretschmann [1]. Equivalently, its members are precisely the normalized nonnegative path distance matrices \(C_{ij}=\sum_{a=\min(i,j)}^{\max(i,j)-1}g_a\), with \(g_a\geq0\) and \(2\sum_a a(n-a)g_a=1\). The interior points have strictly positive path edge lengths and hence are genuine metrics.

All distances, radii, and volume here are **intrinsic** to the affine hull of the metric face, with the full-matrix Frobenius metric. The inradius is not the inradius of the larger hollow symmetric Monge polytope. The case \(n=2\) has a zero-dimensional face and is excluded from radius statements.

## Proof

**1. Gram matrix and discrete Green kernel.** Put \(m=n-1\) and \(G_{ab}=\langle V_a,V_b\rangle_F\). The two cuts simultaneously separate exactly \(2\min(a,b)(n-\max(a,b))\) ordered pairs. Consequently,
\[
 G_{ab}=\frac{K_{ab}}{2w_aw_b},\qquad
 K_{ab}=\min(a,b)(n-\max(a,b)).
\]
Let \(L\) be the \(m\times m\) tridiagonal matrix with diagonal entries \(2\) and adjacent off-diagonal entries \(-1\). Extending each column of \(K\) by zero at indices \(0,n\), direct second differences give \(LK=n\operatorname{Id}\). Since \(w_0=w_n=0\) and \(w_a=a(n-a)\), the same second-difference calculation gives \(Lw=2\mathbf1\). Therefore,
\[
 G^{-1}=\frac2n\operatorname{diag}(w)L\operatorname{diag}(w),\quad
 G^{-1}\mathbf1=\frac4n w,\quad
 S:=\mathbf1^TG^{-1}\mathbf1=\frac{2(n^2-1)}3.
\]
These identities also establish affine independence of the \(V_a\).

**2. Intrinsic facet distances and the incenter.** Express an arbitrary point in the simplex as \(X=\sum_a\lambda_aV_a\), where \(\sum_a\lambda_a=1\) and \(\lambda_a\geq0\). In the translation space of its affine hull, the squared norm of the gradient of the barycentric coordinate \(\lambda_a\) is the \(a\)-th diagonal entry of
\[
 B=G^{-1}-\frac{G^{-1}\mathbf1\mathbf1^TG^{-1}}{S}.
\]
Indeed this is the orthogonal projection of the dual coordinate gradient to the sum-zero coefficient subspace, with metric \(G\). Substitution gives
\[
 B_{aa}=\frac{4w_a^2}{n}\left(1-\frac6{n(n^2-1)}\right)>0.
\]
Thus the distance from \(X\) to the supporting hyperplane \(\lambda_a=0\) is \(\lambda_a/\sqrt{B_{aa}}\). The largest possible minimum of these distances is
\(\bigl(\sum_a\sqrt{B_{aa}}\bigr)^{-1}\), uniquely attained at \(\lambda_a\propto\sqrt{B_{aa}}\propto w_a\). Evaluating the sum yields the stated squared inradius. Since each separated pair \(i<j\) occurs in precisely \(j-i\) cuts, the entry formula for \(I_n\) follows.

**3. All-vertex minimum sphere.** Let \(d_a=G_{aa}=1/(2w_a)\). A point \(O=\sum_a\mu_a V_a\) with \(\sum_a\mu_a=1\) has equal squared distances to all vertices if and only if \(2G\mu-d=\kappa\mathbf1\) for some scalar \(\kappa\). The tridiagonal identity above yields
\[
 (G^{-1}d)_a=\frac{n-1}{n}(\mathbf1_{a=1}+\mathbf1_{a=n-1}),
 \qquad \kappa=\frac{3}{n(n^2-1)},
\]
where normalization fixes \(\kappa\). Solving gives
\[
 \mu_a=\frac{n-1}{2n}(\mathbf1_{a=1}+\mathbf1_{a=n-1})+
 \frac1n\frac{w_a}{W}.
\]
Each coefficient is strictly positive, and \(\sum_a\mu_a=1\). Summing the equal squared distances with weights \(\mu_a\) gives
\[
 R_n^2=\sum_a\mu_a d_a-\|O\|_F^2
 =\frac12\left(\sum_a\mu_a d_a-\kappa\right)
 =\frac{(n-2)(n^2+2n+3)}{4n^2(n^2-1)}.
\]
For any alternative center \(Y\), the positive convex representation implies
\(\sum_a\mu_a\|V_a-Y\|_F^2=R_n^2+\|Y-O_n\|_F^2\). Hence any other center has strictly larger maximal vertex distance; the circumball is uniquely minimum-enclosing in the ambient matrix space as well.

**4. Exact intrinsic volume.** From \(K^{-1}=L/n\) and the tridiagonal determinant \(\det L=n\), one gets \(\det K=n^{n-2}\). Also \(\prod_{a=1}^{n-1}w_a=((n-1)!)^2\), so
\[
 \det G=\frac{n^{n-2}}{2^{n-1}((n-1)!)^4}.
\]
Taking \(V_{n-1}\) as the basepoint, the difference-vector Gram determinant is \(\det G\,(\mathbf1^TG^{-1}\mathbf1)=\det G\,S\). Dividing by \(((n-2)!)^2\) proves the volume formula. The stated asymptotics follow by taking leading powers of \(n\) in the two squared-radius formulas. For \(n\geq4\), an interior cut has coefficient \(w_a/(nW)\) at \(O_n\), versus \(w_a/W\) at \(I_n\); hence their centers differ.

## Verification

The included `check_metric_face.py` uses only the Python standard library and constructs every normalized cut matrix directly. Exact rational arithmetic checks the Gram matrix, inverse Green kernel, barycentric facet distances, center entries, all vertex-to-circumcenter distances, and the intrinsic squared volume for every integer \(3\leq n\leq10\). The checker prints PASS after all eight cases. These finite checks are corroboration, not a proof of the universal statement, which is furnished above by the exact algebraic identities.

## Relationship to prior work

Erickson and Kretschmann [1, Sections 4.1--4.3] defined the normalized hollow symmetric Monge polytope, identified the metric face as the simplex of consecutive cuts, and evaluated the normalized volume of the **whole hollow symmetric Monge polytope**. The consecutive-cut description and characterization of actual metrics are inputs, not new claims here. The contribution here is the intrinsic Euclidean geometry of that distinguished face: a closed path-metric incenter, a different explicit all-contact circumcenter, sharp radii and quadratic aspect growth, and its exact dimensional volume.

General simplex formulas express radii and volumes in terms of Gram matrices, but obtaining the stated explicit results requires the special discrete Green-kernel inverse and the exact weighted-second-difference identities. Earlier general cut-metric and Kalmanson decompositions provide context [2] but are not claimed here to be new.

## Limitations

The result applies to the **metric face**, not arbitrary points of the hollow symmetric Monge simplex or non-symmetric Monge matrices. The norm is the full-matrix Frobenius norm, not a coordinate norm on just the strictly upper triangular entries. The formula describes one fixed natural normalization and makes no claim of affine invariance. The formulas do not imply corresponding claims for general non-Monge metric cones or for alternate matrix norms.

## References

[1] W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, first posted 2023-11-13. https://arxiv.org/abs/2311.07522

[2] V. Chepoi and B. Fichet, *A Note on Circular Decomposable Metrics*, *Geometriae Dedicata* 69 (1998), 237--240. https://doi.org/10.1023/A:1004907919611

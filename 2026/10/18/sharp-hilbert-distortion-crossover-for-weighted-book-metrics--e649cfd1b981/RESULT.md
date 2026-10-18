# Sharp Hilbert-distortion crossover for weighted book metrics

## Finding

Let \(m\ge2\) be an integer. Consider the \(m+2\)-point metric with two distinguished hubs \(a,b\), leaves \(u_1,\ldots,u_m\), and distances
\[
d(a,b)=t,\qquad d(a,u_i)=d(b,u_i)=1,\qquad d(u_i,u_j)=2\quad(i\ne j),
\]
where \(0<t\le2\). Write \(\mathcal F(M_{m,t})\) for its real Lipschitz-free space, of dimension \(m+1\), and \(d_{\mathrm{BM}}\) for multiplicative Banach–Mazur distance. Put
\[
\tau_m=\frac{2}{m+\sqrt{m^2-m+1}}.
\]
Then its **exact squared distance to Hilbert space**, optimized over all invertible real linear maps, is
\[
\boxed{d_{\mathrm{BM}}\!\left(\mathcal F(M_{m,t}),\ell_2^{m+1}\right)^2=
\begin{cases}
1+m\dfrac{2-t}{2+t},&0<t\le\tau_m,\\[7pt]
m+\dfrac{t}{4-t},&\tau_m\le t\le2.
\end{cases}}
\]
The two branches agree at \(t=\tau_m\). The squared distance is strictly decreasing before \(\tau_m\) and strictly increasing thereafter. Thus its **unique globally optimal hub length** is \(\tau_m\), with
\[
\min_{0<t\le2}d_{\mathrm{BM}}\!\left(\mathcal F(M_{m,t}),\ell_2^{m+1}\right)^2
=m+\frac1{2(m+\sqrt{m^2-m+1})-1}.
\]
In particular, \(\tau_m=m^{-1}+O(m^{-2})\) and the minimum squared distance is \(m+(4m)^{-1}+O(m^{-2})\). The two opposite endpoints have the same limiting squared distance \(m+1\): the limit \(t\downarrow0\) within the fixed \((m+1)\)-dimensional family, and the redundant-edge endpoint \(t=2\). At \(t=1\) the result specializes to \(m+1/3\).

## Assumptions and scope

All scalars and linear maps are real. The displayed distances satisfy every triangle inequality exactly for \(0<t\le2\); the limiting object at \(t=0\) is **not** included, since its two hubs coalesce and the space loses a dimension. Distances between distinct leaves are the shortest-path distances in the two-hub spoke graph, so their Lipschitz inequalities follow from the spoke inequalities. A squared distance is always stated explicitly; the distance itself is the positive square root. Banach–Mazur distance is the infimum of \(\|T\|\,\|T^{-1}\|\) over invertible linear maps, and is invariant on passing to finite-dimensional duals against Hilbert space.

To identify the dual Lipschitz space of functions modulo constants, set
\[
h=\frac{f(a)-f(b)}2,\qquad z_i=f(u_i)-\frac{f(a)+f(b)}2,
\qquad H=\frac t2\in(0,1].
\]
Its norm and unit ball are exactly
\[
N_H(h,z)=\max\!\left\{\frac{|h|}{H},\ |h|+\max_i|z_i|\right\},
\qquad B_{m,H}=\{(h,z):|h|\le H,\ |z_i|\le1-|h|\}.
\]
The coordinate map is a linear isomorphism of the \((m+1)\)-dimensional quotient by constants, not necessarily a Euclidean isometry. The theorem is invariant under that choice of coordinates.

## Proof

**1. The correct dual ball.** For any two real numbers \(v,w\), \(\max\{|v+w|,|v-w|\}=|v|+|w|\). The two spoke inequalities at leaf \(i\) therefore reduce to \(|z_i|+|h|\le1\). The hub constraint is \(|2h|\le t\); the leaf-to-leaf constraints are implied by the spokes, since \(|z_i-z_j|\le2(1-|h|)\le2\). Thus the above norm and ball are exact for every claimed parameter.

**2. No loss from symmetrical Euclidean forms.** Let \(q(x)=x^{\mathsf T}Ax\) be an arbitrary positive definite quadratic form, and suppose \(cN_H(x)^2\le q(x)\le CN_H(x)^2\) for all \(x\). The group independently changes the signs of \(h\) and of every \(z_i\), and permutes all the \(z_i\). Every group element preserves \(N_H\). Averaging \(q\) over this finite group preserves both inequalities with the **same** \(c,C\), and produces \(q_{r,b}(h,z)=b(rh^2+\sum_i z_i^2)\), for some \(b,r>0\). Hence averaging cannot increase the best achievable ratio \(C/c\), and the unrestricted problem reduces to one positive shape parameter \(r\). Rescale to \(b=1\).

**3. Exact outer and inner quadratic radii.** Convexity in each leaf coordinate makes \(\sum z_i^2\) maximal, for fixed \(|h|=s\), precisely when every \(|z_i|=1-s\). As a function of \(s\in[0,H]\), the result \(rs^2+m(1-s)^2\) is convex and hence largest at an endpoint. Therefore
\[
A(r):=\max_{x\in B_{m,H}}q_r(x)
=\max\{m,\ rH^2+m(1-H)^2\}.
\]
The minimum of \(q_r\) on the boundary occurs either on a hub facet \(|h|=H\), where its minimum is \(rH^2\), or on a spoke facet \(|z_i|=1-|h|\), where all other leaves may be set to zero. The unrestricted minimum of \(rs^2+(1-s)^2\) over \(s\ge0\) is \(r/(r+1)\), attained at \(s=1/(r+1)\). It beats \(rH^2\) exactly when \(r>H^{-2}-1\), which entails \(1/(r+1)<H^2\le H\): the minimizing spoke point is then feasible. In the complementary regime the hub facet already gives the smaller value. Consequently **with no omitted boundary cases**,
\[
B(r):=\min_{x\in\partial B_{m,H}}q_r(x)
=\min\left\{rH^2,\frac r{r+1}\right\}.
\]
For a quadratic norm, squared multiplicative distortion is \(A(r)/B(r)\).

**4. Global one-variable minimization.** Put
\[
r_{\mathrm i}=H^{-2}-1,\qquad r_{\mathrm o}=\frac{m(2-H)}H.
\]
The inner minimum switches formula at \(r_{\mathrm i}\), while the outer maximum switches at \(r_{\mathrm o}\). On \(0<r<\min\{r_{\mathrm i},r_{\mathrm o}\}\) the ratio is \(m/(rH^2)\), strictly decreasing. If \(r_{\mathrm i}<r_{\mathrm o}\), the intermediate ratio is \(m(1+1/r)\), again strictly decreasing; if \(r_{\mathrm o}<r_{\mathrm i}\), it is \(1+m(1-H)^2/(rH^2)\), likewise decreasing. Beyond \(\max\{r_{\mathrm i},r_{\mathrm o}\}\) it equals
\[
F(r)=H^2(r+1)+m(1-H)^2\left(1+\frac1r\right).
\]
Here \(F'(r)=H^2-m(1-H)^2/r^2>0\), because \(r\ge r_{\mathrm o}=m(2-H)/H>\sqrt m(1-H)/H\) for all \(m\ge2\) and \(H\in(0,1]\). The continuous ratio therefore has its **unique** global minimizer
\[
r_*(m,H)=\max\left\{H^{-2}-1,\frac{m(2-H)}H\right\}.
\]
The inequality \(r_{\mathrm i}\ge r_{\mathrm o}\) is equivalent to \((m-1)H^2-2mH+1\ge0\), which holds exactly for \(0<H\le H_m\), with \(H_m=1/(m+\sqrt{m^2-m+1})\). In the first regime substitution of \(r_*=r_{\mathrm i}\) yields \(1+m(1-H)/(1+H)\). In the second regime \(r_*=r_{\mathrm o}\) yields \(m+H/(2-H)\). Substituting \(t=2H\) gives the displayed two-branch theorem.

**5. Optimizing the metric parameter.** The derivative of \(1+m(2-t)/(2+t)\) is \(-4m/(2+t)^2<0\); that of \(m+t/(4-t)\) is \(4/(4-t)^2>0\). Thus the unique optimum is their intersection \(\tau_m=2H_m\). Its value and asymptotics follow by direct substitution and \(\sqrt{m^2-m+1}=m-1/2+O(m^{-1})\). The limiting endpoint and \(t=1\) evaluations are direct. Finite-dimensional duality gives the stated free-space distance rather than only its Lipschitz dual.

## Verification

The standalone Python 3 standard-library program `verify_weighted_book_bm.py` evaluates the exact rational quadratic-radius formulas over 63 dimension–parameter cases, checks 25,200 positive rational shape parameters against the proposed exact optimum, and independently enumerates 286 polytope vertices to check the outer radius in selected dimensions and parameter values. It checks the known four-point \(7/3\) case and the \(K_{2,2}\) endpoint squared distance \(3\). Run `python3 verify_weighted_book_bm.py` in the directory containing this file; success prints `EXACT_BOOK_BM_CHECKS_PASS`. The proof for all real \(t\) and all \(m\ge2\) is the analytic minimax argument above; finite arithmetic is only a reproducibility consistency check.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (2018, arXiv:1807.03814) give the finite-graph free-space quotient representation and asymptotic comparison with \(\ell_1\) for recursive graph families, but do not compute this complete Euclidean distortion profile. Aliaga (2021, arXiv:2102.01219) characterizes extreme molecules for compact metric spaces, rather than the best ellipsoid-sandwich distortion of the present dual balls.

The published theorem *A sharp Löwner ellipsoid edge-invisibility threshold for book-graph symmetric edge polytopes* solves the **minimum-volume outer ellipsoid** of the unit \(t=1\) book's free-space polytope; it neither optimizes an enclosing-to-inscribed radius ratio nor treats variable hub length. Its Löwner weights and contact thresholds do not imply the displayed Banach–Mazur minimum. The published *Exact Hilbert distortion along a one-edge deformation of the four-point equilateral metric* implies the isolated \(m=2,t=1\) value \(7/3\), expressly **not claimed independently new** here; it does not cover the full weighted-book family. Prior calculations of book-graph dual-ball volumes and covariances similarly address a different invariant, not the Hilbert-distance crossover. The new content is the entire two-parameter distortion formula and the dimension-dependent uniquely optimal edge length.

## Limitations

No result is claimed at the nonmetric endpoint \(t=0\), in complex Banach spaces, for nonsymmetric spoke weights, or for arbitrary graph deformations. The optimal quadratic **shape** has been determined after finite-group averaging; uniqueness among all possibly nonsymmetric quadratic forms is not asserted. Known isolated subcases and the finite-graph duality are explicitly credited. An unindexed equivalent ellipsoid-sandwich calculation remains a bibliographic possibility despite the source and record comparisons.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1, first public 2018-07-10, https://arxiv.org/abs/1807.03814.
2. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219v1, first public 2021-02-01, primary MSC 46B20, https://arxiv.org/abs/2102.01219.
3. *A sharp Löwner ellipsoid edge-invisibility threshold for book-graph symmetric edge polytopes*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-l-wner-ellipsoid-edge-invisibility-threshold-for-book-gr--87e035ae5886.
4. *Exact Hilbert distortion along a one-edge deformation of the four-point equilateral metric*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-hilbert-distortion-along-a-one-edge-deformation-of-the-fou--f6a1d49d869f.

# Three-phase John ellipsoid of a capped hypercube

## Finding

Fix an integer \(n\ge 2\) and a real parameter \(0<\tau\le n\). Let
\[
K_{n,\tau}=\left\{x\in[0,1]^n:\sum_{i=1}^n x_i\le\tau\right\},\qquad
H=\frac{\mathbf1\mathbf1^\top}{n},\qquad P=I-H.
\]
For \(t,a,b>0\), with \(t\) a center coordinate, write
\[
E(t,a,b)=\left\{x:(x-t\mathbf1)^\top(aP+bH)^{-1}(x-t\mathbf1)\le1\right\}.
\]
The unique maximal-volume inscribed ellipsoid (John ellipsoid) of \(K_{n,\tau}\) is \(E(t,a,b)\), with **all three parameters determined exactly** by
\[
(t,a,b)=
\begin{cases}
\left(\dfrac{\tau}{n+1},\dfrac{\tau^2}{n(n+1)},\dfrac{\tau^2}{n(n+1)^2}\right),
&0<\tau\le\dfrac{n+1}{2},\\[7pt]
\left(\dfrac12,\dfrac{\tau(n-\tau)}{n(n-1)},\dfrac{(2\tau-n)^2}{4n}\right),
&\dfrac{n+1}{2}\le\tau\le\dfrac{n+\sqrt n}{2},\\[7pt]
\left(\dfrac12,\dfrac14,\dfrac14\right),
&\dfrac{n+\sqrt n}{2}\le\tau\le n.
\end{cases}
\]
The displayed formulas agree at both boundaries. Its Euclidean volume is exactly
\[
\kappa_n a^{(n-1)/2}b^{1/2},\qquad
\kappa_n=\frac{\pi^{n/2}}{\Gamma(n/2+1)}.
\]
The active supporting facets also undergo two sharp transitions. For \(0<\tau<(n+1)/2\), exactly the \(n\) coordinate lower facets and the rank facet are tangent. At \((n+1)/2\le\tau\le(n+\sqrt n)/2\), all \(2n\) coordinate facets and the rank facet are tangent. Above the second boundary, exactly the \(2n\) coordinate facets are tangent. At \(\tau=n\), the rank inequality is redundant. Whenever \(\tau=k\) is an integer with \(1\le k\le n\), the body is the independence polytope of the uniform matroid \(U_{k,n}\).

## Assumptions and scope

The ambient metric is the standard Euclidean metric of \(\mathbb R^n\), not a unimodularly transported metric on a lifted generalized permutohedron. All parameters \(\tau\) in the displayed real interval are included, including the two transition values and the cube endpoint. The ellipsoid is required to be full-dimensional. The matrix \(aP+bH\) has eigenvalue \(a\) on \(\mathbf1^\perp\) with multiplicity \(n-1\) and \(b\) on the line spanned by \(\mathbf1\); the claimed radii are covariance-semiaxis squares, not inverse quadratic-form eigenvalues.

## Proof

**1. Reduce to three parameters without assuming a symmetric optimizer.** Any full-dimensional compact convex body has a unique John ellipsoid. Coordinate permutations preserve \(K_{n,\tau}\), so uniqueness forces its ellipsoid center to be \(t\mathbf1\) and its positive-definite shape matrix to commute with every permutation. The permutation commutant consists of matrices \(aP+bH\); positive definiteness means \(a,b>0\). The volume to be maximized is \(\kappa_n a^{(n-1)/2}b^{1/2}\).

**2. Translate all halfspace constraints exactly.** The support range of each coordinate functional on \(E(t,a,b)\) is
\[
t\pm s,\qquad s^2=\frac{(n-1)a+b}{n},
\]
while the maximum of the coordinate sum is \(nt+\sqrt{nb}\). Consequently, the ellipsoid lies in \(K_{n,\tau}\) if and only if
\[
s\le t,\qquad s\le1-t,\qquad nt+\sqrt{nb}\le\tau.
\tag{1}
\]
These are exact necessary and sufficient conditions, because they test every defining supporting halfspace separately. In particular, \(0<t\le\tau/n\). If \(t>1/2\), moving its center to \(\mathbf1/2\) without changing its shape relaxes all three inequalities; it yields a different ellipsoid of the same volume, contradicting uniqueness of the maximum. Hence an optimum has \(t\le1/2\). Then \(s\le t\) implies \(s\le1-t\), so the latter constraint is redundant during optimization.

**3. Optimize the two axes at fixed center.** Set \(c=\tau/n\), with \(0<t\le\min\{c,1/2\}\). For any fixed \(t,b\), increasing \(a\) increases volume, hence equality must hold in the lower-coordinate constraint: \((n-1)a+b=nt^2\). Thus
\[
a=\frac{nt^2-b}{n-1},\qquad 0<b\le n(c-t)^2.
\]
Maximizing the determinant \(a^{n-1}b\) at fixed \(t\) is equivalent to maximizing \((nt^2-b)^{n-1}b\). Its unique unconstrained maximizer is \(b=t^2\). It follows exactly that
\[
b(t)=\min\{t^2,n(c-t)^2\}.
\tag{2}
\]
The switch in (2) occurs at \(t_0=c\sqrt n/(1+\sqrt n)\). For \(t\le t_0\), the optimized determinant is \(t^{2n}\), which strictly increases with \(t\). For \(t\ge t_0\), it is a positive constant times
\[
(2t-c)^{n-1}(c-t)^2.
\]
The derivative of its logarithm is
\[
\frac{2(n-1)}{2t-c}-\frac2{c-t},
\]
whose sign is precisely the sign of \(nc-(n+1)t\). Its unique unconstrained maximizer on this branch is \(t_*=nc/(n+1)=\tau/(n+1)\). For \(n\ge2\), \(t_0<t_*<c\). It follows that the optimum center is exactly
\[
t=\min\left\{\frac{\tau}{n+1},\frac12\right\}.
\tag{3}
\]
No local-extremum assumption was made: both branches have been optimized on their full permissible intervals.

**4. Evaluate the regimes and their boundaries.** If \(\tau\le(n+1)/2\), substitute \(t=\tau/(n+1)\) into the active rank constraint \(b=n(c-t)^2\), then use \((n-1)a+b=nt^2\). This gives the first formula. If \(\tau>(n+1)/2\), equation (3) gives \(t=1/2\), and (2) reads
\[
b=\min\left\{\frac14,\frac{(2\tau-n)^2}{4n}\right\},\qquad
 a=\frac{n/4-b}{n-1}.
\]
The second switch is precisely at \(2\tau-n=\sqrt n\), proving both remaining formulas. Every displayed value is positive in its claimed interval; endpoint formulas match by substitution. Uniqueness of the full John ellipsoid rules out all asymmetric competitors.

**5. Tangent facets.** Because equality \(s=t\) holds throughout, every lower-coordinate facet \(x_i=0\) is touched. In the first open regime, the upper coordinate support equals \(2\tau/(n+1)<1\) and the rank support equals \(\tau\). At the first transition the upper support reaches \(1\). In the intermediate regime \(t=s=1/2\), so both coordinate sides touch, and \(nt+\sqrt{nb}=\tau\). At the second transition \(b=1/4\) and the rank facet remains touched; strictly above it, \(nt+\sqrt{nb}=n/2+\sqrt n/2<\tau\), so only coordinate facets touch. At \(\tau=n\) the sum constraint is redundant. This exhausts all defining facets; for \(\tau=1\), the upper-coordinate inequalities are likewise redundant and are not counted.

## Verification

The accompanying standard-library `verify.py` recomputes all exact squared-support inequalities, positive eigenvalues, boundary equalities, and the three regimes using rational arithmetic on thousands of parameter pairs. It separately stress-tests the global determinant maximization on a dense two-parameter family without substituting the reported closed-form eigenvalues. To replay, run `python3 verify.py` in the extracted package directory. The verifier has no network or third-party dependencies. Its finite computations corroborate, but cannot prove, the general theorem: the proof above handles all integers \(n\ge2\) and real \(0<\tau\le n\).

## Relationship to prior work

Ferroni's independence-polytope analysis identifies exactly the same uniform-matroid body and establishes Ehrhart positivity by a half-open hypersimplex decomposition. His later matroid-polytope work has primary classification \(52B40\) and studies lattice/Ehrhart invariants, not the Euclidean John ellipsoid. Goemans–Harvey–Iwata study inscribed ellipsoids of centrally symmetrized polymatroids for approximation; symmetrization changes this body's center and facet geometry, so that theorem does not provide the off-center, three-regime solution here. Jochemko–Ravichandran study Minkowski linear functionals and Ehrhart coefficients on generalized permutahedra, not this Euclidean optimization. A previously available special-case evaluation at the central halfcube slice \(\tau=n/2\), and known Euclidean inball and circumball results for integer ranks, overlap special cases but do not establish the full John-ellipsoid profile and the nontrivial middle regime. The simplex-like and cube-like limiting regimes are elementary geometric bounds; the intermediate anisotropic transition is the principal new calculation.

## Limitations

This is an exact result for a permutation-invariant one-hyperplane truncation of a unit cube, not for arbitrary matroid independence polytopes, weighted knapsacks, or an arbitrary orientation of a cutting hyperplane. An equivalent result under truncated-cube, capped-simplex, or optimal-design terminology may exist; literature-search nonmatches alone are not definitive evidence of originality. No independent mathematical audit has been performed. The formulas use the inherited Euclidean metric, and do not imply corresponding formulas under other affine or lattice metrics.

## References

1. L. Ferroni, *Integer point enumeration on independence polytopes and half-open hypersimplices*, arXiv:2012.04711v1 (first public 2020-12-08), Sections 1–3; https://arxiv.org/html/2012.04711v1.
2. L. Ferroni, *Matroids are not Ehrhart positive*, arXiv:2105.04465v1 (first public 2021-05-10), later version Sections 1, 3–4; https://arxiv.org/html/2105.04465v3. Primary MSC2020 \(52B40\).
3. M. X. Goemans, N. J. A. Harvey, S. Iwata and V. S. Mirrokni, *Approximating submodular functions everywhere* (2009), Sections 2–3 on ellipsoids of symmetrized polymatroids.
4. K. Jochemko and M. Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, Mathematika 68 (2022), Sections 3–4, https://doi.org/10.1112/mtk.12122.

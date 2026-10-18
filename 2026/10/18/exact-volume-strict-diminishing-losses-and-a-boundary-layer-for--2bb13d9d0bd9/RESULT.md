# Exact volume, strict diminishing losses, and a boundary layer for partially shortened star metrics

## Finding

Let \(n\ge3\), \(2\le k\le n-1\), and \(1/2\le t\le1\). On \(M=\{o,v_1,\ldots,v_n\}\), put \(d(v_i,v_j)=1\) for distinct leaves, \(d(o,v_i)=t\) for \(1\le i\le k\), and \(d(o,v_j)=1\) for \(k<j\le n\). In anchored leaf-value coordinates the real Lipschitz-dual unit ball is

\[
Q_{n,k,t}=\left\{x\in\mathbb R^n:
 |x_i|\le t\ (i\le k),\quad |x_j|\le1\ (j>k),\quad
 |x_i-x_j|\le1\ (i\ne j)\right\}.
\]

Its exact coordinate Lebesgue volume is

\[
\boxed{V_{n,k}(t):=\operatorname{vol}_n(Q_{n,k,t})
=1+n(2t-1)+\frac{2(n-k)}{k+1}(1-t^{k+1}).}
\]

The formula also holds for the endpoint numbers \(k=0,1,n\), but the mixed-star regime \(2\le k\le n-1\) and its joint-deformation consequences are the subject of this result. For a fixed \(n\) and \(1/2\le t<1\), the marginal volume loss \(\Delta_k=V_{n,k}(t)-V_{n,k+1}(t)\), \(0\le k<n\), is strictly positive and strictly decreasing in \(k\):

\[
\boxed{\Delta_k=2\int_t^1 s^k\bigl((n-k)(1-s)+s\bigr)\,ds>0,\qquad
\Delta_k-\Delta_{k+1}=2\int_t^1s^k(1-s)\bigl((n-k)-(n-k-2)s\bigr)\,ds>0}
\]

for every \(0\le k\le n-2\) in the second inequality. Thus repeated shortening of incident hub edges has *strictly diminishing*, rather than additive, volume losses. Both inequalities become equalities only when \(t=1\), where there is no shortening.

A further boundary layer occurs as the number of leaves grows. For any integer sequence \(2\le k_n\le n-1\) such that \(k_n/n\to\theta\in(0,1]\), one has, for fixed \(1/2<t\le1\),

\[
\lim_{n\to\infty}\frac{V_{n,k_n}(t)}n=2t-1,
\qquad \lim_{n\to\infty} V_{n,k_n}(1/2)=\frac2\theta-1.
\]

At the critical scale \(t_n=1/2+c/n\), for any fixed \(c\ge0\),

\[
\boxed{\lim_{n\to\infty}V_{n,k_n}(t_n)=2c+\frac2\theta-1.}
\]

This is a sharp inverse-dimension crossover between bounded volumes and volumes growing linearly with dimension.

## Assumptions and scope

All vector spaces, Lipschitz functions and volumes are real. The distinguished hub is fixed at value zero, and the remaining \(n\) values are standard coordinates, not orthonormal coordinates in a zero-sum hyperplane; changing volume normalization would multiply all displayed volumes by a dimension-dependent factor. The inequalities define the dual unit ball of the real \(n\)-dimensional Lipschitz-free space, not the primal molecule ball. The triangle inequality for the prescribed metric follows from \(2t\ge1\); all other potentially restrictive triangles have sides among \(1,t,1\). At \(t=1/2\) some triangles are equalities, which the proof includes.

For the marginal comparisons only, extend the definition to \(k=0,1,n\). The expression for \(k=0\) is \(V_{n,0}(t)=n+1\), because no edge is shortened; \(k=n\) is the fully equiradial hub metric with volume \(2nt-n+1\); and \(k=1\) is the previously determined single-short-pair case \(t(2n-(n-1)t)\). These endpoint specializations are consistency checks, not separately claimed as new.

## Proof

**1. Slice the anchored polytope by its negative minimum.** The entire feasible set consists of vectors whose coordinates lie in their hub intervals and whose range together with the fixed value zero is at most one. The sector with all coordinates nonnegative has volume \(t^k\), as the nonnegative hub bounds are already at most one and all pairwise differences are at most one.

Outside that sector, almost every vector has a unique coordinate attaining its negative minimum. Write that coordinate as \(-s\), \(0<s\le1\). For a remaining coordinate \(x_j\) with hub bound \(a_j\in\{t,1\}\), feasibility conditional on this minimum is exactly

\[
-\min(a_j,s)\le x_j\le\min(a_j,1-s).
\]

Indeed, the left inequality ensures that \(-s\) remains the minimum and the right inequality enforces distance at most one from the minimum and from the hub; it automatically enforces all pairwise differences because every value lies between \(-s\) and \(1-s\). Hence the conditional width for a shortened spoke is

\[
w_t(s)=\min(t,s)+\min(t,1-s)=
\begin{cases}
 t+s,&0\le s\le1-t,\\
 1,&1-t\le s\le t,\\
 1+t-s,&t\le s\le1,
\end{cases}
\]

where \(1-t\le t\) uses \(t\ge1/2\). For an unshortened spoke, the width is exactly one. The unique minimum can be at a shortened spoke only for \(s\le t\); if it is at an unshortened spoke, \(s\le1\) is allowed. Hyperplanes corresponding to ties have zero Lebesgue measure. Therefore the full volume is exactly

\[
V_{n,k}(t)=t^k+k\int_0^t w_t(s)^{k-1}\,ds
+(n-k)\int_0^1w_t(s)^k\,ds.
\]

**2. Evaluate all three regimes without approximation.** On \([0,1-t]\), substitute \(u=t+s\); on \([t,1]\), substitute \(u=1+t-s\). Then

\[
\begin{aligned}
k\int_0^t w_t(s)^{k-1}\,ds
&=(1-t^k)+k(2t-1),\\
\int_0^1w_t(s)^k\,ds
&=(2t-1)+2\int_t^1u^k\,du\\
&=(2t-1)+\frac{2(1-t^{k+1})}{k+1}.
\end{aligned}
\]

Add the initial \(t^k\) sector. The first two terms simplify to one, and the middle interval contributes \(n(2t-1)\), proving the boxed exact volume.

**3. Prove the strict discrete curvature.** Rewrite the result as \(V_{n,k}(t)=1+n(2t-1)+2(n-k)\int_t^1s^k ds\). Successive subtraction gives

\[
\Delta_k=2\int_t^1s^k\left((n-k)-(n-k-1)s\right)ds
=2\int_t^1s^k\left((n-k)(1-s)+s\right)ds.
\]

For \(s\in(t,1)\) and \(k<n\), both factors in the last integrand are positive. Subtracting the same formula at \(k+1\) gives

\[
\Delta_k-\Delta_{k+1}
=2\int_t^1s^k(1-s)\left((n-k)-(n-k-2)s\right)ds.
\]

The final bracket equals \(2+(n-k-2)(1-s)\) and is at least two for \(k\le n-2\). The integrals are therefore strictly positive whenever \(t<1\), proving diminishing loss and strict discrete convexity.

**4. Locate the high-dimensional boundary layer.** Suppose \(k_n/n\to\theta>0\). For any fixed \(t\in[1/2,1)\), the factor \(t^{k_n+1}\to0\), while \((n-k_n)/(k_n+1)\to(1-\theta)/\theta\). At fixed \(t>1/2\), dividing the exact formula by \(n\) removes both the initial constant and this bounded correction, giving the first limit. At \(t=1/2\), the linear term \(n(2t-1)\) vanishes and the correction yields \(1+2(1-\theta)/\theta=2/\theta-1\). For \(t_n=1/2+c/n\), the exponentiated term still tends to zero, and now \(n(2t_n-1)=2c\). This proves the critical crossover. At \(t=1\), the exact volume is \(n+1\), yielding the stated normalized limit directly.

## Verification

The accompanying standalone `check_volume.py` uses rational arithmetic to count lattice points exactly in integral dilations of the polytope for 15 test configurations with \(n\le5\). The constraint matrix is a signed node-incidence matrix with one anchored node and is totally unimodular; after multiplying a rational \(t\) by its denominator, the polytope has integral vertices. Therefore its Ehrhart count is a degree-\(n\) polynomial whose highest finite difference is \(n!\) times its scaled Euclidean volume. The checker compares that coefficient with the proposed formula; all 15 comparisons passed. This independently checks the coefficient and normalization but is not an infinite-dimensional or all-parameter proof; Steps 1–4 supply the general proof.

For example, \((n,k,t)=(3,2,1/2)\) gives volume \(19/12\), and \((n,k,t)=(5,2,1/2)\) gives \(11/4\). The script requires only Python's standard library. Reproduce with `python check_volume.py`.

## Relationship to prior work

Alexander, Fradelizi, García-Lirola and Zvavitch [1] study the canonical finite-metric Lipschitz-free polytope, its polar, volume products and equilateral geometry. Their geometric and volume-product results establish motivation for exact finite-metric volume calculations; the inspected sections do not provide the mixed-spoke contraction volume or the diminishing-loss and inverse-dimension transition laws here.

Gordon and Petrov [2] study general combinatorial properties of Lipschitz polytopes, with emphasis on extreme points and face structures, rather than the present exact continuous volume response. Two previously known volume families are acknowledged explicitly: the single shortened-pair formula \(V_{n,1}(t)=t(2n-(n-1)t)\) and the fully equiradial-hub formula \(V_{n,n}(t)=2nt-n+1\). Neither endpoint statement determines the mixed profile for \(2\le k\le n-1\), much less the strict interaction across all edge counts and the critical dimension scale.

A related exact facet enumeration for *disjoint* shortened pairs studies a matching of short edges rather than overlapping spokes and counts faces, not volume; an exact Euclidean-distortion formula for *fully* equiradial hubs studies a different geometric invariant. Those structures do not imply the mixed-spoke volume statement. The contraction pattern and volume parameter are essential to the new claim.

## Limitations

The theorem concerns coordinate volume of the **dual** real unit ball and partial equal shortening of incident hub edges. It does not give the primal transportation-polytope volume, their Mahler product, arbitrary unequal shortened spoke lengths, a general graph-metric volume formula, complex scalars or any infinite-dimensional volume. The asymptotic statements require a positive limiting proportion of selected spokes; when \(k_n/n\to0\), a different regime may occur. Lattice experiments test only finitely many rational instances and are not a substitute for the analytic proof. An equivalent published formula in unindexed or differently termed literature remains possible; no independent scientific audit has been performed.

## References

[1] M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public version 24 November 2019, https://arxiv.org/abs/1911.10642.

[2] J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848, first public version August 2016, https://arxiv.org/abs/1608.06848.

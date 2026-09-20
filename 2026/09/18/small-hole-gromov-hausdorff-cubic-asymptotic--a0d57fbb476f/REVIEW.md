# Same-model review

## Correctness

**Assessment: PASS.**

The argument has two independent sides.

For the upper bound, the only quantitative refinement beyond Schott's proof is the standard normal-coordinate estimate \(g_{ij}=\delta_{ij}+O(|x|^2)\). On a sufficiently small strongly convex ball this implies a bilipschitz constant \(K_r=1+O(r^2)\) for the inverse exponential chart. Substitution into Schott's displayed correspondence-distortion estimate gives
\[
d_{\mathrm{GH}}(M\setminus B_r(a),M)
\le c_nr+O(r^3).
\]
No empirical approximation is used.

For the lower bound, rescale distances by \(h/r\) with fixed small \(h\). The deleted ball then has fixed Hausdorff radius \(h\), while an upper sectional-curvature bound scales to \(O(r^2)\) and the convexity radius scales to infinity. Adams--Frick--Majhi--McBride Theorem 4 applies to every scaled closed manifold. The fixed choice \(h<\pi/[8(c_n+1)]\) ensures that its first branch is active for all sufficiently small \(r\). Expanding its explicit coefficient at zero curvature gives
\[
\alpha(n,\kappa_r)=c_n+O(r^2),
\]
hence the matching lower bound \(c_nr-O(r^3)\).

The scaling relations, branch comparison, and Taylor expansion were checked algebraically. The dimension-one case is separated and follows from the sharp circle theorem.

Potential failure modes checked:
- the complement is equipped with the subspace metric, matching the cited theorems;
- the same set \(M\setminus B_r^g(a)\) becomes \(M\setminus B_h^{g_r}(a)\) under the chosen metric scaling;
- sectional curvature scales by the inverse square of the distance factor;
- convexity radius and both metric distances scale linearly;
- strong convexity is used before converting the pointwise normal-coordinate metric estimate into a distance bilipschitz estimate.

## Originality

**Assessment: PASS, to the best of our knowledge.**

The closest source is Schott, arXiv:2609.12625v1 (11 September 2026). Its Theorem 3.6 states an upper bound with an arbitrary fixed multiplicative loss \(L>1\), and its text does not state a limit, an asymptotic expansion, a rescaling argument, or a cubic error estimate. Its Euclidean theorem supplies the sharp constant that appears here.

Adams--Frick--Majhi--McBride supply the lower bound with the curvature-dependent coefficient \(\alpha(n,\kappa)\), but do not specialize it to a shrinking deleted ball with a radius-dependent rescaling that forces \(\kappa\) to zero.

Targeted searches were made for combinations of:
- Gromov--Hausdorff distance with deleted/complement geodesic balls;
- punctured Riemannian manifolds and small-hole asymptotics;
- the coefficient \(\sqrt{(n+1)/(2n)}\) with \(M\setminus B_r\);
- cubic or \(r^3\) error estimates for this deletion problem;
- the motivating arXiv identifier and synonymous formulations in the current SCOPE archive.

No prior statement of
\[
d_{\mathrm{GH}}(M\setminus B_r(a),M)
=
\sqrt{\frac{n+1}{2n}}\,r+O(r^3)
\]
or even the corresponding exact first-order limit was found.

The principal residual risk is recency: Schott's motivating preprint is only days old, so parallel work may not yet be indexed. The normal-coordinate expansion and all cited component inequalities are standard or explicitly attributed; originality is claimed only for their combination into the universal small-hole asymptotic and cubic-error estimate.

## Value

**Assessment: PASS.**

The result closes the multiplicative gap in the new manifold converse construction: the arbitrary \(L>1\) is replaced, asymptotically, by the exact Euclidean constant. It also gives a quantitative rate,
\[
\frac{d_{\mathrm{GH}}}{d_{\mathrm H}}=c_n+O(r^2),
\]
and explains geometrically why the Euclidean obstruction is universal at first order: after fixing the hole scale, curvature vanishes quadratically. This provides a local calibration result for comparing Hausdorff and Gromov--Hausdorff distances on smooth manifolds.

## Scientific limitations

The lower argument presently uses a global theorem for closed manifolds. No cubic coefficient is identified, and no optimality claim is made for the \(O(r^3)\) remainder. The statement is for the restricted ambient metric on the deleted-ball complement, not its intrinsic length metric.

Same-model review: passed. Independent audit: not yet performed.

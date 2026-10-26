# Two resonance bands and a sharp damping threshold for oscillatory covariances on regular trees

## Finding

Let \(q\ge 2\) be an integer and let \(T_q\) be the infinite \((q+1)\)-regular tree with graph distance \(d(x,y)\). For \(0\le r\le1\) and \(\theta\in\mathbb R\), consider the real, symmetric kernel
\[
 K_{q,r,\theta}(x,y)=r^{d(x,y)}\cos(\theta d(x,y)),
\]
where \(K_{q,0,\theta}(x,x)=1\) and every off-diagonal entry is zero when \(r=0\). Put \(c=|\cos\theta|\).

**Theorem (complete phase classification).** The kernel is positive semidefinite on *every* finite subset of vertices precisely in the following cases:

1. \(0\le r\le(2q-1)^{-1/2}\), with any \(\theta\);
2. \((2q-1)^{-1/2}<r<q^{-1/2}\), and \(c\notin(c_-(q,r),c_+(q,r))\), where
\[
 c_\pm(q,r)=\frac{\sqrt q(1-r^2)\pm\sqrt{(qr^2+q-2)((2q-1)r^2-1)}}{2(q-1)r};
\]
3. \(r=q^{-1/2}\) and \(c\in\{0,1\}\);
4. \(q^{-1/2}<r\le1\) and \(c=1\).

All displayed parameter endpoints are *included*. In the middle regime, \(0<c_-<c_+<1\), so the allowed angles split into bands near \(\theta\equiv\pi/2\pmod\pi\) and near \(\theta\equiv0\pmod\pi\). At the onset radius \(r=(2q-1)^{-1/2}\), the forbidden band first appears at the explicit tangency
\[
 c=\sqrt{\frac{q}{2q-1}}.
\]
As \(r\uparrow q^{-1/2}\), its two endpoints approach \(0\) and \(1\), respectively. The square-summability boundary therefore has just the two surviving angular phases, and above it only the unmodulated or parity-modulated geometric covariances survive.

Every admissible kernel with \(0\le r<q^{-1/2}\) is **strictly** positive definite on finite sets of distinct vertices. The same is true for \(q^{-1/2}\le r<1\) when \(c=1\). At \(r=q^{-1/2}\), \(c=0\), the kernel is positive semidefinite but *not* strictly positive definite: the \(q+1\) neighbors of any vertex give a singular Gram matrix. At \(r=1\), \(c=1\), the Gram matrix has rank one on any nonempty finite set.

For comparison, on the bi-infinite path (the degree-two tree), the same kernel is positive semidefinite for every \(0\le r\le1\) and every \(\theta\). Thus the forbidden resonance band is a branching phenomenon.

## Assumptions and scope

Positive semidefinite means \(\sum_{i,j=1}^N\overline{z_i}z_jK(x_i,x_j)\ge0\) for all \(N\ge1\), distinct vertices \(x_i\) and complex coefficients \(z_i\). The parameter \(q\) is any finite integer at least two; no asymptotic limit in \(q\) is assumed. Oscillation is measured in radians per graph edge. All endpoints and the isolated singular boundary are part of the exact classification. The analysis concerns unrestricted finite vertex configurations, not just finite balls or radial test vectors.

## Proof

**Step 1 (resolvent inside the spectral disk).** Let \(A\) be the adjacency operator on \(\ell^2(T_q)\). Its spectrum is the entire interval \([-2\sqrt q,2\sqrt q]\), with no point spectrum. For complex \(u\) with \(|u|<q^{-1/2}\), the function \(x\mapsto u^{d(x,y)}\) is in \(\ell^2(T_q)\) for each fixed \(y\), and direct inspection of the center and noncenter vertices gives
\[
 (I-uA+qu^2I)\bigl(u^{d(\cdot,y)}\bigr)
 =(1-u^2)\delta_y.
\]
The operator \(I-uA+qu^2I\) is invertible in this disk. Consequently its bounded inverse has matrix kernel \(u^{d(x,y)}/(1-u^2)\). Hence the operator with kernel \(u^{d(x,y)}\) is
\[
 R(u)=(1-u^2)(I-uA+qu^2I)^{-1}.
\]
Take \(u=re^{i\theta}\). The operator with kernel \(K_{q,r,\theta}\) is \((R(u)+R(\overline u))/2\); by the spectral theorem it is nonnegative exactly when
\[
 G_{q,r,\theta}(\lambda)=\operatorname{Re}\frac{1-u^2}{1-u\lambda+qu^2}\ge0
 \quad\text{for every }\lambda\in[-2\sqrt q,2\sqrt q].
\]
This criterion is necessary as well as sufficient because the adjacency spectrum is the whole indicated interval.

**Step 2 (sharp scalar inequality).** Multiplication by the conjugate denominator yields a strictly positive denominator and the real numerator
\[
 N(\lambda)=1-qr^4+(q-1)r^2\cos(2\theta)-\lambda r(1-r^2)\cos\theta.
\]
Its minimum over the adjacency spectrum equals
\[
 P_q(r,c)=1-qr^4+(q-1)r^2(2c^2-1)
            -2\sqrt q\,r(1-r^2)c.
\]
Thus, for \(0<r<q^{-1/2}\), positive semidefiniteness is equivalent to \(P_q(r,c)\ge0\). As a quadratic in \(c\),
\[
 P_q(r,c)=2(q-1)r^2c^2-2\sqrt q\,r(1-r^2)c
               +(1+r^2)(1-qr^2).
\]
The endpoint values are strictly positive in this open disk:
\[
 P_q(r,0)=(1+r^2)(1-qr^2),\qquad
 P_q(r,1)=(1-r^2)(1-\sqrt q\,r)^2.
\]
The polynomial discriminant, divided by \(4r^2\), is exactly
\[
 (qr^2+q-2)((2q-1)r^2-1).
\]
For \(0<r\le(2q-1)^{-1/2}\) it is nonpositive, so all \(c\in[0,1]\) are admissible. Beyond this radius and below \(q^{-1/2}\), the quadratic has the two stated roots and is negative precisely between them. Indeed its vertex is
\[
 c_*(q,r)=\frac{\sqrt q(1-r^2)}{2(q-1)r},
\]
which lies in \((0,1)\) throughout the intermediate regime, while both endpoint values remain positive. The asserted tangency and the limiting endpoints follow by direct substitution.

**Step 3 (boundary and supercritical regimes).** For every \(0\le t\le1\), the kernel \(t^{d(x,y)}\) is positive semidefinite on any tree. To see this, each edge separates the vertices into two sides, and the two-side kernel with diagonal entries one and cross-side value \(t\) is positive semidefinite. The product over the finitely many relevant separating edges yields \(t^{d(x,y)}\). The Schur product theorem therefore implies that if \(K_{q,r,\theta}\) is positive semidefinite, so is \(K_{q,tr,\theta}\).

At \(r=q^{-1/2}\), sending \(t\uparrow1\) in the subcritical inequality gives the necessary condition
\[
 0\le P_q(q^{-1/2},c)=-\frac{2(q-1)}q c(1-c),
\]
so \(c\in\{0,1\}\). When \(c=1\), the kernel is \((\pm r)^{d(x,y)}\), positive semidefinite by the preceding edge factorization and the bipartite parity sign. When \(c=0\), each subcritical kernel is positive semidefinite by Step 2, hence the limiting kernel is positive semidefinite. But on the \(q+1\) neighbors of a vertex its Gram matrix has diagonal entries one and all off-diagonal entries \(-1/q\); the constant vector lies in its nullspace.

If \(r>q^{-1/2}\) and \(0<c<1\), contract by the positive-definite factor \((q^{-1/2}/r)^{d(x,y)}\). This would give the excluded boundary phase, an impossibility. If instead \(c=0\), the same neighbor-star Gram matrix has off-diagonal entries \(-r^2\) and a negative eigenvalue \(1-qr^2\). If \(c=1\), the edge factorization proves positive semidefiniteness for the whole range \(r\le1\). This completes the necessity and sufficiency proof without invoking a complementary-series classification.

**Step 4 (strictness and the path contrast).** In the open spectral disk the multiplier in Step 1 is positive except possibly at one spectral endpoint; neither endpoint is an adjacency eigenvalue in \(\ell^2(T_q)\). Thus its bounded positive operator has trivial nullspace, proving strictness on all finite sets. For \(0<r<1\), the edge-product construction of \(r^{d(x,y)}\) is strictly positive on any finite set: its feature functions are distinct products of independent full-support binary variables and hence linearly independent. Bipartite parity modulation preserves strictness. The singular configurations have already been identified. On the degree-two tree \(\mathbb Z\), the kernel is the average of two phase-shifted Poisson covariance sequences \(r^{|m-n|}e^{\pm i\theta(m-n)}\), each positive semidefinite, giving the final comparison.

## Verification

The self-contained script `verify.py` checks the scalar polynomial and discriminant identities for rational test values across many branching degrees, confirms the boundary reduction, and constructs an exact rational finite-matrix obstruction. For \(q=2\), \(r=2/3\), \(\theta=\pi/3\), take the ball of radius three (22 vertices) around a root and give vertices at depths \(0,1,2,3\) the respective coefficients \((1,2,0,1)\). The exact quadratic form is
\[
 \sum_{x,y}\!v_x K_{2,2/3,\pi/3}(x,y)v_y=-\frac{49}{243}<0.
\]
Running `python verify.py` produces `ALL_CHECKS_PASSED`. These finite computations corroborate the algebra but are **not** used in place of the infinite-tree spectral and closure arguments.

## Relationship to prior work

The 1982 spherical harmonic analysis of free groups supplies principal/complementary representation theory and radial convolution recurrences, while the 2009 Gaussian-wave analysis gives the regular-tree adjacency spectral framework and normalized oscillatory spherical functions. Vergara's 2019 characterization gives a general integral-moment criterion for all radial positive-definite kernels on homogeneous trees. These are stronger **general frameworks**, but the inspected portions do not state the exact two-parameter damped-cosine phase diagram, universal critical damping \((2q-1)^{-1/2}\), two-band splitting, or isolated singular angular phase. The separate known geometric kernel \(r^{d(x,y)}\) corresponds only to \(c=1\), not the oscillatory classification. The result is not claimed as a new general radial positivity criterion.

## Limitations

The theorem is confined to homogeneous trees of finite branching degree \(q+1\) and geometric damping \(0\le r\le1\); it does not classify arbitrary trees, spatially varying oscillations, or non-geometric radial decays. The originality comparison is bounded by the inspected literature; an equivalent calculation in less accessible literature remains possible. No independent audit or independent mathematical validation is asserted. An earlier 1980 paper on positive-definite functions on free groups was identified bibliographically but not materially inspected in full.

## References

1. A. Figà-Talamanca and M. A. Picardello, *Spherical functions and harmonic analysis on free groups*, Journal of Functional Analysis **47** (1982), 281–304, DOI: `10.1016/0022-1236(82)90108-2`; author-uploaded readable transcription: https://www.researchgate.net/publication/238859798_Spherical_functions_and_harmonic_analysis_on_free_groups.
2. Y. Elon, *Gaussian Waves on the Regular Tree*, arXiv:`0907.5065`, first public submission 2009-07-29, https://arxiv.org/pdf/0907.5065; Sections 1–2, especially the adjacency resolvent and covariance formula.
3. I. Vergara, *Positive definite radial kernels on homogeneous trees and products*, arXiv:`1907.11476`, first submitted 2019-07-26, https://arxiv.org/pdf/1907.11476; Theorem 1.2 and Sections 1, 4.
4. L. De Michele and A. Figà-Talamanca, *Positive definite functions on free groups*, American Journal of Mathematics **102** (1980), 503–509, DOI: `10.2307/2374112` (bibliographic identification only; no substantive noncoverage conclusion drawn).

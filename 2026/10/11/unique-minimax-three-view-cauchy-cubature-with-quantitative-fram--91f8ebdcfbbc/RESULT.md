# Unique minimax three-view Cauchy cubature with quantitative frame rigidity

## Finding

For each compact convex body \(K\subset\mathbb R^3\) with nonempty interior, let \(S(K)>0\) be its surface area and let
\[
B_K(u)=\operatorname{area}(K|u^\perp)
\]
be its ordinary planar projection area. Choose **exactly three unoriented unit directions** \(u_1,u_2,u_3\in S^2\) and calibrated positive weights \(w_1,w_2,w_3>0\), \(\sum_iw_i=1\). Define
\[
\widehat S_{u,w}(K)=4\sum_{i=1}^3w_iB_K(u_i),\qquad
E(u,w)=\sup_{K}\left|\frac{\widehat S_{u,w}(K)}{S(K)}-1\right|.
\]

**Complete minimax classification.** One has
\[
\boxed{\min_{u,w}E(u,w)=\frac13.}
\]
The minimizers are **exactly** the mutually orthogonal triples with the equal weights \(w_i=1/3\), up to relabelling, changing individual signs, and ambient Euclidean orthogonal transformations. No nonorthogonal triple or unequal-weight triple attains the minimum.

**Quantitative stability with optimal exponents.** Suppose
\[
0\le\varepsilon<\frac23,\qquad E(u,w)\le\frac13+\varepsilon.
\]
Then for all \(i\),
\[
\boxed{-\frac\varepsilon2\le w_i-\frac13\le\varepsilon,}
\]
and for every \(i\ne j\),
\[
\boxed{
|\langle u_i,u_j\rangle|
\le\frac{3\sqrt{\varepsilon(4+3\varepsilon)}}{2(1+3\varepsilon)}
\le3\sqrt\varepsilon.
}
\]
The two weight bounds are sharp even for orthogonal triples. The square-root **exponent** in the direction bound cannot be improved uniformly; the displayed numerical coefficient is not asserted to be the best possible stability coefficient.

More precisely, for
\[
u_1=e_1,\quad
u_2=\sin\theta\,e_1+\cos\theta\,e_2,\quad
u_3=e_3,\quad
w_1=w_2=w_3=\frac13,\quad
0\le\theta\le\frac\pi6,
\]
one has the exact formulas
\[
\boxed{E(u,w)=1-\frac23\cos\theta,\qquad
|\langle u_1,u_2\rangle|=\sin\theta.}
\]
Thus \(E-1/3\sim\theta^2/3\) but the off-diagonal Gram entry is \(\sim\theta\).

## Assumptions and scope

All directions are unit vectors on the Euclidean unit sphere. The vectors are allowed to be repeated or dependent when defining the minimax problem. A rule is calibrated by \(\sum_iw_i=1\), exactly the condition making it correct for balls; scaling all weights arbitrarily is **not** permitted. Although we assume \(w_i>0\), the lower bound holds equally for nonnegative calibrated weights.

The supremum in \(E\) runs over full-dimensional convex bodies, without smoothness or symmetry assumptions. We do not claim it is attained by any full-dimensional body: thin-body limits suffice and are treated carefully in the proof. The result concerns the ordinary Cauchy kernel \(|\langle u,v\rangle|\), not the quadratic kernel \(\langle u,v\rangle^2\), for which the cited recent source has an exact three-direction rule.

The primary MSC2020 classification is \(52A22\), integral geometry of convex sets. Only the three-dimensional three-view problem is classified here; there is no assertion of an \(N\)-view optimum for arbitrary \(N\) or a sharp best *constant* in the direction-stability estimate.

## Proof

**1. Exact reduction to a spherical potential.** For the surface area measure \(S_K\) on \(S^2\), Cauchy's projection formula is
\[
B_K(u)=\frac12\int_{S^2}|\langle u,v\rangle|\,dS_K(v).
\]
Put
\[
q(v)=\sum_{i=1}^3w_i|\langle u_i,v\rangle|.
\]
Because \(S(K)=S_K(S^2)\), the relative estimation error is
\[
\frac{\widehat S_{u,w}(K)}{S(K)}-1
=\frac1{S(K)}\int_{S^2}(2q(v)-1)\,dS_K(v).
\]
Consequently
\[
\boxed{E(u,w)=\max_{v\in S^2}|2q(v)-1|.}\tag{1}
\]
For completeness, the upper bound follows immediately by integration. For the reverse, fix a unit normal \(v_0\) maximizing the continuous even integrand's absolute value, and let \(\sigma\) be normalized round surface measure. The measure
\[
\eta_\tau=(1-\tau)\frac{\delta_{v_0}+\delta_{-v_0}}2+\tau\sigma,
\qquad 0<\tau<1,
\]
has zero first moment and is not concentrated on any great circle. Minkowski's existence theorem therefore provides a full-dimensional convex body whose surface area measure is \(\eta_\tau\). Its error tends to \(2q(v_0)-1\) as \(\tau\downarrow0\) because \(q\) is even. Taking absolute values proves (1). This is precisely the sharp convex-body defect principle established by the recent source.

**2. Global lower bound and characterization of equality.** Fix an index \(i\), and choose a unit vector \(v_i\) perpendicular to the other two sampling directions. Such a vector always exists, even for dependent triples. Then
\[
q(v_i)=w_i|\langle u_i,v_i\rangle|\le w_i.
\]
As one of the three calibrated weights is at most \(1/3\),
\[
\min_{S^2}q\le\min_iw_i\le\frac13.
\]
Formula (1) implies
\[
E(u,w)\ge1-2\min_{S^2}q\ge\frac13.
\]

For an orthonormal triple with weights \(1/3\), write \(v=\sum_i v_i u_i\). Then
\[
q(v)=\frac{|v_1|+|v_2|+|v_3|}{3},\qquad \sum_iv_i^2=1,
\]
and the Euclidean-\(\ell_1\) inequalities give
\[
\frac13\le q(v)\le\frac1{\sqrt3}.
\]
Since \(2/\sqrt3-1<1/3\), equation (1) gives \(E=1/3\).

Conversely, suppose \(E=1/3\). Equation (1) gives \(q(v)\ge1/3\) for every unit \(v\). For each \(i\), the preceding perpendicular choice yields \(w_i\ge q(v_i)\ge1/3\). Calibration makes every weight equal to \(1/3\), and therefore
\[
\frac13\le q(v_i)=\frac13|\langle u_i,v_i\rangle|\le\frac13.
\]
Thus \(|\langle u_i,v_i\rangle|=1\), so \(u_i\) is parallel to \(v_i\) and is perpendicular to the other two directions. This holds for all \(i\), proving uniqueness of the orthogonal equal-weight design.

**3. Quantitative near-rigidity.** Suppose \(E\le1/3+\varepsilon\) with \(0\le\varepsilon<2/3\). By (1),
\[
q(v)\ge L:=\frac13-\frac\varepsilon2>0
\quad\text{for every unit }v.
\]
The perpendicular vectors above give \(w_i\ge L\). Since the other two weights each exceed \(L\), also \(w_i\le1-2L=1/3+\varepsilon\). This gives the two weight bounds.

For fixed \(i\ne j\), use the same \(v_i\perp u_j\). From
\[
L\le w_i|\langle u_i,v_i\rangle|
\]
and \(w_i\le1/3+\varepsilon\),
\[
|\langle u_i,v_i\rangle|
\ge\frac{\frac13-\frac\varepsilon2}{\frac13+\varepsilon}
=\frac{2-3\varepsilon}{2+6\varepsilon}=:r_\varepsilon.
\]
Decomposing the unit vector \(u_i\) into the \(v_i\)-component and its perpendicular component, and using \(u_j\perp v_i\), yields
\[
|\langle u_i,u_j\rangle|
\le\sqrt{1-|\langle u_i,v_i\rangle|^2}
\le\sqrt{1-r_\varepsilon^2}
=\frac{3\sqrt{\varepsilon(4+3\varepsilon)}}{2(1+3\varepsilon)}
\le3\sqrt\varepsilon.
\]
The final inequality follows by squaring the elementary inequality \(\sqrt{4+3\varepsilon}\le2(1+3\varepsilon)\).

**4. Optimality of the weight bounds and direction exponent.** Keep the directions orthonormal, but put
\[
(w_1,w_2,w_3)=\left(\frac13+\delta,\frac13-\frac\delta2,\frac13-\frac\delta2\right),
\qquad0\le\delta\le\frac16.
\]
For orthogonal directions,
\[
\min q=\min_iw_i=\frac13-\frac\delta2,
\quad\max q=\sqrt{\sum_iw_i^2}
=\sqrt{\frac13+\frac32\delta^2}.
\]
For the indicated range, \(\max q\le\sqrt{3/8}<2/3\); hence the lower tail dominates in (1) and
\[
E=\frac13+\delta.
\]
Taking \(\varepsilon=\delta\) gives equality simultaneously in the upper weight deviation for \(i=1\) and the lower deviation for \(i=2,3\).

For the angular sharpness family stated in the Finding, the support function is
\[
3q(v)=|v_1|+|\sin\theta\,v_1+\cos\theta\,v_2|+|v_3|.
\]
The matrix sending \(v\) to these three signed expressions has inverse columns of Euclidean lengths \(\sec\theta,\sec\theta,1\), so its \(\ell_1\)-to-\(\ell_2\) inverse norm is \(\sec\theta\). Therefore \(\min q=\cos\theta/3\), with equality at \(v=e_2\). Moreover,
\[
\max q=\frac13\max_{s_i\in\{\pm1\}}\left\|\sum_i s_i u_i\right\|_2
=\frac13\sqrt{3+2\sin\theta}.
\]
For \(0\le\theta\le\pi/6\), \(\max q\le2/3\), so the negative deviation in (1) dominates. Hence
\[
E=1-\frac23\cos\theta,
\quad E-\frac13=\frac23(1-\cos\theta)\sim\frac{\theta^2}{3},
\quad |\langle u_1,u_2\rangle|=\sin\theta\sim\theta.
\]
This rules out an all-rule direction-stability estimate of order \(o(\sqrt\varepsilon)\).

## Verification

The accompanying exact-arithmetic symbolic checker verifies all rational coefficient identities in the stability estimate, the orthogonal-weight example's squared norm, the support-function inverse columns, and the cosine-tilt example's signed-sum profile. The universal convex-body supremum and the uniqueness implication are proved analytically above; finite symbolic checks do not stand in for those proofs.

An independent normalization check takes a Euclidean ball, for which each projection has area \(S(K)/4\), so every calibrated rule estimates its surface area exactly.

## Relationship to prior work

Kiderlen and Meschenmoser (2009) provide sharp inradius/circumradius error bounds for every **fixed** Crofton cubature rule and explicitly record the interval \(2/3\le\widehat S/S\le2/\sqrt3\) for the standard three coordinate directions in the three-dimensional cubic-grid setting. Thus the numerical error \(1/3\) **for an orthogonal rule is previously known** and is not claimed as a new observation. Their full-text argument does not optimize among all possibly oblique three-direction rules, prove the unique globally minimax calibrated triple, or give the near-optimal frame and weight rigidity inequalities.

Fu, Wang, and Yan (2023) prove that when the number of vectors does not exceed ambient dimension, an orthogonal configuration minimizes the **maximum** over directions of the unweighted sum of absolute inner products. This is a different objective from the present Cauchy error, which optimizes the **largest deviation above or below a fixed target**, permits unequal calibrated weights, and is controlled here by an adversarial **minimum**. Their theorem does not imply the asserted weighted full-error minimax classification or the quantitative stability law.

An's 2026 exact finite integral geometry paper proves the sharp convex-body defect identity, impossibility of universal exactness for a finite signed Cauchy rule, and an \(O(t^{-1})\) error for spherical designs. It also classifies exact three-direction rules for the *quadratic* kernel; its inspected full text does not solve the calibrated three-direction ordinary Cauchy minimax problem. The present finding uses its defect reduction to establish the full global optimum, unique optimizer, and sharp-exponent near-optimal stability for the ordinary Cauchy kernel.

## Limitations

The rules are restricted to **three** unoriented directions and to positive weights summing to one. Uncalibrated estimators with a freely chosen overall multiplier are a different minimax problem. No optimality is claimed for four or more directions.

The coefficient \(3\) in the direction stability bound is convenient and explicit, not claimed best possible. Only the exponent \(1/2\) is shown to be optimal.

The worst-case error is a supremum over full-dimensional bodies and is approached by increasingly flattened bodies; it need not be attained by any single full-dimensional convex body. The support-function moment argument is the proof of this supremum statement, not a finite numerical sampling claim.

## References

1. Congpei An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs*, arXiv:2609.05869v1, first submitted 5 September 2026. See Theorem 3.2 and Sections 5--6.
2. Markus Kiderlen and Daniel Meschenmoser, *Error Bounds for Surface Area Estimators Based on Crofton's Formula*, Image Analysis and Stereology 28 (2009), 165--177, DOI:10.5566/ias.v28.p165-177. See Lemma 1, Example 2, and the three-dimensional grid discussion.
3. Weibo Fu, Guanyang Wang, and Jun Yan, *On the Minimax Spherical Designs*, Random Structures & Algorithms 62 (2023), 131--154, DOI:10.1002/rsa.21087. See Proposition 2.2 and Theorem 2.7.
4. Rolf Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, 2nd expanded ed., Cambridge University Press, 2014 (Minkowski existence and surface area measures).

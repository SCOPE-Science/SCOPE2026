# Exact Minkowski symmetry and unique centers of all Euclidean ball truncations

## Finding

Let \(d\ge2\) and \(-1<a<1\). Define the (closed, full-dimensional) truncated unit ball
\[
K_{d,a}=\{(t,y)\in\mathbb R\times\mathbb R^{d-1}:t^2+\|y\|^2\le1,\ t\le a\}.
\]
For a convex body \(K\), define its Minkowski symmetry in the **reflection-ratio** convention by
\[
\operatorname{sym}(K)=\max\{\lambda\in[0,1]:\exists c\in K,\quad c-\lambda(K-c)\subseteq K\}.
\]
Then the complete one-parameter law is
\[
\boxed{\operatorname{sym}(K_{d,a})=\lambda_a
=\frac{a+\sqrt{(1-a)^2+1}}2},\qquad
\boxed{c_a=\frac{a-\lambda_a}{1+\lambda_a}e_1},
\]
where \(c_a\) is the **unique** maximizing Minkowski center. Both the symmetry and its normalized axial center position are independent of dimension. The optimal reflected copy contacts the cut hyperplane at the image of the negative pole and contacts the unit sphere along the reflected entire rim.

The symmetry is strictly increasing in \(a\), with
\[
\lim_{a\downarrow-1}\lambda_a=\frac{\sqrt5-1}{2},\qquad
\lambda_0=\frac1{\sqrt2},\qquad
\lim_{a\uparrow1}\lambda_a=1.
\]
In the natural thin-cap blowup, the limiting truncated paraboloid
\[
P_d=\{(s,y)\in\mathbb R\times\mathbb R^{d-1}:0\le s\le1,\ \|y\|^2\le s\}
\]
has symmetry exactly \((\sqrt5-1)/2\), again independent of \(d\), with unique Minkowski center \(((\sqrt5-1)/2)e_1\). All nonsingular affine images of these bodies share the respective symmetry values.

## Assumptions and scope

The dimension is any integer \(d\ge2\). The truncation parameter lies strictly between \(-1\) and \(1\); the limiting point at \(a=-1\) is not a full-dimensional body. The reflection-ratio convention \(\operatorname{sym}\in[1/d,1]\) is the reciprocal of the alternative Minkowski **asymmetry** convention \(s(K)\in[1,d]\). The center is considered in the original coordinates with clipping normal \(e_1\). A ball is not a special affine image of a nontrivially truncated ball, so distinct cap depths are not collapsed by the affine invariance of the index. The \(a=0\) half-ball special case was known in Belloni--Freund (2008), Section 3.2, and is not asserted as new.

## Proof

**Step 1: Upper bound from two independent boundary orbits.** Fix any feasible \(\lambda\in[0,1]\) and center \(c\), and let \(z=(1+\lambda)c\). The inclusion is equivalent to \(z-\lambda K_{d,a}\subseteq K_{d,a}\). The negative pole \(-e_1\in K_{d,a}\) and the upper clipping plane force
\[
z_1+\lambda\le a.\tag{1}
\]
Every point \(x_v=(a,\sqrt{1-a^2}\,v)\), \(v\in S^{d-2}\), belongs to the unit sphere and the rim of \(K_{d,a}\). Their reflected images belong to the unit ball, so, maximizing over \(v\),
\[
(z_1-\lambda a)^2+(\|z_\perp\|+\lambda\sqrt{1-a^2})^2\le1.\tag{2}
\]
Define \(\lambda_a=(a+\sqrt{(1-a)^2+1})/2\); then \(0<\lambda_a<1\), \(\lambda_a>a\), and
\[
\lambda_a^2-a\lambda_a=\frac{1-a}{2}.\tag{3}
\]
Suppose for contradiction that a feasible \(\lambda>\lambda_a\) exists. Since \(\lambda>\lambda_a>a\), we have \(a-(1+a)\lambda<0\); by (1), \(z_1-\lambda a\le a-(1+a)\lambda<0\). Substituting this bound in (2) and dropping \(\|z_\perp\|\) gives
\[
1\ge [a-(1+a)\lambda]^2+\lambda^2(1-a^2)
=a^2+2(1+a)(\lambda^2-a\lambda).
\]
Because \(1+a>0\), this implies \(\lambda^2-a\lambda\le(1-a)/2\), in contradiction with \(\lambda>\lambda_a\) and (3). Therefore \(\operatorname{sym}(K_{d,a})\le\lambda_a\).

**Step 2: Constructive sharpness.** Put \(\lambda=\lambda_a\) and \(z=(a-\lambda)e_1\), and define \(c=z/(1+\lambda)\). For any \(x=(t,y)\in K_{d,a}\), we have \(t\ge-1\), hence
\[
(z-\lambda x)_1=a-\lambda-\lambda t\le a.\tag{4}
\]
Since \(a-\lambda<0\) and \(t\le a\),
\[
\begin{aligned}
\|z-\lambda x\|^2
&=(a-\lambda)^2+\lambda^2(t^2+\|y\|^2)-2\lambda(a-\lambda)t\\
&\le(a-\lambda)^2+\lambda^2-2\lambda(a-\lambda)a\\
&=a^2+2(1+a)(\lambda^2-a\lambda)=1,
\end{aligned}
\]
using (3). Thus \(z-\lambda K_{d,a}\subseteq K_{d,a}\). The chosen \(c\) lies strictly between the negative pole and the clipping plane since \(a>-1\), \(0<\lambda<1\), and \(\lambda>a\); in particular \(c\in K_{d,a}\). Equality in (4) holds at \(-e_1\), while the norm bound is sharp on the entire rim \(x_v\).

**Step 3: Unique center.** Suppose \(\lambda=\lambda_a\) and \(z'\) is any feasible translation parameter. The same inequalities (1)--(2) apply, and the scalar lower bound in Step 1 is now an equality because of (3). Consequently equality must hold both in (1) and in the discarded nonnegative term, forcing \(z'_1=a-\lambda_a\) and \(z'_\perp=0\). This gives the unique center \(c_a=z'/(1+\lambda_a)\).

**Step 4: Monotonicity and two limits.** Direct differentiation yields
\[
\lambda_a'=\frac12\left(1+\frac{a-1}{\sqrt{(1-a)^2+1}}\right)>0,
\qquad
\lambda_a''=\frac1{2((1-a)^2+1)^{3/2}}>0.
\]
Substituting \(a=-1,0,1\) into the continuous closed formula gives the stated endpoint values.

**Step 5: The universal parabolic limit, with a direct independent proof.** Write \(\delta=a+1\) and make the invertible affine change \(s=(t+1)/\delta\), \(y'=y/\sqrt{2\delta}\). This transforms \(K_{d,a}\) exactly into
\[
0\le s\le1,\qquad \|y'\|^2\le s-\tfrac\delta2s^2.
\]
As \(\delta\downarrow0\), these sets converge to \(P_d\). More decisively, let \(\gamma=(\sqrt5-1)/2\), so \(\gamma+\gamma^2=1\). For the limit \(P_d\), write the reflected-copy parameter as \(z=(1+\lambda)c\). The apex \((0,0)\) requires \(z_1\le1\), while every rim point \((1,v)\), \(\|v\|=1\), requires
\[
z_1-\lambda\ge (\|z_\perp\|+\lambda)^2\ge\lambda^2.
\]
Thus \(\lambda+\lambda^2\le1\), so \(\lambda\le\gamma\). Conversely \(z=(1,0)\) and \(\lambda=\gamma\) work: \((s,y)\in P_d\) maps to \((1-\gamma s,-\gamma y)\), whose squared transverse norm satisfies \(\gamma^2\|y\|^2\le\gamma^2s\le1-\gamma s\) for \(0\le s\le1\). The two equalities at \(\lambda=\gamma\) force \(z=(1,0)\), so the unique center is \(z/(1+\gamma)=\gamma e_1\). This proves the limit theorem without invoking continuity of an optimized invariant.

**Step 6: Affine invariance.** If \(A\) is invertible and \(b\) arbitrary, the inclusion \(c-\lambda(K-c)\subseteq K\) is equivalent under \(x\mapsto Ax+b\) to the same inclusion for \(AK+b\) about \(Ac+b\). Consequently the formula applies to all full-dimensional ellipsoids clipped by one non-tangent affine hyperplane, after normalizing ellipsoid and plane.

## Verification

A standalone standard-library Python diagnostic (`verify.py`) evaluates the closed expression, its quadratic identity and both contact equalities, then tests the reflected inclusion on deterministic pseudorandom points in dimensions \(2,3,5,12\) over nine truncation parameters. It separately checks the limiting paraboloid in dimensions \(2,3,8\). A complete run produced **106,853 successful checks**. The mathematical proof above, not finite sampling, establishes the claims for every admissible real parameter and every finite dimension.

## Relationship to prior work

Belloni and Freund, *On the symmetry function of a convex set* (2008), Section 3.2, explicitly give \(\operatorname{sym}(K_{d,0})=1/\sqrt2\) and the unique half-ball center (up to reversing the first coordinate). That important special case is **prior work**, not the novelty claim here. They develop general symmetry inequalities and affine invariance but do not present the dependence on arbitrary cap depth or the thin-cap paraboloid law. The 2023 work of den Hertog, Pauphilet, and Soali studies computational Minkowski centers and analytic examples such as positive-orthant norm balls, and their numerical methods concern intersections of ellipsoids. Xiong and Freund's 2026 article establishes a symmetry-dependent ellipsoidal rounding bound for every convex body; it uses the symmetry value as an input and does not give this complete cap-depth family or its unique-center formula. Brandenberg, González Merino, and Grundbacher's 2026 work concerns Minkowski-asymmetry stability near simplices rather than cap-depth values.

The present proposed contribution is the **full open interval of cut positions**, the **dimension-free sharp formula**, the **unique optimizing center and contact geometry**, and the **universal golden-ratio paraboloid degeneration**. An equivalent calculation in less-indexed stereology, convexity or optimization literature remains a priority risk; database-search silence cannot prove novelty.

## Limitations

This is not a determination of the optimal ellipsoidal rounding factor; a general rounding theorem converts the symmetry value into a guaranteed upper bound but does not imply that bound is attained by these caps. The endpoint \(a=-1\) is excluded because the cap degenerates to a point; the paraboloid is a separate affine-blowup limit, not the original point-set limit. At \(a=1\) the full unit ball has symmetry \(1\), consistent with the limit. In dimension one every interval has symmetry \(1\); the theorem accordingly requires \(d\ge2\). The \(a=0\) half-ball identity was previously published. Historical priority and any generalization beyond one hyperplane are not established; there is no independent audit.

## References

1. A. Belloni and R. M. Freund, *On the symmetry function of a convex set*, Mathematical Programming 111 (2008), 57--93. DOI: 10.1007/s10107-006-0074-4. Full manuscript: https://people.duke.edu/~abn5/Symmetry.pdf .
2. D. den Hertog, J. Pauphilet, and M. Y. Soali, *Minkowski Centers via Robust Optimization: Computation and Applications*, Operations Research 72 (2024), 2135--2152, first online 2023. DOI: 10.1287/opre.2023.2448. Manuscript: https://lbsresearch.london.edu/id/eprint/2824/1/Minkowski_Final.pdf .
3. Z. Xiong and R. M. Freund, *Symmetry-dependence in Rounding of a Convex Body*, first publicly available 2026-08-31, arXiv:2608.30876. https://arxiv.org/abs/2608.30876 .
4. R. Brandenberg, B. González Merino, and F. Grundbacher, *Tight Stability Estimates Near the Simplex and Improved Bounds for the Diameter of the Banach--Mazur Compactum in Fixed Dimensions*, 2026-07-29, arXiv:2607.27041. https://arxiv.org/abs/2607.27041 .

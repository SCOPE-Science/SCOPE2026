# A dimension-five monotonicity threshold for the isotropic constant of a one-corner clipped cube

## Finding
For an integer \(d\ge2\), remove a growing simplex cap from exactly one vertex of a standard unit cube:
\[
K_d(t)=[0,1]^d\cap\Bigl\{x:\sum_{i=1}^d x_i\le d-t\Bigr\},\qquad 0\le t\le1.
\]
Let \(X\) be uniform with respect to \(d\)-dimensional Lebesgue measure on \(K_d(t)\), and put
\[
L(K)^{2d}=\frac{\det\operatorname{Cov}(X_K)}{\operatorname{Vol}_d(K)^2}.
\]
Define \(q=t^d/d!\), \(u=12t^2/((d+1)(d+2))\), and
\[
F=(1-q)\left(1-\frac{qu}{d+1}\right)
  -\frac{3dq(d+1-2t)^2}{(d+1)^2}.
\]
The squared isotropic-constant ratio relative to the cube is exactly
\[
\boxed{\frac{L(K_d(t))^2}{L([0,1]^d)^2}=
\left(\frac{F(1-qu)^{d-1}}{(1-q)^{d+3}}\right)^{1/d}.}
\]
For \(d=2,3,4\), this ratio first decreases and then increases, having one and only one interior minimizer. Its approximate locations are respectively \(0.295991316562\), \(0.526949247340\), and \(0.810464593248\). For **every \(d\ge5\)**, the ratio is strictly decreasing for \(0<t<1\), so the unique minimizer is \(t=1\). This is a sharp transition between dimensions four and five for the same natural geometric deformation.

## Assumptions and scope
The entire statement concerns integer dimensions \(d\ge2\), clipping parameters \(0\le t\le1\), the usual Euclidean/Lebesgue volume in the full ambient space, and the affine-invariant isotropic constant determined by the determinant of the uniform-volume covariance. In this interval the removed piece is exactly one (possibly zero-volume) simplex and never reaches another original cube vertex. The body remains full-dimensional, including at \(t=1\). At \(t=0\), the ratio is one; strict monotonicity statements refer to the open parameter intervals. The dimension-two endpoint \(t=1\) is a triangle; other endpoint bodies are corner-truncated cubes.

## Proof
**Exact moment calculation.** The removed simplex is the image of \(\{y_i\ge0,\ \sum_i y_i\le1\}\) under \(x_i=1-ty_i\). Its volume fraction inside the unit cube is \(q=t^d/d!\). Its coordinate mean is \(1-t/(d+1)\), and its covariance matrix has diagonal \(d t^2/((d+1)^2(d+2))\) and off-diagonal \(-t^2/((d+1)^2(d+2))\). The unit cube has centroid \(\frac12\mathbf1\) and covariance \(I_d/12\). Subtracting unnormalized first and second moments of the cap and then centering shows that the retained covariance has eigenvalue
\[
a=\frac{1/12-q\,t^2/((d+1)(d+2))}{1-q}
\]
with multiplicity \(d-1\) on \(\mathbf1^\perp\), and eigenvalue
\[
b=\frac{1/12-q\,t^2/((d+1)^2(d+2))}{1-q}-
\frac{dq}{(1-q)^2}\left(\frac12-\frac{t}{d+1}\right)^2
\]
on the line \(\mathbb R\mathbf1\). These eigenvalues are positive because the retained body has nonempty interior. Direct simplification gives \(12a=(1-qu)/(1-q)\) and \(12b=F/(1-q)^2\). Since the volume is \(1-q\) and the cube's isotropic constant squared is \(1/12\), taking the covariance determinant proves the boxed formula.

**Derivative certificate.** Treat \(q\) and \(t\) temporarily as independent symbols and write \(u=12t^2/((d+1)(d+2))\), \(G(t)=F(1-qu)^{d-1}/(1-q)^{d+3}\), with the substitution \(q=t^d/d!\). For a rational function \(A(q,t)\), define \(\mathcal T A=t\partial_tA+dq\partial_q A\). On \(0<t<1\), the sign of \(G'\) is the sign of
\[
N=(\mathcal TF)(1-qu)(1-q)-(d-1)(\mathcal T(qu))F(1-q)
 +(d+3)dqF(1-qu),
\]
because its omitted denominator \(tF(1-qu)(1-q)\) is strictly positive. By exact expansion,
\[
\frac{N}{dq}=c_0(d,t)+qc_1(d,t)+q^2c_2(d,t),\qquad
c_0(d,t)=-\frac{2(d^2-6dt+12t^2-6t-1)}{d+1}.
\]
Here \(c_1,c_2\) are specified *without ambiguity* as the coefficients of \(q,q^2\) in the immediately preceding explicit expression \(N/(dq)\). All remaining sign certificates use only this identity, polynomial arithmetic and positive denominators.

For \(d\ge5\) and \(0\le t\le1\), \(c_0\le0\): at \(d=5\), its negative numerator equals \(12(t-1)(t-2)\ge0\), and the quadratic in \(d\) is increasing for \(d\ge5\). Moreover,
\[
c_2=\frac{12t^2}{(d+1)^3(d+2)}
\bigl[3d^3+(14-12t)d^2+(12t^2-24t+21)d+10-12t-12t^2\bigr]>0
\]
when \(t>0\). Since \(q\le1/d!\le1/120\), it remains to show \(c_1+c_2/120<0\). Set \(k=d-5\ge0\) and
\[
P(k,t)=-(d+1)^3(d+2)\bigl(c_1+c_2/120\bigr).
\]
Its degree-four Bernstein expansion is
\[
P(k,t)=\sum_{j=0}^4 b_j(k)\binom4j t^j(1-t)^{4-j},
\]
where the five explicit polynomials are
\[
\begin{aligned}
b_0&=(k+6)^3(k+7)^2(3k+16),\\
b_1&=(k+6)^2(k+7)(3k^3+52k^2+298k+570),\\
b_2&=(k+6)(180k^5+5280k^4+61260k^3+351597k^2+1000279k+1133140)/60,\\
b_3&=(k+6)(60k^5+1700k^4+18760k^3+101117k^2+268645k+285736)/20,\\
b_4&=(k+4)(30k^5+880k^4+9910k^3+53937k^2+144325k+157566)/10.
\end{aligned}
\]
Every factor or coefficient displayed here is positive for \(k\ge0\), hence \(P>0\). This proves \(N<0\) for \(d\ge5\) and \(0<t<1\), including the borderline \(d=5\), where the strict contribution comes from \(c_1+qc_2<0\).

For dimensions \(d\in\{2,3,4\}\), substitute \(q=t^d/d!\) in \(N\). After dividing by the strictly positive factor \(t^d\), and also dividing by \(t-1\) when \(d=2\), obtain polynomials \(p_d(t)\) of respective degrees \(7,10,12\). The transformation \(h_d(z)=(1+z)^{\deg p_d}p_d(z/(1+z))\) sends \(t\in(0,1)\) bijectively to \(z>0\). Exact integer polynomial expansion gives the coefficient-sign sequences of \(h_d\), listed from constant coefficient to leading coefficient:
\[
\begin{array}{c|c|c}
d&\text{sign sequence}&\bigl(\operatorname{sgn}p_d(0),\operatorname{sgn}p_d(1)\bigr)\\\hline
2&++------&(+, -)\\
3&-----++++++&(-,+)\\
4&----------+++&(-,+)
\end{array}
\]
Each row has exactly one sign variation. Descartes' rule permits at most one positive root; the opposite endpoint signs give at least one. For \(d=2\), the extra factor \(t-1\) changes the derivative's sign as required on \((0,1)\). For \(d=3,4\), the factored derivative has the same sign as \(p_d\). Consequently the unique critical point is always a strict global minimum in the interval. Rational sign evaluations trap the three critical parameters respectively in \((295/1000,297/1000)\), \((526/1000,528/1000)\), and \((810/1000,811/1000)\). All signs, polynomial degrees, coefficient expansions and intervals are independently replayed by the supplied exact-symbolic checker.

## Verification
The standalone `check.py` independently triangulates twelve specific clipped cubes (dimensions two through five; depths \(1/5\), \(1/2\), and \(1\)) by a floating-point convex-hull combinatorial decomposition, then integrates every nondegenerate simplex with **exact rational determinants and exact rational first and second moments**. It compares the resulting covariance matrices and volumes with the analytical expressions. The test covers 1,270 boundary simplices before zero-volume degeneracies are discarded, and it confirms 12 complete volumes and covariance matrices. The same program derives the symbolic derivative, verifies the five all-dimensional positive Bernstein coefficients as polynomials in \(k\), checks the three one-sign-change Descartes certificates and verifies rational root isolations. Execution: `python check.py`, with Python 3, SymPy, NumPy and SciPy installed. In the proof, the all-dimensional conclusion follows from explicit symbolic identities and inequalities, not from finite sampling.

## Relationship to prior work
Pournin's 2022 analysis determines local extrema of **sectional volume as a function of hyperplane orientation** at fixed distance from a cube's center. It does not optimize the **volume-normalized determinant of the covariance of the full retained body** as the clipping depth varies. Kipp's 2023 treatment of small perturbations and 2024 treatment of isotropic constants and Platonic solids give general necessary conditions for polytopal **maximizers** and structural descriptions; those results do not give a complete one-corner truncation profile or its minimum and dimension-five threshold. Related exact formulas for vertex-truncated simplices and uniform corner-subsets of cubes apply to different removed-cap configurations; neither asserts the present one-corner minimizer classification. A mathematical record treating the John ellipsoid of a capped hypercube concerns the **largest inscribed ellipsoid**, which is not determined by uniform-volume covariance. This work does not claim discovery of the basic simplex cap moment formulas, only their sharp global isotropic minimizer classification for the one-corner cube family.

## Limitations
No claim is made for \(t>1\), where additional vertices and other cap combinatorics enter, for arbitrary oblique or off-diagonal truncations, for independent truncation depths at multiple vertices, or for global isotropic-constant extremizers among all convex bodies. The historical-priority comparison is best-knowledge rather than exhaustive; another author may have stated the same special-function optimization under different terminology. Approximate minimizers are illustrations, with exact uniqueness proved by polynomial sign certificates. Independent mathematical validation has not been performed.

## References
1. Lionel Pournin, *Local extrema for hypercube sections*, arXiv:2203.15054, first public version 28 March 2022, https://arxiv.org/abs/2203.15054.
2. Christian Kipp, *Small perturbations of polytopes*, arXiv:2303.18033, first public version 31 March 2023, https://arxiv.org/abs/2303.18033.
3. Christian Kipp, *Isotropic constants and platonic solids*, arXiv:2407.01353, first public version 1 July 2024, https://arxiv.org/abs/2407.01353.

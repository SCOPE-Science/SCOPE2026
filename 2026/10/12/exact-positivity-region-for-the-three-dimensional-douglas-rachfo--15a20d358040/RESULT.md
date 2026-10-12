# Exact positivity region for the three-dimensional Douglas–Rachford heat scheme

## Finding
Consider the original three-dimensional Douglas–Rachford finite-difference scheme for the heat equation on a rectangular tensor grid with homogeneous Dirichlet boundary conditions. Let
\[
T_n=\operatorname{tridiag}(-1,2,-1),
\qquad
P_n(s)=(I+sT_n)^{-1},
\]
and suppose that the interior grid has \(n_x,n_y,n_z\ge2\) points in the three coordinate directions. Put
\[
s_x=\frac{\Delta t}{h_x^2},
\qquad
s_y=\frac{\Delta t}{h_y^2},
\qquad
s_z=\frac{\Delta t}{h_z^2}.
\]

For \(s>0\), define
\[
d_n(s)=(P_n(s))_{11}.
\]
Then the completed Douglas–Rachford step is entrywise nonnegative if and only if
\[
3d_{n_x}(s_x)d_{n_y}(s_y)
\ge
d_{n_x}(s_x)+d_{n_y}(s_y),
\]
\[
3d_{n_x}(s_x)d_{n_z}(s_z)
\ge
d_{n_x}(s_x)+d_{n_z}(s_z),
\]
and
\[
3d_{n_y}(s_y)d_{n_z}(s_z)
\ge
d_{n_y}(s_y)+d_{n_z}(s_z).
\]

For a cubic \(n\times n\times n\) grid with common mesh width \(h\), this collapses to the sharp scalar condition
\[
d_n\!\left(\frac{\Delta t}{h^2}\right)\ge\frac23.
\]
Writing
\[
D_0(s)=1,\qquad
D_1(s)=1+2s,
\]
and
\[
D_k(s)=(1+2s)D_{k-1}(s)-s^2D_{k-2}(s),
\]
one has
\[
d_n(s)=\frac{D_{n-1}(s)}{D_n(s)}.
\]
Hence, if \(\tau_n\) is the unique positive solution of
\[
D_n(\tau_n)=\frac32D_{n-1}(\tau_n),
\]
then
\[
R_{\mathrm{DR},n}\ge0
\quad\Longleftrightarrow\quad
0\le\frac{\Delta t}{h^2}\le\tau_n.
\]
Moreover,
\[
\tau_n\uparrow\frac{3-\sqrt6}{2}
=
0.275255128608411\ldots.
\]

For \(n=2\),
\[
\tau_2=\frac{\sqrt7-1}{6}
=
0.274291885177432\ldots.
\]
At
\[
\frac{\Delta t}{h^2}=\frac7{25},
\]
the one-dimensional resolvent is
\[
P_2\!\left(\frac7{25}\right)
=
\frac1{1472}
\begin{pmatrix}
975&175\\
175&975
\end{pmatrix}.
\]
A one-coordinate-difference entry of the three-dimensional step matrix is then
\[
\frac{175}{1472}
\left[
3\left(\frac{975}{1472}\right)^2
-
2\left(\frac{975}{1472}\right)
\right]
=
-\frac{3241875}{3189506048}<0.
\]
The exact semidiscrete heat flow is positive, so this is a genuine sign failure of the time discretization.

## Assumptions and scope
The result concerns the three-stage scheme printed as equations (2.5)–(2.6) in the original Douglas–Rachford heat-conduction paper. The spatial discretization is the standard centered second difference on a rectangular Cartesian grid, with homogeneous Dirichlet data. The result is about entrywise nonnegativity of the completed one-step map acting on interior data.

The restriction \(n_x,n_y,n_z\ge2\) makes every coordinate resolvent have strictly positive off-diagonal entries when \(\Delta t>0\); this is used for necessity of each pair condition. Degenerate one-point coordinate directions can be treated separately but are not part of the theorem.

The result does not claim positivity of intermediate stages, nonhomogeneous boundary forcing, variable coefficients, nonrectangular domains, or later Douglas and Douglas–Gunn variants.

## Proof
Let
\[
A_x=-h_x^{-2}T_{n_x}\otimes I\otimes I,
\]
and define \(A_y,A_z\) analogously. These three matrices commute. Eliminating the two intermediate stages from the original scheme gives
\[
(I-\Delta t A_x)(I-\Delta t A_y)(I-\Delta t A_z)u^{m+1}
=
\left[
I+\Delta t^2(A_xA_y+A_xA_z+A_yA_z)
-\Delta t^3A_xA_yA_z
\right]u^m.
\]
Let
\[
P_x=(I-\Delta t A_x)^{-1},\qquad
P_y=(I-\Delta t A_y)^{-1},\qquad
P_z=(I-\Delta t A_z)^{-1}.
\]
Since
\[
\Delta t A_xP_x=P_x-I
\]
and similarly in the other directions, the completed step matrix is exactly
\[
R_{\mathrm{DR}}
=
I+3P_xP_yP_z-P_xP_y-P_xP_z-P_yP_z.
\]

Each directional resolvent is a tensor lift of a strictly positive one-dimensional inverse:
\[
P_x=P_{n_x}(s_x)\otimes I\otimes I,
\]
with analogous expressions for \(P_y,P_z\). Write \(p,q,r\) for entries of the three one-dimensional resolvents. A matrix entry of \(R_{\mathrm{DR}}\) has one of four forms.

If all three coordinate indices differ, it equals
\[
3pqr>0.
\]
If exactly two coordinates differ, for example \(x,y\), it equals
\[
pq(3r_{kk}-1).
\]
If exactly one coordinate differs, for example \(x\), it equals
\[
p_{ii'}
\left(3q_{jj}r_{kk}-q_{jj}-r_{kk}\right).
\]
If no coordinate differs, it equals
\[
1+3abc-ab-ac-bc,
\]
where \(a,b,c\) are diagonal entries of the directional resolvents.

It remains to identify the smallest one-dimensional diagonal entry. Let
\[
D_k(s)=\det(I+sT_k).
\]
Continuant expansion gives
\[
D_0=1,\qquad D_1=1+2s,\qquad
D_k=(1+2s)D_{k-1}-s^2D_{k-2}.
\]
The standard tridiagonal inverse formula gives
\[
(P_n(s))_{ii}
=
\frac{D_{i-1}(s)D_{n-i}(s)}{D_n(s)}.
\]
Set
\[
q_k(s)=\frac{D_k(s)}{D_{k-1}(s)}.
\]
Then
\[
q_1=1+2s,\qquad
q_{k+1}=1+2s-\frac{s^2}{q_k}.
\]
For every \(s>0\), the sequence \(q_k\) decreases strictly in \(k\). Comparing products of early and late \(q_k\)'s therefore shows
\[
(P_n(s))_{ii}\ge(P_n(s))_{11}
=
\frac{D_{n-1}(s)}{D_n(s)}
=
d_n(s).
\]
Thus the minimum diagonal is attained at the two boundary-adjacent interior points.

Suppose the three displayed pair inequalities hold at the minima. Each forces the two participating minima to exceed \(1/3\). Consequently the function
\[
F(a,b)=3ab-a-b
\]
is increasing in each variable throughout the relevant diagonal ranges, so every exactly-one-coordinate-difference entry is nonnegative. The same inequalities imply every diagonal minimum exceeds \(1/3\), hence every exactly-two-coordinate-difference entry is nonnegative. Finally, from
\[
3bc\ge b+c
\]
one obtains
\[
1+3abc-ab-ac-bc
\ge
1-bc\ge0.
\]
This proves sufficiency.

Conversely, if one pair condition fails, choose diagonal indices attaining the two corresponding minima and choose distinct indices in the remaining coordinate. The off-diagonal resolvent entry in that remaining coordinate is strictly positive, so the associated exactly-one-coordinate-difference entry is negative. This proves necessity.

For a cube, all three minima coincide, and the criterion becomes
\[
3d_n(s)^2-2d_n(s)\ge0.
\]
Since \(d_n(s)>0\), this is exactly
\[
d_n(s)\ge\frac23.
\]
The derivative identity
\[
\frac{d}{ds}(I+sT_n)^{-1}
=
-(I+sT_n)^{-1}T_n(I+sT_n)^{-1}
\]
shows that every diagonal entry, hence \(d_n(s)\), is strictly decreasing in \(s\). Since \(d_n(0)=1\) and \(d_n(s)\to0\) as \(s\to\infty\), the threshold \(\tau_n\) exists and is unique.

Because \(q_n(s)\) decreases in \(n\), \(d_n(s)=1/q_n(s)\) increases in \(n\), so \(\tau_n\) increases strictly. The limiting continued fraction solves
\[
q_\infty
=
1+2s-\frac{s^2}{q_\infty},
\]
hence
\[
q_\infty
=
\frac{1+2s+\sqrt{1+4s}}2.
\]
At the limiting threshold \(d_\infty=2/3\), so \(q_\infty=3/2\), giving
\[
s=\frac{3-\sqrt6}{2}.
\]

## Verification
The embedded `verify.py` uses exact rational arithmetic to reconstruct the \(2\times2\) directional resolvent at
\[
s=\frac7{25},
\]
forms the full \(2\times2\times2\) Douglas–Rachford step matrix, and checks that its minimum entry is exactly
\[
-\frac{3241875}{3189506048}.
\]
It also checks the exact \(n=2\) threshold equation, numerically isolates \(\tau_n\) for several \(n\), verifies their strict increase, and compares them with the limiting constant
\[
\frac{3-\sqrt6}{2}.
\]

These computations replay consequences of the proof. The all-grid characterization is analytic and does not depend on finite enumeration.

## Relationship to prior work
Douglas and Rachford introduced the three-stage method for heat conduction in two and three space variables. Their paper derives the three-dimensional eliminated equation and proves unconditional stability of the scheme; it does not formulate entrywise nonnegativity as a matrix condition. Its printed front matter records a presentation to the American Mathematical Society on 1955-12-27.

A later ADI reference entry classifies ADI finite-difference methods under MSC 65M06 and 65N06 and identifies the Douglas–Rachford paper as a foundational source. A 2016 full-text study of ADI stability analyzes the traditional Douglas–Rachford method in two dimensions through growth factors and discusses oscillations near discontinuities; its focus is spectral stability and damping rather than a three-dimensional entrywise positivity region.

Douglas's 1962 paper on three-space-variable alternating-direction methods explicitly distinguishes the earlier first-order three-dimensional scheme from the newer second-order construction developed there. Its searchable introduction was inspected, but a complete full-text comparison was not available in the retrieval path used here. This remains a residual originality risk.

The closest prior result in the present collection gives a sharp positivity threshold for the two-dimensional Peaceman–Rachford heat step. That theorem factorizes into two one-dimensional signed factors and has a different boundary constant. The present three-dimensional Douglas–Rachford map has the coupled form
\[
I+3P_xP_yP_z-P_xP_y-P_xP_z-P_yP_z,
\]
so positivity is governed by three pairwise nonlinear diagonal inequalities and is not implied by the Peaceman–Rachford criterion.

## Limitations
The theorem is specific to the original three-stage first-order Douglas–Rachford heat discretization on rectangular tensor grids with homogeneous Dirichlet conditions. It does not cover the later 1962 second-order three-dimensional method, Douglas–Gunn schemes, variable coefficients, irregular domains, or nonhomogeneous boundary terms.

The result classifies positivity of the completed step, not the two intermediate stage vectors. A method can have a nonnegative completed step while an internal stage changes sign.

The literature search recovered the original full paper, a full 2016 stability-and-oscillation study, and several later ADI references, but the complete body of the 1962 three-space-variable paper was not fully retrievable through the inspected source. The originality conclusion therefore retains the specific risk that an older source may encode the same entrywise criterion in different terminology.

## References
1. J. Douglas, Jr. and H. H. Rachford, Jr., “On the numerical solution of heat conduction problems in two and three space variables,” Transactions of the American Mathematical Society 82 (1956), 421–439. DOI 10.1090/S0002-9947-1956-0084194-4. The paper states that it was presented to the Society on 1955-12-27.
2. J. Douglas, Jr., “Alternating Direction Methods for Three Space Variables,” Numerische Mathematik 4 (1962), 41–63. DOI 10.1007/BF01386295.
3. O. Østerby, “On the Stability of ADI Methods,” DAIMI Report Series 42(598), 2016. DOI 10.7146/dpb.v42i598.25146.
4. Q. Sheng, “ADI Methods,” Encyclopedia of Applied and Computational Mathematics, 2015. DOI 10.1007/978-3-540-70529-1_435.

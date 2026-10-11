# Closed-form distance from the identity to every rank stratum of Chen's correlation orbit space
## Finding
For \(n\ge2\), let
\[
\operatorname{Corr}(n,[r])
=
\{Z\in\mathbb S_+^n:\operatorname{diag}Z=\mathbf1,\ \operatorname{rank}Z\le r\}.
\]
Endow the full elliptope \(\operatorname{Corr}(n)=\operatorname{Corr}(n,[n])\) with Chen's default orbit-space metric \(d_{\mathrm{orb},n}\), obtained from the spherical product metric on row-normalized factors modulo \(O(n)\).

For every \(1\le r\le n\),
\[
\boxed{
\inf_{Z\in\operatorname{Corr}(n,[r])}
d_{\mathrm{orb},n}(I_n,Z)
=
\sqrt n\,\arccos\sqrt{\frac rn}.
}
\tag{1}
\]
The complete minimizer set in (1) is
\[
\boxed{
\left\{
\frac nr P:
P^2=P=P^{\mathsf T},\
\operatorname{rank}P=r,\
\operatorname{diag}P=\frac rn\mathbf1
\right\}.
}
\tag{2}
\]
Equivalently, the minimizers are exactly the Gram matrices of real unit-norm tight frames of \(n\) vectors spanning an \(r\)-dimensional space.

Thus the distance from \(I_n\) to the singular part of the elliptope is
\[
\boxed{
\sqrt n\,\arccos\sqrt{\frac{n-1}{n}},
}
\tag{3}
\]
and the nearest singular matrices are exactly
\[
\boxed{
Z_s=
\frac{nI_n-ss^{\mathsf T}}{n-1},
\qquad
s\in\{\pm1\}^n/\{\pm\mathbf1\}.
}
\tag{4}
\]
There are \(2^{n-1}\) such matrices. They are the signed Gram matrices of a regular simplex.

At the opposite endpoint \(r=1\), formula (2) gives the rank-one cut matrices \(ss^{\mathsf T}\), and (1) becomes
\[
\sqrt n\,\arccos\frac1{\sqrt n}.
\]

## Assumptions and scope
Chen defines, for \(k\le n\), an orbit-space metric \(d_{\mathrm{orb},k}\) on \(\operatorname{Corr}(n,[k])\) by representing a correlation matrix as \(XX^{\mathsf T}\), where the rows of \(X\in\mathbb R^{n\times k}\) have unit norm, and quotienting by the right action of \(O(k)\). The source emphasizes that these metrics depend on \(k\) and recommends \(k=n\) by default on the full elliptope.

The theorem concerns that ambient default metric \(d_{\mathrm{orb},n}\), not the smaller-\(k\) metric intrinsic to a lower-rank orbit space. The distinction matters because the source proves that \(d_{\mathrm{orb},k}\) changes with \(k\).

The inverse cosine is the principal value in \([0,\pi]\). No genericity assumption is made. The minimizers in (2) exist for every \(n\ge r\ge1\); existence follows from the real Schur--Horn theorem applied to the eigenvalue vector consisting of \(r\) ones and \(n-r\) zeros and the constant diagonal \((r/n)\mathbf1\).

## Proof
Chen's distance formula gives, for row-normalized factors \(X,Y\in\mathbb R^{n\times n}\),
\[
d_{\mathrm{orb},n}(XX^{\mathsf T},YY^{\mathsf T})^2
=
\inf_{O\in O(n)}
\sum_{i=1}^n
\arccos^2\!\left(
\left\langle (XO)_{i\cdot},Y_{i\cdot}\right\rangle
\right).
\tag{5}
\]

Take \(X=I_n\). Let \(Z=YY^{\mathsf T}\) have rank \(s\le r\). For a fixed \(O\), replace \(Y\) by \(YO^{\mathsf T}\); this leaves \(Z\) unchanged and turns the inner product in (5) into
\[
\langle e_i,y_i\rangle,
\]
where the unit row vectors \(y_1,\ldots,y_n\) lie in a common \(s\)-dimensional subspace \(U\subset\mathbb R^n\).

Let \(P\) be the orthogonal projection onto \(U\) and put
\[
p_i=P_{ii}=\|Pe_i\|^2.
\]
Then
\[
0\le p_i\le1,
\qquad
\sum_{i=1}^n p_i=\operatorname{tr}P=s.
\tag{6}
\]
Since \(y_i\in U\) and \(\|y_i\|=1\),
\[
\langle e_i,y_i\rangle
=
\langle Pe_i,y_i\rangle
\le
\|Pe_i\|
=
\sqrt{p_i}.
\tag{7}
\]
Because \(\arccos\) is decreasing,
\[
d_{\mathrm{orb},n}(I_n,Z)^2
\ge
\sum_{i=1}^n f(p_i),
\qquad
f(p)=\arccos^2\sqrt p.
\tag{8}
\]

The decisive point is that \(f\) is strictly convex on \((0,1)\). Write
\[
p=\cos^2\theta,
\qquad
0<\theta<\frac{\pi}{2}.
\]
A direct differentiation gives
\[
f''(p)
=
\frac{
2\bigl(\sin(2\theta)-2\theta\cos(2\theta)\bigr)
}{
\sin^3(2\theta)
}.
\tag{9}
\]
The numerator is positive because, for
\[
h(\theta)=\sin(2\theta)-2\theta\cos(2\theta),
\]
one has
\[
h(0)=0,
\qquad
h'(\theta)=4\theta\sin(2\theta)>0.
\]
Thus Jensen's inequality and (6) yield
\[
\sum_i f(p_i)
\ge
n f\!\left(\frac sn\right)
\ge
n f\!\left(\frac rn\right),
\tag{10}
\]
where the second inequality uses that \(f\) is strictly decreasing. Equations (8)--(10) prove the lower bound in (1).

For sharpness, the real Schur--Horn theorem supplies a rank-\(r\) orthogonal projection \(P\) with
\[
P_{ii}=\frac rn
\quad\text{for all }i.
\]
Set
\[
y_i=\sqrt{\frac nr}\,Pe_i.
\]
These are unit vectors, they span \(\operatorname{range}P\), and their Gram matrix is
\[
Z=\frac nr P.
\]
Moreover,
\[
\langle e_i,y_i\rangle
=
\sqrt{\frac rn}
\]
for every \(i\). Substitution into (5) gives equality in (1).

The equality conditions are also rigid. If equality holds in (10), strict convexity forces
\[
s=r,
\qquad
p_i=\frac rn
\quad\text{for every }i.
\]
Equality in (7) then forces
\[
y_i=\frac{Pe_i}{\|Pe_i\|}
=
\sqrt{\frac nr}\,Pe_i.
\]
Hence the Gram matrix is exactly \((n/r)P\), proving the complete minimizer classification (2).

For \(r=n-1\), a rank-\((n-1)\) projection has the form
\[
P=I_n-uu^{\mathsf T}
\]
with \(\|u\|=1\). The constant-diagonal condition says
\[
u_i^2=\frac1n
\]
for every \(i\), so \(u=s/\sqrt n\) for a sign vector \(s\). Substituting into \((n/(n-1))P\) gives (4). Global sign does not change \(ss^{\mathsf T}\), yielding exactly \(2^{n-1}\) nearest singular matrices.

## Verification
The proof is arbitrary-dimensional. Its critical source-dependent input, equation (5), was checked directly against Chen's full text. The same source explicitly states that the general alignment problem has no closed-form solution and is handled numerically, so formula (1) is a closed-form symmetric slice of that metric rather than a reformulation of a displayed source formula.

The existence step in the sharpness argument is an application of the real Schur--Horn theorem: the constant vector \((r/n)\mathbf1\) is majorized by \((1,\ldots,1,0,\ldots,0)\) with \(r\) ones, so a real symmetric projection with that diagonal exists.

The accompanying `verify.py` checks the strict-convexity expression in (9) numerically away from the endpoints and verifies the claimed distances for explicit constant-diagonal projection families at \(r=1\), \(r=n-1\), and \(r=n/2\) when \(n\) is even. These finite checks are corroborative only.

## Relationship to prior work
Chen constructs the quotient geometry used here, proves that rank gives the orbit stratification, recommends the ambient choice \(k=n\) on the full elliptope, and derives equation (5). The paper then states that the resulting nonlinear alignment minimization does not admit a closed-form solution in general and develops Riemannian gradient descent for numerical computation. The present theorem isolates a natural family of those distance problems--from the identity to every lower-rank stratum--and solves all of them exactly, including every minimizer.

Classical finite-frame theory characterizes unit-norm tight frames as minimizers of the quadratic frame potential. That theory explains why the minimizer class in (2) is familiar, but its objective is a Hilbert--Schmidt or chordal quadratic energy, not Chen's sum of squared spherical angles after orthogonal registration. The frame-potential theorem therefore does not supply the value in (1) or the Jensen reduction for the quotient angular metric.

A published-result database search for the exact object, metric, rank-stratum distance, tight-frame formulation, and the closed form \(\sqrt n\,\arccos\sqrt{r/n}\) found no covering statement. The closest indexed metric result located concerns a Wasserstein distance between subspace-supported and isotropic spherical measures; its cost and feasible objects are different and it does not imply Chen's quotient-orbit distance formula.

## Limitations
The formula is centered at \(I_n\). It does not provide a closed form for the distance between two arbitrary correlation matrices, and it does not solve the general alignment problem highlighted by Chen.

The metric parameter is fixed to the source's default ambient choice \(k=n\). Distances \(d_{\mathrm{orb},k}\) for smaller ambient \(k\) are genuinely different and are not covered by (1).

The originality comparison leaves a residual risk that an equivalent identity appears in frame geometry under an uncommon spherical-alignment formulation or in unindexed work. The classical frame-potential and Schur--Horn results are explicitly treated as prior ingredients, not as new contributions.

## References
1. Hengchao Chen, *Quotient Geometry of Bounded or Fixed-Rank Correlation Matrices*, arXiv:2401.03126, first public version 2024-01-06; SIAM Journal on Matrix Analysis and Applications 46 (2025), 121--150, DOI 10.1137/24M1630566.
2. John J. Benedetto and Matthew Fickus, *Finite Normalized Tight Frames*, Advances in Computational Mathematics 18 (2003), 357--385, DOI 10.1023/A:1021323312367.
3. Alfred Horn, *Doubly Stochastic Matrices and the Diagonal of a Rotation Matrix*, American Journal of Mathematics 76 (1954), 620--630.

# Sharp squared-correlation envelope for the three-dimensional Gaussian square product
## Finding
Let \(X_1,X_2,X_3\) be centered jointly Gaussian random variables with unit variances, and write
\[
\rho_{ij}=\mathbb E[X_iX_j],\qquad
S=\rho_{12}^2+\rho_{13}^2+\rho_{23}^2.
\]
Define the three-dimensional square-product deficit by
\[
\Delta=\mathbb E[X_1^2X_2^2X_3^2]-1.
\]
For every fixed feasible \(S\in[0,3]\), the exact minimum of \(\Delta\) over all Gaussian correlation matrices with that value of \(S\) is
\[
\Delta_{\min}(S)=
\begin{cases}
2S-8(S/3)^{3/2},&0\le S\le 3/4,\\
6S-4,&3/4\le S\le3.
\end{cases}
\]
This envelope is attained for every \(S\). For \(0<S<3/4\), equality holds exactly when
\[
|\rho_{12}|=|\rho_{13}|=|\rho_{23}|=\sqrt{S/3}
\quad\text{and}\quad
\rho_{12}\rho_{13}\rho_{23}<0.
\]
For \(3/4<S\le3\), equality holds exactly when the correlation matrix is singular. At \(S=3/4\), the two descriptions coincide: the three correlations have absolute value \(1/2\), their product is negative, and the correlation matrix has determinant zero.

A scale-free consequence is the sharp global stability inequality
\[
\mathbb E[X_1^2X_2^2X_3^2]-1\ge
\frac23\left(\rho_{12}^2+\rho_{13}^2+\rho_{23}^2\right).
\]
Besides independence, equality occurs exactly at the sign-equivalent singular pattern with all three correlation magnitudes equal to \(1/2\) and negative correlation product.

## Assumptions and scope
The variables are centered jointly Gaussian with positive unit marginal variances; singular joint laws are allowed. The normalization to unit variances is without loss for a product-moment ratio, but the displayed deficit itself is stated only in this normalized form. The quantity \(S\) measures the total squared pairwise correlation and ranges from \(0\) to \(3\).

The result concerns the exponent-two case of the three-dimensional Gaussian product inequality. It does not give an exact quantitative envelope for arbitrary positive or even exponents, nor does it claim a higher-dimensional analogue.

## Proof
Set
\[
a=\rho_{12},\qquad b=\rho_{13},\qquad c=\rho_{23},\qquad P=abc.
\]
Wick's formula gives the exact sixth mixed moment
\[
\mathbb E[X_1^2X_2^2X_3^2]
=1+2(a^2+b^2+c^2)+8abc,
\]
so
\[
\Delta=2S+8P.
\]
Thus the fixed-\(S\) problem is exactly the problem of minimizing \(P\).

The correlation matrix
\[
R=\begin{pmatrix}1&a&b\\a&1&c\\b&c&1\end{pmatrix}
\]
is positive semidefinite. Its determinant therefore satisfies
\[
0\le\det R=1+2P-S,
\]
which gives
\[
P\ge\frac{S-1}{2}.
\]
Independently, arithmetic-geometric mean applied to \(a^2,b^2,c^2\) gives
\[
|P|=|abc|\le\left(\frac S3\right)^{3/2},
\]
and hence
\[
P\ge-\left(\frac S3\right)^{3/2}.
\]
Therefore
\[
P\ge\max\left\{-\left(\frac S3\right)^{3/2},\frac{S-1}{2}\right\}.
\]
The two lower bounds meet exactly at \(S=3/4\). Indeed, putting \(t=\sqrt{S/3}\), equality of the two bounds becomes
\[
2t^3+3t^2-1=(t+1)^2(2t-1)=0,
\]
so the only nonnegative solution is \(t=1/2\).

For \(0\le S\le3/4\), take
\[
a=b=t,\qquad c=-t,\qquad t=\sqrt{S/3}\le\frac12.
\]
Then
\[
\det R=1-3t^2-2t^3=(1+t)^2(1-2t)\ge0,
\]
so this is a valid correlation matrix, and it attains \(P=-(S/3)^{3/2}\). Conversely, away from \(S=0\), equality in the arithmetic-geometric mean bound forces \(|a|=|b|=|c|=\sqrt{S/3}\), and minimizing \(P\) forces the product to be negative. This proves both the first branch and its equality classification.

For \(3/4\le S\le3\), determinant zero is necessary and sufficient for equality in the determinant bound. Every value of \(S\) in this interval is realized by a singular correlation matrix: take \(t\in[1/2,1]\) and
\[
a=b=t,\qquad c=2t^2-1.
\]
These are Gram correlations of three unit vectors with the second and third symmetrically placed about the first, so the matrix is positive semidefinite and singular. Moreover
\[
S=2t^2+(2t^2-1)^2=4t^4-2t^2+1,
\]
which increases continuously from \(3/4\) to \(3\) on \([1/2,1]\). Hence every \(S\) in the second branch is attained. Substituting the two sharp bounds for \(P\) into \(\Delta=2S+8P\) gives the claimed piecewise envelope.

Finally, on the first branch,
\[
\frac{\Delta_{\min}(S)}S=2-\frac{8}{3\sqrt3}\sqrt S
\]
decreases to \(2/3\), while on the second branch
\[
\frac{\Delta_{\min}(S)}S=6-\frac4S
\]
increases from \(2/3\). This proves the sharp global coefficient \(2/3\) and its equality cases.

## Verification
The proof is analytic and exhaustive. The bundled `verify.py` performs three supplemental checks: it verifies the two explicit extremal families, checks the sharp global linear inequality exactly on a rational grid of positive-semidefinite correlation triples, and numerically checks the piecewise envelope on the same grid. Replaying the packaged script returns `VERIFY_OK`.

Finite grid checks are not used to infer the theorem. The all-parameter proof is supplied by Wick's identity, positive semidefiniteness, arithmetic-geometric mean, and the two explicit sharpness constructions.

## Relationship to prior work
Lan, Hu, and Sun prove the qualitative three-dimensional Gaussian product inequality in a substantial class including equal even exponents, and record that the exponent-two case was already known. Their theorem gives nonnegativity of the deficit and equality only at independence, but it does not state a best lower bound at fixed total squared correlation.

Hu, Zhao, and Zhou develop quantitative two-dimensional Gaussian product inequalities. In their final remarks they explicitly ask for a quantitative version of the three-dimensional Gaussian product inequality and report only partial progress. The present result answers that question for the basic square-product case by determining the exact fixed-\(S\) envelope, not merely a positive lower bound.

Herry, Malicet, and Poly later prove the strong three-dimensional Gaussian product inequality for all triples of even positive integers. Their statement remains qualitative in the covariance parameters. Ouimet and Greaves subsequently prove the strong Gaussian product inequality for arbitrary positive exponents in every dimension and derive several further consequences; their inspected statement and consequences do not provide the exact fixed-\(S\) square-product envelope above.

## Limitations
Only the exponent-two three-dimensional product is classified quantitatively here. The piecewise formula uses the scalar summary \(S\); it does not solve optimization under a fully prescribed correlation pattern, nor does it extend the exact envelope to higher exponents or dimensions. The 2026 all-exponent theorem dominates the qualitative nonnegativity statement but does not by itself imply this sharp dependence-sensitive envelope.

A residual literature risk remains that the elementary fixed-\(S\) optimization has appeared under covariance-matrix or hafnian terminology without being indexed as a quantitative Gaussian product inequality. Targeted searches for the exact moment formula, the coefficient \(2/3\), the determinant reduction, and the fixed total squared-correlation problem did not locate such a statement.

## References
1. G. Lan, Z.-C. Hu, and W. Sun, “The Three-Dimensional Gaussian Product Inequality,” arXiv:1905.04279, first public version 10 May 2019; *Journal of Mathematical Analysis and Applications* 485 (2020), 123858.
2. Z.-C. Hu, H. Zhao, and Q.-Q. Zhou, “Quantitative Versions of the Two-dimensional Gaussian Product Inequalities,” arXiv:2207.09921, first public version 20 July 2022; *Journal of Inequalities and Applications* 2023, article 2.
3. R. Herry, D. Malicet, and G. Poly, “A short proof of the strong three dimensional Gaussian product inequality,” arXiv:2211.07314, first public version 14 November 2022; *Proceedings of the American Mathematical Society* 152 (2024), 403–409.
4. F. Ouimet and D. Greaves, “A proof of the strong Gaussian product inequality conjecture,” arXiv:2609.20234, first public version 27 July 2026.

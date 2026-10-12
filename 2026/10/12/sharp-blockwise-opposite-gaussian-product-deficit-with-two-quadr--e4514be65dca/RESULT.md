# Sharp blockwise opposite Gaussian product deficit with two quadratic factors
## Finding
Let \((X_1,X_2,X_3)\) be a centered real Gaussian vector with unit marginal variances and correlation coefficients
\[
a=\operatorname{Corr}(X_1,X_2),\quad
b=\operatorname{Corr}(X_1,X_3),\quad
c=\operatorname{Corr}(X_2,X_3).
\]
A singular joint covariance is allowed. Fix \(0<s<1\), and put
\[
M_s=\mathbb E|Z|^{-s}=
\frac{2^{-s/2}\Gamma((1-s)/2)}{\sqrt\pi},
\]
where \(Z\) is standard normal. Then
\[
\boxed{
\frac{\mathbb E[|X_1|^{-s}X_2^2X_3^2]}{M_s}
-\mathbb E[X_2^2X_3^2]
=-s\bigl[a^2+b^2+4abc-(2+s)a^2b^2\bigr].
}
\tag{1}
\]
In particular, the blockwise opposite Gaussian product inequality
\[
\mathbb E[|X_1|^{-s}X_2^2X_3^2]
\le M_s\,\mathbb E[X_2^2X_3^2]
\tag{2}
\]
holds **exactly** when
\[
a^2+b^2+4abc-(2+s)a^2b^2\ge0.
\tag{3}
\]
There is also a sharp uniform bound on violations of (2):
\[
\boxed{
\frac{\mathbb E[|X_1|^{-s}X_2^2X_3^2]}{M_s}
-\mathbb E[X_2^2X_3^2]
\le\frac{s}{6-s}.
}
\tag{4}
\]
For every \(s\in(0,1)\), the constant in (4) is attained. All equality matrices, and no others, satisfy
\[
a^2=b^2=\frac1{6-s},\qquad
c=\operatorname{sgn}(ab)\left(\frac2{6-s}-1\right).
\tag{5}
\]
They have determinant zero and rank two. For strictly positive-definite matrices, the same constant is optimal but is only approached at the boundary.

At \(s=1/2\), the exact singular witness
\[
a=b=\sqrt{\frac2{11}},\qquad c=-\frac7{11}
\]
produces the maximal difference \(\Delta_{1/2}=1/11\).

## Assumptions and scope
The correlations form a positive-semidefinite \(3\times3\) matrix with diagonal entries one. No sign restrictions are imposed. The range \(0<s<1\) is exactly the integrability range of the negative one-dimensional Gaussian moment. Degeneracy of the joint Gaussian law does not interfere with integrability because conditioning on the first coordinate yields a polynomial conditional moment.

The comparator in (2) is the **joint** second-and-third-coordinate moment, not the product of their two separate moments. This is the natural comparison between a negative-power block and an arbitrarily dependent positive-power block. Indeed
\[
\mathbb E[X_2^2X_3^2]=1+2c^2.
\]
The naive fully factorized three-factor bound is already false when the first coordinate is independent of a correlated pair; it is not the claim under study.

## Proof
The conditional law of the second and third coordinates given \(X_1=x\) has means \(ax\) and \(bx\), variances \(v_2=1-a^2\) and \(v_3=1-b^2\), and covariance \(r=c-ab\). Isserlis' fourth-moment formula therefore gives the exact conditional polynomial
\[
\begin{aligned}
\mathbb E[X_2^2X_3^2\mid X_1=x]
={}&v_2v_3+2r^2\\
&+(a^2v_3+b^2v_2+4abr)x^2
+a^2b^2x^4.
\end{aligned}
\tag{6}
\]
This remains valid for singular residual covariance matrices by continuity, or directly by Gaussian Wick expansion.

For a standard Gaussian \(Z\), gamma-function recurrence gives
\[
\frac{\mathbb E|Z|^{2-s}}{M_s}=1-s,
\qquad
\frac{\mathbb E|Z|^{4-s}}{M_s}=(1-s)(3-s).
\tag{7}
\]
Multiply (6) by \(|X_1|^{-s}\), integrate over \(X_1\), and use (7). After collecting the coefficients and subtracting
\[
\mathbb E[X_2^2X_3^2]=1+2c^2,
\]
one obtains (1). Since \(s>0\), equation (3) is exactly the sign criterion for (2).

To optimize (1), define
\[
F=a^2+b^2+4abc-(2+s)a^2b^2.
\]
If \(ab=0\), then \(F=a^2+b^2\ge0\). Otherwise put
\[
u=|a|,\quad v=|b|,\quad
w=\operatorname{sgn}(ab)c,\quad q=uv.
\]
The correlation matrix is positive semidefinite precisely when \(u,v\in[0,1]\) and
\[
uv-\sqrt{(1-u^2)(1-v^2)}
\le w\le
uv+\sqrt{(1-u^2)(1-v^2)}.
\tag{8}
\]
This is the usual determinant/Schur-complement constraint, valid also on the singular boundary. Since the coefficient of \(w\) in \(F\) is \(4q>0\), the smallest value for fixed \(u,v\) occurs at the lower endpoint of (8). Thus
\[
F\ge u^2+v^2+(2-s)q^2
-4q\sqrt{(1-u^2)(1-v^2)}.
\tag{9}
\]
By arithmetic-geometric mean,
\[
u^2+v^2\ge2uv=2q
\]
and
\[
\sqrt{(1-u^2)(1-v^2)}
\le1-q,
\]
because \((1-u^2)(1-v^2)=(1-q)^2-(u-v)^2\). Applying these two inequalities to (9) gives
\[
F\ge2q+(2-s)q^2-4q(1-q)
=-2q+(6-s)q^2.
\tag{10}
\]
Completing the square yields
\[
F\ge
(6-s)\left(q-\frac1{6-s}\right)^2
-\frac1{6-s}
\ge-\frac1{6-s}.
\tag{11}
\]
Multiplying by \(-s\) and using (1) proves (4).

Because \(s\in(0,1)\), the minimizing value \(q_*=1/(6-s)\) lies strictly in \((0,1)\). Equality in (11) forces \(q=q_*\); equality in both arithmetic-geometric-mean inequalities forces \(u=v=\sqrt{q_*}\), and equality in (9) forces \(w=2q_*-1\). These are exactly (5). The determinant vanishes by (8); since \(q_*<1\), the matrix has rank two, not one. Conversely, (5) defines a positive-semidefinite rank-two correlation matrix and makes every inequality above an equality. This proves sharpness and classifies all extremizers.

For any such extremizer \(R_*\), the matrices \((1-\varepsilon)R_*+\varepsilon I_3\) are positive definite for \(0<\varepsilon<1\); continuity of the polynomial in (1) shows that they approach the same optimal bound. The stated strict positive-definite sharpness follows.

## Verification
The standalone `verify.py` implements the conditional fourth-moment polynomial (6), the negative Gaussian moment ratios (7), and the exact difference (1) using rational arithmetic at deterministic test cases. It verifies the singular extremizers algebraically for several rational exponent values, including the witness with \(s=1/2\), \(a^2=b^2=2/11\), and \(c=-7/11\).

A separate deterministic set of positive-definite correlation matrices is checked numerically for the bound in (4) and the defining algebraic identity. This grid is a diagnostic replay only; the proof for every admissible matrix is (8)–(11).

Run with `python3 verify.py`. The successful completion line begins `VERIFY_OK exact_extremizers=3`.

## Relationship to prior work
Russell and Sun established the opposite Gaussian product inequality for **two** coordinates when one exponent is in \((-1,0)\) and the other is positive. Their theorem does not classify a negative-power coordinate against the *joint square product* of two correlated positive coordinates.

Zhou, Zhao, Hu, and Song subsequently proved mixed-sign results in higher dimensions. Their Theorem 1.1 gives a covariance-adjusted **lower** estimate for a negative Gaussian power multiplied by positive coordinate squares; their Proposition 1.6 gives a coarse multiplicative **upper** estimate relative to the three separate marginal moments. Neither provides the signed exact difference (1), the blockwise sign criterion (3), or the globally optimal additive groupwise constant (4).

Lan, Ouimet, and Sun further extended mixed-sign lower estimates and proved an upper inequality against convex functions of the positive-coordinate block. The joint factor \((x_2,x_3)\mapsto x_2^2x_3^2\) is **not convex**: its Hessian has negative determinant whenever \(x_2x_3\ne0\). Their convex-order theorem does not cover (2), and their separate product corollary has a different, coarser right-hand side.

The signed blockwise deviation is intrinsically different from a raw mixed moment because its comparator \(M_s\mathbb E[X_2^2X_3^2]\) changes with the positive-block correlation. Accordingly, the bound (4) is proved by optimizing the *difference* over the full correlation elliptope rather than by optimizing either moment separately.

## Limitations
The theorem handles the first nontrivial ternary case with one negative fractional exponent and two quadratic positive factors. It does not determine sharp groupwise deviations for arbitrary mixed exponents, dimensions, or positive-side polynomials.

The proof and global constant depend on exact fourth-order Gaussian regression; non-Gaussian vectors need not obey the same identity. Possible prior presentation of an equivalent polynomial optimization under a different moment-inequality or correlation-elliptope terminology remains a bibliographic risk.

## References
1. O. Russell and W. Sun, “An Opposite Gaussian Product Inequality,” arXiv:2205.10231v1, submitted 20 May 2022; *Statistics & Probability Letters* 191 (2022), 109656. DOI: 10.1016/j.spl.2022.109656.
2. Q.-Q. Zhou, H. Zhao, Z.-C. Hu, and R. Song, “Some New Results on Gaussian Product Inequalities,” arXiv:2308.13740v1, submitted 26 August 2023; *Journal of Mathematical Analysis and Applications*, DOI: 10.1016/j.jmaa.2023.127907.
3. G. Lan, F. Ouimet, and W. Sun, “Results related to the Gaussian product inequality conjecture for mixed-sign exponents in arbitrary dimension,” arXiv:2505.09976v3, 2026 revision.

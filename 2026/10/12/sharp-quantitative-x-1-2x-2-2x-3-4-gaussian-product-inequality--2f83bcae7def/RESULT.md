# Sharp quantitative \(X_1^2X_2^2X_3^4\) Gaussian product inequality
## Finding
Let
\[
(X_1,X_2,X_3)
\]
be a centered jointly Gaussian vector with
\[
\mathbb E[X_i^2]=1
\qquad(i=1,2,3).
\]
Put
\[
a=\operatorname{Corr}(X_1,X_2),\qquad
b=\operatorname{Corr}(X_1,X_3),\qquad
c=\operatorname{Corr}(X_2,X_3).
\]
Then
\[
\mathbb E[X_1^2X_2^2X_3^4]-3
\ge
C_*
\left(6a^2+12b^2+12c^2\right),
\tag{1}
\]
where
\[
C_*=\frac{7-\sqrt{41}}2
=
0.298437881283575\ldots .
\tag{2}
\]
The constant \(C_*\) is optimal.

If singular Gaussian vectors are admitted, the nonzero equality cases in (1) are exactly the correlation matrices satisfying
\[
abc<0,
\]
\[
|b|=|c|
=
\sqrt{\frac{\sqrt{41}-5}{8}},
\]
and
\[
|a|
=
\frac{9-\sqrt{41}}4.
\tag{3}
\]
These matrices have determinant zero. Independence is the only equality case with
\[
a=b=c=0.
\]
If positive definiteness of the joint covariance is imposed, (1) remains sharp, but the nonzero equality matrices in (3) are approached only as boundary limits.

Equation (1) is a sharp quantitative strengthening of the three-dimensional Gaussian product inequality in the first unequal-exponent case
\[
(m_2,m_3)=(1,2).
\]

## Assumptions and scope
The vector is centered and each coordinate has variance one. Joint singularity is allowed in the equality classification; restricting to positive-definite correlation matrices leaves the sharp constant unchanged.

The right-hand side in (1) is the natural quadratic correlation scale supplied by the second-order terms of the exact Gaussian moment polynomial. The result does not claim the analogous sharp constant for arbitrary exponents.

By rescaling coordinates, (1) immediately yields the corresponding homogeneous statement for arbitrary positive marginal variances.

## Proof
Isserlis' formula gives the exact moment identity
\[
\mathbb E[X_1^2X_2^2X_3^4]
=
3
+
6a^2
+
12b^2
+
12c^2
+
48abc
+
24b^2c^2.
\tag{4}
\]
Define
\[
D=
\mathbb E[X_1^2X_2^2X_3^4]-3
\]
and
\[
Q=6a^2+12b^2+12c^2.
\]
We must minimize
\[
R=\frac DQ
\]
over nonzero feasible correlation triples.

If
\[
abc\ge0,
\]
then by (4),
\[
D-Q=48abc+24b^2c^2\ge0,
\]
so
\[
R\ge1>C_*.
\]

It remains to consider
\[
abc<0.
\]
Set
\[
x=|a|,\qquad y=|b|,\qquad z=|c|,
\]
and define
\[
s=y^2+z^2,\qquad t=yz.
\]
Positive semidefiniteness of the correlation matrix is equivalent to
\[
x^2+s+2xt\le1.
\tag{5}
\]
From (4),
\[
R
=
1-
\frac{4t(2x-t)}{x^2+2s}.
\tag{6}
\]

When
\[
t\ge2x,
\]
the correction in (6) is nonpositive and hence
\[
R\ge1.
\]
Assume therefore that
\[
t<2x.
\]
For fixed \(x,t\), the subtracted term in (6) is largest when \(s\) is smallest. By arithmetic-geometric mean,
\[
s\ge2t,
\]
with equality exactly when
\[
y=z=\sqrt t.
\]
Replacing \(s\) by \(2t\) preserves feasibility in (5). Thus every minimizer may be taken with
\[
y=z=\sqrt u,
\qquad
u=t.
\]

The positive-semidefinite constraint becomes
\[
x^2+2u+2xu\le1,
\]
or equivalently
\[
0\le u\le\frac12,
\qquad
0\le x\le1-2u.
\tag{7}
\]
The ratio reduces to
\[
R_u(x)
=
\frac{x^2+4u-8xu+4u^2}{x^2+4u}
=
1-4u\,\frac{2x-u}{x^2+4u}.
\tag{8}
\]
For fixed \(u>0\), put
\[
F_u(x)=\frac{2x-u}{x^2+4u}.
\]
Its derivative has the sign of
\[
-x^2+ux+4u.
\tag{9}
\]
The positive critical point reaches the boundary
\[
x=1-2u
\]
when
\[
6u^2-9u+1=0.
\]
Write
\[
u_c=\frac{9-\sqrt{57}}{12}.
\]

For
\[
0<u\le u_c,
\]
the maximum of \(F_u\) is attained at its interior critical point. There
\[
x^2=u(x+4),
\]
and substitution into (8) gives
\[
R_u(x)=\frac{4-3x}{x+4},
\]
which decreases as the critical point \(x\) increases. Hence this branch decreases down to its value at \(u_c\).

For
\[
u_c\le u\le\frac12,
\]
the maximum of \(F_u\) is attained at the positive-semidefinite boundary
\[
x=1-2u.
\]
Consequently
\[
R_u(1-2u)
=
\frac{24u^2-8u+1}{4u^2+1}.
\tag{10}
\]
Differentiating (10) gives
\[
\frac{d}{du}R_u(1-2u)
=
\frac{8(4u^2+5u-1)}{(4u^2+1)^2}.
\tag{11}
\]
The unique critical point in
\[
(0,1/2)
\]
is
\[
u_*=\frac{\sqrt{41}-5}{8}.
\tag{12}
\]
One has
\[
u_c<u_*<\frac12.
\]
The boundary branch decreases from \(u_c\) to \(u_*\) and increases afterwards, while the interior branch already decreases to the shared value at \(u_c\). Therefore the global minimum is attained at \(u_*\).

Substituting (12) into (10) yields
\[
\min R
=
\frac{7-\sqrt{41}}2
=
C_*.
\]
At the minimum,
\[
x_*=1-2u_*
=
\frac{9-\sqrt{41}}4.
\]
Tracing equality through the reduction gives exactly
\[
y=z=\sqrt{u_*},
\qquad
x=x_*,
\qquad
abc<0,
\]
and equality in the determinant constraint (5). This proves (1), sharpness, and the stated equality classification.

## Verification
The standalone script `verify.py` performs three independent checks.

First, it enumerates all \(105\) Isserlis pairings for
\[
X_1^2X_2^2X_3^4
\]
and recovers exactly the six monomials and coefficients in (4).

Second, it substitutes the radical extremizer into the determinant, the moment deficit, and the quadratic scale and verifies numerically that
\[
D/Q=C_*.
\]

Third, a deterministic grid over the negative-sign positive-semidefinite region checks that all sampled ratios stay above the sharp constant and approach it near the analytic extremizer.

A successful run ends with a line beginning
`VERIFY_OK constant=0.298437881284`.

The finite grid is not used as proof. Sharpness and the global minimum are established analytically in the preceding section.

## Relationship to prior work
Hu, Zhao, and Zhou develop quantitative two-dimensional Gaussian product inequalities and explicitly ask for quantitative versions of the three-dimensional inequalities. Their question includes
\[
\mathbb E[X_1^2X_2^{2m_2}X_3^{2m_3}]
\ge
\mathbb E[X_1^2]\mathbb E[X_2^{2m_2}]\mathbb E[X_3^{2m_3}].
\]
Their results are bivariate and do not supply a three-dimensional quantitative constant.

Russell and Sun prove the qualitative three-dimensional inequality above for every positive integer pair
\[
(m_2,m_3).
\]
Their full argument establishes nonnegativity and equality only at independence, but the inspected manuscript does not state the correlation-weighted sharp bound (1). It explicitly notes that the low cases with
\[
m_2=1
\]
can also be handled by earlier qualitative methods.

Later work extends qualitative three-dimensional Gaussian product inequalities to broader positive-integer exponent ranges. The inspected bibliographic material for that work likewise states qualitative nonnegativity and equality characterization, not a sharp quantitative correlation constant.

Targeted searches using the exact moment
\[
\mathbb E[X_1^2X_2^2X_3^4],
\]
the coefficient
\[
(7-\sqrt{41})/2,
\]
the weighted quadratic correlation form, and the parameter pair
\[
(m_2,m_3)=(1,2)
\]
did not locate a published statement implying (1).

## Limitations
The theorem treats one specific but natural first unequal-exponent three-dimensional case. It does not provide a formula for general
\[
(m_2,m_3).
\]

The quantitative normalization is the exact quadratic part of the moment deficit. Other quantitative formulations may lead to different sharp constants.

An equivalent optimization may exist in earlier Gaussian-moment or polynomial-positivity literature under different terminology; this is the principal residual bibliographic risk.

## References
1. Z.-C. Hu, H. Zhao, and Q.-Q. Zhou, “Quantitative Versions of the Two-dimensional Gaussian Product Inequalities,” arXiv:2207.09921v1, 20 July 2022; *Journal of Inequalities and Applications* 2023, article 2. DOI: 10.1186/s13660-022-02906-w.
2. O. Russell and W. Sun, “Moment ratio inequality of bivariate Gaussian distribution and three-dimensional Gaussian product inequality,” arXiv:2208.13957, 30 August 2022; *Journal of Mathematical Analysis and Applications* 523 (2023), 127410. DOI: 10.1016/j.jmaa.2023.127410.
3. B. Kim, J. Kim, and J. Kim, “Three-dimensional Gaussian product inequality with positive integer order moments,” *Journal of Mathematical Analysis and Applications* 542 (2025), 128804. DOI: 10.1016/j.jmaa.2024.128804.

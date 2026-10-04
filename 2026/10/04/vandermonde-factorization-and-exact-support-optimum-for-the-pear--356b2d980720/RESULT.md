# Vandermonde factorization and exact support optimum for the Pearson skewness–kurtosis gap

## Finding

Let \(X\) take exactly three distinct ordered values
\[
x_1<x_2<x_3
\]
with positive probabilities
\[
\Pr(X=x_1)=a,\qquad
\Pr(X=x_2)=b,\qquad
\Pr(X=x_3)=c,
\qquad
a+b+c=1.
\]
Write
\[
\mu=\mathbb EX,\qquad
\sigma^2=\operatorname{Var}(X)>0,
\]
and define skewness and kurtosis by
\[
\gamma=
\frac{\mathbb E[(X-\mu)^3]}{\sigma^3},
\qquad
\kappa=
\frac{\mathbb E[(X-\mu)^4]}{\sigma^4}.
\]

Then the excess above Pearson's universal boundary factors exactly as
\[
\boxed{
\kappa-\gamma^2-1
=
\frac{
abc\,
(x_2-x_1)^2
(x_3-x_1)^2
(x_3-x_2)^2
}{
\sigma^6
}.
}
\tag{1}
\]

In particular, every genuine three-point law satisfies
\[
\kappa>\gamma^2+1,
\]
and the Pearson boundary is approached precisely when two support points coalesce.

For fixed masses \(a,b,c\), let
\[
r=
\frac{x_2-x_1}{x_3-x_2}>0.
\]
Positive affine invariance lets us represent the support by
\[
(0,r,1+r).
\]
Its variance is
\[
V(r)=ab\,r^2+ac(1+r)^2+bc,
\tag{2}
\]
so (1) becomes
\[
G(r)
:=
\kappa-\gamma^2-1
=
\frac{abc\,r^2(1+r)^2}{V(r)^3}.
\tag{3}
\]

The function \(G\) has exactly one critical point on \((0,\infty)\), and that point is its global maximum. More precisely, let \(r_*>0\) be the unique positive root of
\[
\boxed{
a(b+c)r^3
+
a(2b+c)r^2
-
c(a+2b)r
-
c(a+b)
=0.
}
\tag{4}
\]
Then
\[
\boxed{
\kappa-\gamma^2
\in
\left(
1,\,
1+G(r_*)
\right].
}
\tag{5}
\]
The upper endpoint is attained exactly at the unique support shape with adjacent-gap ratio \(r_*\), up to location and positive scale.

The lower endpoint is not attained by three distinct support points. The approach is quadratic:
\[
G(r)
\sim
\frac{ab}{c^2(a+b)^3}\,r^2
\qquad(r\downarrow0),
\tag{6}
\]
and
\[
G(r)
\sim
\frac{bc}{a^2(b+c)^3}\,\frac1{r^2}
\qquad(r\to\infty).
\tag{7}
\]

For equal masses
\[
a=b=c=\frac13,
\]
equation (4) has the unique positive solution
\[
r_*=1.
\]
Consequently
\[
\boxed{
1<\kappa-\gamma^2\le\frac32,
}
\tag{8}
\]
with equality at \(3/2\) exactly for a uniform law on a three-point arithmetic progression.

## Assumptions and scope

The theorem concerns exactly three distinct real support points with positive fixed masses.

The quantity optimized is the Pearson gap
\[
\kappa-\gamma^2-1,
\]
not kurtosis alone. Fixing the masses is essential for the unique support-shape statement.

The support may be translated and multiplied by any positive constant without changing the result.

The boundary value zero in (1) belongs to the closure of the three-point class, where the law becomes effectively two-point.

## Proof

Define the standardized variable
\[
Y=\frac{X-\mu}{\sigma}.
\]
Then
\[
\mathbb EY=0,\qquad
\mathbb EY^2=1,\qquad
\mathbb EY^3=\gamma,\qquad
\mathbb EY^4=\kappa.
\]
Consider the Gram matrix of the functions \(1,Y,Y^2\):
\[
M
=
\mathbb E
\begin{bmatrix}
1\\Y\\Y^2
\end{bmatrix}
\begin{bmatrix}
1&Y&Y^2
\end{bmatrix}
=
\begin{bmatrix}
1&0&1\\
0&1&\gamma\\
1&\gamma&\kappa
\end{bmatrix}.
\]
Direct expansion gives
\[
\det M=\kappa-\gamma^2-1.
\tag{9}
\]

Let
\[
y_i=\frac{x_i-\mu}{\sigma}.
\]
With
\[
W=
\begin{bmatrix}
1&y_1&y_1^2\\
1&y_2&y_2^2\\
1&y_3&y_3^2
\end{bmatrix},
\qquad
D=\operatorname{diag}(a,b,c),
\]
we also have
\[
M=W^{\mathsf T}DW.
\]
Therefore
\[
\det M
=
abc\,(\det W)^2.
\tag{10}
\]
The Vandermonde determinant is
\[
\det W
=
(y_2-y_1)(y_3-y_1)(y_3-y_2),
\]
and
\[
y_j-y_i=\frac{x_j-x_i}{\sigma}.
\]
Substitution into (9)--(10) proves (1).

Now put the support at
\[
0,\quad r,\quad 1+r.
\]
The standard pairwise variance identity gives
\[
\sigma^2
=
ab\,r^2+ac(1+r)^2+bc
=
V(r),
\]
which proves (3).

Differentiating (3) and collecting positive factors gives
\[
G'(r)
=
-
\frac{
2abc\,r(1+r)
}{
V(r)^4
}
P(r),
\tag{11}
\]
where
\[
P(r)
=
a(b+c)r^3
+
a(2b+c)r^2
-
c(a+2b)r
-
c(a+b).
\tag{12}
\]
The coefficient signs in descending powers are
\[
+,\ +,\ -,\ -.
\]
Hence Descartes' rule of signs gives at most one positive zero. Since
\[
P(0)=-c(a+b)<0
\]
and
\[
P(r)\to+\infty
\qquad(r\to\infty),
\]
there is exactly one positive zero \(r_*\).

Equation (11) shows that \(G\) increases before \(r_*\) and decreases after \(r_*\). Also
\[
G(r)\to0
\]
at both endpoints \(r\downarrow0\) and \(r\to\infty\). Thus \(r_*\) is the unique global maximizer and (5) follows by continuity.

Expanding (3) at the two endpoints gives (6)--(7).

For
\[
a=b=c=\frac13,
\]
equation (12), after multiplication by \(9\), is
\[
2r^3+3r^2-3r-2
=
(r-1)(2r^2+5r+2).
\]
Thus \(r_*=1\). At \(r=1\),
\[
V(1)=\frac23,
\]
for the support \((0,1,2)\), while the numerator in (3) is
\[
\frac4{27}.
\]
Therefore
\[
G(1)=\frac12,
\]
which proves (8).

## Verification

The accompanying exact-rational checker evaluates central moments for thousands of rational three-point laws and verifies identity (1) without floating-point arithmetic.

It independently verifies the normalized formula (3), the derivative-sign polynomial (12), the equal-mass factorization, and the predicted monotonicity around the unique positive critical point.

The computation is supplementary. The universal identity follows from the Gram determinant and Vandermonde determinant, and uniqueness of the support optimum follows from the derivative factorization.

## Relationship to prior work

Pearson's classical inequality
\[
\kappa\ge\gamma^2+1
\]
is a universal moment constraint, with equality at two-point laws. Hürlimann's probability-and-statistics article reviews this inequality explicitly, notes its sharp biatomic equality case, and places it among skewness--kurtosis feasibility bounds.

Klaassen and van Es study the parameter
\[
\kappa-\gamma^2
\]
directly and describe the complete skewness--kurtosis set for arbitrary distributions. Their constructive proof uses a three-valued family to realize every point above the Pearson parabola. The probabilities in that family vary with the target moment pair; it does not give the fixed-mass Vandermonde factorization or optimize support geometry for prescribed \(a,b,c\).

Rohatgi and Székely give sharp skewness--kurtosis inequalities for several distribution classes. The accessible abstract and bibliographic record concern class-wide inequalities rather than a fixed three-atom probability profile.

The present result identifies the exact positive determinant separating a genuine three-point law from the Pearson boundary, and then solves the complete fixed-mass support-shape optimization of that determinant.

Targeted searches for three-point Pearson gaps, Vandermonde moment determinants, fixed probability profiles, and kurtosis-minus-squared-skewness formulas did not locate (1), (4), or the range (5).

## Limitations

The exact factorization and one-parameter support optimization are specific to three support points. With four or more points, the \(3\times3\) moment Gram determinant is a sum of squared Vandermonde minors rather than a single product.

The fixed-mass maximum is given through the unique positive root of a cubic; no simpler closed form is asserted in general.

The originality assessment is targeted. Older moment-problem or Gram-determinant literature may contain the identity in an equivalent algebraic form.

The full 1989 Rohatgi--Székely article was not openly available through the routes checked; its abstract was used only for scope comparison and remains a residual source risk.

## References

1. W. Hürlimann, “Normal variance-mean mixtures (I) an inequality between skewness and kurtosis,” *Advances in Inequalities and Applications* 2014, Article 2, first published 2013-10-16.
2. C. A. J. Klaassen and B. van Es, “Inference via the Skewness-Kurtosis Set,” *International Statistical Review* (2025), DOI 10.1111/insr.70007.
3. V. K. Rohatgi and G. J. Székely, “Sharp inequalities between skewness and kurtosis,” *Statistics & Probability Letters* 8 (1989), 297–299, DOI 10.1016/0167-7152(89)90035-7.
4. K. Pearson, “Mathematical contributions to the theory of evolution, XIX: Second supplement to a memoir on skew variation,” *Philosophical Transactions of the Royal Society A* 216 (1916), 429–457.

# Endpoint curvature law for heterogeneous exponential parallel systems
## Finding
Let
\[
X=\max(X_1,X_2),\qquad Y=\max(Y_1,Y_2),
\]
where \(X_i\sim\operatorname{Exp}(\lambda_i)\) and \(Y_i\sim\operatorname{Exp}(\theta_i)\) are independent. Assume
\[
0<\theta_1<\lambda_1<\lambda_2<\theta_2,
\qquad
\lambda_1+\lambda_2=\theta_1+\theta_2.
\]
This is the strict two-component majorization regime of the motivating convex-transform comparison.

Write \(F_X,F_Y\) for the maximum cdfs and define
\[
Q(x)=F_Y^{-1}(F_X(x)).
\]
Put
\[
S=\lambda_1+\lambda_2,
\quad
A=\sqrt{\frac{\lambda_1\lambda_2}{\theta_1\theta_2}},
\quad
c=\frac{\lambda_1}{\theta_1},
\quad
\alpha=\lambda_2-\lambda_1.
\]
Then
\[
Q(x)=Ax+\frac{S}{4}A(A-1)x^2+O(x^3)
\qquad(x\downarrow0),
\tag{1}
\]
and therefore
\[
Q''(0+)=\frac S2A(A-1)>0.
\tag{2}
\]
At the other endpoint,
\[
Q(x)=cx-\frac1{\theta_1}e^{-\alpha x}+o(e^{-\alpha x}),
\tag{3}
\]
\[
Q'(x)=c+\frac{\alpha}{\theta_1}e^{-\alpha x}+o(e^{-\alpha x}),
\tag{4}
\]
\[
Q''(x)=-\frac{\alpha^2}{\theta_1}e^{-\alpha x}+o(e^{-\alpha x}).
\tag{5}
\]
Thus \(Q\) is strictly convex near zero and strictly concave for all sufficiently large \(x\). It approaches the straight line \(cx\) from below, while its slope approaches \(c\) from above. In particular, \(Q\) has at least one inflection point.

For the paper's numerical example
\[
(\lambda_1,\lambda_2)=(2,3),
\qquad
(\theta_1,\theta_2)=(3/2,7/2),
\]
the tail law becomes
\[
Q(x)=\frac43x-\frac23e^{-x}+o(e^{-x}),
\qquad
Q''(x)=-\frac23e^{-x}+o(e^{-x}).
\]
This explains analytically why the curvature is eventually negative despite being positive near the origin.

## Assumptions and scope
The result concerns exactly two independent exponential components in each parallel system, with strictly ordered hazards and equal hazard sums. The equal-sum condition is the strict two-dimensional majorization setting considered by the source.

The theorem does not claim that the inflection point is unique. It establishes the endpoint curvature signs, at least one curvature change, and the exact first tail correction. It does not extend the correction coefficient to the source's general two-type \(n\)-component model, where repeated slow-rate components introduce additional cancellation patterns.

## Proof
For two exponential components,
\[
F_X(x)=(1-e^{-\lambda_1x})(1-e^{-\lambda_2x}),
\qquad
F_Y(y)=(1-e^{-\theta_1y})(1-e^{-\theta_2y}).
\tag{6}
\]

At the origin, using the common sum \(S\),
\[
F_X(x)
=
\lambda_1\lambda_2x^2
-
\frac{S\lambda_1\lambda_2}{2}x^3
+O(x^4),
\]
and similarly
\[
F_Y(y)
=
\theta_1\theta_2y^2
-
\frac{S\theta_1\theta_2}{2}y^3
+O(y^4).
\]
Write
\[
Q(x)=Ax+Bx^2+O(x^3).
\]
Matching the quadratic terms in \(F_Y(Q(x))=F_X(x)\) gives
\[
A^2=\frac{\lambda_1\lambda_2}{\theta_1\theta_2}.
\]
Matching cubic terms then gives
\[
B=\frac S4A(A-1),
\]
which proves (1) and (2). Because the two positive numbers \(\lambda_1,\lambda_2\) have the same sum as \(\theta_1,\theta_2\) but are strictly less spread, their product is larger, so \(A>1\).

For the tail, the survival functions are
\[
\overline F_X(x)
=
e^{-\lambda_1x}
\left(1+e^{-\alpha x}-e^{-\lambda_2x}\right)
\tag{7}
\]
and
\[
\overline F_Y(y)
=
e^{-\theta_1y}
\left(1+e^{-(\theta_2-\theta_1)y}-e^{-\theta_2y}\right).
\tag{8}
\]
Set
\[
Q(x)=cx+\eta(x),
\qquad
c=\frac{\lambda_1}{\theta_1}.
\]
The source proves \(\eta(x)\to0\). Moreover,
\[
c(\theta_2-\theta_1)-\alpha
=
(\lambda_1+\lambda_2)
\left(\frac{\lambda_1}{\theta_1}-1\right)>0.
\tag{9}
\]
Hence every correction from the bracket in (8) is of smaller order than \(e^{-\alpha x}\). Dividing the identity \(\overline F_Y(Q(x))=\overline F_X(x)\) by \(e^{-\lambda_1x}\) gives
\[
e^{-\theta_1\eta(x)}
=
1+e^{-\alpha x}+o(e^{-\alpha x}).
\]
Taking logarithms proves (3).

To obtain the derivative expansions without differentiating an uncontrolled remainder, use the exact implicit identities
\[
F_Y(Q(x))=F_X(x),
\qquad
f_Y(Q(x))Q'(x)=f_X(x),
\tag{10}
\]
and
\[
f_Y'(Q(x))(Q'(x))^2+f_Y(Q(x))Q''(x)=f_X'(x).
\tag{11}
\]
The finite exponential formulas
\[
f_X(x)=\lambda_1e^{-\lambda_1x}+\lambda_2e^{-\lambda_2x}-Se^{-Sx}
\]
and its \(Y\)-analogue, together with (3) and (9), yield (4) from (10) and (5) from (11). Since the leading coefficients in (2) and (5) are strictly positive and strictly negative, respectively, continuity of \(Q''\) on \((0,\infty)\) gives the stated endpoint convexity and at least one inflection point.

## Verification
The standalone `verify.py` checks the source's numerical example. It computes \(Q\) by bisection from the exact cdfs, evaluates \(Q'\) and \(Q''\) from the exact implicit derivative formulas, and checks both endpoint asymptotic constants.

A successful run ends with
`VERIFY_OK tail_q=-0.666554373 tail_qp=0.666438679 tail_qpp=-0.666213879 local_qpp=0.184816890`.

The finite checks are not used to prove the asymptotic statements.

## Relationship to prior work
Arab, Hadjikyriakou, and Oliveira prove that the corresponding heterogeneous exponential parallel systems are not comparable in convex transform order. For the two-component case they state that the transform \(F_Y^{-1}(F_X(x))\) behaves almost like a straight line, note that an explicit inverse and simple derivative formulas appear out of reach, and report only numerical second derivatives for the example \((2,3)\) versus \((1.5,3.5)\). They later prove only the zeroth-order tail statement
\[
F_Y^{-1}(F_X(x))-\frac{\lambda_1}{\theta_1}x\to0.
\]
Equations (1)–(5) sharpen those observations by giving analytic curvature signs at both endpoints and the exact exponential rate and coefficient of approach to the tail asymptote.

The authors' later general paper on non-comparability in convex transform order develops broad criteria and lists the parallel-system work as an application. Its accessible abstract and indexed material do not state the endpoint correction above.

Targeted searches using convex-transform, heterogeneous-exponential-maxima, quantile-map, inflection, and second-order tail formulations did not locate the displayed endpoint laws.

## Limitations
At least one inflection point is proved, but uniqueness is not claimed. The asymptotic theorem is restricted to the strict two-component equal-sum regime.

Literature searches cannot exclude an equivalent endpoint expansion appearing under general quantile-transform or reliability asymptotics terminology, although the directly motivating full text and the closest follow-up were checked.

## References
1. I. Arab, M. Hadjikyriakou, and P. E. Oliveira, “On a conjecture about the comparability of parallel systems with respect to the convex transform order,” arXiv:1901.03238v1, 10 January 2019; *Probability and Mathematical Statistics* 41 (2021), 347–358, DOI: 10.37190/0208-4147.41.2.8.
2. I. Arab, M. Hadjikyriakou, and P. E. Oliveira, “Non-Comparability with respect to the convex transform order with applications,” *Journal of Applied Probability* 57 (2020), 1339–1348, DOI: 10.1017/jpr.2020.67.
